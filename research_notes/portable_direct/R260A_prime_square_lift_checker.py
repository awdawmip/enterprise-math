"""Exact first prime-square non-lifting witness for R260A.
Run alongside R260_labelled_modular_quotient.py.
"""
from fractions import Fraction as F
from R260_labelled_modular_quotient import reconstruct, sequence

s=F(866,2197)
J,T,K=3327364117,3975468120,36933000
Cs,Qs=reconstruct(s,J,T,K)
q9=sequence(Cs[9],Qs[9],169,6)
q10=sequence(Cs[10],Qs[10],169,6)
assert q9[:2]==[96,139], q9
assert q10[:2]==[18,113], q10
det=(q9[0]*q10[1]-q9[1]*q10[0])%169
assert det==65 and det%13==0
assert pow(q9[0],-1,169)==125
coef=q10[0]*pow(q9[0],-1,169)%169
assert coef==53 and coef*q9[1]%169==100
assert (q10[1]-coef*q9[1])%169==13
print("PASS R260A exact non-lift mod169:", {"q9":q9[:2],"q10":q10[:2],"det":det,"coef":coef})
