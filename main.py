import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open media player" in c.lower():
        # This command will open the Groove Music (Media Player)
        subprocess.Popen(["start", "mswindowsmusic:"], shell=True)
    elif "open my linkedin profile" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/siddhant-rana-7a942a34b/")

#rename file system
def rename_file(command):
    #Extract filenames and rename the file on the Desktop
    try:
        # Extract the filenames from the command
        parts = command.lower().replace("change", "").strip().split(" to ")
        
        if len(parts) != 2:
            speak("Please say the original file name followed by 'to' and the new file name.")
            return

        old_name = parts[0].strip()  # Extract old file name
        new_name = parts[1].strip()  # Extract new file name

        old_file_path = os.path.join(desktop_path, old_name)
        new_file_path = os.path.join(desktop_path, new_name)

        # Check if the original file exists
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            speak(f"Successfully changed {old_name} to {new_name}")
        else:
            speak("The file does not exist on your desktop.")
    except Exception as e:
        speak("An error occurred while renaming the file.")
        print(f"Error: {e}")

    
    
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    # Listen for the wake word "Jarvis"
    # obtain audioo from the microphone
    while True:
        r = sr.Recognizer()
      

        print("recognizing...")  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                     print("Jarvis Active...")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)

                     processCommand(command)

        except Exception as e:
            print("Error;{0}".format(e))
             


                    

           

       

