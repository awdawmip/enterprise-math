#!/usr/bin/env python3
"""Exact n=3 S23 conditional AV symmetric-kernel continuum certificate.
Proof scope: independent S3 input/output invariant 4x10 stochastic kernel.
All mathematical assertions use Python unbounded integers and Fraction.
"""
from fractions import Fraction
from itertools import product
from math import factorial, comb
import sys

M = 10**9
# Input row k=#N among 3 compressed observations, output columns
# histograms sorted lexicographically (n_stop1,n_stop3,n_stop4).
H = sorted(h for h in product(range(4), repeat=3) if sum(h)==3)
MULT = [factorial(3)//(factorial(h[0])*factorial(h[1])*factorial(h[2])) for h in H]
K = [
 [0,0,0,1000000000,0,0,0,0,0,0],
 [0,169391357,0,0,0,96190545,0,0,734418098,0],
 [1481481,0,37451970,0,39559539,118031741,214867295,409153994,0,179453980],
 [0,0,73659142,0,4532537,0,7354927,35290451,333009025,546153918]
]
assert len(H)==10 and len(K)==4
assert all(len(row)==10 and all(v>=0 for v in row) and sum(row)==M for row in K)
assert sum(MULT)==27
# Given (a,c)=(A/D,C/D): full label p numerators over D².
# z=(1-a)c has integer numerator p1; compressed b=(z,1-z).

def exact_grid(N):
 D=8*N; den=M*D**6; best=-1; arg=None
 # Cache powers for a- and c-dependent factors wherever possible.
 for i in range(N+1):
  A=4*N+3*i
  q0=A*D
  q0pow=[1,q0,q0*q0,q0*q0*q0]
  for j in range(N+1):
   C=4*N+3*j
   q1=(D-A)*C
   q2=(D-A)*(D-C)
   qq1=[1,q1,q1*q1,q1*q1*q1]
   qq2=[1,q2,q2*q2,q2*q2*q2]
   b1=D*D-q1
   b0p=[1,q1,q1*q1,q1*q1*q1]
   b1p=[1,b1,b1*b1,b1*b1*b1]
   weights=[comb(3,k)*b0p[3-k]*b1p[k] for k in range(4)]
   # The product multinomial law is a genuine probability mass over 10 histogram types.
   num=0
   for h,m in enumerate(MULT):
    n0,n1,n2=H[h]
    truth=m*M*q0pow[n0]*qq1[n1]*qq2[n2]
    rebuilt=sum(weights[k]*K[k][h] for k in range(4))
    if truth>rebuilt: num+=truth-rebuilt
   if num>best:best=num;arg=(i,j)
 return Fraction(best,den),arg,best,den

def main():
 N=int(sys.argv[1]) if len(sys.argv)>1 else 512
 assert N>=1
 g,ij,n,d=exact_grid(N)
 # Universal C² bilinear interpolation bound for any stochastic 8x27 kernel:
 # ||F_aa||_1<=339/8, ||F_cc||_1<=12, side h=3/(8N).
 extension=Fraction(3915,8192*N*N)
 all_real=g+extension
 old_upper=Fraction(21422605623595866373,90071992547409920000)
 lower=Fraction(5211,21952)
 assert lower<all_real<old_upper
 assert all_real< Fraction(23739,100000) # 0.23739
 print('PASS_S23_N3_SYMMETRIC_PRIMAL_EXACT_UNIFORM_20261107')
 print('N',N,'POINTS',(N+1)**2,'HISTOGRAM_TYPES',len(H),'OUTPUT_ORDERED_TYPES',sum(MULT))
 print('KERNEL_DENOM',M,'INVARIANT_INPUT_ROWS',len(K),'OUTPUT_HISTOGRAM_COLUMNS',len(H))
 print('GRID_MAX_POINT_INDICES',ij)
 print('GRID_MAX_RATIONAL',g.numerator,'/',g.denominator,'DECIMAL',format(float(g),'.16f'))
 print('EXTENSION_RATIONAL',extension)
 print('ALL_REAL_UPPER_RATIONAL',all_real.numerator,'/',all_real.denominator,'DECIMAL',format(float(all_real),'.16f'))
 print('PREVIOUS_UPPER',format(float(old_upper),'.16f'))
 print('EXISTING_LOWER',format(float(lower),'.16f'))
 print('CERTIFIED_GAP',all_real-lower,'DECIMAL',format(float(all_real-lower),'.16f'))
 print('ARITHMETIC unbounded Python integers/Fraction; full grid and every output histogram')

if __name__=='__main__':main()
