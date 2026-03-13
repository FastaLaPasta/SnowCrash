# Level09

**Box**: SnowCrash

**Name**: Level09

**Category**: Reverse Engineering / Encoding  

**Difficulty**: Medium  

## Analysis

Start by exploring the directory:

```bash
ls -la
```

I find a binary `level09` and a file `token`. The token file contains encoded data that needs to be decoded.

First I get the binary by running:
```bash
scp -P 4242 level09@10.13.250.191:level09 ~/Desktop/
```
Then I decompile it using [dogbolt.org](https://dogbolt.org).

### Vulnerability

The program:
1. Checks if the program is being debugged or manipulated via LD_PRELOAD
2. Accepts exactly one argument
3. Applies a transformation on each character of the argument: `output[i] = input[i] + i`

The token file contains encoded data - it's not directly readable with `cat`.

## Exploitation

The program encodes each byte by adding its index. To retrieve the real token, we apply the inverse:

```
decoded[i] = encoded[i] - i
```
So I retrieve the token file with:
```bash
scp -P 4242 level09@10.13.250.191:token ~/Desktop/
chmod 777 ~/Desktop/token
```
Write a Python script to decode the token file:

```python
data = open("token","rb").read()
decoded = bytes([(b - i) % 256 for i,b in enumerate(data)])
print(decoded.decode('utf-8', errors='ignore'))
```

This method reproduces exactly the inverse logic of the binary. Non-printable characters are correctly transformed.

The script displays the actual contents of the token: the flag for level 09.

## Flag

**FLAG_FOUND**

