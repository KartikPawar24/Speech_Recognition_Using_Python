import speech_recognition as sr

r = sr.Recognizer()

print("You can speak now:")
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    print("I have analysed that you have spoken:\n{}".format(r.recognize_google(audio)))

except sr.UnknownValueError:
    print("I did not understood what you have spoken!!!")

except sr.RequestError:
    print("Request processing failed!!!")


