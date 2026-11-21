"""Instance-optimal full-identity certificates for fixed mandatory words.
Offline compilation receives one preparation; the replay policy takes only actual
bit/presence/full-copy outputs. At each create it revalidates its chosen key."""
from functools import cache
from itertools import product
from oracle import Model
from origin_checks import compile_graph, projected

def graph(r,events):
    ops={'round':'W','copy':'C','drop':'D'}
    return compile_graph(r,tuple((ops[e[0]],*e[1:]) for e in events))

@cache
def minimum_mask(x,keys,q):
    if x in keys:return None
    return min((m for m in range(1<<q) if all((x^k)&m for k in keys)),key=lambda m:(m.bit_count(),m))

def optimum(r,events,x):
    m=Model(r,events);g=graph(r,events);x=tuple(x)
    stop=tuple(min(a for a in (g.ends[i],g.first_full[i],g.first_presence[i] if x[i]==0 else None) if a is not None)
               for i in range(r))
    base=sum(m.fixed[t] for t in g.targets)+sum(m.q+9 if e[0]=='drop' else 8
         for e in events if e[0]=='drop' or (e[0]=='copy' and e[1]==e[2]))
    best=None
    for keys in product(*(m.keys(t) for t in g.targets)):
        physical=projected(g,x,keys)
        if physical is None:continue
        ms=tuple(minimum_mask(x[i],tuple(sorted(set(keys[:stop[i]]))),m.q) for i in range(r))
        assert None not in ms
        cost=base+physical[0]+8*sum(a.bit_count() for a in ms)
        line=(cost,keys,ms,tuple(a&b for a,b in zip(ms,x)))
        if best is None or line<best:best=line
    assert best is not None
    return best

def replay(r,events,hint,read,perform):
    """No access to the true table; read(i,b) and perform(event,key) are callbacks.
    A hint may cross a different free-disclosure branch: check at EVERY creation."""
    m=Model(r,events);value,preferred,masks,expected=hint
    if len(masks)!=r or len(expected)!=r or len(preferred)!=sum(e[0]=='round' for e in events):raise ValueError('malformed hint')
    full=m.domain; dom=[full]*r; count=0
    def probe(i,b):
        nonlocal count
        bit=read(i,b);count+=1;dom[i]&=m.ones[b] if bit else ~m.ones[b]
        assert dom[i]
        return int(bit)
    for i in range(r):
        if masks[i] >= (1<<m.q) or masks[i]<0:raise ValueError('mask')
        for b in range(m.q):
            if masks[i]>>b&1:probe(i,b)
    j=0;diverged=False
    for e in events:
        if e[0]=='round':
            _,t,d=e;k=preferred[j];j+=1
            def available(k):return all(not ((a>>k)&1) for a in dom)
            if k not in m.keys(t) or not available(k):
                diverged=True
                for i,a in enumerate(dom):
                    if a.bit_count()==1:continue
                    for b in range(m.q):
                        s=dom[i];o=m.ones[b]
                        if s&o and s&~o:probe(i,b)
                k=min((k for k in m.keys(t) if available(k)),key=lambda k:(m.weight(k),k))
            perform(e,k);dom[d]=1<<k
        else:
            k=perform(e,None);d=e[1]
            if e[0]=='copy' and d!=e[2]:
                s=e[2];assert dom[s]>>k&1
                dom[d]=dom[s]=1<<k
            elif e[0]=='drop':dom[d]=1
            elif k:dom[d]&=~1
            else:dom[d]=1
    return count,diverged
