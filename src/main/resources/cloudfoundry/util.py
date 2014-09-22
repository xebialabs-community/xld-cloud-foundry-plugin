from cloudfoundry.client import CFClient


class CFClientUtil(object):

    @staticmethod
    def createClient(container, autologin=True):
        client = CFClient.createClient(container.getProperty("apiEndpoint"), container.getProperty("username"), container.getProperty("password"),
                                       org=container.getProperty("org"), space=container.getProperty("spaceName"))
        if autologin: client.login()
        return client


    @staticmethod
    def createClientWithoutOrgSpace(container, autologin=True):
        client = CFClient.createClient(container.getProperty("apiEndpoint"), container.getProperty("username"), container.getProperty("password"))
        if autologin: client.login()
        return client

