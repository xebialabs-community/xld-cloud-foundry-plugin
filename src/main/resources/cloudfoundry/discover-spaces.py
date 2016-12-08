#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from cloudfoundry.util import CFClientUtil
import sys

def new_instance(id, ci_type):
    return Type.valueOf(ci_type).descriptor.newInstance(id)

def create_or_read(ci):
    if not repositoryService.exists(ci.id):
        ci = repositoryService.create([ci])[0]
    else:
        ci = repositoryService.read(ci.id)
    return ci

def reverse_engineer_space(cf_space, organization_id):
    space_ci = new_instance("%s/%s" % (organization_id, cf_space.name), "cf.Space")
    if not repositoryService.exists(space_ci.id):
        space_ci.setProperty("spaceName", cf_space.name)
        create_or_read(space_ci)
        print "Space [%s] has been discovered" % cf_space.name

cf_client = CFClientUtil.create_organization_client(thisCi)

if cf_client is None:
        sys.exit("Could not connect to cloudfoundry organization")

spaces = cf_client.discover_spaces()

for space in spaces:
        reverse_engineer_space(space, thisCi.id)
