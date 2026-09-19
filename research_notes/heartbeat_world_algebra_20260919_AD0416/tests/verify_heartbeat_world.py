from __future__ import annotations
import hashlib, itertools, json, pathlib, random, sys, time
from fractions import Fraction as F

ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE=ROOT/'vendor'/'enterprise_math'
if not SOURCE.is_dir(): SOURCE=ROOT.parents[1]/'src'/'enterprise_math'
DEFINITIONS=ROOT/'definitions'
if not DEFINITIONS.is_dir(): DEFINITIONS=ROOT.parents[1]/'definitions'
sys.path[:0]=[str(SOURCE.parent),str(ROOT/'research')]
from heartbeat_algebra import *
from enterprise_math.brc_transport import eye, mm, mpow, point_moment
from enterprise_math.brc_histogram import histogram_serial
R=random.Random(190926)
checks={}
def randvec(): return tuple(R.randint(-9,9) for _ in range(6))
def check_contract(c):
    req={'world_id':'HEARTBEAT_WORLD','world_name_zh':'心跳世界','total_dimension':7,'spatial_dimension':6,'time_dimension':1,'spatial_coordinate_system':'ENTERPRISE_NATIVE_X6','signed_primitive_direction_count':12,'native_axis_relation':'PAIRWISE_PERP_E','native_right_angle_degrees':120,'time_is_spatial_axis':False,'scale_is_complete_time':False,'phase_is_complete_time':False,'space_return_is_event_return':False,'fixed_heartbeat_program':None,'research_examples_are_world_axioms':False}
    for k,v in req.items():
        if type(c.get(k)) is not type(v) or c[k]!=v: raise ValueError(k)
    if c['raw_spatial_fields']!={'count':6,'domain':'SIGNED_INTEGER','scope':'CHART_RELATIVE_DISPLACEMENT'}: raise ValueError('raw chart')
    if c['final_cell_address']['count']!=6 or c['final_cell_address']['domain']!='NONNEGATIVE_INTEGER': raise ValueError('final address')

expected={'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1','brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1','predictive_quotient.py':'f27d9ddf908f5b07051acfaf0c69f359d499b98b'}
for name,h in expected.items():
    s=(SOURCE/name).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(s)).encode()+b'\0'+s).hexdigest()==h
checks['source_reuse']=expected

c=json.loads((DEFINITIONS/'HEARTBEAT_WORLD_NATIVE_X6_TIME.json').read_text())
check_contract(c)
for k,v in [('spatial_dimension',3),('time_dimension',7),('time_is_spatial_axis',True),('native_right_angle_degrees',90),('fixed_heartbeat_program',12),('world_name_zh','六维心跳场')]:
    bad=dict(c);bad[k]=v
    try: check_contract(bad)
    except ValueError: pass
    else: raise AssertionError(k)
checks['contract']={'valid':True,'mutant_rejections':6}

