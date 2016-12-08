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

def reverse_engineer_domain(cf_domain, organization_id):
    domain_ci = new_instance("%s/%s" % (organization_id, cf_domain.name), "cf.Domain")
    if not repositoryService.exists(domain_ci.id):
        domain_ci.setProperty("domainName", cf_domain.name)
        create_or_read(domain_ci)
        print "Domain [%s] has been discovered" % cf_domain.name


cf_client = CFClientUtil.create_organization_client(thisCi)

if cf_client is None:
    sys.exit("Could not connect to cloudfoundry organization")

domains = cf_client.discover_domains()

for domain in domains:
    reverse_engineer_domain(domain, thisCi.id)