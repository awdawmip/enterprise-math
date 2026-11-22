#!/usr/bin/env python3
"""R762JT archive witness checker, independent of producer's forest search.
Checks exact enumerated case coverage, rainbow trees, and GF(2) parity quotient.
"""
from itertools import combinations
import json,base64,zlib,hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
P=list(combinations(range(6),2));S=list(combinations(range(6),3))
MATCH=[(),((0,1),),((0,1),(2,3)),((0,1),(2,3),(4,5))]

def row_reduce(rows):
    piv={}
    for u in rows:
        while u:
            h=u.bit_length()-1
            if h in piv:u ^= piv[h]
            else:piv[h]=u;break
    return piv

def mod(u,piv):
    for h in sorted(piv,reverse=True):
        if (u>>h)&1:u^=piv[h]
    return u

def check():
    evidence=json.load(open(HERE/'R762JT_EVIDENCE.json'))
    b=open(HERE/'R762JT_RAINBOW_CERTS.b64','rb').read()
    assert hashlib.sha256(b).hexdigest()==evidence['certificates_b64_sha256']
    raw=zlib.decompress(base64.b64decode(b))
    assert hashlib.sha256(raw).hexdigest()==evidence['certificate_records_sha256']
    records=json.loads(raw)
    lookup={}
    for m,d,t in records:
        key=(m,tuple(d));assert key not in lookup
        lookup[key]=t
    assert len(lookup)==9648
    observed=0;gone=0;parity=0
    for m,miss in enumerate(MATCH):
        active=[p for p in P if p not in miss];ix={v:i for i,v in enumerate(active)}
        flexible=[s for s in S if all(p in ix for p in combinations(s,2))]
        frozen=[s for s in S if s not in flexible]
        parents={p:p for p in active}
        def root(p):
            while parents[p]!=p:p=parents[p]
            return p
        for s in frozen:
            members=[p for p in combinations(s,2) if p in ix]
            assert len(members)==2
            parents[root(members[0])]=root(members[1])
        blocks={}
        for v in active:blocks.setdefault(root(v),[]).append(v)
        block={v:i for i,vertices in enumerate(blocks.values()) for v in vertices}
        for k in range(5):
            for ds in combinations(flexible,k):
                D=set(ds);observed+=1
                vectors={s:[(1<<ix[a])^(1<<ix[b]) for a,b in combinations(tuple(combinations(s,2)),2)] for s in flexible}
                B=row_reduce(z for s in flexible if s not in D for z in vectors[s])
                reach={0}
                for s in ds:reach={mod(z^x,B) for z in reach for x in vectors[s]}
                assert len(reach)==1<<(len(active)-1-len(B))
                parity+=1
                exceptional=k==4 and any(all(p in tuple(combinations(s,2)) for s in ds)
                    and all(set(p).isdisjoint(z) for z in miss) for p in P if p not in miss)
                key=(m,tuple(S.index(s) for s in ds))
                if exceptional:
                    gone+=1;assert key not in lookup
                    continue
                tree=lookup.pop(key)
                assert len(tree)==len(blocks)-1
                used=set(); uf=list(range(len(blocks)))
                def ru(x):
                    while uf[x]!=x:x=uf[x]
                    return x
                for label,i in tree:
                    assert label not in used and S[label] in flexible and S[label] not in D and 0<=i<3
                    used.add(label)
                    a,b=list(combinations(tuple(combinations(S[label],2)),2))[i]
                    x,y=ru(block[a]),ru(block[b]);assert x!=y;uf[x]=y
                assert len(set(ru(x) for x in uf))==1
    assert observed==9670 and parity==9670 and gone==22 and not lookup
    print('INDEPENDENT_ARCHIVE_CHECK PASS cases=',observed,'parity=',parity,'rainbow=',len(records),'exceptions=',gone)

if __name__=='__main__':check()
