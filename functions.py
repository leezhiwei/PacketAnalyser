import socket
import os
import signal

def endproc(signum, frame, pidtcpdump):
    os.killpg(os.getpgid(pidtcpdump), signal.SIGTERM) # function in case you CTRL + C ends tcpdump gracefully

def resolvehostname(iporhostname, ping): # resolve into IP if hostname
    splittediporhostname = iporhostname.split('.') # split into list
    if ping: # if ICMP/Ping request
        for p in splittediporhostname: # try to see if IP
            try:
                int(p) # try to turn to int
            except:
                ip = socket.gethostbyname(iporhostname) # if not get IP
                port = "ICMP" # set port to ICMP or ping
                return ip, port # return values
        ip = iporhostname # if able to complete loop, put in initial IP
        port = "ICMP" # set port to ICMP
        return ip, port # return vals
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
        ip = iporhostname.replace('.' + port, "") # strip off port part
        for p in ip.split('.'): # if multi part hostname (eg AWS)
            try:
                int(p) # try to turn into int()
            except:
                ip = socket.gethostbyname(ip) # resolve host name
                break # break out
    return ip, port # return end IP and port