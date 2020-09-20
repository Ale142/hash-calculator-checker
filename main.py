#!/usr/local/bin/python3
import tkinter as tk
import hashlib
from tkinter.filedialog import askopenfilename
from tkinter import ttk,messagebox,Toplevel

window = tk.Tk()
window.title("H4$H")
window.rowconfigure([0,1,2,3],minsize=50,weight=1)
window.columnconfigure(0, minsize=50,weight=1)

labelFileName = tk.Label(master=window)

hashType = ttk.Combobox(master=window, width=15, state = "readonly")
hashType["values"] = ["SHA1","SHA256","SHA512", "MD5"]
hashType.set("SHA1")

labelHashCalculated = tk.Text(master=window,height = 1, borderwidth=1)


name = ""

def checkEqual(hash1,hash2,label):
    if hash1 == hash2:
        label["text"] = "Equals"
    else:
        label["text"] = "Not equals"

def openCheckWindow():
    checkWindow = Toplevel(window)
    checkWindow.title("Check")
    checkWindow.geometry("500x200")
    checkWindow.rowconfigure([0,1,2,3],minsize = 30,weight = 1)
    checkWindow.columnconfigure(0, minsize=50, weight = 1)

    labelResultEqual = tk.Label(master=checkWindow)
    labelResultEqual.grid(row=3,column=0)

    firstHash = tk.Entry(master=checkWindow,borderwidth = 1)
    firstHash.grid(row = 0,column = 0,sticky="ew")

    secondHash = tk.Entry(master=checkWindow,borderwidth = 1)
    secondHash.grid(row=1,column=0, sticky="ew")

    btn_check = tk.Button(master=checkWindow,text="Check!",command = lambda: checkEqual(firstHash.get(),secondHash.get(),labelResultEqual))
    btn_check.grid(row=2,column=0)







def openFile():
    global name,labelFileName
    name = askopenfilename(initialdir="/Users/alessandrobacci/Desktop/", title="Choose file")
    labelFileName["text"] = name

def calculateHash():
    global hashType,labelHashCalculated
    hash = hashType.get()
    if name != "":
        f = open(name, "rb")
        f_bytes = f.read()

        hex_hash = ""
        if hash == "SHA256":
            hex_hash = hashlib.sha256(f_bytes).hexdigest()

        elif hash == "MD5":
            hex_hash = hashlib.md5(f_bytes).hexdigest()
        elif hash == "SHA1":
            hex_hash = hashlib.sha1(f_bytes).hexdigest()
        elif hash == "SHA512":
            hex_hash = hashlib.sha512(f_bytes).hexdigest()
        labelHashCalculated.insert(1.0,hex_hash)
    else:
        messagebox.showerror("Error", "Open file first")




# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    button = tk.Button(master=window, text = "Open file", command=openFile)
    button.grid(row=0,column=0, columnspan = 2)
    print(name)

    hashType.grid(row=1,column=1)
    labelFileName.grid(row=1, column=0)

    btn_calculate = tk.Button(master=window, text="Calculate", command = calculateHash)
    btn_calculate.grid(row=2, column=0,columnspan = 2)

    labelHashCalculated.grid(row=3,column=0,columnspan = 2)

    btn_equal = tk.Button(master=window, text="Check", command=openCheckWindow)
    btn_equal.grid(row=4,column=0,columnspan = 2)
    window.mainloop()

