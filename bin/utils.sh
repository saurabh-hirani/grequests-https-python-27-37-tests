#!/bin/bash

export COLOR_BLACK=`tput setaf 0`
export COLOR_RED=`tput setaf 1`
export COLOR_GREEN=`tput setaf 2`
export COLOR_YELLOW=`tput setaf 3`
export COLOR_BLUE=`tput setaf 4`
export COLOR_MAGENTA=`tput setaf 5`
export COLOR_CYAN=`tput setaf 6`
export COLOR_WHITE=`tput setaf 7`
export FONT_BOLD=`tput bold`
export COLOR_RESET=`tput sgr0`

function log_error() {
    msg="$1"
    echo "${COLOR_RED}ERROR: $msg${COLOR_RESET}"
}

function log_success() {
    msg="$1"
    echo "${COLOR_CYAN}STATUS: $msg${RESET}"
}

function log_status() {
    msg="$1"
    echo "STATUS: $msg"
}
