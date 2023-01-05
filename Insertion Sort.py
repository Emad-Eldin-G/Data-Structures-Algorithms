""" 
DECLARE myList : ARRAY[0:8] OF INTEGER
DECLARE upperBound : INTEGER
DECLARE lowerBound : INTEGER
DECLARE index : INTEGER
DECLARE key : BOOLEAN
DECLARE place : INTEGER
upperBound ← 8
lowerBound ← 0
FOR index ← lowerBound + 1 TO upperBound
key ← myList[index]
place ← index - 1
IF myList[place] > key
THEN
WHILE place >= lowerBound AND myList[place] > key
temp ← myList[place + 1]
myList[place + 1] ← myList[place]
myList[place] ← temp
place ← place - 1
ENDWHILE
myList[place + 1] ← key
ENDIF
NEXT index
"""