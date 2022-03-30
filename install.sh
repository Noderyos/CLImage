#!/bin/bash
if [ $UID != 0 ]; then
  echo "Please run this script at root"
  exit 1
fi
echo "Insalling in /usr/bin ..."
cp main.py /usr/bin/climage
a=$?
chmod /usr/bin/climage
if [ $? != 0 || $a != 0 ]; then
  echo "Error during install proccess :)"
else
  echo "Successfully installed :)"
  echo "You can use it now with this command: "
  echo "climage [image-file] [size]"
fi
