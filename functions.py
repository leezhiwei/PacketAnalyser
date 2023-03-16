import socket
import os
import signal

def endproc(signum, frame, pidtcpdump):
    os.killpg(os.getpgid(pidtcpdump), signal.SIGTERM) # function in case you CTRL + C ends tcpdump gracefully

def resolvehostname(iporhostname): # resolve into IP if hostname
    splittediporhostname = iporhostname.split('.') # split into list
    port = splittediporhostname[-1] # get port from negative index
    if len(splittediporhostname) != 5: # if len is not 5 , eg using hostname
        hostname = '' # init hostname var
        if len(splittediporhostname) != 2: # if length of splitted string is not 2 eg
            for part in splittediporhostname: # for each string in the list
                if part == port: # if port
                    break # break (dont want include)
                if splittediporhostname[0] == part: # if first string (like google in google.com)
                    hostname += part # add it to hostname
                else: # else (eg com part in google.com)
                    hostname += f'.{part}' # add a dot in front
        else: # if length is 2 (like TestMachine1.12345)
            hostname = splittediporhostname[0] # take front part as hostname
        ip = socket.gethostbyname(hostname) # get IP
    else: # if IP address (192.168.1.1:8080)
        ip = iporhostname.strip('.' + port) # strip off port part
    return ip, port # return end IP and port
