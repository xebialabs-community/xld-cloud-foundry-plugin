#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.client import CFClient


class CFClientUtil(object):

    @staticmethod
    def createSpaceClient(container, autologin=True):
        organization = container.getProperty("organization")
        client = CFClient.createClient(organization.getProperty("apiEndpoint"), organization.getProperty("username"), organization.getProperty("password"),
                                       org=organization.getProperty("organizationName"), space=container.getProperty("spaceName"))
        if autologin: client.login()
        return client


    @staticmethod
    def createOrganizationClient(container, autologin=True):
        client = CFClient.createClient(container.getProperty("apiEndpoint"), container.getProperty("username"), container.getProperty("password"))
        if autologin: client.login()
        return client

