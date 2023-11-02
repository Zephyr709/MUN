#Usable Ascii Chars decimal values of 32 - 126
def testForHashCode(bits, dictonary):
    
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

def printProbableMessages(dictonary,fragList):
    for key,value in dictonary.items():
        if value > 40:
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
    
    for message in messageFrags:
        binaryMessageFrags.append(bin(message))
    
    for element in binaryMessageFrags: 
        testForHashCode(element,xorDictionary)
    
    printProbableMessages(xorDictionary,binaryMessageFrags)
    
    
main()

# One of the outputs of the print probable messages functions contains the hash code used for encryption along with # the message and is as follows:
# This message is decyphered with : 190 0b10111110
# https://www.youtube.com/watch?v=Dlto1VQ5Fv4
# 
