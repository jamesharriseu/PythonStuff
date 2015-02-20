# Knights to was "ni" video reference
# https://www.youtube.com/watch?v=zIV4poUZAQo


file = open("stop-words.rtf")
stopwords = file.readlines()

for word in stopwords:
    input = raw_input("Hello, what is your name?")
    next = word.strip()
    input = input.replace(" " + next + " ", " ")

#while True:
    #input = raw_input("Say something interesting: ")
    #filtered = input.replace(" ni ", " <beep> ")
    #print("Your filtered text was: " + filtered)
    
name = raw_input("What is your name? ")
print "Hello, %s." % name
greeting = raw_input("How are you? ")
print "Why is that, %s?" % name
explain = raw_input ("I dont have feelings, so I could never feel %s , %s" % (greeting, name))




