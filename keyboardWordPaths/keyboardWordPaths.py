# Created by http://puzzling.stackexchange.com/users/18429/spiritfryer on 2016-01-26.

# This program was written to answer the question at http://puzzling.stackexchange.com/questions/25789/the-keyboard-word-paths

# `sowpods.txt` is a list of English words which I downloaded from https://raw.githubusercontent.com/jmlewis/valett/master/scrabble/sowpods.txt

# Find four- and five-letter words
fours = set()
fives = set()
with open("sowpods.txt", "r") as f:
  for word in f:
    if(len(word) == 5):
      fours.add(word[:-1])
    elif(len(word) == 6):
      fives.add(word[:-1])

# Set-up our keyboard layout. The 0s make it easy to loop over the possibilities and just ignore the ones involving 0s.
rows = [
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
['0', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '0'],
['0', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '0', '0'],
['0', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
]

# found[0] = Triangle, [1] = Open Rhombus, [2] = Rhombus
found = [[], [], []]

# `check` checks a given word `s` of type `type` (0 = Triangle, 1 = Open Rhombus, 2 = Rhombus) 
# and adds it to the relevant `found` list if it's an English word.
def check(s, type):
  global found
  
  if not '0' in s:
    if (type == 0 or type == 1):
      if s in fours:
        found[type].append(s)
    elif type == 2:
      if s in fives:
        found[type].append(s)
   
# Loop through our keyboard layout's letters.
for i in range(1, len(rows) - 2):
  for j in range(len(rows[i]) - 2):
    if rows[i][j] != '0':
      # Triangles: DES, DSX, DXC, DCF, DFR, DRE, DER, DRF, DFC, DCX, DXS, DSE. 
      for k in [[[-1, 0], [0, -1]],
               [[0, -1], [1, -1]],
               [[1, -1], [1, 0]],
               [[1, 0], [0, 1]],
               [[0, 1], [-1, 1]],
               [[-1, 1], [-1, 0]],
               [[-1, 0], [-1, 1]],
               [[-1, 1], [0, 1]],
               [[0, 1], [1, 0]],
               [[1, 0], [1, -1]],
               [[1, -1], [0, -1]],
               [[0, -1], [-1, 0]]]:
        check(rows[i][j] + rows[i + k[0][0]][j + k[0][1]] + 
              rows[i + k[1][0]][j + k[1][1]] + rows[i][j], 0)
      
      # Open-Rhombuses: DEWS, DSXC, DXCF, DCVF, DFRE, DRES, DERF, 
      #                 DRTF, DFVC, DFCX, DCXS, DXZS, DSWE.
      for k in [[[-1, 0], [-1, -1], [0, -1]],
                [[0, -1], [1, -1], [1, 0]],
                [[1, -1], [1, 0], [0, 1]],
                [[1, 0], [1, 1], [0, 1]],
                [[0, 1], [-1, 1], [-1, 0]],
                [[-1, 1], [-1, 0], [0, -1]],
                [[-1, 0], [-1, 1], [0, 1]],
                [[-1, 1], [-1, 2], [0, 1]],
                [[0, 1], [1, 1], [1, 0]],
                [[0, 1], [1, 0], [1, -1]],
                [[1, 0], [1, -1], [0, -1]],
                [[1, -1], [1, -2], [0, -1]],
                [[0, -1], [-1, -1], [-1, 0]]]:
        word = (rows[i][j] + rows[i + k[0][0]][j + k[0][1]] + 
                rows[i + k[1][0]][j + k[1][1]] + rows[i + k[2][0]][j + k[2][1]])
        check(word, 1)
        
        # Rhombuses - just add current letter.
        check(word + rows[i][j], 2)

types = ["triangles", "open-rhombuses", "rhombuses"]
for i in range(3):
  print "{} {} found{}".format(len(found[i]), types[i], ':' if len(found[i]) > 0 else '.')
  for word in found[i]:
    print word
  print
  
