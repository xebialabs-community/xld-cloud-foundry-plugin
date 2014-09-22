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

