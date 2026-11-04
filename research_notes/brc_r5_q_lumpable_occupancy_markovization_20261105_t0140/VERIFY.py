from fractions import Fraction as F
from collections import defaultdict
from random import Random

# Frozen R5 preceding source: two hidden histories A/B, then likelihood-ratio 1/2 or 3/2.
# Balanced continuation: A sees experiment E_A for c=0, E_B for c=1;
# B sees E_B for c=0, E_A for c=1. All Q path probabilities are strictly positive.
R2=(F(1,2),F(3,2))
U=((F(3,4),F(5,4)),(F(1,2),F(3,2)))
H=('A','B')
ACTIONS=('P','Q','C')


def experiment(h,c):
    return (0 if h=='A' else 1) ^ c

def policy(seed):
    rng=Random(seed)
    def law(k):
        weights=[rng.randrange(0,5) for _ in range(k)]
        if sum(weights)==0: weights[0]=1
        s=sum(weights)
        return tuple(F(w,s) for w in weights)
    first={h:law(3) for h in H}
    second={(h,s):law(3) for h in H for s in range(2)}
    third={(h,s,c,j):law(2) for h in H for s in range(2)
           for c in range(2) for j in range(2)}
    return first,second,third


def observation_full(p):
    first,second,third=p
    key_mass=defaultdict(F)
    key_action=defaultdict(F)
    obs=[F(0)]*4
    def put(t,r,q,acts,labels):
        key=(t,r)
        key_mass[key]+=q
        for a,prob in zip(labels,acts):
            key_action[(t,r,a)]+=q*prob
            if a=='P':
                obs[1]+=q*prob
                obs[2]+=q*r*prob*t
                obs[3]+=q*prob*t
            elif a=='Q':
                obs[0]+=q*r*prob
                obs[2]+=q*r*prob*t
                obs[3]+=q*prob*t
        return q*acts[labels.index('C')] if 'C' in labels else F(0)
    for h in H:
        q2=put(1,F(1),F(1,2),first[h],ACTIONS)
        for s in range(2):
            r2=R2[s]
            q3=put(2,r2,q2/2,second[(h,s)],ACTIONS)
            for c in range(2):
                e=experiment(h,c)
                for j in range(2):
                    r3=r2*U[e][j]
                    put(3,r3,q3/4,third[(h,s,c,j)],('P','Q'))
    return tuple(obs),key_mass,key_action


def markovize(mass,actions):
    out={}
    for (t,r),q in mass.items():
        labels=('P','Q','C') if t<3 else ('P','Q')
        out[(t,r)]={a:actions[(t,r,a)]/q for a in labels} if q else {
            a:F(int(a==labels[0])) for a in labels}
    return out


def observation_lr(p):
    obs=[F(0)]*4
    keys={F(1):F(1)}
    for t in (1,2,3):
        next_keys=defaultdict(F)
        for r,q in keys.items():
            pi=p[(t,r)]
            qp=q*pi['P']
            qq=q*pi['Q']
            obs[1]+=qp
            obs[0]+=r*qq
            obs[2]+=t*r*(qp+qq)
            obs[3]+=t*(qp+qq)
            qc=q*pi.get('C',F(0))
            if t==1:
                for r2 in R2: next_keys[r2]+=qc/2
            elif t==2:
                for u in (F(3,4),F(5,4),F(1,2),F(3,2)):
                    next_keys[r*u]+=qc/4
        keys=next_keys
    return tuple(obs)


# First print a deterministic adversarial example involving overlapping LR=3/4 terminal histories.
first={h:(F(0),F(0),F(1)) for h in H}
second={(h,s):((F(1),F(0),F(0)) if h=='A' and s==1 else
               (F(0),F(1),F(0)) if h=='B' and s==0 else
               (F(0),F(0),F(1))) for h in H for s in range(2)}
third={(h,s,c,j):((F(1),F(0)) if h=='A' else (F(0),F(1)))
       for h in H for s in range(2) for c in range(2) for j in range(2)}
o,m,a=observation_full((first,second,third))
pi=markovize(m,a)
assert o==observation_lr(pi)
assert (3,F(3,4)) in pi and 0<pi[(3,F(3,4))]['P']<1
print('example FULL=LR observation',o)
print('example terminal LR=3/4 P-declaration probability',pi[(3,F(3,4))]['P'])
print('Q key-kernel at t=2 for each hidden history: 1/4 each of multipliers',U[0]+U[1])

# Exact arbitrary rational behavioral-policy tests. These test the constructive map,
# not the all-real theorem (which follows from the occupancy induction).
for seed in range(512):
    oo,mm,aa=observation_full(policy(seed))
    lr=markovize(mm,aa)
    assert oo==observation_lr(lr),(seed,oo,observation_lr(lr))
    for laws in lr.values():
        assert all(F(0)<=v<=1 for v in laws.values())
        assert sum(laws.values())==1
print('exact rational behavioral FULL-to-LR reconstruction checks',512)
assert set(R2)=={F(1,2),F(3,2)}
assert len({r*u for r in R2 for u in U[0]+U[1]})==7
assert sum(U[0])==sum(U[1])==2
print('positive terminal LR key count',7)
print('PASS_EXACT_R5_Q_LUMPABLE_OCCUPANCY_MARKOVIZATION')
