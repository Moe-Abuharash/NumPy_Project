import numpy as np
import random

### we have 2 rows and 3 columns
## 1, 2 ,3 represents the high rows
## 4, 5 and 6 represents the lower rows
arr01 = np.array([[1,2,3],
                  [4,5,6]])

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

for row in arr01:
    print(row)
    for col in row:
        print(col, end='')
    print()

for i in arr01.flat:
    print(i)

arr03 = np.zeros(5)
arr04 = np.ones((2, 4), dtype = int)
arr05 = np.full((3, 5), 13)



#Exercise
#################

#create a 2 dimensional arry of integer elements each using the random module
#and list comprehension


a = np.array ([[random.randint(1, 10) for i in range (5)], 
                                [random.randint(1,10) for i in range (5)]]

b = np.array(np.random.randint(1, 10, size = (2, 5)))

arr06 = np.arange(5)

arr07 = np.arange(5, 10)

arr08 = np.arange (10, 1, -2)





print()