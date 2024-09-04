import speech_recognition as sr
import yagmail

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message")
    recordedaudio=recognizer.listen(source)
    print('Done recording.')
text=''
try:
    print('Printing the message')
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))

    #Automate mails:

    reciever='21eg105j33@anurag.edu.in'
    message=text
    sender=yagmail.SMTP('email','activity password')
    sender.send(to=reciever,subject='This is an automated mail',contents=message)
    sender.close()
    print('mail sent')

except Exception as ex:
    print('Error sending email:', ex)