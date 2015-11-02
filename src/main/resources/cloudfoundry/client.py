#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from org.cloudfoundry.client.lib import CloudCredentials
from org.cloudfoundry.client.lib.domain import CloudEntity, CloudService, CloudApplication, Staging
from org.cloudfoundry.client.lib.rest import CloudControllerClientFactory
from java.net import URI
from java.util import HashMap
from java.lang import String
import time


class CFClient(object):
    def __init__(self, apiEndpoint, client, factory):
        self._apiEndpoint = apiEndpoint
        self._client = client
        self._factory = factory

    @staticmethod
    def createClient(apiEndpoint, username, password, org=None, space=None):
        apiEndpointUrl = URI(apiEndpoint).toURL()
        credentials = CloudCredentials(username, password)
        factory = CloudControllerClientFactory(None, False)

        if space is not None and org is not None:
            client = factory.newCloudController(apiEndpointUrl, credentials, org, space)
        else:
            client = factory.newCloudController(apiEndpointUrl, credentials, None)

        return CFClient(apiEndpointUrl, client, factory)

    def login(self):
        self._client.login()

    def logout(self):
        self._client.logout()

    def discoverSpaces(self, organizationName):
        spaces = []
        for space in self._client.spaces:
            if space.organization.name == organizationName:
                spaces.append(space)
        return spaces

    def discoverDomains(self, organizationName):
        domains = []
        for domain in self._client.domains:
            if domain.owner.name == "none" or domain.owner.name == organizationName:
                domains.append(domain)
        return domains

    def createSpace(self, orgName, spaceName):
        org_uuid = None
        for org in self._client.organizations:
            print org.name
            if org.name == orgName:
                org_uuid = org.meta.guid
                break

        if org_uuid is None:
            raise Exception("Org [%s] not found." % orgName)

        for space in self._client.spaces:
            if space.name == spaceName and space.organization.name == orgName:
                print "Space [%s] already exists for org [%s]." % (spaceName, orgName)
                return False

        req = HashMap()
        req.put("organization_guid", org_uuid)
        req.put("name", spaceName)
        url = "%s/v2/spaces" % self._apiEndpoint
        self._factory.restTemplate.postForObject(url, req, String)
        print "Space [%s] created for org [%s]." % (spaceName, orgName)
        return True

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
            self._client.updateApplicationUris(appName,uris)

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
            counter = 0
            while True and counter < retrialCount:
                counter += 1
                if CloudApplication.AppState.STARTED == self._getApplication(appName).state:
                    print "Application [%s] started" % appName
                    return True
                time.sleep(waitTime)

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
