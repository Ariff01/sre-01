Inheritance Self-Assessment: File System
For this assessment, you will use Python to model a computer's file system.

Create a class called FileItem that represents any file in an operating system.
Research and identify attributes that are common to all files in an OS, such as permissions, owner, size, and so on.

Create a class called CsvFile that inherits from FileItem and that represents a CSV file in an operating system.
Include attributes that are specific to a CSV file.

Create a class JpgFile that inherits from FileItem and that represents a JPG file in an operating system.
Include attributes that are specific to a JPG file.
Create a class Mp3File that inherits from FileItem and that represents an MP3 file in an operating system.
Include attributes that are specific to an MP3 file.
------------------------------------------------------------------------------------------------------------

Challenge
Create a class Directory that inherits from FileItem and that represents a directory in an operating system.

Create a filesystem with at least 20 objects
Include at least three objects of each type (CsvFile, JpgFile, Mp3File, and Directory)
Include a directory structure with a depth of at least three (directory in a directory in a directory)
Include at least one directory that contains at least two other directories and at least two files.

------------------------------------------------------------------------------------------------------------
Requirements
Include your name and a current date in a comment on the first line of code.
Use meaningful names so that another developer can easily read your code to understand what it does.
The final version of this file must include at least four separate classes: the original FileItem class and three child classes that inherit from FileItem.
Each class must include appropriate attributes for that class.

#Ariff 12/08/2022
#code
class FileItem:
    def __init__(self, name, permissions, owner, size, time):
        self.name=name
        self.permissions=permissions
        self.owner=owner
        self.size=size
        self.time=time
class CsvFile(FileItem):
    directory='d1'
    def __init__(self, name, permissions, owner, size, time, headers):
        FileItem.__init__(self, name, permissions, owner, size, time)
        self.headers=headers
        
class JpgFile(FileItem):
    directory='d2'
    def __init__(self, name, permissions, owner, size, time, wpixel, hpixel, camera):    
        FileItem.__init__(self, name, permissions, owner, size, time)
        self.wpixel=wpixel
        self.hpixel=hpixel
        self.camera=camera

class Mp3File(FileItem):
    directory='d3'
    def __init__(self, name, permissions, owner, size, time, artist, album,directory):    
        FileItem.__init__(self, name, permissions, owner, size, time)
        self.artist=artist
        self.album=album
        self.d1=directory

class Directory(FileItem):
    pass
       
d1=Directory('directory1','read','user1','137.5MB','12:05:33')
d2=Directory('directory2','read','user1','237.4MB','10:53:12')
d3=Directory('directory3','read','user1','47.5MB','07:32:41')

c1=CsvFile('file1','read','user1','13.4MB','17:45:11',['name','address','number'])
c2=CsvFile('file2','read,write','user2','1.4MB','16:25:23',['name','date'])
c3=CsvFile('file3','read','user1','65.4MB','08:21:34',['stock','price'])
c4=CsvFile('file4','read','user2','4.0MB','14:15:13',['ID','salary','date'])
c5=CsvFile('file5','read,write','user1','11.4MB','08:45:11',['StudentID','School','City'])
c6=CsvFile('file6','read','user2','3.3MB','13:36:33',['Name','ID','address'])

j1=JpgFile('image1','read','user1','1.1MB','17:45:11',1400,800,'Android')
j2=JpgFile('image2','read','user3','844KB','14:15:13',700,450,'Iphone')
j3=JpgFile('image3','read','user2','398KB','16:25:23',1800,900,'Canon')
j4=JpgFile('image4','read','user1','3.5MB','08:45:11',1750,400,'Sony')
j5=JpgFile('image5','read','user1','4.4MB','13:36:33',1200,600,'Android')
j6=JpgFile('image6','read','user2','3.6MB','11:43:12',1650,450,'Iphone')

m1=Mp3File('song1','read,write,execute','user1','4.8MB','13:32:55','Olivia Rodrigo', 'x0')
m1=Mp3File('song2','read,execute','user1','3.6MB','17:45:11','The Weekend', 'ABCD')
m1=Mp3File('song3','read,execute','user2','6.2MB','08:45:11','Taylor Swift', 'Song')
m1=Mp3File('song4','read,write,execute','user3','6.1MB','11:43:12','Ariana Grande', 'Another Song')
m1=Mp3File('song5','execute','user1','7.3MB','08:21:34','Khalid', 'The Song')
m1=Mp3File('song6','read,write,execute','user1','4.2MB','13:36:33','Ariff', 'NewAlbum')




