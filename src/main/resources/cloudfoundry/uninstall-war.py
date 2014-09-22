from cloudfoundry.util import CFClientUtil
import sys
from org.cloudfoundry.client.lib.domain import CloudEntity, CloudSpace, CloudService, CloudApplication, Staging

cfClient = CFClientUtil.createClient(deployed.container)

cfClient.deleteApplication(deployed.name)
cfClient.logout()