#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import time

from org.cloudfoundry.operations import DefaultCloudFoundryOperations
from org.cloudfoundry.operations.spaces import CreateSpaceRequest
from org.cloudfoundry.reactor import DefaultConnectionContext
from org.cloudfoundry.reactor.client import ReactorCloudFoundryClient
from org.cloudfoundry.reactor.uaa import ReactorUaaClient
from org.cloudfoundry.reactor.tokenprovider import PasswordGrantTokenProvider

class CFClient(object):
    def __init__(self, api_endpoint, client):
        self._apiEndpoint = api_endpoint
        self._client = client

    @staticmethod
    def create_client(api_endpoint, username, password, ssl=False, org=None, space=None):
        connection_context = DefaultConnectionContext.builder().apiHost(api_endpoint).skipSslValidation(ssl).build()
        token_provider = PasswordGrantTokenProvider.builder().password(password).username(username).build()
        cloud_foundry_client = ReactorCloudFoundryClient.builder().connectionContext(connection_context).tokenProvider(token_provider).build()
        uaa_client = ReactorUaaClient.builder().connectionContext(connection_context).tokenProvider(token_provider).build()

        if space is not None and org is not None:
            client = DefaultCloudFoundryOperations.builder().cloudFoundryClient(cloud_foundry_client).uaaClient(uaa_client).organization(org).space(space).build()
        elif org is not None:
            client = DefaultCloudFoundryOperations.builder().cloudFoundryClient(cloud_foundry_client).uaaClient(uaa_client).organization(org).build()

        return CFClient(api_endpoint, client)


    def login(self):
        self._client.login()


    def logout(self):
        self._client.logout()


    def discover_spaces(self):
        spaces = []
        for space in self._client.spaces().list().toIterable():
            spaces.append(space)
        return spaces


    def discover_domains(self):
        domains = []
        for domain in self._client.domains().list().toIterable():
            domains.append(domain)
        return domains


    def create_space(self, space_name, organization_name):
        self._client.spaces().create(CreateSpaceRequest.builder().name(space_name).organization(organization_name).build()).block()


    def deleteSpace(self, orgName, spaceName):
        space_uuid = None
        for space in self._client.spaces:
            if space.name == spaceName and space.organization.name == orgName:
                space_uuid = space.meta.guid
                break

        if space_uuid is None:
            print "Space [%s] does not exist for org [%s]." % (spaceName, orgName)
            return False

        url = "%s/v2/spaces/%s" % (self._apiEndpoint, space_uuid)
        self._factory.restTemplate.delete(url)
        print "Space [%s] delete from org [%s]." % (spaceName, orgName)
        return True


    def applicationExists(self, appName):
        try:
            self._client.getApplication(appName)
            return True
        except:
            return False


    def createApplication(self, appName, memory=512, uris=[]):
        if not self.applicationExists(appName):
            print "Creating application [%s] with memory [%s] and the following uris %s" % (appName, memory, uris)
            self._client.createApplication(appName, Staging(), memory, uris, None)
        else:
            self._client.updateApplicationUris(appName, uris)


    def deleteApplication(self, appName):
        if self.applicationExists(appName):
            self._client.deleteApplication(appName)


    def uploadApplication(self, appName, file):
        self._client.uploadApplication(appName, file, None)


    def _getApplication(self, appName):
        return self._client.getApplication(appName)


    def startApplication(self, appName, retrialCount=30, waitTime=2):
        time.sleep(waitTime)
        if CloudApplication.AppState.STARTED == self._getApplication(appName).state:
            print "Application [%s] already started" % appName
            return True
        else:
            print "Starting application [%s] ..." % appName
            self._client.startApplication(appName)
            print "Starting application [%s] called" % appName
            counter = 0
            while True and counter < retrialCount:
                counter += 1
                print "Waiting to check status application [%s] ..." % waitTime
                time.sleep(waitTime)
                print "Checking application status [%s] ..." % appName
                if CloudApplication.AppState.STARTED == self._getApplication(appName).state:
                    print "Application [%s] started" % appName
                    return True

        return False


    def stopApplication(self, appName, retrialCount=30, waitTime=2):
        time.sleep(waitTime)
        if CloudApplication.AppState.STOPPED == self._getApplication(appName).state:
            print "Application [%s] already stopped" % appName
            return True
        else:
            self._client.stopApplication(appName)
            counter = 0
            while True and counter < retrialCount:
                counter += 1
                if CloudApplication.AppState.STOPPED == self._getApplication(appName).state:
                    print "Application [%s] stopped" % appName
                    return True
                time.sleep(waitTime)
        return False


    def scaleApplication(self, appName, instances, memory):
        self._client.updateApplicationInstances(appName, instances)
        self._client.updateApplicationMemory(appName, memory)


    def _serviceInstanceExists(self, instanceName):
        return self._client.getService(instanceName) is not None


    def createService(self, instanceName, serviceName, servicePlan):
        if not self._serviceInstanceExists(instanceName):
            service = CloudService(CloudEntity.Meta.defaultMeta(), instanceName)
            service.setLabel(serviceName)
            service.setPlan(servicePlan)
            self._client.createService(service)
            print "Service [%s] created" % instanceName


    def deleteService(self, instanceName):
        if self._serviceInstanceExists(instanceName):
            self._client.deleteService(instanceName)
            print "Service [%s] deleted" % instanceName


    def _serviceAlreadyBound(self, appName, instanceName):
        services = self._getApplication(appName).services
        return services is not None and instanceName in services


    def bindService(self, appName, instanceName):
        if not self._serviceAlreadyBound(appName, instanceName):
            self._client.bindService(appName, instanceName)


    def setEnvironmentVariables(self, appName, vars):
        if self.applicationExists(appName):
            self._client.updateApplicationEnv(appName, vars)
