import urllib

testfile = urllib.URLopener()
testfile.retrieve("http://ftp.uk.debian.org/debian/dists/stable/main/Contents-udeb-arm64.gz", "filecontent.gz")