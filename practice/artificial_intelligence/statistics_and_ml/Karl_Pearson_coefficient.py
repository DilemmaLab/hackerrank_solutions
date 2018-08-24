#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import statistics

# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem
# Problem:
# Here are the test scores of 10 students in physics and history:

# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15

# Compute Karl Pearson’s coefficient of correlation between these scores.
# Compute the answer correct to three decimal places.

# Output Format

# In the text box, using the language of your choice, print the floating point/decimal value required. Do not leave any leading or trailing spaces.

# For example, if your answer is 0.255. In python you can print using

# print("0.255")

# This is NOT the actual answer - just the format in which you should provide your answer.


x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

x_avg = statistics.mean(x)
x[:] = [round(item - x_avg, 1) for item in x]

y_avg = statistics.mean(y)
y[:] = [round(item - y_avg, 1) for item in y]



x_y_sum_of_multiplications = sum([round(xi*yi,1) for xi,yi in zip(x,y)])
x_y_square_root_of_quadro_power = math.sqrt(sum([round(xi*xi,1) for xi in x])*sum([round(yi*yi,1) for yi in y]))
r = round(x_y_sum_of_multiplications/x_y_square_root_of_quadro_power, 2)

print(r)
