#!/usr/bin/env python3
"""Stage409-B: exact X6-embedded Euler/K transfer and independent finite checks."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product
import json

ALPH = ('A','B')
AXIS = {'A':(0,1),'B':(0,-1),'C':(2,1),'D':(2,-1)}
OPPOSITE = {'A':'B','B':'A','C':'D','D':'C'}
M = 8
P = 'A'*M
TARGET = {('A','A'):3,('A','B'):2,('B','A'):2}

def edges(w):
    return Counter(zip(w,w[1:]))

def last_arun(w):
    return len(w)-len(w.rstrip('A'))

def observe(p,q):
    def end(w):
        z=[0]*6
        for c in w:
            i,s=AXIS[c]; z[i]+=s
        return tuple(z)
    return (len(p),len(q),end(p),end(q),tuple(sorted(edges(p).items())),
            tuple(sorted(edges(q).items())),sum(a==b for a,b in zip(p,q)))

# Residual-edge exact transfer (counts equivalent prefixes, not complete histories).
# State: last letter, remaining labelled edges, last-4 suffix, signed Q endpoint,
# synchronized K; P=A^8 so K is the Q count of A.
def euler_k_dp():
    edge_types=tuple(sorted(TARGET))
    rem0=tuple(TARGET[t] for t in edge_types)
    state=Counter()
    for c in ALPH:
        state[(c,rem0,c, 1 if c=='A' else -1, int(c=='A'))]+=1
    max_states=len(state)
    for step in range(1,M):
        new=Counter()
        for (last,rem,suf,z,k),count in state.items():
            for j,(a,b) in enumerate(edge_types):
                if a!=last or not rem[j]: continue
                r=list(rem);r[j]-=1
                new[(b,tuple(r),(suf+b)[-4:],z+(1 if b=='A' else -1),k+int(b=='A'))]+=count
        state=new
        max_states=max(max_states,len(state))
    dist=Counter()
    for (last,rem,suf,z,k),count in state.items():
        if not any(rem) and z==4 and k==6:
            dist[suf]+=count
    return dist,max_states

def descendants(q):
    """Only used for small finite future cross-check, not for proof of infinite scope."""
    return q

def act(p,q,kind,a=None,b=None):
    if kind=='APP':return (p+a,q+b)
    if kind=='POP':return None if not q else (p,q[:-1])
    if kind=='CANCEL':
        if len(p)<2 or len(q)<2 or OPPOSITE[p[-1]]!=p[-2] or OPPOSITE[q[-1]]!=q[-2]:return None
        return (p[:-2],q[:-2])
    raise ValueError(kind)

def finite_compare(q1,q2,steps=4):
    init=((P,q1),(P,q2),0,0,0,0)
    todo=deque([init]); seen={init}; transitions=0
    while todo:
        a,b,pop,cancel,consec,depth=todo.popleft()
        assert observe(*a)==observe(*b),(q1,q2,depth,'observation')
        if depth>=steps:continue
        actions=[('POP',None,None),('CANCEL',None,None)]
        if consec<2:actions += [('APP',x,y) for x in ('A','B','C') for y in ('A','B','C')]
        for op,x,y in actions:
            if op=='POP' and pop:continue
            if op=='CANCEL' and cancel:continue
            na=act(*a,op,x,y);nb=act(*b,op,x,y);transitions+=1
            assert (na is None)==(nb is None),(q1,q2,depth,op,x,y,'enabledness')
            if na is None:continue
            st=(na,nb,pop+(op=='POP'),cancel+(op=='CANCEL'),consec+1 if op=='APP' else 0,depth+1)
            assert observe(*na)==observe(*nb),(q1,q2,depth,op,x,y,'observations differ')
            if st not in seen:seen.add(st);todo.append(st)
    return len(seen),transitions

def brc8():
    dirs=tuple((i,s) for i in range(6) for s in (-1,1))
    a={(0,)*6:(1,1)}
    for _ in range(M):
        b=defaultdict(lambda:[0,0])
        for z,(n,w) in a.items():
            for i,s in dirs:
                zz=list(z);zz[i]+=s;zz=tuple(zz)
                wt=2 if (i,s)==(0,1) else 3 if (i,s)==(0,-1) else 1
                b[zz][0]+=n;b[zz][1]+=w*wt
        a=b
    return {'P_8E1':a[(8,0,0,0,0,0)],'Q_4E1':a[(4,0,0,0,0,0)]}

def main():
    d,peak=euler_k_dp()
    brute=Counter();qwords=[]
    for bits in product(ALPH,repeat=M):
        w=''.join(bits)
        if edges(w)==Counter(TARGET) and sum(c=='A' for c in w)==6:
            brute[w[-4:]]+=1;qwords.append(w)
    assert d==brute,(d,brute)
    assert len(qwords)==10
    by_class=defaultdict(list)
    for q in qwords:by_class[min(3,last_arun(q))].append(q)
    assert {i:len(v) for i,v in by_class.items()}=={1:4,2:3,3:3}
    checks=[]
    for g,words in sorted(by_class.items()):
        for j in range(len(words)):
            for k in range(j+1,len(words)):
                n,t=finite_compare(words[j],words[k]);checks.append((g,words[j],words[k],n,t))
    # One-POP distinguishes class 1 from 2/3. POP,APP(B,B),CANCEL separates class 2 from 3.
    reps={g:words[0] for g,words in by_class.items()}
    o1=observe(*act(P,reps[1],'POP'))
    o2=observe(*act(P,reps[2],'POP'))
    o3=observe(*act(P,reps[3],'POP'))
    assert o1!=o2 and o1!=o3 and o2==o3
    s2=(P,reps[2]);s3=(P,reps[3])
    for op,x,y in [('POP',None,None),('APP','B','B'),('CANCEL',None,None)]:
        s2=act(*s2,op,x,y);s3=act(*s3,op,x,y)
        assert s2 is not None and s3 is not None
    assert observe(*s2)!=observe(*s3)
    out={
        'status':'STAGE409B_EULER_K_THREE_CLASS_PASS',
        'input':{'P':'A'*8,'m':8,'J_Q':{'AA':3,'AB':2,'BA':2},'K':6,'Z_Q': '4E1','native_alphabet':'12 signed X6 directions'},
        'transfer':{'peak_distinct_states':peak,'suffix4_counts':dict(sorted(d.items())),'total_fiber':sum(d.values())},
        'independent_bruteforce':{'words':sorted(qwords),'suffix4_counts':dict(sorted(brute.items()))},
        'exact_quotient':{'classes':{str(g):sorted(words) for g,words in sorted(by_class.items())},'class_sizes':{str(g):len(words) for g,words in sorted(by_class.items())},'q':len(by_class),'raw_suffix4_states':len(d)},
        'finite_three_symbol_crosschecks':{'pairs':len(checks),'visited_states':sum(x[3] for x in checks),'transitions':sum(x[4] for x in checks),'operation_depth':4,'APP_alphabet':['A','B','C']},
        'separation':{'class1_POP':'different J after Q POP','class2_vs3':'POP_Q, APP(B,B), CANCEL yields different J_Q'},
        'native_brc_integer_recurrence':brc8()
    }
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
