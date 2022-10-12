import os
from gtts import gTTS
Text = "Hello! I am Areeb And i am here to tell you that you are a very Nice person to me, Love you so Much"
my_voice = gTTS(text=Text, lang='es', tld='es', slow=False)
my_voice.save("Audio.mp3")
os.system("Audio.mp3")