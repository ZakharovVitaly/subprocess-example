#!/usr/bin/python2
import os
import sys
import subprocess as sp
import shlex

def shell(cmd, user):
#This is injectable but simple and common code example that could receive malicious parameters through `user` variable
    #out = os.popen(cmd + ' | /bin/egrep -w ^' + user).read()
#Or more realistic variation but vulnerable too
    #out = os.popen(cmd + ' | /bin/egrep -w ^' + user + ' 2>/dev/null').read()
    #return out.strip()

#This code do the same thing but it is protected from that type of injection
    with open(os.devnull, 'wb') as devnull:
        first = sp.Popen(shlex.split(cmd), stdout=sp.PIPE, stderr=devnull, shell=False)
        if first:
            second = sp.Popen(shlex.split('/bin/egrep -w ^' + user), stdin=first.stdout, stdout=sp.PIPE, stderr=devnull, shell=False)
            first.stdout.close()
            out = second.communicate()[0]
            return out.strip()
        else:
            return None

if __name__ == '__main__':
    try:
        cmd = '/bin/ps -axwug'
        #cmd = '/bin/ps -ef'
        user = raw_input('Select user to get info: ')
        result = shell(cmd, user)
        if result:
            print result
            sys.exit(0)
        else:
            print 'No such user or wrong parameters: ' + user
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(0)
