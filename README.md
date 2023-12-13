# Steganography-
Encrypted Messaging

Stenography is taking a message and ecrypting it into the least significant bits of an images
RGB values. this is done by converting the image, in the case of this project a png, into its 
RGB values. A string of text is also taken and converted to its ASCII value and than its bianry 
value. if a bit of the message is 1, and the R value is odd, than the R value stays odd. If the 
bit is 0 and the R value is odd, than the R value is changed to an even number. By doing this 
to every pixel value, the message is able to be encrypted into the image.

RUNNING STEG.EXE

To run steg.exe, open the windows cmd and cd to the root directory. This file should also 
contain the image to be encrpted. It can also contain the txt file of the message but is
not necassary. run steg by entering:

steg -e <image.png> <encryptedImageName.png> <message.txt>
 
If the message is not in the txt file, do not enter the last command, instead press enter
after typing the encryptedImageName. After this a prompt will appear to enter the ecrypted
message.

to decrypt the message enter:

steg -d <modifiedImageName> <outPutFileName.txt>

This will decrypt the modified image and append the message to a new txt file.
