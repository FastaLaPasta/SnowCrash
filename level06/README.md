# Level06

**Box**: SnowCrash


**Name**: Level06

**Category**: Code Execution / PHP  

**Difficulty**: Easy  

## Analysis

Start by exploring the directory:

```bash
ls -la
```

You'll find two files:
- `level06` - A compiled Linux executable
- `level06.php` - The source PHP script

The PHP script header `#!/usr/bin/php` indicates it can be executed directly as a binary.

### Vulnerability

The script performs string replacements on an input file, then uses the `/e` modifier in `preg_replace()`, which allows **code execution** on the replaced string. This is a critical vulnerability - user-controlled input gets evaluated as PHP code.

## Exploitation

Create a malicious file that exploits the preg_replace code execution:

```bash
echo '[x ${`/bin/getflag`} ]' > /tmp/exploit.sh
```

Run the exploit:

```bash
./level06 /tmp/exploit.sh
```

This triggers the vulnerability - the `${...}` syntax executes the enclosed command, and the `/e` modifier evaluates it as PHP code, giving you the flag.

## Flag

**FLAG FOUND**
