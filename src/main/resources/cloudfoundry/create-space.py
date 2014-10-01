from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createOrganizationClient(thisCi)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry organization")

if not cfClient.createSpace(thisCi.getProperty("organizationName"), parameters["spaceName"]):
    print "Failed to create space [%s] for organization [%s]" % (parameters["Instances"], thisCi.getProperty("organizationName"))
