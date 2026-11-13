from fractions import Fraction as Q
from itertools import combinations
import json, hashlib

I=(Q(0),Q(1)); X=Q(1,4); TIMES=(-2,-1,0,1,2); BRANCHES=(0,1)
U=tuple(sorted(((t,b) for t in TIMES for b in BRANCHES),reverse=True))

def frac(x): return x-(x.numerator//x.denominator)

def eligible(t,q):
    y=frac(X+t*q); a=Q(0); b=frac(q)
    return False if a==b else (a<=y<b if a<b else (y>=a or y<b))

def cuts_t(t):
    forms=[(Q(t),X),(Q(0),Q(0)),(Q(1),Q(0)),(Q(t),X),(Q(t-1),X),(Q(1),Q(0))]
    res=set()
    for c,d in forms:
        if not c: continue
        v0=d; v1=c+d
        lo=min(v0,v1); hi=max(v0,v1)
        for n in range(lo.numerator//lo.denominator, hi.numerator//hi.denominator+2):
            q=(Q(n)-d)/c
            if I[0]<q<I[1]:res.add(q)
    return res

def atoms():
    cuts=sorted(set().union(*(cuts_t(t) for t in TIMES)))
    points=[I[0]]+cuts+[I[1]]
    reps=[]
    for k,pt in enumerate(points):
        if k:reps.append((points[k-1]+pt)/2)
        reps.append(pt)
    return cuts,reps

CUTS,ATOMS=atoms()
SIGS=tuple(tuple(eligible(t,q) for t in TIMES) for q in ATOMS)

def cap(F,G,sig):
    common=F&G; diff=F^G
    above=0
    for i,(t,b) in enumerate(U):
        if sig[TIMES.index(t)]:
            bit=1<<i
            if diff&bit:return above
            if common&bit:above+=1
    return None

def reachable_counts(F,G,max_h):
    n=len(U); size=2*n
    cur=[() for _ in ATOMS];counts=[]; witnesses=[]
    for h in range(max_h+1):
        for cs in combinations(range(size),h):
            f,g=F,G
            for j in cs:
                if j<n:f ^= 1<<j
                else:g ^= 1<<(j-n)
            for a,sig in enumerate(SIGS):cur[a] = cur[a] + (cap(f,g,sig),)
        groups={}
        for j,v in enumerate(cur):groups.setdefault(v,[]).append(j)
        counts.append(len(groups))
        witnesses.append(tuple(tuple(v) for v in groups.values() if len(v)>1))
        if len(groups)==len(set(SIGS)):break
    return counts

def h_bound(F,G):
    res={}
    for t in TIMES:
        res[t]=min(min((F^(1<<i)).bit_count()+G.bit_count(),F.bit_count()+(G^(1<<i)).bit_count()) for i,u in enumerate(U) if u[0]==t)
    return max(res.values()),res

# original R114 future-stable signature, all-histories observer should have exactly distinct signature vectors
D=len(set(SIGS))
CHECKS={}
for label,F,G in [
    ('empty',0,0),
    ('symmetric_full',(1<<len(U))-1,(1<<len(U))-1),
    ('single_top',1,0),
    ('single_low',1<<(len(U)-1),0),
    ('asymmetric_split',sum(1<<i for i in (0,2,4)),sum(1<<i for i in (1,3,5)))
]:
    bound,by_time=h_bound(F,G)
    c=reachable_counts(F,G,bound)
    assert c[-1]==D
    assert all(x<=y for x,y in zip(c,c[1:]))
    assert len(c)-1<=bound
    CHECKS[label]={'F':[U[i] for i in range(len(U)) if F>>i&1], 'G':[U[i] for i in range(len(U)) if G>>i&1], 'counts':c,'witness_horizon_upper':bound, 'time_bounds':by_time}

# Enumerate all starting history pairs for tiny U: use three distinct time positions with one branch only.
SMALL=tuple((t,0) for t in (-1,0,1))
small_sigs=tuple(tuple(eligible(t,q) for t,b in SMALL) for q in ATOMS)

def small_cap(f,g,s):
    above=0
    for i,(t,b) in reversed(tuple(enumerate(SMALL))):
        bit=1<<i
        if s[i]:
            if (f^g)&bit:return above
            if (f&g)&bit:above+=1
    return None

scoped_states_checked=0
for F in range(1<<3):
    for G in range(1<<3):
        observed=[() for _ in ATOMS]
        for h in range(7):
            for ds in combinations(range(6),h):
                f,g=F,G
                for v in ds:
                    if v<3:f^=1<<v
                    else:g^=1<<(v-3)
                for z,s in enumerate(small_sigs):observed[z]+=(small_cap(f,g,s),)
            classes=len(set(observed))
            assert classes<=len(set(small_sigs))
            if h==6:assert classes==len(set(small_sigs))
        scoped_states_checked+=1


# Independent direct ordered tuple oracle for exact all-k equality.
def topk(F,sig,k):
    return tuple(u for i,u in enumerate(U) if (F>>i)&1 and sig[TIMES.index(u[0])])[:k]

oracle_checks=0
for F in range(1<<len(SMALL)):
    for G in range(1<<len(SMALL)):
        bigF=sum(1<<U.index(u) for i,u in enumerate(SMALL) if (F>>i)&1)
        bigG=sum(1<<U.index(u) for i,u in enumerate(SMALL) if (G>>i)&1)
        for sig in SIGS:
            capacity=cap(bigF,bigG,sig)
            for k in range(1,len(SMALL)+2):
                equal=(topk(bigF,sig,k)==topk(bigG,sig,k))
                assert equal==(capacity is None or k<=capacity)
                oracle_checks+=1

# Find two parameters whose signatures diverge but do not diverge under one edit starting with top-only.
F=1;G=0
sig_pairs=[]
for i in range(len(ATOMS)):
    for j in range(i+1,len(ATOMS)):
        if SIGS[i]==SIGS[j]:continue
        same=True
        for a in range(1+2*len(U)):
            f,g=F,G
            if a>0:
                k=a-1
                if k<len(U):f^=1<<k
                else:g^=1<<(k-len(U))
            if cap(f,g,SIGS[i])!=cap(f,g,SIGS[j]):same=False;break
        if same:sig_pairs.append((i,j))

result={'status':'R115_PASS','frozen_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
'input':{'U':U,'times':TIMES,'branches':BRANCHES,'interval':['0','1'],'x':'1/4','arc':'[0,{theta}) on fractional circle'},
'cut_count':len(CUTS),'atom_count':len(ATOMS),'signatures':D,'max_atom_numerator_bits':max(q.numerator.bit_length() for q in ATOMS),'max_atom_denominator_bits':max(q.denominator.bit_length() for q in ATOMS), 'cases':CHECKS, 
'small_initial_pairs_exhausted':scoped_states_checked, 'direct_topk_oracle_checks':oracle_checks, 'small_parameter_signature_count':len(set(small_sigs)),
'one_edit_indistinguishable_nonidentical_signature_pairs':len(sig_pairs),
'example':{'theta':str(ATOMS[sig_pairs[0][0]]),'phi':str(ATOMS[sig_pairs[0][1]]),'theta_signature':SIGS[sig_pairs[0][0]],'phi_signature':SIGS[sig_pairs[0][1]]} if sig_pairs else None}
with open('verification_r115.json','w') as out:json.dump(result,out,indent=2,ensure_ascii=False,default=str)
print(json.dumps({k:v for k,v in result.items() if k not in ['cases','input']},ensure_ascii=False,default=str,indent=2))
for label,v in CHECKS.items():print(label,v['counts'],v['witness_horizon_upper'])
