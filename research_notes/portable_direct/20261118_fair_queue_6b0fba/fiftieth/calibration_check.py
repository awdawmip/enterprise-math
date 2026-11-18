"""Finite positive-world readout from the pinned recorder formula and public weighted-BRC."""
import argparse
from collections import Counter,defaultdict
from fractions import Fraction as F
from hashlib import sha1
from itertools import permutations,product
import json
from pathlib import Path
import sys

PINS={
    'research_tasks/RS-EULER-RR-20261012-05_B03_GEN2.md':'7d2699dca92fc38f65ccc7d02778382d1db81c57',
    'research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md':'03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b',
    'src/enterprise_math/brc_weighted.py':'3f205696709e847909958a153f8fe10d3f6b70f0',
    'src/enterprise_math/brc_logarithm.py':'4732e5fc381ce613d240c4381ccbef03c27a69c7',
    'src/enterprise_math/exact_arithmetic.py':'35ea95b0916494b83a92386e3e313928362dd79e',
}
def load(root):
    for name,pin in PINS.items():
        raw=(root/name).read_bytes()
        assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin
    sys.path.insert(0,str(root/'src'))
    from enterprise_math import brc_weighted
    return brc_weighted

def compositions(total):
    for i in range(total+1):
        for j in range(total+1-i):
            yield (i,j,total-i-j)

def lines(M):
    return tuple(tuple(sum(M[i][j] for i in range(3) for j in range(3)
                      if fn(i,j)%3==k) for k in range(3)) for fn in
                 (lambda i,j:i,lambda i,j:j,lambda i,j:i+j,lambda i,j:i-j))

def bayes(M):
    return sum(max(M[i][(y-i)%3] for i in range(3)) for y in range(3))

def lattice(grid):
    candidates=list(compositions(grid))
    best={}
    checked=0
    for M in product(candidates,repeat=3):
        p,q,v,s=lines(M)
        mass=3*grid
        score=bayes(M)
        assert all(3*M[i][b]==p[i]+q[b]+v[(i+b)%3]+s[(i-b)%3]-mass
                   for i in range(3) for b in range(3))
        assert 3*score==sum(max(p[i]+q[(y-i)%3]+s[(2*i-y)%3] for i in range(3))
                            for y in range(3))-2*mass
        L=max(q)
        U=max(L,sum(min(a,grid) for a in q))
        assert L<=score<=U
        best[q]=max(best.get(q,0),score)
        checked+=1
    assert all(val==max(max(q),sum(min(a,grid) for a in q)) for q,val in best.items())
    return dict(row_total=grid,total_joint_tables=checked,distinct_offset_margins=len(best),
                all_sharp_upper_bounds_attained=True)

def finite_kernel(brc,counts,offsets,mod=3,evolving_reference=False):
    # Input weights are joint laws, not products of experimental marginals.
    # A is an independent uniform gauge preparation for these displayed witnesses.
    pool=defaultdict(lambda:brc.CWM_ZERO)
    before=defaultdict(lambda:brc.CWM_ZERO)
    after=defaultdict(lambda:brc.CWM_ZERO)
    marg=Counter()
    unit=brc.cwm_edge(1)
    for (j,bs),mass in offsets.items():
        if not mass:continue
        for a in range(mod):
            w=brc.cwm_edge(mass/mod)
            k=(j,a,(a+bs[0])%mod)
            before[k]=brc.cwm_recoalesce(before[k],w)
            read=[]
            common_ready=(a+bs[0])%mod
            for b in bs:
                ref=(common_ready-b)%mod if evolving_reference else a
                receiver=common_ready if evolving_reference else (ref+b)%mod
                turns=(j-ref)%mod
                for step in range(max(1,turns)):
                    w=brc.cwm_propagate(w,unit)
                    counts['contact' if turns else 'hold']+=1
                    if turns:receiver=(receiver+1)%mod
                assert receiver==(j+b)%mod
                read.append(receiver)
            after[j,a,tuple(read)]=brc.cwm_recoalesce(after[j,a,tuple(read)],w)
            pool[j,tuple(read)]=brc.cwm_recoalesce(pool[j,tuple(read)],w)
            marg[j]+=w.total
    assert sum(w.total for w in after.values())==1
    assert all(marg[j]==F(1,mod) for j in range(mod))
    assert all(sum(w.total for (j,a,b),w in before.items() if a==k)==F(1,mod) for k in range(mod))
    output=sorted(set(y for j,y in pool))
    table=[[pool[j,y].total*mod for y in output] for j in range(mod)]
    score=sum(max(pool[j,y].total for j in range(mod)) for y in output)
    if len(output)<=3:
        cert=max(sum(pool[guess,y].total for guess,y in zip(decision,output))
                 for decision in product(range(mod),repeat=len(output)))
        assert cert==score
    return dict(record_words=output,channel_by_source=[[str(z) for z in row] for row in table],
                best_score=str(score),optimal_decoder=[max(range(mod),key=lambda j:pool[j,y].total) for y in output],
                full_initial_27_cells=[str(before[j,a,r].total) for j,a,r in product(range(3),repeat=3)])

