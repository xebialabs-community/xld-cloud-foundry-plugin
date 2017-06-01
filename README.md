# Preface #

This document describes the functionality provided by the Cloud Foundry plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The Cloud Foundry plugin is a XL Deploy plugin that adds capability for deploying applications to a Cloud Foundry space.

# CI status #

[![Build Status][xld-cloud-foundry-plugin-travis-image] ][xld-cloud-foundry-plugin-travis-url]
[![Codacy Badge][xld-cloud-foundry-plugin-codacy-image] ][xld-cloud-foundry-plugin-codacy-url]
[![Code Climate][xld-cloud-foundry-plugin-code-climate-image] ][xld-cloud-foundry-plugin-code-climate-url]
[![License: MIT][xld-cloud-foundry-plugin-license-image] ][xld-cloud-foundry-plugin-license-url]
[![Github All Releases][xld-cloud-foundry-plugin-downloads-image] ]()

[xld-cloud-foundry-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-cloud-foundry-plugin.svg?branch=master
[xld-cloud-foundry-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-cloud-foundry-plugin
[xld-cloud-foundry-plugin-codacy-image]: https://api.codacy.com/project/badge/grade/869116a652014efe81a5ff8380b0a6a9    
[xld-cloud-foundry-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xld-cloud-foundry-plugin
[xld-cloud-foundry-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xld-cloud-foundry-plugin/badges/gpa.svg
[xld-cloud-foundry-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xld-cloud-foundry-plugin
[xld-cloud-foundry-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-cloud-foundry-plugin-license-url]: https://opensource.org/licenses/MIT
[xld-cloud-foundry-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xld-cloud-foundry-plugin/total.svg


# Requirements #

* **Requirements**
	* **XL Deploy** 6.0.1+
	* **XL Plugins**
		* Database Plugin
	* **Additional Runtime Libraries**
	    * [hotfix-basestep-ctx-public.jar](blob/master/src/main/hotfix/plugins/hotfix-basestep-ctx-public.jar) (should be put under the hotfix/plugins)..

# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.   Make sure you have additional runtime libraries mentioned in the requirements section also installed in the correct directory.

Extract `cloudfoundry/discoveryapp/index.php` from the JAR and copy it to `SERVER_HOME/ext/cloudfoundry/discoveryapp/index.php`

# Upgrade #

* When upgrading from a version before 4.5.4 to a version >=4.5.4, be aware that the containers under Infrastructure have changed. From 4.5.4+ the Organizations, Spaces and Domains have been split into different CI. If you want to upgrade, you have to start from a clean repository (Delete all cf.Space instances), install 4.5.4+ and discover the domains and spaces.
* When upgrading to version 5.0.1+, be aware that most dependencies are packaged into the xldp plugin file.
* When upgrading to version 6.0.0+, the new api is being used from CloudFoundry.

# Usage #

1. Go to `Repository - Infrastructure`, create a new `cf.Organization` and discover the spaces and domains.
2. Create an environment under `Repository - Environments`
3. Create an application with `cf.ServiceSpec` and `cf.War` as deployables.
4. Start deploying

# Types #
+ `cf.Organization`
+ `cf.Space`
+ `cf.Domain`
+ `cf.War`
+ `cf.RouteSpec`
+ `cf.ServiceSpec`

