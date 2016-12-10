#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil

cf_client = CFClientUtil.create_space_client(deployed.container)
for route in deployed.routes:
    if green:
        cf_client.map_route(appName, route.domainName, "%s_green" % route.hostname, route.path, route.port, route.randomPort)
    else:
        cf_client.map_route(appName, route.domainName, route.hostname, route.path, route.port, route.randomPort)