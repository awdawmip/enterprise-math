from __future__ import annotations
import hashlib, itertools, json, pathlib, random, sys
from fractions import Fraction as Q
ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT/'vendor'/'enterprise_math'
if not SOURCE.is_dir(): SOURCE = ROOT.parents[1]/'src'/'enterprise_math'
DEFINITIONS = ROOT/'definitions'
if not DEFINITIONS.is_dir(): DEFINITIONS = ROOT.parents[1]/'definitions'
sys.path[:0] = [str(ROOT/'research'), str(SOURCE.parent)]
import heartbeat_algebra as h
from phase_algebra import Frame, FrameProgram, FramedEvent, analyze_fiber, synthesize_fiber, fiber_product
from enterprise_math.brc_transport import explicit_moment
from enterprise_math.brc_histogram import WeightHistogram
R = random.Random(26091941)
results = {}

def randvec(): return tuple(R.randint(-7, 7) for _ in range(6))
def measure_moment(atoms):
    counts = {}
    for w, z in atoms:
        bucket = counts.setdefault(z, {})
        bucket[w] = bucket.get(w, 0)+1
    return explicit_moment({z: WeightHistogram.from_counts(v) for z,v in counts.items()})

def rejected(call):
    try: call()
    except (ValueError, TypeError): return
    raise AssertionError('invalid operation was not rejected')

# Verbatim function excerpt from the recovered test source; not a full-suite replay.
def check_contract(c):
    req={'world_id':'HEARTBEAT_WORLD','world_name_zh':'心跳世界','total_dimension':7,'spatial_dimension':6,'time_dimension':1,'spatial_coordinate_system':'ENTERPRISE_NATIVE_X6','signed_primitive_direction_count':12,'native_axis_relation':'PAIRWISE_PERP_E','native_right_angle_degrees':120,'time_is_spatial_axis':False,'scale_is_complete_time':False,'phase_is_complete_time':False,'space_return_is_event_return':False,'fixed_heartbeat_program':None,'research_examples_are_world_axioms':False}
    for k,v in req.items():
        if type(c.get(k)) is not type(v) or c[k]!=v: raise ValueError(k)
    if c['raw_spatial_fields']!={'count':6,'domain':'SIGNED_INTEGER','scope':'CHART_RELATIVE_DISPLACEMENT'}: raise ValueError('raw chart')
    if c['final_cell_address']['count']!=6 or c['final_cell_address']['domain']!='NONNEGATIVE_INTEGER': raise ValueError('final address')

expected = {
'research/heartbeat_algebra.py': 'c8d0b73a805740075e9b485d53e3b9ab71636490',
'vendor/enterprise_math/brc_transport.py': 'be1debe367263931bd5e93fd750be3ed54624fe1',
'vendor/enterprise_math/brc_histogram.py': '9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
'vendor/enterprise_math/predictive_quotient.py': 'f27d9ddf908f5b07051acfaf0c69f359d499b98b',
'definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json': '77bc5e6e018057063130b3999e3c0ccaaf4fa5f5'}
for path, wanted in expected.items():
    file = ROOT/path
    if path.startswith('vendor/enterprise_math/'):
        file = SOURCE/path.split('/')[-1]
    elif path.startswith('definitions/'):
        file = DEFINITIONS/path.split('/')[-1]
    s = file.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(s)).encode()+b'\0'+s).hexdigest() == wanted
results['source_identity'] = {'full_files_checked': 5, 'hashes': expected}

contract = json.loads((DEFINITIONS/'HEARTBEAT_WORLD_NATIVE_X6_TIME.json').read_text())
check_contract(contract)
for k, v in [('spatial_dimension',3), ('total_dimension',6), ('time_dimension',6),
             ('time_is_spatial_axis',True), ('native_right_angle_degrees',90),
             ('fixed_heartbeat_program',12), ('spatial_dimension',True)]:
    bad = dict(contract); bad[k] = v
    rejected(lambda: check_contract(bad))
results['world_contract'] = {'valid':True, 'invalid_mutations_rejected':7}

for _ in range(600):
    f = Frame(R.randrange(13), R.choice((2,3,4,5,7)))
    x,y,z=randvec(),randvec(),randvec()
    a,b,c=f.encode(x),f.encode(y),f.encode(z)
    assert f.decode(a)==x
    assert f.product(a,b)==f.folded_product(a,b)==f.encode(h.multiply(x,y,f.b))
    assert f.product(a,b)==f.product(b,a)
    assert f.product(f.product(a,b),c)==f.product(a,f.product(b,c))
    assert f.product(a,h.add(b,c))==h.add(f.product(a,b),f.product(a,c))
    assert f.product(a,f.unit)==a
results['transported_ring']={'random_triples':600,'radices':[2,3,4,5,7],'depths':'0..12','two_product_algorithms_agree':True}

x,y=randvec(),randvec()
for i,p in enumerate(itertools.permutations(range(6))):
    f=Frame(i%13,2,p)
    assert f.decode(f.product(f.encode(x),f.encode(y)))==h.multiply(x,y)
