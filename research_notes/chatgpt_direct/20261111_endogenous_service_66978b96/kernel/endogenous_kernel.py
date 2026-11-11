"""Real BRC copies and writes; second list consumes first original bind's delivered code."""
import argparse,json,sys
from functools import cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent))
from projected.kernel.subset_kernel import core, prefix,initial,emit,marker_slot,least_one,Recorder
BACK=11
FULL=255
def worlds(u):return [h for h in range(8) if u>>h&1]
def f(kind,j,h):
    if kind=='mux':return (h>>(j-1))&1 if j<=3 else 0
    if j==1:return int(h.bit_count()>=2)
    if j<8:return int(h==[1,2,4,6,5,3][j-2])
    return h>>(j-8)&1
def route(kind):
    return lambda j:sum(1<<h for h in range(8) if f(kind,j,h))
def suffix(kind,first):
    assert first in (1,BACK)
    if kind=='mux':return (2,) if first==1 else (3,)
    return (2,3,4) if first==1 else (5,6,7)
def output(kind,h,union=False):
    g=f(kind,1,h);first=BACK if g else 1
    if union:return tuple(f(kind,j,h) for j in (range(1,4) if kind=='mux' else range(1,8)))
    return (first,)+tuple(BACK if f(kind,j,h) else j for j in suffix(kind,first))
def advice(h,s):
    # Function of the actual 3 prefix guard responses, before forgetting. Intentional
    # first s bits of the realised (selector, selected data), with a third unused bit
    # when asked to preserve all 3 for the union comparator below.
    return ((h&1,h>>(2 if h&1 else 1)&1,(h>>(1 if h&1 else 2))&1)[:s])
def union_advice(h,s):return tuple((h>>j)&1 for j in range(s))
def price(k):return 97+2*k.bit_count()+4*int(not k&8)
def policy(kind,mode,bycost,delay):
    mask=route(kind);un=(mode=='union')
    @cache
    def val(u,t,delivered):
        # Charge actual business at terminal, irrespective of union acquisition.
        if len({output(kind,h,un) for h in worlds(u)})==1:
            assert len({output(kind,h) for h in worlds(u)})==1
            h=worlds(u)[0];return (sum(price(k) for k in output(kind,h)) if bycost else 0,0,0)
        sels={f(kind,1,h) for h in worlds(u)}
        resolved=len(sels)==1 or delivered
        if not resolved and t==0:return (10**8,0,0)
        opts=[]
        for j in range(1,11):
            lo=u&~mask(j);hi=u&mask(j)
            if lo and hi:
                z=val(lo,max(0,t-1),resolved);o=val(hi,max(0,t-1),resolved)
                opts.append(((8 if bycost else 1)+max(z[0],o[0]),1+max(z[1],o[1]),j))
        return min(opts)
    return val

def runone(C,kind,mode,s,h,deadline,rec=False,bycost=True):
    support=route(kind);p=prefix(C,initial(h),support,record=rec);pre=p.cost
    before=p.codes()
    # Real guard outputs, distinct from harness input, supply permitted advice.
    observed=sum(int(p.events[i]['present'])<<i for i in range(3))
    enc=union_advice if mode=='union' else advice
    if s and kind!='mux': raise ValueError
    msg=enc(observed,s)
    U=sum(1<<v for v in range(8) if enc(v,s)==msg)
    def read(j):return p.probe(marker_slot(j),least_one(j))
    def business(k):return emit(p,[k])[0]
    # Begin policy boundary: receives public U, scripts, hook for a single physical bit
    # and hook for an actual original program delivery. Audit data/prefix aren't read.
    def operate(U,read,business):
        tree=policy(kind,mode,bycost,deadline)
        t=deadline;first=None;next_list=None;trace=[];jobs=[];reads_at_first=None
        while True:
            poss=worlds(U)
            selectors={BACK if f(kind,1,v) else 1 for v in poss}
            if first is None and len(selectors)==1 and (mode!='union' or len({output(kind,v,True) for v in poss})==1):
                job=business(next(iter(selectors)))
                jobs.append(job);first=job['bind_delivered'];reads_at_first=len(trace)
                next_list=suffix(kind,first) # ONLY the actual returned original bind code
            outputs={output(kind,v,mode=='union') for v in poss}
            if len(outputs)==1:break
            _,_,j=tree(U,t,first is not None);prior=U;r=read(j)
            U=U&support(j) if r else U&~support(j);t=max(t-1,0)
            trace.append(dict(marker=j,answer=r,prior=worlds(prior),posterior=worlds(U)))
        assert first is not None and next_list==suffix(kind,first)
        for j in next_list:
            outcomes={BACK if f(kind,j,v) else j for v in worlds(U)};assert len(outcomes)==1
            job=business(next(iter(outcomes)));jobs.append(job)
        return U,trace,jobs,next_list,reads_at_first
    U,trace,jobs,T,reads1=operate(U,read,business)
    assert U>>h&1 and p.codes()==before
    if mode!='union':assert reads1<=deadline
    seq=tuple(j['bind_delivered'] for j in jobs);assert seq==output(kind,h)
    assert len(trace)==p.probes and p.cost==pre+8*len(trace)+sum(price(k) for k in seq)
    for job,k in zip(jobs,seq):assert sum(job['words'])==price(k)
    return dict(h=h,message=msg,prefix=pre,queries_before_first=reads1,actual_first=jobs[0]['bind_delivered'],
                active_second_list=T,deliveries=seq,queries=trace,posteriors=worlds(U),service_jobs=jobs,
                total=p.cost,paid_probes=len(trace),**({'word':p.packed()} if isinstance(p,Recorder) else {}))

def run():
    C=core.prior.Compiler(slots=15);groups=[]
    for kind in ('mux','majority'):
        cases=([(mode,s,8) for s in range(4) for mode in ('actual','union')] if kind=='mux' else
               [('actual',0,d) for d in (1,2,3)]+[('union',0,8)])
        for mode,s,deadline in cases:
            data=[runone(C,kind,mode,s,h,deadline,rec=(kind=='majority' and h==2 and mode=='actual' and deadline in (1,3))) for h in range(8)]
            enc=union_advice if mode=='union' else advice
            cells={tuple(enc(h,s)):sum(1<<v for v in range(8) if enc(v,s)==enc(h,s)) for h in range(8)}
            d=max(policy(kind,mode,False,deadline)(u,deadline,False)[0] for u in cells.values())
            w=max(policy(kind,mode,True,deadline)(u,deadline,False)[0] for u in cells.values())+2346
            assert max(z['total'] for z in data)==w
            assert max(z['paid_probes'] for z in data)==d
            assert d==(max(0,(3 if mode=='union' else 2)-s) if kind=='mux' else 4 if deadline<3 else 3)
            groups.append(dict(kind=kind,mode=mode,s=s,deadline=deadline,optimal_read_depth=d,optimal_total_for_given_code=w,paths=data))
    return dict(status='PASS',original_runs=sum(len(g['paths']) for g in groups),inventory=dict(slots=C.slots,members=C.members,relations=len(C.H)),groups=groups,
                cost_scope='Exact command tree for given advice map; mux proof by saturated leaves plus 206..208 service-price range makes these total optima over all allowed advice. Union solves a stronger information requirement and emits only realized business.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'endogenous_kernel_results.json');a=ap.parse_args();data=run()
    a.out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n');print('PASS',data['original_runs']);print([(z['kind'],z['mode'],z['s'],z['deadline'],z['optimal_read_depth'],z['optimal_total_for_given_code'])for z in data['groups']])
