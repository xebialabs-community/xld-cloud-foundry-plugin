# Preface #

This document describes the functionality provided by the Cloud Foundry plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The Cloud Foundry plugin is a XL Deploy plugin that adds capability for deploying applications to a Cloud Foundry space.

# Requirements #

* **Requirements**
	* **XL Deploy** 4.5.0
	* **XL Plugins**
		* Database Plugin
	* **Additional Runtime Libraries**
		* protobuf-java-2.5.0.jar
		* tomcat-embed-websocket-8.0.8.jar
		* cloudfoundry-client-lib-1.0.3.jar
		* jackson-core-asl-1.9.2.jar
		* spring-security-oauth2-1.0.5.RELEASE.jar       
		* jackson-mapper-asl-1.9.2.jar
		* tomcat-embed-core-8.0.8.jar
	    * yamlbeans-1.06.jar
	    * spring-core-3.2.2.RELEASE.jar (should be under plugins)
	    * spring-web-3.2.2.RELEASE.jar (should replace the existing spring-web under `lib`, and also be put under `lib`)
	    * hotfix-basestep-ctx-public.jar (should be put under the hotfix).
	    * hotfix-DEPL-6955.jar (should be put under hotfix).

# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.   Make sure you have additional runtime libiraries mentioned in the requirements section also installed in the same directory.

Extract `cloudfoundry/discoveryapp/index.php` from the JAR and copy it to `SERVER_HOME/ext/cloudfoundry/discoveryapp/index.php`

