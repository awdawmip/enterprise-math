#!/usr/bin/env python3
"""Exact 9D physical / 8D statistical fixed 14-edge R5 Blackwell chamber.
Requires SymPy exact Rational arithmetic and predecessor VERIFY_2D.py."""
from fractions import Fraction as F
from pathlib import Path
from runpy import run_path
import sympy as s

p=Path(__file__).resolve().parents[1]/"brc_r5_two_dimensional_14edge_fan_20261109_t11"/"VERIFY_2D.py"
c=run_path(str(p))
R=c["R"];X0=c["X0"];X1=c["X1"];Y0=c["Y0"];Y1=c["Y1"]
SA=c["SA"];A0=c["A0"];AH=c["AH"];D=c["D"];DX=c["DX"];DY=c["DY"]
Q=c["Q"];add=c["add"];linear=c["linear"];masses=c["masses"];times=c["times"]
slack=c["slack"];lawful=c["lawful"];verify=c["verify"]
K=Q("-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1")
DX2=tuple(x-y for x,y in zip(DX,K))
L=F(1,4);DEL=F(1,240);EPS=F(1,100000)
x=add(linear(X0,X1,L),DX2,DEL)
y=add(linear(Y0,Y1,L),DY,DEL)
w=tuple((1-2*L)*a+2*L*b+DEL*D.get(k,F(0)) for k,a,b in zip(SA,A0,AH))
assert lawful(x) and lawful(y) and x[0]==x[2]
assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
assert times(x)==times(y)
assert sum(masses(x))==sum(masses(y))==1
assert verify(SA,w,x,y)[0]==14

g,a,b,u,v,q,z=s.symbols("g a b u v q z")
symbols=(g,a,b,u,v,q,z)
Mexpr=masses(symbols);Texpr=times(symbols)
M=s.Matrix([[s.diff(m,par) for par in symbols] for m in Mexpr])
T=s.Matrix([[s.diff(t,par) for par in symbols] for t in Texpr])
C=s.zeros(26,28)
for i in range(7):
    for k in range(7): C[i,7+k]=-M[i,k]
    for h,(ii,jj) in enumerate(SA):
        if i==ii:C[i,14+h]+=1
for j in range(7):
    for k in range(7): C[7+j,k]=-M[j,k]
    for h,(ii,jj) in enumerate(SA):
        if j==jj:C[7+j,14+h]+=1
for j in range(7):
    for h,(ii,jj) in enumerate(SA):
        if j==jj:C[14+j,14+h]+=s.Rational(R[ii].numerator,R[ii].denominator)
    C[14+j,:7]-=s.Rational(R[j].numerator,R[j].denominator)*M[j,:]
C[21,0]=1;C[21,2]=-1
C[22,13]=1;C[22,8]=-s.Rational(1,10)
C[23,11]=1;C[23,13]=-1;C[23,9]=-s.Rational(9,40)
C[24,:7]=T[0,:]; C[24,7:14]=-T[0,:]
C[25,:7]=T[1,:]; C[25,7:14]=-T[1,:]
assert C.rank()==19
N=C.nullspace()
assert len(N)==9
assert all(C*vec==s.zeros(26,1) for vec in N)
directions=[(tuple(F(t) for t in vec[:7,0]),
             tuple(F(t) for t in vec[7:14,0]),
             tuple(F(t) for t in vec[14:,0])) for vec in N]

base_slacks=slack(x)+slack(y)
deriv_slacks=[tuple(t0-t1 for t0,t1 in zip(
     slack(add(x,dx,F(1)))+slack(add(y,dy,F(1))),base_slacks))
     for dx,dy,dw in directions]
assert tuple(i for i,t in enumerate(base_slacks) if t==0)==(4,23,25)
assert all(all(ds[i]==0 for ds in deriv_slacks) for i in (4,23,25))
ratios=[]
for i,value in enumerate(base_slacks):
    norm=sum(abs(ds[i]) for ds in deriv_slacks)
    if norm:ratios.append(value/norm)
for i,value in enumerate(w):
    norm=sum(abs(dw[i]) for dx,dy,dw in directions)
    if norm:ratios.append(value/norm)
rmin=min(ratios)
assert rmin==F(1181037643981,2086671428467200)
assert EPS<rmin
assert min(w)>0
assert all(value>EPS*sum(abs(dw[i]) for dx,dy,dw in directions) for i,value in enumerate(w))

def increment(f,d,fun):
    return tuple(t1-t0 for t0,t1 in zip(fun(f),fun(add(f,d,F(1)))))
def rat(q):return s.Rational(q.numerator,q.denominator)
O=s.Matrix.hstack(*[
    s.Matrix([rat(v) for v in increment(x,dx,masses)+increment(y,dy,masses)+increment(x,dx,times)])
    for dx,dy,dw in directions])
assert O.shape==(16,9) and O.rank()==8
obs_minor=O[list((0,1,2,3,7,8,9,10)),1:].det()
assert obs_minor==s.Rational(1,6)
phys=s.Matrix.hstack(*[s.Matrix([rat(t) for t in dx+dy]) for dx,dy,dw in directions])
assert phys.rank()==9
phys_minor=phys[list((0,1,3,4,5,6,7,8,9)),:].det()
assert phys_minor==-s.Rational(83980800000,1111424393)
print("PASS_EXACT_AFFINE_CONSTRAINT_RANK",C.rank(),"KERNEL_DIMENSION",len(N))
print("PASS_EXACT_9D_UNIFORM_CUBE_EPS",EPS,"DIRECT_L1_BOUND",rmin)
print("PASS_EXACT_PHYSICAL_RANK_9_MINOR",phys_minor)
print("PASS_EXACT_STATISTICAL_IMAGE_RANK_8_MINOR",obs_minor)
print("THEOREM_ALL_REAL_9D_PHYSICAL_8D_STATISTICAL_FIXED_14_EDGE_CHAMBER")
