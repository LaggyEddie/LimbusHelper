import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Limbus Helper")
root.geometry("800x600")

root.tk.call("source", "Azure/azure.tcl")
root.tk.call("set_theme", "dark")

sidePanelColor = '#383838'

# icons
def sidePanelIcons(path):
    originalImage = Image.open(path)
    resizedImage = originalImage.resize((40, 40), Image.Resampling.LANCZOS) 
    return ImageTk.PhotoImage(resizedImage)

menuIcon = sidePanelIcons("img/menu.png")
closeIcon = sidePanelIcons("img/close.png")

enkephalinIcon = sidePanelIcons("img/enkephalin.png")
moduleIcon = sidePanelIcons("img/module.png")
crateIcon = sidePanelIcons("img/crate.png")
sinnerIcon = sidePanelIcons("img/sinner.png")

# pages    
def enkephalinRecharge():
    enkephalinRechargeFm = tk.Frame(pageFrame)
    lb = tk.Label(enkephalinRechargeFm, text="Enkephalin recharge", font=('Bold', 20))
    lb.place(x=100, y=200)
    enkephalinRechargeFm.pack(fill=tk.BOTH, expand=True)
    # print("Enkephalin recharge")

def modulesExchange():
    modulesExchangeFm = tk.Frame(pageFrame)
    lb = tk.Label(modulesExchangeFm, text="Modules exchange", font=('Bold', 20))
    lb.place(x=100, y=200)
    modulesExchangeFm.pack(fill=tk.BOTH, expand=True)
    
def cratesEstimator():
    cratesEstimatorFm = tk.Frame(pageFrame)
    lb = tk.Label(cratesEstimatorFm, text="Crates Estimator", font=('Bold', 20))
    lb.place(x=100, y=200)
    cratesEstimatorFm.pack(fill=tk.BOTH, expand=True)
    
def sinner():
    sinnerFm = tk.Frame(pageFrame)
    lb = tk.Label(sinnerFm, text="Sinner", font=('Bold', 20))
    lb.place(x=100, y=200)
    sinnerFm.pack(fill=tk.BOTH, expand=True)
    
pageFrame = tk.Frame(root)
pageFrame.place(relwidth=1.0, relheight=1.0, x=55)
enkephalinRecharge()


# side panel
def switchIndication(indicatorLb, page):
    for indicator in [enkephalinBtnIndicator, moduleBtnIndicator, crateBtnIndicator, sinnerBtnIndicator]:
        indicator.config(bg=sidePanelColor)
    indicatorLb.config(bg="white")
    if sidePanelFrame.winfo_width() > 50:
        shrinkSidePanel()
    for frame in pageFrame.winfo_children():
        frame.destroy()
    page()
    
def extendingAnimation():
    currentWidth = sidePanelFrame.winfo_width()
    if currentWidth < 250:
        currentWidth += 10
        sidePanelFrame.config(width=currentWidth)
        root.after(ms=6, func=extendingAnimation)    

def extendSidePanel():
    extendingAnimation()
    menuBtn.config(image=closeIcon, command=shrinkSidePanel)
    
    
def shrinkingAnimation():
    currentWidth = sidePanelFrame.winfo_width()
    if currentWidth != 50:
        currentWidth -= 10
        sidePanelFrame.config(width=currentWidth)
        root.after(ms=6, func=shrinkingAnimation)

def shrinkSidePanel():
    shrinkingAnimation()
    menuBtn.config(image=menuIcon, command=extendSidePanel)

sidePanelFrame = tk.Frame(root, bg=sidePanelColor)

# side panel buttons
menuBtn = tk.Button(sidePanelFrame, image=menuIcon, bg=sidePanelColor, bd=0, activebackground=sidePanelColor, command=extendSidePanel)
menuBtn.place(x=3, y=10)

enkephalinBtn = tk.Button(sidePanelFrame, image=enkephalinIcon, bg=sidePanelColor, bd=0, activebackground=sidePanelColor,command=lambda: switchIndication(indicatorLb=enkephalinBtnIndicator, page=enkephalinRecharge))
enkephalinBtn.place(x=6, y=130)
enkephalinBtnIndicator = tk.Label(sidePanelFrame, bg="white")
enkephalinBtnIndicator.place(x=3, y=135, height=30, width=3)
enkephalinLb = tk.Label(sidePanelFrame, text="Enkephalin recharge", bg=sidePanelColor, fg="white", font=("Bold", 15), anchor=tk.W)
enkephalinLb.place(x=50, y=130, width=200, height=40)
enkephalinLb.bind("<Button-1>", lambda e: switchIndication(indicatorLb=enkephalinBtnIndicator, page=enkephalinRecharge))

moduleBtn = tk.Button(sidePanelFrame, image=moduleIcon, bg=sidePanelColor, bd=0, activebackground=sidePanelColor, command=lambda: switchIndication(indicatorLb=moduleBtnIndicator, page=modulesExchange))
moduleBtn.place(x=6, y=180)
moduleBtnIndicator = tk.Label(sidePanelFrame, bg=sidePanelColor)
moduleBtnIndicator.place(x=3, y=185, height=30, width=3)
moduleLb = tk.Label(sidePanelFrame, text="Modules exchange", bg=sidePanelColor, fg="white", font=("Bold", 15), anchor=tk.W)
moduleLb.place(x=50, y=180, width=200, height=40)
moduleLb.bind("<Button-1>", lambda e: switchIndication(indicatorLb=moduleBtnIndicator, page=modulesExchange))

crateBtn = tk.Button(sidePanelFrame, image=crateIcon, bg=sidePanelColor, bd=0, activebackground=sidePanelColor,command=lambda: switchIndication(indicatorLb=crateBtnIndicator, page=cratesEstimator))
crateBtn.place(x=6, y=230)
crateBtnIndicator = tk.Label(sidePanelFrame, bg=sidePanelColor)
crateBtnIndicator.place(x=3, y=235, height=30, width=3)
crateLb = tk.Label(sidePanelFrame, text="Crates Estimator", bg=sidePanelColor, fg="white", font=("Bold", 15), anchor=tk.W)
crateLb.place(x=50, y=230, width=200, height=40)
crateLb.bind("<Button-1>", lambda e: switchIndication(indicatorLb=crateBtnIndicator, page=cratesEstimator))

sinnerBtn = tk.Button(sidePanelFrame, image=sinnerIcon, bg=sidePanelColor, bd=0, activebackground=sidePanelColor, command=lambda: switchIndication(indicatorLb=sinnerBtnIndicator, page=sinner))
sinnerBtn.place(x=6, y=280)
sinnerBtnIndicator = tk.Label(sidePanelFrame, bg=sidePanelColor)
sinnerBtnIndicator.place(x=3, y=285, height=30, width=3)
sinnerLb = tk.Label(sidePanelFrame, text="Sinner (maybe)", bg=sidePanelColor, fg="white", font=("Bold", 15), anchor=tk.W)
sinnerLb.place(x=50, y=280, width=200, height=40)
sinnerLb.bind("<Button-1>", lambda e: switchIndication(indicatorLb=sinnerBtnIndicator, page=sinner))

# panel frame
sidePanelFrame.pack(side=tk.LEFT, fill=tk.Y)
sidePanelFrame.pack_propagate(False)

sidePanelFrame.configure(width=50)
root.mainloop()