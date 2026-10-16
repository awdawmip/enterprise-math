"""R1-01 source-restatement instance; execute once only under own Native admission."""
from __future__ import annotations
import copy, hashlib, importlib, itertools, json, sys, types
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'outputs'
STATES = tuple(itertools.product((0, 1), repeat=3))
NAMES = ('s1', 's2', 's3')
PORT = 'tetrahedron.chart0'

def sid(x):
    return ''.join(map(str, x))

def tagged(x):
    return {'type': 'F2^3', 'value': list(x)}

def state(x):
    if not isinstance(x, dict) or set(x) != {'type', 'value'} or x['type'] != 'F2^3':
        raise ValueError('explicit F2^3 state tag required')
    v = x['value']
    if not isinstance(v, list) or len(v) != 3 or any(type(a) is not int or a not in (0, 1) for a in v):
        raise ValueError('three strict integer bits required')
    return tuple(v)

def action(name, x):
    p, q, e = x
    if name == 's1': return (p, p ^ q, e ^ p)
    if name == 's2': return (q, p, e)
    if name == 's3': return (p, p ^ q, e)
    raise ValueError('unknown operation')

def matching(x):
    p, q, _ = x
    return (p, q, p ^ q)

def stars(x):
    p, q, e = x
    return (e, e ^ p, e ^ q, e ^ p ^ q)

def integer_edge(x):
    if not isinstance(x, dict) or set(x) != {'type', 'value'} or x['type'] != 'E0(Z)':
        raise ValueError('integral lifting requires E0(Z), never a mod-two state')
    v = x['value']
    if not isinstance(v, list) or len(v) != 6 or any(type(a) is not int for a in v) or sum(v) != 0:
        raise ValueError('six strict integers of total zero required')
    return tuple(v)

def integral_observation(x):
    a, b, c, d, e, f = integer_edge(x)
    return ((a + f, b + e, c + d), (a + b + c) % 2)

def integral_legal(x):
    m, e = integral_observation(x)
    return m == (0, 0, 0) and e == 0

def validate_fixture(f):
    if f.get('type') != 'F2^3_SOURCE_RESTATEMENT' or f.get('state_order') != [list(x) for x in STATES]:
        raise ValueError('exact finite carrier/order required')
    for name in NAMES:
        d = f['operations'][name]
        if d.get('source') != PORT or d.get('target') != PORT:
            raise ValueError('operation source/target port mismatch')
        if set(d.get('enabled', {})) != {sid(x) for x in STATES}:
            raise ValueError('enabledness must be explicit for every state')
        for x in STATES:
            if type(d['enabled'][sid(x)]) is not bool:
                raise ValueError('enabledness must be boolean')
            y = state(d['transition'][sid(x)])
            if d['enabled'][sid(x)] is not True or y != action(name, x):
                raise ValueError('this frozen generator is total and source-defined')
    return True

def rejection(fn):
    try: fn()
    except (ValueError, TypeError, KeyError): return True
    return False

