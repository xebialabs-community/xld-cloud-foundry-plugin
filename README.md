# Requirements #

* **Requirements**
	* **XL Deploy** 4.1-beta-2
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

# Installation #

Place the plugin JAR file into your `SERVER_HOME/plugins` directory.   Make sure you have additional runtime libiraries mentioned in the requirements section also installed in the same directory.

Extract `cloudfoundry/discoveryapp/index.php` from the JAR and copy it to `SERVER_HOME/ext/cloudfoundry/discoveryapp/index.php`

