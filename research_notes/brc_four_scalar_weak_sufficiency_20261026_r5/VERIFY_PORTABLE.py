from fractions import Fraction as F
from itertools import product

H = [()] + [(a,) for a in 'ab'] + [(a,e,z) for a in 'ab' for e in '+-' for z in '01']
P,Q = {():F(1)},{():F(1)}
for a in 'ab': P[(a,)]=Q[(a,)]=F(1,2)
for a in 'ab':
    for e in '+-':
        for z in '01':
            r=(F(3,4) if z=='0' else F(1,4)) if a=='a' else (F(1,4) if z=='0' else F(3,4))
            P[(a,e,z)]=F(1,4)*r
            Q[(a,e,z)]=(F(3,8) if e=='+' else F(1,8))*r
L={h:Q[h]/P[h] for h in H}
S=lambda h: (len(h),h[1] if len(h)==3 else '*')
T=lambda h: (len(h),(h[1],h[2]) if len(h)==3 else '*')

def evaluate(pi):
    live={h:F(0) for h in H}; live[()]=F(1)
    o=[F(0)]*4
    for h in H:
        p=pi(h);m=live[h]
        assert sum(p.values())==1 and all(v>=0 for v in p.values())
        assert len(h)<3 or 'C' not in p
        o[0]+=m*p.get('Q',0);o[1]+=m*L[h]*p.get('P',0)
        o[2]+=m*p.get('C',0);o[3]+=m*L[h]*p.get('C',0)
        if len(h)<3:
            kids=[(a,) for a in 'ab'] if not h else [g for g in H if len(g)==3 and g[0]==h[0]]
            for g in kids: live[g]+=m*p.get('C',0)*P[g]/P[h]
    return tuple(o),live

def quotient(pi,stat):
    target,live=evaluate(pi)
    accum={}
    for h in H:
        c=stat(h);d=accum.setdefault(c,{'P':F(0),'Q':F(0),'C':F(0)})
        for a,p in pi(h).items(): d[a]+=live[h]*p
    policy={}
    for c,d in accum.items():
        m=sum(d.values())
        policy[c]={a:v/m for a,v in d.items() if v} if m else {'P':F(1)}
    actual,other_live=evaluate(lambda h:policy[stat(h)])
    return target,actual,live,other_live

assert all(x>0 for x in P.values()) and all(x>0 for x in Q.values())
assert all(len({L[h] for h in H if T(h)==k})==1 for k in set(map(T,H)))
assert all(len({L[h] for h in H if S(h)==k})==1 for k in set(map(S,H)))
assert all(sum(P[(a,e,z)] for z in '01')/P[(a,)]==F(1,2) for a in 'ab' for e in '+-')
assert P[('a','+','0')]/P[('a',)]==F(3,8)!=F(1,8)==P[('b','+','0')]/P[('b',)]

def witness(h):
    return {'C':F(1)} if h in ((),('a',)) else {'P':F(1)} if h==('b',) or h[1]=='-' else {'Q':F(1)}
x,y,l,b=quotient(witness,T)
assert x==y==(F(1,4),F(5,8),F(3,2),F(3,2))
defect={(e,z):sum(l[h]-b[h] for h in H if len(h)==3 and h[1:]==(e,z)) for e in '+-' for z in '01'}
assert defect=={('+','0'):F(1,16),('+','1'):-F(1,16),('-','0'):F(1,16),('-','1'):-F(1,16)}

count=0; distinct=set()
for root in 'PQC':
    for a,b in product('PQC',repeat=2):
        for terminal in product('PQ',repeat=8):
            acts=dict(zip(H,[root,a,b]+list(terminal)))
            pi=lambda h:{acts[h]:F(1)}
            before,after,_,_=quotient(pi,S)
            assert before==after
            count+=1;distinct.add(before)
assert count==6912
print('STRICT_T_NONLUMPABILITY: 3/8 != 1/8')
print('S_LUMPABLE_P=(1/2,1/2), Q=(3/4,1/4)')
print('WITNESS',*(str(v) for v in x))
print('SIGNED_FINE_T_DEFECT',defect)
print('DETERMINISTIC_POLICIES',count,'DISTINCT_OBSERVERS',len(distinct))
print('ALL_AUTHOR_EXACT_CHECKS_PASS')
