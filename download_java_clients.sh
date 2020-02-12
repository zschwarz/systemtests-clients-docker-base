#!/usr/bin/env bash

function install_java_client(){
    rm -rf ./build
    rm -rf ./cli-java
    mkdir -p build/java_clients
    wget https://github.com/rh-messaging/cli-java/releases/download/v2.4.0er2/cli-activemq-1.2.2-SNAPSHOT-5.11.0.redhat-630377.jar -O build/java_clients/cli-activemq.jar
    wget https://github.com/rh-messaging/cli-java/releases/download/v2.4.0er2/cli-artemis-jms-1.2.2-SNAPSHOT-2.7.0.redhat-00056.jar -O build/java_clients/cli-artemis-jms.jar
    wget https://github.com/rh-messaging/cli-java/releases/download/v2.4.0er2/cli-qpid-jms-1.2.2-SNAPSHOT-0.42.0.redhat-00001.jar -O build/java_clients/cli-qpid-jms.jar
    wget https://github.com/rh-messaging/cli-java/releases/download/v2.4.0er2/cli-paho-java-1.2.2-SNAPSHOT-RELEASE.jar -O build/java_clients/cli-paho-java.jar
}

install_java_client