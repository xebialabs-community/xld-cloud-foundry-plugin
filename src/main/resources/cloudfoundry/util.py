#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.client import CFClient


class CFClientUtil(object):

    @staticmethod
    def createSpaceClient(container, auto_login=True):
        organization = container.getProperty("organization")
        client = CFClient.createClient(organization.getProperty("apiEndpoint"), organization.getProperty("username"), organization.getProperty("password"), ssl=organization.getProperty("ignoreSsl"),
                                       org=organization.getProperty("organizationName"), space=container.getProperty("spaceName"))
        if auto_login: client.login()
        return client


    @staticmethod
    def createOrganizationClient(container, auto_login=True):
        client = CFClient.createClient(container.getProperty("apiEndpoint"), container.getProperty("username"), container.getProperty("password"), ssl=container.getProperty("ignoreSsl"))
        if auto_login: client.login()
        return client

