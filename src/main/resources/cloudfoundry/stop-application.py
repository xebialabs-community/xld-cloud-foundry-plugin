from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(deployed.container)

if not cfClient.stopApplication(deployed.name):
    print "Application [%s] failed to stop." % deployed.name
    cfClient.logout()
    sys.exit(1)

cfClient.logout()