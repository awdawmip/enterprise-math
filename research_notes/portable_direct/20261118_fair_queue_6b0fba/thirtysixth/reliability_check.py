"""Reproduce mathematical certificates; standard library. Optional real positive-CWM backend."""
import argparse
import hashlib
import json
import math
import resource
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PRIORS = {
    'fixed': ((0,), (F(1),), ((F(1),),), (F(1,10),)),
    'latent_iid': ((0,1), (F(1,2),F(1,2)), ((F(1,2),F(1,2)),(F(1,2),F(1,2))), (F(1,4),F(3,4))),
    'latent_markov': ((0,1), (F(1,2),F(1,2)), ((F(3,4),F(1,4)),(F(1,4),F(3,4))), (F(1,4),F(3,4))),
}
PIN = '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f'


class Kernel:
    def __init__(self,root):
        if root:
            source = root/'src/enterprise_math/brc_weighted.py'
            assert hashlib.sha256(source.read_bytes()).hexdigest()==PIN
            sys.path.insert(0,str(root/'src'))
            from enterprise_math import brc_weighted as mod
            self.box,self.zero,self.one = mod.CWMState,mod.CWM_ZERO,mod.CWM_ONE
            self.append,self.merge = mod.cwm_propagate,mod.cwm_recoalesce
            self.unpack = lambda a:(a.count,a.total,a.dominant)
        else:
            self.box = lambda k,w,m:(k,w,m)
            self.zero,self.one=(0,F(0),F(0)),(1,F(1),F(1))
            self.append = lambda l,r:(l[0]*r[0],l[1]*r[1],l[2]*r[2])
            self.merge = lambda l,r:(l[0]+r[0],l[1]+r[1],max(l[2],r[2]))
            self.unpack = lambda a:a
        self.edges = {}
        self.cost = Counter()

    def edge(self,multiple,single):
        key = multiple,single
        if key not in self.edges:
            self.edges[key] = self.box(multiple,multiple*single,single)
        return self.edges[key]

    def put(self,table,key,old,multi,w):
        if w:
            self.cost['positive_transition_bundles'] += 1
            self.cost['individual_choices_represented_by_bundles'] += multi
            table[key] = self.merge(table.get(key,self.zero),self.append(old,self.edge(multi,w)))


def predicted(x):
    return F(1,2)+x/8


def observe(x,obs):
    sign = 1 if obs else -1
    return 2*(x+sign)/(4+sign*x)


def hmm_checks(limit=12):
    xs = {'':F(0)}
    aa,bb,cc,dd = 1,0,0,1
    pell_u,pell_v=1,0
    sizes,examples = [],{}
    for t in range(1,limit+1):
        xs = {w+str(obs):observe(x,obs) for w,x in xs.items() for obs in (0,1)}
        ordered = sorted((predicted(x),w) for w,x in xs.items())
        exact = F(6**(t-1),8)/(dd**2-F(cc**2,4))
        assert exact==F(1,3+5*pell_u+8*pell_v)
        pell_u,pell_v=2*pell_u+3*pell_v,pell_u+2*pell_v
        diffs = [a[0]-b[0] for a,b in zip(ordered[1:],ordered)]
        assert len(set(xs.values()))==2**t and min(diffs)==exact>0
        assert ordered[-1][1]=='1'*t and ordered[-2][1]=='0'+'1'*(t-1)
        assert ordered[-1][0]-ordered[-2][0]==exact
        assert all(-F(3,4)<x<F(3,4) for x in xs.values())
        sizes.append(len(xs))
        if t in (1,2,3,4,8,12):
            examples[t]={'separation':str(exact),'smallest_predictive':str(ordered[0][0]),
                         'largest_predictive':str(ordered[-1][0])}
        aa,bb,cc,dd = 2*aa+2*cc,2*bb+2*dd,aa+4*cc,bb+4*dd
    return {'distinct_predictive_states':sizes,'smallest_next_failure_gaps':examples}


def micro(kernel):
    weights = {}
    g = {}
    groups = {}
    for s in (0,1):
        if s:
            weights['shock'] = F(1,5)
            kernel.put(groups,('shock',0),kernel.one,1,F(1,5))
            continue
        for bits in product((0,1),repeat=3):
            j = sum(bits)
            w = F(4,5)*F(9,10)**j*F(1,10)**(3-j)
            label = ''.join(map(str,bits))
            weights['no-shock/'+label] = w
            kernel.put(groups,('private',j),kernel.one,1,w)
    rel = sum(kernel.unpack(v)[1] for (_,j),v in groups.items() if j>=2)
    assert rel==F(486,625)
    iid = (F(18,25)**3+3*F(7,25)*F(18,25)**2)
    assert iid-rel==F(486,15625)
    _,pi,P,rate=PRIORS['latent_markov']
    failures = {}
    for h,j in product((0,1),repeat=2):
        tag = ('L' if h else 'H')+('L' if j else 'H')
        w=pi[h]*P[h][j]*rate[h]*rate[j]
        failures[tag] = w
        kernel.put(g,'11',kernel.one,1,w)
    c,w,m = kernel.unpack(g['11'])
    assert (c,w,m)==(4,F(9,32),F(27,128))
    assert w/F(1,2)==F(9,16)
    return {'A_survives':str(rel),'A_iid_marginal':str(iid),'A_shock_posterior_given_system_failure':str(F(1,5)/(1-rel)),
            'A_each_positive_atomic_event_record':{k:str(v) for k,v in weights.items()},
            'B_11_environment_weights':{k:str(v) for k,v in failures.items()},
            'B_11_CWM':[c,str(w),str(m)],'B_11_conditional':str(w/F(1,2)),
            'B_rank_two_Hankel_minor':str(w-F(1,4))}


