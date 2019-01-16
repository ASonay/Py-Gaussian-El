import numpy as np
import sys

class MatrixSolve:

    def FindMax(self,mat,i):
        n = mat.shape[0]
        imax = i
        max_pivot = abs(mat[i][i])
        
        for k in range(i+1,n):
            maxv = abs(mat[k][i])
            if maxv > max_pivot:
                max_pivot = maxv
                imax = k

        return imax

    
    def GaussianElimination(self,mat,vec):
        n = mat.shape[0]
        m = mat.shape[1]
        
        if n!=m:
            print("\nNon-squared matrix detected!!")
            print("Try another method...")
            sys.exit()
      
        for k in range(n):
            imax = self.FindMax(mat,k)
            if mat[imax][k] == 0:
                return True
            mat[[imax,k]] = mat[[k,imax]]
            vec[k],vec[imax] = vec[imax],vec[k]
            for i in range(k+1,n):
                c = mat[i][k]/mat[k][k]
                vec[i] = vec[i] - c*vec[k]
                mat[i][k] = 0
                for j in range(k+1,n):
                    mat[i][j] = mat[i][j] - c*mat[k][j]

        return False

    
    def SolveGE(self,m,v):
        mat = m.copy()
        vec = v.copy()
        
        n = mat.shape[0]
        m = mat.shape[1]
        x = [0.] * n

        if n != vec.shape[0]:
            print("\nVector size different than matrix size!\n")
            sys.exit()

        cond = self.GaussianElimination(mat,vec)
        
        if cond == True:
            print("\nSingular matrix detected!!")
            print("Try another method...")
            sys.exit()
        
        for i in range(n-1,-1,-1):
            s = 0.
            for j in range(i+1,n):
                s = s + mat[i][j]*x[j]
            x[i] = (vec[i] - s) / mat[i][i]

        return x
