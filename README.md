# Temperature_Control-CHIP_i2c
[LICENSE]
Released under GPL v3 and newer ¢ copyright and copyleft. Created by Filippo Falezza

[What is it?]
This is a temperature control script created to work with chip, yet editable to work with any board. It controls an mcp23017 which starts a fan via a transistor if the temperature is more than 34°C.

[Installing]
First of all you have to clone the repo:
  git clone https://github.com/effeffe/Temperature_Control-CHIP_i2c
Then you have to execute the script:
  python temp.py
If you want to make it auto-executed at boot time, obviousely you can!

[Hardware connection]
I've connected the fan to an i2c port thorugh the MCP23017 because i've just 8 GPIOs, so i preferred to leave them free for some projects.
Remember to connect the three pins defining the right i2c adress, otherwise if you leve them floating the chip will change adress during the use. I've also connected a 100Khom resistor between Ground and Pin 18 for resetting reasons.

[TODO]
-add script to be executed automatically when the system starts. It has to check the temperature every 2/5 minutes according to user settings.
-the print functions in the python script are for debug only, so they have to be commented or removed
