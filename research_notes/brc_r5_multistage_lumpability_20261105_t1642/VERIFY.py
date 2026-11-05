"""Exact rational finite test for R5 multistage observer lumpability."""
from fractions import Fraction as F
from random import Random
H=("A","B")
w={"A":F(2,5),"B":F(3,5)}
L={1:(F(1),),2:(F(1,2),F(1),F(3,2)),3:(F(1,4),F(1),F(7,4)),4:(F(1,8),F(1),F(15,8))}
K1={"A":(F(1,4),F(1,2),F(1,4)),"B":(F(3,8),F(1,4),F(3,8))}
K2={F(1,2):(F(3,4),F(1,6),F(1,12)),F(1):(F(1,4),F(1,2),F(1,4)),F(3,2):(F(1,12),F(1,6),F(3,4))}
K3={F(1,4):(F(25,28),F(1,14),F(1,28)),F(1):(F(1,4),F(1,2),F(1,4)),F(7,4):(F(1,28),F(1,14),F(25,28))}
for h in H:
    assert sum(K1[h])==1
    assert sum(x*y for x,y in zip(L[2],K1[h]))==1
    assert all(x>0 for x in K1[h])
for t,k in ((2,K2),(3,K3)):
    for r,row in k.items():
        assert all(x>0 for x in row) and sum(row)==1
        assert sum(x*y for x,y in zip(L[t+1],row))==r
assert all(K2[r][1]>0 for r in L[2])
assert K3[F(1)][0]>0 and K3[F(1)][2]>0
def transition(h,t,r):
    return K1[h] if t==1 else K2[r] if t==2 else K3[r]
def random_policy(rng,full):
    return {(h if full else None,t,r):
        (F(rng.randrange(13),12) if t<4 else F(0),F(rng.randrange(13),12))
        for h in (H if full else (None,)) for t in range(1,5) for r in L[t]}
def occupancies(policy,full):
    flow={(h,1,F(1)):w[h] for h in H}
    out={}
    for t in range(1,5):
        for h in H:
            for r in L[t]:
                mass=flow.get((h,t,r),F(0))
                key=(h if full else None,t,r)
                a,b=policy[key]
                cont=mass*a
                decl=(mass-cont)*b
                v=out.get(key,(F(0),F(0),F(0)))
                out[key]=(v[0]+mass,v[1]+cont,v[2]+decl)
                if t<4:
                    for nxt,p in zip(L[t+1],transition(h,t,r)):
                        z=(h,t+1,nxt)
                        flow[z]=flow.get(z,F(0))+cont*p
    return out
def four(obs):
    eQ=eP=TQ=TP=F(0)
    for (_,t,r),(m,c,d) in obs.items():
        eQ+=d
        eP+=r*(m-c-d)
        TQ+=m
        TP+=r*m
    return (eP,eQ,TP,TQ)
def mix(m1,m2,a):
    return {k:tuple(a*m1.get(k,(0,0,0))[i]+(1-a)*m2.get(k,(0,0,0))[i] for i in range(3))
            for k in set(m1)|set(m2)}
def inverse(obs):
    ans={}
    for k,(m,c,d) in obs.items():
        assert 0<=c<=m and 0<=d<=m-c
        ans[k]=(c/m if m else F(0),d/(m-c) if m>c else F(0))
    return ans
rng=Random(202611051642)
for full in (False,True):
    for i in range(120):
        a=F(rng.randrange(17),16)
        O1=occupancies(random_policy(rng,full),full)
        O2=occupancies(random_policy(rng,full),full)
        Om=mix(O1,O2,a)
        rec=occupancies(inverse(Om),full)
        assert rec==Om,(full,i)
        assert four(rec)==tuple(a*x+(1-a)*y for x,y in zip(four(O1),four(O2)))
print("PASS_EXACT_R5_FOUR_STAGE_LUMPABLE_REAL_IMAGE_CONVEXITY")
print("sources=2; horizon=4; ratio_stages=[1,3,3,3]")
print("strict_Q_kernels=PASS; P_martingale_means=PASS")
print("common_nonterminal_t3_merger=PASS; t3_to_t4_split=PASS")
print("LR_inverse_occupancy_mixtures=120; FULL_inverse_occupancy_mixtures=120")
print("arithmetic=fractions.Fraction; random_seed=202611051642")
