#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.client import CFClient


class CFClientUtil(object):

    @staticmethod
    def create_space_client(container):
        organization = container.getProperty("organization")
        client = CFClient.create_client(organization.getProperty("apiEndpoint"), organization.getProperty("username"), organization.getProperty("password"), ssl=organization.getProperty("ignoreSsl"),
                                        org=organization.getProperty("organizationName"), space=container.getProperty("spaceName"))
        return client


    @staticmethod
    def create_organization_client(container):
        client = CFClient.create_client(container.getProperty("apiEndpoint"), container.getProperty("username"), container.getProperty("password"), ssl=container.getProperty("ignoreSsl"),org=container.getProperty("organizationName"))
        return client

