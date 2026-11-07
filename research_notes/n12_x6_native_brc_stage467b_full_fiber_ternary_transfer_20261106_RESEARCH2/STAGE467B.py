"""Stage467-B: native-X6 ternary full-initial-observer-fiber BRC tail transfer.
Model: ordered P,Q, 2<=m<n, first letters A, h_Q original-or-appended POP,
Q APPEND>=1 all 12 signed-X6 directions, no P operations. Ternary original
letters A=+E1,B=+E2,C=+E3. The future equivalence label is the tail of
Q emissions i>=t=max(1,n-h_Q), P emissions i>t. All arithmetic exact integer.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
import json

ABC=(0,2,4) # signed native X6 direction codes
DIRS=tuple(range(12))
D=25   # P counts(3), Q counts(3), P directed edges(9), Q edges(9), K(1)
Z=(0,)*D

def inc(s, p, q, oldp=None, oldq=None, bridge=True):
    x=list(s)
    if p is not None:
        x[p//2]+=1
        if bridge and oldp is not None:x[6+3*(oldp//2)+(p//2)]+=1
    if q is not None:
        x[3+q//2]+=1
        if bridge and oldq is not None:x[15+3*(oldq//2)+(q//2)]+=1
    if p is not None and q is not None and p==q:x[24]+=1
    return tuple(x)

def obs(p,q):
    x=Z; pp=qq=None
    for i in range(max(len(p),len(q))):
        a=p[i] if i<len(p) else None
        b=q[i] if i<len(q) else None
        x=inc(x,a,b,pp,qq)
        if a is not None:pp=a
        if b is not None:qq=b
    return x

def native_observer(p,q):
    # Original 12-direction observer: full signed X6 endpoint and 12x12 edges.
    def endpoint(w):
        v=[0]*6
        for a in w:v[a//2]+= (1 if a%2==0 else -1)
        return tuple(v)
    def adj(w):
        z=[0]*144
        for a,b in zip(w,w[1:]):z[a*12+b]+=1
        return tuple(z)
    return (len(p),len(q),endpoint(p),endpoint(q),adj(p),adj(q),sum(a==b for a,b in zip(p,q)))

def tail_key(p,q,hq):
    m=len(p);n=len(q);t=max(1,n-hq)
    return tuple((p[i-1],q[i-1]) if t<i<=m else (q[i-1],) for i in range(t,n+1))

class TailTransfer:
    def __init__(self,m,n,hq,target):
        assert 2<=m<n and 0<=hq<=n and len(target)==D
        self.m,self.n,self.hq,self.t=m,n,hq,max(1,n-hq)
        self.target=tuple(target)
        # Prefix transfer counts *source-distinct histories*, indexed by
        # additive observer and the two last native directions at the cut.
        states={(Z,None,None):1}
        for i in range(1,self.t):
            nxt=defaultdict(int)
            for (stats,lp,lq),weight in states.items():
                for p in ((0,) if i==1 else ABC) if i<=m else (None,):
                    for q in (0,) if i==1 else ABC:
                        v=inc(stats,p,q,lp,lq)
                        if all(v[j]<=target[j] for j in range(D)):
                            nxt[(v,p if p is not None else lp,q)]+=weight
            states=nxt
        # At cut index t, Q_t is visible, while P_t remains hidden.
        # Preserve P_t as a hidden boundary letter so [P_t=Q_t] is
        # decided only when the visible Q_t has been chosen.
        boundary=defaultdict(int)
        for (stat,lp,lq),weight in states.items():
            for pt in (((0,) if self.t==1 else ABC) if self.t<=self.m else (None,)):
                v=inc(stat,pt,None,lp,None)
                if all(v[j]<=target[j] for j in range(D)):
                    boundary[(v,pt if pt is not None else lp,lq,pt)]+=weight
        self.prefix=boundary
        self.visited=0
        self._f=lru_cache(None)(self._rec)

    def terminal_mass(self,vis,fp,fq):
        # A completed visible label has a single additive state; hidden
        # completions are summed, not used to branch the support language.
        # Constant-sized bridge boundary enumeration indexed into the
        # positive-integer hidden-prefix transfer table.
        mass=0
        lp_options=ABC if self.t>1 else ((0,) if self.t<=self.m else (None,))
        lq_options=ABC if self.t>1 else (None,)
        for lp in lp_options:
            for lq in lq_options:
                pt=lp if self.t<=self.m else None
                need=[self.target[j]-vis[j] for j in range(D)]
                if fp is not None and lp is not None:
                    need[6+3*(lp//2)+(fp//2)]-=1
                if fq is not None and lq is not None:
                    need[15+3*(lq//2)+(fq//2)]-=1
                if pt is not None and fq is not None and pt==fq:
                    need[24]-=1
                if min(need)<0:continue
                mass+=self.prefix.get((tuple(need),lp,lq,pt),0)
        return mass

    def choices(self,i):
        assert self.t<=i<=self.n
        return tuple((p,q) for p in ABC for q in ABC) if self.t<i<=self.m else tuple((None,q) for q in ((0,) if i==1 else ABC))

    def step(self,i,vis,fp,fq,lp,lq,p,q):
        v=inc(vis,p,q,lp,lq)
        if any(v[j]>self.target[j] for j in range(D)):
            return None
        return (i+1,v,p if fp is None and p is not None else fp,
                q if fq is None else fq,p if p is not None else lp,q)

    def _rec(self,i,vis,fp,fq,lp,lq):
        self.visited+=1
        if i>self.n:
            mass=self.terminal_mass(vis,fp,fq)
            return int(mass>0),mass
        support=mass=0
        for p,q in self.choices(i):
            nxt=self.step(i,vis,fp,fq,lp,lq,p,q)
            if nxt is None:continue
            a,b=self._f(*nxt)
            support+=a;mass+=b
        return support,mass

    def summary(self):
        x=self._f(self.t,Z,None,None,None,None)
        return {'classes':x[0],'original_population':x[1],
                'hidden_transfer_states':len(self.prefix), 'suffix_dp_states':self.visited}

    def unrank(self,rank):
        assert 0<=rank<self.summary()['classes']
        state=(self.t,Z,None,None,None,None);word=[]
        while state[0]<=self.n:
            i,vis,fp,fq,lp,lq=state
            for p,q in self.choices(i):
                nxt=self.step(i,vis,fp,fq,lp,lq,p,q)
                num=self._f(*nxt)[0] if nxt is not None else 0
                if rank<num:
                    word.append((p,q) if p is not None else (q,));state=nxt;break
                rank-=num
            else:raise AssertionError('unrank support exhaustion')
        return tuple(word)

    def rank(self,word):
        assert len(word)==self.n-self.t+1
        state=(self.t,Z,None,None,None,None);rank=0
        for col in word:
            i,vis,fp,fq,lp,lq=state
            pair=col if len(col)==2 else (None,col[0])
            for p,q in self.choices(i):
                nxt=self.step(i,vis,fp,fq,lp,lq,p,q)
                num=self._f(*nxt)[0] if nxt is not None else 0
                if (p,q)==pair:
                    assert num>0
                    state=nxt;break
                rank+=num
            else:raise ValueError('invalid label')
        assert self.terminal_mass(state[1],state[2],state[3])>0
        return rank

    def mass_of(self,word):
        state=(self.t,Z,None,None,None,None)
        for col in word:
            pair=col if len(col)==2 else (None,col[0])
            nxt=self.step(*state,*pair)
            if nxt is None:return 0
            state=nxt
        return self.terminal_mass(state[1],state[2],state[3])


def histories(m,n):
    ps=[(0,)+z for z in product(ABC,repeat=m-1)]
    qs=[(0,)+z for z in product(ABC,repeat=n-1)]
    fibers=defaultdict(list)
    for p in ps:
        for q in qs:fibers[obs(p,q)].append((p,q))
    return fibers

def exhaustive_verification():
    out={'fibers_tested':0,'parameter_cases':0,'classes_checked':0,
         'history_pairs_future_checked':0,'max_fiber_population':0,
         'with_population_gt_one':0,'splitting_fibers':0,'all_assertions':'PASS'}
    exemplars=[]
    for m,n in ((2,3),(3,4),(3,5),(4,5),(4,6),(5,6)):
        fibers=histories(m,n)
        # Select all multi-history fibers for shorter lengths; bounded indexed
        # sample for larger. Unique histories still validate zero/one boundary.
        good=[(k,v) for k,v in fibers.items() if len(v)>1]
        singles=[(k,v) for k,v in fibers.items() if len(v)==1]
        chosen=(good[:35] if m>=4 else good[:100])+(singles[:5])
        for target,people in chosen:
            out['fibers_tested']+=1
            out['max_fiber_population']=max(out['max_fiber_population'],len(people))
            assert len({native_observer(*z) for z in people})==1
            for hq in range(n+1):
                trans=TailTransfer(m,n,hq,target)
                expect=defaultdict(int)
                for p,q in people:expect[tail_key(p,q,hq)]+=1
                calc=trans.summary()
                assert calc['classes']==len(expect),(m,n,hq,people,calc,len(expect))
                assert calc['original_population']==len(people)
                if len(expect)>1:out['splitting_fibers']+=1
                for rank,key in enumerate(sorted(expect)):
                    assert trans.unrank(rank)==key
                    assert trans.rank(key)==rank
                    assert trans.mass_of(key)==expect[key]
                    if expect[key]>1:out['with_population_gt_one']+=1
                    out['classes_checked']+=1
                out['parameter_cases']+=1
                # Full 12-direction probe trace: select exact pair comparisons,
                # including equal labels when available.
                if len(people)>=2 and hq in (0,1,n-m,n-m+1,n):
                    for x in range(min(len(people),5)):
                        for y in range(x+1,min(len(people),5)):
                            p1,q1=people[x];p2,q2=people[y]
                            same=tail_key(p1,q1,hq)==tail_key(p2,q2,hq)
                            obs1=[];obs2=[]
                            for j in range(hq+1):
                                a=q1[:n-j];b=q2[:n-j]
                                obs1.append(native_observer(p1,a));obs2.append(native_observer(p2,b))
                                for u in DIRS:
                                    obs1.append(native_observer(p1,a+(u,)))
                                    obs2.append(native_observer(p2,b+(u,)))
                            assert (obs1==obs2)==same
                            out['history_pairs_future_checked']+=1
                if len(exemplars)<5 and (len(expect)>=2 or any(v>1 for v in expect.values())):
                    exemplars.append({'m':m,'n':n,'hq':hq,'fiber_population':len(people),
                         'classes':len(expect),'class_masses':sorted(expect.values()),
                         'states':calc['suffix_dp_states']})
    out['examples']=exemplars
    return out

def large_exact_tests():
    cases=[]
    for kp,kq,hq in ((20,24,18),(30,40,27),(40,60,50)):
        p=(0,)+tuple(x for i in range(kp) for x in (2 if i%2==0 else 4,0))
        q=(0,)+tuple(x for i in range(kq) for x in (4 if i%3==0 else 2,0))
        transfer=TailTransfer(len(p),len(q),hq,obs(p,q))
        result=transfer.summary()
        assert result['classes']>0 and result['original_population']>0
        samples=[]
        for rank in sorted({0,result['classes']//2,result['classes']-1}):
            word=transfer.unrank(rank)
            mass=transfer.mass_of(word)
            assert transfer.rank(word)==rank and mass>0
            samples.append({'rank':rank,'population':mass})
        cases.append({'m':len(p),'n':len(q),'Q_pop_budget':hq,
                      'classes':result['classes'],
                      'original_population':result['original_population'],
                      'hidden_states':result['hidden_transfer_states'],
                      'suffix_states':result['suffix_dp_states'],
                      'rank_population_checks':samples})
    return cases

if __name__=='__main__':
    out={'stage':'467B',
         'scope':'ternary A/B/C native signed-X6 original histories; Q-only future POP and APPEND>=1',
         'verification':exhaustive_verification(),
         'larger_exact_without_history_or_class_enumeration':large_exact_tests()}
    print(json.dumps(out,indent=2,ensure_ascii=False))
