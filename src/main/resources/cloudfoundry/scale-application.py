from cloudfoundry.util import CFClientUtil
import sys

cfClient = CFClientUtil.createClient(thisCi.container)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry space")


cfClient.scaleApplication(thisCi.name, parameters["Instances"], parameters["Memory"])

cfClient.logout()