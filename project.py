from tkinter import *
import threading

root = Tk()
root.title('Clicker')
root.geometry('700x700')
root.configure(background="white")


StartLabel = Label(root, text="Go to full screen and press ENTER to get to the 2 level!",
                   bg="white", fg="red", font=("Helvetica", 16))
StartLabel.pack()


ClickerImage = PhotoImage(file="Welcome.gif")
Yan2 = PhotoImage(file="YAN2.gif")
Yan3 = PhotoImage(file="YAN3.gif")
Yan4 = PhotoImage(file="YAN4.gif")
Yan5 = PhotoImage(file="YAN5.gif")
Yan6 = PhotoImage(file="YAN6.gif")
Yan7 = PhotoImage(file="YAN7.gif")
Yan8 = PhotoImage(file="YAN8.gif")
Yan9 = PhotoImage(file="YAN9.gif")
Yan10 = PhotoImage(file="YAN10.gif")
lvl1 = Label(root, image=ClickerImage, bg="black")
lvl2 = Label(root, image=Yan2, bg="black")
lvl3 = Label(root, image=Yan3, bg="black")
lvl4 = Label(root, image=Yan4, bg="black")
lvl5 = Label(root, image=Yan5, bg="black")
lvl6 = Label(root, image=Yan6, bg="black")
lvl7 = Label(root, image=Yan7, bg="black")
lvl8 = Label(root, image=Yan8, bg="black")
lvl9 = Label(root, image=Yan9, bg="black")
lvl10 = Label(root, image=Yan10, bg="black")


score = 0
level = 1
currentImage = lvl1

autoClickers = 1
multipleClickers = 1

ClickerLabel = Label(root, text="Points:" + str(score),
                     bg="white", fg="green", font=("Helvetica", 14))
LevelLabel = Label(root, text="Level:" + str(level),
                   bg="white", fg="green", font=("Helvetica", 14))


gameFinished = False

priceArray = [0, 0, 300, 1500, 12000, 78000, 630000,
              3600000, 18000000, 96000000, 1999999999]
photosArray = [0, 0, Yan2, Yan3, Yan4, Yan5, Yan6, Yan7, Yan8, Yan9, Yan10]


def level_button():
    global score
    global level
    if score >= priceArray[level + 1]:
        currentImage.config(image=photosArray[level + 1])
        level += 1
        score -= priceArray[level]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
        if level == 1:
            StartLabel.config(text="Press ENTER to get YAN out of bed!")
        elif level == 5:
            StartLabel.config(text="You are in the middle of the road!")
        elif level == 9:
            StartLabel.config(text="You are gonna need the last portion of patience!")
        elif level == 10:
            StartLabel.config(text="Very well done!!!")
            levelButton.destroy()


def multiclick_button():
    global score
    global level
    global multipleClickers
    if score >= priceArray[multipleClickers + 1] and level > multipleClickers:
        multipleClickers += 1
        score -= priceArray[multipleClickers]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
        if level == 10:
            multiClickButton.destroy()


def click():
    if not gameFinished:
        def raisingscore():
            global score
            global autoClickers
            score += (autoClickers - 1)**5
            ClickerLabel.config(text="Points:" + str(score))
        threading.Timer(1, click).start()
        raisingscore()


def autoclick_button():
    global score
    global level
    global autoClickers
    if score >= priceArray[autoClickers + 1] and level > autoClickers:
        autoClickers += 1
        score -= priceArray[autoClickers]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1) ** 5))
        threading.Timer(1, click).start()
        if level == 10:
            autoClickButton.destroy()


def quit_button():
    global gameFinished
    gameFinished = True
    root.destroy()


levelButton = Button(root, text="Next level", font=("Helvetica", 14),
                     bg="white", fg="black", command=level_button)


def lvl_color_button():
    global score
    global level
    if score >= priceArray[level + 1]:
        levelButton.config(bg="yellow")
    else:
        levelButton.config(bg="white")


multiClickButton = Button(root, text="MultipleClicker X" + str(multipleClickers),
                          font=("Helvetica", 14), bg="white", fg="black",
                          command=multiclick_button)


def multiclick_color_button():
    global score
    global level
    global multipleClickers
    if multipleClickers < level and score >= priceArray[multipleClickers + 1]:
        multiClickButton.config(text="MultipleClickers", bg="orange")
    else:
        if multipleClickers == level:
            multiClickButton.config(text="Next level required")
        else:
            multiClickButton.config(text=str(-priceArray[multipleClickers + 1] + score))
        multiClickButton.config(bg="white")


autoClickButton = Button(root, text="AutoClickers X" + str((autoClickers - 1)**5),
                         bg="white", fg="black", font=("Helvetica", 14),
                         command=autoclick_button)


def autoclick_color_button():
    global score
    global level
    global autoClickers
    if autoClickers < level and score >= priceArray[autoClickers + 1]:
        autoClickButton.config(text="AutoClickers", bg="orange")
    else:
        if autoClickers == level:
            autoClickButton.config(text="Next level required")
        else:
            autoClickButton.config(text=str(-priceArray[autoClickers + 1] + score))
        autoClickButton.config(bg="white")


quitButton = Button(root, text="Quit the game", bg="red", fg="black",
                    font=("Helvetica", 14), command=quit_button)


def game(event):
    global score
    global level
    global multipleClickers
    global multiClickButton
    global levelButton
    lvl_color_button()
    multiclick_color_button()
    autoclick_color_button()
    score += multipleClickers ** 3
    ClickerLabel.config(text="Points:" + str(score))
    levelButton.pack()
    multiClickButton.place(x=1, y=240)
    autoClickButton.place(x=1195, y=240)
    quitButton.place(x=1, y=660)


ClickerLabel.pack()
LevelLabel.pack()
currentImage.pack()

root.bind('<Return>', game)
root.mainloop()
