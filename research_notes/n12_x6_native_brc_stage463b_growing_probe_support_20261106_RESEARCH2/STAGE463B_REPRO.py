"""Stage463-B: exact growing-window BRC support and rank/unrank (Python 3 stdlib)."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json

def positions(m,n,r):
    p=sorted({i for i in (m-3,m-2) if 1<=i<m-1})
    q={i for i in (m-2,m-1,n-3,n-2) if 1<=i<n-1}
    q.update(i for i in range(m,min(n-1,m+r)) if 1<=i<n-1)
    return tuple([('P',i) for i in p]+[('Q',i) for i in sorted(q)])

class Exact:
    def __init__(self,m,n,kp,kq,d,r):
        assert 2<=m<n and r>=0
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
            assert c>0 and a%c==0
            self.group[(sig,v)]=(c,a//c)
        self.classes=sum(x for x,y in self.group.values())
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
            if any(((sg>>self.si[x])&1)!=bit for x,bit in fixed if x[0]=='P' or x in self.si):continue
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
        if len(bits)!=len(self.coords) or self.prefix(tuple(bits))!=1:raise ValueError(bits)
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

if __name__=='__main__':
    rows=[]
    for m,n in [(2,3),(2,5),(3,5),(3,7),(4,6),(4,8),(5,8),(5,10)]:
        for r in (0,1,2,3,5,n):
            f,c=check(m,n,r);rows.append((m,n,r,f,c))
    examples=[]
    for m,n,kp,kq,d,r in [(64,80,15,17,1,2),(64,80,15,17,1,8),(64,80,15,17,1,16)]:
        x=Exact(m,n,kp,kq,d,r)
        for j in sorted(set((0,x.classes//2,x.classes-1))):
            assert x.rank(x.unrank(j))==j and x.population(x.unrank(j))>0
        examples.append((m,n,kp,kq,d,r,x.classes,str(x.population_total),len(x.coords),len(x.group)))
    print(json.dumps({'small_fibres':sum(x[3] for x in rows),'small_classes':sum(x[4] for x in rows),'large':examples,'PASS':True}))
