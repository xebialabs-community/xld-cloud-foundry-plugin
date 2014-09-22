#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

def createClient(container, autologin=True):
	client = CFClient(container.getProperty("apiEndpoint"), container.getProperty("org"), container.getProperty("spaceName"), container.getProperty("username"), container.getProperty("password") )
	if autologin: client.login()
	return client