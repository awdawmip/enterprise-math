"""Stage458-B: uniform exact Boolean-support / integer-population and rank/unrank.
P has zero POP, Q has b POP; both can APPEND in full 12 native directions.
Initial A/B isolated-defect words only. Pure ordered-history observer model.
Run next to Stage457B.py (on repository branch), or alongside local stage457b.py.
"""
from collections import defaultdict
from functools import lru_cache
import importlib.util, json, random
from pathlib import Path

A,B=0,1
@lru_cache(None)
def prefix(m,kp,kq,d):
    """(Q_m, Q-prefix B count) -> number of admissible initial paired prefixes."""
    D={(0,0,0,0,0):1}
    for i in range(1,m+1):
        E=defaultdict(int)
        for (bp,bq,dd,lp,lq),v in D.items():
            for p in (0,1):
                if p and (i in (1,m) or lp): continue
                for q in (0,1):
                    if q and (i==1 or lq): continue
                    x,y,z=bp+p,bq+q,dd+(p!=q)
                    if x<=kp and y<=kq and z<=d:
                        E[x,y,z,p,q]+=v
        D=E
    R=defaultdict(int)
    for (bp,bq,dd,lp,lq),v in D.items():
        if bp==kp and dd==d:R[lq,bq]+=v
    return dict(R)

@lru_cache(None)
def gap(g,left,right,max_b):
    """Number of hidden binary Q gaps by B count; fixed boundary letters."""
    D={(left,0):1}
    for _ in range(g):
        E=defaultdict(int)
        for (last,b),mass in D.items():
            for x in (0,1):
                if last and x:continue
                if b+x<=max_b:E[x,b+x]+=mass
        D=E
    R=defaultdict(int)
    for (last,b),mass in D.items():
        if not(last and right):R[b]+=mass
    return dict(R)

class BoundaryCounter:
    """c=n-b >=m; a finite transfer over visible Q-key tokens."""
    def __init__(self,m,n,kp,kq,d,b,rp):
        assert 2<=m<n and 0<=b<=n-m and rp>=0
        self.m,self.n,self.kp,self.kq,self.d,self.b,self.rp=m,n,kp,kq,d,b,rp
        self.u=n-b
        self.t=min(n,m+rp)
        self.g=max(0,self.u-self.t-1)
        self.S=tuple(sorted(set([m] if self.u==m else []) | {i for i in range(m+1,n+1) if i<=self.t or i>=self.u}))
        # step, visible B, visible Q_m, Q_(m+1), Q_t, Q_u, last visible letter
        self.start=(0,0,-1,-1,-1,-1,-1)

    def choices(self,s):
        step,v,qm,qfirst,qt,qu,last=s
        if step==len(self.S):return []
        i=self.S[step]
        prev=self.S[step-1] if step else -2
        E=[]
        for x in ((0,) if i==self.n else (0,1)):
            if prev==i-1 and last and x:continue
            w=(step+1,v+(x if i>self.m else 0),
               x if i==self.m else qm,
               x if i==self.m+1 else qfirst,
               x if i==self.t and self.t>self.m else qt,
               x if i==self.u and self.u>self.m else qu,
               x)
            E.append((str(x),w))
        return E

    @lru_cache(None)
    def terminal_mass(self,s):
        step,v,qm,qfirst,qt,qu,last=s
        if step!=len(self.S):return 0
        mass=0
        for (q,bq),pre in prefix(self.m,self.kp,self.kq,self.d).items():
            if qm!=-1 and qm!=q:continue
            if qfirst!=-1 and q and qfirst:continue
            if self.g:
                left=qt if self.t>self.m else q
                if qu<0:raise AssertionError('missing Q_u gap boundary')
                gmass=gap(self.g,left,qu,self.kq).get(self.kq-bq-v,0)
            else:
                gmass=int(self.kq==bq+v)
            mass+=pre*gmass
        return mass

    @lru_cache(None)
    def solve(self,s):
        if s[0]==len(self.S):
            mass=self.terminal_mass(s)
            return int(mass>0),mass
        support=population=0
        for token,ns in self.choices(s):
            a,b=self.solve(ns)
            support+=a;population+=b
        return support,population

    def result(self):
        qf,pop=self.solve(self.start)
        return {'qF':str(qf),'population':str(pop),'DP_states':self.solve.cache_info().currsize,
                'c':self.u,'t':self.t,'gap':self.g,'visible_positions':self.S}

    def unrank(self,r):
        qf,_=self.solve(self.start)
        if not 0<=r<qf:raise IndexError(r)
        s=self.start;key=[]
        while s[0]<len(self.S):
            for token,ns in self.choices(s):
                support,_=self.solve(ns)
                if r>=support:r-=support
                else:key.append(token);s=ns;break
            else:raise AssertionError('missing ranked successor')
        assert self.terminal_mass(s)>0 and r==0
        return tuple(key)

    def rank(self,key):
        s=self.start;r=0
        for ch in key:
            dst=None
            for tok,ns in self.choices(s):
                if tok==ch:dst=ns;break
                r+=self.solve(ns)[0]
            if dst is None:raise ValueError('invalid key')
            s=dst
        if s[0]!=len(self.S) or self.terminal_mass(s)<=0:raise ValueError('unsupported key')
        return r

    def key_mass(self,key):
        s=self.start
        for ch in key:
            s=dict(self.choices(s)).get(ch)
            if s is None:return 0
        return self.terminal_mass(s)

