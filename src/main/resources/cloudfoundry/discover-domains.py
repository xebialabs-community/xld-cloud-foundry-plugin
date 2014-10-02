#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

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

def reverse_engineer_domain(domain, organizationId):
    organizationCi = create_or_read(new_instance(organizationId, "cf.Organization"))
    domainCi = new_instance("%s/%s" % (organizationId, domain.name), "cf.Domain")
    if not repositoryService.exists(domainCi.id):
        domainCi.setProperty("domainName", domain.name)
        create_or_read(domainCi)
        print "Domain [%s] has been discovered" % domain.name


cfClient = CFClientUtil.createOrganizationClient(thisCi)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry organization")

domains = cfClient.discoverDomains(thisCi.getProperty("organizationName"))

for domain in domains:
	reverse_engineer_domain(domain, thisCi.id)