def main():
    OUT.mkdir(exist_ok=True)
    # Load exact existing components with their relative import structure intact.
    # The repository aggregate __init__ imports unrelated methods; it is not needed.
    package = types.ModuleType('gbrc_existing_components')
    package.__path__ = [str(ROOT / 'scientific_tools/src/enterprise_math')]
    sys.modules[package.__name__] = package
    pq = importlib.import_module(package.__name__ + '.partial_operation_quotient')
    cc = importlib.import_module(package.__name__ + '.composition_safe_collapse')
    operations = {name: {x: action(name, x) for x in STATES} for name in NAMES}
    fixture = {'type': 'F2^3_SOURCE_RESTATEMENT', 'vertices': ['A','B','C','D'],
      'edge_order': ['AB','AC','AD','BC','BD','CD'], 'state_order': [list(x) for x in STATES],
      'action_convention': 'left action; first a then b means F_b(F_a(x))',
      'operations': {n: {'source': PORT, 'target': PORT, 'enabled': {sid(x): True for x in STATES},
          'transition': {sid(x): tagged(action(n,x)) for x in STATES}} for n in NAMES},
      'observations': {sid(x): {'matching_mod2': list(matching(x)), 'e': x[2],
          'all_star_mod2': list(stars(x))} for x in STATES},
      'integral_model': {'V0': '{v in Z^4 : sum(v)=0}', 'E0': '{x in Z^6 : sum(x)=0}',
          'delta': '(v_i+v_j) in frozen edge order', 'R': 'E0/delta(V0)',
          'm': '(x_AB+x_CD,x_AC+x_BD,x_AD+x_BC)', 'e': '(x_AB+x_AC+x_AD) mod 2',
          'N': '(e,0,0,-p-q,q,p-e), p,q in Z and e in {0,1}',
          'integer_lift_boundary': 'm=(0,0,0) over Z and e=0; mod-two m=0 is insufficient'},
      'evidence': 'Original PROGRAM restatement; September 11 PDF itself unavailable, not full-PDF verified',
      'novelty': 'Typed integration and negative-input fixture; old 2/4/8 is regression only',
      'native_X6_bridge': 'NOT_CONSTRUCTED; tetrahedral edges and F2^3 are external carriers'}
    schema = {'schema': 'GBRC_R101_INSTANCE_SCHEMA_V1', 'evidence_status': 'SOURCE_RESTATEMENT_TYPED_INTEGRATION',
      'X': {'type': 'finite_set', 'carrier': 'F2^3', 'encoding': 'explicit tag plus three strict integer bits'},
      'G': {'type': 'geometric_ports_charts', 'values': [PORT], 'not_group_G': True},
      'q': {'source': 'X', 'target': '{(p,q,p+q) in F2^3}', 'formula': 'matching_mod2'},
      'A': {'type': 'operation_alphabet', 'values': list(NAMES)},
      'F': {'source': 'D_a subset X', 'target': 'X', 'ports': PORT + ' -> ' + PORT,
          'enabledness': 'explicit total bool table; D_a=X for these frozen generators'},
      'O': {'source': 'X', 'targets': ['matching F2^3', 'star bit F2', 'all-star F2^4'],
          'formulas': ['(p,q,p+q)', 'e', '(e,e+p,e+q,e+p+q)'], 'readout_types_preserved': True},
      'W': {'type': 'positive_rational_branch_metadata', 'this_instance': 'one branch weight 1',
          'interpretation': 'unit gain; not asserted probability normalization or signed cancellation'},
      'R': {'general_type': 'q-fiber sets', 'integral_type': 'E0(Z)/delta(V0(Z))',
          'finite_torsion_type': 'F2^3; no automatic real-valued residual norm'},
      'encode': {'source': 'X', 'target': 'tagged strict bit triple', 'map': 'identity with explicit type', 'lossless': True},
      'H': {'language': 'all finite words over s1,s2,s3', 'declared_regression_horizons': [0,1,2],
          'unbounded_claim': 'only existing finite deterministic congruence theorem, not integral/native dynamics'},
      'all_functions': ['state: tagged F2^3 -> X, rejects all malformed tags/bits',
          'F_a: X -> X with explicit enabledness and geometric port compatibility',
          'integer_edge: tagged E0(Z) -> six strict integers of total zero',
          'integral_observation: E0(Z) -> {m in Z^3:sum(m)=0} x F2',
          'integral_legal: E0(Z) -> bool; no F2-to-Z implicit coercion'],
      'missing_maps': ['native X6 comparison', 'arbitrary torsion-to-real norm', 'general affine transport outside supplied assumptions'],
      'reuse': {'partial_operation_quotient': 'REUSE_EXECUTED', 'composition_safe_collapse': 'REUSE_EXECUTED',
          'new_generic_quotient_engine': False}, 'independence': 'own author; directed context; second independent reconstruction pending'}
    checks = {}
    checks['fixture_reconstructs_all_8_states_and_24_generator_edges'] = validate_fixture(fixture)
    checks['all_three_generators_are_involutions'] = all(action(n,action(n,x)) == x for n in NAMES for x in STATES)
    checks['all_star_formula_agrees_with_integral_normal_representative'] = all(
      tuple(z % 2 for z in (x[2], x[2]-x[0], -x[1]-x[2], x[0]+x[1]-x[2])) == stars(x) for x in STATES)
    stages = pq.partial_family_future_partition_sequence(STATES, operations, {x:x[2] for x in STATES})
    counts = [len(set(p.values())) for p in stages]
    checks['old_2_4_8_regression_only'] = counts == [2,4,8]
    checks['matching_is_compatible'] = pq.partial_family_descends(STATES, operations, {x:matching(x) for x in STATES})
    checks['matching_does_not_determine_star'] = not cc.descends_through(STATES, {x:matching(x) for x in STATES}, {x:x[2] for x in STATES})
    bad = copy.deepcopy(fixture); del bad['operations']['s1']['enabled']['000']
    checks['reject_missing_enabledness'] = rejection(lambda: validate_fixture(bad))
    bad_port = copy.deepcopy(fixture); bad_port['operations']['s1']['target']='other.chart'
    checks['reject_illegal_source_target'] = rejection(lambda: validate_fixture(bad_port))
    checks['reject_bool_as_integer_bit'] = rejection(lambda: state({'type':'F2^3','value':[False,0,0]}))
    checks['reject_nonbinary_state'] = rejection(lambda: state(tagged((2,0,0))))
    checks['reject_untagged_state'] = rejection(lambda: state([0,0,0]))
    checks['reject_mod2_as_integral_lift'] = rejection(lambda: integral_legal(tagged((0,0,0))))
    checks['reject_nonintegral_edge'] = rejection(lambda: integral_legal({'type':'E0(Z)','value':[0.0,0,0,0,0,0]}))
    checks['reject_wrong_integer_lattice'] = rejection(lambda: integral_legal({'type':'E0(Z)','value':[1,0,0,0,0,0]}))
    counter = {'type':'E0(Z)','value':[0,0,0,-2,0,2]}
    checks['mod2_zero_is_not_integer_zero'] = integral_observation(counter) == ((2,0,-2),0) and not integral_legal(counter)
    checks['reject_partial_target_outside_domain_existing_tool'] = rejection(lambda: pq.partial_family_descends(STATES, {'bad':{STATES[0]:(9,0,0)}}, {x:0 for x in STATES}))
    checks['existing_tool_detects_enabledness_erasure'] = not pq.partial_operation_descends(STATES, {STATES[0]:STATES[0]}, {x:0 for x in STATES})
    checks['zero_integer_lift_legal'] = integral_legal({'type':'E0(Z)','value':[0]*6})
    fixture['regression_actual'] = {'old_class_counts':counts, 'new_theorem':False}
    for name, data in [('instance_schema.json',schema),('tetrahedron_fixture.json',fixture)]:
        (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    result={'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'check_count':len(checks),
      'claims':'one author exact integration/check; not independent replication, full PDF verification or new theorem',
      'tool_source_manifest':'SCIENTIFIC_TOOL_EXACT_CURRENT_SOURCE_MANIFEST.json'}
    (OUT/'exact_test_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    return 0 if all(checks.values()) else 1

if __name__ == '__main__':
    raise SystemExit(main())
