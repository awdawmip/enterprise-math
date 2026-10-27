"""Exact N=3 BRC early-stop activation/masking verifier."""
from fractions import Fraction as F
from itertools import product

ONE=F(1)
HIST=('A','B')
SECOND=('C','L','H')
YR={'C':ONE,'L':F(1,4),'H':F(7,4)}
T2={'C':F(1,2),'L':F(1,4),'H':F(1,4)}
FINAL_Y=(F(1,4),ONE,F(7,4))
K={'A':(F(2,5),F(1,5),F(2,5)),
   'B':(F(1,20),F(9,10),F(1,20))}

assert sum(T2.values())==1
assert sum(T2[z]*YR[z] for z in SECOND)==1
for h in HIST:
    assert sum(K[h])==1
    assert sum(k*y for k,y in zip(K[h],FINAL_Y))==1

leaves=[]
for h in HIST:
    for z in SECOND:
        q2=F(1,2)*T2[z]
        ys=zip(FINAL_Y,K[h]) if z=='C' else [(YR[z],ONE)]
        for y,k in ys:
            q3=q2*k
            p3=q3*y
            leaves.append((h,z,y,q3,p3))
assert len(leaves)==10
assert all(q>0 and p>0 for h,z,y,q,p in leaves)
assert sum(row[3] for row in leaves)==1
assert sum(row[4] for row in leaves)==1
for h in HIST:
    assert sum(row[3] for row in leaves if row[0]==h)==F(1,2)
    assert sum(row[4] for row in leaves if row[0]==h)==F(1,2)

def observer(early,late):
    err_p=err_q=et_p=et_q=F(0)
    for h,z,y,q,p in leaves:
        if not early(h):
            tau,r=1,ONE
        elif not late(h,z):
            tau,r=2,YR[z]
        else:
            tau,r=3,y
        decide_q=r<ONE
        err_p+=p if decide_q else 0
        err_q+=q if not decide_q else 0
        et_p+=tau*p
        et_q+=tau*q
    return err_p,err_q,et_p,et_q

def objective(o,s):
    return o[0]+o[1]+s*o[3]

def exhaustive(s):
    full=[]
    for alpha in product((False,True),repeat=2):
        for beta in product((False,True),repeat=6):
            a=dict(zip(HIST,alpha))
            b=dict(zip(product(HIST,SECOND),beta))
            o=observer(lambda h:a[h],lambda h,z:b[h,z])
            full.append((objective(o,s),alpha,beta,o))
    lr=[]
    for a in (False,True):
        for beta in product((False,True),repeat=3):
            b=dict(zip(SECOND,beta))
            o=observer(lambda h:a,lambda h,z:b[z])
            lr.append((objective(o,s),a,beta,o))
    return min(full),min(lr),len(full),len(lr)

def bellman(s):
    d={h:ONE-sum(k*min(y,ONE) for k,y in zip(K[h],FINAL_Y))
       for h in HIST}
    db=(d['A']+d['B'])/2
    b=F(3,16)
    v_full=ONE+s+sum((min(F(0),s-b+F(1,2)*min(F(0),s-d[h]))
                     for h in HIST),F(0))/2
    v_lr=ONE+s+min(F(0),s-b+F(1,2)*min(F(0),s-db))
    return v_full,v_lr,d,db,b

def phase_gap(s):
    assert s>=0
    if s<=F(3,80): return F(0)
    if s<=F(27,160): return (s-F(3,80))/4
    if s<=F(3,16): return (F(3,10)-s)/4
    if s<=F(9,40): return F(27,160)-F(3,4)*s
    return F(0)

print('MODEL=positive_rational_N3_ten_leaf_optional_stop')
print('Q_TOTAL=',sum(row[3] for row in leaves),'P_TOTAL=',sum(row[4] for row in leaves))
print('t1_Q_histories=',tuple(F(1,2) for h in HIST))
print('t2_LR_alphabet=',tuple(YR[z] for z in SECOND))
print('t3_LR_alphabet=',FINAL_Y)
print('terminal_Q_kernels=',K)

for s in (F(1,16),F(1,4)):
    bf,bl,d,db,b=bellman(s)
    f,l,nf,nl=exhaustive(s)
    assert f[0]==bf and l[0]==bl
    assert nf==256 and nl==16 and l[0]>=f[0]
    assert s-d['A']<0<s-d['B']
    print('s=',s,'d_A=',d['A'],'d_B=',d['B'],'d_bar=',db,'t1_gain=',b)
    print('V_full=',f[0],'V_LR=',l[0],'GAP=',l[0]-f[0])
    print('full_witness_early=',f[1],'late=',f[2],'O=',f[3])
    print('lr_witness_early=',l[1],'late=',l[2],'O=',l[3])
    if s==F(1,16):
        assert f[0]==F(281,320) and l[0]==F(283,320)
        assert l[0]-f[0]==F(1,160)
        assert f[1]==(True,True) and l[1] is True
    if s==F(1,4):
        assert f[0]==l[0]==F(5,4)
        assert f[1]==(False,False) and l[1] is False

breakpoints=(F(0),F(3,80),F(27,160),F(3,16),F(9,40),F(1,4))
samples=breakpoints+tuple((a+b)/2 for a,b in zip(breakpoints,breakpoints[1:]))
for s in samples:
    f,l,d,db,b=bellman(s)
    assert l-f==phase_gap(s), (s,l-f,phase_gap(s))
    full_min,lr_min,_,_=exhaustive(s)
    assert full_min[0]==f and lr_min[0]==l, s
assert phase_gap(F(27,160))==F(21,640)
print('phase_breakpoints=',breakpoints)
print('phase_max_gap=',F(21,640),'at_s=',F(27,160))
print('phase_symbolic_segments_verified_by_rational_bellman_and_vertex_checks=',len(samples))
print('ALL EXACT CHECKS PASSED')