def families(brc):
    calls=Counter()
    out={}
    for name in ('independent','reflected','positive_mixture'):
        law={}
        for j in range(3):
            for b in range(3):
                law[j,(b,)]=dict(independent=F(1,9),reflected=F(int(b==j),3),
                                  positive_mixture=(F(1,9)+F(int(b==j),3))/2)[name]
        out['single_'+name]=finite_kernel(brc,calls,law)
    assert out['single_positive_mixture']['best_score']=='2/3'
    assert all(F(x)>0 for x in out['single_positive_mixture']['full_initial_27_cells'])
    q=(F(1,2),F(1,2),F())
    for name in ('independent','shared','evolving'):
        law={}
        for j,b,c in product(range(3),repeat=3):
            if name=='independent':mass=q[b]*q[c]
            if name=='shared':mass=q[b] if c==b else F()
            if name=='evolving':mass=q[b] if c==(1-b)%3 else F()
            law[j,(b,c)]=mass/3
        out['double_'+name]=finite_kernel(brc,calls,law,evolving_reference=name=='evolving')
    assert [out[k]['best_score'] for k in ('single_independent','single_reflected','double_independent',
          'double_shared','double_evolving')]==['1/3','1','3/4','1/2','1']
    return out,dict(calls)

def signatures(g,T):
    n=len(g)
    out=[]
    for b in range(n):
        values=[]
        state=b
        for _ in range(T-1):
            values.append((g[state]-state)%n)
            state=g[state]
        out.append(tuple(values))
    return out

def even_permutation(n):
    m=n//2
    return tuple((2*(b%m)+int(b>=m)+1)%n for b in range(n))

def permutation_grid():
    info=[]
    for n in range(2,9):
        dist=Counter()
        for g in permutations(range(n)):
            a=len(set(signatures(g,2)))
            b=len(set(signatures(g,3)))
            # Direct enumeration of all n^2 actual (j,b) outputs, on this small grid.
            if n<=6:
                for T,count in [(2,a),(3,b)]:
                    words=defaultdict(set)
                    for j,k in product(range(n),repeat=2):
                        y=[]
                        for _ in range(T):
                            y.append((j+k)%n)
                            k=g[k]
                        words[tuple(y)].add(j)
                    assert len(words)==n*count
            dist[a,b]+=1
        if n%2:
            example=tuple((2*b)%n for b in range(n))
            assert len(set(signatures(example,2)))==n
        else:
            example=even_permutation(n)
            assert len(set(signatures(example,2)))==n-1
            assert len(set(signatures(example,3)))==(n if n>2 else 1)
        assert max(a for a,b in dist)==(n if n%2 else n-1)
        info.append(dict(n=n,all_permutations=sum(dist.values()),best_two=max(a for a,b in dist),
                         best_three=max(b for a,b in dist),example=example,
                         counts_by_two_three={'%d,%d'%k:v for k,v in sorted(dist.items())}))
    for n in range(9,101):
        g=even_permutation(n) if n%2==0 else tuple((2*b)%n for b in range(n))
        assert len(set(signatures(g,2)))==n-int(n%2==0) and len(set(signatures(g,3)))==n
    return info

def box_example():
    # 60-unit grid; analytic endpoints below attained and separately checked at their rational q.
    lo,hi=(21,9,0),(39,30,15)
    possible=[q for q in compositions(60) if all(l<=v<=h for l,v,h in zip(lo,q,hi))]
    lower=min(max(q) for q in possible)
    upper=max(max(max(q),sum(min(v,20) for v in q)) for q in possible)
    qlo=(F(3,8),F(3,8),F(1,4))
    qhi=(F(21,60),F(24,60),F(15,60))
    assert max(qlo)==F(3,8) and sum(min(F(1,3),v) for v in qhi)==F(11,12)
    return dict(den=60,low=lo,high=hi,admissible_grid=len(possible),least=lower,greatest=upper,
                rational_simplex_endpoints=['3/8','11/12'],
                rational_endpoint_witnesses=[[str(v) for v in q] for q in (qlo,qhi)],
                minimizer=next(q for q in possible if max(q)==lower),
                maximizer=next(q for q in possible if max(max(q),sum(min(v,20) for v in q))==upper))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    args=p.parse_args()
    brc=load(args.repo)
    jobs,calls=families(brc)
    print(json.dumps(dict(source_git_blobs=PINS,positive_world_channels=jobs,brc_unit_updates=calls,
                exact_transport_grid=lattice(6),box_example=box_example(),permutation_grid=permutation_grid()),
                sort_keys=True,indent=2))
if __name__=='__main__': main()
