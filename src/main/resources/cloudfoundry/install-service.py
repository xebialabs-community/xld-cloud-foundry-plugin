from cloudfoundry.util import CFClientUtil

cfClient = CFClientUtil.createClient(deployed.container)
cfClient.createService(deployed.getProperty("instanceName"), deployed.getProperty("serviceLabel"), deployed.getProperty("servicePlan"))
cfClient.logout()