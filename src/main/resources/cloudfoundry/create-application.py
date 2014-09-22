#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(deployed.container)
uris = []
if len(deployed.getProperty('contextRoot')) > 0:
	uris = ["%s.%s" % (deployed.getProperty('contextRoot'), deployed.container.getProperty('defaultDomain'))]

cfClient.createApplication(deployed.name, uris=uris)

cfClient.logout()