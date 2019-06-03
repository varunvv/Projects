To convert images to a video file 

Prerequirement

Images should be named in the order of their time sequence


1.  Create a file containing the names of images 
    a.  Open a terminal direct to the folder in which images are stored
    b.  run ls > filname.txt 
        File with name filename.txt will be saved in the working folder
        remove last line from the file
2.Give the file name in CopyFilestoasingleFolder.py (inputFile)
3.set parentFolder
4.outFolderName
Scrip will Read all the images from the parent folder and save them to outFolderName


6. After this direct terminal to outFolderName
 run the command "x=1; for i in *png; do counter=$(printf %03d $x); ln "$i" /tmp/img"$counter".png; x=$(($x+1)); done"
 This will copy the remaned images to temp folder with their names changed
 
7. ffmpeg -f image2 -i /tmp/img%03d.png /tmp/a.mp4
    Run this command to create the video file 


