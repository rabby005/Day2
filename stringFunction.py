

#String Functions


#str = "I am a coder."
#str.endswith("er.")        returns true if string ends with substr
#str. capitalize()          capitalizes 1st char
#str.replace old, new)      replaces all occurrences of old with paradfor
#str.find (word )           returns 1st index of 1st occurrence
#str.count("am")            counts the occurrence of substr in string



#---------------------endwith-----------------

str = "I am a coder. I love to code."
print(str.endswith("de"))
print(str.endswith("de."))

#false 
print(str.endswith("ove"))


#---------------------capitalize-----------------

#capitalize
name = "faraby"
print(name.capitalize())
print(name)

#sob somoy  captalize  variable er value capatilize rakhte hole
name2 = "faraby"
name3=(name2.capitalize())
print(name3)


#---------------------replace-----------------

#replace || chaile je kono word replace kora jay

name4="My name is faraby abdulla all rabby, farabya in my nicknime ."
print(name4.replace("a","o"))

#eiline word replace kora hoyese
print(name4.replace("faraby","rabby")) 


#---------------------fine-----------------

#find //je okhorta find korbe tar index number dekhabe 
name5="i am a good coder. i love to code. i code everyday."
print(name5.find("o"))

#je word ta  find korbe tar prothom okhorer index number dekhabe 
name6="i am a good coder. i love to code. i code everyday."
print(name6.find("code"))

#emon kono kiso jodi find kori jeta nai ,tahole reasult asbe -1 .tar mane neita kono valid index na.
name7="i am a good coder. i love to code. i code everyday."
print(name7.find("Q"))



#---------------------count-----------------
name7="i am a good coder. i love to code. i code everyday."
print(name7.count("good"))