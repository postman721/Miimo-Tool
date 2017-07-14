#!/bin bash
#This is the Miimo_tool starter script. Copyright (C) 2015 JJ Posti from techtimejourney.net
#This program comes with ABSOLUTELY NO WARRANTY; for details see: 
#http://www.gnu.org/copyleft/gpl.html
#This is free software, and you are welcome to redistribute it
#under GPL Version 3, 29 June 2007."

echo "Enter the directory path which contains 
the content you want to decompress or compress  \c  "
read FILE
cd $FILE
sleep 2
echo "\n"
python /usr/share/miimo.py 

