'''
Created on Apr 22, 2015

@author: Vijay
'''
import os
import numpy as np
from multiprocessing import Pool
import cProfile

n = None
grid = None

def place_queen(r,c):
    i = r
    if (r == n):
        return True
    for j in range(c,n):
        row_sum = grid[i,:].sum()
        col_sum = grid[:,j].sum()
        super_sum = row_sum + col_sum + diagonal_sum(i, j)
        if(super_sum == 0):
            grid[i,j] = 1
            placed = place_queen(i+1,0)
            if (placed):
                return True
            grid[i,j] = 0
    
    return False
        
    
    
 
def diagonal_sum(r,c): 
    d_sum = 0    
    for x in range(n):
        k = abs(c-x)
        k1 = r-k
        k2 = r+k
        if(k1>=0):
            d_sum += grid[k1,x]
        if(k2<n):
            d_sum += grid[k2,x]

    d_sum -= grid[r,c]
    return d_sum


def test_nQueen(no_queens):
    global n, grid
    n = no_queens
    grid = np.zeros((n,n))
    soln_exists = place_queen(0, 0)
    #info("Process info")
    if(soln_exists):
        print "No of queens =", n
        print grid
    else:
        print "No solution exists for no of queens =", n
        
def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

if __name__ == '__main__':
    runtype = 'single'
    
    #single
    if(runtype == 'single'):
        cProfile.run('test_nQueen(18)')
        
    #multiprocess
    if (runtype == 'multiprocess'):
        queens = range(15,20)
        pool = Pool(processes=len(queens))
        pool.map(test_nQueen,queens)

    
