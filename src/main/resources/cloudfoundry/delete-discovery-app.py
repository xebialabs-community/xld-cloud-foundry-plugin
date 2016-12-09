#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil

sqlClient = deployed.container
space = sqlClient.getProperty("space")
cfClient = CFClientUtil.create_space_client(space)

appName = "discovery-%s-%s" % (deployed.name, space.getProperty('spaceName'))

print "Delete discovery application"
cfClient.delete_application(appName)

cfClient.logout()
