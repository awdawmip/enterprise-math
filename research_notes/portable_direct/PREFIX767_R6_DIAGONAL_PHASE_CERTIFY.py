"""PREFIX-767 exact integer evidence for the frozen 189-row stopped-BRC/Gamma auxiliary model.
Only native Python integers are used for signs and bounds; floats are display-only.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from fractions import Fraction

N, W = 189, 1 << 18

@lru_cache(None)
def inside(n, k, x):
    return 40 * (n + 1) * comb(n, k) * x**k * (W-x)**(n-k) > W**n

@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0: lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t): b=t
            else: a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t): a=t
        else: b=t
    if 4*(a-hi)>W: return True
    if 4*(b-lo)<W: return False
    raise ArithmeticError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
    c=defaultdict(int)
    for k,v in rows[-1].items():c[k]+=v;c[k+1]+=v
    rows.append({k:v for k,v in c.items() if wide(n,k)})
assert len(rows[-1])==0 and sum(map(len,rows[:N]))==9529

@lru_cache(None)
def scaled(x, B, derivatives=False):
    """Return s_i(x) B^188 and optionally derivatives similarly scaled."""
    assert 0 < x < B//2
    P=[1]; Q=[1]
    for _ in range(N):P.append(P[-1]*x);Q.append(Q[-1]*(B-x))
    all0,all1,all2=[],[],[]
    for n,row in enumerate(rows[:N]):
        s0=s1=s2=0
        for k,v in row.items():
            j=n-k
            s0+=v*P[k]*Q[j]
            if derivatives:
                if k: s1+=v*k*P[k-1]*Q[j]
                if j: s1-=v*j*P[k]*Q[j-1]
                if k>=2:s2+=v*k*(k-1)*P[k-2]*Q[j]
                if k and j:s2-=2*v*k*j*P[k-1]*Q[j-1]
                if j>=2:s2+=v*j*(j-1)*P[k]*Q[j-2]
        all0.append(s0*B**(188-n))
        if derivatives:
            all1.append(s1*B**(189-n))
            all2.append(s2*B**(190-n))
    H=B**188
    assert all0[:25]==[H]*25
    assert all0[25] == H-(x**25+(B-x)**25)*B**(188-25)
    return (all0,all1,all2) if derivatives else all0

@lru_cache(None)
def kernels():
    return tuple(tuple(comb(i+j,i) << (376-i-j) for j in range(i,N)) for i in range(N))

def bilinear(v,w,want_L=False):
    C=L=0
    for i, row in enumerate(kernels()):
        vi=v[i];wi=w[i]
        for idx,t in enumerate(row):
            j=i+idx
            vterm=vi*w[j] if i==j else vi*w[j]+v[j]*wi
            u=t*vterm
            C+=u
            if want_L:L+=(i+j+1)*u
    return (C,L) if want_L else C

def diagonal(a,B,with_derivative=False):
    H=B**188; T=1<<377; E=H*H*T
    if with_derivative:U,U1,U2=scaled(a,B,True)
    else: U,U1,U2=scaled(a,B,True)
    Cuu=bilinear(U,U); Cu1u=bilinear(U1,U)
    A,Ldd=bilinear(U1,U1,True)
    m=2*sum(U)*H*T-Cuu
    v=sum(U1)*H*T-Cu1u
    D=Ldd*E+2*v*v-2*m*A
    assert A>0 and D>0,(a,B,'bad positive square mixture')
    qr=Fraction(A*E,D)
    if not with_derivative: return qr
    A1,L1=bilinear(U2,U1,True)
    A1*=2;L1*=2
    v1=sum(U2)*H*T-bilinear(U2,U)-A
    D1=L1*E+4*v*v1-4*v*A-2*m*A1
    sign_num=A1*D-A*D1
    return qr,sign_num

# A finer exact square near an interior diagonal candidate.
B=65536
lo,hi=3296,3297
Ulo=scaled(lo,B); Uhi=scaled(hi,B)
Dvec=[u-v for u,v in zip(Uhi,Ulo)]
H=B**188;T=1<<377;E=H*H*T
Caa=bilinear(Ulo,Ulo); Cab=bilinear(Ulo,Uhi); Cbb=bilinear(Uhi,Uhi)
CDD,LDD=bilinear(Dvec,Dvec,True)
m_aa=2*sum(Ulo)*H*T-Caa
m_ab=(sum(Ulo)+sum(Uhi))*H*T-Cab
m_bb=2*sum(Uhi)*H*T-Cbb
dMU=-CDD
dVAR=-LDD*E-(m_bb*m_bb-2*m_ab*m_ab+m_aa*m_aa)
assert dMU==m_bb-2*m_ab+m_aa
assert dMU<0 and dVAR<0
q_sq=Fraction(-dMU*E,-dVAR)
# Exact upper bound: 0.0285186
assert q_sq < Fraction(285186,10_000_000)

# Exact stationary bracket of the rational diagonal local phase ratio.
ql,sl=diagonal(1,20,True)                 # 0.0500
qr,sr=diagonal(51,1000,True)              # 0.0510
assert sl<0 and sr>0
# Improve with narrower exact rational endpoints.
qll,sll=diagonal(251,5000,True)           # 0.0502
qrr,srr=diagonal(63,1250,True)           # 0.0504
assert sll<0 and srr>0

sq_a,sq_b,sq_B,sq_E=lo,hi,B,E
# Exact interval proof that D(u)>0 throughout [251/5000,252/5000].
# Positive monomials are bounded by p in [a,b] and 1-p in [1-b,1-a].
a,b,B=251,252,5000
H=B**188;T=1<<377;E=H*H*T
pa=[1];pb=[1];qa=[1];qb=[1]
for _ in range(N):
    pa.append(pa[-1]*a);pb.append(pb[-1]*b)
    qa.append(qa[-1]*(B-b));qb.append(qb[-1]*(B-a))
SL=[];SU=[];VL=[];VU=[]
for n,row in enumerate(rows[:N]):
    if n<25:
        SL.append(H);SU.append(H);VL.append(0);VU.append(0);continue
    sl=su=pl=pu=nl=nu=0
    for k,c in row.items():
        j=n-k
        sl+=c*pa[k]*qa[j]; su+=c*pb[k]*qb[j]
        if k:
            pl+=c*k*pa[k-1]*qa[j];pu+=c*k*pb[k-1]*qb[j]
        if j:
            nl+=c*j*pa[k]*qa[j-1];nu+=c*j*pb[k]*qb[j-1]
    SL.append(sl*B**(188-n));SU.append(su*B**(188-n))
    VL.append((pl-nu)*B**(189-n));VU.append((pu-nl)*B**(189-n))
assert min(VL)>=0
Ahi=bilinear(VU,VU)
_,Blo=bilinear(VL,VL,True)
Mhi=2*sum(SU)*H*T-bilinear(SL,SL)
Vlow=sum(VL)*H*T-bilinear(VU,SU)
assert Ahi<3156*E
assert Blo>242137*E
assert Mhi<50*E
assert Vlow>225*E
assert 242137+2*225**2-2*50*3156>0
print('ALL_CHECKS_PASS PREFIX767')
print('survivor_nonzero_positions',sum(map(len,rows[:N])))
print('square_bounds',f'[{sq_a}/{sq_B},{sq_b}/{sq_B}]')
print('square_q',format(float(q_sq),'.17g'))
print('square_delta_mu',format(float(Fraction(dMU,sq_E)),'.17g'))
print('square_delta_var',format(float(Fraction(dVAR,sq_E*sq_E)),'.17g'))
print('diagonal_stationary_bracket', '251/5000', '63/1250')
print('left_local_q',format(float(qll),'.17g'),'sign_prime', '<0')
print('right_local_q',format(float(qrr),'.17g'),'sign_prime','>0')
print('square_ratio_cert', 'q_R<285186/10000000')
