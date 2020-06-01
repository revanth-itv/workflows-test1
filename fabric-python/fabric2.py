from fabric import Connection

result = Connection('demo.itversity.com').run('hostname')

result

