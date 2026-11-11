"""Bellman planning for original create/bind/release, addressed copy, and drop.

Old source labels carry independent *full-key* domains. Physical slots may share
one source. Known constants are represented by -(K+1), initial origin i by i.
The opposite implementation for finite comparisons uses explicit complete worlds.
Only physical reader/copy/presence replies are exposed to the selected controller.
"""
from functools import cache
from itertools import product

def members(mask):
    while mask:
        bit=mask & -mask
        yield bit.bit_length()-1
        mask-=bit

def replace(seq,pos,value):
    return seq[:pos]+(value,)+seq[pos+1:]

class Model:
    def __init__(self,r,events):
        self.r=r;self.events=tuple(tuple(e) for e in events);self.M=r+1
        self.b=r.bit_length();self.q=(3*self.M).bit_length();self.limit=3*self.M
        self.domain=(1<<(self.limit+1))-1
        self.ones=tuple(sum(1<<k for k in range(self.limit+1) if k>>j&1) for j in range(self.q))
        # Proven from the fixed three-target library, independently checked against actual words.
        A=8*self.b+2*self.q+38
        self.fixed=(A,A+3,A)
        for e in self.events:
            if e[0]=='round': assert len(e)==3 and 0<=e[1]<3 and 0<=e[2]<r
            elif e[0]=='copy': assert len(e)==3 and 0<=e[1]<r and 0<=e[2]<r
            elif e[0]=='drop': assert len(e)==2 and 0<=e[1]<r
            else: raise ValueError(e)
    def keys(self,t):
        return range(1+t*self.M,1+(t+1)*self.M)
    def weight(self,k):
        return 2*k.bit_count()+4*(1-((k>>(self.b-1))&1))
    def copy_charge(self,k):
        return 9*self.q+1 if k==0 else 9*self.q+2+k.bit_count()+4*(1-((k>>(self.q-1))&1))

class DomainBellman(Model):
    """actual=None gives the uniform adversarial value. actual=table gives a
    pointwise value over safe policies, never free admissibility of a key.
    Disabling copy bits is only supported for pointwise cost or pure read/weight:
    hidden unequal-path charges cannot be split and made visible to a planner."""
    def __init__(self,r,events,actual=None,*,charge_business=True,visible_copy=True,early_probes=True):
        super().__init__(r,events)
        self.actual=None if actual is None else tuple(actual)
        if self.actual is not None:
            assert len(self.actual)==r and all(0<=x<=self.limit for x in self.actual)
        if self.actual is None and not visible_copy and charge_business: raise ValueError('unequal hidden prefix charges')
        self.charge_business=charge_business;self.visible_copy=visible_copy;self.early_probes=early_probes
        self.start=(0,tuple(range(r)),(self.domain,)*r)
        self.lookup=cache(self._solve)
    def normalize(self,t,slots,doms):
        slots=tuple((-doms[a].bit_length() if a>=0 and doms[a].bit_count()==1 else a) for a in slots)
        return t,slots,tuple(d if i in slots else 0 for i,d in enumerate(doms))
    def possible(self,a,doms):
        return doms[a] if a>=0 else 1<<(-1-a)
    def actual_value(self,a):
        return self.actual[a] if a>=0 else -1-a
    def outcomes(self,a,doms,out):
        m=self.possible(a,doms);groups={}
        for k in members(m):groups[out(k)]=groups.get(out(k),0)|(1<<k)
        if self.actual is None:return groups.items()
        v=out(self.actual_value(a));return ((v,groups[v]),)
    def _solve(self,t,slots,doms):
        if t==len(self.events):return 0,('end',)
        e=self.events[t]; fixed=self.charge_business; candidates=[]
        def val(u,s,d):return self.lookup(*self.normalize(u,s,d))[0]
        if e[0]=='round':
            _,target,d=e
            blocked=0
            for a in slots:blocked |= self.possible(a,doms)
            for k in self.keys(target):
                if not (blocked>>k)&1:
                    c=self.weight(k)+(self.fixed[target] if fixed else 0)
                    candidates.append((c+val(t+1,replace(slots,d,-1-k),doms),('round',k)))
        else:
            if e[0]=='drop': d=e[1];src=d;kind='drop'
            else:_,d,src=e;kind='self' if d==src else 'copy'
            a=slots[src];full=kind=='copy' and self.visible_copy
            out=(lambda k:k) if full else bool
            dstval=-1 if kind=='drop' else a
            branches=[]
            for z,m in self.outcomes(a,doms,out):
                newdom=replace(doms,a,m) if a>=0 else doms
                cost=0
                if fixed:
                    if kind=='copy':cost=self.copy_charge(z if full else self.actual_value(a))
                    elif kind=='drop':cost=self.q+9
                    else:cost=8
                branches.append(cost+val(t+1,replace(slots,d,dstval),newdom))
            candidates.append((max(branches),('operation',)))
        if e[0]=='round' or self.early_probes:
            seen=set()
            for i,a in enumerate(slots):
                if a<0 or a in seen:continue
                seen.add(a);m=doms[a]
                for b,ones in enumerate(self.ones):
                    if not (m&ones) or not (m&~ones):continue
                    vals=[]
                    for answer,g in self.outcomes(a,doms,lambda k:(k>>b)&1):
                        vals.append(val(t,slots,replace(doms,a,g)))
                    candidates.append((8+max(vals),('read',i,b)))
        assert candidates
        # Prefer the mandatory operation on ties, then the lower full key or lowest probe.
        return min(candidates,key=lambda ch:(ch[0],ch[1][0]=='read',ch[1]))
    def value(self):return self.lookup(*self.start)[0]
    def action(self,state):
        """Public uniform strategy: consult only current observed information."""
        return self.lookup(*state)[1]
    def advance(self,state,act,result):
        """Consume a real action result, never an unseen request table.
        For a round result is the actually selected/written full key.
        For nonself copy it is the actually delivered full code (or only
        presence under the explicit hidden-bit comparison mode).
        For drop/self-copy and read it is the delivered Boolean."""
        t,slots,doms=state
        if t==len(self.events) or act!=self.action(state):raise ValueError('unexpected decision or position')
        if act[0]=='read':
            _,i,b=act;a=slots[i]
            if result not in (0,1) or a<0:raise ValueError('invalid observation')
            mask=self.ones[b] if result else ~self.ones[b]
            if not (doms[a]&mask):raise ValueError('inconsistent bit')
            return self.normalize(t,slots,replace(doms,a,doms[a]&mask))
        e=self.events[t]
        if e[0]=='round':
            if result!=act[1]:raise ValueError('business wrote different full key')
            return self.normalize(t+1,replace(slots,e[2],-1-result),doms)
        d=e[1];src=e[2] if e[0]=='copy' else d;a=slots[src]
        full=e[0]=='copy' and d!=src and self.visible_copy
        if full:
            if not 0<=result<=self.limit:raise ValueError('code out of domain')
            mask=1<<result
        else:
            if result not in (0,1):raise ValueError('invalid presence')
            mask=~1 if result else 1
        if not (self.possible(a,doms)&mask):raise ValueError('inconsistent business response')
        if a>=0:doms=replace(doms,a,doms[a]&mask)
        return self.normalize(t+1,replace(slots,d,-1 if e[0]=='drop' else a),doms)
    def replay(self,x):
        if self.actual is not None:assert tuple(x)==self.actual
        t,slots,doms=self.start;X=list(x);c=0;trace=[]
        while t<len(self.events):
            val,act=self.lookup(t,slots,doms);e=self.events[t]
            if act[0]=='read':
                _,i,b=act;z=(X[i]>>b)&1;a=slots[i]
                assert a>=0;mask=self.ones[b] if z else ~self.ones[b]
                doms=replace(doms,a,doms[a] & mask);c+=8
                trace.append(('read',i,b,z));t,slots,doms=self.normalize(t,slots,doms);continue
            if act[0]=='round':
                k=act[1];_,target,d=e;assert k in self.keys(target) and k not in X
                X[d]=k;slots=replace(slots,d,-1-k);c+=self.weight(k)+self.fixed[target]*self.charge_business
                trace.append(('create',target,d,k))
            else:
                src=e[2] if e[0]=='copy' else e[1];d=e[1];a=slots[src];k=X[src]
                full=e[0]=='copy' and d!=src and self.visible_copy
                obs=k if full else bool(k)
                if a>=0:
                    mask=(1<<k) if full else (~1 if k else 1)
                    doms=replace(doms,a,doms[a]&mask)
                if e[0]=='drop':X[d]=0;slots=replace(slots,d,-1);price=self.q+9
                else:X[d]=k;slots=replace(slots,d,a);price=8 if d==src else self.copy_charge(k)
                c+=price*self.charge_business;trace.append(tuple(e)+(obs,))
            t,slots,doms=self.normalize(t+1,slots,doms)
        return c,trace,tuple(X)

