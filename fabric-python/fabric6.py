import fabric 
from fabric import Connection

connect = Connection('cdhhost.itversity.com',user='cmadmin')

#connection=fabric.connection('192.168.110.130',user='vagrant',gateway='cdhhost.itversity.com')



connect.run('')
