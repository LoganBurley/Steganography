from PIL import Image
import numpy as np
import sys
#FUNCTIONS
def getImageData(image):
    im = Image.open(image)
    
    #get RGB in base 10 and width, height values
    pixels = list(im.getdata())
    width, height = im.size        
    
    #convert pixles from tuples to list
    pixelData = [list(x) for x in pixels] 
    
    return pixelData, width, height  

def readFile(messageFile):
    message = ''
    #open file and write to string
    with open(messageFile, 'r') as f:
        message = f.read()

    return message

def encode(originalImage, message, modifiedImageName):
    message += '01111110' #add stop bit
    
    messageLength = len(message) #find the length of message
    
    pixelData, width, height = getImageData(originalImage) 
    
    #change pixel values
    pixelData = changePixel(pixelData, message, messageLength) 
    
    #create empty image
    modifiedImage = [[0 for _ in range(width)] for _ in range(height)]
    
    #create new image with message encoded
    index = 0
    for y in range(height):
        for x in range(width):
            modifiedImage[y][x] = pixelData[index]
            index += 1
    
    #convert list to a format that PIL can use
    modifiedImageNP = np.array(modifiedImage, dtype=np.uint8)
    
    image = Image.fromarray(modifiedImageNP).convert('RGB')
    image.save(modifiedImageName)
    
    pixelData, _, _ = getImageData(modifiedImageName)
    
def isEven(num):
    return num % 2 == 0
               
def changePixel(pixelData, message, messageLength):
    bitTracker = 0 
    for pixel in pixelData:
        for pixelIndex in range(3):
            if isEven(pixel[pixelIndex]) and not isEven(int(message[bitTracker])):
                pixel[pixelIndex] += 1 #make pixel odd
            if not isEven(pixel[pixelIndex]) and isEven(int(message[bitTracker])):
                pixel[pixelIndex] += 1 #make pixel even
           
            if pixel[pixelIndex] > 255: #if RGB value is edge case
                pixel[pixelIndex] -= 2
                
            bitTracker += 1       
            if bitTracker >= messageLength: #end of message reached
                return pixelData 
            
def decode(modifiedImage, outFile):
    pixelData, _, _ = getImageData(modifiedImage) #get RGB values
    
    print("Encoded Message: ")
    
    #printing to stdout
    encodedMessage = ''
    for pixel in pixelData:
        for pixelIndex in range(3):
            if pixel[pixelIndex] % 2 == 0: 
                encodedMessage += '0'
            else:
                encodedMessage +='1'
            
            if len(encodedMessage) == 8:
                if encodedMessage == '01111110': #stop byte
                    sys.exit()
                char = chr(int(encodedMessage, 2))
                print(char, end='') #print a char from the message
                
                #add char to txt
                hiddenMessages = open(outFile, "a")
                hiddenMessages.write(char)
                
                #reset message
                encodedMessage = ''