class WorldBellman(Model):
    """Independent explicit Cartesian worlds oracle: no origin identifiers, no
    per-origin masks, and no theorem about disclosure is used in its state."""
    def __init__(self,r,events):
        super().__init__(r,events)
        self.start=tuple(product(range(self.limit+1),repeat=r))
        self.dp=cache(self._dp)
    def _dp(self,t,S,X=None):
        if t==len(self.events):return 0
        e=self.events[t];possible=[]
        def kid(rows): return tuple(sorted(set(rows)))
        if e[0]=='round':
            _,target,d=e
            for k in self.keys(target):
                if all(k not in x for x in S):
                    possible.append(self.fixed[target]+self.weight(k)+self.dp(t+1,kid(replace(x,d,k) for x in S),None if X is None else replace(X,d,k)))
        else:
            src=e[2] if e[0]=='copy' else e[1];dst=e[1];groups={}
            for x in S:
                k=x[src]
                if e[0]=='drop':obs=bool(k);w=self.q+9;y=replace(x,dst,0)
                elif src==dst:obs=bool(k);w=8;y=x
                else:obs=k;w=self.copy_charge(k);y=replace(x,dst,k)
                groups.setdefault((obs,w),[]).append(y)
                if x==X: xbranch,xx=(obs,w),y
            if X is None:possible.append(max(w+self.dp(t+1,kid(child)) for (z,w),child in groups.items()))
            else:possible.append(xbranch[1]+self.dp(t+1,kid(groups[xbranch]),xx))
        for i in range(self.r):
            for b in range(self.q):
                left=tuple(x for x in S if not ((x[i]>>b)&1))
                right=tuple(x for x in S if (x[i]>>b)&1)
                if left and right:
                    if X is None:possible.append(8+max(self.dp(t,left),self.dp(t,right)))
                    else:possible.append(8+self.dp(t,right if (X[i]>>b)&1 else left,X))
        return min(possible)
    def value(self):return self.dp(0,self.start)
    def value_on(self,x):return self.dp(0,self.start,tuple(x))
