#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createOrganizationClient(thisCi)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry organization")

if not cfClient.createSpace(thisCi.getProperty("organizationName"), parameters["spaceName"]):
    print "Failed to create space [%s] for organization [%s]" % (parameters["Instances"], thisCi.getProperty("organizationName"))
