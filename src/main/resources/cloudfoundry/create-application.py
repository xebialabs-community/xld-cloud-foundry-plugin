from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(deployed.container)
uris = []
if len(deployed.getProperty('contextRoot')) > 0:
	uris = ["%s.%s" % (deployed.getProperty('contextRoot'), deployed.container.getProperty('defaultDomain'))]

cfClient.createApplication(deployed.name, uris=uris)

cfClient.logout()