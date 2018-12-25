#!/bin/sh

# OSx broke Pip, this updates Pip in the
# current environment to install dependencies
updatePip() {
    echo 'Updating pip'
    curl https://bootstrap.pypa.io/get-pip.py | python
}

installRequirements() {
    echo 'Installing pip requirements'
    pip3 install -r requirements.txt
}

workingDir='pwd'

updatePip
installRequirements

echo 'Done'
