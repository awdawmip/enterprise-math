"""Control-side direct products of independent local 3-bit majority service gadgets."""
import argparse,json
from functools import cache
from itertools import permutations
from pathlib import Path
HERE=Path(__file__).resolve().parent
maj=sum(1<<h for h in range(8) if h.bit_count()>=2)
rows=(maj,)+tuple(1<<h for h in (1,2,4,6,5,3))+tuple(sum(1<<h for h in range(8) if h>>i&1)for i in range(3))
perms=[tuple((sum(((h>>p[i])&1)<<i for i in range(3))^f) for h in range(8))for p in permutations(range(3))for f in (0,7)]
canon={u:min(sum(1<<g[h] for h in range(8) if u>>h&1)for g in perms)for u in range(1,256)}
assert all(sum(1<<g[h] for h in range(8) if m>>h&1) in set(rows)|{255^r for r in rows} for g in perms for m in rows)
spl={u:tuple(sorted({tuple(sorted((canon[u&m],canon[u&~m])))for m in rows if u&m and u&~m})) for u in set(canon.values())}
def known(u):return not(u&maj and u&~maj)
@cache
def depth(u):
    return 1+min(max(depth(a),depth(b))for a,b in spl[u]) if spl[u] else 0
@cache
def feasible(U,a,b):
    n=sum(not known(u) for u in U)
    if b<sum(depth(u)for u in U):return False
    if n==0 or a>=b:return True
    if a<n:return False
    for i,u in enumerate(U):
        if i and U[i-1]==u:continue
        for l,r in spl[u]:
            def child(v):
                x=U[:i]+U[i+1:]+(v,)
                return tuple(sorted(x))
            if feasible(child(l),a-1,b-1) and feasible(child(r),a-1,b-1):return True
    return False
def frontier(q):
    U=(255,)*q
    frontier=[(a,next(b for b in range(3*q,4*q+1) if feasible(U,a,b))) for a in range(q,3*q+1)]
    assert all(b==4*q-(a-q)//2 for a,b in frontier)
    return frontier
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'product_results.json');p.add_argument('--max-q',type=int,default=6);z=p.parse_args()
    out=[]
    for q in range(1,z.max_q+1):
        v=frontier(q);out.append(dict(q=q,frontier=v));print(q,v,flush=True)
    z.out.write_text(json.dumps(dict(status='PASS',models=out),sort_keys=True,indent=2)+'\n')
