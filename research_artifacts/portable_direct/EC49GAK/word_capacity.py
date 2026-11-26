from verify_gak import intervals
from collections import Counter
from math import comb
from pathlib import Path
import json

def max_word_capacity(st,k,H=14):
    iv=intervals(st,k,H)
    # all original p<=k
    assert all(0<=a<=b<=k for a,b in iv)
    # independent matching to individual words
    opts=[[w for w in range(1<<k) if a<=w.bit_count()<=b] for a,b in iv]
    mate={}
    def aug(x,seen):
        for w in opts[x]:
            if w in seen:continue
            seen.add(w)
            if w not in mate or aug(mate[w],seen):
                mate[w]=x;return True
        return False
    m=sum(aug(x,set()) for x in range(len(st)))
    # maximize additive interval overload, separated components.
    f=[0]*(k+2)
    for b in range(k+1):
        f[b+1]=max([f[b]]+[f[max(0,a-1)]+sum(l>=a and h<=b for l,h in iv)-sum(comb(k,j) for j in range(a,b+1)) for a in range(b+1)])
    assert m==len(st)-f[k+1]
    return m

if __name__=='__main__':
    fr=json.loads(Path('recoverable_frontier.out').read_text())
    rows=[]
    for i,line in enumerate(Path('ga_nodes.txt').read_text().splitlines()):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]))
        v=n-min(x.bit_count() for x in fr['rows'][i]['frontier'])
        m=max_word_capacity(st,k)
        assert m>=v
        rows.append([i,k,n,v,m])
    print(json.dumps({'rows':rows,'gap_hist':dict(Counter(r[4]-r[3] for r in rows))},separators=(',',':')))
