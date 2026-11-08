#!/usr/bin/env python3
"""PREFIX-590-R6: exact finite-window native BRC cubic-observer rank."""
from fractions import Fraction as F
from collections import defaultdict
import json
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, edge, ACTIONS, ZERO_ROOT

assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
assert len(ACTIONS)==6
EXP=[(a,b,d-a-b) for d in range(4)
     for a in range(d+1) for b in range(d-a+1)]
assert len(EXP)==20

def conditional_moments(n):
    rows=[]
    for start in range(96):
        state={(start,0,0,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (port,t,p0,p1),m in state.items():
                for act in ACTIONS:
                    j,w=edge(port,act,ZERO_ROOT)
                    dt=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
                    nxt[(j,t+dt,p0+w[0]+w[1],p1+w[2]+w[3])]+=m
            state=nxt
        assert sum(state.values())==6**n
        rows.append([sum(m*t**a*p0**b*p1**c
                     for (_,t,p0,p1),m in state.items()) for a,b,c in EXP])
    return rows

def col_basis(matrix):
    A=[[F(x) for x in row] for row in matrix]
    piv=[];rank=0;n=len(A);m=len(A[0])
    for j in range(m):
        i=next((i for i in range(rank,n) if A[i][j]),None)
        if i is None:continue
        A[rank],A[i]=A[i],A[rank]
        q=A[rank][j]
        for k in range(j,m):A[rank][k]/=q
        for i in range(rank+1,n):
            if A[i][j]:
                q=A[i][j]
                for k in range(j,m):A[i][k]-=q*A[rank][k]
        piv.append(j)
        rank+=1
        if rank==n:break
    return piv

def det_mod(A,p):
    A=[[x%p for x in row] for row in A]
    n=len(A);result=1
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None:return 0
        if j!=k:A[j],A[k]=A[k],A[j];result=-result
        q=A[j][j]
        result=result*q%p
        inv=pow(q,-1,p)
        for i in range(j+1,n):
            if A[i][j]:
                f=A[i][j]*inv%p
                for k in range(j+1,n):
                    A[i][k]=(A[i][k]-f*A[j][k])%p
                A[i][j]=0
    return result%p

stack=[];per_depth=[];prefix=[];piv=[]
for depth in range(9):
    M=conditional_moments(depth)
    per_depth.append(len(col_basis(M)))
    stack=M if not stack else [r+s for r,s in zip(stack,M)]
    piv=col_basis(stack)
    prefix.append(len(piv))
assert per_depth==[1,6,9,16,14,16,16,16,16]
assert prefix==[1,6,14,22,30,33,33,33,33]
expected_piv=[0,21,22,23,27,29,41,42,43,47,48,49,57,59,
              63,67,68,69,71,74,75,76,83,87,88,89,94,97,98,99,103,107,108]
assert piv==expected_piv
basis=[[row[j] for j in piv] for row in stack]
basis_row_ids=col_basis(list(map(list,zip(*basis))))
expected_rows=[0,2,4,6,7,8,10,12,14,16,18,20,22,24,28,32,
               34,36,38,42,46,48,50,52,54,56,60,64,68,72,76,80,84]
assert basis_row_ids==expected_rows
minor=[[stack[i][j] for j in piv] for i in basis_row_ids]
p=1000003;d=det_mod(minor,p)
assert d==325742
result={
 "schema":"PREFIX590_R6_NATIVE_BRC_CUBIC_FINITE_WINDOW_RANK_V1",
 "status":"ALL_CHECKS_PASS",
 "science_pin":SCIENCE_PIN,
 "native_ports":96,"actions":6,"root":"ZERO_ROOT",
 "depth_range":[0,8],"moments_per_depth":20,
 "individual_ranks":per_depth,"cumulative_ranks":prefix,
 "stacked_matrix_shape":[96,180],"stacked_rank":33,
 "minimal_normalized_variable_linear_statistics":32,
 "basis_columns":piv,"witness_port_rows":basis_row_ids,
 "modulus":p,"minor_det_mod":d,
 "scope":"exact finite horizon 0..8, uniform action kernel, arbitrary initial-port laws",
 "all_length_rank":"OPEN; invariant-subspace proof required"
}
print("ALL_CHECKS_PASS")
print(json.dumps(result,indent=2))
