#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.create_space_client(deployed.container)

if not cfClient.stopApplication(deployed.name, deployed.retrialCount, deployed.waitTime):
    print "Application [%s] failed to stop." % deployed.name
    cfClient.logout()
    sys.exit(1)

cfClient.logout()