#!/usr/bin/env python3
"""R5 fifth rare-failure coefficient: exact integer/rational verifier."""
import hashlib, json, sys, zipfile
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb

C = lambda n, r: comb(n, r) if n >= r >= 0 else 0
A = tuple(range(214, 219))
B = tuple(range(219, 315))
D = tuple(range(222, 315))
S1 = (214, 216, 217, 218, 219, 220, 221)
S2 = (215, 216, 217, 218, 219, 220, 221)
S, Q, Q4 = sum(B), sum(x*x for x in B), sum(x**4 for x in B)
R, T, U, V = [sum(x**j for x in A) for j in range(1, 5)]
E, E2 = sum(D), sum(x*x for x in D)
J = 219 * 220 * 221
PIN = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"

def moments5(m):
    b, c, d, g, h = (C(m+4, j) for j in range(5, 10))
    m2 = d*(R*R+T)+c*T
    m3 = g*R**3+3*(g+d)*R*T+(2*g+3*d+c)*U
    m4 = (h*R**4 + 6*R*R*T*C(m+5,9) + 3*T*T*C(m+6,9)
          + 4*R*U*(C(m+6,9)+C(m+5,9))
          + V*(C(m+7,9)+4*C(m+6,9)+C(m+5,9)))
    return (b, c*R, m2, m3, m4)

def moments7(m, prices):
    r = sum(prices)
    t = sum(x*x for x in prices)
    h, j, d = C(m+6,7), C(m+6,8), C(m+6,9)
    return h, j*r, d*(r*r+t)+j*t

def overlap_raw(m):
    k = w = 0
    # 3+3 equal-cost multiplicity groups preserve first price moment.
    for a in range(m):
      for b in range(m):
       for c in range(m):
        for d in range(m):
         nfail = int(a+b+c<m)+int(a+c+d<m)+int(b+c+d<m)
         if nfail < 2: continue
         count = C(c+2,2)*C(d+2,2)*(nfail-1)
         k += count
         w += count*(214*a+215*b+217*c+220*d)
    return k,w

def overlap_grouped(m):
    # Independent pairwise/triple intersection enumeration using hockey-stick.
    k01=k02=k12=kt=0
    w01=w02=w12=wt=F(0)
    for c in range(m):
      pc=C(c+2,2)
      for a in range(m-c):
       t=m-1-c-a
       wd=C(t+3,3)
       n=(t+1)*wd
       sum_y=(t*(t+1)//2)*wd
       sum_d=3*C(t+3,4)*(t+1)
       k01+=pc*n; k02+=pc*n
       w01+=pc*((214*a+217*c)*n+215*sum_y+220*sum_d)
       w02+=pc*((215*a+217*c)*n+214*sum_y+220*sum_d)
      for d in range(m-c):
       pd=C(d+2,2)
       h=m-1-c-d
       n=(h+1)**2
       sum_ab=h*(h+1)**2
       k12+=pc*pd*n
       w12+=pc*pd*((217*c+220*d)*n+F(429,2)*sum_ab)
       exc=max(0, 2*h-(m-1-c))
       ntr=n-exc*(exc+1)//2
       sumtr=sum_ab-h*exc*(exc+1)+(exc-1)*exc*(exc+1)//3
       kt+=pc*pd*ntr
       wt+=pc*pd*((217*c+220*d)*ntr+F(429,2)*sumtr)
    ans=(k01+k02+k12-kt, w01+w02+w12-wt)
    assert ans[1].denominator == 1
    return int(ans[0]), int(ans[1])

def gf_coeff(m, poly, p, q):
    # [z^(m-1)] poly(z)/[(1-z)^p(1+z)^q].
    def den(n):
        if n<0:return 0
        return sum((-1)**j*C(j+q-1,q-1)*C(n-j+p-1,p-1) for j in range(n+1))
    return sum(a*den(m-1-i) for i,a in enumerate(poly))

def coefficients(m):
    mm=moments5(m)
    l2=F(S*S,8)-F(Q,24)
    l3=F(S**3-S*Q,48)
    l4=F(S**4,384)-F(S*S*Q,192)+F(Q*Q,1152)+F(Q4,2880)
    b5=mm[0]*l4-mm[1]*l3+F(mm[2],2)*l2-F(S*mm[3],12)+F(mm[4],24)
    b7=F(0)
    for prices,extra in ((S1,215),(S2,214)):
        h,v1,v2=moments7(m,prices)
        sf=E+extra; qf=E2+extra*extra
        b7+=F(J,extra)*(h*(F(sf*sf,8)-F(qf,24))-F(sf*v1,2)+F(v2,2))
    k,w=overlap_grouped(m)
    b8=-J*(F(E*k,2)-w)
    return b5,b7,b8,b5+b7+b8,k,w

def direct_moments(m, prices, max_power):
    ans=[0]*(max_power+1)
    for n in range(m):
      for selection in combinations_with_replacement(prices,n):
       v=sum(selection)
       for j in range(max_power+1):ans[j]+=v**j
    return ans

def validate(pin_file=None):
    if pin_file:
        if pin_file.endswith(".zip"):
            with zipfile.ZipFile(pin_file) as z: raw=z.read("EXACT_R5_ALL_101_BUDGETS.json")
        else:
            with open(pin_file,"rb") as f:raw=f.read()
        assert hashlib.sha256(raw).hexdigest()==PIN
        assert json.loads(raw)["budget_range"]==[214,314]
    for m in (1,2,3,8,17):
        assert tuple(direct_moments(m,A,4))==moments5(m)
        for p in (S1,S2):
            assert tuple(direct_moments(m,p,2))==moments7(m,p)
    for m in range(1,18):
        assert overlap_raw(m)==overlap_grouped(m)
    for m in range(1,61):
        k,w=overlap_grouped(m)
        assert k==gf_coeff(m,(2,13,24,20,6),9,3)
        assert w==gf_coeff(m,(0,6516,37584,86457,94710,52995,11727),10,4)
    samples={}
    for m in (1,2,3,8,17):
        b5,b7,b8,total,k,w=coefficients(m)
        samples[str(m)]={"K":k,"Z":w,"B91_5":str(b5),"B91_7":str(b7),
                          "B91_8":str(b8),"B91_total":str(total)}
    return {"schema":"EM_R5_FIXED_M_N91_EXACT_V1","review":"NOT_REVIEWED",
            "frozen_sha256":PIN,"input_sha_checked":bool(pin_file),
            "raw_grouped_overlap_m":"1..17","gf_coeff_m":"1..60",
            "moments_full_m":[1,2,3,8,17],"samples":samples}

if __name__=="__main__":
    print(json.dumps(validate(sys.argv[1] if len(sys.argv)>1 else None),indent=2))
