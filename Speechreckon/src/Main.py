__author__ = "Juaan"
__date__ = "$22-abr-2019 22:09:27$"

import speech_recognition as sr
from googletrans import Translator
import pygubu

r = sr.Recognizer()
translator = Translator()

class Application:
             
    def __init__(self):
                       
        self.builder = pygubu.Builder()        
        self.builder.add_from_file('MainForm.ui')       
        self.mainwindow = self.builder.get_object('MainFrame')
        
        lblSpokenPhrase = self.builder.get_object("lblSpokenPhrase")
        lblTranslated = self.builder.get_object("lblTranslated")
        
        def onListenClicked():
    
            with sr.Microphone() as source:  
                
                received_audio = r.listen(source)    
                audio_to_text = r.recognize_google(received_audio)
                lblSpokenPhrase.config(text=("{}".format(audio_to_text)))        
                translation = translator.translate(("{}".format(audio_to_text)), dest="es")
                lblTranslated.config(text=translation.text)
                        
        callbacks = {
            'onListenClicked': onListenClicked
        }

        self.builder.connect_callbacks(callbacks)
        
    def run(self):
        self.mainwindow.mainloop()
    
if __name__ == '__main__':    
    app = Application()
    app.run()