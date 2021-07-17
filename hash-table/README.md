# Hashtables

Hash - A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array.

## Challenge

Implement a Hashtable Class with the following methods: add, get, contains and hash

## Approach & Efficiency
time ==> o(1)

## API

1. add: This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

2. get: Returns a value associated with that key in the table if exist

3. contains: Returns a boolean, indicating if the key exists in the table already.

4. hash: Returns the Index in the collection for that key