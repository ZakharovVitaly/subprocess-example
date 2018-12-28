#!/usr/bin/python2
import os
import sys
import subprocess as sp
import shlex

def shell(cmd, user):
    with open(os.devnull, 'wb') as devnull:
        first = sp.Popen(shlex.split(cmd), stdout=sp.PIPE, stderr=devnull, shell=False)
        if first:
            #Potentially dangerous shell call which presumably may be injected through `user` variable but not
            second = sp.Popen(shlex.split('/bin/egrep ^' + user), stdin=first.stdout, stdout=sp.PIPE, stderr=devnull, shell=False)
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
        else:
            print 'No such user or wrong parameteres: ' + user
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(0)
