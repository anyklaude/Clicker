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


def level_button():
    global score
    global level
    if level == 1 and score >= priceArray[2]:
        currentImage.config(image=Yan2)
        level += 1
        score -= priceArray[2]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
        StartLabel.config(text="Press ENTER to get YAN out of bed!")
    elif level == 2 and score >= priceArray[3]:
        currentImage.config(image=Yan3)
        level += 1
        score -= priceArray[3]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
    elif level == 3 and score >= priceArray[4]:
        currentImage.config(image=Yan4)
        level += 1
        score -= priceArray[4]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
    elif level == 4 and score >= priceArray[5]:
        currentImage.config(image=Yan5)
        level += 1
        score -= priceArray[5]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
        StartLabel.config(text="You are in the middle of the road!")
    elif level == 5 and score >= priceArray[6]:
        currentImage.config(image=Yan6)
        level += 1
        score -= priceArray[6]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
    elif level == 6 and score >= priceArray[7]:
        currentImage.config(image=Yan7)
        level += 1
        score -= priceArray[7]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
    elif level == 7 and score >= priceArray[8]:
        currentImage.config(image=Yan8)
        level += 1
        score -= priceArray[8]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
    elif level == 8 and score >= priceArray[9]:
        currentImage.config(image=Yan9)
        level += 1
        score -= priceArray[9]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
        StartLabel.config(text="You are gonna need the last portion of patience!")
    elif level == 9 and score >= priceArray[10]:
        StartLabel.config(text="Very well done!!!")
        currentImage.config(image=Yan10)
        level += 1
        score -= priceArray[10]
        LevelLabel.config(text="Level:" + str(level))
        ClickerLabel.config(text="Points:" + str(score))
        levelButton.destroy()


def multiclick_button():
    global score
    global level
    global multipleClickers
    if multipleClickers == 1 and score >= priceArray[2] and level > 1:
        multipleClickers *= 2
        score -= priceArray[2]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 2 and score >= priceArray[3] and level > 2:
        multipleClickers *= 2
        score -= priceArray[3]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 3 and score >= priceArray[4] and level > 3:
        multipleClickers *= 2
        score -= priceArray[4]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 4 and score >= priceArray[5] and level > 4:
        multipleClickers *= 2
        score -= priceArray[5]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 5 and score >= priceArray[6] and level > 5:
        multipleClickers *= 2
        score -= priceArray[6]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 6 and score >= priceArray[7] and level > 6:
        multipleClickers *= 2
        score -= priceArray[7]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 7 and score >= priceArray[8] and level > 7:
        multipleClickers *= 2
        score -= priceArray[8]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 8 and score >= priceArray[9] and level > 8:
        multipleClickers *= 2
        score -= priceArray[9]
        ClickerLabel.config(text="Points:" + str(score))
        multiClickButton.config(text="MultipleClicker X " + str(multipleClickers))
    elif multipleClickers == 9 and score >= priceArray[10] and level > 9:
        score -= priceArray[10]
        ClickerLabel.config(text="Points:" + str(score))
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
    if autoClickers == 1 and score >= priceArray[2] and level > 1:
        autoClickers += 1
        score -= priceArray[2]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 2 and score >= priceArray[3] and level > 2:
        autoClickers += 1
        score -= priceArray[3]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 3 and score >= priceArray[4] and level > 3:
        autoClickers += 1
        score -= priceArray[4]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 4 and score >= priceArray[5] and level > 4:
        autoClickers += 1
        score -= priceArray[5]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 5 and score >= priceArray[6] and level > 5:
        autoClickers += 1
        score -= priceArray[6]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 6 and score >= priceArray[7] and level > 6:
        autoClickers += 1
        score -= priceArray[7]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 7 and score >= priceArray[8] and level > 7:
        autoClickers += 1
        score -= priceArray[8]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 8 and score >= priceArray[9] and level > 8:
        autoClickers += 1
        score -= priceArray[9]
        ClickerLabel.config(text="Points:" + str(score))
        autoClickButton.config(text="AutoClicker X " + str((autoClickers - 1)**5))
        threading.Timer(1, click).start()
    elif autoClickers == 9 and score >= priceArray[10] and level > 9:
        score -= priceArray[10]
        ClickerLabel.config(text="Points:" + str(score))
        threading.Timer(1, click).start()
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
    if multipleClickers < level and score >= priceArray[multipleClickers // 2 + 2]:
        multiClickButton.config(bg="orange")
    else:
        multiClickButton.config(bg="white")


autoClickButton = Button(root, text="AutoClickers X" + str((autoClickers - 1)**5),
                         bg="white", fg="black", font=("Helvetica", 14),
                         command=autoclick_button)


def autoclick_color_button():
    global score
    global level
    global autoClickers
    if autoClickers < level and score >= priceArray[autoClickers + 1]:
        autoClickButton.config(bg="orange")
    else:
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
    score += multipleClickers
    ClickerLabel.config(text="Points:" + str(score))
    levelButton.pack()
    multiClickButton.place(x=1, y=240)
    autoClickButton.place(x=1212, y=240)
    quitButton.place(x=1, y=660)


ClickerLabel.pack()
LevelLabel.pack()
currentImage.pack()

root.bind('<Return>', game)
root.mainloop()
