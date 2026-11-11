"""Exact menu/advice and one-query overlap checks. No kernel or nonstandard modules."""
from argparse import ArgumentParser
from functools import cache
from itertools import combinations
from pathlib import Path
import json

def parts(N):
    cells=[]
    def visit(i):
        if i==N:
            yield tuple(cells);return
        for j in range(len(cells)):
            old=cells[j];cells[j]=old|(1<<i)
            yield from visit(i+1);cells[j]=old
        cells.append(1<<i);yield from visit(i+1);cells.pop()
    yield from visit(0)

def tiny_mux():
    # p=1, two independent one-bit banks. Oracle exhaustively optimizes ALL encoders.
    ws=range(8);masks=[sum(1<<w for w in ws if w>>i&1) for i in range(3)]
    P=list(parts(8))
    def members(U):return [w for w in ws if U>>w&1]
    def splits(U):return [(U&m,U&~m) for m in masks if U&m and U&~m]
    def label(w,t):return (w&1,(w>>(1+((w&1)^t)))&1)
    @cache
    def fixed(U,t):
        if len({label(w,t) for w in members(U)})==1:return 0
        return 1+min(max(fixed(a,t),fixed(b,t)) for a,b in splits(U))
    @cache
    def allbits(U):
        if U.bit_count()==1:return 0
        return 1+min(max(allbits(a),allbits(b)) for a,b in splits(U))
    @cache
    def early(U,T,v):
        can_emit=not (U&masks[0] and U&~masks[0])
        post=max(fixed(U,t) for t in T)
        if can_emit and (v<0 or post<=v):best=post if v<0 else 0
        else:best=20
        for a,b in splits(U):best=min(best,1+max(early(a,T,v),early(b,T,v)))
        return best
    rows=[];counts=0
    for T in [(0,),(1,),(0,1)]:
        m=len(T)
        for s in range(4):
            admiss=[b for b in P if len(b)<=1<<s]
            def opt(val):
                return min(max(val(U) for U in b) for b in admiss)
            know=max(opt(lambda U:fixed(U,t)) for t in T)
            blind=opt(lambda U:early(U,T,-1));union=opt(allbits)
            stage=[opt(lambda U:early(U,T,v)) for v in range(3)]
            assert know==max(0,2-s)
            assert blind==max(0,2-s,(1+m-s+m-1)//m)
            assert union==max(0,3-s)
            assert stage==[max(0,1+m*max(0,1-v)-s) for v in range(3)]
            counts+=len(admiss)*(len(T)+5)
            rows.append(dict(menu=T,s=s,encoders=len(admiss),preknown=know,after_selector=blind,syntactic_union=union,
                             best_common_early_reads_given_late_cap_0_1_2=stage))
    return dict(worlds=8,nonlinear_partitions=len(P),partition_objectives=counts,cases=rows)

def graph_census(n):
    E=list(combinations(range(n),2));num=1<<len(E);pairs=[(1<<a)|(1<<b) for a,b in E]
    nc=1<<(1<<n);allp=(1<<n)-1
    # For every nonempty residual, compute which edges can be served in <=one physical query,
    # independent of the structural theorem. With <=2 output pairs, at least one of the two
    # demanded coordinate tests separates the pair if necessary. Check separation by an actual
    # column (including all off-list columns), not just a numerical-output criterion.
    masks=[sum(1<<w for w in range(1<<n) if w>>i&1) for i in range(n)]
    allowed=[[sum(1<<w for w in range(1<<n) if (w&e)==y) for y in range(allp+1) if (y&e)==y] for e in pairs]
    size_by=[0]*num
    counts=[0]*num
    for U in range(1,nc):
        valid=0
        for i,ys in enumerate(allowed):
            active=[U&y for y in ys if U&y]
            ok=(len(active)==1 or any(all(not (a&q) for a in active[1:]) and len(active)==2 and not (active[0]&~q)
                 or len(active)==2 and not (active[0]&q) and not (active[1]&~q) for q in masks))
            assert ok==(len(active)<=2)
            if ok:valid|=1<<i
        size_by[valid]=max(size_by[valid],U.bit_count());counts[valid]+=1
    rows=[]
    for G in range(num):
        maxcell=max(v for a,v in enumerate(size_by) if G&a==G)
        tau=min(S.bit_count() for S in range(1<<n) if all(S&e for i,e in enumerate(pairs) if G>>i&1))
        assert maxcell==1<<(n-tau)
        rows.append(dict(graph=G,vertex_cover=tau,maxcell=maxcell))
    return dict(n=n,edge_order=E,graphs=num,nonempty_cells=nc-1,
                graph_cell_comparisons=num*(nc-1),results=rows)

def main():
    p=ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('menu_results.json'));args=p.parse_args()
    g=[graph_census(n) for n in (2,3,4)]
    out=dict(status='PASS',mux=tiny_mux(),graphs=g,total_graphs=sum(x['graphs'] for x in g),graph_cell_pairs=sum(x['graph_cell_comparisons'] for x in g))
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS',out['mux']['partition_objectives'],out['graph_cell_pairs'])
if __name__=='__main__':main()
