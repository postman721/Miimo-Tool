#!/usr/bin/python3
import glob, tarfile, zipfile, os, bz2, gzip, sys, subprocess ,time, shutil
#files = filter(os.path.isfile, os.listdir( os.curdir ) )
enter = ("Please press Enter to exit")

def start ():
	print ""	
	print ("Welcome to Miimo Tool Version B (Revision 2) Copyright (C) 2015 JJ Posti") 
	print ("from techtimejourney.net") 
	print ""
	print ("This program comes with ABSOLUTELY NO WARRANTY; for details see:") 
	print ("http://www.gnu.org/copyleft/gpl.html")
	print ""
	print ("This is free software, and you are welcome to redistribute it")
	print ("under GPL Version 3, 29 June 2007.")
	print ""
	choice = raw_input ("Continue? y/n ")
	if choice == "y":
		selection ()
	elif choice == "n":
		print ("Program exits.")
	else:
		print ("Incorrect key selection")
		raw_input (enter)
		sys.exit(0)
def selection ():
	decompress ="1"
	comp ="2"
	print ""						
	select=raw_input ("Do you want to 1. decompress or 2. compress )? ")
	time.sleep (1)
	print ""		
	if select == "1":
		archives () 		
	elif select == "2":
		compre ()
	else:
		print ("Incorrect key selection")
		raw_input (enter)
		sys.exit(0)

#Defining zip directory function
def zipdir(zipname, dir_to_zip):
    dir_to_zip_len = len(dir_to_zip.rstrip(os.sep)) + 1
    with zipfile.ZipFile(zipname, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for dirname, subdirs, files in os.walk(dir_to_zip):
            for filename in files:
                path = os.path.join(dirname, filename)
                entry = path[dir_to_zip_len:]
                zf.write(path, entry)
        						
def archives ():
	gz  ="1"
	bz2 ="2"
	zip ="3"
	print ""
	types=raw_input ("What filetype you want to decompress (1. gz, 2. bz2 or 3. zip)? ")
	time.sleep (1)
	print ""				
	if types == "1": 
		print ""
		print ""
		files = glob.glob('./*.gz')
		print files
		print ""
		time.sleep (1)
		decom=raw_input("What file you want to decompress? ")
		print ""
		print ("tar.gz decompress")
		time.sleep (1)
		gets0=tarfile.open("%s" % decom , 'r:gz')
		gets0
		print ("Now decompressing:") ,  decom
		print ""
		print ("The following content is now available inside decompressed direcory")
		print ""
		gets0.extractall('decompressed')
		print os.listdir('decompressed')
		print ""
		print "All done. Time to exit"			
	elif types == "2": 
		print ""
		print ""
		files = glob.glob('./*.bz2')
		print files
		print ""
		time.sleep (1)
		decom=raw_input("What file you want to decompress? ")
		print ""
		print ("tar.bz2 decompress")
		time.sleep (1)
		gets0=tarfile.open("%s" % decom , 'r:bz2')
		gets0
		print ("Now decompressing:") ,  decom
		print ""
		print ("The following content is now available inside decompressed direcory")
		print ""
		gets0.extractall('decompressed')
		print os.listdir('decompressed')
		print ""
		print "All done. Time to exit"	
	elif types == "3": 
		print ""
		print ""
		files = glob.glob('./*.zip')
		print files
		print ""
		time.sleep (1)
		decom=raw_input("What file you want to decompress? ")
		print ""
		print ("zip decompress")
		time.sleep (1)
		gets0=zipfile.ZipFile("%s" % decom ,)
		gets0
		print ("Now decompressing:") ,  decom
		print ""
		print ("The following content is now available inside decompressed direcory")
		print ""
		gets0.extractall('decompressed')
		print os.listdir('decompressed')
		print ""
		print "All done. Time to exit"
	else:
		print ("Incorrect key selection")
		raw_input (enter)
		sys.exit(0)
def compre ():
	gz  ="1"
	bz2 ="2"
	zip ="3"
	zip ="4"
	print ""
	print ""
	print ""
	types=raw_input("Select compression format: 1.tar.gz 2. tar.bz2 3. zip(files) 4.zip(folder) ? ")
	print ""
	time.sleep (1)
	print ""
	if types == "1":
		print ""
		print ("tar.gz compress")
		time.sleep (1)
		print ""
		files = os.listdir(os.curdir) 
		print files
		print ""
		decom=raw_input("What you want to compress? ")
		print ""
		print ""
		gets0=tarfile.open("%s.tar.gz" % decom , 'w:gz')
		gets0
		for name in [decom]:
			gets0.add(name)
		gets0.close()
		print ("Now compressing:") ,  decom
		print ""
		print ("The following tar.gz content is now available inside the current direcory")
		print ""
		files1 = glob.glob('./*.gz')
		print files1	
	elif types == "2":
		print ""
		print ("tar.bz2 compress")
		time.sleep (1)
		print ""
		files = os.listdir(os.curdir) 	
		print files
		print ""
		decom=raw_input("What you you want to compress? ")
		print ""
		print ""
		gets0=tarfile.open("%s.tar.bz2" % decom , 'w:bz2')
		for name in [decom]:
			gets0.add(name)
		gets0.close()
		print ("Now compressing:") ,  decom
		print ""
		print ("The following bz2 content is now available inside the current direcory")
		print ""
		files1 = glob.glob('./*.bz2')
		print files1	
	elif types == "3":
		print ""
		print ("zip compress")
		time.sleep (1)
		print ""
		files = os.listdir(os.curdir) 
		print files
		print ""
		decom=raw_input("What you you want to compress? ")
		print ""
		print ""
		gets0=zipfile.ZipFile("%s.zip" % decom , mode='w')
		for name in [decom]:
			gets0.write(name)
		gets0.close()
		print ("Now compressing:") ,  decom
		print ""
		print ("The following zip content is now available inside the current direcory")
		print ""
		files1 = glob.glob('./*.zip')
		print files1	
	elif types == "4":
		print ""
		print ("zip compress")
		time.sleep (1)
		print ""
		files = os.listdir(os.curdir) 
		print files
		print ""
		decom=raw_input("What you you want to compress? ")
		print ""
		print ""
		os.chdir (decom)
		shutil.make_archive(os.getcwd(), 'zip')
		
		print ("Now compressing:") ,  decom
		print ""
		print ("The zip content should now be available inside your home direcory")
		
	else:
		print ("Incorrect key selection")
		raw_input (enter)
		sys.exit(0)
start ()

