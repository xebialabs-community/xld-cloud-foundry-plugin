from cloudfoundry.util import CFClientUtil

cfClient = CFClientUtil.createClient(deployed.container)
print "Uploading ..."
cfClient.uploadApplication(deployed.name, deployed.file.file)
cfClient.logout()