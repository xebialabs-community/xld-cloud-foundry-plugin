#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.create_space_client(deployed.container)

for binding in deployed.getProperty('bindings'):
	print "Binding service instance [%s]" % binding
	cfClient.bindService(deployed.name, binding)

cfClient.logout()
