#!/bin/bash

echo "Installing Explore..."

mkdir ~/.Explore
cp * -r ~/.Explore

echo "Installing Dependencies..."
pip3 install -r ~/.Explore/requirements.txt

echo "Installing Explore Executable..."

cat << EXPSCR > ~/.Explore/explore
cd ~/.Explore
python3 Explore.py
EXPSCR
chmod +x ~/.Explore/explore

echo "Installing Explore Server..."
cat << EXPSER > ~/.Explore/explore-server
cd ~/.Explore
node server.js
EXPSER

chmod +x ~/.Explore/explore ~/.Explore/explore-server

echo "Adding to PATH..."
if [ -e ~/.bashrc ]; then
  echo "export PATH=\"~/.Explore:$PATH\"" >> ~/.bashrc
fi

if [ -e ~/.zshrc ]; then
  echo "export PATH=\"~/.Explore:$PATH\"" >> ~/.zshrc
fi

echo ""
cat << FIN
Installation Finished!
Explore Installed at ~/.Explore

Restart the terminal and run:
explore : For starting Explore.
explore-server: For running Explore Server.

FIN
