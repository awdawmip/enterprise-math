#!/usr/bin/env python3
"""Stage464-B: native-X6 two-source three-POP growing-probe BRC transfer."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json
DIRECTIONS=tuple(range(12))

def positions(m,n,r):
    assert 2<=m<n and r>=0
    p=sorted(i for i in (m-4,m-3,m-2) if 1<=i<m-1)
    q={i for i in (m-3,m-2,m-1,n-4,n-3,n-2) if 1<=i<n-1}
    q.update(i for i in range(m,min(n-1,m+r)) if 1<=i<n-1)
    return tuple([('P',i) for i in p]+[('Q',i) for i in sorted(q)])

class Exact:
    def __init__(self,m,n,kp,kq,d,r):
        assert 2<=m<n and r>=0 and min(kp,kq,d)>=0
        self.m,self.n,self.kp,self.kq,self.d,self.r=m,n,kp,kq,d,r
        self.coords=positions(m,n,r)
        self.W=tuple(i for s,i in self.coords if s=='Q')
        bound={i for j,i in enumerate(self.W) if j==0 or j==len(self.W)-1 or i!=self.W[j-1]+1 or self.W[j+1]!=i+1}
        bound.update(i for i in self.W if i<m)
        self.S=tuple(x for x in self.coords if x[0]=='P' or x[1] in bound)
        self.si={x:j for j,x in enumerate(self.S)}
        self.mass=self.transfer()
        self.group={}
        for (sig,v),a in self.mass.items():
            c=self.visible(sig,v,())
            assert c>0 and a%c==0,(sig,v,a,c)
            self.group[(sig,v)]=(c,a//c)
        self.classes=sum(c for c,_ in self.group.values())
        self.population_total=sum(self.mass.values())
    def transfer(self):
        m,n,kp,kq,d=self.m,self.n,self.kp,self.kq,self.d
        W=set(self.W);cur={(0,0,0,0,0,0,0):1}
        for i in range(n):
            nxt=defaultdict(int)
            pp=(None,) if i>=m else ((0,) if i in (0,m-1) else (0,1))
            qq=(0,) if i in (0,n-1) else (0,1)
            ip=self.si.get(('P',i));iq=self.si.get(('Q',i))
            for (a,b,e,lp,lq,sg,v),cnt in cur.items():
                for p in pp:
                    if p is not None and (a+p>kp or p==lp==1):continue
                    for q in qq:
                        if b+q>kq or q==lq==1:continue
                        ee=e+(p!=q if p is not None else 0)
                        if ee>d:continue
                        ns=sg|((p==1)<<ip if ip is not None else 0)|((q==1)<<iq if iq is not None else 0)
                        nxt[(a+(p or 0),b+q,ee,lp if p is None else p,q,ns,v+(q if i in W else 0))]+=cnt
            cur=nxt
        out=defaultdict(int)
        for (a,b,e,lp,lq,sg,v),cnt in cur.items():
            if (a,b,e)==(kp,kq,d):out[(sg,v)]+=cnt
        return dict(out)
    @lru_cache(None)
    def visible(self,sg,v,forced):
        fixed=dict(forced)
        for (s,i),j in self.si.items():
            if s!='Q':continue
            bit=(sg>>j)&1
            if i in fixed and fixed[i]!=bit:return 0
            fixed[i]=bit
        dp={(0,0):1};last=-9
        for i in self.W:
            nxt=defaultdict(int)
            for (b,prev),c in dp.items():
                for x in ((fixed[i],) if i in fixed else (0,1)):
                    if (i==last+1 and x==prev==1) or b+x>v:continue
                    nxt[(b+x,x)]+=c
            dp=nxt;last=i
        return sum(c for (b,_),c in dp.items() if b==v)
    @lru_cache(None)
    def prefix(self,bits):
        fixed=list(zip(self.coords,bits));answer=0
        for (sg,v),(cnt,pop) in self.group.items():
            if any(((sg>>self.si[x])&1)!=bit for x,bit in fixed if x in self.si):continue
            forced=tuple((i,bit) for (s,i),bit in fixed if s=='Q')
            answer+=self.visible(sg,v,forced)
        return answer
    def population(self,bits):
        if len(bits)!=len(self.coords):return 0
        ass=dict(zip(self.coords,bits))
        sg=sum(ass[x]<<j for x,j in self.si.items())
        v=sum(ass[('Q',i)] for i in self.W)
        return self.group.get((sg,v),(0,0))[1]
    def unrank(self,i):
        if not 0<=i<self.classes:raise ValueError(i)
        bits=()
        for _ in self.coords:
            z=self.prefix(bits+(0,))
            if i<z:bits+=(0,)
            else:i-=z;bits+=(1,)
        assert i==0
        return bits
    def rank(self,bits):
        bits=tuple(bits)
        if len(bits)!=len(self.coords) or self.prefix(bits)!=1:raise ValueError(bits)
        i=0;t=()
        for b in bits:
            if b:i+=self.prefix(t+(0,))
            t+=(b,)
        return i

def original(n):
    for k in range((n-1)//2+1):
        for comb in combinations(range(1,n-1),k):
            if any(j==i+1 for i,j in zip(comb,comb[1:])):continue
            w=[0]*n
            for i in comb:w[i]=1
            yield tuple(w)

def check(m,n,r):
    fibres=defaultdict(lambda:defaultdict(int))
    coords=positions(m,n,r)
    for p in original(m):
        for q in original(n):
            f=(sum(p),sum(q),sum(x!=y for x,y in zip(p,q)))
            key=tuple((p if s=='P' else q)[i] for s,i in coords)
            fibres[f][key]+=1
    num=0
    for f,keys in fibres.items():
        z=Exact(m,n,*f,r)
        assert z.classes==len(keys) and z.population_total==sum(keys.values())
        for i,key in enumerate(sorted(keys)):
            assert z.population(key)==keys[key] and z.rank(key)==i and z.unrank(i)==key
        num+=len(keys)
    return len(fibres),num

def observation(p,q):
    def stats(w):
        end=[0]*6;adj=defaultdict(int)
        for s in w:end[s//2]+=(1 if s%2==0 else -1)
        for x,y in zip(w,w[1:]):adj[(x,y)]+=1
        return len(w),tuple(end),tuple(sorted(adj.items()))
    return stats(p),stats(q),sum(x==y for x,y in zip(p,q))

class Oracle:
    def __init__(self):self.memo={};self.intern={}
    def future(self,p,q,bp,bq,ap,aq):
        state=(p,q,bp,bq,ap,aq)
        if state in self.memo:return self.memo[state]
        edges=[]
        if bp and p:edges.append(('POP_P',self.future(p[:-1],q,bp-1,bq,ap,aq)))
        if bq and q:edges.append(('POP_Q',self.future(p,q[:-1],bp,bq-1,ap,aq)))
        if ap:
            for u in DIRECTIONS:edges.append((('APPEND_P',u),self.future(p+(u,),q,bp,bq,ap-1,aq)))
        if aq:
            for u in DIRECTIONS:edges.append((('APPEND_Q',u),self.future(p,q+(u,),bp,bq,ap,aq-1)))
        signature=(observation(p,q),tuple(edges))
        value=self.intern.get(signature)
        if value is None:value=len(self.intern)+1;self.intern[signature]=value
        self.memo[state]=value
        return value

def future_check(m,n,r,s):
    groups=defaultdict(list);coords=positions(m,n,r);oracle=Oracle()
    for p in original(m):
        for q in original(n):
            f=(sum(p),sum(q),sum(x!=y for x,y in zip(p,q)))
            key=tuple((p if src=='P' else q)[i] for src,i in coords)
            sig=oracle.future(p,q,3,3,r,s)
            groups[f].append((key,sig))
    pairs=0
    for group in groups.values():
        for i,(k1,t1) in enumerate(group):
            for k2,t2 in group[:i]:
                assert (k1==k2)==(t1==t2),(m,n,r,s,k1,k2,t1,t2)
                pairs+=1
    return dict(m=m,n=n,r=r,s=s,fibres=len(groups),pairs=pairs,states=len(oracle.memo),intern=len(oracle.intern))

def main():
    checks=[]
    for m,n in [(2,3),(2,5),(3,4),(3,5),(3,7),(4,5),(4,7),(5,8),(5,10)]:
        for r in (0,1,2,3,5,n):
            f,c=check(m,n,r);checks.append((m,n,r,f,c))
    examples=[]
    for params in [(25,38,5,7,1,8),(64,80,15,17,1,2),(64,80,15,17,1,8),(64,80,15,17,1,16)]:
        z=Exact(*params)
        for j in sorted(set((0,z.classes//2,z.classes-1))):
            assert z.rank(z.unrank(j))==j and z.population(z.unrank(j))>0
        examples.append(dict(parameters=params,classes=z.classes,population=str(z.population_total),coordinates=len(z.coords),signature_fields=len(z.S),signature_groups=len(z.group),sample_population=str(z.population(z.unrank(z.classes//2)))))
    futures=[]
    for m,n,r,s in [(2,3,0,0),(3,4,0,0),(3,5,1,0),(2,4,1,1),(4,6,0,0),(4,6,1,0),(4,6,0,1),(4,6,1,1),(5,7,1,0),(5,7,1,1),(5,7,2,0)]:
        futures.append(future_check(m,n,r,s))
    print(json.dumps({'model':'two source native X6 A/B isolated internal defects, each source POP<=3, full 12 signed direction APPEND','small_parameter_cases':len(checks),'nonempty_fibres':sum(x[3] for x in checks),'checked_classes':sum(x[4] for x in checks),'examples':examples,'full_future_checks':futures,'PASS':True},indent=2))

if __name__=='__main__':main()
