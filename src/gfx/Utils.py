
def destroyRecursively(frame):
    for c in frame.winfo_children():
        destroyRecursively(c)
    frame.destroy()

