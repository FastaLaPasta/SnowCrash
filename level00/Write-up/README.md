# WRITE UP

**Box**:            SnowCrash

**Name**:           Level00

**Description**:    Find the flag to connect to level01

**Category**:       Cryptographie

**Difficulty**:     Easy

---

At first I don't really know what I'm looking for, after some researche i've figured that flag can be found in files or in specific services we can access thanks to open ports.

So I basicly run
```bash
nmap 
```
It result in a command not found, so i start looking for files.

```bash
find -iname password
```
```bash
find -iname flag00
```
and
```bash
grep -R "password" <directory>
```

But I faced several permission denied with a lot of file and directory (to much)

So I've tried to look for the users

```bash
cat /etc/passwd/
```

I then see that there is a flag00 User so i look if I could find some file own by this user (flag00)

```bash
find / -user flag00 2>/dev/null/
```

I find 2 of them then look into one of these by:

```bash
cat /usr/bin/john
```

**FLAG FOUNDED**

IT DOESN'T WORK !! Oh lord.
---

We just need to decrypt it on [decrypter](https://www.dcode.fr/chiffre-cesar)


## And we're done !
