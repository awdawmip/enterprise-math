"""Exact rank-minor check for source-aware 3-key stopping model."""
from fractions import Fraction as Q
import VERIFY as V

half=Q(1,2)
cols=[]
for i in range(4):
    lo=[half]*7
    hi=[half]*7
    lo[i]=Q(0)
    hi[i]=Q(1)
    a=V.physical(*lo)
    b=V.physical(*hi)
    cols.append(tuple(b[k]-a[k] for k in range(4)))
M=[[cols[j][i] for j in range(4)] for i in range(4)]
print("3-key FULL Jacobian columns (x,jB,jI,kC):", cols)
d=V.det(M)
assert d==Q(-1,5120), (d, M)
print("det J_FULL(x,jB,jI,kC) at all seven parameters =1/2:", d)
print("PASS_EXACT_R5_THREE_KEY_FULL_JACOBIAN_RANK4")
