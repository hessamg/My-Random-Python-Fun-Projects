#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Update package lists
sudo apt-get update

# Install Qt 5 qmake, make, bear, and clangd
# DEBIAN_FRONTEND=noninteractive is used to avoid interactive prompts
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y qtbase5-dev qt5-qmake make bear clangd

echo "Setup complete. Qt, make, bear, and clangd have been installed."
