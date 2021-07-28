import os 

def left_join( hash , hash1):
    
    words = []

    for value in  hash.keys():

        if value in hash1.keys():
            words.append([value, hash [value],hash1[value] ])
            
            

        else:

            words.append([value, hash [value],'NULL' ])
            

    return words



if __name__ == "__main__":
    hash = {                                        
    'fond':'enamored',
    'wrath':'anger',
    'diligent':'employed',
    'outfit':'garb',
    'guide':'usher'
          }

    hash1 = {
    'fond':'averse',
    'wrath':'delight',
    'diligent':'idle',
    'guide':'follow',
    'flow':'jam'
           }
   
    print(left_join(hash,hash1) )
    