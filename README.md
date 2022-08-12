# sar
This PoC was created while working on the Sar machine in the OFFSEC Proving Grounds Play.
The idea stems from the exploit titled Sar2HTML 3.2.1 - Remote Command Execution (https://www.exploit-db.com/exploits/47204).


# How to use?
Save the script as sar.py. Then run it from command line.
![image](https://user-images.githubusercontent.com/110873255/184284767-29ea44ec-aaec-4ecd-8ccd-41f6bc02d9fd.png)


The IP address and port in the URL is not hardcoded for ease of use. Please make sure you put your target IP in the command line. After you run it, the command prompt will become kali@kali. 


![image](https://user-images.githubusercontent.com/110873255/184284839-ecb7b5d4-b203-43f0-8cd1-d6caf446d8aa.png)


From here, you can do your thang.

![image](https://user-images.githubusercontent.com/110873255/184286617-a1f51365-e073-4032-b2a6-69ef33bf3d11.png)




# How it works?
Sar2HTML v3.2.1 has a command injection vulnerability in the 'plot' parameter of the web application. This script exploits the vulnerability to execute commands on the target. 

Sar2HTML does not validate user input when processing the $plot variable before passing it to PHP's exec function.  

![image](https://user-images.githubusercontent.com/110873255/184285985-758d3e4f-9722-4356-8344-277f250d6193.png)





This is one of my first attempts at this so please be nice :)