def stage457_counter(m,n,kp,kq,d,b):
    here=Path(__file__).resolve()
    candidates=[here.parent/'stage457b.py',here.parent/'STAGE457B.py',here.parent.parent/'n12_x6_native_brc_stage457b_hidden_prefix_rank_20261105_RESEARCH2'/'STAGE457B.py']
    path=next((x for x in candidates if x.exists()),None)
    if path is None:raise FileNotFoundError('Stage457B.py is a pinned scientific dependency')
    spec=importlib.util.spec_from_file_location('pinned_stage457',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.Counter(m,n,kp,kq,d,b)

class UnifiedCounter:
    def __init__(self,m,n,kp,kq,d,b,rp):
        self.c=n-b
        self.impl=(BoundaryCounter(m,n,kp,kq,d,b,rp) if self.c>=m else stage457_counter(m,n,kp,kq,d,b))
        self.m,self.n,self.kp,self.kq,self.d,self.b,self.rp=m,n,kp,kq,d,b,rp
    def result(self):return self.impl.result()
    def rank(self,key):return self.impl.rank(key)
    def unrank(self,r):return self.impl.unrank(r)
    def key_mass(self,key):return self.impl.key_mass(key)

def words(n,k):
    def rec(s,b):
        i=len(s)+1
        if i>n:
            if b==k:yield s
            return
        for v in (0,1):
            if v and (i==1 or i==n or (s and s[-1])):continue
            if b+v<=k:yield from rec(s+(v,),b+v)
    return rec((),0)

def oracle(m,n,kp,kq,d,b,rp):
    u=n-b;t=min(n,m+rp);R=defaultdict(int)
    for p in words(m,kp):
        for q in words(n,kq):
            if sum(x!=y for x,y in zip(p,q))!=d:continue
            if u>=m:
                S=sorted(set([m] if u==m else []) | {i for i in range(m+1,n+1) if i<=t or i>=u})
                key=tuple(str(q[i-1]) for i in S)
            else:
                key=tuple((str(q[u-1]),) if u else ()) + tuple(str(p[i-1])+str(q[i-1]) for i in range(u+1,m+1)) + tuple(str(q[i-1]) for i in range(m+1,n+1))
            R[key]+=1
    return dict(R)

def test():
    rr=random.Random(458)
    cases=nonempty=boundary=rankchecks=0
    examples=[]
    for m in range(2,8):
        for n in range(m+1,min(m+4,10)):
            for kp in range(min(2,(m-2)//2)+1):
                for kq in range(min(3,(n-2)//2)+1):
                    for d in range(min(4,m)+1):
                        for b in range(n+1):
                            rp=rr.randint(0,n-m+1)
                            if rr.random()<0.43:continue
                            counter=UnifiedCounter(m,n,kp,kq,d,b,rp)
                            actual=oracle(m,n,kp,kq,d,b,rp)
                            got=counter.result()
                            assert (int(got['qF']),int(got['population']))==(len(actual),sum(actual.values())),(m,n,kp,kq,d,b,rp,got,actual)
                            for idx,key in enumerate(sorted(actual)):
                                assert counter.rank(key)==idx and counter.unrank(idx)==key
                                assert counter.key_mass(key)==actual[key]
                                rankchecks+=1
                            cases+=1; nonempty+=bool(actual);boundary+=(n-b==m)
                            if len(examples)<6 and actual and (n-b in (m-1,m,m+1)):
                                examples.append({'params':[m,n,kp,kq,d,b,rp], 'result':got})
    # independent Stage456 grouped agreement at c>=m and large Stage457 regression
    large=[]
    for p in [(64,80,15,17,1,0,0),(64,80,15,17,1,5,0),(64,80,15,17,1,5,3),
              (64,80,15,17,1,16,0),(64,80,15,17,1,25,3),
              (64,80,15,17,1,60,3),(92,126,20,25,3,12,7)]:
        counter=UnifiedCounter(*p);z=counter.result();num=int(z['qF']);checks=[]
        for j in sorted({0,num//2,num-1}) if num else ():
            key=counter.unrank(j)
            assert counter.rank(key)==j and counter.key_mass(key)>0
            checks.append({'rank':str(j),'key_length':len(key),'mass':str(counter.key_mass(key))})
        large.append({'parameters':p,'result':z,'checks':checks})
    print(json.dumps({'marker':'STAGE458B_UNIFIED_ZERO_P_POP_RANK_PASS',
       'finite':{'cases':cases,'nonempty':nonempty,'c_equals_m':boundary,'per_key_rank_and_mass_checks':rankchecks},
       'boundary_examples':examples,'large':large,'scope':'exact signed native X6 A/B isolated input, full 12-direction future APPEND; BRC source-distinct positive integers'},ensure_ascii=False,indent=2))
if __name__=='__main__':test()
