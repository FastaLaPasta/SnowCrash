# Level08

**Box**: SnowCrash

**Name**: Level08

**Category**: Symlink Bypass / File Name Validation Bypass  

**Difficulty**: Easy  

## Analysis

Start by exploring the directory:

```bash
ls -la
```

I find a binary `level08` and a file `token`. The token file contains the password for the next level.

First I get the binary by running:
```bash
scp -P 4242 level08@10.13.250.191:level08 ~/Desktop/
```
Then I decompile it using [dogbolt.org](https://dogbolt.org).

### Vulnerability

The program:
1. Opens the file passed as an argument
2. Explicitly refuses files whose name contains the string "token"
3. The verification is done only on the filename provided, not on the actual file opened by the system

This reveals a classic weakness: the check is done on the filename, but not on the actual destination if it's a symbolic link.

## Exploitation

Create a symbolic link to the token file:

```bash
ln -s /home/user/level08/token /tmp/link
```

Then execute the binary with this link:

```bash
./level08 /tmp/link
```

The program:
- Checks the name `/tmp/link` (which does not contain "token")
- Opens the file pointed to by the symbolic link

The contents of the token file are displayed, giving you the password for the next level.

## Flag

**FLAG_FOUND**

## Vulnerability

**Symlink Bypass / File Name Validation Bypass**

The program only checks the filename provided, which allows bypassing the restriction by using a symbolic link pointing to the forbidden file.