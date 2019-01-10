import urllib, os, os.path

testfile = urllib.URLopener()
testfile.retrieve("http://ftp.uk.debian.org/debian/dists/stable/main/Contents-udeb-arm64.gz", "filecontent.gz")

DIR = '/tmp'
print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])