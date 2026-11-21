"""A real intervening writer with private observations: five-cycle update and certificate repair."""
import argparse,json,sys
from pathlib import Path
from collections import Counter
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent))
from projected.kernel.subset_kernel import prefix,initial,marker_slot,least_one,core
from adaptive.graph.feedback_graph import V,E,fcol,audit,suffix,single_policy,partition
F={'identity':tuple(V),'rotation':(1,2,3,4,0),'reflection':(0,4,3,2,1),'doubling':(0,2,4,1,3)}
proper=(0,1,0,1,2)
codes={0:(0,0,0,0,0),1:(0,1,0,1,0),2:(0,1,2,3,0),3:(0,1,2,3,4)}
def read_vertex(p,i):return p.probe(marker_slot(i+1),least_one(i+1))
def rewrite(p,M):
    start=p.cost;before=p.probes
    bits=[read_vertex(p,i) for i in V]
    assert sum(bits)==1;old=bits.index(1);new=M[old]
    meter=[p.cost-start]
    # The writer learned its old world through the real marker readings alone.
    for j in range(1,11):p.drop(marker_slot(j))
    assert not any(p.codes())
    meter.append(p.cost-start-sum(meter));ops=[]
    for j in range(1,11):
        dest=marker_slot(j) if (fcol(j)>>new)&1 else 14
        oldp=p.cost
        k=p.round(0,dest,j)
        assert k==j and p.events[-1]['business_words']
        b=p.events[-1]['business_words']
        p.drop(14)
        ops.append((dest,k,tuple(b),p.cost-oldp))
    meter.append(p.cost-start-sum(meter))
    assert p.probes-before==5 and p.codes()==(0,0,0)+tuple(j if (fcol(j)>>new)&1 else 0 for j in range(1,11))+(0,0)
    return dict(old=old,new=new,cost=p.cost-start,parts=meter,readings=bits,binds=ops)
def runone(C,h,e,kind,code):
    p=prefix(C,initial(h),route=fcol);initial_cost=p.cost
    observed=sum(int(p.events[i]['present'])<<i for i in range(3));msg=code[observed]
    w=rewrite(p,F[kind])
    assert w['old']==h and w['new']==F[kind][h]
    # No writes, traversal/arithmetic traces or writer answers reach the decoder.
    # Only public named map, old message, future edge and actual first delivery.
    new_code=tuple(code[F[kind].index(x)] for x in V)
    p.events=[]
    result=suffix(p,F[kind][h],e,msg,single_policy(new_code))
    assert result['pre']==initial_cost+w['cost'] and (result['first'], result['second'])==audit(e,F[kind][h])
    return dict(h=h,edge=e,actual_new=F[kind][h],map=kind,old_message=msg,prefix=initial_cost,writer_paid=w['cost'],writer_parts=w['parts'],
                mandatory_copy=result['copy_then_clear'],first=result['first'],second=result['second'],supplements=result['supplements'],total=result['total'])
def run():
    C=core.prior.Compiler(slots=15);autos={}
    for name in ('identity','rotation','reflection'):
        paths=[runone(C,h,e,name,proper)for h in V for e in V]
        assert all(not r['supplements'] for r in paths)
        autos[name]=paths
    mixed={};allpaths=[r for v in autos.values()for r in v]
    for s,c in codes.items():
        paths=[runone(C,h,e,name,c)for name in ('identity','doubling')for h in V for e in V]
        for r in paths:
            h=r['actual_new'];u,v=E[r['edge']];M=F[r['map']]
            assert len(r['supplements'])==int(h in (u,v) and c[M.index(u)]==c[M.index(v)])
        classes=Counter(c);expected=sum(k*(k-1) for k in classes.values())
        assert sum(len(r['supplements']) for r in paths)==[20,8,2,0][s]==expected
        # Every nonzero supplementary read is an original 8-command word.
        mixed[s]=dict(code=c,messages=len(classes),total_reads=expected,worst_reads=max(len(r['supplements']) for r in paths),worst_total=max(r['total']for r in paths),paths=paths)
        allpaths+=paths
    witnesses=[runone(C,h,4,'doubling',proper)for h in (0,2)]
    assert [r['first'] for r in witnesses]==[11,11] and [r['second']for r in witnesses]==[5,11]
    assert [r['old_message']for r in witnesses]==[0,0] and all(len(r['supplements'])==1 for r in witnesses)
    assert len({r['prefix'] for r in allpaths+witnesses})==1 and len({r['writer_paid'] for r in allpaths+witnesses})==1
    # Verify *every* partition of 5 old histories with <=2^s messages independently.
    best={}
    for s in range(4):
        summaries=list(partition(5,1<<s))
        def forced(c):
            return sum(2*(c[F[kind].index(u)]==c[F[kind].index(v)])for kind in ('identity','doubling')for u,v in E)
        best[s]=min(forced(c) for c in summaries)
        assert best[s]==mixed[s]['total_reads']
    sample=prefix(C,initial(2),route=fcol);audit_writer=rewrite(sample,F['doubling'])
    return dict(status='PASS',inventory=dict(slots=C.slots,members=C.members,candidates=len(C.H)),
                original_complete_paths=len(allpaths)+len(witnesses),independent_extra_writer_audit=1,
                public_maps=F,proper_color=proper,prefix_cost=allpaths[0]['prefix'],writer_cost=allpaths[0]['writer_paid'],
                writer_word_costs=allpaths[0]['writer_parts'],sample_writer=audit_writer,
                old_three_color_auto=autos,late_id_or_double=mixed,partition_minima=best,stale_witness=witnesses,
                scope='Mandatory rewrite sees five paid, private vertex observations; F is announced to resumed decoder. Sums minimized over the 50 equally counted (old,edge,map) scenarios, not per-run worst charges or expectations under another prior.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'phase_results.json');a=ap.parse_args()
    d=run();a.out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
    print('PASS',d['original_complete_paths'],d['prefix_cost'],d['writer_cost'],d['writer_word_costs'],[(s,v['total_reads'],v['worst_total']) for s,v in d['late_id_or_double'].items()])
