# WRITE UP

**Box**:            SnowCrash

**Name**:           Level01

**Description**:    Find the flag to connect to level01

**Category**:       Forensic

**Difficulty**:     Easy

---

Usual checking:
```bash
ls
```

Oh lord there is a **.pcap** file. (a packet analyzer)
I can only read it, and it's a real mess innit. So i get it into my own computer by running:
```bash
scp -P 4242 level02@10.12.237.184:level02.pcap ~/Desktop/
```

I want to use wireshark (a powerful tool that allow to easly analyze packet in a friendly way) because of it's wonderful UI but because of permission issues, I rather use tshark (less friendly) inside a docker to extract potential data.

(Can run my dockerfile with: **docker build -t tshark . && docker run -it tshark)

Inside of it I first try to read the file:
```bash
tshark -r level02.pcap -z follow,tcp,ascii,0'
```

This way I can see the content from tcp, in ascii format. And I notice a password !!!
The issue now is that there is some character '.' that can either be a real point or a non-representable char as tabulation for example.

To verify the real value of these point I run:
```bash
tshark -r level02.pcap -z follow,tcp,hex,0
```
To get the hexadecimal value of these points, that reveal to be 7f (delete).
after computing all this I finaly get something... And it work!
**FLAG FOUND**
