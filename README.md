# Digital Radiography System
Raspberry Pi Python application for a control panel 
 
 # Control Panel:

 # Set new i2c bus (bus 3) on pi for ADC and accelerometer:
cd /boot
sudo nano config.txt
dtoverlay=i2c-gpio,bus=4,i2c_gpio_delay_us=1,i2c_gpio_sda=4,i2c_gpio_scl=5

# Rotate screen and touch
sudo nano /boot/config.txt
display_hdmi_rotate=2
dtoverlay=rpi-ft5406,touchscreen-swapped-x-y=2,touchscreen-inverted-x=2 # rotates touches


# GUI
![](./Screenshots/GUInew.png)

# Raspberry Pi GPIO Pinout
![](./Schematics/RaspberryPiGPIO.png)

