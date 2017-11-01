import time

def show(text):
    print(text)

def playdied(pygame):
    pygame.mixer.music.load('music/died.mp3')
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.stop()