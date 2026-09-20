import time
import board
import neopixel

# Set up the built-in RGB pixel
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5)

while True:
    # Bright blue midday sky
    for i in range(0, 100, 2):
        pixel[0] = (0, int(150 * i / 100), int(255 * i / 100))
        time.sleep(0.04)
    time.sleep(2)

    # Transition from blue sky to campus green
    for i in range(0, 100, 2):
        r = int((0 + (104 - 0) * i / 100))
        g = int((150 + (138 - 150) * i / 100))
        b = int((255 + (59 - 255) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)
    time.sleep(1)

    # Transition from campus green to golden hour orange
    for i in range(0, 100, 2):
        r = int((104 + (200 - 104) * i / 100))
        g = int((138 + (100 - 138) * i / 100))
        b = int((59 + (40 - 59) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)
    time.sleep(2)

    # Transition from golden hour to pink sunset
    for i in range(0, 100, 2):
        r = int((200 + (248 - 200) * i / 100))
        g = int((100 + (220 - 100) * i / 100))
        b = int((40 + (235 - 40) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)
    time.sleep(2)

    # Transition from pink to NYUAD purple sunset
    for i in range(0, 100, 2):
        r = int((248 + (87 - 248) * i / 100))
        g = int((220 + (6 - 220) * i / 100))
        b = int((235 + (140 - 235) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)
    time.sleep(2)

    # Transition from NYUAD purple sunset to deep purple dusk
    for i in range(0, 100, 2):
        r = int((87 + (48 - 87) * i / 100))
        g = int((6 + (25 - 6) * i / 100))
        b = int((140 + (52 - 140) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)
    time.sleep(2)

    # Transition from deep purple dusk to dark night
    for i in range(0, 100, 2):
        r = int((48 + (5 - 48) * i / 100))
        g = int((25 + (5 - 25) * i / 100))
        b = int((52 + (20 - 52) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)
    time.sleep(2)

    # Transition from night to soft NYUAD purple glow
    for i in range(0, 100, 2):
        r = int((5 + (40 - 5) * i / 100))
        g = int((5 + (5 - 5) * i / 100))
        b = int((20 + (60 - 20) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.04)

    # NYUAD building purple glow - slow pulse
    for repeat in range(3):
        for i in range(0, 100, 2):
            r = int((40 + (87 - 40) * i / 100))
            g = int((5 + (6 - 5) * i / 100))
            b = int((60 + (140 - 60) * i / 100))
            pixel[0] = (r, g, b)
            time.sleep(0.06)
        for i in range(0, 100, 2):
            r = int((87 + (40 - 87) * i / 100))
            g = int((6 + (5 - 6) * i / 100))
            b = int((140 + (60 - 140) * i / 100))
            pixel[0] = (r, g, b)
            time.sleep(0.06)

    # Fade to dark before restarting
    for i in range(0, 100, 2):
        r = int((40 + (5 - 40) * i / 100))
        g = int((5 + (5 - 5) * i / 100))
        b = int((60 + (20 - 60) * i / 100))
        pixel[0] = (r, g, b)
        time.sleep(0.06)
    time.sleep(1)