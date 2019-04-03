from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
button1 = Button(23)
camera = PiCamera()
i=125
j=0
print("Press 1st button to on the camera")
button.wait_for_press()
camera.start_preview()
while j<3:
    button1.wait_for_press()
    file = '/home/pi/image'+str(i)+'.jpg'
    camera.capture(file)
    i = i+1
    j=j+1
print("Press 1st button to stop the camera")
button.wait_for_press()
camera.stop_preview()