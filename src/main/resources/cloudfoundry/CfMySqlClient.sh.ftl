<#--

    Copyright 2017 XEBIALABS

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

-->
#!/bin/sh

<#include "/generic/templates/linuxExportEnvVars.ftl">

<#assign username=step.ctx.getAttribute(deployed.cloudFoundryDbService + "-username")>
<#assign password=step.ctx.getAttribute(deployed.cloudFoundryDbService + "-password")>
<#assign host=step.ctx.getAttribute(deployed.cloudFoundryDbService + "-host")>
<#assign db=step.ctx.getAttribute(deployed.cloudFoundryDbService + "-db")>

<#--
<#assign username="2UnLMgwlpEFMxD4X"/>
<#assign password="almA98NnSAPcWcKs"/>
<#assign db="cf_4045b2ae_3e5a_437a_84f3_eb958dc7363d"/>
-->

"/usr/bin/mysql" --host=${host} --user=${username} --password=${password} ${db} < "${step.uploadedArtifactPath}"

res=$?
if [ $res != 0 ] ; then
exit $res
fi

