from fabric import SerialGroup


result=SerialGroup('demo.itversity.com','cdhhost.itversity.com').run('hostname')

result
