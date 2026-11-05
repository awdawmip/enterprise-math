"""Stage457-B: exact BRC Boolean support, integer source mass and rank/unrank.
Original native X6 subfamily: A=+E1, B=-E1, source-distinct ordered words;
A endpoints and isolated B. Observer (V,J,K) is preserved by indexed repair.
Regime P POP=0, Q POP budget b>n-m, c=n-b<m (0<=b<=n).
Both future APPEND streams may use all 12 primitive signed directions.
No classical dynamics, phases, amplitudes or physical residual attribution.
"""
from collections import defaultdict
from functools import lru_cache
import json, random, sys

@lru_cache(None)
def hidden_prefix(c, qc, firstp, kp, kq, d):
    """T: (b_P,b_Q,delta) -> number of hidden ordered paired prefixes.
    Q_c is indexed-visible and fixed; P_(c+1) is indexed-visible.
    Q boundary edge (Q_c,Q_(c+1)) is checked by visible automaton.
    P boundary edge (P_c,P_(c+1)) is checked here.
    """
    if c == 0:
        return {(0,0,0):1}
    D = {(0,0,0,0,0):1}
    for i in range(1,c+1):
        E = defaultdict(int)
        for (bp,bq,dd,lp,lq),count in D.items():
            for p in (0,1):
                if (i == 1 and p) or (i>1 and lp and p): continue
                if i==c and firstp and p:continue
                for q in (0,1):
                    if (i==1 and q) or (i>1 and lq and q):continue
                    if i==c and q!=qc:continue
                    x,y,z=bp+p,bq+q,dd+(p!=q)
                    if x<=kp and y<=kq and z<=d:E[x,y,z,p,q]+=count
        D=E
    R=defaultdict(int)
    for (bp,bq,dd,p,q),count in D.items():R[bp,bq,dd]+=count
    return dict(R)

class Counter:
    def __init__(self,m,n,kp,kq,d,b):
        assert 2<=m<n and 0<=b<=n and b>n-m
        self.m,self.n,self.kp,self.kq,self.d,self.b=m,n,kp,kq,d,b
        self.c=n-b
        self.memo_calls=0
        self.memo_hits=0
        self.start=(self.c if self.c>0 else 1, 0,0,0,-1,-1,-1,-1)
        self.options_cache={}

    def choices(self,s):
        i,bp,bq,dd,lp,lq,fp,qc=s
        if i>self.n:return []
        choices=[]
        if self.c>0 and i==self.c:
            for q in (0,1):
                if i==1 and q:continue
                choices.append((str(q),(i+1,bp,bq,dd,lp,q,fp,q)))
        elif i<=self.m:
            for p in (0,1):
                if (i==1 or i==self.m) and p:continue
                if lp==1 and p:continue
                for q in (0,1):
                    if i==1 and q:continue
                    if lq==1 and q:continue
                    x,y,z=bp+p,bq+q,dd+(p!=q)
                    if x>self.kp or y>self.kq or z>self.d:continue
                    choices.append((str(p)+str(q),(i+1,x,y,z,p,q,p if fp<0 else fp,qc)))
        else:
            for q in (0,1):
                if i==self.n and q:continue
                if lq==1 and q:continue
                y=bq+q
                if y<=self.kq:
                    choices.append((str(q),(i+1,bp,y,dd,lp,q,fp,qc)))
        return choices

    def terminal_mass(self,s):
        i,bp,bq,dd,lp,lq,fp,qc=s
        if i!=self.n+1:return 0
        remain=(self.kp-bp,self.kq-bq,self.d-dd)
        if min(remain)<0:return 0
        if self.c==0:
            return int(remain==(0,0,0))
        return hidden_prefix(self.c,qc,fp,self.kp,self.kq,self.d).get(remain,0)

    @lru_cache(None)
    def solve(self,s):
        """Return (# supported indexed keys, total source-pair mass)."""
        self.memo_calls+=1
        if s[0]>self.n:
            mass=self.terminal_mass(s)
            return (int(mass>0),mass)
        qf=0;population=0
        for token,ns in self.choices(s):
            q,raw=self.solve(ns)
            qf+=q;population+=raw
        return (qf,population)

    def result(self):
        qf,pop=self.solve(self.start)
        return dict(qF=str(qf),population=str(pop),DP_states=self.solve.cache_info().currsize,
                    hidden_T_states=sum(len(hidden_prefix(self.c,q,f,self.kp,self.kq,self.d)) for q in (0,1) for f in (0,1)),
                    c=self.c,visible_P=self.m-self.c,visible_Q=self.n-self.c)

    def unrank(self,r):
        qf,_=self.solve(self.start)
        if not 0<=r<qf:raise IndexError(r)
        s=self.start;tokens=[]
        while s[0]<=self.n:
            for token,ns in self.choices(s):
                q,_=self.solve(ns)
                if r>=q:r-=q
                else:
                    tokens.append(token);s=ns;break
            else:raise AssertionError('no supported successor')
        assert self.terminal_mass(s)>0 and r==0
        return tuple(tokens)

    def rank(self,tokens):
        s=self.start;r=0
        for chosen in tokens:
            match=None
            for token,ns in self.choices(s):
                if token==chosen:
                    match=ns;break
                q,_=self.solve(ns)
                r+=q
            if match is None:raise ValueError('invalid token')
            s=match
        if s[0]!=self.n+1 or not self.terminal_mass(s):raise ValueError('unsupported repair key')
        return r

    def key_mass(self,tokens):
        s=self.start
        for tok in tokens:
            opts=dict(self.choices(s))
            if tok not in opts:return 0
            s=opts[tok]
        return self.terminal_mass(s)


