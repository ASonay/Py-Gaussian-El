import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from MatrixSolve_ import MatrixSolve as ms

def ProveResult(mat,vecx,vecy):
    if all(abs(vecy-np.dot(mat,vecx)) < 1e-10):
        print "Solution is true:"
        print vecx, "\n"
    else:
        print "Solution is wrong!\n"

def PlotText(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            plt.text(j + 0.0, i + 0.0, '%.2f' % mat[i, j],
                     horizontalalignment='center',
                     verticalalignment='center',
                     fontsize=9, color='white',
            )

#Object for matrix solving
solver = ms()

#GAUSSIAN ELIMINATION-----------------------//
print "\nGaussian elimination for matrix A..."
A = np.random.random((5,5))
Y = np.random.random(5)

#Check if matrix applicable
AGE = A.copy()
YGE = Y.copy()
print "Is matrix A applicable for gaussian elimination: ",solver.GaussianElimination(AGE,YGE) == False

#Solve matrix A for vector Ya with
#Gaussian elimination.
X = solver.SolveGE(A,Y)

#Prove vector Xa is the solution.
ProveResult(A,X,Y)

#PRINT WITH PANDA---------------------------//
pd.options.display.float_format = '{:,.2f}'.format
SHOWLM = pd.DataFrame(A)
SHOWLM['MP'] = ['','','X','','']
SHOWLM['X'] = X
SHOWLM['EQ'] = ['','','=','','']
SHOWLM['Y'] = Y
print SHOWLM


#DRAW WITH PYPLOT----------------------------//
plt.subplot(1, 2, 1)
plt.imshow(A);
plt.title("Matrix A")
PlotText(A)
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(AGE);
plt.title("Gaussian El. Effect to Matrix A")
PlotText(AGE)
plt.colorbar()

plt.show()