results['axis_relabeling']={'positive_axis_permutations':720,'algebra_transported_not_fixed':True}

for _ in range(500):
    b=R.choice((2,3,4,5,7));j=R.randrange(13);x,y=randvec(),randvec()
    a,c=analyze_fiber(x,j,b),analyze_fiber(y,j,b)
    assert synthesize_fiber(*a,b)==x
    assert fiber_product(a,c,b)==analyze_fiber(h.multiply(x,y,b),j,b)
results['coarse_residue_product']={'signed_pairs':500,'max_depth':12,'no_residue_dropped':True}

breathing=FrameProgram((0,1,2,3,4,5,6,5,4,3,2,1))
plain=FrameProgram((0,))
for initial in (h.ONE,h.add(h.ONE,h.LAM),randvec()):
    pulse=FramedEvent.from_material(initial,0,breathing)
    identity=FramedEvent.from_material(initial,0,breathing)
    base=FramedEvent.from_material(initial,0,plain)
    for _ in range(8):
        pulse=pulse.advance(h.ONE,square=True)
        base=base.advance(h.ONE,square=True)
        identity=identity.advance()
        assert pulse.material()==base.material()
        assert identity.material()==initial
    assert pulse.tick==8
results['nonlinear_evolution_covariance']={'initial_states':3,'steps_per_state':8,'material_U':'x*x+1','baseline_and_breathing_identical_material_evolution':True}

f=Frame(1);a=f.encode(h.ONE)
assert a==h.LAM
assert f.product(a,a)==h.LAM
assert h.multiply(a,a)==(0,0,1,0,0,0)
results['false_frame_dynamics_witness']={'phase_depth':1,'encoded_material_one':a,'correct_same_phase_product':f.product(a,a),'incorrect_static_formula':h.multiply(a,a)}

mu=[(Q(1,2),h.neg(h.ONE)),(Q(1,2),h.ONE)]
nu=[(Q(1,8),h.scale(-2,h.ONE)),(Q(3,4),h.ZERO),(Q(1,8),h.scale(2,h.ONE))]
assert measure_moment(mu)==measure_moment(nu)
sq=lambda dist:[(w,h.multiply(z,z)) for w,z in dist]
m,n=measure_moment(sq(mu)),measure_moment(sq(nu))
assert m[0][6]==n[0][6]==1 and m[0][0]==1 and n[0][0]==4
results['quadratic_moment_boundary']={'equal_input_degree2_moments':True,'next_first_moments':[str(m[0][6]),str(n[0][6])],'next_second_moments':[str(m[0][0]),str(n[0][0])],'moment_degree_sufficient_after_K_steps':'2^(K+1), not asserted minimal'}

shared=[(Q(1,2),z,z) for z in (h.neg(h.ONE),h.ONE)]
independent=[(Q(1,4),x,y) for x in (h.neg(h.ONE),h.ONE) for y in (h.neg(h.ONE),h.ONE)]
for side in (1,2):
    assert measure_moment([(w,row[side]) for row in shared for w in [row[0]]])==measure_moment([(w,row[side]) for row in independent for w in [row[0]]])
a=measure_moment([(w,h.multiply(x,y)) for w,x,y in shared])
b=measure_moment([(w,h.multiply(x,y)) for w,x,y in independent])
assert a[0][6]==1 and b[0][6]==0
results['joint_BRC_multiplication']={'equal_input_marginals':True,'shared_sign_product_mean':'1','independent_sign_product_mean':'0','positive_mass_preserved':str(a[6][6])==str(b[6][6])=='1'}

v=FramedEvent.from_material(h.ONE,0,breathing)
rejected(lambda: v.product(FramedEvent.from_material(h.ONE,12,breathing)))
rejected(lambda: Frame(1).decode(h.ONE))
rejected(lambda: Frame(1).product(h.ONE,h.LAM))
rejected(lambda: Frame(1,permutation=(0,0,1,2,3,4)))
rejected(lambda: Frame(True))
rejected(lambda: v.advance(square=1))
rejected(lambda: Frame(1).decode((0.0,1,0,0,0,0)))
rejected(lambda: fiber_product((h.ZERO,(0,)),(h.ZERO,(0,0))))
results['invalid_ports_and_domains']={'rejected':8,'same_phase_later_time_not_same_event':True}

payload={'schema':'HEARTBEAT_PHASE_ALGEBRA_VALIDATION_V1','status':'PASS','check_groups':len(results),'seed':26091941,'results':results,'limits':['research adapter, not production or Foundation','no whole-project suite or independent referee','fixed frame program; no new physical law','no generic finite-memory guarantee','prior 15-group suite consumed, not recounted as this run']}
text=json.dumps(payload,ensure_ascii=False,indent=2)+'\n'
(ROOT/'research/PHASE_RESULTS.json').write_text(text)
print(text)
