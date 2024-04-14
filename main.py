from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    stop_play = int(input("Press 2 anytime to stop playback and go back to the menu: "))
    if stop_play == 2:
      source.paused = True #player paused
      return #goes back to the menu
    else:
      continue
          
      


       
while True:
    os.system("clear") # Show the menu
    print("Welcone to Nina's Replit 80's Playlist!")
    time.sleep(2)
    #menu options
    print("Press 1 to Play")
    time.sleep(1)
    print("Press 2 to Exit")
    time.sleep(1)  
    print("Press anything else to see the menu again.")
    user_input = int(input(">>>  "))
  
    if user_input == 1:
      print(" Now playing 'Classical Music'")
      play()
      time.sleep(5)
    elif user_input == 2:
      exit()
    else:
      continue
        
  

  # check whether you should call the play() subroutine depending on user's input