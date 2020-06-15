import Tkinter as tk

root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

image_file = 'splash screen.gif'
#assert os.path.exists(image_file)
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

# show the splash screen for 5000 milliseconds then destroy
root.after(5000, root.destroy)
root.mainloop()
exec(open("clientgui.py").read())