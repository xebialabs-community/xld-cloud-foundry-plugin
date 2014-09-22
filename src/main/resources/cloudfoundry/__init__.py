def createClient(container, autologin=True):
	client = CFClient(container.getProperty("apiEndpoint"), container.getProperty("org"), container.getProperty("spaceName"), container.getProperty("username"), container.getProperty("password") )
	if autologin: client.login()
	return client