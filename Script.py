import urllib2
import os

url = "http://python.org/ftp/python/2.7.3/python-2.7.3.msi"
url2 = "http://download.microsoft.com/download/4/0/6/4067968E-5530-4A08-B8EC-17D2B3F02C35/vs_ultimateweb.exe"
url3 = "http://pygame.org/ftp/pygame-1.9.2a0.win32-py2.7.msi"
url4 = "http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe"
url5 = "http://pypi.python.org/packages/2.7/p/pykinect/pykinect-1.0-py2.7.egg"
url6 = "https://dl.dropbox.com/u/101363146/PTVS%201.5%20Beta%201.msi"
url7 = "https://dl.dropbox.com/u/101363146/PTVS%201.5%20Beta%201%20-%20PyKinect%20Sample.msi"
url8 = "https://dl.dropbox.com/u/101363146/KinectSDK-v1.5-Setup.exe" 
url9 = "https://dl.dropbox.com/u/101363146/KinectDeveloperToolkit-v1.5.2-Setup.exe"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url2.split('/')[-1]
u = urllib2.urlopen(url2)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url3.split('/')[-1]
u = urllib2.urlopen(url3)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url4.split('/')[-1]
u = urllib2.urlopen(url4)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url5.split('/')[-1]
u = urllib2.urlopen(url5)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url6.split('/')[-1]
u = urllib2.urlopen(url6)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url7.split('/')[-1]
u = urllib2.urlopen(url7)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url8.split('/')[-1]
u = urllib2.urlopen(url8)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

file_name = url9.split('/')[-1]
u = urllib2.urlopen(url9)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

raw_input("Press Enter to open Python 2.7.3")
os.system('"python-2.7.3.msi"');

raw_input("Press Enter to open Visual Studio Ultimate")
os.system('"vs_ultimateweb.exe"');

raw_input("Press Enter to open PTVS 1.5 Beta 1")
os.system('"PTVS%201.5%20Beta%201.msi"');

raw_input("Press Enter to open PyGame 1.9.2a0")
os.system('"pygame-1.9.2a0.win32-py2.7.msi"');

raw_input("Press Enter to open KinectSDK v1.5")
os.system('"KinectSDK-v1.5-Setup.exe"');

raw_input("Press Enter to open Kinect Developer Toolkitv1.5.2")
os.system('"KinectDeveloperToolkit-v1.5.2-Setup.exe"');

raw_input("Press Enter to open PyKinect")
os.system('"PTVS%201.5%20Beta%201%20-%20PyKinect%20Sample.msi"');

raw_input("Press Enter to open SetupTools 0.6c11")
os.system('"setuptools-0.6c11.win32-py2.7.exe"');
