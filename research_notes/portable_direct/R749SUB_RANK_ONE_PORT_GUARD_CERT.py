#!/usr/bin/env python3
"""Exact rational regression for WBRC rank-one port-feedback stability.
Proof for arbitrary finite n is in the companion markdown manuscript.
"""
from fractions import Fraction as F
from itertools import product
import json

Q = [F(0), F(1,4), F(1,2), F(3,4)]
T = [F(0), F(1,4), F(1,2), F(3,4), F(1), F(5,4), F(3,2), F(2)]

def stable_2(W):
    a,b,c,d=W
    return a < 1 and d < 1 and (1-a)*(1-d)-b*c > 0

def inverse_star_2(W):
    a,b,c,d=W
    det=(1-a)*(1-d)-b*c
    assert det > 0
    return ((1-d)/det,b/det,c/det,(1-a)/det)

def grid_bin(s,K,M):
    if s==0: return 0
    # unstable for j*s>=K, j in 1,...,M
    return sum(j*s>=K for j in range(1,M+1))

def vector(W,K,M):
    s00,s01,s10,s11=inverse_star_2(W)
    return tuple(grid_bin(s,K,M) for s in (s00,s10,s01,s11))

def main():
    checked=0
    matrices=0
    equalities=0
    grid_checks=0
    for W in product(Q,repeat=4):
        if not stable_2(W): continue
        matrices+=1
        s00,s01,s10,s11=inverse_star_2(W)
        for i,j,s in [(0,0,s00),(0,1,s10),(1,0,s01),(1,1,s11)]:
            for t in T:
                X=list(W)
                X[2*i+j]+=t
                actual=stable_2(X)
                predicted=t*s<1
                assert actual==predicted,(W,i,j,t,actual,predicted)
                checked+=1
                equalities+=(t*s==1)
        for K in range(2,9):
            for M in range(1,K):
                bins=vector(W,K,M)
                for i,j,s,h in [(0,0,s00,bins[0]),(0,1,s10,bins[1]),(1,0,s01,bins[2]),(1,1,s11,bins[3])]:
                    obs=sum(not stable_2(tuple(W[k]+(F(t,K) if k==2*i+j else 0) for k in range(4))) for t in range(1,M+1))
                    assert obs==h
                    grid_checks+=1
    W1=(F(1,2),F(0),F(0),F(1,2))
    W2=(F(1,4),F(1,4),F(3,4),F(1,4))
    S1=inverse_star_2(W1); S2=inverse_star_2(W2)
    assert (S1[0],S1[3])==(S2[0],S2[3])==(F(2),F(2))
    assert S1[2]==0 and S2[2]==2
    P=[F(1,4),F(1,2),F(3,4)]
    assert all(stable_2((W1[0]+t,W1[1],W1[2],W1[3]))==stable_2((W2[0]+t,W2[1],W2[2],W2[3])) for t in P)
    assert stable_2((W1[0],W1[1]+F(1,2),W1[2],W1[3]))
    assert not stable_2((W2[0],W2[1]+F(1,2),W2[2],W2[3]))
    result={"status":"PASS","rational_matrix_grid":"{0,1/4,1/2,3/4}^4","stable_matrices":matrices,"rank_one_guard_checks":checked,"tested_feedback":"0,1/4,1/2,3/4,1,5/4,3/2,2","critical_equalities":equalities,"finite_feedback_class_checks":grid_checks,"finite_grid_K":"2..8","finite_grid_M":"1..K-1","counterexample":{"W1":["1/2","0","0","1/2"],"W2":["1/4","1/4","3/4","1/4"],"diagonal_star":["2","2"],"cross_star_S_21":["0","2"],"separating_feedback":"E12/2"},"proof_scope":"All finite nonnegative-rational stable n-port W by determinant lemma and nonnegative inverse; finite regression only n=2"}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return result
if __name__=='__main__': main()
