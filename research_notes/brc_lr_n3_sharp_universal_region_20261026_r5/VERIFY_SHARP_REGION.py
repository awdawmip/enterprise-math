#!/usr/bin/env python3
"""Independent Fraction Bellman and probability validator for two N=3 sharp-region witnesses."""
from fractions import Fraction as F
from itertools import product

R=(F(1,2),F(1),F(3,2))

def H(r,A,B):
    return min(A*r,B)

def witness(name,alpha,beta,A,B,gamma,terminal):
    # terminal: dict of r -> tuples (Y,Q-prob). All probabilities are Q-conditional.
    assert 0<alpha<=beta<F(1,2)
    rows=[(alpha,F(1)-2*alpha,alpha),(beta,F(1)-2*beta,beta)]
    for row in rows:
        assert sum(row)==1 and all(x>0 for x in row)
        assert sum(x*y for x,y in zip(row,R))==1
    for r,pairs in terminal.items():
        assert r in R and sum(q for y,q in pairs)==1 and all(y>0 and q>0 for y,q in pairs)
        assert sum(y*q for y,q in pairs)==r
        assert sum(y*q/r for y,q in pairs)==1
    terminal_v={r:min(H(r,A,B),gamma+sum(q*H(y,A,B) for y,q in terminal[r])) for r in R}
    f=[sum(q*terminal_v[r] for q,r in zip(row,R)) for row in rows]
    full1=[min(H(F(1),A,B),gamma+f_i) for f_i in f]
    full=min(H(F(1),A,B),gamma+sum(full1)/2)
    lr1=min(H(F(1),A,B),gamma+sum(f)/2)
    lr=min(H(F(1),A,B),gamma+lr1)
    d0=H(F(1),A,B)-terminal_v[F(1)]
    G=2*terminal_v[F(1)]-terminal_v[F(1,2)]-terminal_v[F(3,2)]
    da=H(F(1),A,B)-f[0]
    db=H(F(1),A,B)-f[1]
    assert (da,db)==(d0+alpha*G,d0+beta*G)
    assert full<lr
    print(name)
    for k,v in [('alpha',alpha),('beta',beta),('gamma',gamma),('d0',d0),('G',G),('da',da),('db',db),('V_full',full),('V_LR',lr),('gap',lr-full)]:print(' ',k,'=',v)
    return full,lr

small=F(1,100)
terminal_pos={r:((r-small,F(1,2)),(r+small,F(1,2))) for r in R}
witness('BETA_GT_3ALPHA',F(1,12),F(1,3),F(2),F(2),F(5,48),terminal_pos)
terminal_neg={R[0]:((R[0]-small,F(1,2)),(R[0]+small,F(1,2))),
              R[1]:((F(1,2),F(3,4)),(F(5,2),F(1,4))),
              R[2]:((R[2]-small,F(1,2)),(R[2]+small,F(1,2)))}
witness('THREE_BETA_MINUS_ALPHA_GT_1',F(1,4),F(9,20),F(46,5),F(92,5),F(3,20),terminal_neg)
print('ALL_EXACT_CHECKS_PASS')
