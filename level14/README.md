# Level14

**Box**: SnowCrash

**Name**: Level14

**Category**: Reverse Engineering / Anti-Debug Bypass + UID Check

**Difficulty**: Medium

## Analysis

Explore the directory:

```bash
ls -la
```

Unlike previous levels, there is **no exploitable file**. The only interesting program is:

```bash
getflag
```

Try to execute it:

```bash
getflag
```

The program displays:

```
Check flag.Here is your token :
Nope there is no token here for you sorry. Try again :)
```

The program refuses to give the flag.

## Binary Analysis

Since there is no script to exploit, we need to **analyze the binary** using a debugger:

```bash
gdb /bin/getflag
```

In GDB, we can:
- Run the program
- Analyze its assembly code
- Modify registers during execution

Display the assembly code of the main function:

```bash
disas main
```

We quickly notice an important instruction:

```asm
call ptrace
```

This means the program checks **if someone is trying to debug it**. This is an **anti-debug protection**.

## Bypass Anti-Debug Protection

Set a breakpoint right after the `ptrace` call:

```bash
break *0x0804898e
```

Then run the program:

```bash
run
```

When execution stops, modify the `eax` register:

```bash
set $eax=0
```

This makes the program believe that `ptrace` succeeded.

Continue execution:

```bash
continue
```

The program now passes the anti-debug protection.

## Find the Program Logic

Continuing the analysis of the assembly code, we find:

```asm
call getuid
```

The program retrieves **the UID of the current user**.

Then we see a series of comparisons:

```asm
cmp $0xbb8,%eax
cmp $0xbba,%eax
cmp $0xbbc,%eax
...
```

This means **the program chooses the flag based on the UID**.

## Find the Correct UID

To know which UID corresponds to system users, look at the file:

```bash
cat /etc/passwd | grep level
```

We get a list like:

```
level00:x:3000
level01:x:3001
level02:x:3002
...
level14:x:3014
```

So:

```
level14 → UID 3014
```

If the program believes our UID is **3014**, it will display the flag.

## Modify UID in GDB

Set a breakpoint right after `getuid`:

```bash
break *0x08048b02
```

Then restart the program:

```bash
run
```

After bypassing `ptrace` again, execution stops at the breakpoint.

Modify the value returned by `getuid`:

```bash
set $eax=3014
```

Then continue:

```bash
continue
```

## Result

The program now thinks our UID is **3014**, so it displays:

```
Check flag.Here is your token :
<FLAG>
```

The token for the next level is obtained.

## Conclusion

The binary implements two layers of protection:
1. **Anti-debug**: Uses `ptrace` to detect if being debugged
2. **UID-based flag selection**: The displayed flag depends on the user's UID

By bypassing both protections in GDB (setting `eax=0` after `ptrace` and `eax=3014` after `getuid`), we can obtain the flag.

## Flag

**FLAG_FOUND**