def endpoint_enumeration(n,regime,shock,t,cost):
    env,prior,trans,rates=PRIORS[regime]
    size=2**n
    vals=[F(0)]*(n+1)
    survivor_masks=Counter(mask.bit_count() for mask in range(size))
    cost['explicit_endpoint_masks_materialized']+=size
    for word in product(env,repeat=t):
        weight,age=prior[word[0]],F(1)
        for j,h in enumerate(word):
            age*=1-rates[h]
            if j: weight*=trans[word[j-1]][h]
        cost['explicit_environment_words']+=1
        cost['explicit_environment_mask_pairs_before_equal_count_grouping']+=size
        # Each explicit mask with j survivors has the same probability given this word.
        for j,mult in survivor_masks.items():
            vals[j] += weight*mult*age**j*(1-age)**(n-j)
            cost['endpoint_grouped_positive_terms']+=1
    ns=(1-shock)**t
    return [ns*v+(1-ns if j==0 else 0) for j,v in enumerate(vals)]


def all_grid(kernel,timings):
    full={}
    cost=Counter()
    maxden=maxnum=maxcount=0
    for n in (3,5,7):
        for regime,(env,prior,trans,rates) in PRIORS.items():
            for shock in (F(0),F(1,5)):
                # Initial H1 is stationary; only subsequent ticks perform a hidden transition.
                old={(h,n,False):kernel.edge(1,prob) for h,prob in zip(env,prior)}
                dd={(h,n,False):prob for h,prob in zip(env,prior)}
                identifier=f'{n}/{regime}/s={shock}'
                rows=[]
                first_cause=[F(0)]*(n-1)
                previous_survival=[F(1)]*(n-1)
                for t in range(1,9):
                    stage=time.perf_counter()
                    nxt,dp={},defaultdict(F)
                    for (h,m,seen),cell in old.items():
                        for j,next_h in enumerate(env):
                            transition=trans[h][j] if t>1 else F(h==next_h)
                            if not transition: continue
                            kernel.put(nxt,(next_h,0,True),cell,1,transition*shock)
                            for alive in range(m+1):
                                multiplicity=math.comb(m,alive)
                                probability=(1-shock)*transition*(1-rates[j])**alive*rates[j]**(m-alive)
                                kernel.put(nxt,(next_h,alive,seen),cell,multiplicity,probability)
                    timings['positive_BRC_weight_creation_conversion_and_group_update_s']+=time.perf_counter()-stage
                    stage=time.perf_counter()
                    # Independent direct mask transitions for each current live-count state;
                    # label assignment is exchangeable for this observer, a different routine.
                    for (h,m,seen),mass in dd.items():
                        for j,next_h in enumerate(env):
                            transition=trans[h][j] if t>1 else F(h==next_h)
                            if not transition: continue
                            base=mass*transition
                            if shock: dp[next_h,0,True]+=base*shock
                            cache=[base*(1-shock)*(1-rates[j])**s*rates[j]**(m-s) for s in range(m+1)]
                            for bits in range(1<<m):
                                alive=bits.bit_count()
                                dp[next_h,alive,seen]+=cache[alive]
                                cost['dp_explicit_masks_visited']+=1
                    timings['conditional_DP_named_mask_enumeration_s']+=time.perf_counter()-stage
                    stage=time.perf_counter()
                    assert set(nxt)==set(dp)
                    dist=[F(0)]*(n+1)
                    flagged=F(0)
                    for key,v in nxt.items():
                        count,mass,dominant=kernel.unpack(v)
                        assert mass==dp[key] and 0<dominant<=mass
                        dist[key[1]]+=mass
                        if key[2]:flagged+=mass
                        maxden=max(maxden,mass.denominator.bit_length(),dominant.denominator.bit_length())
                        maxnum=max(maxnum,mass.numerator.bit_length(),dominant.numerator.bit_length())
                        maxcount=max(maxcount,count.bit_length())
                    assert sum(dist)==1 and flagged==1-(1-shock)**t
                    timings['per_state_CWM_and_DP_verification_s']+=time.perf_counter()-stage
                    stage=time.perf_counter()
                    assert dist==endpoint_enumeration(n,regime,shock,t,cost)
                    timings['environment_word_endpoint_enumeration_and_check_s']+=time.perf_counter()-stage
                    stage=time.perf_counter()
                    tail=[sum(dist[k:]) for k in range(2,n+1)]
                    first_cause=[old+s*shock for old,s in zip(first_cause,previous_survival)]
                    assert all(0<=f<=1-r for f,r in zip(first_cause,tail))
                    rows.append({'t':t,'survival_k2_to_n':list(map(str,tail)),'ever_shock':str(flagged),
                                 'first_threshold_loss_due_to_shock_k2_to_n':list(map(str,first_cause))})
                    previous_survival=tail
                    timings['all_thresholds_source_queries_and_recovery_s']+=time.perf_counter()-stage
                    old,dd=nxt,dp
                full[identifier]=rows
    return full,{**cost,'largest_endpoint_mass_or_dominant_numerator_bits':maxnum,
                 'largest_endpoint_mass_or_dominant_denominator_bits':maxden,'largest_cwm_path_count_bits':maxcount}


