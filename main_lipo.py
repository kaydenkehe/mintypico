# Created by Kayden Kehe, May 2022
# This version is for those using a Pimoroni Pico LiPo with a LiPo battery
# REMEMBER TO RENAME THIS FILE TO "main.py"

from random import randint, choice
from machine import Pin, I2C, ADC
from sh1106 import SH1106_I2C
from utime import sleep, time

# Configure display
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)  
display = SH1106_I2C(128, 64, i2c, None, 60)

# Configure buttons
lowPowerButton = Pin(5, Pin.IN, Pin.PULL_UP)
restartButton = Pin(22, Pin.IN, Pin.PULL_UP)
leftButton = Pin(28, Pin.IN, Pin.PULL_UP)
rightButton = Pin(1, Pin.IN, Pin.PULL_UP)
upButton = Pin(17, Pin.IN, Pin.PULL_UP)
downButton = Pin(14, Pin.IN, Pin.PULL_UP)

# For reading power
vsys = ADC(29)
charging = Pin(24, Pin.IN)

score = 0
games = [1, 2, 3, 4, 5, 6]
currentGame = games[0]
batteryConversion = 3 * 3.3 / 65535

# Turn display on and set black
display.sleep(False)
display.fill(0)
display.rotate(180)

# Create outline
display.fill_rect(0, 0, 128, 2, 1)
display.fill_rect(0, 62, 128, 2, 1)
display.fill_rect(0, 0, 2, 64, 1)
display.fill_rect(126, 0, 2, 64, 1)

def clearScreen(): display.fill_rect(2, 2, 124, 60, 0) # Fill screen with black    

def renderMenu():
    clearScreen()
    display.text('PRESS START', 20, 16, 1)
    
    if currentGame == 1:
        display.text('SNAKE', 42, 26, 1)
    
        # Snake symbol
        display.fill_rect(32, 41, 4, 12, 1)
        display.fill_rect(32, 41, 12, 4, 1)
        display.fill_rect(44, 41, 4, 12, 1)
        display.fill_rect(44, 49, 12, 4, 1)
        display.fill_rect(56, 41, 4, 12, 1)
        display.fill_rect(56, 41, 12, 4, 1)
        display.fill_rect(68, 41, 4, 12, 1)
        display.fill_rect(68, 49, 12, 4, 1)
        display.fill_rect(80, 41, 4, 12, 1)
        display.fill_rect(80, 41, 12, 4, 1)
    
    elif currentGame == 2:
        display.text('BREAKOUT', 32, 26, 1)
        
        # Space Invaders symbol
        display.fill_rect(48, 52, 30, 2, 1)
        display.fill_rect(48, 50, 30, 2, 1)
        display.fill_rect(48, 48, 30, 2, 1)
        display.fill_rect(50, 46, 26, 2, 1)
        display.fill_rect(58, 44, 10, 2, 1)
        display.fill_rect(60, 42, 6, 2, 1)
        display.fill_rect(62, 40, 2, 2, 1)

    elif currentGame == 3:
        display.text('PONG', 46, 26, 1)

        # Pong symbol
        display.fill_rect(44, 40, 2, 16, 1)
        display.fill_rect(78, 40, 2, 16, 1)
        display.fill_rect(66, 45, 2, 4, 1)
        display.fill_rect(65, 46, 4, 2, 1)

    elif currentGame == 4:
        display.text('DODGE', 42, 26, 1)
        
        # Dodge symbol
        display.fill_rect(56, 40, 12, 14, 1)
        display.fill_rect(55, 41, 14, 12, 1)
        display.fill_rect(50, 54, 2, 4, 1)
        display.fill_rect(49, 55, 4, 2, 1)
        display.fill_rect(48, 40, 2, 4, 1)
        display.fill_rect(47, 41, 4, 2, 1)
        display.fill_rect(75, 45, 2, 4, 1)
        display.fill_rect(74, 46, 4, 2, 1)

    elif currentGame == 5:
        display.text('SPACE RACE', 24, 26, 1)
        
        # Space Race symbol
        display.fill_rect(46, 40, 6, 2, 1)
        display.fill_rect(48, 42, 4, 2, 1)
        display.fill_rect(46, 54, 6, 2, 1)
        display.fill_rect(48, 52, 4, 2, 1)
        display.fill_rect(52, 40, 4, 16, 1)
        display.fill_rect(56, 41, 2, 14, 1)
        display.fill_rect(58, 42, 4, 12, 1)
        display.fill_rect(60, 42, 4, 12, 1)
        display.fill_rect(62, 43, 2, 10, 1)
        display.fill_rect(64, 43, 2, 10, 1)
        display.fill_rect(66, 43, 2, 10, 1)
        display.fill_rect(68, 43, 2, 10, 1)
        display.fill_rect(70, 44, 2, 8, 1)
        display.fill_rect(72, 44, 2, 8, 1)
        display.fill_rect(74, 45, 2, 6, 1)
        display.fill_rect(76, 46, 2, 4, 1)
        display.fill_rect(78, 47, 2, 2, 1)

    # Battery display
    elif currentGame == 6:
        timeStep = 0
        lowPowerSwitchUsable = False
        
        while True:
            # Update display every 2.5 seconds (50 * 0.05)
            if timeStep % 50 == 0:
                clearScreen()
                display.text('BATTERY', 36, 14, 1)
                voltage, battery = getBattery() # Get voltage and estimated capacity
                
                # Make sure text with battery percentage is centered
                batteryStr = str(round(battery))
                if len(batteryStr) == 3: batteryX = 48
                elif len(batteryStr) == 2: batteryX = 53
                else: batteryX = 58
                         
                display.text(batteryStr + '%', batteryX, 26, 1)
                display.text('{0:.2f}'.format(voltage) + 'v', 44, 38, 1)
                if charging.value() == 1: display.text('CHARGING...', 4, 53, 1)
                
                display.text(str(currentGame), 116, 52, 1)
                display.show()
            
            sleep(0.05)
            timeStep += 1
            
            # This code for the low power mode is copied from mainLoop
            if lowPowerButton.value() == 1 and not lowPowerSwitchUsable: lowPowerSwitchUsable = True
            if lowPowerButton.value() == 0 and lowPowerSwitchUsable:
                lowPowerSwitchUsable = False
                lowPowerLoop()
                
            if upButton.value() == 0 or downButton.value() == 0: return

    display.text(str(currentGame), 116, 52, 1)
    display.show()

