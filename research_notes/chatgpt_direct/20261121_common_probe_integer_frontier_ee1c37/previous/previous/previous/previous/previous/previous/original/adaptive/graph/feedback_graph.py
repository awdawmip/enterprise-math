"""Five-cycle conditional service, joint zero-reread color, original words. Standard library."""
from pathlib import Path
from itertools import combinations,product
from functools import cache
from collections import Counter
import sys,json,argparse,copy
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from projected.kernel.subset_kernel import prefix,initial,emit,marker_slot,least_one,core

V=tuple(range(5));E=tuple((i,(i+1)%5) for i in V);P=list(product(V,repeat=2))
def fcol(j):
    return sum(1<<h for h in V if (h==j-1 if j<=5 else h in E[j-6]))
def sides(e,h):return int(h in E[e])
def audit(e,h):return (11 if sides(e,h) else 6+e, (11 if h==E[e][0] else 1+E[e][0]) if sides(e,h) else 12)
def partition(n,maxcells):
    def visit(t):
        if len(t)==n:yield t;return
        for c in range(min(maxcells,2+max(t,default=-1))):yield from visit(t+(c,))
    yield from visit(())
def single_policy(cols):
    def decide(e,msg,first,probe):
        # Input is the transmitted message, not a history.
        if first!=11:
            assert first==e+6;return 12
        u,v=E[e];possible=[x for x in (u,v) if cols[x]==msg]
        assert possible
        if len(possible)==2:
            return 11 if probe(u+1) else u+1
        return 11 if possible[0]==u else u+1
    return decide
def execute(C,h,e,encoder,decoder):
    p=prefix(C,initial(h),route=fcol);pre=p.cost
    # Encoder sees actual historical guard bits and never sees a future menu or the prepared h.
    observed=sum(int(p.events[i]['present'])<<i for i in range(3))
    msg=encoder(observed)
    return suffix(p,h,e,msg,decoder)
def suffix(p,h,e,msg,decoder):
    pre=p.cost
    j=e+6;old=p.copy(13,marker_slot(j))
    assert old in (0,j)
    p.drop(13);mandatory=p.cost-pre
    first=emit(p,[11 if old==j else j])[0]['bind_delivered']
    # Next demanded name and key depend on the actual first binding output.
    asked=[]
    def probe(k):
        b=p.probe(marker_slot(k),least_one(k));asked.append([k,b]);return b
    k=decoder(e,msg,first,probe)
    sec=emit(p,[k])[0]['bind_delivered']
    assert (first,sec)==audit(e,h) and p.codes()==tuple([0,0,0]+[j if fcol(j)&(1<<h) else 0 for j in range(1,11)]+[0,0])
    return dict(pre=pre,copy_then_clear=mandatory,copy_result=old,first=first,second=sec,
                supplements=asked,total=p.cost)
def rectangles():
    # A color may cover only a subset of a product of two nonadjacent pairs.
    I=[(i,(i+2)%5) for i in V]
    rect=[(a,b)for a in I for b in I]
    masks=[sum(1<<P.index(v) for v in product(*r)) for r in rect];full=(1<<25)-1
    @cache
    def cover(U,left):
        if not U:return ()
        if left*4<U.bit_count():return None
        bit=U&-U
        for j,M in enumerate(masks):
            if M&bit:
                ans=cover(U&~M,left-1)
                if ans is not None:return (j,)+ans
        return None
    assert cover(full,7) is None;sol=cover(full,8);assert sol and len(sol)==8
    rects=[rect[i] for i in sol]
    colors={v:next(i for i,(a,b) in enumerate(rects) if v[0] in a and v[1] in b) for v in P}
    assert len(set(colors.values()))==8
    for u,v in combinations(P,2):
        conflict=any(sides(e,u[0])==sides(e,v[0]) and sides(f,u[1])==sides(f,v[1]) and (audit(e,u[0]),audit(f,u[1]))!=(audit(e,v[0]),audit(f,v[1])) for e,f in P)
        expected=any(tuple(sorted((a,b))) in {tuple(sorted(edge))for edge in E} for a,b in zip(u,v))
        assert conflict==expected and (not conflict or colors[u]!=colors[v])
    return rects,colors

