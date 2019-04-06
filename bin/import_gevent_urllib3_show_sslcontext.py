from __future__ import print_function
import gevent
from gevent import monkey
monkey.patch_all()
import urllib3
print(urllib3.util.ssl_.SSLContext)
