from fractions import Fraction as F
from math import comb
from itertools import product

Z_MIN,Z_MAX=F(1,16),F(7,16)
D=F(5211,10976)
LB=D/2
UB=F(99,343)
K2=((F(0),F(0),F(0),F(1),F(0),F(0)),
    (F(0),F(11,21),F(1,4),F(0),F(5,28),F(1,21)),
    (F(340,441),F(2,21),F(59,441),F(0),F(0),F(0)))
ORBITS=(((1,1),),((1,3),(3,1)),((1,4),(4,1)),((3,3),),((3,4),(4,3)),((4,4),))
K1={'Y':(F(0),F(1),F(0)),'N':(F(88,105),F(0),F(17,105))}
LABELS=(1,3,4)

def endpoints(z):
    assert Z_MIN<=z<=Z_MAX
    return max(F(1,2),1-2*z),min(F(7,8),1-F(8,7)*z)

def law(a,z,n=3):
    u=1-a-z
    return {(i,j,n-i-j):comb(n,i)*comb(n-i,j)*a**i*z**j*u**(n-i-j)
            for i in range(n+1) for j in range(n-i+1)}

def tv(p,q):
    assert p.keys()==q.keys()
    return sum(abs(p[k]-q[k]) for k in p)/2

def full(a,z):
    p=(a,z,1-a-z)
    return {t:p[LABELS.index(t[0])]*p[LABELS.index(t[1])]*p[LABELS.index(t[2])]
            for t in product(LABELS,repeat=3)}

def rec(z):
    rows=[]
    for orbit_row in K2:
        r={x:F(0) for x in product(LABELS,repeat=2)}
        for prob,orbit in zip(orbit_row,ORBITS):
            for v in orbit:r[v]=prob/len(orbit)
        assert sum(r.values())==1 and min(r.values())>=0
        rows.append(r)
    out={x:F(0) for x in product(LABELS,repeat=3)}
    for b in product(('Y','N'),repeat=3):
        bp=__import__('math').prod(z if x=='Y' else 1-z for x in b)
        row=0 if b[:2]==('Y','Y') else 2 if b[:2]==('N','N') else 1
        for two,p2 in rows[row].items():
            for last,p1 in zip(LABELS,K1[b[2]]):
                out[two+(last,)]+=bp*p2*p1
    assert sum(out.values())==1 and min(out.values())>=0
    return out

def run():
    assert LB==F(5211,21952)
    assert UB==1-(1-F(9,49))*(1-F(9,70))
    z=F(1,4);a,b=endpoints(z)
    assert (a,b)==(F(1,2),F(5,7))
    assert tv(law(a,z),law(b,z))==D
    assert tv(full(a,z),full(b,z))==D
    assert (b+z)**3-(a+z)**3==D
    zs={Z_MIN,Z_MAX,F(7,64),F(1,4)}
    zs.update(Z_MIN+(Z_MAX-Z_MIN)*F(i,100) for i in range(101))
    tested=0
    for z in sorted(zs):
        lo,hi=endpoints(z)
        assert lo>=F(2,3)*(1-z)
        assert F(1,2)<=z/(1-lo)<=F(7,8)
        assert F(1,2)<=z/(1-hi)<=F(7,8)
        for i in range(5):
            for j in range(i+1,5):
                a=lo+(hi-lo)*F(i,4);b=lo+(hi-lo)*F(j,4)
                assert tv(law(a,z),law(b,z))==(b+z)**3-(a+z)**3
                assert tv(law(a,z),law(b,z))<=D
                tested+=1
    grid=0
    for i in range(9):
        a=F(1,2)+F(3*i,64)
        for j in range(9):
            c=F(1,2)+F(3*j,64);z=(1-a)*c
            assert tv(full(a,z),rec(z))<=UB
            grid+=1
    print('PASS_S23_N3_EXACT_FIBER_DIAMETER_AND_TENSOR_UPPER_20261106')
    print('extremal z:',F(1,4),'fiber endpoints:',F(1,2),F(5,7))
    print('exact diameter:',D)
    print('delta_3 bounds:',LB,'<= delta_3 <=',UB)
    print('rational fiber samples:',len(zs))
    print('rational fiber pairs:',tested)
    print('kernel grid evaluations:',grid)
    print('continuous proof: monotone likelihood signs + three piecewise derivative bounds')
if __name__=='__main__':run()
