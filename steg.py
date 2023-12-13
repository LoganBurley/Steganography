import sys  
from functions import encode
from functions import decode
from functions import readFile

#START MAIN

#checks num arguments
numArgs = len(sys.argv)

if numArgs < 2:
    print("Missing Argumets")
    sys.exit(1)

#assign encode or decode
command = sys.argv[1] 

#encode
if command == '-e':
    if numArgs < 4:
        print("Too Few Arguments")
        sys.exit(1)
        
    #assign arguments to variables
    originalImage = sys.argv[2]
    modifiedImage = sys.argv[3]
    
    message = ''
    if len(sys.argv) < 5: 
        print('Type in your message to encode. Type "ctr+z <return>" to stop: ')
        message += sys.stdin.read() #stops reading after ctr + z
    else:
        messageFile = sys.argv[4]
        message = readFile(messageFile)
         
    #conver to ASCII and then binary
    message = ''.join(format(ord(i), '08b') for i in message)
        
    encode(originalImage, message, modifiedImage)

#decode
elif command == '-d':
    if numArgs < 4:
        print("Too Few Arguments")
        sys.exit(1)

    #assign arguments to variables
    modifiedImage = sys.argv[2]
    outFile = sys.argv[3]        
    
    decode(modifiedImage, outFile)

else:
    print("Invalid Command")
    sys.exit(1)