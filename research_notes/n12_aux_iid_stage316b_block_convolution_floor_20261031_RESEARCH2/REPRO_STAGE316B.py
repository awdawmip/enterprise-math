#!/usr/bin/env python3
"""Exact rational verification for Stage316-B's two-block envelope and TV floor.
This program checks finite arithmetic identities. Universal real/n claims use the proof.
"""
from fractions import Fraction as Q
from itertools import product

P0, P1 = Q(1,4), Q(3,4)
DENS=Q(256)
MASS=((63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63))
RATES0=(P0,P0,P0,P1,P0,P1,P1,P1)

def words(n):return list(product((0,1),repeat=n))
def B(t,w):
    k=sum(w);return t**k*(1-t)**(len(w)-k)
def TV_dist(a,b):return sum((abs(x-y) for x,y in zip(a,b)),Q(0))/2
def D(n,s,t):return TV_dist([B(s,w) for w in words(n)],[B(t,w) for w in words(n)])

def full(n,rates):
    p=Q(0); t=Q(0)
    for wy in product((0,1), repeat=2):
        # one public fiber (W,Y), summing over J and S
        for w in words(n):
            original=Q(0);represented=Q(0)
            for j in (0,1):
                idx=4*j+2*wy[0]+wy[1]
                a,b=MASS[idx]
                original+=(a*B(P0,w)+b*B(P1,w))/DENS
                represented+=(a+b)*B(rates[idx],w)/DENS
            p+=abs(original-represented)/2
    for i,(a,b) in enumerate(MASS):
        t+=(a*D(n,P0,rates[i])+b*D(n,P1,rates[i]))/DENS
    return p,t

def block(n,u,v):
    p=sum((abs(64*B(u,w)+16*B(v,w)-72*B(P0,w)-8*B(P1,w)) for w in words(n)),Q(0))/512
    c=(63*D(n,P0,u)+D(n,P1,u)+9*D(n,P0,v)+7*D(n,P1,v))/256
    return p,c

for n in range(1,6):
    d=D(n,P0,P1)
    pmap,tmap=full(n,RATES0)
    assert pmap==d/16,(n,'pmap',pmap,d/16)
    assert tmap==Q(7,64)*d,(n,'tmap',tmap,Q(7,64)*d)
    assert block(n,P0,P0)==(d/32,d/32)
    samples=[(P0,P0,P0,P0), (Q(1,8),Q(3,7),Q(4,9),Q(2,3)),
             (Q(0),Q(1),Q(1),Q(0)),(Q(9,40),Q(3,5),Q(9,40),Q(3,5)),
             (Q(1,4),Q(7,16),Q(3,4),Q(1,2))]
    for u,v,up,vp in samples:
        rates=list(RATES0)
        rates[0],rates[4]=u,v
        rates[7],rates[3]=1-up,1-vp
        fp,ft=full(n,rates)
        bp,bc=block(n,u,v)
        cp,cc=block(n,up,vp)
        assert fp==bp+cp,(n,'public',u,v,up,vp,fp,bp+cp)
        assert ft==Q(12,256)*d+bc+cc,(n,'tagged',ft,bc+cc+Q(12,256)*d)
print('EXACT_BLOCK_CONJUGACY_N1_TO_N5_PASS')
assert full(3,RATES0)==(Q(11,256),Q(77,1024))

# Third-central-moment invariant for two-point mixing weights 4/5,1/5.
def moments_mix(weight,z,z2):return tuple(weight*z**j+(1-weight)*z2**j for j in (1,2,3))
def V_C_H(m):
    x,y,z=m
    v=y-x*x;c=z-3*x*y+2*x**3
    return v,c,c*c-Q(9,4)*v**3
true_m=moments_mix(Q(9,10),P0,P1)
var,cent,h=V_C_H(true_m)
assert true_m==(Q(3,10),Q(9,80),Q(9,160))
assert var==Q(9,400) and cent==Q(9,1000) and h==Q(567,10240000)
for u,v in ((Q(0),Q(1)),(Q(9,40),Q(3,5)),(Q(1,4),Q(3,4)),(Q(1,3),Q(1,3))):
    assert V_C_H(moments_mix(Q(4,5),u,v))[2]==0

# Algebraic derivative bounds on the segment between any moments within d
# of true moments. These are necessary if three-word TV <= d.
d=Q(1,896)
m1,m2,m3=true_m
amin=6*(m1-d)**2-3*(m2+d)
amax=6*(m1+d)**2-3*(m2-d)
assert 0<amin and amax<Q(21,100)
assert 3*(m1+d)<Q(91,100)
assert 2*(m1+d)<Q(61,100)
L_C=Q(53,25)  # 0.21+0.91+1: |Delta C|/TV
L_V=Q(161,100) # 0.61+1: |Delta V|/TV
L=(2*cent+L_C*d)*L_C+Q(27,4)*(var+L_V*d)**2*L_V
assert h-d*L==Q(9601171,411041792000000)>0
assert Q(5,8)*d==Q(5,7168)
print('MOMENT_CERTIFICATE_H=',h)
print('MOMENT_CERTIFICATE_L=',L)
print('MOMENT_CERTIFICATE_STRICT_GAP=',h-d*L)
print('PUBLIC_TV_FLOOR_N_GE_3=',Q(5,7168))
print('PREVIOUS_FLOOR_IMPROVEMENT_FACTOR=',Q(5,7168)/Q(567,446720000))
print('STAGE316B_BLOCK_INFIMAL_CONVOLUTION_AND_STRONG_TV_FLOOR_EXACT_PASS')
