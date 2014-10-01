#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createSpaceClient(thisCi.container)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry space")


cfClient.scaleApplication(thisCi.name, parameters["Instances"], parameters["Memory"])

cfClient.logout()