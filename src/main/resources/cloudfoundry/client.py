#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from org.cloudfoundry.operations import DefaultCloudFoundryOperations
from org.cloudfoundry.operations.applications import DeleteApplicationRequest, GetApplicationManifestRequest, PushApplicationRequest, RenameApplicationRequest, ScaleApplicationRequest, StartApplicationRequest, StopApplicationRequest
from org.cloudfoundry.operations.routes import MapRouteRequest, UnmapRouteRequest
from org.cloudfoundry.operations.services import CreateServiceInstanceRequest, DeleteServiceInstanceRequest, GetServiceInstanceRequest, BindServiceInstanceRequest
from org.cloudfoundry.operations.spaces import CreateSpaceRequest, DeleteSpaceRequest
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


    def delete_space(self, space_name):
        self._client.spaces().delete(DeleteSpaceRequest.builder().name(space_name).build()).block()


    def application_exists(self, app_name):
        for application in self._client.applications().list().toIterable():
            if application.getName() == app_name:
                return True
        return False


    def create_application(self, app_name, file, memory=512, instances=1, build_pack=None, hostname=None):
        if self.application_exists(app_name):
            self.delete_application(app_name)
        print "Creating application [%s] with memory [%s]" % (app_name, memory)
        self._client.applications().push(PushApplicationRequest.builder().name(app_name).application(file).buildpack(build_pack).host(hostname).instances(instances).memory(memory).noRoute(True).noStart(True).build()).block()


    def delete_application(self, app_name):
        if self.application_exists(app_name):
            self._client.applications().delete(DeleteApplicationRequest.builder().name(app_name).build()).block()


    def _get_application_manifest(self, app_name):
        return self._client.applications().getApplicationManifest(GetApplicationManifestRequest.builder().name(app_name).build()).block()

    def rename_application(self, app_name):
        self._client.applications().rename(RenameApplicationRequest.builder().name("%s_green" % app_name).newName(app_name).build()).block()

    def start_application(self, app_name):
        self._client.applications().start(StartApplicationRequest.builder().name(app_name).build()).block()


    def stop_application(self, app_name):
        self._client.applications().stop(StopApplicationRequest.builder().name(app_name).build()).block()


    def scale_application(self, app_name, instances, memory):
        self._client.applications().scale(ScaleApplicationRequest.builder().name(app_name).instances(instances).memoryLimit(memory).build()).block()


    def _service_instance_exists(self, instance_name):
        try:
            service_instance = self._client.services().getInstance(GetServiceInstanceRequest.builder().name(instance_name).build()).block()
            print "Service instance [%s] exists" % service_instance.getName()
            return True
        except:
            return False


    def create_service(self, instance_name, service_name, service_plan):
        if not self._service_instance_exists(instance_name):
            self._client.services().createInstance(CreateServiceInstanceRequest.builder().serviceInstanceName(instance_name).serviceName(service_name).planName(service_plan).build()).block()
            print "Service [%s] created" % instance_name
        else:
            print "Service [%s] already exists" % instance_name


    def delete_service(self, instance_name):
        if self._service_instance_exists(instance_name):
            self._client.services().deleteInstance(DeleteServiceInstanceRequest.builder().name(instance_name).build()).block()
            print "Service [%s] deleted" % instance_name
        else:
            print "Service [%s] not found" % instance_name


    def _service_already_bound(self, app_name, instance_name):
        services = self._get_application_manifest(app_name).getServices()
        return services is not None and instance_name in services


    def bind_service(self, app_name, service_instance_name):
        if not self._service_already_bound(app_name, service_instance_name):
            self._client.services().bind(BindServiceInstanceRequest.builder().applicationName(app_name).serviceInstanceName(service_instance_name).build()).block()

    def map_route(self, app_name, domain_name, hostname, path, port=None, random_port=None):
        self._client.routes().map(MapRouteRequest.builder().applicationName(app_name).domain(domain_name).host(hostname).path(path).build()).block()

    def unmap_route(self, app_name, domain_name, hostname, path, port=None):
        self._client.routes().unmap(UnmapRouteRequest.builder().applicationName(app_name).domain(domain_name).host(hostname).path(path).build()).block()
