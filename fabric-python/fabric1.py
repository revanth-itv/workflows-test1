from fabric import Connection

c = Connection('localhost') #demo.itversity.com

c.run('id -u revanth')


'''
result = c.run('uname -s')

result.connection

result.stdout.strip() == 'Linux'

result.stdout.strip
'''