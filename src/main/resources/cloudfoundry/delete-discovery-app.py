#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil

sqlClient = deployed.container
space = sqlClient.getProperty("space")
cf_client = CFClientUtil.create_space_client(space)

app_name = "discovery-%s-%s" % (deployed.name, space.getProperty('spaceName'))

print "Delete discovery application"
cf_client.delete_application(app_name)