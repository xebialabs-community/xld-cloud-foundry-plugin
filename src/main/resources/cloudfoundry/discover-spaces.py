from cloudfoundry.util import CFClientUtil
import sys

def new_instance(id, ciType):
    return Type.valueOf(ciType).descriptor.newInstance(id)

def create_or_read(ci):
    if not repositoryService.exists(ci.id):
        ci = repositoryService.create([ci])[0]
    else:
        ci = repositoryService.read(ci.id)
    return ci

def reverse_engineer_space(space, organizationId):
    organizationCi = create_or_read(new_instance(organizationId, "cf.Organization"))
    space = new_instance("%s/%s" % (organizationId, space.name), "cf.Space")
    if not repositoryService.exists(space.id):
        space.setProperty("spaceName", space.name)
        space.setProperty("organization", organizationCi)
        repositoryService.create([space])

cfClient = CFClientUtil.createOrganizationClient(thisCi)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry organization")

spaces = cfClient.discoverSpaces(thisCi.getProperty("organizationName"))

for space in spaces:
	reverse_engineer_space(space, thisCi.getProperty("id"))