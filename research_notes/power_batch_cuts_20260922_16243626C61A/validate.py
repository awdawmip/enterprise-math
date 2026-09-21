"""Bounded checks and cost accounting. Run with PYTHONPATH=src; no network."""
from collections import Counter
from pathlib import Path
import argparse, gc, hashlib, importlib.util, json, platform, random, statistics, sys, time, tracemalloc
from math import gcd, isqrt
from enterprise_math.group_ring_batch_response import window_responses, dyadic_cut_responses, compile_terminal_index
from enterprise_math.group_ring_terminal_response import terminal_responses, suffix_responses, cyclic_terminal_value

ROOT=Path(__file__).resolve().parents[2]
SPEC=importlib.util.spec_from_file_location('old_validation',ROOT/'research_notes/power_terminal_moments_20260921_16243626C61A/validate.py')
OLD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(OLD)


def classical_prepare(n,a,states):
    """Independently computed order + shared conventional BSGS discrete logs.

    Neither true order nor exponent labels are input. Cost includes solving
    order, building the log table, and membership/log lookup for all states.
    """
    r=OLD.adaptive_bsgs_order(n,a)
    targets=sorted(set(u for u in states if gcd(u,n)==1))
    B=min(r,isqrt(max(1,len(targets))*r)+1)
    baby={}; z=1
    for j in range(B): baby[z]=j; z=z*a % n
    step=pow(z,-1,n); logs={}
    for u in targets:
        v=u
        for i in range((r-1)//B+1):
            j=baby.get(v)
            if j is not None and i*B+j<r:
                logs[u]=i*B+j; break
            v=v*step % n
    return r,logs


def classical_windows(n,a,requests):
    r,logs=classical_prepare(n,a,[u for L,u in requests])
    return tuple(cyclic_terminal_value(r,L,logs[u]) if u in logs else 0 for L,u in requests)


def classical_cuts(n,a,m,cuts,states):
    r,logs=classical_prepare(n,a,states); vals=[]
    for cut in cuts:
        z=1<<cut; g=gcd(r,z); s=r//g
        inv=pow(z//g,-1,s) if s>1 else 0
        vals.append(tuple(cyclic_terminal_value(s,1<<(m-cut),logs[u]//g*inv)
                          if u in logs and logs[u]%g==0 else 0 for u in states))
    return tuple(vals)


def bounded_log_setup(n,a,span,states):
    """Classical same-task baseline: bound the order/log work by the query span.

    Shared baby table; first positive identity match certifies an order only
    within the scanned interval. A missing match is NOT a subgroup absence
    certificate outside that interval. Earliest logs suffice because repetitions
    are then an arithmetic progression, or there are none within this span.
    """
    signed=set(u for u in states if gcd(u,n)==1)
    signed |= {pow(u,-1,n) for u in signed}
    B=min(span,isqrt(max(1,len(signed)+1)*span)+1)
    baby={}; z=1; r=None
    for j in range(B):
        baby[z]=j; z=z*a%n
        if z==1:
            r=j+1; break
    if r is not None:
        return r,{u:baby[u] for u in signed if u in baby}
    step=pow(z,-1,n); v=1
    for i in range(span//B+1):
        j=baby.get(v)
        if j is not None and 0<i*B+j<=span:
            r=i*B+j; break
        v=v*step%n
    logs={}
    for u in signed:
        v=u
        for i in range((span-1)//B+1):
            j=baby.get(v)
            if j is not None and i*B+j<span:
                logs[u]=i*B+j; break
            v=v*step%n
    return r,logs


def bounded_log_windows(n,a,req):
    r,logs=bounded_log_setup(n,a,max(L for L,u in req),[u for L,u in req])
    inv={u:pow(u,-1,n) for u in set(u for L,u in req) if gcd(u,n)==1}
    def positive(L,u):
        e=logs.get(u)
        if e is None or e>=L: return 0
        count=1 if r is None else (L-1-e)//r+1
        return count*(L-e)-(0 if r is None else r*count*(count-1)//2)
    return tuple(positive(L,u)+positive(L,inv[u])-L*int(u==1) if u in inv else 0 for L,u in req)


def bounded_log_cuts(n,a,m,cuts,states):
    N=1<<m; r,logs=bounded_log_setup(n,a,N,states)
    inv={u:pow(u,-1,n) for u in set(states) if gcd(u,n)==1}
    out=[]
    for j in cuts:
        step=1<<j; L=N//step
        if r is None:
            def positive(u):
                e=logs.get(u)
                return L-e//step if e is not None and e%step==0 else 0
            row=tuple(positive(u)+positive(inv[u])-L*int(u==1) if u in inv else 0 for u in states)
        else:
            g=gcd(r,step); s=r//g; reciprocal=pow(step//g,-1,s) if s>1 else 0
            row=tuple(cyclic_terminal_value(s,L,logs[u]//g*reciprocal)
                      if u in logs and logs[u]%g==0 else 0 for u in states)
        out.append(row)
    return tuple(out)


def measured(fn):
    fn(); times=[]
    for _ in range(7):
        gc.collect(); start=time.perf_counter_ns(); fn(); times.append((time.perf_counter_ns()-start)/1e6)
    gc.collect(); tracemalloc.start(); fn(); _,peak=tracemalloc.get_traced_memory(); tracemalloc.stop()
    return {'median_ms':statistics.median(times),'samples_ms':times,'peak_python_bytes':peak}


def histogram(n,a,bits):
    out={1:1}; work=0
    for j in range(bits):
        b=pow(a,1<<j,n); bi=pow(b,-1,n); nxt=Counter()
        for u,w in out.items():
            nxt[u]+=2*w; nxt[u*b%n]+=w; nxt[u*bi%n]+=w; work+=1
        out=dict(nxt)
    return out,work


def actual_prefix_work(n,a,m,cuts):
    """Build all prefix histograms in one pass, then query/contract; timed in full."""
    histories={}; h={1:1}; work=0
    for j in range(max(cuts)+1):
        if j in cuts: histories[j]=dict(h)
        if j==max(cuts): break
        b=pow(a,1<<j,n); bi=pow(b,-1,n); nxt=Counter()
        for u,w in h.items():
            nxt[u]+=2*w; nxt[u*b%n]+=w; nxt[u*bi%n]+=w; work+=1
        h=dict(nxt)
    states=tuple(sorted(set().union(*(set(h) for h in histories.values()))))
    result=dyadic_cut_responses(n,a,m,cuts,states,max_baby_steps=1<<16,max_scan_steps=10**7)
    assert result.status=='COMPLETE'
    values=tuple(sum(h.get(u,0)*v for u,v in zip(states,row))
                 for h,row in zip((histories[j] for j in cuts), result.values))
    return values,work,sum(map(len,histories.values())),len(states)


def main(out):
    # Authentic inherited dependencies, not reimplemented comparison stubs.
    expected={'src/enterprise_math/group_ring_terminal_response.py':'354633331b05f8c7f275e852ae04df85aad63004',
              'src/enterprise_math/brc_control_mass.py':'e8811e5f194fc57b294be7255214361fe99395d5'}
    for path,h in expected.items():
        data=(ROOT/path).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==h
    rng=random.Random(20260922); observer_checks=0; cut_checks=0; baseline_checks=0; compiled_checks=0
    for n in range(3,101):
        for b in [x for x in range(1,n) if gcd(x,n)==1][:3]:
            req=[(rng.randrange(1,80),rng.randrange(n)) for _ in range(80)]
            actual=window_responses(n,b,req)
            byL={L:[u for LL,u in req if LL==L] for L,_ in req}
            verified={}
            for L,states in byL.items():
                occ=Counter(pow(b,i,n) for i in range(L))
                for u in states:
                    verified[(L,u)]=sum(w*occ.get(u*v%n,0) for v,w in occ.items())
            assert actual.values==tuple(verified[q] for q in req)
            observer_checks+=len(req)
            compiler=compile_terminal_index(n,b,max(L for L,u in req),[u for L,u in req])
            assert compiler.index.windows(req)==actual.values; compiled_checks+=1
            assert classical_windows(n,b,req)==bounded_log_windows(n,b,req)==actual.values; baseline_checks+=2
            m=rng.randrange(1,10); k=min(4,m); cuts=tuple(range(k+1)); states=tuple(range(n))
            actual=dyadic_cut_responses(n,b,m,cuts,states,width_bits=k)
            expected=tuple(suffix_responses(n,b,m,j,states).values for j in cuts)
            assert actual.values==expected==classical_cuts(n,b,m,cuts,states)==bounded_log_cuts(n,b,m,cuts,states)
            cut_checks+=len(cuts)*len(states); baseline_checks+=2
            compiler=compile_terminal_index(n,b,1<<m,states)
            assert compiler.index.cuts(m,cuts,states)==actual.values; compiled_checks+=1
    windows=[]
    for n,a,H,T,Lmax in [(100160063,2,32,8,1<<18),(65537,3,64,16,1<<17),(10007,5,32,32,1<<16)]:
        states=tuple(pow(a,rng.randrange(Lmax),n) for _ in range(T))
        lengths=tuple(Lmax-i*max(1,Lmax//(2*H)) for i in range(H))
        req=tuple((L,u) for L in lengths for u in states)
        old=lambda:tuple(v for L in lengths for v in terminal_responses(n,a,L,states).values)
        new=lambda:window_responses(n,a,req)
        classic=lambda:classical_windows(n,a,req)
        bounded=lambda:bounded_log_windows(n,a,req)
        compiled=lambda:compile_terminal_index(n,a,Lmax,states).index.windows(req)
        result=new(); assert result.values==old()==classic()==bounded()==compiled()
        old_scans=sum(terminal_responses(n,a,L,states).executed_scan_steps for L in lengths)
        windows.append({'n':n,'a':a,'horizons':H,'states':T,'query_count':len(req),'max_length':Lmax,
                        'batch_width':result.baby_width,'table_entries':result.table_entries,'learned_order':result.learned_order,
                        'independent_window_scans':old_scans,'shared_scans':result.executed_scans,
                        'old_grouped_by_window':measured(old),'shared':measured(new),'order_plus_shared_bsgs':measured(classic),'bounded_order_and_logs':measured(bounded),'compiled_bounded_index_end_to_end':measured(compiled)})
    cut_benches=[]
    for n,a,m,J,T in [(100160063,2,22,10,8),(65537,3,17,8,16),(10007,5,16,6,32)]:
        states=tuple(pow(a,rng.randrange(1<<m),n) for _ in range(T)); cuts=tuple(range(J+1))
        old=lambda:tuple(suffix_responses(n,a,m,j,states).values for j in cuts)
        new=lambda:dyadic_cut_responses(n,a,m,cuts,states)
        classic=lambda:classical_cuts(n,a,m,cuts,states)
        bounded=lambda:bounded_log_cuts(n,a,m,cuts,states)
        compiled=lambda:compile_terminal_index(n,a,1<<m,states).index.cuts(m,cuts,states)
        result=new(); assert result.status=='COMPLETE' and result.values==old()==classic()==bounded()==compiled()
        old_scans=sum(suffix_responses(n,a,m,j,states).executed_scan_steps for j in cuts)
        cut_benches.append({'n':n,'a':a,'total_bits':m,'cuts':cuts,'states':T,'query_count':len(cuts)*T,
                            'batch_width':result.baby_width,'table_entries':result.table_entries,'learned_order':result.learned_order,
                            'independent_cut_scans':old_scans,'shared_scans':result.executed_scans,
                            'old_grouped_by_cut':measured(old),'shared':measured(new),'order_plus_shared_bsgs':measured(classic),'bounded_order_and_logs':measured(bounded),'compiled_bounded_index_end_to_end':measured(compiled)})
    prefixes=[]
    for n,a,m,cuts in [(1009,11,12,(0,2,4,6)),(10007,5,16,(0,2,4,6))]:
        query=lambda:actual_prefix_work(n,a,m,cuts)
        once=lambda:histogram(n,a,m)[0].get(1,0)
        val,work,records,states=query(); assert all(x==once() for x in val)
        prefixes.append({'n':n,'a':a,'bits':m,'cuts':cuts,'prefix_row_updates':work,
                         'prefix_records':records,'response_states':states,'terminal_mass':val[0],
                         'build_prefix_query_contract':measured(query),'one_full_propagation':measured(once),
                         'one_direct_terminal_query':measured(lambda:terminal_responses(n,a,1<<m))})
    result={'python':sys.version,'platform':platform.platform(),'new_pytest_tests':40,'combined_pytest_tests':93,
            'independent_window_observers':observer_checks,'cut_observers':cut_checks,
            'no_oracle_classical_baseline_batches_checked':baseline_checks,'compiled_index_batches_checked':compiled_checks,
            'windows':windows,'cuts':cut_benches,'charged_prefix_experiments':prefixes,
            'limits':['one host; seven timed complete calls, median; warmup separate; no saved tables from a prior call',
                      'input target generation not timed (common explicit input); inputs, sorting, table construction, solving included',
                      'Python peak allocations traced separately; not RSS',
                      'scan budgets omit inversions, sorting, output, bit and RAM costs',
                      'aligned cuts only; generic heterogeneous-base cache reuse is not assumed',
                      'not faster generic order finding; not RSA-270; no full repository test or independent admission']}
    Path(out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--out',default=str(Path(__file__).with_name('results.json')))
    main(p.parse_args().out)
