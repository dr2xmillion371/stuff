import tkinter as tk

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 

root = tk.Tk()
root.title("number counter")
label = tk.Label(root, fg="blue")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
