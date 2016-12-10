#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
from java.io import File

cf_client = CFClientUtil.create_space_client(deployed.container)
cf_client.create_application(appName, File(deployed.file.path).toPath(), memory=deployed.memory, instances=deployed.instances, build_pack=deployed.buildPack, hostname=deployed.hostname)