#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys
from org.cloudfoundry.client.lib.domain import CloudEntity, CloudSpace, CloudService, CloudApplication, Staging

cfClient = CFClientUtil.createClient(deployed.container)

cfClient.deleteApplication(deployed.name)
cfClient.logout()