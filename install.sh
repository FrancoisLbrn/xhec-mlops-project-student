#!/bin/bash

# Ensure pip-tools is installed
pip install pip-tools

# Compile requirements.in to requirements.txt
pip-compile requirements.in

# Compile requirements-dev.in to requirements-dev.txt
pip-compile requirements-dev.in
