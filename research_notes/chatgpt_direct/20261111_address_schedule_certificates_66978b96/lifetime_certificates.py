"""Full identity pointwise certificates; no original request word is inspected by the controller."""
from functools import cache
from itertools import product

def weight(r, k):
    return 2*k.bit_count()+4*(1-((k >> (r.bit_length()-1)) & 1))

def costs(r, rounds):
    # D is not a universal constant across target member geometries. Supply that separately.
    return tuple(tuple(range(1+t*(r+1),1+(t+1)*(r+1))) for t,_ in rounds)

def obligations(r, rounds, keys):
    """Return, per old slot, full keys selected before or at its first overwrite."""
    if len(rounds)!=len(keys): raise ValueError('length mismatch')
    live=[None]*r
    prefixes=[set() for _ in live]
    for (t,d),k in zip(rounds,keys):
        if not (0<=d<r and t*(r+1)<k<=(t+1)*(r+1)): raise ValueError('illegal action')
        if k in live: return None
        for i,v in enumerate(live):
            if v is None: prefixes[i].add(k)
        live[d]=k
    return tuple(tuple(sorted(p)) for p in prefixes)

@cache
def min_mask(x, keys, q):
    """Least cardinality slot-bit certificate, or None for actual equality."""
    if x in keys: return None
    return min((m for m in range(1<<q) if all(m & (x^k) for k in keys)),
               key=lambda m:(m.bit_count(),m))

def optimal_certificate(initial, rounds, target_count=3):
    r=len(initial); q=(target_count*(r+1)).bit_length()
    if not all(0<=x<=target_count*(r+1) for x in initial):raise ValueError('initial domain')
    if not all(0<=t<target_count for t,d in rounds):raise ValueError('target')
    best=None
    for keys in product(*costs(r,rounds)):
        p=obligations(r,rounds,keys)
        if p is None: continue
        ms=tuple(min_mask(x,ks,q) for x,ks in zip(initial,p))
        if None in ms: continue
        val=sum(weight(r,k) for k in keys)+8*sum(m.bit_count() for m in ms)
        candidate=(val,keys,ms,tuple(x&m for x,m in zip(initial,ms)))
        if best is None or candidate<best: best=candidate
    if best is None:raise AssertionError('r+1 choices always suffice')
    return best

def verify_or_fallback(r,rounds,plan,read_bit,target_count=3):
    """Execute abstract key choices via actual read callbacks. No initial key array argument.
    All reads here are before the first write; on mismatch, fallback finishes the full table.
    Returns branch, selected full keys, charged probe count. Business words executed elsewhere."""
    q=(target_count*(r+1)).bit_length()
    _,ks,ms,expect=plan
    if len(ms)!=r or len(expect)!=r or any(m<0 or m>=1<<q for m in ms):
        raise ValueError('malformed hint')
    ps=obligations(r,rounds,ks)
    if ps is None or any(v&~m or any(not ((v^k)&m) for k in p)
                         for v,m,p in zip(expect,ms,ps)):raise ValueError('uncertified hint')
    obs={}
    def actual(i,j):
        if (i,j) not in obs: obs[i,j]=int(bool(read_bit(i,j)))
        return obs[i,j]
    matched=True
    for i,m in enumerate(ms):
        for j in range(q):
            if m>>j&1 and actual(i,j)!=(expect[i]>>j&1):
                matched=False;break
        if not matched:break
    if matched:return 'certificate',ks,len(obs)
    curr=[sum(actual(i,j)<<j for j in range(q)) for i in range(r)]
    selected=[]
    for (t,d),legal in zip(rounds,costs(r,rounds)):
        k=min((k for k in legal if k not in curr),key=lambda k:(weight(r,k),k))
        selected.append(k);curr[d]=k
    return 'fallback',tuple(selected),len(obs)

def sequential_oracle(r,rounds,initial=None,target_count=3):
    """Independent Bellman over compatible complete-key domains, not proof masks.
    If initial=None, take both adversary branches; else take that input's actual branch.
    Costs exclude the same mandatory business words for every policy."""
    ceiling=target_count*(r+1); q=ceiling.bit_length(); universe=(1<<(ceiling+1))-1
    ones=tuple(sum(1<<x for x in range(ceiling+1) if x>>bit&1) for bit in range(q))
    choices=costs(r,rounds)
    @cache
    def dp(j,domains):
        if j==len(rounds):return 0
        ans=10**12; t,d=rounds[j]
        for k in choices[j]:
            if not any(s>>k&1 for s in domains):
                after=domains[:d]+(1<<k,)+domains[d+1:]
                ans=min(ans,weight(r,k)+dp(j+1,after))
        for i,s in enumerate(domains):
            for bit,mask in enumerate(ones):
                aa=s&~mask; bb=s&mask
                if not aa or not bb:continue
                kids=(aa,bb) if initial is None else ((bb if initial[i]>>bit&1 else aa),)
                ans=min(ans,8+max(dp(j,domains[:i]+(v,)+domains[i+1:]) for v in kids))
        return ans
    return dp(0,(universe,)*r)
