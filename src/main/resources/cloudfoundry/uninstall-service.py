from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(deployed.container)
cfClient.deleteService(deployed.getProperty("instanceName"))
cfClient.logout()