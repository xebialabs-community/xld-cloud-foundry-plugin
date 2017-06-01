#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from cloudfoundry.util import CFClientUtil
from java.io import File
import json
import urllib2
import time

sql_client = deployed.container
space = sql_client.getProperty("space")
cf_client = CFClientUtil.create_space_client(space)

app_name = "discovery-%s-%s" % (deployed.name, space.getProperty('spaceName'))
uris = ["%s.%s" % (app_name, space.getProperty("organization").getProperty('defaultDomain'))]


print "Creating discovery application"
cf_client.create_application(app_name, File('ext/cloudfoundry/discoveryapp').toPath())
print "Binding db service"
cf_client.bind_service(app_name, deployed.getProperty('cloudFoundryDbService'))

print "Mapping route"
cf_client.map_route(app_name, space.organization.defaultDomain, app_name, None, None, None)
print "Starting discovery application"
cf_client.start_application(app_name)

print "Fetch information from http://%s" % uris[0]

retryCount = 0
while retryCount < 20:
    req = urllib2.Request("http://%s" % uris[0])
    try:
        response = urllib2.urlopen(req)
        vcapServices = json.load(response)
        break
    except urllib2.HTTPError, e:
        print "failed to connect to discovery application. will retry in 5 secondes"
        time.sleep(5)
        retryCount += 1

if retryCount == 20:
    raise Exception("Could not access discovery application")

print "Find database credentials"
for vcapService in vcapServices.keys():
    for vcapServiceInstance in vcapServices[vcapService]:
        if "mysql" in vcapServiceInstance["tags"]:
            print "Found database creds"
            creds = vcapServiceInstance["credentials"]
            context.setAttribute("%s-username" % vcapServiceInstance["name"], creds["username"])
            context.setAttribute("%s-password" % vcapServiceInstance["name"], creds["password"])
            context.setAttribute("%s-host" % vcapServiceInstance["name"], creds["hostname"])
            context.setAttribute("%s-db" % vcapServiceInstance["name"], creds["name"])
