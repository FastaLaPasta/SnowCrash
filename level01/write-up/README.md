# WRITE UP

**Box**:            SnowCrash

**Name**:           Level01

**Description**:    Find the flag to connect to level01

**Category**:       Cryptographie

**Difficulty**:     Easy

---

I know i'm looking for a file within there is my flag, it can be located inside a service or on directly on the box so I first try to look for open port:

```bash
nmap
```

It result by a **command not found** so i'm pretty (we could have put a dot here) sure I have to find it directly on the machine.

---

I Look for the users know by the system by running:
```bash
cat /etc/passwd
```
and have noticed that the line attribute to the flag01 user contain a weird sequence of character:
```
flag00:x:3000:3000::/home/flag/flag00:/bin/bash
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
flag02:x:3002:3002::/home/flag/flag02:/bin/bash
```

(The interesting part is **flag01:42hDRfypTqqnw**)

I tried to decrypt it with my dear [decrypter](https://www.dcode.fr/).
It recommended me to try **Base_58** but it gives nothing relevant.

After some research i've found that password can be stocked **hashed**, so if I have the right key I can find the right password. But it would take at least hundreds of tries. So let's use a specific tools for that **john**.

I basicly run a debian docker image within I create a file with my hashed password (and install john)
```bash
echo <hash password> > hash.txt
```

Then I run:
```bash
./john --show <path/to/hash.txt>
```

And YEAAAAAH it gives me something.
**FLAG FOUNDED**