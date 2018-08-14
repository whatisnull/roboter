#!/bin/bash


#set +u -ex


verify_root() {
    # Verify running as root:
    if [ "$(id -u)" != "0" ]; then
        if [ $# -ne 0 ]; then
            echo "Failed running with sudo. Exiting." 1>&2
            exit 1
        fi
        echo "This script must be run as root. Trying to run with sudo."
        sudo bash "$0" --with-sudo
        exit 0
    fi
}


clear_old_env() {
    echo "clear old env"
    rm -rf android-tools/ node node-v9.11.1-linux-x64/
}


mkdir_data_dir() {
    echo "mkdir source data dir"
    mkdir -p ../data/apk
}


install_jdk() {
    echo "download jdk from remote server, and install"
    # wget http://xxx.com/jdk-8u171-linux-x64.rpm -P /tmp/
    rpm -ivh /tmp/jdk-8u171-linux-x64.rpm
}


install_android_tools() {
    echo "download android tools from remote server, and install"
    # wget http://xxx.com/android-tools.tar.gz -P /tmp/
    tar -xzf /tmp/android-tools.tar.gz -C /opt

}


install_node() {
    echo "download node from remote server, and install/create link"
    # wget http://xxx.com/node.tar.tz -P /tmp/
    tar -xzf /tmp/node.tar.gz -C /opt
    ln -s /opt/node-v9.11.1-linux-x64 /opt/node

}


set_env() {
    echo "set java/android/apktool/node path"
    cat env >> /etc/bashrc
    source /etc/bashrc

}


test_env() {
    echo "test some env:"
    echo "java version: "`java -version`
    echo "adb version: "`adb version`
    echo "apktool versionL "`apktool -version`
    echo "aapt version: "`aapt v`

}



verify_root
clear_old_env
mkdir_data_dir
#install_jdk
install_android_tools
install_node
set_env
test_env


