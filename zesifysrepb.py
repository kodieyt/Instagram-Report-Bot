
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import requests
import uuid
from time import sleep
import json
done = 1
r = requests.Session()
uid = uuid.uuid4()
main=Tk()
style = ttk.Style()
main.configure(background='blue')
main.geometry("400x200+550+300")
main.resizable(False,False)
main.title("ZESIFYS REPORT-BOT")
style.theme_use("classic")
style.configure('TButton',foreground='white',background='blue')
euser = StringVar()
epass = StringVar()
userl = ttk.Label(main,text="username:",foreground='white',background='blue',font='elvetica 12').grid(row=1,column=2, pady=10)
enuserr = ttk.Entry(main, width=30,textvariable=euser,font='Helvetica, 10')
enuserr.grid(row=1,column=3, pady=10)
passl = ttk.Label(main,text="password:",foreground='white',background='blue',font='Helvetica 12').grid(row=2,column=2, pady=10)
enpass = ttk.Entry(main, width=30,textvariable=epass,font='Helvetica, 10')
enpass.grid(row=2,column=3, pady=10)
bnlogin = ttk.Button(main,text="login")
bnlogin.grid(row=3,column=3)
bnlogin.config(command=lambda : login())
sTr = StringVar()
sSle = IntVar()
ssleep = IntVar()
laspams = ttk.Label(main,textvariable=ssleep,background='blue',foreground='white')
laspams.grid(row=6,column=4)
ltar = ttk.Label(main, text='target:', foreground='white', background='blue',font='Helvetica, 12').grid(row=5, column=1)
entar = ttk.Entry(main, width=15, textvariable=sTr,font='Helvetica, 9').grid(row=5, column=2)
lsle = ttk.Label(main, text='sleep:', foreground='white', background='blue',font='Helvetica, 12').grid(row=6, column=1)
esle = ttk.Entry(main, width=15, textvariable=sSle,font='Helvetica, 9').grid(row=6, column=2)
btnspam = ttk.Button(main, text="start")
btnspam.grid(row=6, column=3)
btnspam.configure(command=lambda: reports())
#================================================

def login():
    user = euser.get()
    password = epass.get()
    url = "https://i.instagram.com/api/v1/accounts/login/"

    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com'
    }

    data = {
        '_uuid': uid,
        'username': user,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }
    loginreq = r.post(url, data=data, headers=headers, allow_redirects=True)
    if ("logged_in_user") in loginreq.text:
        tkinter.messagebox.showinfo('login respone','login true')
        bnlogin.config(state='disabled')
        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
    else:
        tkinter.messagebox.showinfo('login response', 'login faild!')

#=========================================
def reports():
    global done
    target = sTr.get()
    sle = sSle.get()
    url_id = "https://www.instagram.com/{}/?__a=1".format(target)
    url_get_user_id = r.get(url_id).json()
    user_id = str(url_get_user_id.get("logging_page_id"))
    your_user_id = str(user_id.split("_")[1])
    urlRep = "https://i.instagram.com/users/" + your_user_id + "/report/"
    datas = {
            'source_name': '', 'reason_id': 1, 'frx_context': ''  # Spam
            }
    req_SessionID = r.post(urlRep, data=datas)
    ssleep.set(done)
    done += 1
    laspams.after(sle,reports)
main=mainloop()
