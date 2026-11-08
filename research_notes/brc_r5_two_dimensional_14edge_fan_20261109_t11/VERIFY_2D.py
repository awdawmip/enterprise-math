#!/usr/bin/env python3
"""R5 two-chart 14-edge gluing: exact endpoint transport certificates."""
from fractions import Fraction as F

def Q(s):return tuple(map(F,s.split()))
R=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X0=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0=Q('871/1000 9/40 5/6 273/4000 21/100 143/1000 9/400')
X1=Q('1 1/10 1 27/800 1/100 27/400 1/100')
Y1=Q('4673/6400 1311/6400 4673/6400 38759/512000 47301/256000 103999/512000 1311/64000')
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
SB=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5))
A0=Q('33553/432000 38053/432000 3997/624000 3997/390000 1105679/28080000 15711211/52650000 14339/216000 388729/32400000 3298/16875 367/24000 7261/506250 113/6000 2612321/32400000 20761/270000')
AH=Q('54023/1080000 69773/1080000 6697/1248000 6697/780000 1175439949/17971200000 8008067351/33696000000 76032887/691200000 415111079/20736000000 101129/432000 367/48000 120750673/2592000000 113/12000 585724921/20736000000 155310673/1382400000')
BH=Q('54023/1080000 69773/1080000 6697/1248000 6697/780000 206393/4992000 3547343/12480000 206393/1920000 101129/432000 33263473/1382400000 367/48000 1731407/691200000 113/12000 3089/64000 155310673/1382400000')
B1=Q('16109/720000 29609/720000 9/2080 9/1300 16163/299520 21277/83200 16163/115200 98191/360000 2878057/76800000 0 1533829/115200000 0 1/256 34054171/230400000')

def masses(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u,(g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def lawful(f):
    g,a,b,u,v,w,z=f
    return (0<=a<=g<=1 and 0<=b<=g and
            0<=u<=F(13,40)*a+b/80 and
            0<=w<=F(3,40)*a+F(21,80)*b and
            0<=z<=a/10 and z<=v<=z+F(9,40)*b)

def midpoint(x,y):return tuple((a+b)/2 for a,b in zip(x,y))

def verify(support,weights,x,y):
    assert len(support)==len(weights)==14 and len(set(support))==14
    assert all(z>=0 for z in weights)
    E=dict(zip(support,weights));M=masses(y);N=masses(x)
    assert all(sum(E.get((i,j),F(0)) for j in range(7))==M[i] for i in range(7))
    assert all(sum(E.get((i,j),F(0)) for i in range(7))==N[j] for j in range(7))
    assert all(sum(R[i]*E.get((i,j),F(0)) for i in range(7))==R[j]*N[j] for j in range(7))
    return sum(z>0 for z in weights),min(weights)

for name,x,y in [('zero',X0,Y0),('one',X1,Y1)]:
    assert lawful(x) and lawful(y) and x[0]==x[2]
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert times(x)==times(y)
    assert sum(masses(x))==sum(masses(y))==1
    assert sum(R[i]*m for i,m in enumerate(masses(x)))==1
    assert sum(R[i]*m for i,m in enumerate(masses(y)))==1
    print('PASS_LAWFUL_SEEDLESS_TIME',name)
XH,YH=midpoint(X0,X1),midpoint(Y0,Y1)
for name,S,W,x,y in [('A_0',SA,A0,X0,Y0),('A_HALF',SA,AH,XH,YH),('B_HALF',SB,BH,XH,YH),('B_1',SB,B1,X1,Y1)]:
    n,m=verify(S,W,x,y)
    print('PASS_EXACT_21',name,'positive',n,'min',m)
assert len(set(SA)&set(SB))==12
cross=F(13,18400)/(F(13,18400)+F(2109829,147200000))
assert cross==F(104000,2213829)<F(1,2)
print('EXACT_OLD_CHART_CROSSING',cross)
print('PROVED_REAL_LAMBDA_0_TO_1_TWO_14_EDGE_SUPPORTS')


# --- R5 exact two-dimensional support-atlas extension (2026-11-09) ---
DX=Q('-1802718000/1111424393 -1802718000/1111424393 -1802718000/1111424393 -608417325/1111424393 -496963350/1111424393 -608417325/1111424393 0')
DY=Q('-6000/3761 -6000/3761 -6000/3761 -2025/3761 -1950/3761 -2025/3761 -600/3761')
D={(0,0):-F(1,2),(6,6):-F(1,2),(3,3):F(1)}
EPS=F(1,1000)
def add(v,d,t):return tuple(a+t*z for a,z in zip(v,d))
def linear(v,w,t):return tuple((1-t)*a+t*z for a,z in zip(v,w))
def shifted(s,weights,t):return tuple(w+t*D.get(e,F(0)) for e,w in zip(s,weights))
def slack(f):
 g,a,b,u,v,w,z=f
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
# All exact affine derivative identities, with no sampling inference.
mx=tuple(a-c for a,c in zip(masses(add(X0,DX,1)),masses(X0)))
my=tuple(a-c for a,c in zip(masses(add(Y0,DY,1)),masses(Y0)))
assert mx==my==Q('-1/2 0 0 1 0 0 -1/2')
assert tuple(a-c for a,c in zip(times(add(X0,DX,1)),times(X0)))==tuple(a-c for a,c in zip(times(add(Y0,DY,1)),times(Y0)))
assert DX[0]==DX[2] and DY[6]==DY[1]/10 and DY[4]-DY[6]==F(9,40)*DY[2]
print('PASS_EXACT_TRANSVERSE_PHYSICAL_DEFORMATION')
XH=linear(X0,X1,F(1,2));YH=linear(Y0,Y1,F(1,2))
vertices=[
 ('A0',SA,A0,X0,Y0),('AH',SA,AH,XH,YH),
 ('BH',SB,BH,XH,YH),('B1',SB,B1,X1,Y1),
 ('A0top',SA,shifted(SA,A0,EPS),add(X0,DX,EPS),add(Y0,DY,EPS)),
 ('AHtop',SA,shifted(SA,AH,EPS/2),add(XH,DX,EPS/2),add(YH,DY,EPS/2)),
 ('BHtop',SB,shifted(SB,BH,EPS/2),add(XH,DX,EPS/2),add(YH,DY,EPS/2))]
for name,s,w,x,y in vertices:
 assert all(z>=0 for z in slack(x)+slack(y)) and lawful(x) and lawful(y)
 assert x[0]==x[2] and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 assert times(x)==times(y) and sum(masses(x))==sum(masses(y))==1
 assert sum(R[i]*v for i,v in enumerate(masses(x)))==sum(R[i]*v for i,v in enumerate(masses(y)))==1
 nonzero,small=verify(s,w,x,y)
 print('PASS_EXACT_21',name,'edges',nonzero,'min_edge',small)
dlambda_nu0=masses(X1)[0]-masses(X0)[0]
dlambda_mu1=masses(Y1)[1]-masses(Y0)[1]
det=dlambda_nu0*my[1]-mx[0]*dlambda_mu1
assert det==-F(367,48000)
print('EXACT_TWO_INDEPENDENT_MARGINAL_COORDINATES_DETERMINANT',det)
print('THEOREM_ALL_REAL_TWO_DIMENSIONAL_14_EDGE_TRIANGLE', 'delta<=',EPS,'*(1-lambda)')
