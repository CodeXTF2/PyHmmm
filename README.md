# PyHmmm
<p align="center">
<img src="pyhmmm.png" width="300" height="300">
</p>

## What is this?
This is a third party agent for Havoc C2 written in python. It is intended to be a basic PoC used to learn how to write custom Havoc agents, with its accompanying blog post https://codex-7.gitbook.io/codexs-terminal-window/red-team/red-team-dev/extending-havoc-c2/third-party-agents

## Features
It currently only supports 2 commands:
- shell {system command}
- exit

It is *not* meant to be OPSEC safe or safe to use in real life. It was meant to be used to learn the Havoc agent spec. I am working on an improved version that is safer to use in real environments (encrypted comms etc.) and that will be linked here when it's done.

## Usage
1. start Havoc teamserver
2. python handler.py
3. python agent.py

Be sure to manually modify the ip address and port in the agent manually, I didn't write the GUI auto generator script yet ;-;

## Why did you name it this? This is a dumb name!
I literally could not think of a name and it was like 2 minutes to Havoc drop. Decided to name it after a funny emote.
![image](https://user-images.githubusercontent.com/29991665/193332178-506de9b7-160f-46da-9be7-e76446c8b729.png)


Have fun
~ CodeX