def run():
    C=core.prior.Compiler(slots=15);cols={0:(0,0,0,0,0),1:(0,0,1,0,1),2:(0,1,0,1,2)}
    independent={}
    for s,code in cols.items():
        paths=[dict(h=h,e=e,**execute(C,h,e,lambda actual:code[actual],single_policy(code))) for h,e in P]
        reads=[len(v['supplements'])for v in paths]
        independent[str(s)]=dict(paths=paths,total_reads=sum(reads),worst_reads=max(reads),worst_commands=max(v['total'] for v in paths))
    for s,(total,worst) in {0:(10,1),1:(2,1),2:(0,0)}.items():
        assert (independent[str(s)]['total_reads'],independent[str(s)]['worst_reads'])==(total,worst)
    base=independent['2']['paths']
    opt={}
    for s in range(4):
        options=[]
        for c in partition(5,2**s):
            d=[int(h in E[e] and c[E[e][0]]==c[E[e][1]]) for h,e in P]
            worst=max(row['total']+8*t for row,t in zip(base,d))
            options.append((sum(d),max(d),worst,c))
        opt[str(s)]={'best_read_sum':min(v[0]for v in options),'best_max_reads':min(v[1]for v in options),'best_max_commands':min(v[2]for v in options),'messages_checked':len(options)}
    for s in range(3):assert opt[str(s)]['best_max_commands']==independent[str(s)]['worst_commands']
    rects,colors=rectangles()
    # Both components are really prepared; the one shared message is computed from the two
    # observed deletion-reply logs BEFORE menu indices are supplied. Branch-local clones share only
    # an immutable compiler; all mutable matching, ledger and private answer state are independent.
    agg=Counter();transcript_checks=0;raw_suffixes=0;traces=[]
    for v in P:
        ps=[prefix(C,initial(h),route=fcol) for h in v]
        actual=tuple(sum(int(p.events[i]['present'])<<i for i in range(3)) for p in ps)
        message=colors[actual]
        for p in ps:p.events=[]  # erase pre-join log from decoder/harness clone
        for menus in P:
            inst=ps if menus==P[-1] else [copy.deepcopy(p,{id(C):C}) for p in ps]
            rows=[]
            for i,(p,h,e) in enumerate(zip(inst,v,menus)):
                def decoder(menu,msg,first,probe,cidx=i):
                    if first!=11:
                        assert first==6+menu;return 12
                    u,w=E[menu];possible=set(rects[msg][cidx])&{u,w}
                    assert len(possible)==1
                    return 11 if u in possible else u+1
                r=suffix(p,h,e,message,decoder)
                assert not r['supplements'] and (r['first'],r['second'])==audit(e,h)
                rows.append(r);raw_suffixes+=1
            agg[sum(r['total'] for r in rows)]+=1;transcript_checks+=1
            if menus==P[-1] or (v==(0,0) and menus==(0,0)):
                traces.append(dict(histories=v,menus=menus,joint_message=message,paths=rows))
    assert raw_suffixes==1250 and transcript_checks==625
    return dict(status='PASS',single=independent,finite_optima=opt,
                two_coordinates=dict(rectangles=rects,colors=[colors[v]for v in P],world_order=P,
                  original_pair_preparations=25,original_suffixes=raw_suffixes,paired_executions=transcript_checks,representative_traces=traces,command_histogram=dict(sorted(agg.items())),
                  supplement_queries=0,logical_pair_checks=300),
                counts=dict(single_raw=75,paired_original_prefixes=50,paired_original_suffixes=1250,paired_cases=625),
                scope='Two physically independent 15-slot units, all 625 joint cases really dispatch both selected original services; same certified prefix snapshots reused across the 25 menus of each history pair. 25 pairs use the freshly constructed originals; prefixes are not counted 625 times.')
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,default=Path(__file__).with_name('feedback_graph_results.json'));o=a.parse_args()
    r=run();o.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(r['counts'],r['finite_optima'])
