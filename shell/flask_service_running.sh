#!/bin/bash
# Author: Ryan
# Date: 2020-08-10

function start_application() {
    service_running_start
    echo "[NOTICE]Running Function => [service_running_start]"
}

function service_running_start() {
    service_source_file=../manager.py
    python ${service_source_file} server

}

function main() {
    echo "-----------------[PROCESSING]-----------------"
    start_application
    echo "-----------------[PROCESSING]-----------------"
}

main
