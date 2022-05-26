# **mintyPico**
##### This repo contains the code and files necessary to build the mintyPico <br/>
##### YouTube tutorial: https://youtube.com/ <br/>
##### My YouTube channel: https://www.youtube.com/channel/UCn5eZ8l-LLnRv9ov-WQtwqA
##### For this project, you should have a drill, a dremel, and a soldering iron. A set of metal files would also be nice! <br/>
#

### **USAGE:**<br/>
The top left button starts games <br/>
The bottom left button switches the pico into "low-power" mode (disables display and turns cpu clock frequency down 5x) <br/>
To switch the Pico back into normal mode, while holding the low-power button, press the right button, then the top button, then the left button <br/>
The four right buttons operate the games <br/>

### **CODE:** <br/>
**sh1106.py:** Driver for display, code can be found at https://github.com/robert-hh/SH1106 <br/>
**main_lipo.py:** Main code for those using Pimoroni Pico LiPo with a battery (Rename to main.py) <br/>
**main_normal.py:** Main code for those using a normal Pico without a battery (Rename to main.py) <br/>

### **OTHER FILES:** <br/>
**highscores.txt:** Keeps records of highscores. Should be downloaded to the Pico along with main.py and sh1106.py <br/>
**prints.zip:** Contains all 3D print files <br/>
--**screenholder.obj:** Holds display in place <br/>
--**holeguide.obj:** Guide for drilling holes in the tin <br/>
--**base.obj:** Holds the Pico and battery <br/>
--**buttonholder.obj:** Holds the button switches <br/>
**pcb.zip:** Contains gerber files for PCB. I ordered my PCB from https://www.pcbway.com/ <br/>

### **PARTS:** <br/>
**Display:** https://www.amazon.com/Teyleten-Robot-Display-Raspberry-Microcontroller/dp/B08J1D212N/ <br/>
**Pimoroni Pico LiPo:** https://shop.pimoroni.com/products/pimoroni-pico-lipo <br/>
**LiPo battery:** https://www.amazon.com/Battery-Packs-Lithium-Polymer-100mAh/dp/B0137KTPP0/ <br/>
**Altoids Smalls Tins:** https://www.amazon.com/ALTOIDS-Smalls-Peppermint-Breath-0-37-Ounce/dp/B005CXDWT6/ <br/>
**Buttons:** https://www.amazon.com/dp/B09YPQV1F9/ <br/>
**Wire:** https://www.amazon.com/StrivedayTM-Flexible-Silicone-electronic-electrics/dp/B01KQ2JNLI/ <br/>
**Tape:** (I know it's expensive, but it works really well) https://www.amazon.com/gp/product/B07GWRF9D8/ <br/>

### **NOTES:** <br/>
Feel free to use the code and files from this project in any capacity you like, commercial or otherwise :) <br/>
My two main sources of inspiration for this project are the mintyPi from sudomod, and the Pico snake project from Hari Wiguna <br/>
mintyPi: https://www.youtube.com/watch?v=YqE2x-0JYzs <br/>
Pico snake: https://www.youtube.com/watch?v=5r_6mbYlLVo <br/>
