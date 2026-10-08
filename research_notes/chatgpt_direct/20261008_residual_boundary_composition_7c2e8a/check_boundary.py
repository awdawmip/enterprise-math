"""BRC boundary/score composition, NOT a native force or release law.

Run python check_boundary.py. Pinned old functions are imported, never their
main suites. A table key is (occupied boundary occurrences, event count).
Coefficients remain positive CWM; top-degree observation is scoped to optimal
forward assembly only. Frozen factor grammar retains provenance for replay.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, permutations

ROOT = Path(__file__).resolve().parent
PRIOR = ROOT/'prior/check_selector.py'
if not PRIOR.exists():
    PRIOR = ROOT.parent/'20261008_residual_selector_7c2e8a/check_selector.py'
data = PRIOR.read_bytes()
if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() != 'e2c84a17f3c9f59a28d51bd65460c48d3fc90a08':
    raise RuntimeError('prior selector source mismatch')
spec = importlib.util.spec_from_file_location('boundary_prior_selector', PRIOR)
p = importlib.util.module_from_spec(spec); sys.modules[spec.name] = p
spec.loader.exec_module(p)
s, r = p.s, p.r
CHECKS = 0

def ck(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok: raise AssertionError(message)


def plus(a, b):
    out = dict(a)
    for key, v in b.items():
        out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), v)
    return out


def conv(a, b):
    """Positive CWM convolution over disjoint boundary masks and score sum."""
    out = {}
    for (x, k), u in a.items():
        for (y, ell), v in b.items():
            if x & y: continue
            key = (x|y, k+ell)
            out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), r.serial(u, v))
    return out


def project(poly, boundary):
    out = {}
    for (events, used), v in poly.items():
        key = (used & boundary, len(events))
        out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), v)
    return out


def forget(table, boundary):
    out = {}
    for (x,k),v in table.items():
        key = (x & boundary, k)
        out[key] = r.merge(out.get(key, r.brc.CWM_ZERO), v)
    return out


def top(table):
    """Observer projection, NOT a mass-preserving dynamics or sampler."""
    best = {}
    for x,k in table: best[x] = max(best.get(x,-1), k)
    return {(x,k):v for (x,k),v in table.items() if k == best[x]}


def domain(events):
    return frozenset().union(*(e.occurrences for e in events))


def compose(a, b, left_events, right_events, boundary):
    if {e.key for e in left_events} & {e.key for e in right_events}:
        raise ValueError('module event identities overlap')
    if not (domain(left_events) & domain(right_events)) <= boundary:
        raise ValueError('boundary omits a shared occurrence')
    return conv(a,b)


def serial_rows(table):
    return [{'occupied':sorted(x),'score':k,'C':v.count,
             'W':str(v.total),'M':str(v.dominant)}
            for (x,k),v in sorted(table.items(),key=lambda kv:(sorted(kv[0][0]),kv[0][1]))]


def digest_table(table):
    return hashlib.sha256(json.dumps(serial_rows(table),sort_keys=True).encode()).hexdigest()


def sweep(events, optimize=False, compare_prefix=False):
    """Known finite forward factor list; boundary includes ALL remaining uses.

    No old event may be released or reconsidered here. Computing this boundary
    requires the frozen future factor list; this is not local physical foresight.
    """
    events = tuple(events)
    if len({e.key for e in events}) != len(events):
        raise ValueError('duplicate event identity')
    suffix = [frozenset()]*(len(events)+1)
    for j in range(len(events)-1,-1,-1):
        suffix[j] = suffix[j+1] | events[j].occurrences
    seen = frozenset(); table = {(frozenset(),0):r.brc.CWM_ONE}
    full = {s.EMPTY:r.brc.CWM_ONE}; trace = []
    max_boundary = max_masks = max_entries = 0
    for j,e in enumerate(events):
        boundary_before = seen & suffix[j]
        ck(seen & e.occurrences <= boundary_before,'new overlap covered')
        out = dict(table)  # explicit skip branch, coefficient ONE
        for (x,k),v in table.items():
            if not x & e.occurrences:
                key = (x|e.occurrences,k+1)
                out[key] = r.merge(out.get(key,r.brc.CWM_ZERO),r.serial(v,e.weight))
        seen |= e.occurrences
        boundary = seen & suffix[j+1]
        table = forget(out,boundary)
        if optimize: table = top(table)
        if compare_prefix:
            full = s.times(full,s.factor(e))
            expected = project(full,boundary)
            if optimize: expected = top(expected)
            ck(table==expected,'every prefix agrees with original full BRC assembly')
        b=len(boundary); masks=len({x for x,k in table})
        max_boundary=max(max_boundary,b);max_masks=max(max_masks,masks)
        max_entries=max(max_entries,len(table))
        trace.append({'processed':j+1,'boundary':sorted(boundary),
                      'entries':len(table),'masks':masks,'sha256':digest_table(table)})
    return table, {'max_boundary_occurrences':max_boundary,'max_masks':max_masks,
                   'max_entries':max_entries,'trace':trace}


def test_fixed_composition():
    universe=frozenset(range(1,7)); cases=0
    triples=list(combinations(range(1,7),3))
    for index,hs in enumerate(combinations(triples,3)):
        # Nontrivial positive branch families; C is not just Boolean support.
        events=tuple(s.TestEvent(f'H{j}',frozenset(h),
                     r.merge(r.edge(j+1),r.edge(Q(j+2,3)))) for j,h in enumerate(hs))
        a,b,c=events
        B=(a.occurrences&b.occurrences)|(a.occurrences&c.occurrences)|(b.occurrences&c.occurrences)
        fa,fb,fc=(project(s.factor(e),B) for e in events)
        full=s.assemble(events,universe)
        ab=compose(fa,fb,(a,),(b,),B)
        left=compose(ab,fc,(a,b),(c,),B)
        right=compose(fa,conv(fb,fc),(a,),(b,c),B)
        ck(left==right==project(full,B),'exact graded composition and association')
        ck(top(conv(top(ab),fc))==top(left),'safe middle optimization')
        ck(top(conv(conv(top(fa),top(fb)),top(fc)))==top(left),'all masked optima compose')
        ck(conv(fa,plus(fb,fc))==plus(conv(fa,fb),conv(fa,fc)),'left distribution')
        ck(conv(plus(fa,fb),fc)==plus(conv(fa,fc),conv(fb,fc)),'right distribution')
        for small in (frozenset(),frozenset((1,)),B):
            ck(top(forget(top(left),small))==top(forget(left,small)),
               'certified forget followed by optimum preserves tied CWM')
        cases+=1
    bad=False
    try: compose(fa,fb,(a,),(b,),frozenset())
    except ValueError: bad=True
    ck(bad,'unsafe hidden overlap rejected')
    return cases


def test_original_opt_repair():
    I=frozenset(range(1,7));B=frozenset((1,4,5))
    E=tuple(s.TestEvent(k,frozenset(h),r.edge(1)) for k,h in
            [('A',(1,2,3)),('B',(1,4,5)),('C',(4,5,6))])
    a,b,c=E
    first=project(s.factor(b),B)
    later=project(s.times(s.factor(a),s.factor(c)),B)
    correct=top(forget(conv(top(first),top(later)),frozenset()))
    ck(next(iter(correct))[1]==2,'masked optimization retains AC option')
    for perm in permutations(E):
        full,tr=sweep(perm,False,True)
        best,br=sweep(perm,True,True)
        ck(top(full)==best,'all six orderings preserve complete optimum CWM')
    full=project(s.assemble(E,I),frozenset())
    best=top(full)
    eta=r.edge(2)
    def evaluate(tab):
        ans=r.brc.CWM_ZERO
        for (x,k),v in tab.items():
            value=v
            for _ in range(k):value=r.serial(value,eta)
            ans=r.merge(ans,value)
        return ans
    z=evaluate(full);truncated=evaluate(best)
    ck(z.total==11 and truncated.total==4,'optimizer does not preserve selector normalizer')
    return {'first_boundary_table':serial_rows(first),'repaired_optimum':serial_rows(correct),
            'full_score_table':serial_rows(full),'at_eta_2_full_W':str(z.total),
            'at_eta_2_optimized_W':str(truncated.total)}


def test_mask_distinguishability():
    B=tuple(range(6)); masks=[frozenset(B[i] for i in range(6) if n>>i&1) for n in range(64)]
    pairs=0
    for x,y in combinations(masks,2):
        b=min(x^y)
        # Each mask can be realized using per-boundary private filler triples.
        # The new probe triple has b plus two fresh private occurrences.
        probe={(frozenset((b,)),1):r.brc.CWM_ONE}
        tx={(x,len(x)):r.brc.CWM_ONE}; ty={(y,len(y)):r.brc.CWM_ONE}
        ck(bool(conv(tx,probe))!=bool(conv(ty,probe)),
           'fresh one-occurrence probe distinguishes boundary masks')
        pairs+=1
    return pairs


def test_release_boundary():
    I=frozenset(range(1,8)); B=frozenset((1,2,3))
    events={k:s.TestEvent(k,frozenset(h),r.edge(1)) for k,h in
            [('A',(1,2,3)),('C',(4,5,6)),('D',(1,2,4)),('E',(3,5,6)),('F',(2,3,7))]}
    def basis(J):return (frozenset(J),frozenset().union(*(events[k].occurrences for k in J)))
    left,right=basis(('A','C')),basis(('D','E'))
    full=s.assemble(tuple(events.values()),I)
    ck(left in full and right in full,'both preparations use same declared library')
    ck(project({left:r.brc.CWM_ONE},B)==project({right:r.brc.CWM_ONE},B),
       'same whole allocation, count, boundary table before release')
    outcomes=[]
    for state in (left,right):
        J,U=state
        members=[k for k in J if 1 in events[k].occurrences]
        ck(len(members)==1,'member query identifies unique current reservation')
        released=members[0]
        after=basis(J-{released})
        proposed=s.times({after:r.brc.CWM_ONE},
                         {(frozenset(('F',)),events['F'].occurrences):r.brc.CWM_ONE})
        # A rejected proposal stays explicitly held; no positive physical mass
        # is inferred absent from an empty compatible-certificate polynomial.
        outcomes.append({'before':sorted(J),'release_member':1,'released_event':released,
          'after_release':sorted(after[0]),'unassigned':sorted(I-after[1]),
          'F_accepted':bool(proposed),'proposal_CWM':{'C':1,'W':'1','M':'1'},
          'rejected_proposal_retained':not bool(proposed)})
    ck(outcomes[0]['F_accepted'] and not outcomes[1]['F_accepted'],
       'new release language requires membership, not only occupancy')
    return outcomes


def main():
    fixed=test_fixed_composition();small=test_original_opt_repair()
    probes=test_mask_distinguishability();release=test_release_boundary()
    path_runs=[]
    for n in (2,4,7,100):
        E,I=p.path_library(n)
        all_scores,at=sweep(E,False,n<=7)
        optimum,ot=sweep(E,True,n<=7)
        ck(top(all_scores)==optimum,'large forward optimum projection agrees')
        score=next(iter(optimum))[1];winner=next(iter(optimum.values()))
        ck(score==n+1 and winner.count==1,'unique whole-path optimum')
        ck(at['max_boundary_occurrences']==1 and ot['max_masks']==2,'one live interface occurrence')
        total=r.total(all_scores.values())
        # An independent BRC recurrence for the number of independent sets of
        # a conflict path. Still positive BRC, not a non-BRC numeric baseline.
        previous,current=r.brc.CWM_ONE,r.merge(r.brc.CWM_ONE,r.brc.CWM_ONE)
        for _ in range(2,len(E)+1):previous,current=current,r.merge(previous,current)
        ck(total==current,'full score spectrum preserves every compatible assembly')
        path_runs.append({'n':n,'events':len(E),'occurrences':len(I),
             'compatible_assembly_C':total.count,'compatible_assembly_W':str(total.total),
             'maximum_selected':score,'unassigned_at_maximum':len(I)-3*score,
             'optimal_CWM':{'C':winner.count,'W':str(winner.total),'M':str(winner.dominant)},
             'exact_spectrum':serial_rows(all_scores),'full_sweep':at,'optimal_sweep':ot,
             'full_original_prefix_enumeration':n<=7})
    result={'schema':'EM_BRC_BOUNDARY_COMPOSITION_V1',
      'status':'CONDITIONAL_FORWARD_INTERFACE_NOT_NATIVE_DYNAMICS',
      'event_id':'EM-20261008-RESIDUAL-BOUNDARY-COMPOSITION-7C2E8A',
      'global_read':'8de6086e90d954b05672cbee20a5da5eb86bb741',
      'source_read':'1c1d4c19b0cfa5ab9b22cb0aae3fbfa93fefacf0',
      'fixed_three_module_cases':fixed,'boundary_probe_pairs':probes,
      'original_opt_repair':small,'release_counterexample':release,'paths':path_runs,
      'assertions':CHECKS,'BRC_calls':dict(r.CALLS),
      'old_suites_reexecuted':False,'recurrent_analysis_called':False,
      'native_release_permission_or_cost_supplied':False,
      'source_sensitive_or_release_language_covered_by_forward_quotient':False,
      'optimality_projection_preserves_sampling_weights':False,
      'independent_review':False}
    raw=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(raw)
    print(json.dumps({k:result[k] for k in ('status','assertions','BRC_calls','fixed_three_module_cases','boundary_probe_pairs')},indent=2))
    print('long path', {k: path_runs[-1][k] for k in ('events','occurrences','compatible_assembly_C','maximum_selected','unassigned_at_maximum')})
    print('interface maxima',at['max_entries'],ot['max_entries'])
    print('results bytes / SHA256',len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':main()
