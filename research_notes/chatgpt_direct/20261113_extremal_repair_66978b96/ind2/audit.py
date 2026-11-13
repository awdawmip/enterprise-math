"""Independent finite audits shared by the reduction and the extension verifier."""
import argparse,itertools,json
from collections import Counter
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
def depth(angles):
    @lru_cache(None)
    def f(mask):
        if mask.bit_count()<=1:return 0
        res=[]
        for j in (1,2,4):
            m=sum(1<<a for a in range(8)if mask>>a&1 and a&j)
            if m and m!=mask:res.append(1+max(f(m),f(mask^m)))
        return min(res)
    return f(angles)
def run():
    H=Counter();small=Counter()
    for m in range(256):
        claw=any(all(m>>a&1 for a in (i,i^1,i^2,i^4))for i in range(8))
        illegal=m.bit_count()>4 or claw
        assert illegal==(depth(m)>2)
        H[depth(m)]+=1;small[m.bit_count(),claw]+=1
    V=range(5)
    axis_lines=[tuple(tuple(t[i] if i!=k else a for i in range(3))for a in V)for t in itertools.product(V,repeat=3)for k in range(3)if t[k]==0]
    planes=[{t for t in itertools.product(V,repeat=3)if t[k]==a}for k in range(3)for a in V]
    assert len(axis_lines)==75 and len(planes)==15
    assert all(sum(set(l)<=p for p in planes)==2 for l in axis_lines)
    # independent, plain reading of each output section using no numeric canonicalization code
    checked=[]
    for s in map(int,(HERE/'seeds.txt').read_text().split()):
        w=list(map(int,nvec(s,3,25)));row=[w[i*5:i*5+5]for i in range(5)];col=list(zip(*row))
        sing=lambda a:sum(n==1 for n in Counter(a).values())
        d=sum(2-sing(r) for r in row+col)
        both=sum(row[j].count(w[5*j+k])==col[k].count(w[5*j+k])==1 for j,k in itertools.product(V,repeat=2))
        assert 2*d+both<=6;checked.append([s,d,both])
    return {'local_valid_by_depth':dict(sorted(H.items())),'minimal_forbidden_five_sets_per_cube':small[5,False], 'lines':len(axis_lines),'planes':len(planes),'normalized_degree_profiles':[[d,b,n] for (d,b),n in sorted(Counter((d,b)for s,d,b in checked).items())]}
def nvec(s,b,n):
    v=[0]*n
    for j in range(n-1,-1,-1):s,v[j]=divmod(s,b)
    assert s==0
    return v
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'audit_results.json');a=ap.parse_args();r=run();a.out.write_text(json.dumps(r,indent=1)+'\n');print(r)
