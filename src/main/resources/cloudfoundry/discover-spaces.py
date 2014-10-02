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
    spaceCi = new_instance("%s/%s" % (organizationId, space.name), "cf.Space")
    if not repositoryService.exists(spaceCi.id):
        spaceCi.setProperty("spaceName", space.name)
        create_or_read(spaceCi)
        print "Space [%s] has been discovered" % space.name

cfClient = CFClientUtil.createOrganizationClient(thisCi)

if cfClient is None:
        sys.exit("Could not connect to cloudfoundry organization")

spaces = cfClient.discoverSpaces(thisCi.getProperty("organizationName"))

for space in spaces:
        reverse_engineer_space(space, thisCi.id)
