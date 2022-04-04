import tkinter as tk

# Creating Main GUI
window=tk.Tk()
# Adding Title For GUI
window.title("Diary App Made By -Nolen Avery")
# Setting Resolution For Newly Created GUI
window.geometry("800x700")

# Function For The Quit Button That Quits Out Of The Program When Clicked
def quitprogram(event):
  quit()

#Creating The Quit Button
quitapp = tk.Button(window, text = "Quit")
quitapp.grid(column=200,row=9000)
# Binding The Quit Button To The Left Mouse Button And Specifying A Function I Wrote Earlier That Makes It So When The Button Is Clicked It Quits Out The Program.
quitapp.bind("<Button-1>", quitprogram)

# Prompting The User In The GUI To Write There Diary In The Terminal
newlabel = tk.Label(text = "Write Your Diary In The Terminal.")
newlabel.grid(column=0,row=0)

# Adding User Input Prompt To The Terminal That Lets The User Write There Diary.
diary = input("Start Writing Your Diary: ")


# Creating A Label In The GUI That Asks The User If They Want To Save The Diary They Wrote.
savelabel = tk.Label(text = "Do u want to save the file?")
savelabel.grid(column=0,row=1)
# Printing In The Terminal That It Is Waiting For A Responce From The User In The GUI.
print("Waiting For Responce In GUI.")

# Function That Writes The Users Diary Into The Diary.txt
def save(event):
  # Opens the diary.txt file
  w = open("diarys.txt", "w")
  # Writes The Diary In The File We Just Opened.
  w.write(diary)
  # Closes The File We Just Opened And Wrote The Diary In.
  w.close()
  # Creates A Label That Informs The User That The Diary Has Been Written To The Diarys.txt File.
  success = tk.Label(text = "Success! Your Diary Is Now Written In The diarys.txt :)")
  success.grid(column=0,row=2)
  # Prints To The Terminal That The User Picked Yes To Saving The File.
  print("Got Responce Yes.")

# Creating A Yes Button For The Label We Wrote Above. When Clicked It Will Write Whatever The User Wrote In The Diary Prompt From Earlier Into The Diary.txt File!
saveyes = tk.Button(window, text = "Yes")
saveyes.grid(column=1,row=1)
# Binding This Yes Button To The Left Mouse Click And Specifying A Function I Wrote Above Called Save Which Will Write The Diary To The Diary.txt
saveyes.bind("<Button-1>", save)


# Function Used For The No Button.
def savenope(event):
  # Creating a Label Which Informs The User That The Diary Was Not Saved And Thanks The User For Using The Program
  success = tk.Label(text = "Diary Not Saved! Thanks For Using My Program.")
  success.grid(column=0,row=2)
  # Prints To The Terminal That The User Chose No.
  print("Got Responce No.")

# Creating A No Button That Will Not Write The File To The Diarys.txt
saveno = tk.Button(window, text = "No")
saveno.grid(column=2,row=1)
# Binding The No Button To The Left Mouse Button And Specifying The Function I Wrote Earlier Called savenope.
saveno.bind("<Button-1>", savenope)

# Creating A Variable Called Answer That Is = To The Users Input()
answer = input()


# Wrote By Nolen Avery Beginner Python Dev 2022