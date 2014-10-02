#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil

cfClient = CFClientUtil.createSpaceClient(deployed.container)

appName = "discovery-%s" % deployed.name

print "Delete discovery application"
cfClient.deleteApplication(appName)

cfClient.logout()