#!/usr/bin/env python3
"""Exact R5 high-p F-face Blackwell certificate verifier. Python stdlib only."""
from fractions import Fraction as F
from itertools import product

R = tuple(F(v) for v in ("1/10","1/2","3/4","1","5/4","3/2","19/10"))
# tbit(0=1/13,1=1), pbit(0=5/7,1=1), qbit, theta_bit, kappa_bit; then g,a,b,u,v,w,z.
CERT = """
0 0 0 0 0 461/777 5777/10101 461/777 0 15409/80808 10701/53872 5777/101010
0 0 0 0 1 75369/76505 15137/153010 75369/76505 105129/4284280 141719/612040 8527/1224080 15137/1530100
0 0 0 1 0 10021/16835 748/1295 10021/16835 0 25817/134680 53757/269360 374/6475
0 0 0 1 1 1 1/13 1 3/112 121/520 0 1/130
0 0 1 0 0 93131/101010 313/202020 93131/101010 0 167761/808080 65223/269360 313/2020200
0 0 1 0 1 579513/581945 47972/581945 579513/581945 220483/9311120 1081501/4655560 2491521/9311120 23986/2909725
0 0 1 1 0 2393/2590 487/67340 2393/2590 0 56191/269360 13095/53872 487/673400
0 0 1 1 1 1 1/13 1 3/112 121/520 279/1040 1/130
0 1 0 0 0 23/39 23/39 23/39 3/520 23/120 207/1040 23/390
0 1 0 0 1 75369/76505 15137/153010 75369/76505 2697/76505 141719/612040 8527/1224080 15137/1530100
0 1 0 1 0 77/130 77/130 77/130 69/10400 77/400 2079/10400 77/1300
0 1 0 1 1 1 1/13 1 3/80 121/520 0 1/130
0 1 1 0 0 13193/14430 1159/28860 13193/14430 0 24211/115440 9351/38480 1159/288600
0 1 1 0 1 579513/581945 47972/581945 579513/581945 64049/1862224 1081501/4655560 2491521/9311120 23986/2909725
0 1 1 1 0 339/370 441/9620 339/370 0 8109/38480 9387/38480 441/96200
0 1 1 1 1 1 1/13 1 3/80 121/520 279/1040 1/130
1 0 0 0 0 139/168 139/168 139/168 1251/4480 1807/6720 171/4480 139/1680
1 0 0 0 1 9299/10203 9299/10203 9299/10203 112015/380912 120887/408120 721/13604 9299/102030
1 0 0 1 0 241/280 241/280 241/280 6507/22400 3133/11200 1107/22400 241/2800
1 0 0 1 1 1 1 1 27/112 13/40 0 1/10
1 0 1 0 0 107/120 107/120 107/120 4581/22400 1391/4800 963/3200 107/1200
1 0 1 0 1 29/30 29/30 29/30 1287/5600 377/1200 261/800 29/300
1 0 1 1 0 37/40 37/40 37/40 4833/22400 481/1600 999/3200 37/400
1 0 1 1 1 1 1 1 27/112 13/40 27/80 1/10
1 1 0 0 0 2573/2820 2573/2820 1111/1410 72/235 3029/11280 0 2573/28200
1 1 0 0 1 686/705 686/705 659/705 1233/3760 347/1128 0 343/3525
1 1 0 1 0 883/940 883/940 401/470 297/940 215/752 0 883/9400
1 1 0 1 1 1 1 1 27/80 13/40 0 1/10
1 1 1 0 0 107/120 107/120 107/120 963/3200 1391/4800 963/3200 107/1200
1 1 1 0 1 29/30 29/30 29/30 261/800 377/1200 261/800 29/300
1 1 1 1 0 37/40 37/40 37/40 999/3200 481/1600 999/3200 37/400
1 1 1 1 1 1 1 1 27/80 13/40 27/80 1/10
"""
Y = {}
for line in CERT.strip().splitlines():
    ib,jb,kb,lb,mb,*coords=line.split()
    Y[tuple(map(int,(ib,jb,kb,lb,mb)))] = tuple(map(F,coords))
assert len(Y)==32 and len(set(Y))==32

def source(t,p,q,theta,kappa):
    return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
            F(9,40)*kappa+t*theta/10,
            (F(3,40)*t+F(21,80))*q,t*theta/10)
def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,
            (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,
            F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w
def hinge(f,k):
    return sum(max(ri-k,F(0))*mi for ri,mi in zip(R,mass(f)))
def lawful(f):
    g,a,b,u,v,w,z=f
    assert 0<=a<=g<=1 and 0<=b<=g
    assert 0<=u<=F(13,40)*a+b/80
    assert 0<=w<=F(3,40)*a+F(21,80)*b
    assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
    m=mass(f)
    assert all(mi>=0 for mi in m)
    assert sum(m)==1 and sum(ri*mi for ri,mi in zip(R,m))==1
def verify(x,y):
    lawful(x); lawful(y)
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    assert tp(x)==tp(y) and tq(x)==tq(y)
    assert all(hinge(y,k)>=hinge(x,k) for k in R[1:-1])
def product_weight(bits,axes):
    result=F(1)
    for bit,v in zip(bits,axes): result*=v if bit else 1-v
    return result
def target(t,p,q,theta,kappa):
    assert F(1,13)<=t<=1 and F(5,7)<=p<=1
    assert 0<=q<=1 and 0<=theta<=1 and 0<=kappa<=1
    axes=((t-F(1,13))/(1-F(1,13)),(p-F(5,7))/(1-F(5,7)),
          q,theta,kappa)
    y=tuple(sum(Y[bits][j]*product_weight(bits,axes)
          for bits in product((0,1),repeat=5)) for j in range(7))
    verify(source(t,p,q,theta,kappa),y)
    return y
def main():
    for bits,y in Y.items():
        i,j,k,l,m=bits
        t=(F(1,13),F(1))[i]
        p=(F(5,7),F(1))[j]
        verify(source(t,p,F(k),F(l),F(m)),y)
    print("PASS_EXACT_F_FACE_32_CORNERS",len(Y))
    for j in range(307):
        t=F(1,13)+(1-F(1,13))*F((31*j+7)%307,307)
        p=F(5,7)+(1-F(5,7))*F((19*j+5)%307,307)
        q=F((23*j+13)%307,307)
        theta=F((29*j+17)%307,307)
        kappa=F((37*j+11)%307,307)
        target(t,p,q,theta,kappa)
    print("PASS_EXACT_307_INTERIOR_REGRESSIONS")
    print("PASS_ALL_REAL_F_FACE_INTERPOLATION_T_1_13_TO_1_P_5_7_TO_1")
if __name__=="__main__":
    main()
