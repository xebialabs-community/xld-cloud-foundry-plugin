#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
