#!/usr/bin/env bash

sudo apt-get update

# Python Installation
yes | sudo apt-get install python-setuptools python-dev build-essential
yes | sudo easy_install pip

# Virtualenv Installation
yes | sudo apt-get install python-virtualenv