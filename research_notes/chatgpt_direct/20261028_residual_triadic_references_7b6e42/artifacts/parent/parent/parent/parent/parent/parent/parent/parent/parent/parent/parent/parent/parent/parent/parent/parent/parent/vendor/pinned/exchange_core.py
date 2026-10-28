"""Same-occupancy fibers, legal exchanges, and transient vacancy in pinned BRC.

Finite reservation-model results, not a native force/geometry law. All
preparations, compatible products and executed transitions use inherited CWM
BRC. Graph reachability uses its explicitly typed Boolean-support observer.
No old main is run. Atomic exchange is a boundary relation; its compiled
release/reserve word may change intermediate occupancy.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from collections import deque
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path

ROOT=Path(__file__).resolve().parent
P=ROOT/'prior/check_membership.py'
if not P.exists(): P=ROOT.parent/'20261008_residual_membership_7c2e8a/check_membership.py'
raw=P.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='be1b60446e31c2c8489d1ce0db16cc1e952d11c8':
    raise RuntimeError('membership source mismatch')
spec=importlib.util.spec_from_file_location('exchange_membership',P)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
s,r=m.s,m.r
CHECKS=0;STEPS=0

def ck(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def cw(x): return dict(C=x.count,W=str(x.total),M=str(x.dominant))
def put(d,k,w): d[k]=r.merge(d.get(k,r.brc.CWM_ZERO),w)
def prep(J): return m.active_monomial(J,Q(1))

def catalog(H):
    H=tuple(sorted(set(tuple(sorted(h)) for h in H)))
    I=frozenset().union(*map(frozenset,H))
    events=tuple(s.TestEvent(str(i),frozenset(h),r.brc.CWM_ONE) for i,h in enumerate(H))
    poly=s.assemble(events,I)
    out={}
    for (selected,U),w in poly.items():
        J=m.canon(H[int(i)] for i in selected)
        ck(m.used(J)==U,'catalog retains exact occupancy')
        put(out,J,w)
    return I,out

def step(J,op,H):
    global STEPS
    if op[0] not in ('release','reserve'): raise ValueError('unknown command')
    if op[0]=='reserve' and tuple(sorted(op[1])) not in H: raise ValueError('event outside declared library')
    STEPS+=1
    out,delta,ok=m.full_step(J,op)
    return out,delta,ok

def run(J,word,H):
    w=prep(J);I=m.used(J);trace=[];deficits=[0];start=J
    for op in word:
        old=J;J,delta,ok=step(J,op,H);w=r.serial(w,r.brc.CWM_ONE)
        ck(m.used(J)<=I,'compiled word stays in declared initial inventory')
        deficit=len(I)-len(m.used(J));deficits.append(deficit)
        trace.append(dict(command=op,before=old,after=J,success=ok,vacancy=deficit))
    return dict(start=start,end=J,word=word,steps=len(word),peak_vacancy=max(deficits),
                vacancy_trace=deficits,CWM=cw(w),trace=trace)

def project_static(poly):
    out={}
    for (J,U),w in poly.items():put(out,U,w)
    return out

def occupancy_product(a,b):
    out={}
    for U,u in a.items():
        for V,v in b.items():
            if not U&V:put(out,U|V,r.serial(u,v))
    return out

def test_projection():
    H=((1,7,13),(2,19,25),(1,7,19),(2,13,25),(3,31,32))
    E=[s.TestEvent(str(i),frozenset(h),r.brc.CWM_ONE) for i,h in enumerate(H)]
    samples=[{s.EMPTY:r.brc.CWM_ONE}]+[s.factor(e) for e in E]
    samples+=[s.assemble(E,frozenset().union(*(e.occurrences for e in E)))]
    tests=0
    for a in samples:
        for b in samples:
            ck(project_static(s.times(a,b))==occupancy_product(project_static(a),project_static(b)),
               'static positive-BRC occupancy projection preserves compatible product')
            tests+=1
    left=m.canon((H[0],H[1],H[4]));right=m.canon((H[2],H[3],H[4]))
    ck(m.used(left)==m.used(right),'old complementary boundary occupancy')
    word=[('release',1),('release',2),('reserve',H[2]),('reserve',H[3])]
    out=run(left,word,set(map(tuple,map(sorted,H))))
    ck(out['end']==right and out['peak_vacancy']==6,'two-event relation compiled with six-vacancy peak')
    return dict(product_cases=tests,old_complementary_exchange=out,
                projection_scope='static compatible assembly; not release-compatible quotient')

def support_reachability(H,start,target,max_vacancy):
    """Exact finite Boolean-support closure, not a law of all path weights."""
    I=m.used(start);q=deque([start]);seen={start};parents={};edge_count=0
    seed=prep(start);unit=r.brc.CWM_ONE
    while q:
        J=q.popleft()
        commands=[('release',min(h)) for h in J]+[('reserve',h) for h in H]
        for op in commands:
            nxt,_,ok=step(J,op,set(H))
            weight=r.serial(unit,r.brc.CWM_ONE)
            edge_count+=1
            # Occupancy threshold is a declared reachability question.
            if len(I)-len(m.used(nxt))>max_vacancy:continue
            if r.brc.boolean_support(weight) and nxt not in seen:
                seen.add(nxt);parents[nxt]=(J,op);q.append(nxt)
    path=[]
    if target in seen:
        cur=target
        while cur!=start:cur,op=parents[cur];path.append(op)
        path.reverse()
    return dict(reachable=target in seen,states=len(seen),edges_examined=edge_count,
                max_vacancy=max_vacancy,shortest_word=path,
                scope='Boolean support; visited-set reduction preserves reachability only')

def grid_case():
    A=((1,2,3),(4,5,6),(7,8,9));B=((1,4,7),(2,5,8),(3,6,9));H=A+B
    I,p=catalog(H);fiber=[J for J in p if m.used(J)==I]
    ck(set(fiber)=={m.canon(A),m.canon(B)},'grid has exactly two saturated states')
    ck(len(set(A)-set(B))==3,'grid balanced exchange replaces three events')
    lower=support_reachability(H,m.canon(A),m.canon(B),6)
    upper=support_reachability(H,m.canon(A),m.canon(B),9)
    ck(not lower['reachable'] and upper['reachable'],'nine-vacancy barrier certified by full support search')
    out=run(m.canon(A),upper['shortest_word'],set(H))
    ck(out['steps']==6 and out['peak_vacancy']==9,'grid minimum command and vacancy witness')
    # All complete reserve-only orders still have identical full occupancy.
    law={};weight=r.edge(Q(1,720));orders=0
    for order in permutations(H):
        J=();w=weight
        for h in order:J,_,_=step(J,('reserve',h),set(H));w=r.serial(w,r.brc.CWM_ONE)
        ck(J in fiber,'every grid order ends in one full-occupancy partition')
        put(law,J,w);orders+=1
    ck(all(v.count==360 and v.total==Q(1,2) for v in law.values()),'symmetric order multiplicities retained')
    return dict(events=H,all_assemblies=len(p),saturated_states=fiber,exchange_degree=3,
                below_barrier=lower,at_barrier=upper,optimal_compiled_trace=out,
                complete_orders=orders,order_law=[dict(J=J,CWM=cw(v)) for J,v in sorted(law.items())])

def cyclic(n):
    if n<3:raise ValueError('n>=3')
    A=tuple(tuple(3*i+k+1 for k in range(3)) for i in range(n))
    B=tuple(tuple(sorted((3*j+1,3*((j-1)%n)+2,3*((j-2)%n)+3))) for j in range(n))
    return A,B

def test_cycles():
    rows=[]
    for n in range(3,13):
        A,B=cyclic(n);H=A+B;start=m.canon(A);target=m.canon(B)
        # Rolling vacancy, never a new primitive operation.
        word=[('release',min(A[i])) for i in range(3)]+[('reserve',B[2])]
        for i in range(3,n):word += [('release',min(A[i])),('reserve',B[i])]
        word += [('reserve',B[0]),('reserve',B[1])]
        out=run(start,word,set(H))
        ck(out['end']==target,'rolling route reaches other saturated phase')
        ck(out['steps']==2*n and out['peak_vacancy']==9,'size-independent exact vacancy and size-dependent commands')
        ck(all(len(set(b)&set(a))<=1 for a in A for b in B),'each new event meets three distinct old events')
        row=dict(n=n,inventory_size=3*n,events=H,atomic_exchange_size=n,
                 optimal_peak_vacancy=9,minimum_commands=2*n,rolling_route=out)
        if n<=8:
            I,p=catalog(H);by_occ={}
            for J,v in p.items():by_occ.setdefault(m.used(J),[]).append(J)
            collisions=[js for U,js in by_occ.items() if len(js)>1]
            ck(len(collisions)==1 and set(collisions[0])=={start,target},'only occupancy collision is entire balanced cycle')
            ck(len(set(start)-set(target))==n,'no proper fixed-occupancy exchange')
            row.update(all_assemblies=len(p),fiber_size=2,all_occupancy_collisions=collisions)
        if n<=5:
            low=support_reachability(H,start,target,6)
            high=support_reachability(H,start,target,9)
            ck(not low['reachable'] and high['reachable'],'threshold barrier independently checked by support closure')
            ck(len(high['shortest_word'])==2*n,'exact shortest compiled path')
            row.update(below_barrier=low,at_barrier=high)
        rows.append(row)
    return rows

def pair_exchange(J,old,new,H):
    old=m.canon(old);new=m.canon(new)
    ck(len(old)==len(new)==2,'pair macro replaces two triples')
    ck(set(old)<=set(J),'old events present')
    ck(m.used(old)==m.used(new) and len(m.used(new))==6,'same six distinct occurrences')
    expected=m.canon((set(J)-set(old))|set(new))
    word=[('release',min(h)) for h in old]+[('reserve',h) for h in new]
    out=run(J,word,H)
    ck(out['end']==expected and out['peak_vacancy']==6,'macro correctly compiles using old kernel')
    return expected,out

def transform_complete(start,target,H):
    J=start;macros=[];fixed=set()
    for T in target:
        if T not in J:
            touched=[h for h in J if set(h)&set(T)]
            ck(len(touched) in (2,3),'missing target block intersects two or three current blocks')
            if len(touched)==3:
                x,y,z=T
                A=next(h for h in touched if x in h);B=next(h for h in touched if y in h)
                U=set(A)|set(B);extra=min(U-{x,y});N=tuple(sorted((x,y,extra)))
                J,out=pair_exchange(J,(A,B),(N,tuple(sorted(U-set(N)))),H);macros.append(out)
            touched=[h for h in J if set(h)&set(T)]
            U=set().union(*map(set,touched))
            J,out=pair_exchange(J,touched,(T,tuple(sorted(U-set(T)))),H);macros.append(out)
        fixed.add(T);ck(fixed<=set(J),'already fixed target blocks remain intact')
    ck(J==target and len(macros)<=2*(len(start)-1),'complete library pair exchanges connect within proved bound')
    return dict(start=start,target=target,macro_count=len(macros),macros=macros)

def complete_cases():
    results=[]
    for size in (6,9):
        H=tuple(combinations(range(1,size+1),3));I,p=catalog(H)
        fiber=tuple(sorted(J for J in p if m.used(J)==I))
        start=m.canon(tuple(range(i,i+3)) for i in range(1,size+1,3))
        paths=[transform_complete(start,J,set(H)) for J in fiber]
        ck(len(fiber)==(10 if size==6 else 280),'complete fiber size from original BRC enumerator')
        total=r.total(p[J] for J in fiber)
        results.append(dict(occurrences=size,fiber_size=len(fiber),fiber_CWM=cw(total),
                            paths=paths,max_constructed_macro_count=max(x['macro_count'] for x in paths)))
    return results

def main():
    a=test_projection();b=grid_case();c=test_cycles();d=complete_cases()
    result=dict(schema='EM_RESIDUAL_EXCHANGE_FIBER_V1',
                event_id='EM-20261010-RESIDUAL-EXCHANGE-FIBER-7C2E8A',
                status='CONDITIONAL_EXECUTED_BRC_UNREVIEWED',
                global_read='cfa5ceb7a48aae08b1e4c10a877327947d8ebe8e',
                source_read='a297578f23b36d9e1cc4fe38389681a104213973',
                static_projection=a,grid_three_event_obstruction=b,cyclic_family=c,
                complete_library_connectivity=d,assertions=CHECKS,full_step_calls=STEPS,
                inherited_helper_checks=m.CHECKS,BRC_calls=dict(r.CALLS),
                scope=dict(native_mapping_supplied=False,independent_review=False,
                           physical_time_energy_or_six_axes=False,old_main_suites_executed=False,
                           counts_are_model_occurrences_and_commands=True),
                activity_id=None,registration='PENDING_PREVIOUS_PLATFORM_DENIAL_NOT_REPLAYED')
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    summary={k:result[k] for k in ('event_id','status','assertions','full_step_calls','inherited_helper_checks','BRC_calls')}
    summary.update(grid_fiber_size=len(b['saturated_states']),grid_all_orders=b['complete_orders'],
                   cyclic_n_checked=[x['n'] for x in c],full_cyclic_catalogs=[x['n'] for x in c if 'all_assemblies' in x],
                   complete_fibers=[x['fiber_size'] for x in d],
                   output_bytes=len(data),output_sha256=hashlib.sha256(data).hexdigest())
    (ROOT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
