#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

cf_client = CFClientUtil.create_space_client(thisCi.container)

if cf_client is None:
	sys.exit("Could not connect to cloudfoundry space")


cf_client.scale_application(thisCi.name, params["Instances"], params["Memory"])