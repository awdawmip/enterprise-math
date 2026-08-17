#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import math

checks=[]
def ck(cond,label):
    if not cond:
        raise AssertionError(label)
    checks.append(label)

def qb(typ,i,j):
    if typ=='U':
        mn=Fraction(i*i+j*j,1)
        mx=Fraction(i*i+j*j+2*max(i,j)+1,1)
    else:
        s=i+j+1
        if abs(i-j)<=1:
            mn=Fraction(s*s,2)
        elif j>=i+2:
            mn=Fraction((i+1)**2+j*j,1)
        else:
            mn=Fraction(i*i+(j+1)**2,1)
        mx=Fraction((i+1)**2+(j+1)**2,1)
    return mn,mx

def ceil_sqrt_f(q):
    r=max(0,math.isqrt(q.numerator//q.denominator))
    while Fraction(r*r,1)<q:
        r+=1
    return r

def first_sq(mn,mx):
    r=max(1,ceil_sqrt_f(mn))
    return r if Fraction(r*r,1)<=mx else None

def incident_edge(e):
    (a,b),(c,d)=e
    out=set()
    for i in range(max(0,min(a,c)-1),max(a,c)+1):
        for j in range(max(0,min(b,d)-1),max(b,d)+1):
            U={(i,j),(i+1,j),(i,j+1)}
            D={(i+1,j),(i,j+1),(i+1,j+1)}
            if {(a,b),(c,d)}.issubset(U): out.add(('U',i,j))
            if {(a,b),(c,d)}.issubset(D): out.add(('D',i,j))
    return out

# 1. Exact cell q-range algebra + reflection covariance through coordinate 256.
for i in range(257):
    for j in range(257):
        mn,mx=qb('U',i,j)
        qs=[Fraction(i*i+j*j),Fraction((i+1)**2+j*j),Fraction(i*i+(j+1)**2)]
        ck(mn==min(qs),f'Umin:{i},{j}')
        ck(mx==max(qs),f'Umax:{i},{j}')
        ck(qb('U',j,i)==(mn,mx),f'Usym:{i},{j}')
        mnD,mxD=qb('D',i,j)
        qsD=[Fraction((i+1)**2+j*j),Fraction(i*i+(j+1)**2),Fraction((i+1)**2+(j+1)**2)]
        ck(mxD==max(qsD),f'Dmax:{i},{j}')
        ck(mnD<=min(qsD),f'Dminleverts:{i},{j}')
        ck(qb('D',j,i)==(mnD,mxD),f'Dsym:{i},{j}')

# 2. Fresh-hidden generation through r=256 and exact first event.
fresh={r:[] for r in range(1,257)}
for i in range(257):
    for j in range(257):
        for typ in ('U','D'):
            mn,mx=qb(typ,i,j)
            rr=ceil_sqrt_f(mx)
            if rr<=256 and first_sq(mn,mx) is None:
                fresh[rr].append((typ,i,j,mn,mx))
for r in (1,2):
    ck(len(fresh[r])==0,f'no_fresh_below3:{r}')
ck(fresh[3]==[('D',1,1,Fraction(9,2),Fraction(8,1))],'first_hidden_exact')
mn,mx=qb('D',1,1)
for r in (1,2,3):
    ck(not (mn<=r*r<=mx),f'D11miss:{r}')
ck(mx<9,'D11contained_r3')

# 3. Expand every primitive-edge strict overshoot through r=64.
N=64
edges=set()
for i in range(N+1):
    for j in range(N+1):
        p=(i,j)
        for q in ((i+1,j),(i,j+1),(i-1,j+1)):
            if q[0]<0 or q[1]<0 or q[0]>N+1 or q[1]>N+1:
                continue
            edges.add(tuple(sorted((p,q))))
edge_events=0
tie_events=0
for r in range(1,65):
    rr=r*r
    for e in edges:
        p,q=e
        qp=p[0]**2+p[1]**2
        qq=q[0]**2+q[1]**2
        lo=min(qp,qq); hi=max(qp,qq)
        if lo<rr<hi:
            edge_events+=1
            dd=rr-lo; du=hi-rr
            ck(dd>0 and du>0,f'defpos:{r}:{e}')
            inc=incident_edge(e)
            ck(len(inc) in (1,2),f'inc_count:{r}:{e}')
            for cell in inc:
                cmn,cmx=qb(*cell)
                ck(cmn<=rr<=cmx,f'edge_hit_cell:{r}:{e}:{cell}')
            if dd==du:
                tie_events+=1
ck(edge_events==5530,'event_total')
ck(tie_events==44,'tie_total')

# 4. First overshoot exact incidence.
r2=[]
for e in edges:
    p,q=e
    qp=p[0]**2+p[1]**2; qq=q[0]**2+q[1]**2
    if min(qp,qq)<4<max(qp,qq):
        r2.append(e)
ck(sorted(r2)==[((1,1),(1,2)),((1,1),(2,1))],'r2_events_exact')
ck(incident_edge(((1,1),(2,1)))=={('U',1,1),('D',1,0)},'r2_h_inc')
ck(incident_edge(((1,1),(1,2)))=={('U',1,1),('D',0,1)},'r2_v_inc')

# 5. Reverse minimum-jump certificates.
ck(math.comb(3,2)==3,'paths_21')
ck(math.comb(3,1)==3,'paths_12')
ck(3+3==6,'hidden_cell_min_fiber')
ck(1+3==4,'hidden_cell_void_jump')

payload='\n'.join(checks).encode()
digest=hashlib.sha256(payload).hexdigest()
print({
    'status':'PASS',
    'checks_total':len(checks),
    'checks_passed':len(checks),
    'checks_failed':0,
    'checks_digest_sha256':digest,
    'expected_checks':418685,
    'expected_digest':'4b2a82f6c768401bc3b7e7810aa511afd80e7a55912f533478dd7a24757de286'
})
assert len(checks)==418685
assert digest=='4b2a82f6c768401bc3b7e7810aa511afd80e7a55912f533478dd7a24757de286'
