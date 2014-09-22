from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(deployed.container)

if not cfClient.startApplication(deployed.name):
    print "Application [%s] failed to start." % deployed.name
    cfClient.logout()
    sys.exit(1)

cfClient.logout()