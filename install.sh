#!/bin/bash

EXPLORE_DIR=$(pwd)

echo "Welcome to Explore Installer!"

echo "Enter the number for your selection: "
echo "1 Install Explore (recommended)."
echo "2 Repair (If you've run into a System Error)."
echo "3 Exit Installer."

read -p ":) > " CHOICE

if [ -z "$CHOICE" ]; then
  exit
fi

if [ $CHOICE == "1" ]; then
  pip3 install -r requirements.txt
  echo ""
  echo "Dependencies Installed!"

  touch explore
  echo "cd $EXPLORE_DIR" > explore
  echo "python3 $EXPLORE_DIR/Explore.py" >> explore
  chmod +x explore
  echo ""
  echo "Executable Script genereted!"

  echo "export PATH=\"$EXPLORE_DIR:$PATH\"" >> $HOME/.bashrc
  echo ""
  echo "Executable Script added to PATH (modified .bashrc)!"

  echo ""
  echo "Explore installed successfully!"

elif [ $CHOICE == "2" ]; then
  rm .val .cipher log.txt 2> /dev/null
  echo "System repaired!"

else
  exit

fi
