from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
button1 = Button(23)
camera = PiCamera()
##i=100
#j=0
#while j<5:
print("Press 1st button to on the camera")
button.wait_for_press()
camera.start_preview()
button1.wait_for_press()
file = '/home/pi/image5.jpg'
#print(file)
camera.capture(file)
print("Press 1st button to stop the camera")
button.wait_for_press()
camera.stop_preview()
#   i = i+1
#  j=j+1
