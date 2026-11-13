#!/usr/bin/env python3
"""PREFIX579-R2: exact fourth cumulant tensor on frozen native X6 96-port / 37-class observer.
Import-only native kernel derived without changing equations from PREFIX578-R2 published certificate.
Pure exact SymPy rational arithmetic; rerun to verify the published coefficient JSON.
"""
import json
import sympy as sp
from math import factorial
from PREFIX579_R2_native_kernel import Q,P,pi,ones,n,Z,Zinv,growth,ids,edge,ACTIONS
assert n==37 and growth==[1,4,13,21,33,37]
def directional(a,b,c):
    M=[None]+[sp.zeros(n,n) for k in range(4)]
    for i,row in enumerate(Q):
        for (j,x,y,g),m in row.items():
            r=a*x+b*y+c*g
            for k in range(1,5):
                M[k][i,j]+=sp.Rational(m*r**k,6*factorial(k))
    vec=[ones]
    ell=[sp.Integer(1)]
    for k in range(1,5):
        u=sp.zeros(n,1)
        for j in range(1,k+1):
            u+=M[j]*vec[k-j]
        l=(pi*u)[0]
        ell.append(l)
        rhs=u-l*ones
        for j in range(1,k):
            rhs-=ell[j]*vec[k-j]
        v=Zinv*rhs
        assert (pi*v)[0]==0 and (sp.eye(n)-P)*v==rhs
        vec.append(v)
    l1,l2,l3,l4=ell[1:]
    return (24*l4-24*l1*l3-12*l2*l2+24*l1*l1*l2-6*l1**4,
            6*l3-6*l1*l2+2*l1**3)
directions={'A5':(1,0,0),'S':(1,1,0),'D':(1,-1,0),'K':(0,0,1),
    'A5+K':(1,0,1),'A5-K':(1,0,-1),'A5+2K':(1,0,2),
    'D+K':(1,-1,1),'S+K':(1,1,1)}
out={name:directional(*p) for name,p in directions.items()}
E={name:values[0] for name,values in out.items()}
A,I=E['A5'],E['K']
B=(E['S']-E['D'])/4
C=(E['S']+E['D'])/2-2*A
up=E['A5+K']-A-I
um=E['A5-K']-A-I
u2=E['A5+2K']-A-16*I
F=(up+um)/2
v=(up-um)/2
H=(u2-4*F-2*v)/6
DD=v-H
G=2*A-2*B+C+2*F+I-E['D+K']
EE=(E['S+K']-(2*A+2*B+C+2*DD+2*F+G+2*H+I))/2
coef=(A,B,C,DD,EE,F,G,H,I)
known=['-659/93312','85/5832','-191/15552','319/746496',
 '-149/248832','39167/28311552','-7031/4718592',
 '-3378511/1528823808','434651857/97844723712']
assert coef==tuple(map(sp.Rational,known))
def F4(a,b,c):
    return (A*(a**4+b**4)+B*(a**3*b+a*b**3)+C*a*a*b*b+
       DD*(a**3+b**3)*c+EE*(a*a*b+a*b*b)*c+
       F*(a*a+b*b)*c*c+G*a*b*c*c+H*(a+b)*c**3+I*c**4)
def F3(a,b,c):
    return (sp.Rational(-49,5184)*(a**3+b**3)+
       sp.Rational(33,5184)*(a*a*b+a*b*b)+
       sp.Rational(57,82944)*(a*a+b*b)*c-
       sp.Rational(66,82944)*a*b*c-
       sp.Rational(18159,10616832)*(a+b)*c*c+
       sp.Rational(206963,42467328)*c**3)
extra={'A6':(0,1,0),'D-K':(1,-1,-1),'S-K':(1,1,-1),'A5+3K':(1,0,3)}
for name,p in extra.items():out[name]=directional(*p)
for name,p in {**directions,**extra}.items():
    assert out[name][0]==F4(*p) and out[name][1]==F3(*p),name
tensor=(A,B/4,C/6,DD/4,EE/12,F/6,G/12,H/4,I)
result={'status':'ALL_ASSERTIONS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'states':37,'native_ports':96,'directional':{k:{'kappa4':str(x[0]),'kappa3':str(x[1])} for k,x in out.items()},
 'fourth_form_coefficients':dict(zip(['A','B','C','D','E','F','G','H','I'],map(str,coef))),
 'fourth_tensor_representatives':dict(zip(['5555/6666','5556/5666','5566','555K/666K','556K/566K',
     '55KK/66KK','56KK','5KKK/6KKK','KKKK'],map(str,tensor))),
 'checks':['normalized 37-dimensional rational perturbation order 1-4','nine directions uniquely determine form',
 'four additional 4th-order directions verified','all thirteen reproduce PREFIX578 third-order form',
 'gate fourth equals PREFIX577-R2','axis 5/6 exchange retained']}
print(json.dumps(result,indent=2))
