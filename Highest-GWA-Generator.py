#Anonuevo, Loraine N.
#BSCpE 1-4
#Highest-GWA-Generator

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mAyooo! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

#Request about the user's name.
print("")
print("\033[1;3mMy name is \033[;45;1;3mLoraine\033[0m")
your_name = input("\033[1;3mWhat is your name?\033[0m")
print("\033[;1;3mI'm glad that you're here!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, and i'll share to you the student who got the highest GWA!\033[0m")

# Open the txt file for reading
with open("Students.txt") as main_file:
    # Create a variable to keep track of the name of the student who received the highest GWA and his/her GWA.
    highest_gwa = 5.00
    student_highest = ""

