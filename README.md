# Preface #

This document describes the functionality provided by the Cloud Foundry plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The Cloud Foundry plugin is a XL Deploy plugin that adds capability for deploying applications to a Cloud Foundry space.

# CI status #

[![Build Status][xld-cloud-foundry-plugin-travis-image] ][xld-cloud-foundry-plugin-travis-url]
[![Codacy Badge][xld-cloud-foundry-plugin-codacy-image] ][xld-cloud-foundry-plugin-codacy-url]
[![Code Climate][xld-cloud-foundry-plugin-code-climate-image] ][xld-cloud-foundry-plugin-code-climate-url]

[xld-cloud-foundry-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-cloud-foundry-plugin.svg?branch=master
[xld-cloud-foundry-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-cloud-foundry-plugin
[xld-cloud-foundry-plugin-codacy-image]: https://api.codacy.com/project/badge/grade/869116a652014efe81a5ff8380b0a6a9
[xld-cloud-foundry-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xld-cloud-foundry-plugin
[xld-cloud-foundry-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xld-cloud-foundry-plugin/badges/gpa.svg
[xld-cloud-foundry-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xld-cloud-foundry-plugin


# Requirements #

* **Requirements**
	* **XL Deploy** 5.5.0+
	* **XL Plugins**
		* Database Plugin
	* **Additional Runtime Libraries**
	    * Extract the following jar's from the `xldp` release, and put them under `lib`:
	        * `jackson-annotations-2.3.0.jar`
	        * `jackson-core-2.3.3.jar`
	        * `jackson-databind-2.3.3.jar`
	    * [hotfix-basestep-ctx-public.jar](blob/master/src/main/hotfix/plugins/hotfix-basestep-ctx-public.jar) (should be put under the hotfix/plugins)..

# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.   Make sure you have additional runtime libraries mentioned in the requirements section also installed in the correct directory.

Extract `cloudfoundry/discoveryapp/index.php` from the JAR and copy it to `SERVER_HOME/ext/cloudfoundry/discoveryapp/index.php`

# Upgrade #

* When upgrading from a version before 4.5.4 to a version >=4.5.4, be aware that the containers under Infrastructure have changed. From 4.5.4+ the Organizations, Spaces and Domains have been split into different CI. If you want to upgrade, you have to start from a clean repository (Delete all cf.Space instances), install 4.5.4+ and discover the domains and spaces.
* When upgrading to version 5.0.1+, be aware that most dependencies are packaged into the xldp plugin file.

# Usage #

1. Go to `Repository - Infrastructure`, create a new `cf.Organization` and discover the spaces and domains.
2. Create an environment under `Repository - Environments`
3. Create an application with `cf.ServiceSpec` and `cf.War` as deployables.
4. Start deploying
