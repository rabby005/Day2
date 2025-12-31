#String Functions
#str = "I am a coder."
#str.endswith("er.") #returns true if string ends with substr
#str. capitalize() #capitalizes 1st char
#str.replace old, new) #replaces all occurrences of old with paradfor
#str.find (word )
#returns 1st index of 1st occurrence
#str.count("am") #counts the occurrence of substr in string


str = "I am a coder. I love to code."
print(str.endswith("de"))
print(str.endswith("de."))

#false 
print(str.endswith("ove"))


#capitalize
name = "faraby"
print(name.capitalize())
print(name)

#sob somoy  captalize  variable er value capatilize rakhte hole
name2 = "faraby"
name3=(name2.capitalize())
print(name3)


#replace || chaile je kono word replace kora jay

name4="My name is faraby abdulla all rabby, farabya in my nicknime ."
print(name4.replace("a","o"))

print(name4.replace("faraby","rabby"))