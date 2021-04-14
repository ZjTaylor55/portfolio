import random
import tkinter
import tkinter.messagebox

window = tkinter.Tk()

window.title("Oc Generator")

# OC Names
original_character_list_female = ['Åshild', 'Ravenna Stormwraith', 'Ravenna Mage-Hunter', 'Freyja', 'Luna', 'Svala', 'Valkyria', 'Svanna', 'Aradan Thornberg', 'Asharil', 'Lanaya', 'Ælflaed'
, 'Æthelflæd', 'Anthemia', 'Sigrunn Silenthelm', 'Atheleys les Forgeron', 'Telvanni Whitemane', 'Sarvaste', 'Mirana', 'Kerillian', 'Naestra', 'Arahan' ]
original_character_list_male = ['Torstein Scalp-Taker', 'Germanicus', 'Tyr', 'Eomer', 'Caius Umbrius Auxentius', 'Sertorius', 'Maximus Flavonius Marcellinus', 'Boric the Grim', 'Alberic le Bint', 'Bjorn Rannveigsson', 'Trajanus Justicia' ]

#print(random.choice(original_character_list_female))
#print(random.choice(original_character_list_male))

#Retrieve a name at random from the lists
def maleNames () :
    tkinter.messagebox.showinfo ("Name", random.choice(original_character_list_male))

def femaleNames () :
    tkinter.messagebox.showinfo ("Name", random.choice(original_character_list_female))

#Window Size
window.geometry ("1920x1080")

#Create the Buttons
A = tkinter.Button (window, text = "Male", bg = 'blue', command = maleNames)

B = tkinter.Button (window, text = "Female", bg = 'pink', command = femaleNames)


A.pack ()
B.pack ()
window.mainloop ()