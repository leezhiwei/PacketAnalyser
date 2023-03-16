import signal
import subprocess as sub # importing modules
from functions import *

interface = 'wlp2s0' # set interface eg tun0, wlan0, eth0 etc
p = sub.Popen(('sudo', 'tcpdump', '-l', '-i', interface), stdout=sub.PIPE) # open tcpdump with a subprocess
pidtcpdump = p.pid # set the PID of tcpdump

signal.signal(signal.SIGINT, lambda signum, frame: endproc(signum, frame, pidtcpdump)) # when you CTRL+C will run this

for row in iter(p.stdout.readline, b''): # for each row written to STDOUT for TcpDump
    row = row.rstrip().decode('utf-8') # decode bytes into string 
    splitted = row.split(' ') # split by space
    if 'IP' in splitted: # if IP stuff happens
        ipindex = splitted.index('IP') # get index of IP
        srciporhostname = splitted[ipindex + 1] # fixed for now (source IP)
        destiporhostname = splitted[ipindex + 3] # fixed for now (destination IP)
        proto = splitted[ipindex + 4] # protocol like TCP/UDP
        length = splitted[-1] # get length from last index
        srcip, srcport = resolvehostname(srciporhostname) # use function to get src IP and Port
        destip, destport = resolvehostname(destiporhostname) # use function to get dest IP and Port
        print(f'Source IP: {srcip}, Source Port: {srcport}, Destination IP: {destip}, Destination Port: {destport}, Protocol: {proto}, Length : {length}')
        # print out info