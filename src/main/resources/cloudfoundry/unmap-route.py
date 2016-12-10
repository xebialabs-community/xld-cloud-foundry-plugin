#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil

cf_client = CFClientUtil.create_space_client(previousDeployed.container)
cf_client.unmap_route(previousDeployed.appName, previousDeployed.domainName, previousDeployed.hostname, previousDeployed.path, previousDeployed.port)