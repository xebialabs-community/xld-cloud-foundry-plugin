from cloudfoundry.util import CFClientUtil

cfClient = CFClientUtil.createClient(deployed.container.getProperty('space'))

appName = "discovery-%s" % deployed.name

print "Delete discovery application"
cfClient.deleteApplication(appName)

cfClient.logout()