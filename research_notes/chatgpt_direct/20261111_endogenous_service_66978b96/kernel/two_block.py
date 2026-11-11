"""Two independently marked majority gadgets, 28-slot original BRC; sealed actual deliveries."""
import argparse,json,sys
from functools import cache
from itertools import product
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent))
from adaptive.kernel.endogenous_kernel import core,f,emit
from copylife.kernel_checks import Physical
from adaptive.kernel.product_deadline import rows,maj
from adaptive.kernel.endogenous_kernel import worlds
B=2;BACK=21
def mask(j):return (j&-j).bit_length()-1
def key(g,j):return 10*g+j
def slot(k):return 5+k
def prefix(C,prep):
    guards=[(v>>i)&1 for v in prep for i in range(3)]
    p=Physical(C,tuple(guards)+tuple(range(1,21))+(0,0))
    obs=[0,0]
    for i in range(6):
        p.drop(i);obs[i//3]|=int(C.observe_result(p.J))<<(i%3)
    for g in range(2):
        for j in range(1,11):
            k=key(g,j);s=slot(k);temp=26;waste=27
            assert p.copy(temp,s)==k;p.drop(s);assert p.copy(waste,temp)==k
            assert p.copy(s if f('majority',j,obs[g]) else waste,temp)==k
            p.drop(temp);p.drop(waste)
    assert p.codes()==(0,)*6+tuple(key(g,j) if f('majority',j,obs[g]) else 0 for g in range(2) for j in range(1,11))+(0,0)
    return p
def route(g,k):
    assert k in (key(g,1),BACK)
    return (2,3,4) if k==key(g,1) else (5,6,7)
def policy(fully,read,serve):
    recovered=[None,None];sel=[];actual=[];routes=[];logs=[];calls=0
    def take(g,j):
        nonlocal calls
        calls+=1
        ans=read(key(g,j));logs.append([g,j,ans]);return ans
    for g in range(2):
        if g<fully:
            recovered[g]=sum(take(g,j)<<(j-8) for j in range(8,11));a=f('majority',1,recovered[g])
        else:a=take(g,1)
        out=serve(BACK if a else key(g,1));sel.append(out)
        routes.append(route(g,out));actual.append(out) # only real bind receipt feeds suffix list
    before=calls
    for g,js in enumerate(routes):
        if recovered[g] is None:
            # Three permitted digits recover this half; every allowed query isolates a single
            # nonbaseline vertex within it, so some physical world requires all three.
            recovered[g]=sum(take(g,j)<<(j-8) for j in range(8,11))
        for j in js:actual.append(serve(BACK if f('majority',j,recovered[g]) else key(g,j)))
    return dict(selectors=sel,activated_lists=routes,deliveries=actual,probes=logs,prequeries=before,queries=calls)
def physical(C,h,t):
    p=prefix(C,h);pre=p.cost;start=p.codes();charged=[]
    def serve(k):
        job=emit(p,[k])[0];charged.append(sum(job['words']));return job['bind_delivered']
    out=policy(t,lambda k:p.probe(slot(k),mask(k)),serve)
    expect=[BACK if f('majority',1,h[g]) else key(g,1) for g in range(2)]
    for g in range(2):expect.extend(BACK if f('majority',j,h[g]) else key(g,j) for j in route(g,expect[g]))
    assert out['deliveries']==expect and p.codes()==start
    assert out['prequeries']==2+2*t and out['queries']==8-t and p.cost==pre+8*out['queries']+sum(charged)
    return dict(h=h,early_blocks=t,prefix=pre,original_business=charged,total=p.cost,**out)
def optimal_tree(base):
    @cache
    def val(U,t):
        if all(u.bit_count()==1 for u in U):return (base[tuple(worlds(u)[0] for u in U)],0,-1,-1)
        known=all(not(u&maj and u&~maj) for u in U)
        if t<=0 and not known:return (10**8,0,-1,-1)
        opts=[];t=max(t-1,0)
        for g,u in enumerate(U):
            for j,m in enumerate(rows,1):
                lo=u&~m;hi=u&m
                if not lo or not hi:continue
                a=val(U[:g]+(lo,)+U[g+1:],t);b=val(U[:g]+(hi,)+U[g+1:],t)
                opts.append((8+max(a[0],b[0]),1+max(a[1],b[1]),g,j))
        return min(opts)
    return val
def physical_opt(C,h,lim,tree):
    p=prefix(C,h);pre=p.cost;start=p.codes();U=(255,255);t=lim;trace=[];service=[];js=[];when=[]
    def serve(k):
        receipt=emit(p,[k])[0];service.append(receipt);return receipt['bind_delivered']
    while True:
        while len(js)<2:
            g=len(js);v={f('majority',1,x) for x in worlds(U[g])}
            if len(v)!=1:break
            d=serve(BACK if next(iter(v)) else key(g,1));js.append(route(g,d));when.append(len(trace))
        _,_,g,j=tree(U,t)
        if g<0:break
        k=key(g,j);ans=p.probe(slot(k),mask(k));trace.append([g,j,ans])
        sub=(U[g]&rows[j-1]) if ans else (U[g]&~rows[j-1]);assert 0<sub<U[g];U=U[:g]+(sub,)+U[g+1:];t=max(0,t-1)
    assert len(js)==2 and when[-1]<=lim
    for g,group in enumerate(js):
        assert U[g].bit_count()==1;source=worlds(U[g])[0]
        for j in group:serve(BACK if f('majority',j,source) else key(g,j))
    expected=[BACK if f('majority',1,h[g]) else key(g,1) for g in range(2)]
    for g in range(2):expected.extend(BACK if f('majority',j,h[g]) else key(g,j) for j in route(g,expected[g]))
    assert [j['bind_delivered'] for j in service]==expected and p.codes()==start
    assert p.cost-pre==8*len(trace)+sum(sum(j['words']) for j in service)
    return dict(h=h,deadline=lim,pre=pre,service=service,trace=trace,first_receipt_read_indices=when,routes=js,paid_reads=len(trace),total=p.cost)

def run():
    C=core.prior.Compiler(slots=28)
    cases=[physical(C,h,t) for h in product(range(8),repeat=2) for t in range(3)]
    base={tuple(r['h']):r['total']-r['prefix']-8*r['queries'] for r in cases}
    assert len(base)==64
    mincost=optimal_tree(base);optvals={a:mincost((255,255),a)[0]+5322 for a in range(2,7)}
    extra=[physical_opt(C,h,5,mincost) for h in product(range(8),repeat=2)]
    assert max(r['total'] for r in extra)==optvals[5]
    assert max(r['paid_reads'] for r in extra)==7
    for a,t in ((2,0),(3,0),(4,1),(6,2)):assert max(r['total'] for r in cases if r['early_blocks']==t)==optvals[a]
    return dict(status='PASS',optimal_worst_total_by_deadline=optvals,weighted_bound_attaining_runs=extra,inventory=dict(slots=C.slots,colors=C.colors,members=C.members,relations=len(C.H)),original_runs=len(cases)+len(extra),
        common_prefix=sorted({r['prefix']for r in cases}),worst_original_commands_for_attaining_read_policy={t:max(r['total']for r in cases if r['early_blocks']==t)for t in range(3)},cases=cases,
        scope='All 64 worlds: 3 simple read-frontier attaining policies plus separate 5-read deadline exact minimum total command tree. Leaf service costs come from raw fixed business; deadline 3 uses the deadline-2 optimal tree.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'two_block_results.json');a=p.parse_args()
    d=run();a.out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(d['inventory'],d['original_runs'],d['common_prefix'],d['worst_original_commands_for_attaining_read_policy'])
