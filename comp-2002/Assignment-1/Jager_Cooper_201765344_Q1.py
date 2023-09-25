# Jager Cooper
# 201765344

import math

def question1(m,n,p):
    if n < 1:
        return m + p
    if p < 1:
        return m + n
    
    return question1(m, math.log2(n), math.log2(p)) + question1(m, n/2, question1(m,n,math.log2(p)))
