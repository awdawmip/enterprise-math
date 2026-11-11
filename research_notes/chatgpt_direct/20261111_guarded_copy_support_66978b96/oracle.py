"""Adaptive original-word program as a finite acyclic graph.
World and per-origin implementations share only program/price semantics.
A policy receives delivered observations, never a preparation from the test harness.
"""
from functools import cache
from itertools import product

def change(s,i,k):return s[:i]+(k,)+s[i+1:]
def vals(v):
    while v:
        k=v&(-v);yield k.bit_length()-1;v-=k

class Program:
    """Terminal pc=-1; all actual transitions point backward in storage order."""
    def __init__(self,r):
        self.r=r;self.M=r+1;self.b=r.bit_length();self.q=(3*self.M).bit_length()
        self.limit=3*self.M;self.all=(1<<(self.limit+1))-1
        self.ones=tuple(sum(1<<x for x in range(self.limit+1) if x>>b&1) for b in range(self.q))
        a=8*self.b+2*self.q+38;self.fixed=(a,a+3,a);self.nodes=[]
    def add(self,op,default=-1,overrides=()):
        op=tuple(op);overrides=tuple((int(x),y) for x,y in overrides)
        assert -1<=default<len(self.nodes) and all(-1<=u<len(self.nodes) for _,u in overrides)
        assert len({x for x,_ in overrides})==len(overrides)
        z=op[0]
        assert ((z=='round' and len(op)==3 and 0<=op[1]<3 and 0<=op[2]<self.r) or
            (z=='copy' and len(op)==3 and all(0<=v<self.r for v in op[1:])) or
            (z=='drop' and len(op)==2 and 0<=op[1]<self.r) or
            (z=='bit' and len(op)==3 and 0<=op[1]<self.r and 0<=op[2]<self.q))
        self.nodes.append((op,default,overrides));return len(self.nodes)-1
    def dest(self,i,z):
        e,other,m=self.nodes[i]
        return next((v for k,v in m if k==int(z)),other)
    def keys(self,t):return range(t*self.M+1,(t+1)*self.M+1)
    def create_price(self,t,k):return self.fixed[t]+2*k.bit_count()+4*(1-((k>>(self.b-1))&1))
    def cp(self,k):return 9*self.q+1 if not k else 9*self.q+2+k.bit_count()+4*(1-((k>>(self.q-1))&1))
    def physical(self,e,x,key=None):
        """Offline/oracle literal transition used only by explicit-world model and replay."""
        kind=e[0];a=e[1]
        if kind=='round':
            assert key in self.keys(a) and key not in x
            return key,change(x,e[2],key),self.create_price(a,key)
        if kind=='bit':return (x[a]>>e[2])&1,x,8
        if kind=='drop':return int(bool(x[a])),change(x,a,0),self.q+9
        if a==e[2]:return int(bool(x[a])),x,8
        k=x[e[2]];return k,change(x,a,k),self.cp(k)

