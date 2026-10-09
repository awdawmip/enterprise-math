"""State-dependent order defects in the pinned positive-BRC reservation model.

This is NOT native six-axis dynamics. Reserve/release are imported unchanged.
Endpoint identities explicitly exclude command transcripts and physical costs.
Run: python check_order.py. Every executed word retains its positive CWM weight;
readout subtraction compares two outputs and never creates negative mass.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIOR = ROOT/'prior/check_membership.py'
if not PRIOR.exists():
    PRIOR = ROOT.parent/'20261008_residual_membership_7c2e8a/check_membership.py'
raw = PRIOR.read_bytes()
expected = 'be1b60446e31c2c8489d1ce0db16cc1e952d11c8'
actual = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
if actual != expected:
    raise RuntimeError('pinned membership source mismatch')
spec = importlib.util.spec_from_file_location('order_pinned_membership', PRIOR)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
s, r = m.s, m.r
CHECKS = 0
KERNEL_CALLS = 0


def ck(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def cw(w):
    return {'C': w.count, 'W': str(w.total), 'M': str(w.dominant)}


def step(J, op):
    global KERNEL_CALLS
    if op[0] not in ('release', 'reserve'):
        raise ValueError('unknown command')
    KERNEL_CALLS += 1
    return m.full_step(J, op)


def run(J, word, weight=None):
    w = r.brc.CWM_ONE if weight is None else weight
    trace = []
    for op in word:
        before = J
        J, released, ok = step(J, op)
        w = r.serial(w, r.brc.CWM_ONE)
        trace.append({'op': op, 'before': before, 'after': J,
                      'successful_releases': released, 'success': ok})
    return J, w, trace


def put(out, key, w):
    out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), w)


def triples(n):
    return tuple(combinations(range(1, n+1), 3))


def prepare(n):
    H = triples(n)
    events = tuple(s.TestEvent(str(i), frozenset(h), r.brc.CWM_ONE)
                   for i, h in enumerate(H))
    poly = s.assemble(events, frozenset(range(1, n+1)))
    return {m.canon(H[int(i)] for i in J): w for (J, used), w in poly.items()}


def independent_at(J, a, b):
    """Closed-form theorem criterion, independent of the execution wrapper."""
    if a[0] == b[0] == 'release':
        return True
    occupied = m.used(J)
    if a[0] == b[0] == 'reserve':
        D, E = frozenset(a[1]), frozenset(b[1])
        bad = D != E and bool(D & E) and not (D & occupied) and not (E & occupied)
        return not bad
    release, reserve = (a, b) if a[0] == 'release' else (b, a)
    x, D = release[1], frozenset(reserve[1])
    owner = next((frozenset(h) for h in J if x in h), frozenset())
    free_before = not (D & occupied)
    free_after = not (D & (occupied-owner))
    bad = (free_before and x in D) or (not free_before and free_after)
    return not bad


def check_algebra():
    states = prepare(6)
    ck(len(states) == 31, 'all six-occurrence disjoint triad assemblies')
    ops = tuple(('release', b) for b in range(1, 7)) + tuple(('reserve', D) for D in triples(6))
    counts = Counter()
    certificate = hashlib.sha256()
    for J, w0 in sorted(states.items()):
        for a in ops:
            first, w1, _ = run(J, (a,), w0)
            twice, w2, _ = run(J, (a,a), w0)
            ck(first == twice and w1 == w2, 'endpoint idempotence, not transcript equality')
            for b in ops:
                left, wl, _ = run(J, (a,b), w0)
                right, wr, _ = run(J, (b,a), w0)
                equal = left == right
                ck(equal == independent_at(J,a,b), 'complete statewise commutation criterion')
                ck(wl == wr == w0, 'deterministic word does not alter preparation weight')
                kind = a[0]+'/'+b[0]
                counts[kind+('/equal' if equal else '/different')] += 1
                certificate.update(repr((J,a,b,left,right)).encode())
    J = m.canon(((1,2,3),))
    x = run(J, (('release',1),('release',2)))
    y = run(J, (('release',2),('release',1)))
    ck(x[0] == y[0], 'release words same endpoint')
    by_name_x = {t['op'][1]:t['success'] for t in x[2]}
    by_name_y = {t['op'][1]:t['success'] for t in y[2]}
    ck(by_name_x != by_name_y, 'same endpoint does not erase command-specific records')
    d = ('reserve',(2,4,5))
    u, v = run(J,(('release',1),d)), run(J,(d,('release',1)))
    ck(u[0] != v[0], 'disjoint syntactic arguments hide owner-member dependence')
    D = ('reserve',(1,2,3))
    ck(run((),(D,))[0] == J and run(J,(D,))[0] == J, 'nonidentity reserve is noninjective on current states')
    ck(run((),(('release',1),))[0] == () == run(J,(('release',1),))[0], 'release is noninjective on current states')
    return {'states':len(states), 'commands':len(ops), 'ordered_pair_tests':len(states)*len(ops)**2,
            'idempotence_tests':len(states)*len(ops), 'commutation_counts':dict(sorted(counts.items())),
            'transition_certificate_sha256':certificate.hexdigest(),
            'transcript_counterexample':{'initial':J,'left':x[2],'right':y[2]},
            'hidden_support_counterexample':{'initial':J,'release_then_reserve':u[2],'reserve_then_release':v[2]}}


def final_rows(hist):
    return [{'state':J, 'weight':cw(w)} for J,w in sorted(hist.items())]


def schedule_law(J, H, normalized=False):
    orders = tuple(permutations(H))
    initial_weight = r.edge(Q(1,len(orders))) if normalized else r.brc.CWM_ONE
    hist = {}
    traces = []
    for order in orders:
        end,w,trace = run(J,tuple(('reserve',D) for D in order),initial_weight)
        put(hist,end,w)
        traces.append({'order':order,'end':end,'weight':cw(w),'trace':trace})
    return hist,traces


def maximal_extensions(J,H):
    events = tuple(s.TestEvent(str(i),frozenset(h),r.brc.CWM_ONE) for i,h in enumerate(H))
    I = frozenset().union(*(frozenset(h) for h in tuple(H)+tuple(J)))
    poly = s.assemble(events,I)
    valid = {key:w for key,w in poly.items() if not key[1] & m.used(J)}
    maximal = [k for k in valid if not any(k[0] < l[0] for l in valid)]
    return {m.canon(tuple(J)+tuple(H[int(i)] for i in k[0])) for k in maximal}


def check_schedule_theorem():
    certificate = hashlib.sha256()
    cases = 0
    for H in combinations(triples(6),3):
        hist,_ = schedule_law((),H)
        ck(set(hist) == maximal_extensions((),H), 'all and only maximal extensions reachable')
        pairwise_disjoint = all(not set(D)&set(E) for D,E in combinations(H,2))
        ck((len(hist)==1) == pairwise_disjoint, 'order invariance iff feasible supports disjoint')
        ck(r.total(hist.values()).count==6 and r.total(hist.values()).total==6,
           'all six schedule branches preserved')
        certificate.update(repr((H,final_rows(hist))).encode())
        cases += 1
    positive_H = ((1,2,3),(4,5,6),(7,8,9))
    positive_hist,_ = schedule_law((),positive_H)
    ck(set(positive_hist)==maximal_extensions((),positive_H)=={m.canon(positive_H)}, 'nontrivial disjoint case all orders agree')
    H = ((1,2,3),(1,4,5),(4,5,6))
    for J in prepare(6):
        hist,_ = schedule_law(J,H)
        F = tuple(D for D in H if not set(D)&m.used(J))
        independent = all(not set(D)&set(E) for D,E in combinations(F,2))
        ck(set(hist)==maximal_extensions(J,H),'same theorem with preexisting occupied events')
        ck((len(hist)==1)==independent,'only initially feasible events matter')
        cases += 1
    hist,traces = schedule_law((),H,True)
    AC,B = m.canon((H[0],H[2])),m.canon((H[1],))
    ck(hist[AC].total==Q(2,3) and hist[B].total==Q(1,3),'uniform orders not uniform maximal states')
    ck(hist[AC].count==4 and hist[B].count==2,'order multiplicity retained')
    return {'three_event_libraries':1140,'nonempty_and_empty_fixed_library_cases':31,
            'total_cases':cases+1,'schedule_words':(cases+1)*6,'additional_disjoint_nine_occurrence_case':True,'certificate_sha256':certificate.hexdigest(),
            'uniform_order_example':{'events':H,'endpoints':final_rows(hist),'traces':traces,
            'preparation':'uniform six permutations; an algorithmic choice, not physical probability'}}


def check_competitive_intervention():
    initial=m.canon(((1,2,3),))
    D,E=(1,4,5),(4,5,6)
    pairs=[]
    for order in ((D,E),(E,D)):
        control,w0,t0=run(initial,tuple(('reserve',h) for h in order))
        treated,w1,t1=run(initial,(('release',1),)+tuple(('reserve',h) for h in order))
        # One preparation weight belongs to this pair, not its tensor square.
        ck(w0==w1==r.brc.CWM_ONE,'same preparation, weight counted once')
        delta=int(6 in m.used(treated))-int(6 in m.used(control))
        pairs.append({'order':order,'control_trace':t0,'treated_trace':t1,
                      'control_target6':int(6 in m.used(control)),
                      'treated_target6':int(6 in m.used(treated)),
                      'difference':delta,'pair_weight':cw(w0)})
    ck([p['difference'] for p in pairs]==[-1,0],'extra freedom can inhibit rather than facilitate')
    order_mixtures=[]
    for alpha in (Q(0),Q(1,5),Q(1,2),Q(4,5),Q(1)):
        law={}
        for p,weight in zip(pairs,(alpha,1-alpha)):
            if weight>0:
                put(law,p['difference'],r.serial(r.edge(weight),r.brc.CWM_ONE))
        total=r.total(law.values())
        ck(total.total==1,'every scheduler branch kept')
        negative=law.get(-1,r.brc.CWM_ZERO).total
        ck(negative==alpha,'negative-response mass equals competing-order mass')
        order_mixtures.append({'alpha':str(alpha),'law':{str(k):cw(v) for k,v in law.items()},
                               'signed_mean_comparison':str(-negative)})
    return {'initial':initial,'competing_event':D,'target_event':E,'target_member':6,
            'paired_traces':pairs,'scheduler_mixtures':order_mixtures,
            'physical_force_or_axis_attribution':False}


def check_gate_budget_and_fanout_order():
    initial=m.canon(((1,2,3),))
    gates=((1,7,13),(2,19,25),(3,31,32))
    competitor=(1,7,19)
    targets=(7,13,19,25,31)
    rows=[]
    for order in permutations(gates+(competitor,)):
        c,w0,t0=run(initial,tuple(('reserve',h) for h in order))
        t,w1,t1=run(initial,(('release',1),)+tuple(('reserve',h) for h in order))
        delta=tuple(int(b in m.used(t))-int(b in m.used(c)) for b in targets)
        theta=int(all(delta))
        rows.append({'order':order,'delta':delta,'joint':theta,'control':c,'treated':t,
                     'control_trace':t0,'treated_trace':t1})
    yes=r.brc.CWM_ZERO; no=r.brc.CWM_ZERO
    for row in rows:
        w=r.edge(Q(1,24))
        if row['joint']:yes=r.merge(yes,w)
        else:no=r.merge(no,w)
    # The competitor must precede BOTH first two gates to win. Third gate independent.
    ck(yes.total==Q(2,3) and no.total==Q(1,3),'four-event schedule-dependent five-target fanout')
    masks=Counter(tuple(bool(x) for x in row['delta']) for row in rows)
    ck(set(masks)=={(True,True,True,True,True),(True,False,True,False,True)},'competitor carries different targets')
    return {'source':initial,'gates':gates,'competitor':competitor,'targets':targets,
            'all_orders':24,'full_response_orders':yes.count,'partial_response_orders':no.count,
            'full_response_weight':str(yes.total),'partial_response_weight':str(no.total),
            'masks':{''.join('1' if b else '0' for b in k):v for k,v in masks.items()},'traces':rows,
            'probability_scope':'uniform permutation diagnostic only'}


def main():
    algebra=check_algebra()
    schedule=check_schedule_theorem()
    inhibition=check_competitive_intervention()
    fanout=check_gate_budget_and_fanout_order()
    result={'schema':'EM_BRC_ORDER_DEFECT_V1','status':'CONDITIONAL_UNREVIEWED_NOT_NATIVE_DYNAMICS',
            'event_id':'EM-20261009-RESIDUAL-ORDER-7C2E8A',
            'global_read':'a5016513f59f5b4d690eff09ff11e19551bf351f',
            'source_read':'eef565a6e15271ff6afc2688099f5fdae1139fde',
            'algebra':algebra,'schedule':schedule,'inhibition':inhibition,'fanout':fanout,
            'assertions':CHECKS,'membership_helper_assertions':m.CHECKS,
            'actual_full_step_calls':KERNEL_CALLS,'BRC_calls':dict(r.CALLS),
            'old_main_suites_executed':False,'new_native_transition_law':False,'independent_review':False}
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    summary={k:result[k] for k in ('status','event_id','assertions','membership_helper_assertions','actual_full_step_calls','BRC_calls')}
    summary.update(ordered_pair_tests=algebra['ordered_pair_tests'],schedule_cases=schedule['total_cases'],
                   scheduler_negative_differences=[p['difference'] for p in inhibition['paired_traces']],
                   fanout_full_response_orders=fanout['full_response_orders'],
                   fanout_partial_response_orders=fanout['partial_response_orders'],
                   output_bytes=len(data),output_sha256=hashlib.sha256(data).hexdigest())
    (ROOT/'summary.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
