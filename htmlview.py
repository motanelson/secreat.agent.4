import os 
import copy
import tkinter as tk
from tkinter import font
import subprocess
class tApp:
    def __init__(self, root,texts,titles):
        self.root = root
        self.root.title(titles)
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        # Frame com barra de scroll
        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(fill="both", expand=True)

        # Canvas para desenhar texto
        self.canvas = tk.Canvas(self.frame, bg="white", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Barra de scroll vertical
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Fonte
        self.font = font.Font(family="Courier", size=16)
        ff=texts.split("\n")
        y=20
        for t in ff:
            tt=self.canvas.create_text(10, y, text=t, anchor="nw", font=self.font, fill="red")
            y=y+16
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Scroll automático para o fim
        self.canvas.yview_moveto(1.0)

print("\033c\033[47;31m\ngive me a html file to view ? \n")
a=input().strip()
tyy=a
f1=open(a,"r")
f=f1.read()
f1.close()
sss=f.find("<body")
if sss<0:
    sss=f.find("<BODY")
if sss>-1:
    f=f[sss:]
sss=f.find("</body")
if sss<0:
    sss=f.find("</BODY")
if sss>-1:
    f=f[:sss]
f=f.replace("\r\n","")
f=f.replace("\n","")
f=f.replace("\r","")
f=f.replace("  "," ")
f=f.replace("<br>","\r\n")
f=f.replace("<BR>","\r\n")
f=f.replace("<p","\r\n<")
f=f.replace("</p","\r\n<")
f=f.replace("<P","\r\n<")
f=f.replace("</P","\r\n<")
ff=f.split("<")
ddf=""
for d in ff:
    d=d.strip()
    dd=d.split(">")
    if len(dd)>1:
        if dd[1].strip()!="":
            ddf=ddf+dd[1].strip()+" "

root = tk.Tk()

app = tApp(root,ddf,tyy)
root.mainloop()