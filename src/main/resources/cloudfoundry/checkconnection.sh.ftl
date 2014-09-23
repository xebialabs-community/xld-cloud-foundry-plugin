<#--

    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.

-->
#!/bin/sh

rm -rf cloudfoundry
mkdir cloudfoundry
mv *.py cloudfoundry
mv cloudfoundry/checkconnection.py .

<#assign pluginFolder=params.pluginFolder>
<#assign libFolder=params.libFolder>

export CLASSPATH="${pluginFolder}/*:${libFolder}/*"
jython checkconnection.py '${container.apiEndpoint}' '${container.username}' '${container.password}' '${container.org}' '${container.spaceName}' >/dev/null 2>/dev/null
