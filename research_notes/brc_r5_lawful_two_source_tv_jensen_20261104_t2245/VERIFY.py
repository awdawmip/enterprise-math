from fractions import Fraction as F
from itertools import product

H=("A","B")
S=("+","-")
w={"A":F(1,2),"B":F(1,2)}
q={(h,s):F(1,2) for h in H for s in S}
p={('A','+'):F(3,4),('A','-'):F(1,4),('B','+'):F(5,8),('B','-'):F(3,8)}
r={k:p[k]/q[k] for k in p}
assert len(set(r.values())) == 4

def observe(first,terminal):
    ep=eq=F(0)
    tp=tq=F(1)
    for h in H:
        a=first[h]
        if a == 'P': eq += w[h]
        elif a == 'Q': ep += w[h]
        else:
            tp += w[h]
            tq += w[h]
            for s in S:
                if terminal[(h,s)]=='P': eq += w[h]*q[(h,s)]
                else: ep += w[h]*p[(h,s)]
    return ep,eq,tp,tq

terms=list(product('PQ',repeat=4))
def decisions(t):return dict(zip(product(H,S),t))
full=[]
for x in product('PQC',repeat=2):
    for t in terms:
        full.append(observe(dict(zip(H,x)),decisions(t)))
lr=[]
for a in ('P','Q'):
    lr.append(observe({h:a for h in H},decisions(terms[0])))
for t in terms:
    lr.append(observe({h:'C' for h in H},decisions(t)))
assert len(full)==144 and len(lr)==18

def support(points,lam):
    return max(-v[0]-v[1]-lam*v[2] for v in points)

delta={h:sum(abs(p[(h,s)]-q[(h,s)]) for s in S)/2 for h in H}
assert delta=={'A':F(1,4),'B':F(1,8)}
mean=sum(w[h]*delta[h] for h in H)
assert mean==F(3,16)
def plus(x):return max(F(0),x)
for lam in (F(0),F(1,16),F(1,8),F(3,16),F(1,4),F(3,8),F(1)):
    f=support(full,lam)
    l=support(lr,lam)
    analytic_f=-(1+lam)+sum(w[h]*plus(delta[h]-lam) for h in H)
    analytic_l=-(1+lam)+plus(mean-lam)
    assert (f,l)==(analytic_f,analytic_l), (lam,f,l,analytic_f,analytic_l)
    print('lambda',lam,'FULL',f,'LR',l,'gap',f-l)

lam=F(3,16)
W=observe({'A':'C','B':'Q'},
          {('A','+'):'P',('A','-'):'Q',('B','+'):'P',('B','-'):'Q'})
assert W==(F(5,8),F(1,4),F(3,2),F(3,2))
assert -W[0]-W[1]-lam*W[2]==support(full,lam)
assert support(full,lam)-support(lr,lam)==F(1,32)
assert (support(full,lam)-support(lr,lam))/(2+lam)==F(1,70)
assert support(full,lam)-support(lr,lam)==sum(w[h]*abs(delta[h]-mean) for h in H)/2
print('witness',W,'hFULL',support(full,lam),'hLR',support(lr,lam),'Linf_lower',F(1,70))
print('FULL deterministic',len(full),'LR deterministic',len(lr),'unique FULL',len(set(full)),'unique LR',len(set(lr)))
print('PASS_EXACT_R5_LAWFUL_TWO_SOURCE_TV_JENSEN')
