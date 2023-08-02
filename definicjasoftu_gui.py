import sys
import subprocess
import tkinter as tk


def ping(address, count=1):
    cmd = ['ping']
    if sys.platform in ('windows', 'win32'):
        cmd.append('-n')
        print("Platforma: Windows")
    elif sys.platform.startswith('linux'):
        cmd.append('-c')
        print("Platforma: Linux")
    elif sys.platform.startswith('freebsd'):
        cmd.append('-c')
        print("Platforma: FreeBSD")
    elif sys.platform.startswith('darwin'):
        cmd.append('-c')
        print("Platforma: MacosX")

    cmd.append(str(count))
    cmd.append(str(address))
    output = subprocess.check_output(cmd)
    return output


def on_click():
    address = entry.get()
    count = int(spinbox.get())
    result = ping(address, count)
    text.delete('1.0', tk.END)
    text.insert(tk.END, result)


root = tk.Tk()
root.title("Ping")

label1 = tk.Label(root, text="Adres IP:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Liczba pingów:")
label2.grid(row=1, column=0, padx=5, pady=5)

spinbox = tk.Spinbox(root, from_=1, to=10)
spinbox.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Ping", command=on_click)
button.grid(row=2, column=0, padx=5, pady=5)

text = tk.Text(root, width=50, height=10)
text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()