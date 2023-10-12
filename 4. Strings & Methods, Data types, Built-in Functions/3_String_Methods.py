# String Methods
first = "vinAyAk"

print(first)
print(first.lower()) # doesn't changes the original value in first
print(first.upper()) # doesn't changes the original value in first
print(first)
print('')

#Multiline
multiline = "vinayak   singhal is good"

print(multiline.title()) #every word start with capital
print(multiline.replace("good", "ok")) # doesn't changes the original value in first
print(multiline)

print(len(multiline))
multiline += "                                        " # adds space in the end
multiline = "                  " + multiline # adds spaces in starting
print(len(multiline))

print('')

print(multiline.strip())
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "*"))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