def startGame():
    clearScreen()
    global score
    score = 0
    
    # Snake
    if currentGame == 1:
        snakeHead = [randint(12, 54) * 2, randint(12, 20) * 2] # Position of head of snake
        snakeBody = [[snakeHead[0], snakeHead[1]]] # Contains all positions of snake body parts
        applePos = [randint(4, 62) * 2, randint(4, 30) * 2]
        while applePos in snakeBody: applePos = [randint(4, 62) * 2, randint(4, 30) * 2] # Position of apple
        
        # For velocity, [0, 1] means down, [0, -1] means up, [1, 0] means left, and [-1, 0] means right
        snakeInitVelocityX = choice([-1, 1, 0, 0])
        snakeInitVelocityY = choice([-1, 1]) if snakeInitVelocityX == 0 else 0
        snakeVelocity = [snakeInitVelocityX, snakeInitVelocityY]
        
        timeStep = 0
        movementQueue = [snakeVelocity] * 5
        secondGrowth = False
        
        while True:
            clearScreen()
            
            # End game if snake touches wall or itself
            if snakeHead[0] < 2 or snakeHead[0] > 126 or snakeHead[1] < 2 or snakeHead[1] > 62 or snakeHead in snakeBody[:-1]:
                score = (len(snakeBody) - 9) // 2
                break

            # Change velocity based on button press
            if downButton.value() == 0 and snakeVelocity != [0, -1]: movementQueue.insert(0, [0, 1])
            if upButton.value() == 0 and snakeVelocity != [0, 1]: movementQueue.insert(0, [0, -1])
            if rightButton.value() == 0 and snakeVelocity != [1, 0]: movementQueue.insert(0, [-1, 0])
            if leftButton.value() == 0 and snakeVelocity != [-1, 0]: movementQueue.insert(0, [1, 0])
            movementQueue = movementQueue[:5]
            snakeVelocity = movementQueue.pop(0)
            while len(movementQueue) < 5: movementQueue.insert(0, snakeVelocity)

            # Display body of snake
            for body in snakeBody:
                display.fill_rect(body[0], body[1], 2, 2, 1)
            display.fill_rect(applePos[0], applePos[1], 2, 2, 1) # Display apple
            
            # Update snake based on velocity
            if snakeVelocity[0] != 0: snakeHead[0] = snakeHead[0] + snakeVelocity[0] * 2
            elif snakeVelocity[1] != 0: snakeHead[1] = snakeHead[1] + snakeVelocity[1] * 2
            snakeBody.append([snakeHead[0], snakeHead[1]])
            
            # Remove oldest bit of snake unless game started fewer than 8 timesteps ago OR the snake is on the apple
            if snakeHead == applePos:
                applePos = [randint(4, 62) * 2, randint(4, 30) * 2]
                while applePos in snakeBody: applePos = [randint(4, 62) * 2, randint(4, 30) * 2]
                secondGrowth = True
            elif timeStep >= 8 and secondGrowth == False: snakeBody.pop(0)
            elif timeStep >= 8 and secondGrowth == True: secondGrowth = False
        
            display.show()
            timeStep += 1
            sleep(0.01 if timeStep >= 8 else 0.04)
    
    # Breakout
    elif currentGame == 2:
        gameOver = False
        playerPos = [52, 58]
        ballPos = [randint(2, 126), randint(44, 56)]
        ballVelocity = [choice([-1, 1]), -1]
        
        # Set positions of blocks to be broken
        blocksPos = []
        for i in range(5):
            for j in range(12):
                blocksPos.append([5 + 10 * j, 14 + 4 * i])
        
        while not gameOver:
            clearScreen()
            display.fill_rect(playerPos[0], playerPos[1], 16, 2, 1)
            
            # Display each block and destroy them if the ball is touching them
            for blockPos in blocksPos:
                if ballPos[0] - blockPos[0] <= 8 and ballPos[0] - blockPos[0] >= -2 and ballPos[1] - blockPos[1] <= 2 and ballPos[1] - blockPos[1] >= -2:
                    blocksPos.remove(blockPos)
                    if ballPos[1] - blockPos[1] == 0 or ballPos[1] - blockPos[1] == -1: ballVelocity[0] = -1 if ballVelocity[0] == 1 else 1
                    else: ballVelocity[1] = -1 if ballVelocity[1] == 1 else 1
                    score += 1
                else: display.fill_rect(blockPos[0], blockPos[1], 8, 2, 1)
            
            
            # Change ball velocity when it hits a surface
            if ballPos[0] >= 122: ballVelocity[0] = -1
            elif ballPos[0] <= 4: ballVelocity[0] = 1
            if ballPos[1] <= 2 : ballVelocity[1] = 1
            elif ballPos[1] >= 56 and ballPos[0] - playerPos[0] <= 16 and ballPos[0] - playerPos[0] >= 0: ballVelocity[1] = -1
                                                                                                                            
            elif ballPos[1] > 56: gameOver = True # Ball goes past player
            
            # Update ball position
            ballPos[0] = ballPos[0] + ballVelocity[0]
            ballPos[1] = ballPos[1] + ballVelocity[1]
            display.fill_rect(ballPos[0], ballPos[1], 2, 2, 1)
            
            # Move player
            if leftButton.value() == 0 and playerPos[0] < 108: playerPos[0] = playerPos[0] + 2
            if rightButton.value() == 0 and playerPos[0] > 4: playerPos[0] = playerPos[0] - 2
            
            display.show()
            sleep(0.001)
    
    # Pong
    elif currentGame == 3:
        timeStep = 0
        wallPos = [126, 0]
        wallDirection = -1
        playerPos = [4, 24]
        gameOver = False
        
        # Position and velocity of all four balls
        ballsPos = [] # [[randint(14, 124), randint(2, 62)], [randint(14, 124), randint(2, 62)], [randint(14, 124), randint(2, 62)], [randint(14, 124), randint(2, 62)], [randint(14, 124), randint(2, 62)], [randint(14, 124), randint(2, 62)]]
        ballsVelocity = [] # [] [[choice([-1, 1]), choice([-1, 1])], [choice([-1, 1]), choice([-1, 1])], [choice([-1, 1]), choice([-1, 1])], [choice([-1, 1]), choice([-1, 1])], [choice([-1, 1]), choice([-1, 1])], [choice([-1, 1]), choice([-1, 1])]]
        for i in range(3):
            ballsPos.append([randint(14, 124), randint(2, 62)])
            ballsVelocity.append([choice([-1, 1]), choice([-1, 1])])
        
        while not gameOver:
            clearScreen()
            display.fill_rect(wallPos[0], wallPos[1], 2, 64, 1)
            display.fill_rect(playerPos[0], playerPos[1], 2, 20, 1)
            
            for ballPos, ballVelocity in zip(ballsPos, ballsVelocity):
                # Change ball velocity when it hits surface
                if ballPos[0] >= wallPos[0] - 2: ballVelocity[0] = -1
                if ballPos[1] >= 58: ballVelocity[1] = -1
                elif ballPos[1] <= 4: ballVelocity[1] = 1
                
                # Ball hits player paddle
                if ballPos[0] == 6 and ballPos[1] - playerPos[1] <= 20 and ballPos[1] - playerPos[1] > 0:            
                    ballVelocity[0] = 1
                    score += 1
                    
                if ballPos[0] < 6: gameOver = True # Ball goes past player
                
                # Update ball position
                ballPos[0] = ballPos[0] + ballVelocity[0]
                ballPos[1] = ballPos[1] + ballVelocity[1]
                display.fill_rect(ballPos[0], ballPos[1], 2, 2, 1)
            
            # Move player
            if upButton.value() == 0 and playerPos[1] > 4: playerPos[1] = playerPos[1] - 2
            if downButton.value() == 0 and playerPos[1] < 40: playerPos[1] = playerPos[1] + 2
            
            display.show()
            sleep(0.001)
            timeStep += 1
            if timeStep % 3 == 0:
                if wallPos[0] <= 32: wallDirection = 1
                elif wallPos[0] >= 126: wallDirection = -1
                wallPos[0] = wallPos[0] + wallDirection
    
    # Dodge
    elif currentGame == 4:
        beginTime = time()
        playerPos = [9, 8]
        ballsPos = []
        ballsVelocity = []
        for _ in range(6):
            ballsPos.append([randint(6, 124), randint(6, 62)])
            ballsVelocity.append([choice([-1, 1]), choice([-1, 1])])
        gameOver = False
        
        while not gameOver:
            clearScreen()
            display.fill_rect(playerPos[0], playerPos[1], 8, 10, 1)
            display.fill_rect(playerPos[0] - 1, playerPos[1] + 1, 10, 8, 1)
            
            for ballPos, ballVelocity in zip(ballsPos, ballsVelocity):
                # Change ball velocity when it hits surface
                if ballPos[0] >= 124: ballVelocity[0] = -1
                elif ballPos[0] <= 4: ballVelocity[0] = 1
                if ballPos[1] >= 60: ballVelocity[1] = -1
                elif ballPos[1] <= 2: ballVelocity[1] = 1
                
                # Update ball position
                ballPos[0] = ballPos[0] + ballVelocity[0]
                ballPos[1] = ballPos[1] + ballVelocity[1]
                display.fill_rect(ballPos[0], ballPos[1], 2, 2, 1)
                
                if ballPos[0] - playerPos[0] <= 10 and ballPos[0] - playerPos[0] >= -3 and ballPos[1] - playerPos[1] <= 10 and ballPos[1] - playerPos[1] >= -3:
                    score = round(time() - beginTime)
                    gameOver = True
            
            if leftButton.value() == 0 and playerPos[0] <= 114: playerPos[0] = playerPos[0] + 2
            if rightButton.value() == 0 and playerPos[0] >= 7: playerPos[0] = playerPos[0] - 2
            if upButton.value() == 0 and playerPos[1] >= 5: playerPos[1] = playerPos[1] - 2
            if downButton.value() == 0 and playerPos[1] <= 48: playerPos[1] = playerPos[1] + 2
            
            display.show()
            sleep(0.001)
    
    # Space Race
    elif currentGame == 5:
        gameOver = False
        playerPos = [62, 41]
        playerHeight = 0
        blocksPos = [] # Includes xPos, yPos, and velocity
        
        # Create floor
        for i in range(7):
            blocksPos.append([41 + 7 * i, 55, 0])
            
        # Create first two obstacles
        for i in range(2):
            blocksPos.append([randint(34, 90), 16 + 16 * i, choice([-1, 1])])
            
        while not gameOver:
            clearScreen()
            display.fill_rect(34, 0, 2, 128, 1)
            display.fill_rect(92, 0, 2, 128, 1)
            for i, blockPos in enumerate(blocksPos):
                # See if block is colliding with player
                if blockPos[0] - playerPos[0] <= 6 and blockPos[0] - playerPos[0] >= -6 and blockPos[1] - playerPos[1] <= 10 and blockPos[1] - playerPos[1] >= -2: gameOver = True
                
                # See if block is colliding with wall
                if blockPos[0] > 88: blocksPos[i][2] = -1
                elif blockPos[0] < 36: blocksPos[i][2] = 1
                if blockPos[1] > 135: blocksPos.remove(blockPos)
                else:
                    blocksPos[i][0] = blockPos[0] + blockPos[2]
                    display.fill_rect(blockPos[0], blockPos[1], 4, 2, 1)
            
            if upButton.value() == 0:
                # Move player up at start
                if playerHeight <= 12:
                    playerPos[1] = playerPos[1] - 1
                    playerHeight += 1
                # Move obstacles down after start
                else:
                    for blockPos in blocksPos: blockPos[1] = blockPos[1] + 1
                    playerHeight += 1
                    if playerHeight % 16 == 0:
                        # Create new obstacle when the player travels up for 16 frames
                        blocksPos.append([randint(34, 90), 0, choice([-1, 1])])
                        score += 1
                    
            display.fill_rect(playerPos[0], playerPos[1], 4, 10, 1)
            display.fill_rect(playerPos[0] - 1, playerPos[1] + 1, 6, 8, 1)
            
            display.show()
            sleep(0.001)
    
    # Battery percentage screen
    elif currentGame == 6: return
    
    clearScreen()
    
    # Read and write highscores
    highscore = 0
    with open('highscores.txt', 'r+') as hs:
        hsLines = hs.readlines()
        if score > int(hsLines[currentGame - 1].strip()): hsLines[currentGame - 1] = str(score) + '\n'
        hs.seek(0)
        hs.write(''.join(hsLines))
        highscore = int(hsLines[currentGame - 1].strip())
    
    display.text('GAME OVER', 28, 16, 1)
    display.text(f'SCORE: {score}', 28, 28, 1)
    display.text(f'BEST: {highscore}', 28, 40, 1)
    display.show()
    sleep(0.5)

