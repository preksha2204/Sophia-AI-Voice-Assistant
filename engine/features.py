import eel
import os
import re
import pywhatkit as kit
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME

#sound function for playing sound
def playAssistantSound():
    music_dir = 'www\\assets\\audio\\start_sound.mp3'
    playsound(music_dir)

# Click sound for mic button
@eel.expose
def playClickSound():
    music_dir = 'www\\assets\\audio\\click_sound.mp3'
    playsound(music_dir)

def OpenCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    query.lower()

    if query!="":
        speak("Opening" +query)
        os.system("start" +  query)
    else:
        speak(f"{query} not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I couldn't find what to play on YouTube.")

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+YouTube' #Dynamic term is extracted using regular expressions allowing us to work with just the part we need for the YouTube search.
    match = re.search(pattern, command, re.IGNORECASE) # re helps to search for patterns in the commands.
    return match.group(1) if match else None