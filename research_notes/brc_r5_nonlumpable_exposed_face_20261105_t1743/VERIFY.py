"""Exact finite R5 verification. Python3 stdlib Fraction; all 5832 deterministic LR strategies."""
from fractions import Fraction as F
from itertools import product
R2=(F(3,4),F(5,4)); R3=(F(1,2),F(1),F(3,2)); R4=(F(1,10),F(1),F(19,10))
q2=(F(1,2),F(1,2))
q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
q4_common={R3[0]:(F(509,900),F(382,900),F(9,900)),
           R3[2]:(F(9,900),F(382,900),F(509,900))}
q4_merge={R2[0]:(F(1,90),F(44,45),F(1,90)),
          R2[1]:(F(67,162),F(14,81),F(67,162))}
N=(-F(1),-F(1),-F(3,25),F(1,50))
def obs(acts):
    a1,a2,a3,a4=acts
    ep=eq=tp=tq=F(0)
    def stop(r,m,act):
        nonlocal ep,eq
        if act=='P':eq+=m
        elif act=='Q':ep+=r*m
        else:raise ValueError(act)
    if a1!='C':
        stop(F(1),F(1),a1)
        return (ep,eq,F(1),F(1))
    tp=tq=F(2)
    for i,r2 in enumerate(R2):
        m2=q2[i]
        if a2[i]!='C':
            stop(r2,m2,a2[i]);continue
        tp+=r2*m2; tq+=m2
        for j,r3 in enumerate(R3):
            m3=m2*q3[i][j]
            if a3[j]!='C':
                stop(r3,m3,a3[j]);continue
            tp+=r3*m3; tq+=m3
            row=q4_merge[r2] if j==1 else q4_common[r3]
            for k,r4 in enumerate(R4):
                stop(r4,m3*row[k],a4[k])
    return ep,eq,tp,tq
def score(v):return sum(n*x for n,x in zip(N,v))
def check_rows():
    assert sum(q2)==1 and sum(q2[i]*R2[i] for i in range(2))==1
    for i,r in enumerate(R2):
        row=q3[i]
        assert all(p>0 for p in row) and sum(row)==1
        assert sum(p*s for p,s in zip(row,R3))==r
    for r,row in list(q4_common.items())+[(F(1),row) for row in q4_merge.values()]:
        assert all(p>0 for p in row) and sum(row)==1
        assert sum(p*s for p,s in zip(row,R4))==r
    assert q4_merge[R2[0]] != q4_merge[R2[1]]
check_rows()
A=('C',('C','P'),('Q','Q','P'),('Q','Q','P'))
B=('C',('Q','C'),('Q','C','P'),('Q','Q','P'))
wa,wb=obs(A),obs(B)
assert wa==(F(21,80),F(23,40),F(19,8),F(5,2))
assert wb==(F(773,1800),F(16,45),F(57,20),F(109,40))
mid=tuple((x+y)/2 for x,y in zip(wa,wb))
assert mid==(F(2491,7200),F(67,144),F(209,80),F(209,80))
assert score(wa)==score(wb)==score(mid)==-F(429,400)
mx=None; mt=set(); ct=0; tot=0
for a1 in 'PQC':
  for a2 in product('PQC',repeat=2):
    for a3 in product('PQC',repeat=3):
      for a4 in product('PQ',repeat=3):
        v=obs((a1,a2,a3,a4));s=score(v);tot+=1
        if mx is None or s>mx:mx=s;mt={(v[2],v[3])};ct=1
        elif s==mx:mt.add((v[2],v[3]));ct+=1
assert tot==5832 and mx==-F(429,400)
assert mt=={(F(19,8),F(5,2)),(F(57,20),F(109,40))}
assert (mid[2],mid[3]) not in mt
for i,r in enumerate(R2):
    g=min(r,1)-sum(p*min(s,1) for p,s in zip(q3[i],R3))
    c=F(3,25)*r-F(1,50)
    assert g-c==(F(1,200),-F(47,400))[i]
    row=q4_merge[r]
    g2=1-sum(p*min(s,1) for p,s in zip(row,R4))
    assert q3[i][1]*(g2-F(1,10))==(-F(9,500),F(49,400))[i]
for r in (R3[0],R3[2]):
    row=q4_common[r]
    g=min(r,1)-sum(p*min(s,1) for p,s in zip(row,R4))
    assert g==F(9,1000) and g<F(3,25)*r-F(1,50)
print('MODEL=2 observable stage2 ratios; one nonlumpable shared (t3,r=1) key; four stages')
print('N=',N)
print('A=',wa,'score=',score(wa))
print('B=',wb,'score=',score(wb))
print('MID=',mid,'score=',score(mid))
print('MAX_DETERMINISTIC=',mx,'MAX_COUNT=',ct,'MAX_TIMES=',sorted(mt))
print('POLICIES_EXHAUSTED=',tot)
print('PROOF: two isolated all-real support-maximizing timing patterns; midpoint excluded')
print('PASS_EXACT_R5_NONLUMPABLE_NONCONVEX_REAL_O4')
