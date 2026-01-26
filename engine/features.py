from playsound import playsound
import eel

#sound function for playing sound
def playAssistantSound():
    music_dir = 'www\\assets\\audio\\start_sound.mp3'
    playsound(music_dir)

# Click sound for mic button
@eel.expose
def playClickSound():
    music_dir = 'www\\assets\\audio\\click_sound.mp3'
    playsound(music_dir)