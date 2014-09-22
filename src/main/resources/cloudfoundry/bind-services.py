from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(deployed.container)

for binding in deployed.getProperty('bindings'):
	print "Binding service instance [%s]" % binding
	cfClient.bindService(deployed.name, binding)

cfClient.logout()
