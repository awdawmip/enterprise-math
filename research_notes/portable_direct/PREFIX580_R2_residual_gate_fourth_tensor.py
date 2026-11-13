#!/usr/bin/env python3
"""PREFIX580: full-96-port exact rational Perron cumulants through fourth order."""
import json
from math import factorial
import sympy as sp
from PREFIX579_R2_native_kernel import edge,ACTIONS
n=96
pi=sp.ones(1,n)/n
one=sp.ones(n,1)
P=sp.zeros(n,n); rows=[]
for i in range(n):
    row=[]
    for action in ACTIONS:
        j,w=edge(i,action)
        M=64*w[6]-(3*w[0]+w[1]+3*w[2]+w[3])
        row.append((j,M,w[6]))
        P[i,j]+=sp.Rational(1,6)
    rows.append(row)
assert P*one==one and pi*P==pi
Z=sp.eye(n)-P+one*pi
Zinv=Z.inv()
def rate(a,b):
    coeff=[None]+[sp.zeros(n,n) for _ in range(4)]
    for i,row in enumerate(rows):
        for j,M,g in row:
            w=a*M+64*b*g
            for k in range(1,5):
                coeff[k][i,j]+=sp.Rational(w**k,6*factorial(k))
    v=[one]; ell=[sp.Integer(1)]
    for k in range(1,5):
        u=sum((coeff[j]*v[k-j] for j in range(1,k+1)),sp.zeros(n,1))
        l=(pi*u)[0]; ell.append(l)
        rhs=u-l*one-sum((ell[j]*v[k-j] for j in range(1,k)),sp.zeros(n,1))
        vk=Zinv*rhs
        assert Z*vk==rhs and (pi*vk)[0]==0
        v.append(vk)
    l1,l2,l3,l4=ell[1:]
    return (
      sp.factor((24*l4-24*l1*l3-12*l2*l2+24*l1*l1*l2-6*l1**4)/64**4),
      sp.factor((6*l3-6*l1*l2+2*l1**3)/64**3),
      sp.factor((2*l2-l1**2)/64**2),
      sp.factor(l1/64))
p={'Y':(1,0),'K':(0,1),'Y+K':(1,1),'Y-K':(1,-1),
   'Y+2K':(1,2),'Y-2K':(1,-2)}
values={name:rate(*ab) for name,ab in p.items()}
assert values['Y'][1]==sp.Rational(28537,6291456)
assert values['Y'][2]==sp.Rational(367,73728)
assert values['Y'][3]==sp.Rational(-1,64)
E4={name:val[0] for name,val in values.items()}
A,E=E4['Y'],E4['K']
u_plus=E4['Y+K']-A-E
u_minus=E4['Y-K']-A-E
u_two=E4['Y+2K']-A-16*E
C=(u_plus+u_minus)/2
V=(u_plus-u_minus)/2
D=(u_two-4*C-2*V)/6
B=V-D
assert (A,B,C,D,E)==tuple(map(sp.Rational,[
 '87518285/21743271936','89759141/5435817984',
 '1656329771/65229815808','35360777/2038431744',
 '434651857/97844723712']))
assert E4['Y-2K']==A-2*B+4*C-8*D+16*E
result={'status':'ALL_ASSERTIONS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':'96 native ports, six original labeled actions per port',
 'residual':'Y=K-beta.R ; beta=(5,-1,5,-1,-4,-4)/192',
 'Y_rate2':str(values['Y'][2]),'Y_rate3':str(values['Y'][1]),'Y_rate4':str(A),
 'rate4_polynomial_coefficients':dict(zip('ABCDE',map(str,(A,B,C,D,E)))),
 'rate4_tensor':dict(zip(['YYYY','YYYK','YYKK','YKKK','KKKK'],map(str,(A,B/4,C/6,D/4,E)))),
 'directions':{k:str(v[0]) for k,v in values.items()}}
print(json.dumps(result,indent=2))