def marginal_crossing(grid):
    crossing={}
    for n in (3,5,7):
        entry=[]
        for t in range(1,9):
            no_shock,unit=F(4,5)**t,F(9,10)**t
            def tail(p,k):
                return sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
            truth=[no_shock*tail(unit,k) for k in range(1,n+1)]
            assert list(map(str,truth[1:]))==grid[f'{n}/fixed/s=1/5'][t-1]['survival_k2_to_n']
            ratios=[value/tail(no_shock*unit,k) for k,value in enumerate(truth,start=1)]
            assert ratios[0]<1<ratios[-1] and all(x<y for x,y in zip(ratios,ratios[1:]))
            entry.append(next(k for k,val in enumerate(ratios,start=1) if val>=1))
        crossing[n]=entry
    return crossing


def check_storm(grid):
    raw=json.loads(Path(__file__).with_name('reliability_storm_checked.json').read_text())
    joined=0
    for n in (3,5,7):
        for shock in (F(0),F(1,5)):
            for latent,mode in ((0,'fixed'),(1,'latent_markov')):
                key=f'n{n}_shock{int(bool(shock))}_latent{latent}'
                scenarios=raw['scenarios'][key]['by_threshold']
                rows=grid[f'{n}/{mode}/s={shock}']
                for k in range(2,n+1):
                    for row,endpoints in zip(rows,scenarios[str(k)],strict=True):
                        safe=F(row['survival_k2_to_n'][k-2])
                        source=F(row['first_threshold_loss_due_to_shock_k2_to_n'][k-2])
                        assert list(map(F,endpoints))==[safe,source,1-safe-source]
                        joined+=1
    assert joined==raw['grid_rows']==384
    return joined


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--profile',type=Path,help='Optional nonrepeatable timings, not part of certificate')
    args=parser.parse_args()
    times=defaultdict(float)
    start=time.perf_counter()
    kernel=Kernel(args.source_root)
    times['kernel_setup_s']=time.perf_counter()-start
    start=time.perf_counter()
    a=micro(kernel)
    times['source_micro_and_labels_s']=time.perf_counter()-start
    start=time.perf_counter()
    b=hmm_checks()
    times['hmm_enumeration_and_next_lookup_s']=time.perf_counter()-start
    start=time.perf_counter()
    grid,cost=all_grid(kernel,times)
    times['grid_construction_three_way_execution_and_all_query_checks_s']=time.perf_counter()-start
    assert len(grid)==18 and sum(len(row['survival_k2_to_n']) for rows in grid.values() for row in rows)==576
    start=time.perf_counter()
    joined=check_storm(grid)
    times['external_Storm_384_row_exact_comparison_s']=time.perf_counter()-start
    start=time.perf_counter()
    result={'actual_Storm_grid_rows_joined_on_three_values':joined,'kernel_sha256':PIN,'H_label':0,'L_label':1,'grid_threshold_queries':576,
            'grid_ever_shock_queries':144,'grid_first_cause_threshold_queries':576,'atomic_microcase':a,'hmm_gap_frontier':b,
            'grid_source_process':'stationary H1, later transition to H_j, shock first, independent private failures among survivors if no shock; no ordinary repairs',
            'grid':grid,'first_k_where_true_reliability_ge_iid':marginal_crossing(grid),'operation_counts':{**kernel.cost,**cost,'cached_distinct_bundle_weights':len(kernel.edges)}}
    payload=json.dumps(result,sort_keys=True,indent=2)+'\n'
    sys.stdout.write(payload)
    times['result_serialization_and_stdout_s']=time.perf_counter()-start
    if args.profile:
        times.update({'process_peak_rss_kib_Linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      'exact_JSON_bytes':len(payload.encode()),'python':sys.version.split()[0],
                      'actual_project_kernel':bool(args.source_root)})
        args.profile.write_text(json.dumps(times,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':
    main()
