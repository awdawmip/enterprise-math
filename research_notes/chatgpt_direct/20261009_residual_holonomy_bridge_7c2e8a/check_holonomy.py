"""Source-derived K4 connection lifted to positive CWM BRC.

Runs the new finite interface checks, not the historical V18 checker. The six
channels belong to the declared carrier model; physical axes/force are not
inferred. Endpoint, path, source channel and CWM remain typed separately.
"""
from __future__ import annotations
import ast
import hashlib
import json
import sys
import types
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raw = (ROOT / 'sources/brc_weighted.py').read_bytes()
blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
if blob != '3f205696709e847909958a153f8fe10d3f6b70f0':
    raise RuntimeError('BRC source pin mismatch')
tree = ast.parse(raw.decode())
removed = [n.module for n in tree.body if isinstance(n, ast.ImportFrom) and n.level]
if removed != ['brc_logarithm', 'exact_arithmetic']:
    raise RuntimeError('Unexpected package imports')
orig = [ast.dump(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
tree.body = [n for n in tree.body if not (isinstance(n, ast.ImportFrom) and n.level)]
assert orig == [ast.dump(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
brc = types.ModuleType('holonomy_pinned_positive_brc')
sys.modules[brc.__name__] = brc
exec(compile(tree, str(ROOT/'sources/brc_weighted.py'), 'exec'), brc.__dict__)
CALLS = Counter()
CHECKS = Counter()
V = ('A', 'B', 'C', 'D')
EDGES = (('A','B'), ('A','C'), ('A','D'), ('B','C'), ('B','D'), ('C','D'))
OPPOSITE = (5, 4, 3, 2, 1, 0)
IDENTITY = tuple(range(6))
EIDX = {e:i for i,e in enumerate(EDGES)}
# These literals are the inputs of the source T_NONFLAT rule (e,opposite(e)).
SOURCE_PIN = '00697049758a4d709f3fce00d356e58dc0d82fbb'
GLOBAL_PIN = '147dfe8735b97ca1db494d4aa40daeb86f69ead5'
EVENT = 'EM-20261009-RESIDUAL-HOLONOMY-BRIDGE-7C2E8A'


def check(ok, section):
    CHECKS[section] += 1
    if not ok:
        raise AssertionError(section)


def edge(a):
    CALLS['cwm_edge'] += 1
    return brc.cwm_edge(a)


def serial(a, b):
    CALLS['cwm_propagate'] += 1
    return brc.cwm_propagate(a, b)


def merge(a, b):
    CALLS['cwm_recoalesce'] += 1
    return brc.cwm_recoalesce(a, b)


def total(values):
    out = brc.CWM_ZERO
    for value in values:
        out = merge(out, value)
    return out


def put(out, key, val):
    if val.live:
        out[key] = merge(out.get(key, brc.CWM_ZERO), val)


def kernel(mapping):
    """BRC relation: input channel -> output channel, each allowed edge weight 1."""
    if sorted(mapping) != list(range(6)):
        raise ValueError('six-channel bijection required')
    return {(i,j): brc.CWM_ONE for i,j in enumerate(mapping)}


def compose(after, before):
    """Actual BRC serial relation composition, not a matrix-product fallback."""
    out = {}
    by_middle = {}
    for (middle, dest), weight in after.items():
        by_middle.setdefault(middle, []).append((dest, weight))
    for (source, middle), weight in before.items():
        for dest, following in by_middle.get(middle, ()):
            put(out, (source, dest), serial(weight, following))
    return out


def apply(K, state):
    """State keys retain (original source label,current channel)."""
    out = {}
    by_input = {}
    for (i,j), w in K.items():
        by_input.setdefault(i, []).append((j,w))
    for (source, i), w in state.items():
        for j, kw in by_input.get(i, ()):
            put(out, (source,j), serial(w,kw))
    return out


def seed(values, tag='input'):
    if len(values) != 6 or any(v < 0 for v in values):
        raise ValueError('six nonnegative rational channel budgets required')
    return {((tag,i),i):edge(v) for i,v in enumerate(values) if v > 0}


def channel_coefficients(state):
    return tuple(total(w for (_,j),w in state.items() if j == i) for i in range(6))


def vector(state):
    return tuple(w.total for w in channel_coefficients(state))


def cw(w):
    return {'C':w.count, 'W':str(w.total), 'M':str(w.dominant)}


def norm_readout(state):
    # Formal quadratic observation on the channel totals. These paired factors
    # are a declared algebraic diagnostic, not physical replicas or probabilities.
    return total(serial(w,w) for w in channel_coefficients(state)).total


def star_set(x):
    return frozenset(i for i,e in enumerate(EDGES) if x in e)


def detector(state, x, selected=None):
    selected = star_set(x) if selected is None else selected
    return total(w for (_,j),w in state.items() if j in selected)


def conn(x, y):
    i = EIDX[tuple(sorted((x,y)))]
    j = OPPOSITE[i]
    p = list(IDENTITY)
    p[i],p[j] = p[j],p[i]
    return kernel(tuple(p))


ID = kernel(IDENTITY)
P = kernel(OPPOSITE)
T = {(x,y):conn(x,y) for x in V for y in V if x != y}
U = {x:ID if x=='A' else T['A',x] for x in V}


def path_kernel(path):
    out = ID
    for x,y in zip(path,path[1:]):
        out = compose(T[x,y],out)
    return out


def transport(path, state):
    tr = [{'vertex':path[0], 'channels':list(map(str,vector(state))),
           'source_state':repr(sorted((str(k),cw(w)) for k,w in state.items()))}]
    for x,y in zip(path,path[1:]):
        state = apply(T[x,y],state)
        tr.append({'vertex':y,'channels':list(map(str,vector(state))),
                   'star_W':str(detector(state,y).total),
                   'source_state':repr(sorted((str(k),cw(w)) for k,w in state.items()))})
    return state,tr


def check_source_structure():
    perms=[]
    for labels in permutations(V):
        pv=dict(zip(V,labels))
        pe=tuple(EIDX[tuple(sorted((pv[x],pv[y])))] for x,y in EDGES)
        E=kernel(pe)
        perms.append((pv,E))
        for (x,y),k in T.items():
            check(compose(T[pv[x],pv[y]],E)==compose(E,k),'source_equivariance')
        for x in V:
            st=seed(tuple(1 if x in e else 0 for e in EDGES),('pf',x))
            moved=apply(E,st)
            check(vector(moved)==tuple(1 if pv[x] in e else 0 for e in EDGES),'source_pf_star')
    check(all(P != E for _,E in perms),'holonomy_not_structural_s4')
    for (x,y),k in T.items():
        check(compose(T[y,x],k)==ID,'reverse_edge')
        # Full graph consistency is checked by actual BRC relations.
        exponent=(1+int(x!='A')+int(y!='A'))%2
        normal=compose(U[y],compose(P if exponent else ID,U[x]))
        check(k==normal,'normal_form_local')
        # Source star profile transports to the complement at the next vertex.
        st=seed(tuple(1 if x in e else 0 for e in EDGES),'star_flip')
        check(vector(apply(k,st))==tuple(0 if y in e else 1 for e in EDGES),'star_flip')
    triangles=[]
    for x,y,z in permutations(V,3):
        path=(x,y,z,x)
        K=path_kernel(path)
        check(K==P,'triangle_holonomy')
        triangles.append({'path':path,'image':OPPOSITE})
    check(compose(P,P)==ID,'loop_order_two')
    return {'vertices':V,'channels':EDGES,'opposite':OPPOSITE,
            'structural_permutations':len(perms),'triangles':triangles}


def check_path_normal_form(max_edges=8):
    # Exhaustive finite support; provenance is each explicit word, not an
    # independently sampled transition. No old source checker is executed.
    stack=[(('A',),ID)]
    rows=[]
    counts=Counter()
    digest=hashlib.sha256()
    while stack:
        path,K=stack.pop()
        n=len(path)-1
        y=path[-1]
        parity=(n+int(y!='A'))%2
        expected=compose(U[y],P if parity else ID)
        check(K==expected,'all_path_normal_form')
        counts[(n,y)]+=1
        digest.update(repr((path,sorted(K),parity)).encode())
        if n<=3:
            rows.append({'path':path,'parity':parity,'image':sorted(K)})
        if n<max_edges:
            for nxt in V:
                if nxt!=y:
                    stack.append((path+(nxt,),compose(T[y,nxt],K)))
    return {'paths':sum(counts.values()),'max_edges':max_edges,'base':'A',
            'counts':[{'edges':n,'vertex':y,'count':v} for (n,y),v in sorted(counts.items())],
            'complete_path_check_digest':digest.hexdigest(),'short_explicit_paths':rows}


def check_profile_and_defect():
    rows=[]
    for a,b in product((0,1,2,3),repeat=2):
        family={x:seed(tuple(a if x in e else b for e in EDGES),('profile',x)) for x in V}
        for (x,y),k in T.items():
            v=vector(apply(k,family[x])); target=vector(family[y])
            check((v==target)==(a==b),'parallel_iff_equal')
            check(v==tuple(b if y in e else a for e in EDGES),'parallel_swaps_parameters')
        initial=family['A']
        end,trace=transport(('A','B','C','A'),initial)
        restored,_=transport(('A','B','C','A'),end)
        check(restored==initial,'two_loops_sourcewise_return')
        check(norm_readout(initial)==norm_readout(end),'quadratic_exact_invariance')
        check(total(initial.values())==total(end.values()),'positive_cwm_exact_invariance')
        check(detector(initial,'A').total==3*a and detector(end,'A').total==3*b,'fixed_detector_reveals_bit')
        check(all((p!=q)==(a!=b) for p,q in zip(vector(initial),vector(end))),'six_channel_change')
        rows.append({'a':a,'b':b,'before':list(map(str,vector(initial))),
                     'after':list(map(str,vector(end))),'quadratic':str(norm_readout(initial)),
                     'total_CWM':cw(total(initial.values())),
                     'detector_before':cw(detector(initial,'A')),
                     'detector_after':cw(detector(end,'A')),
                     'trace':trace if (a,b)==(1,2) else None})
    return rows


def check_observer_and_gauge():
    basic=seed((1,1,1,2,2,2),'gauge_seed')
    base_end=apply(P,basic)
    rows=[]
    # All base relabellings. Gauge laws are checked at the BRC kernel
    # and fixed observable levels; these are label changes, not physical steps.
    for p in permutations(range(6)):
        E=kernel(p)
        inverse=[0]*6
        for i,j in enumerate(p):inverse[j]=i
        Einv=kernel(inverse)
        Pg=compose(E,compose(P,Einv))
        st=apply(E,basic)
        end=apply(Pg,st)
        selected=frozenset(p[i] for i in star_set('A'))
        check(end==apply(E,base_end),'gauge_transport_commutes')
        check(Pg!=ID,'nonidentity_holonomy_survives_gauge')
        check(detector(st,'A',selected).total==3 and detector(end,'A',selected).total==6,'gauge_readout_invariant')
    for vals in product((1,2,3),repeat=6):
        st=seed(vals,'arbitrary_budget')
        moved=apply(P,st)
        coefficients=channel_coefficients(st)
        before=detector(st,'A').total
        after=detector(moved,'A').total
        check((before==after)==(before*2==total(st.values()).total),'star_visibility_criterion')
        # A star-only observer can miss a nontrivial full-channel change.
        if vals==(1,2,3,1,2,3):
            rows.append({'initial':vals,'after':list(map(str,vector(moved))),
                         'fixed_star_equal':before==after,'full_vector_equal':vector(st)==vector(moved)})
        for (x,y),k in T.items():
            nx=detector(st,x).total
            ny=detector(apply(k,st),y).total
            check(total((edge(nx),edge(ny))).total==total(st.values()).total,'star_observer_two_state_recurrence')
    for j in range(6):
        changed=dict(basic)
        put(changed,(('extra',j),j),edge(Q(1,3)))
        moved=apply(P,changed)
        delta=tuple(x-y for x,y in zip(vector(moved),vector(base_end)))
        check(delta==tuple(Q(1,3) if k==OPPOSITE[j] else 0 for k in range(6)),'single_channel_perturbation_is_not_dense')
        rows.append({'input_extra_channel':j,'output_difference':list(map(str,delta))})
    return {'all_base_gauges':720,'budget_tuples':729,'visibility_and_perturbation_witnesses':rows}


def check_same_length_paths_and_mixtures():
    # Equal six-step words remove word length as an explanation of the residual.
    triangle_twice=('A','B','C','A','B','C','A')
    square_then_back=('A','B','C','D','A','B','A')
    initial=seed((1,1,1,2,2,2),'mixed')
    a,_=transport(triangle_twice,initial); b,_=transport(square_then_back,initial)
    check(a==b==initial,'same_even_length_return')
    # Two equal length THREE-edge words cannot end at A with opposite parity.
    # Instead compare no-change identity via a branch hold operation of the same
    # declared clock cost only if such a clock exists; none is inferred here.
    # Readout comparisons in this unit concern current carrier state and paths.
    fam={}
    histories=[(('A',),Q(1,5)), (('A','B','C','A'),Q(3,10)),
               (triangle_twice,Q(1,2))]
    for path,w in histories:
        out=apply(path_kernel(path),initial)
        q=(len(path)-1)%2
        put(fam,q,edge(w))
    check(fam[0].total==Q(7,10) and fam[1].total==Q(3,10),'mixed_parity_weights')
    detector_expectation=total(serial(w,edge(3 if q==0 else 6)) for q,w in fam.items()).total
    check(detector_expectation==Q(39,10),'mixed_detector_expectation')
    full_channels = [brc.CWM_ZERO for _ in range(6)]
    reduced_channels = [brc.CWM_ZERO for _ in range(6)]
    for path,p in histories:
        out = apply(path_kernel(path),initial)
        for j,c in enumerate(channel_coefficients(out)):
            full_channels[j] = merge(full_channels[j],serial(edge(p),c))
    for q,p in fam.items():
        out = apply(P if q else ID,initial)
        for j,c in enumerate(channel_coefficients(out)):
            reduced_channels[j] = merge(reduced_channels[j],serial(p,c))
    check(full_channels == reduced_channels,'full_and_phase_compressed_CWM')
    check(total(full_channels).total == 9,'mixed_signal_budget')
    # Fixed input with provenance retained in the preparation table. The active
    # quotient is for source-blind current channel CWM observations and transport.
    return {'full_channel_CWM':list(map(cw,full_channels)),
            'compressed_channel_CWM':list(map(cw,reduced_channels)),
            'history_preparations':[{'path':p,'weight':str(w)} for p,w in histories],
            'parity_law':{str(q):cw(w) for q,w in sorted(fam.items())},
            'expected_fixed_star':str(detector_expectation)}


def main():
    structure=check_source_structure()
    paths=check_path_normal_form()
    profiles=check_profile_and_defect()
    gauges=check_observer_and_gauge()
    mixed=check_same_length_paths_and_mixtures()
    result={'schema':'EM_SOURCE_DERIVED_HOLONOMY_BRC_V1','event_id':EVENT,
            'status':'SOURCE_DERIVED_CONDITIONAL_UNREVIEWED',
            'source_read':SOURCE_PIN,'global_read':GLOBAL_PIN,
            'source_checker_blob':'32aa00fd8f36b7c5bf5285e4cec79499dec87509',
            'brc_blob':blob,'registration':'PENDING_PRIOR_PLATFORM_DENIAL_NOT_RETRIED',
            'source_structure':structure,'path_checks':paths,'profile_checks':profiles,
            'observer_checks':gauges,'mixed_input':mixed,
            'assertions':dict(CHECKS),'assertion_total':sum(CHECKS.values()),
            'BRC_calls':dict(CALLS),'old_main_suites_executed':False,
            'native_force_law_or_final_coordinate_mapping_supplied':False,
            'independent_review':False}
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    summary={'event_id':EVENT,'assertions':result['assertion_total'],
             'BRC_calls':result['BRC_calls'],'exhaustive_paths':paths['paths'],
             'base_gauges':gauges['all_base_gauges'],'profiles':len(profiles),
             'example':next(x for x in profiles if (x['a'],x['b'])==(1,2)),
             'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    (ROOT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
