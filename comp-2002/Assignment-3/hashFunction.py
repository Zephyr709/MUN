#Usable Ascii Chars decimal values of 32 - 126
def testForHashCode(bits, dictonary):
    """ This function parses 32-bit binary integers into 8-bit chunks representing characters
        it then tests every possible XOR value from 0-255, and if the result lands within the acceptable 
        realm of characters to construct a message, adds the hash code as a key in the dictionary and increments
        its correlated value by 1 to illustrate the most probable hash codes to create a understandable message.

    Args:
        bits (string): 34 character long string that represents a 32-bit integer
        dictonary (dictionary): dictionary to store the frequency of a succesful hash code
    """
    #Parses the 32-bits into 8-bits representing chars
    i = 2
    chars = []
    while i < len(bits):
        chars.append(int(bits[i:i+8],2))
        #print(chars)
        i+= 8
    
    for element in chars:
        #print("The element is:", element)
        for i in range(0,256):
            xorResult = element ^ i
            #print(xorResult)
            if xorResult >= 32 and xorResult < 127:
                #print(xorResult, i)
                
                if i in dictonary: 
                    #print(dictonary.get(i))
                    dictonary[i] = dictonary.get(i) + 1
                else:
                    dictonary[i] = 1

def printProbableMessages(dictonary,fragList,frequencyThreshold):
    """ This function prints out all the total messages that get decyphered by each hash code with a frequency greater than the threshold in the possible hash code dictionary.
       

    Args:
        dictonary (Dictionary): dictionary containing the possible hash codes and the frequency
                                they generated an acceptable character
        fragList (List): a list containing all the fragments of the message in binary form
        frequencyThreshold (Integer): an integer that represents the frequency threshold of the hash codes to check
    """
    for key,value in dictonary.items():
        if value > frequencyThreshold:
            message = ""
            print("This message is decyphered with :", key, bin(key))
            
            for element in fragList:
                
                x = 2
                chars = []
                while x < len(element):
                    chars.append(int(element[x:x+8],2))
                    x+= 8
                
                for item in chars:
                    message += chr(key ^ item)
            
            print(message)
            print()



def main():
    messageFrags = [3603614414, 3448017297, 3385444752, 3352415178, 3420248976, 3721515921, 3386886877, 3598829699, 4208118481, 2414407563, 4173892254]
    
    binaryMessageFrags =[]
    xorDictionary = {}
    
    #converts each integer into its binary representation
    for message in messageFrags:
        binaryMessageFrags.append(bin(message))
    
    # For each binary represented integer tests for hash codes that provide succesful letters
    for element in binaryMessageFrags: 
        testForHashCode(element,xorDictionary)
    
    printProbableMessages(xorDictionary,binaryMessageFrags,40)
    
    
main()

# One of the outputs of the print probable messages functions contains the hash code used for encryption along with # the message and is as follows:
# This message is decyphered with : 190 0b10111110
# https://www.youtube.com/watch?v=Dlto1VQ5Fv4
# 
