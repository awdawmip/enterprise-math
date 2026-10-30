from fractions import Fraction as F
from itertools import product

z,o,h=F(0),F(1),F(1,2)
q={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
   'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}
pL,qL={},{}
for s,j,k in product(q,range(2),range(2)):
    qL[s,j,k]=q[s]/4
    pL[s,j,k]=qL[s,j,k]*r[s][j]
assert len(pL)==16 and len(qL)==16
assert all(x>0 for x in (*pL.values(),*qL.values()))
assert sum(pL.values())==sum(qL.values())==1
coarse=lambda s:'B' if s=='BU' else 'A' if s=='AU' else 'E'
for c,w in [('E',F(7,12)),('A',F(1,6)),('B',F(1,4))]:
    assert all(sum(v for (s,_,_),v in law.items() if coarse(s)==c)==w
               for law in (pL,qL))

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),z)/2

def calc(e,u,v,d00,d01,d10,d11):
    fs=[]
    for rate,d0,d1 in ((u,d00,d01),(v,d10,d11)):
        fs.append((1-rate,rate*d0/2,rate*(1-d0)/2,
                   rate*d1/2,rate*(1-d1)/2))
    f0,f1=fs
    assert all(sum(f)==1 and all(x>=0 for x in f) for f in fs)
    D=tv(f0,f1);t=1-2*e
    formula=sum(max(abs(x-y),t*(x+y)) for x,y in zip(f0,f1))/20
    out=[]
    for law in (pL,qL):
        a={}
        for (s,j,k),mass in law.items():
            if s!='BU':
                key=(coarse(s),'NA','STOP')
                a[key]=a.get(key,z)+mass
                continue
            rate=(u,v)[j]
            dec=((d00,d01),(d10,d11))[j][k]
            for zz,wz in ((j,1-e),(1-j,e)):
                for yy,wy in (('B3',1-rate),(f'B4P{k}',rate*dec),
                              (f'B4Q{k}',rate*(1-dec))):
                    key=('B',zz,yy)
                    a[key]=a.get(key,z)+mass*wz*wy
        assert sum(a.values())==1
        out.append(a)
    keys=set(out[0])|set(out[1])
    direct=sum(abs(out[0].get(k,z)-out[1].get(k,z)) for k in keys)/2
    L=max(D,t)/10; U=(D+t*(1-D))/10
    assert formula==direct and L<=direct<=U
    return D,direct,L,U

def low(D):return ((1-D)/2,(1+D)/2,z,z,z,z)
def high(D):return (D,D,o,o,z,z)
def between(D,lam):
    u=(1-lam)*(1-D)/2+lam*D
    v=(1-lam)*(1+D)/2+lam*D
    dec=lam*D/u if u else z
    return (u,v,dec,dec,z,z)

noise=[F(i,8) for i in range(5)]
rate=[F(i,4) for i in range(5)]
dec=[z,h,o]
n1=n2=n3=0
for e,u,v,d0,d1 in product(noise,rate,rate,dec,dec):
    calc(e,u,v,d0,d0,d1,d1);n1+=1
for e,u,v,d00,d01,d10,d11 in product((z,F(1,4),h),
    (z,h,o),(z,h,o),dec,dec,dec,dec):
    calc(e,u,v,d00,d01,d10,d11);n2+=1
for e,D,lam in product(noise,rate,[F(i,4) for i in range(5)]):
    _,_,L,U=calc(e,*between(D,lam))
    assert calc(e,*low(D))[1]==L
    assert calc(e,*high(D))[1]==U
    assert calc(e,*between(D,lam))[0]==D
    n3+=1
e,D=F(1,4),F(1,2)
assert (calc(e,*low(D))[1],
        calc(e,z,F(1,2),z,z,z,z)[1],
        calc(e,*high(D))[1])==(F(1,20),F(1,16),F(3,40))
print('PASS_BRC_N4_FIXED_NOISE_D_JOINT_TV_SHARP_INTERVAL')
print(f'16 positive leaves; coarse P/Q equal; {n1} S23, {n2} S2, {n3} constant-D exact cases')
print('eps=1/4,D=1/2: lower=1/20, prior interior=1/16, upper=3/40')
print('All-real theorem is proved algebraically in PROOF.md.')