basis=[tuple(int(i==j) for i in range(6)) for j in range(6)]
for b in (2,3,4,5,7):
    A=multiplication_matrix(LAM,b)
    assert mpow(A,6)==matrix([[b*int(i==j) for j in range(6)] for i in range(6)])
    for i in range(6): assert beats(ONE,i,b)==basis[i]
    for i,j in itertools.product(range(6),repeat=2):
        assert multiply(basis[i],basis[j],b)==scale(b**((i+j)//6),basis[(i+j)%6])
checks['cyclic_representation']={'radices':[2,3,4,5,7],'basis_products':180,'minimal_degree':6}

N=2400
for _ in range(N):
    b=R.choice((2,3,4,5,7));x,y,z=randvec(),randvec(),randvec()
    assert multiply(x,y,b)==multiply(y,x,b)
    assert multiply(multiply(x,y,b),z,b)==multiply(x,multiply(y,z,b),b)
    assert multiply(x,add(y,z),b)==add(multiply(x,y,b),multiply(x,z,b))
    assert multiply(x,ONE,b)==x and add(x,neg(x))==ZERO
    assert multiply(beat(x,b),y,b)==beat(multiply(x,y,b),b)
    assert multiply(beat(x,b),beat(y,b),b)==beats(multiply(x,y,b),2,b)
checks['ring_laws']={'random_triples':N,'laws':['commutative','associative','distributive','unit','additive_inverse','degree_transport']}

for _ in range(120):
    b=R.choice((2,3,5));x,y=randvec(),randvec()
    assert multiplication_matrix(multiply(x,y,b),b)==mm(multiplication_matrix(x,b),multiplication_matrix(y,b))
    assert norm(multiply(x,y,b),b)==norm(x,b)*norm(y,b)
    n,d=divide_readout(x,y,b)
    assert multiply(n,y,b)==scale(d,x)
checks['division_and_norm']={'random_cases':120,'lambda_norm':norm(LAM),'scalar_two_norm':norm(scale(2,ONE)),'one_plus_lambda_norm':norm(add(ONE,LAM))}
assert divide_readout(ONE,LAM)==((0,0,0,0,0,1),2)
assert divide_readout(ONE,add(ONE,LAM))==((-1,1,-1,1,-1,1),1)
for z in itertools.product((-1,0,1),repeat=6):
    n,d=divide_readout(z,add(ONE,LAM))
    assert d==1 and multiply(n,add(ONE,LAM))==z
checks['unit_division']={'exhaustive_vectors':729,'inverse_one_plus_lambda':[-1,1,-1,1,-1,1]}

u=(-2,0,0,1,0,0);v=(2,0,0,1,0,0)
assert multiply(u,v,4)==ZERO and u!=ZERO and v!=ZERO
try: divide_readout(ONE,u,4)
except ValueError: pass
else: raise AssertionError('zero divisor inverse must reject')
checks['nonfield_counterexample']={'b':4,'left':list(u),'right':list(v),'product':list(ZERO)}

for _ in range(5000):
    b=R.choice((2,3,4,5,7));x,y=randvec(),randvec()
    q,r=analyze(x,b);p,s=analyze(y,b)
    assert synthesize(q,r,b)==x
    assert lift_add(q,r,p,s,b)==analyze(add(x,y),b)
    assert lift_subtract(q,r,p,s,b)==analyze(add(x,neg(y)),b)
    assert lift_multiply(q,r,p,s,b)==analyze(multiply(x,y,b),b)
checks['residue_arithmetic']={'random_pairs':5000,'operations':['reconstruction','addition','subtraction','multiplication'],'carry_axis':6}

A=multiplication_matrix(LAM)
H=Affine(A,ZERO)
Tu=Affine(eye(6),basis[0]);Tv=Affine(eye(6),basis[1])
assert Tu.then(H)==H.then(Affine(eye(6),beat(basis[0])))
left=H.then(Tu).then(H).then(Tv).apply(ZERO)
right=H.then(Tv).then(H).then(Tu).apply(ZERO)
assert left==(0,2,0,0,0,0) and right==(1,0,1,0,0,0)
for _ in range(300):
    k,l,m=[R.randrange(8) for _ in range(3)];u,v,w=randvec(),randvec(),randvec()
    def join(a,b):
        k,u=a;l,v=b
        return k+l,add(beats(u,l),v)
    assert join(join((k,u),(l,v)),(m,w))==join((k,u),join((l,v),(m,w)))
checks['timed_order']={'random_associativity_triples':300,'u_then_v':list(map(int,left)),'v_then_u':list(map(int,right))}

h6=TimedAffine(0,6,Affine(mpow(A,6),ZERO))
s2=TimedAffine(0,1,Affine(mpow(A,6),ZERO))
assert h6.effect==s2.effect and h6.end!=s2.end
forward=TimedAffine(0,1,H);backward_spatial=TimedAffine(1,1,H.inverse())
event=forward.then(backward_spatial).apply((0,basis[0]))
assert event==(2,basis[0])
try: forward.then(TimedAffine(2,1,H))
except ValueError: pass
else: raise AssertionError('mismatched time ports accepted')
checks['space_vs_event_identity']={'same_space_different_end_times':[6,1],'spatial_inverse_return_time':event[0]}

packets=[]
for t in range(6):
    effects=EffectHistogram.from_terms(6,[(F(1,2),Affine(A,ZERO),1),(F(1,2),Affine(A,ONE),1)])
    packets.append(TimedPacket(t,1,effects))
whole=packets[0]
for p in packets[1:]:whole=whole.then(p)
raw={ZERO:F(1)}
for _ in range(6):
    nxt={}
    for x,w in raw.items():
        for r in (0,1):
            y=add(beat(x),scale(r,ONE));nxt[y]=nxt.get(y,F())+w/2
    raw=nxt
out=whole.effects.evaluate(ZERO)
assert {x:h.total_mass for x,h in out.items()}==raw
assert len(out)==64 and whole.effects.forget_effects().count==64
assert whole.effects.forget_effects().total_mass==1
# Alternative means alternative branches, not addition of the spatial effects.
alt=packets[0].alternatives(packets[0])
assert alt.effects.forget_effects().count==4 and alt.effects.forget_effects().total_mass==2
p,q,r=packets[:3]
assert p.then(q.alternatives(q))==p.then(q).alternatives(p.then(q))
assert p.then(q).then(r)==p.then(q.then(r))
try: p.alternatives(TimedPacket(0,2,p.effects))
except ValueError: pass
else: raise AssertionError('incompatible branch time ports')
checks['BRC_time_ports']={'literal_paths':64,'mass':'1','temporal_associativity_and_distribution':True,'incompatible_ports_rejected':True}

orders={}
for M in (3,5,7,9,11,13,17,19,25,27):
    u=2%M;r=1
    while u!=1:u=u*2%M;r+=1
    expected=6*r
    a=ONE
    for k in range(1,expected+1):
        a=tuple(v%M for v in beat(a))
        assert (a==ONE)==(k==expected)
    orders[str(M)]=expected
for k in range(1,9):
    assert any(v%(2**k) for v in beats(ONE,6*k-1))
    assert not any(v%(2**k) for v in beats(ONE,6*k))
checks['modular_dynamics']={'odd_modulus_order':orders,'two_power_nilpotent_cases':8,'rule':'6*k for modulus 2^k; residue erasure, not full-state annihilation'}

from enterprise_math.predictive_quotient import predictive_block_profile
profile=predictive_block_profile(tuple(range(64)), {'contract': lambda x:x//2}, lambda x:x%2, 6)
assert profile==(2,4,8,16,32,64,64)
checks['predictive_digit_horizon']={'raw_states':64,'profile':list(profile),'observer':'parity','future':'floor division by 2'}

# A heartbeat-induced product is not automatically invariant under all native axis relabelings.
positive_automorphisms=[]
signed_automorphisms=[]
for perm in itertools.permutations(range(6)):
    for signs in itertools.product((-1,1), repeat=6):
        def image(v):
            out=[0]*6
            for i,a in enumerate(v): out[perm[i]]=signs[i]*a
            return tuple(out)
        if image(ONE)!=ONE: continue
        if all(image(multiply(basis[i],basis[j]))==multiply(image(basis[i]),image(basis[j])) for i,j in itertools.product(range(6),repeat=2)):
            signed_automorphisms.append((perm,signs))
            if signs==(1,)*6: positive_automorphisms.append(perm)
assert positive_automorphisms==[tuple(range(6))]
assert len(signed_automorphisms)==2
checks['axis_symmetry_boundary']={'signed_axis_permutations_scanned':46080,'positive_axis_permutations':720,'positive_ring_automorphisms':1,'signed_ring_automorphisms':2,'scope':'chosen multiplication, not reduction of native geometric S6'}

invalid=[lambda:vector((1,2,3)),lambda:vector((True,0,0,0,0,0)),lambda:beat(ZERO,1),lambda:beats(ONE,-1),lambda:synthesize(ZERO,2,2),lambda:divide_readout(ONE,ZERO),lambda:TimedAffine(-1,1,H)]
for fn in invalid:
    try:fn()
    except (TypeError,ValueError,ZeroDivisionError):pass
    else:raise AssertionError('bad input accepted')
checks['invalid_input_rejections']=len(invalid)

result={'status':'PASS','check_groups':len(checks),'random_seed':190926,'checks':checks,'scope':'new algebraic construction under a chosen integer heartbeat, not universal intrinsic multiplication or production integration','independent_review':False,'full_project_tests':False}
path=ROOT/'research'/'RESULTS.json'
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
