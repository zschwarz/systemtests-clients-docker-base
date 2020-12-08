#!/usr/bin/env bash

function install_java_client(){
    rm -rf ./build
    rm -rf ./cli-java
    mkdir -p build/java_clients
    git clone https://github.com/rh-messaging/cli-java
    cd cli-java
    mvn clean package
    cd ..
    cp cli-java/cli-activemq/target/cli-activemq-*-SNAPSHOT-*.jar build/java_clients/cli-activemq.jar
    cp cli-java/cli-artemis-jms/target/cli-artemis-jms-*-SNAPSHOT-*.jar build/java_clients/cli-artemis-jms.jar
    cp cli-java/cli-qpid-jms/target/cli-qpid-jms-*-SNAPSHOT-*.jar build/java_clients/cli-qpid-jms.jar
    cp cli-java/cli-paho-java/target/cli-paho-java-*-SNAPSHOT-*.jar build/java_clients/cli-paho-java.jar
}

install_java_client