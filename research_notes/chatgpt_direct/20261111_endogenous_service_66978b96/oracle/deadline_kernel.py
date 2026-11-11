"""Seven original slots. A real delivered complete key selects the second list."""
import argparse,json,sys
from pathlib import Path
from functools import cache
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from copylife.kernel_checks import Physical,core
from projected.kernel.subset_kernel import emit
sel,a,b=1,2,3;backup=4
def mark(j,h):
    return int(h==3) if j==sel else ((h>>(j-a))&1)
def bit(j):return (j&-j).bit_length()-1
def prepare(C,h_input):
    P=Physical(C,[(h_input>>i)&1 for i in range(2)]+[1,2,3,0,0])
    h=0
    for i in range(2):
        P.drop(i);h|=int(C.observe_result(P.J))<<i
    for j in (sel,a,b):
        i=j+1
        assert P.copy(5,i)==j;P.drop(i);assert P.copy(6,5)==j
        assert P.copy(i if mark(j,h) else 6,5)==j;P.drop(5);P.drop(6)
    return P
def serve(read,create,mode):
    H=list(range(4));schedule=[]
    def q(j):
        ans=read(j);H[:]=[h for h in H if mark(j,h)==ans];schedule.append(dict(probe=j,reply=ans))
    def vals(j):return {mark(j,h) for h in H}
    if mode=='early':q(sel)
    elif mode=='joint':
        q(a)
        if len(vals(sel))>1:q(b)
    else:raise ValueError(mode)
    assert len(vals(sel))==1
    first=backup if vals(sel)=={1} else sel
    before_first=len(schedule);got=create(first)
    schedule.append(dict(preferred=sel,delivered=got))
    if got==sel:next_demand=(a,b)
    elif got==backup:next_demand=(a,)
    else:raise AssertionError('unreachable actual first delivery')
    for j in next_demand:
        if len(vals(j))>1:q(j)
        requested=backup if vals(j)=={1} else j
        delivered=create(requested);schedule.append(dict(preferred=j,delivered=delivered))
    return dict(stage_latency=before_first,route=next_demand,operations=schedule)
def once(C,h,mode):
    P=prepare(C,h);prefix=P.cost;start=P.codes();ev=[]
    def read(j):return P.probe(j+1,bit(j))
    def create(k):
        row=emit(P,(k,))[0];ev.append(row)
        return row['bind_delivered']
    o=serve(read,create,mode)
    expect=(a,b) if h!=3 else (a,)
    assert o['route']==expect and P.codes()==start and prefix+8*P.probes+sum(sum(r['words']) for r in ev)==P.cost
    assert [row['bind_delivered'] for row in ev]==[backup if mark(j,h) else j for j in (sel,*expect)]
    return dict(**o,h=h,mode=mode,prefix=prefix,reads=P.probes,commands=P.cost,business=P.cost-prefix-8*P.probes,real_deliveries=ev)
def run():
    C=core.prior.Compiler(slots=7)
    rows=[once(C,h,mode) for h in range(4) for mode in ('early','joint')]
    assert len(set(p['prefix'] for p in rows))==1
    # Weighted oracle enumerates first queries/deadline, with the exact irreversible
    # service charges supplied by real execution. Determined business receipts
    # reveal only a key already certified, so no paid data can be extracted from them.
    leaf=[rows[2*h]['business'] for h in range(4)]
    @cache
    def V(H,L):
        if len(H)==1:return leaf[H[0]]
        fixed_first=len({mark(sel,h) for h in H})==1
        if L==0 and not fixed_first:return 10**8
        cand=[]
        for j in (sel,a,b):
            X=tuple(h for h in H if mark(j,h));Y=tuple(h for h in H if not mark(j,h))
            if X and Y:cand.append(8+max(V(X,L-1 if L>0 else L),V(Y,L-1 if L>0 else L)))
        return min(cand)
    summary={}
    for mode,L,dt in [('early',1,3),('joint',2,2)]:
        z=[r for r in rows if r['mode']==mode]
        t=max(r['commands'] for r in z)
        summary[mode]=dict(maximum_reads=max(r['reads'] for r in z),maximum_latency=max(r['stage_latency'] for r in z),
                           worst_commands=t,certified_minimax_commands=rows[0]['prefix']+V(tuple(range(4)),L))
        assert summary[mode]['maximum_reads']==dt and summary[mode]['maximum_latency']==L
        assert t==summary[mode]['certified_minimax_commands']
    return dict(status='PASS',unit='one slot bit = eight original commands; counts include prefix, not admission',slots=C.slots,members=C.members,relations=len(C.H),raw_runs=8,summary=summary,paths=rows)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('deadline_kernel_results.json'));a0=p.parse_args()
    out=run();a0.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(out['summary'])