def words(length,k):
    def go(prefix,ones):
        i=len(prefix)+1
        if i>length:
            if ones==k:yield prefix
            return
        for v in (0,1):
            if v and (i==1 or i==length or (prefix and prefix[-1])):continue
            if ones+v<=k:yield from go(prefix+(v,),ones+v)
    return go((),0)

def oracle(m,n,kp,kq,d,b):
    c=n-b
    classes=defaultdict(int)
    for p in words(m,kp):
        for q in words(n,kq):
            if sum(p[i]!=q[i] for i in range(m))!=d:continue
            parts=[]
            if c>0:parts.append(str(q[c-1]))
            for i in range(c if c>0 else 0,m):parts.append(str(p[i])+str(q[i]))
            for i in range(m,n):parts.append(str(q[i]))
            classes[tuple(parts)]+=1
    return dict(classes)

def test():
    rr=random.Random(457)
    cases=0;nonempty=0;mass_matches=0;rank_checks=0;zero_case=0;edge=[]
    # Exhaustive small parameter grid (b controls c=0 through c=m-1).
    for m in range(2,8):
        for n in range(m+1,min(10,m+4)):
            for b in range(n-m+1,n+1):
                for kp in range(min(3,(m-2)//2)+1):
                    for kq in range(min(3,(n-2)//2)+1):
                        for d in range(min(m,4)+1):
                            if rr.random()<0.46:continue
                            counter=Counter(m,n,kp,kq,d,b)
                            result=counter.result();oracle_mass=oracle(m,n,kp,kq,d,b)
                            observed=(int(result['qF']),int(result['population']))
                            actual=(len(oracle_mass),sum(oracle_mass.values()))
                            assert observed==actual,(m,n,kp,kq,d,b,observed,actual)
                            cases+=1
                            nonempty+=actual[1]>0
                            zero_case+=counter.c==0
                            if actual[0] and len(edge)<4 and counter.c in (0,1,m-1):
                                edge.append(dict(parameters=[m,n,kp,kq,d,b],result=result))
                            for idx,key in enumerate(sorted(oracle_mass)):
                                got=counter.unrank(idx)
                                assert got==key and counter.rank(got)==idx
                                assert counter.key_mass(got)==oracle_mass[key]
                                rank_checks+=1;mass_matches+=1
    larger=[]
    for x in [
       (64,80,15,17,1,25),
       (64,80,15,17,1,60),
       (92,126,20,25,3,64),
    ]:
        counter=Counter(*x)
        R=counter.result();nq=int(R['qF'])
        sample=[]
        if nq:
            for idx in sorted({0,nq//2,nq-1}):
                key=counter.unrank(idx)
                assert counter.rank(key)==idx and counter.key_mass(key)>0
                sample.append(dict(rank=str(idx),key='|'.join(key),mass=str(counter.key_mass(key))))
        larger.append(dict(parameters=x,result=R,rank_checks=sample))
    print(json.dumps({'marker':'STAGE457B_HIDDEN_PREFIX_SUPPORTED_RANK_PASS',
      'finite_oracle':dict(cases=cases,nonempty=nonempty,c_zero_cases=zero_case,per_key_masses_checked=mass_matches,
                           rank_unrank_checked=rank_checks),
      'edge_examples':edge,'large':larger,
      'semantics':'exact integer indexed source-distinct BRC population, no physical residual attribution',
      'complexity':'O((n-c)*(kP+1)*(kQ+1)*(d+1)) DP state bound up to constant boundary fields, with c hidden prefix transfer of same counter dimension; per-rank O(n) cached transitions'},indent=2))

if __name__=='__main__':test()
