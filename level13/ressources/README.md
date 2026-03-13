# Level13

**Box**: SnowCrash

**Name**: Level13

**Category**: Reverse Engineering / UID Check Bypass

**Difficulty**: Medium

## Analysis

Explore the directory:

```bash
ls -la
```

I find a binary named `level13`. The objective is to get the flag.

Try to execute it:

```bash
./level13
```

The program displays:

```
UID XXX started us but we expect 4242
```

This means the program checks that the user executing it has UID 4242.

## Binary Analysis

Decompile the binary with my [decompiler](https://dogbolt.org) to understand its behavior.

In the `main` function, we observe:

```c
if (getuid() != 4242) {
    printf("UID %d started us but we expect %d\n", ...);
    exit(1);
}
```

So the program refuses to execute if the user does not have UID 4242.

However, if the condition is met, the program calls the function:

```c
ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I")
```

And displays the result as the token.

## Algorithm Understanding

The `ft_des()` function applies a character-by-character transformation to the string:

```
boe]!ai0FB@.:|L6l@A?>qJ}I
```

This is a custom encryption algorithm.

## Exploitation Strategy

Instead of trying to execute the binary with UID 4242, we reproduce the algorithm in a Python script.

This script applies the same operations as the `ft_des()` function to the given string.


## Conclusion

The binary checks for a specific UID (4242) before executing its core logic. By reverse engineering the encryption algorithm used in `ft_des()`, we can compute the token without needing to bypass the UID check.

## Flag

**FLAG_FOUND**
