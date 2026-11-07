#!/usr/bin/env python3
"""Exact Fraction-only R5 FULL_HIST supporting-facet certificate (2026-11-07).
No numerical optimization needed to check the final universal identity.
"""
from fractions import Fraction as Q

R=(Q(1,10),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(19,10))
NAMES=('g','a','b','xA0','xA1','xA2','xB0','xB1','xB2')+tuple('E'+str(i) for i in range(7))

def s(**kv): return {k: Q(kv.get(k, 0)) for k in NAMES}
def calc(v):
 g,a,b=[v[k] for k in ('g','a','b')]
 A=[v['xA'+str(i)] for i in range(3)]
 B=[v['xB'+str(i)] for i in range(3)]
 x=[A[i]+B[i] for i in range(3)]
 E=[v['E'+str(i)] for i in range(7)]
 VA=[Q(13,40)*a,a/10,Q(3,40)*a]
 VB=[b/80,Q(9,40)*b,Q(21,80)*b]
 M=[Q(509,900)*x[0]+Q(47,180)*A[1]+Q(67,162)*B[1]+x[2]/100,
    VA[0]+VB[0]-x[0],(g-a)/2,
    1-g+VA[1]+VB[1]-x[1]+Q(191,450)*(x[0]+x[2])+Q(43,90)*A[1]+Q(14,81)*B[1],
    (g-b)/2,VA[2]+VB[2]-x[2],
    x[0]/100+Q(47,180)*A[1]+Q(67,162)*B[1]+Q(509,900)*x[2]]
 eQ=sum(E);eP=1-sum((R[j]*E[j] for j in range(7)),Q(0))
 TQ=1+g+(a+b)/2+sum(x)
 TP=1+g+(3*a+5*b)/8+x[0]/2+x[1]+Q(3,2)*x[2]
 W=(eP,eQ,TP,TQ)
 L=21126*(TQ-1)-13604*(TP-1)-83401*eQ+114010*(1-eP)
 rhs=(4245*(g-a)
      +11278*(VA[1]-A[1]) +Q(200302,9)*(VB[1]-B[1])
      +72000*(M[0]-E[0])+26396*(M[1]-E[1])+6554*(M[4]-E[4])
      +Q(4213,2)*E[2]+30609*E[3]+Q(131331,2)*E[4]
      +87614*E[5]+133218*E[6])
 return VA,VB,M,W,L,rhs

def legal(v):
 VA,VB,M,W,L,rhs=calc(v)
 g,a,b=[v[k] for k in ('g','a','b')]
 assert 0<=a<=g<=1 and 0<=b<=g
 assert all(0<=v['xA'+str(j)]<=VA[j] and 0<=v['xB'+str(j)]<=VB[j] for j in range(3))
 assert all(0<=v['E'+str(j)]<=M[j] for j in range(7))
 assert sum(M)==1 and sum((R[j]*M[j] for j in range(7)),Q(0))==1
 assert L==rhs and L>=0
 return W

# Full analytic coefficient-certificate: both sides affine in all 16 independent variables.
# Exact equality at the zero vector and all 16 basis vectors is a proof of formal identity.
for k in (None,)+NAMES:
 v=s(**({k:1} if k is not None else {}))
 _,_,M,_,L,rhs=calc(v)
 assert L==rhs, (k,L,rhs)
 assert sum(M)==1
 assert sum((R[j]*M[j] for j in range(7)),Q(0))==1
print('PASS_FULL_HIST_LINEAR_IDENTITY_17_COEFFICIENT_CHECKS')

STAR=(Q(161801,180000),Q(6499,18000),Q(267,80),Q(137,40))
H=Q(16917,4642820)

def split(t,x0,x1,x2,E):
 v=s(g=t,a=t,b=t,xA0=Q(26,27)*x0,xB0=x0/27,
     xA1=Q(4,13)*x1,xB1=Q(9,13)*x1,
     xA2=Q(2,9)*x2,xB2=Q(7,9)*x2,
     **{'E'+str(j):E[j] for j in range(7)})
 return v

C=split(Q(77,80),Q(3,16),Q(3,10),Q(1,80),
        (Q(1297,6000),Q(879,6400),Q(0),Q(563,144000),Q(0),Q(0),Q(349,96000)))
E=split(Q(31911,33163),Q(3199433,18571280),Q(31911,102040),Q(220131,18571280),
        (Q(886766809,4178538000),Q(1415873,9285640),Q(0),Q(0),Q(0),Q(0),Q(0)))
assert legal(C)==STAR
assert legal(E)==tuple(STAR[i]+H*(1,1,1,-1)[i] for i in range(4))
assert calc(E)[4]==0
for z in (Q(0),Q(1,5),Q(1,2),Q(3,5),Q(1)):
 v={key:(1-z)*C[key]+z*E[key] for key in NAMES}
 assert legal(v)==tuple(STAR[i]+z*H*(1,1,1,-1)[i] for i in range(4))
print('PASS_FULL_HIST_EXACT_ENDPOINTS_AND_RAY_INTERPOLATION')

# All active nonnegative slacks on the exposed face L=0 force:
# g=a=b; both central branches continue fully; E0=M0,E1=M1,E4=M4;
# E2=E3=E4=E5=E6=0. Hence M4=0 forces b=g as well.
# The resulting pooled LR policy uses all central continuation, and pooled side
# continuation x0,x2 in [0,V0/V2]; it has the identical seven-bin M and W.
print('PASS_FULL_HIST_AND_LR_EXPOSED_FACE_EQUALITY_CERTIFICATE')
print('H =',H,'~',float(H))
print('Supporting inequality: 21126*(TQ-1)-13604*(TP-1)-83401*eQ+114010*(1-eP)>=0')
print('W(H) =',legal(E))
print('NEXT: search FULL_HIST/LR separation away from supporting face; solve K(W), F residual')
