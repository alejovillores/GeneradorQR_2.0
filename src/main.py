import qr_object
import tkinter as tk
from PIL import ImageTk, Image

def generar(url):
    qr = qr_object.QRObject()

    qr.set_data(url)
    img = qr.get_qr()
    img.save('../img/qr.png')
    
    img.show()
    




def main():
    #Tk config
    root = tk.Tk()
    root.geometry("400x400")
    root.title('Qr Generator')

    try:
        img = ImageTk.PhotoImage(Image.open('../img/qr.png'))
        label = tk.Label(root,image = img)
        label.pack()
    except:
        label = tk.Label(root,text ="No hay img")
        label.pack()

    url_label = tk.Label(root,text = 'URL',)
    url_label.pack()
    url = tk.Entry(root,width = 50)
    url.pack()

       
    btn = tk.Button(root,text = 'generar',command = lambda: generar(url.get()))
    btn.pack()
    
    root.mainloop()


main()