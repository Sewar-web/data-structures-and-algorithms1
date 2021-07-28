# Challenge Summary
rite a function that LEFT JOINs two hashmaps into a single data structure. The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values. The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values. Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic. LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.



## Whiteboard Process

![img](code34.png)

## Approach & Efficiency

bigo(n^2)

## Solution

```
def left_join( hash , hash1):
    
    words = []

    for value in  hash.keys():

        if value in hash1.keys():
            words.append([value, hash [value],hash1[value] ])
            
            

        else:

            words.append([value, hash [value],'NULL' ])
            

    return words
    
```