class Domains:
    def __init__(self,P,entry=None,actual=None,forbid_preprobes=()):
        self.P=P;self.x=None if actual is None else tuple(actual);self.stop=frozenset(forbid_preprobes)
        d=(P.all,)*P.r if entry is None else tuple(entry)
        assert len(d)==P.r and all(0<m<=P.all for m in d)
        if self.x is not None:assert all(m>>k&1 for m,k in zip(d,self.x))
        self.start=self.norm(len(P.nodes)-1,tuple(range(P.r)),d);self.dp=cache(self.solve)
    def norm(self,pc,s,D):
        s=tuple(-D[a].bit_length() if a>=0 and D[a].bit_count()==1 else a for a in s)
        return pc,s,tuple(D[i] if i in s else 0 for i in range(len(D)))
    @staticmethod
    def pos(a,d):return 1<<(-1-a) if a<0 else d[a]
    def partition(self,a,D,f):
        groups={}
        for k in vals(self.pos(a,D)):
            z=f(k);groups[z]=groups.get(z,0)|(1<<k)
        if self.x is None:return groups.items()
        z=f(self.x[a] if a>=0 else -1-a);return [(z,groups[z])]
    def solve(self,pc,s,D):
        if pc<0:return 0,('end',)
        p=self.P;e=p.nodes[pc][0];kind=e[0];a=e[1];choices=[]
        def v(i,slots,dom):return self.dp(*self.norm(i,slots,dom))[0]
        if kind=='round':
            for k in p.keys(a):
                if all(not ((self.pos(o,D)>>k)&1) for o in s):
                    choices.append((p.create_price(a,k)+v(p.dest(pc,k),change(s,e[2],-1-k),D),('round',k)))
        else:
            src=e[2] if kind=='copy' else a;o=s[src]
            if kind=='bit':
                assert src==a;get=lambda k:(k>>e[2])&1;pay=lambda z:8;ns=s
            elif kind=='drop':get=lambda k:int(bool(k));pay=lambda z:p.q+9;ns=change(s,a,-1)
            elif src==a:get=lambda k:int(bool(k));pay=lambda z:8;ns=s
            else:get=lambda k:k;pay=p.cp;ns=change(s,a,o)
            options=[pay(z)+v(p.dest(pc,z),ns,change(D,o,m) if o>=0 else D) for z,m in self.partition(o,D,get)]
            choices.append((max(options),('operation',)))
        if pc not in self.stop:
            seen=set()
            for i,o in enumerate(s):
                if o<0 or o in seen:continue
                seen.add(o)
                for b,yes in enumerate(p.ones):
                    if not (D[o]&yes and D[o]&~yes):continue
                    options=[v(pc,s,change(D,o,m)) for z,m in self.partition(o,D,lambda k:(k>>b)&1)]
                    choices.append((8+max(options),('read',i,b)))
        assert choices
        return min(choices,key=lambda z:(z[0],z[1][0]=='read',z[1]))
    def value(self):return self.dp(*self.start)[0]
    def replay(self,x):
        """Physical simulator separate; controller advances only by event reply."""
        x=tuple(x);state=self.start;c=0;tr=[]
        while state[0]>=0:
            pc=state[0];a=self.dp(*state)[1];e=self.P.nodes[pc][0]
            obs,nx,price=self.P.physical(('bit',*a[1:]) if a[0]=='read' else e,x,a[1] if a[0]=='round' else None)
            state=self.advance(state,a,obs);tr.append((pc,a,obs,price));x=nx;c+=price
        return c,tr,x
    def advance(self,state,act,obs):
        pc,s,D=state;p=self.P;assert self.dp(*state)[1]==act
        e=p.nodes[pc][0];kind=e[0]
        if act[0]=='read':src=act[1];m=p.ones[act[2]] if obs else (p.all^p.ones[act[2]]);dst=pc;S=s
        elif kind=='round':
            assert obs==act[1];return self.norm(p.dest(pc,obs),change(s,e[2],-1-obs),D)
        else:
            src=e[2] if kind=='copy' else e[1];dst=p.dest(pc,obs);S=s
            if kind=='bit':m=p.ones[e[2]] if obs else (p.all^p.ones[e[2]])
            elif kind=='drop' or e[1]==src:
                m=(p.all^1) if obs else 1
                if kind=='drop':S=change(s,e[1],-1)
            else:m=1<<obs;S=change(s,e[1],s[src])
        o=s[src];allowed=m&self.pos(o,D);assert allowed
        return self.norm(dst,S,change(D,o,allowed) if o>=0 else D)

class Worlds:
    def __init__(self,p,entry=None):
        self.p=p;ds=entry or (p.all,)*p.r
        self.start=tuple(product(*(tuple(vals(d)) for d in ds)));self.dp=cache(self.solve)
    def value(self,x=None):return self.dp(len(self.p.nodes)-1,self.start,None if x is None else tuple(x))
    def solve(self,pc,S,x):
        if pc<0:return 0
        p=self.p;e=p.nodes[pc][0];cand=[]
        keys=p.keys(e[1]) if e[0]=='round' else [None]
        for key in keys:
            if key is not None and any(key in world for world in S):continue
            split={}
            for world in S:
                obs,end,fee=p.physical(e,world,key);split.setdefault((obs,fee),set()).add(end)
                if world==x:actual=(obs,fee,end)
            if x is None:cand.append(max(f+self.dp(p.dest(pc,z),tuple(sorted(X)),None) for (z,f),X in split.items()))
            else:
                z,f,end=actual;cand.append(f+self.dp(p.dest(pc,z),tuple(sorted(split[z,f])),end))
        for i in range(p.r):
            for b in range(p.q):
                bits=tuple(tuple(v for v in S if (v[i]>>b)&1==z) for z in (0,1))
                if not all(bits):continue
                cand.append(8+(max(self.dp(pc,B,None) for B in bits) if x is None else self.dp(pc,bits[(x[i]>>b)&1],x)))
        return min(cand)

def fork_m(m):
    """drop after first B. Both branches contain a second B then m addressed copies."""
    p=Program(2);z=n=-1
    for _ in range(m):
        z=p.add(('copy',1,0),z);n=p.add(('copy',0,1),n)
    z=p.add(('round',1,1),z);n=p.add(('round',1,1),n)
    d=p.add(('drop',1),z,[(1,n)]);p.add(('round',1,0),d)
    return p
