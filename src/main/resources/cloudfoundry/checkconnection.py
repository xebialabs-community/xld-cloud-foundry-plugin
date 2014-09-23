from cloudfoundry.util import CFClientUtil
import sys

for arg in sys.argv:
    print arg

class Container:
   def __init__(self,apiEndpoint,username,password,org,spaceName):
      self.apiEndpoint = apiEndpoint
      self.username = username
      self.password = password
      self.org = org
      self.spaceName = spaceName

   def getProperty(self,propertyName):
      if propertyName == "apiEndpoint":
          return self.apiEndpoint
      if propertyName == "username":
          return self.username
      if propertyName == "password":
          return self.password
      if propertyName == "org":
          return self.org
      if propertyName == "spaceName":
          return self.spaceName

container = Container(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])

cfClient = CFClientUtil.createClient(container)

if cfClient is None:
	sys.exit("Could not connect to cloudfoundry space")