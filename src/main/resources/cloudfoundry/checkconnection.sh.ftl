#!/bin/sh

rm -rf cloudfoundry
mkdir cloudfoundry
mv *.py cloudfoundry
mv cloudfoundry/checkconnection.py .

<#assign pluginFolder=params.pluginFolder>
<#assign libFolder=params.libFolder>

export CLASSPATH="${pluginFolder}/*:${libFolder}/*"
jython checkconnection.py '${container.apiEndpoint}' '${container.username}' '${container.password}' '${container.org}' '${container.spaceName}' >/dev/null 2>/dev/null