def getBattery():
    voltage = vsys.read_u16() * batteryConversion
    batteryPercent = 100 * ((voltage - 2.8) / (4.2 - 2.8))
    return voltage, batteryPercent

# Put the Pico in "low-power" mode
def lowPowerLoop():
    # Disable screen and decrease CPU frequency
    display.sleep(True)
    machine.freq(25000000)
    while True:
        sleep(0.5)
        while lowPowerButton.value() == 0:
            while leftButton.value() == 0:
                sleep(0.05)
                while leftButton.value() == 1:
                    while upButton.value() == 0:
                        sleep(0.05)
                        if upButton.value() == 1:
                            machine.freq(125000000)
                            display.sleep(False)
                            return

def mainLoop():
    global currentGame
    lowPowerSwitchUsable = False # This variable helps make sure that low-power mode is not immediately reactivated upon being deactivated
    
    while True:
        if lowPowerButton.value() == 1 and not lowPowerSwitchUsable: lowPowerSwitchUsable = True
        if lowPowerButton.value() == 0 and lowPowerSwitchUsable:
            lowPowerSwitchUsable = False
            lowPowerLoop()
        if restartButton.value() == 0: startGame() # Start game when start button pressed
        
        # Cycle through menu when up/down buttons pressed
        elif upButton.value() == 0:
            currentGame = games[(currentGame) % len(games)]
            renderMenu()    
        elif downButton.value() == 0:
            currentGame = games[(currentGame - 2) % len(games)]
            renderMenu()
            
        sleep(0.1)

renderMenu()
mainLoop()

