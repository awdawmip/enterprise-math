"""Exact largest one-read color class for independently selectable arbitrary pairs, q>=5 and the five-symbol case."""
from itertools import product
from functools import cache
from pathlib import Path
import argparse,json
@cache
def result(a):
    choices=[range(1,v) if v>1 else (1,) for v in a]
    if max(a)==1:return 1,None
    best=0;cut=None
    for b in product(*choices):
        c=tuple(v-x if v>1 else 1 for v,x in zip(a,b))
        if b>c:continue
        ans=result(tuple(sorted(b)))[0]+result(tuple(sorted(c)))[0]
        if ans>best:best=ans;cut=(b,c)
    return best,cut
def actual(a):
    if max(a)==1:return [tuple(0 for _ in a)]
    # result uses coordinate order and recurses via sorted budgets for value only.
    _,(b,c)=result(a)
    return actual(b)+[tuple(ti+(bi if ai>1 else 0)for ti,ai,bi in zip(v,a,b))for v in actual(c)]
def laminar(W):
    blocks=[frozenset(i for i,p in enumerate(W) if p[k]==x)for k in range(len(W[0])) for x in {p[k] for p in W}]
    return all(not (u&v) or u<=v or v<=u for u in blocks for v in blocks)
@cache
def compact(t):
    # counts of coordinates with 2,3,4,5 available labels; a constant coordinate is implicit.
    if not any(t):return 1
    def splits(q,m):
        def gen(r,left,ls):
            if r==1:
                yield [left]+ls
            else:
                for v in range(left+1):yield from gen(r-1,left-v,[v]+ls)
        for ns in gen(q-1,m,[]):
            u=[0]*4;v=[0]*4
            for j,n in enumerate(ns,1):
                if j>1:u[j-2]+=n
                if q-j>1:v[q-j-2]+=n
            yield u,v
    best=0
    for parts in product(*(splits(q,m) for q,m in enumerate(t,2))):
        u=tuple(map(sum,zip(*(x for x,y in parts))));v=tuple(map(sum,zip(*(y for x,y in parts))))
        if u<=v:best=max(best,compact(u)+compact(v))
    return best
def run():
    tab={}
    for q,upto in [(2,6),(3,6),(4,6),(5,7),(6,5),(7,4),(8,3)]:
        row=[]
        for n in range(1,upto+1):
            a=(q,)*n;w=actual(a);v=result(a)[0]
            assert len(w)==len(set(w))==v and laminar(w)
            row.append(v)
        tab[q]=row
    assert tab[5][:3]==[5,8,10]
    full=[compact((0,0,0,n)) for n in range(1,9)]
    assert full[:7]==tab[5] and full[7]==16
    scalar={str(q):min((n for n in range(1,9) if compact(tuple(n if j==q else 0 for j in range(2,6)))==2**(q-1)),default=None) for q in range(2,6)}
    assert scalar=={'2':1,'3':2,'4':4,'5':8}
    return dict(status='PASS',five_symbol_capacity_n1_to_8=full,minimum_coordinates_for_saturation=scalar,homogeneous_maximum_class_by_alphabet={str(k):v for k,v in tab.items()},five_symbol_three_coordinate_witness=actual((5,5,5)),five_symbol_root_split=result((5,5,5))[1],scope='combinatorial laminar class capacity, with physical equivalence in the independent five-cycle protocol; entries with other alphabets are combinatorial only')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('capacity_results.json'));a=ap.parse_args();d=run();a.out.write_text(json.dumps(d,indent=2)+'\n');print(d)
