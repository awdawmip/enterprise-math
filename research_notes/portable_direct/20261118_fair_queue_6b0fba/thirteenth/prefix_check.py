"""Fixed public 28-bit toy ledger and square-shell counting identities; no target-input interface."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import accumulate
import json
from math import ceil, gcd, isqrt
from pathlib import Path
from random import Random
from statistics import median
import sys
from time import perf_counter_ns
import tracemalloc

PIN='24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14'
FILES={
 'brc_opportunistic_shortcuts.py':'7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7',
 'brc_multiplier_priority_jump.py':'ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d',
 'brc_multiplier_transition.py':'b87bea689bced5e773bb450e2c3f51198209b06661a5488581f6b050c468baf5',
 'brc_multiplier_factor_scan.py':'287521603fd04a7dd8d7b89069a062d10f117a1f53172bd2d086bc7b00921f1e',
 'brc_square_gap_prefilter.py':'f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716',
 'brc_square_gap_table_46189.py':'ae36d0ea1316de3aa461d8b9e5c86486276e79a3a44568a21209724697f47e43'}
ARMS=('structure','learned20','kernel13','rr4')
STRIP=(3*5*7*11*13*17*19*23*29*31)


def cohorts():
    # Hidden generator labels never reach the evaluation or routing loops.
    prime=bytearray([1])*30001;prime[0:2]=b'\0\0'
    for j in range(2,isqrt(30000)+1):
        if prime[j]:prime[j*j::j]=bytes((30000-j*j)//j+1)
    def take(values,tag):
        return sorted(set(values),key=lambda n:sha256(f'prefix-public-28:{tag}:{n}'.encode()).digest())[:48]
    near=take((p*q for p in range(7200,7551) if prime[p]
             for q in range(3*p-30,3*p+31) if prime[q]),'fixed-3')
    # Separate source prime intervals; independent rectangular product then uniform hash subsample.
    primes1=[i for i in range(6200,8701) if prime[i] and not 7200<=i<=7550]
    primes2=[i for i in range(19000,29001) if prime[i]]
    control=take((a*b for a in primes1 for b in primes2 if (a*b).bit_length()==28),'independent')
    assert len(set(near+control))==96 and all(n.bit_length()==28 for n in near+control)
    return {'near3':near,'independent':control}


def plan(arm,port):
    if arm=='structure':return port.structural_order(1000),0
    if arm=='kernel13':
        order=port.kernel13_order(1000)
        return order,98
    if arm=='learned20':return port.learned_cover_order(1000),20
    batches=port.multiplier_probe_batches(max_multiplier=1000,include_kernel_specialist=True,quantum=4)
    return port.flatten_probe_batches(batches),sum(len(ms) for tag,ms in batches if tag!='structural_fallback')


def scale_groups(ms,port):
    groups=defaultdict(list)
    for m in ms:
        d=port.squarefree_kernel(m);a=isqrt(m//d)
        assert a*a*d==m
        groups[d].append(a)
    return groups


def uniform_mean(scales):
    vmax=max(scales);val=F(0)
    for v in range(1,vmax+1):
        covering=[a for a in scales if a%v==0]
        if covering:
            val+=F(sum(gcd(i,v)==1 for i in range(1,v+1)),min(covering))
    cuts=sorted({F(j,a) for a in scales for j in range(a+1)})
    audit=sum((b-a)*len({F(ceil(s*(a+b)/2),s) for s in scales}) for a,b in zip(cuts,cuts[1:]))
    assert audit==val
    return val


def stats_int(vals):
    ordered=sorted(vals)
    return dict(total=sum(ordered),median=str(F(ordered[(len(vals)-1)//2]+ordered[len(vals)//2],2)),
                p95=ordered[ceil(0.95*len(vals))-1],worst=ordered[-1])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path('.'))
    parser.add_argument('--output',type=Path)
    parser.add_argument('--measure',type=Path,help='optional raw environment-dependent paired timing log')
    args=parser.parse_args()
    for fn,digest in FILES.items():
        assert sha256((args.repo/'src/enterprise_math'/fn).read_bytes()).hexdigest()==digest
    sys.path.insert(0,str((args.repo/'src').resolve()))
    from enterprise_math import brc_opportunistic_shortcuts as port
    from enterprise_math import brc_multiplier_factor_scan as gate
    from enterprise_math.brc_multiplier_transition import initial_multiplier_root_state as root
    sets=cohorts();plans={a:plan(a,port) for a in ARMS}
    base=plans['structure'][0];ken=port.kernel13_prefix(1000)
    assert len(base)==625 and len(ken)==98 and plans['kernel13'][0][:98]==ken
    assert all(len(o)==625 and set(o)==set(base) for o,n in plans.values())
    domains={'kernel13':ken,'learned20':plans['learned20'][0][:20],'complete':base}
    rays={name:scale_groups(ms,port) for name,ms in domains.items()}
    means={name:str(sum(uniform_mean(scales) for scales in gs.values())) for name,gs in rays.items()}
    context=port.ShortcutContext(28,max_multiplier=1000,states_materialized=False)
    trials=[(v.shortcut_id,v.max_probe_candidates) for v in port.opportunistic_trial_plan(context)]
    result={}
    for name,ns in sets.items():
        ledger=port.RegimeShortcutLedger(); logs=[]; ray_totals=Counter()
        for n in ns:
            assert gcd(n,STRIP)==1
            outcomes={}
            for m in base:
                st=root(m*n);x=st.root+int(st.remainder!=0);gap=st.ceiling_completion_gap
                first=gate._table_contains(gate.square_residue_table(gate.CASCADE_FIRST_MODULUS),gate.CASCADE_FIRST_MODULUS,gap)
                both=gate.strong_cascade_passes_squarehood(gap)
                y=gate.strong_cascade_square_root(gap); hit=False;calls=0
                if y is not None:
                    for term in (x-y,x+y):
                        calls+=1;g=gcd(term,n)
                        if 1<g<n:
                            assert n%g==0; hit=True;break
                outcomes[m]=(x,gap,first,both,hit,calls)
            hitset={m for m,o in outcomes.items() if o[4]}
            for tag,group in rays.items():
                for d,scales in group.items():
                    bins={}
                    for a in scales:
                        x,gap,_,_,h,_=outcomes[a*a*d];f=F(x,a);u,v=f.numerator,f.denominator
                        assert gcd(a,n)==1 and gap==(a//v)**2*(u*u-v*v*d*n)
                        if f in bins:assert bins[f]==h
                        bins[f]=h
                    ray_totals[tag]+=len(bins)
            row={'N':n,'hittable':bool(hitset),'arms':{}}
            visits={}
            for arm in ARMS:
                seq,p=plans[arm]
                stop=next((j for j,m in enumerate(seq,1) if m in hitset),625)
                visited=seq[:stop];visits[arm]=set(visited)
                costs={'states':stop,'qr_lookup1':stop,'qr_lookup2':sum(outcomes[m][2] for m in visited),
                       'square_roots_after_filters':sum(outcomes[m][3] for m in visited),
                       'witness_gcd':sum(outcomes[m][5] for m in visited),'common_presieve_gcd':1,
                       'prefix_visits':min(p,stop),'fallback_visits':max(0,stop-p),
                       'prefix_hit':bool(set(seq[:p])&hitset)}
                row['arms'][arm]=costs
                if arm!='structure':
                    extra=len(visits[arm]-visits['structure']);avoided=len(visits['structure']-visits[arm])
                    assert avoided-extra==row['arms']['structure']['states']-stop
                    ledger.record(context,arm,hit=costs['prefix_hit'],probe_cost=extra,saved_cost=avoided)
            logs.append(row)
        summary={}
        for arm in ARMS:
            rs=[r['arms'][arm] for r in logs]
            summary[arm]={'states':stats_int([r['states'] for r in rs]),'prefix_hits':sum(r['prefix_hit'] for r in rs),
                **{k:sum(r[k] for r in rs) for k in ('qr_lookup2','square_roots_after_filters','witness_gcd',
                                                    'prefix_visits','fallback_visits')}}
        result[name]=dict(ledger_measure='one unit per exact root-state visit; plan and clocks accounted separately',
                          ledger=ledger.to_dict(),summary=summary,ray_totals=dict(ray_totals),
                          scan_hits=sum(r['hittable'] for r in logs),rows=logs)
    if args.measure:
        def timed_batch(arm,inputs):
            start=perf_counter_ns();order,p=plan(arm,port);setup=perf_counter_ns()-start
            rows=[]
            for n in inputs:
                ts=perf_counter_ns(); found=False
                if gcd(n,STRIP)==1:
                    for m in order:
                        st=root(m*n);y=gate.strong_cascade_square_root(st.ceiling_completion_gap)
                        if y is not None:
                            x=st.root+int(st.remainder!=0)
                            for term in (x-y,x+y):
                                g=gcd(term,n)
                                if 1<g<n:
                                    assert n%g==0;found=True;break
                        if found:break
                rows.append((perf_counter_ns()-ts,found))
            return setup,rows,perf_counter_ns()-start
        # Steady interpreter; previously audited tables already warm. Each arm pays for rebuilding its ordered plan.
        for tag,inputs in sets.items():
            for arm in ARMS:timed_batch(arm,inputs)
        rng=Random(20261101);measure={}
        for tag,inputs in sets.items():
            observations=[]
            for rep in range(9):
                perm=list(ARMS);rng.shuffle(perm)
                for arm in perm:
                    setup,rs,total=timed_batch(arm,inputs)
                    assert [r[1] for r in rs]==[r['hittable'] for r in result[tag]['rows']]
                    observations.append(dict(rep=rep,arm=arm,setup_ns=setup,input_ns=[r[0] for r in rs],total_ns=total))
            peaks={}
            for arm in ARMS:
                tracemalloc.start();timed_batch(arm,inputs);cur,hi=tracemalloc.get_traced_memory();tracemalloc.stop()
                peaks[arm]=[cur,hi]
            measure[tag]=dict(replays=observations,isolated_traced_current_peak_bytes=peaks)
        args.measure.write_text(json.dumps({'clock':'perf_counter_ns','python':sys.version,'fixed_interleave_seed':20261101,
                                  'regime':'one freshly built plan per 48 fixed inputs, cached QR tables and interpreter',
                                  'by_population':measure},separators=(',',':'))+'\n')
    out={'pinned_ref':PIN,'source_sha256':FILES,'trial_plan':trials,'number_of_multipliers':{k:len(v) for k,v in domains.items()},
         'prefix_widths':{a:plans[a][1] for a in ARMS},'uniform_fractional_part_expected_rays':means,'cohorts':result}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if args.output:args.output.write_text(txt)
    print(txt,end='')


if __name__=='__main__':main()
