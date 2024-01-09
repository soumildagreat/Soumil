import pyttsx3
talkingtom = pyttsx3.init()
for i in range(2):
    talkingtom.say(input("What do you want Talking Tom to say? He will say whatever you want him to say twice."))
    talkingtom.runAndWait()