import os, socket

base_dir = os.path.dirname(os.path.abspath(__file__))

user = 'cars'
passwd = 'cars'
db = 'cars'
host = 'localhost'

if socket.gethostname() == 'ubuntu-s-2vcpu-4gb-nyc1-01':
    mode = False
    proxy = ''
else:
    mode = True
    proxy = '173.208.36.232'
