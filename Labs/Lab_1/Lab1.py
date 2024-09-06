# Q6
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'generateNNaturalNumbers' function below.
#
# The function is expected to return a numpy array.
# The function accepts an INTEGER n as parameter.
#

def generateNNaturalNumbers(n):
    # Write your code here
    if n >=1:
        x = np.arange(1,n+1)
        return x
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = generateNNaturalNumbers(n)

    fptr.write(', '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Q7
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'pacmanScore' function below.
#
# The function is expected to return a np scalar int.
# The function accepts following parameters:
#  1. np scalar float time
#  2. np scalar int dots
#  3. np scalar int berries
#  4. np scalar int ghosts
#

def pacmanScore(time, dots, berries, ghosts):
    # Write your code here. REMEMBER TO RETURN AN INTEGER
    intege = 10 * max((np.subtract(time, 30)), 0) + np.multiply(20, dots) + np.multiply(50, berries) + np.multiply(100, ghosts)
    return int(intege)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    time,dots,berries,ghosts = [float(val) for val in input().strip().split()]
    
    time = np.asarray(time,dtype=np.float64)
    dots = np.asarray(dots,dtype=int)
    berries = np.asarray(berries,dtype=int)
    ghosts = np.asarray(ghosts,dtype=int)
    result = pacmanScore(time, dots, berries, ghosts)
    fptr.write(str(result) + '\n')

    fptr.close()

#Q8
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'calculateBMI' function below.
#
# The function is expected to return an np scalar float.
# The function accepts following parameters:
#  1. np scalar float height
#  2. np scalar float weight
#

def calculateBMI(height, weight):
    # Write your code here
    height_in_m = np.divide(height, 100)
    BMI = np.divide(weight, np.square(height_in_m))
    return np.round(BMI, 2)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    height = np.array(float(input().strip()))

    weight = np.array(float(input().strip()))

    result = calculateBMI(height, weight)

    fptr.write(str(result) + '\n')

    fptr.close()


# Q9
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'calculateBMI' function below.
#
# The function is expected to return a numpy vector.
# The function accepts following parameters:
#  1. numpy vector of floats heights
#  2. numpy vector of floats weights
#

def calculateBMI(heights, weights):
    # Write your code here
    heights_in_m = np.divide(heights, 100)
    BMIs = np.divide(weights, np.square(heights_in_m))
    return np.round(BMIs, 2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    heights = np.asarray([float(height) for height in input().strip().split()])

    weights = np.asarray([float(weight) for weight in input().strip().split()])


    result = calculateBMI(heights, weights)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Q10
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

def billionaire_influence(current_landscape, demands):
    # Hint: Column Broadcast
    # Write your code here
    current_landscape = current_landscape + demands
    return current_landscape
    



def politician_influence(current_landscape, index, update_amount):
    # Hint : Column Broadcast
    # write your code here
    current_landscape[:,index] = current_landscape[:,index] + update_amount
    return current_landscape
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    type_of_testcase, m,n = [int(i) for i in input().strip().split()]
    

    current_landscape = []

    for _ in range(m):
        current_landscape.append(list(map(int, input().rstrip().split())))
    current_landscape = np.array(current_landscape)
    if type_of_testcase == 1:
        demands = list(map(int, input().rstrip().split()))
        demands = np.array(demands)
        result = billionaire_influence(current_landscape, demands)
    else:
        index, update_amount = [int(i) for i in input().strip().split()]
        result = politician_influence(current_landscape, index, update_amount)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


# Q11
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'getMultiplicationTable' function below.

def getMultiplicationTable(multiply_with_left, multiply_with_right):
    # Write your code here
    right = np.reshape(multiply_with_right, (4,1))
    table = np.multiply(multiply_with_left, right).T
    return table
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    multiply_with_left = np.array([int(i) for i in input().strip().split()])
    multiply_with_right = np.array([int(i) for i in input().strip().split()])

    result = getMultiplicationTable(multiply_with_left, multiply_with_right)
    ans = ""
    for i in result:    
        ans +=(" ".join([str(np.round(j,2)) for j in i]))
        ans+='\n'
    fptr.write(ans)

    fptr.close()


#Q12
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'softmax_preprocess' function below.
#
# The function is expected to return a 2D numpy array.
# The function accepts 2D numpy array y as parameter.
#

def softmax_preprocess(y):
    # Write your code here
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    y_rows,y_columns = [int (i) for i in input().strip().split()]

    y = []

    for _ in range(y_rows):
        y.append(list(map(float, input().rstrip().split())))

    result = softmax_preprocess(np.array(y))
    result = np.round(result,2)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
