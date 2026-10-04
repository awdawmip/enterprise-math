"""Exact new checks only; previous 38,815-check suite is not rerun."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json
import brc_three_route as r

ROOT=Path(__file__).parent
counts={}
def check(name, predicate):
    if not predicate:
        raise AssertionError(name)
    counts[name]=counts.get(name,0)+1

def scalar(v, values):
    return tuple(v*a for a in values)

def stable_cwm(paths, count, dominant):
    s=r.positive_summary(paths)
    return (s.count,s.total,s.dominant)==(count,F(1),dominant)

for index,x in enumerate(product((-1,0,1),repeat=6)):
    p=r.initial('cube-'+str(index),x)
    b=p[0].state; c=r.e.c12(b); h=r.e.c4(b)
    check('raw_gluing_zero',r.gluing_defect(c,h)==(0,0))
    paths=r.three_route(p)
    check('filter_visible_zero',r.c_observer(paths)==(0,)*4)
    check('filter_hidden_unchanged',r.h_observer(paths)==h)
    check('filter_positive_weights',stable_cwm(paths,3,F(1,3)))
    check('all_paths_integral_compatible',all(r.gluing_defect(r.e.c12(q.state),r.e.c4(q.state))==(0,0) for q in paths))
    check('all_branch_lengths_retained',all(r.e.native_length_square(q.state)==sum(v*v for v in x) for q in paths))
    check('root_and_path_identity',len({q.key for q in paths})==3 and all(q.state.source_id==b.source_id for q in paths))
    expected=(F(h[0],3),F(h[1],3),-F(h[0],3),-F(h[1],3),F(h[0],3),F(h[1],3))
    moment=r.raw_first_moment(paths)
    check('exact_projector_first_moment',moment==expected)
    check('single_cell_integrality_criterion',all(a.denominator==1 for a in moment)==(h[0]%3==0 and h[1]%3==0))
    echo=r.act(paths,('U',))
    check('echo_from_hidden',r.c_observer(echo)==r.unhide_coefficients(h))
    check('echo_vanishes_iff_hidden_zero',(r.c_observer(echo)==(0,)*4)==(h==(0,0)))
    twice=r.three_route(echo)
    check('mix_then_filter_hidden_third',r.h_observer(twice)==scalar(F(1,3),h))
    check('mix_then_filter_visible_zero',r.c_observer(twice)==(0,)*4)

# On arbitrary integer encoding tuples (not native inputs), the defect rotates.
for v in product(range(3),repeat=6):
    c,h=v[:4],v[4:]
    d=r.gluing_defect(c,h)
    nc,nh=r.e.observed_T(c,h)
    check('defect_transport',r.gluing_defect(nc,nh)==((-d[1])%3,d[0]))

# Repeated filtering has identical endpoint law but increasing path population.
seed=r.initial('filter-repeat',(1,0,0,0,0,0))
paths=seed; reference=None
repeated_filter=[]
for n in range(1,7):
    paths=r.three_route(paths)
    if reference is None: reference=r.endpoint_distribution(paths)
    check('endpoint_idempotence',r.endpoint_distribution(paths)==reference)
    check('filter_not_full_state_idempotent',stable_cwm(paths,3**n,F(1,3**n)))
    check('persistent_hidden',r.h_observer(paths)==(1,0))
    check('persistent_echo',r.c_observer(r.act(paths,('U',)))==(F(2,3),0,F(-2,3),0))
    repeated_filter.append({'generations':n,'paths':len(paths),'hidden':list(map(str,r.h_observer(paths)))})

# Any waiting word T^n leaves a nonzero hidden input recoverable by U.
for s,t in product(range(-2,3),repeat=2):
    paths=r.three_route(r.initial('delay',(s,t,0,0,0,0)))
    h=(s,t)
    for n in range(49):
        check('waiting_exact_echo',r.c_observer(r.act(paths,('U',)))==r.unhide_coefficients(h))
        check('waiting_hidden_no_decay',r.h_observer(paths)==h)
        paths=r.act(paths,('T',))
        h=(-h[1],h[0])

# Positive unequal route weights still preserve the hidden channel.
for weights in ((F(1,2),F(1,4),F(1,4)),(F(2,3),F(1,6),F(1,6))):
    paths=r.initial('unequal',(1,0,0,0,0,0)); lam=weights[0]-weights[1]
    for n in range(1,6):
        paths=r.three_route(paths,weights)
        check('unequal_visible_contraction',r.c_observer(paths)==(lam**n,0,0,0))
        check('unequal_hidden_unchanged',r.h_observer(paths)==(1,0))

# The explicit protocol U then E, starting after E, attenuates h by exactly 1/3.
paths=r.three_route(r.initial('attenuation',(1,0,0,0,0,0)))
attenuation=[]
for n in range(6):
    check('attenuation_exact',r.h_observer(paths)==(F(1,3**n),0))
    check('attenuation_echo',r.c_observer(r.act(paths,('U',)))==(F(2,3**(n+1)),0,F(-2,3**(n+1)),0))
    check('attenuation_mass_not_lost',stable_cwm(paths,3**(n+1),F(1,3**(n+1))))
    # All common T/U words through length four obey the future coefficient bound.
    bound=F(2,3**(n+1))
    for depth in range(5):
        for w in product(('T','U'),repeat=depth):
            check('common_future_bound',max(map(abs,r.c_observer(r.act(paths,w))))<=bound)
    # Path-dependent inverses restore all raw coordinates, not the past history.
    if n <= 3:
        restored=r.reverse_each_recorded_path(paths)
        check('path_sensitive_restore',all(p.state.x==(1,0,0,0,0,0) for p in restored))
        check('path_sensitive_observer_restore',r.c_observer(restored)==(1,0,0,0))
        check('restore_preserves_positive_population',stable_cwm(restored,3**(n+1),F(1,3**(n+1))))
    attenuation.append({'cycles':n,'paths':len(paths),'hidden':str(r.h_observer(paths)[0]),'echo_c0':str(r.c_observer(r.act(paths,('U',)))[0])})
    if n<5: paths=r.three_route(r.act(paths,('U',)))

# Classify every even sign mask generated by the existing T/U alphabet.
classes={'both_persistent':0,'one_attenuated':0,'both_attenuated':0}
mask_rows=[]; masks=set()
for bits in product((0,1),repeat=5):
    word,signs=r.even_sign_program(bits)
    masks.add(signs)
    factors=(F(sum(signs[::2]),3),F(sum(signs[1::2]),3))
    damped=sum(abs(v)<1 for v in factors)
    category=('both_persistent','one_attenuated','both_attenuated')[damped]
    classes[category]+=1
    for j in range(6):
        x=tuple(int(i==j) for i in range(6))
        transformed=r.act(r.initial('mask-basis',x),word)
        check('mask_word_realizes_diagonal',transformed[0].state.x==tuple(signs[i]*x[i] for i in range(6)))
    for j in (0,1):
        x=tuple(int(i==j) for i in range(6))
        p=r.three_route(r.initial('sandwich-basis',x))
        out=r.three_route(r.act(p,word))
        expected=tuple(factors[i]*int(i==j) for i in range(2))
        check('mask_filter_transfer',r.h_observer(out)==expected and r.c_observer(out)==(0,)*4)
    mask_rows.append({'signs':signs,'factors':list(map(str,factors)),'class':category,'TU_word_length':len(word)})
check('all_even_masks_covered',len(masks)==32 and all(sum(v==-1 for v in m)%2==0 for m in masks))
check('exact_mask_class_counts',classes=={'both_persistent':2,'one_attenuated':12,'both_attenuated':18})

# A weighted readout is not an integer Cell; the type guard must reject it.
try:
    r.gluing_defect((F(0),)*4,(F(1),F(0)))
except TypeError:
    check('rational_aggregate_not_integer_carrier',True)
else:
    raise AssertionError('weighted mean silently admitted')

files={}
for p in [ROOT/'brc_three_route.py',ROOT/'check_three_route.py',ROOT/'brc_x6_extension.py',ROOT/'source/brc_weighted.py']:
    data=p.read_bytes()
    files[str(p.relative_to(ROOT))]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
receipt={'schema':'BRC_THREE_ROUTE_FILTER_CERTIFICATE_V1','status':'MODEL_FINITE_CHECKS_PASSED_NOT_FORMALLY_ADMITTED',
 'base_model_commit':'9b4c1a0bc187f97ab4d0ca4bca2d96e57be867f3','source_cwm_commit':r.e.SOURCE_COMMIT,
 'source_cwm_blob':r.e.SOURCE_BLOB,'counts':counts,'total_assertions':sum(counts.values()),
 'source_CWM_calls':r.e.CALL_COUNTS,'mask_classes':classes,'mask_rows':mask_rows,'repeated_filter':repeated_filter,'attenuation':attenuation,'files':files,
 'scope':{'raw_cube':729,'waiting_inputs':25,'waiting_indices':'0..48','repeat_depth':'1..6','attenuation_cycles':'0..5','future_words':'all T/U words length <=4','path_sensitive_restore_cycles':'0..3'},
 'excluded_claims':['native triadic force law','Cell-gate/native X6 intertwiner','physical heartbeat timing','spatial transmission distance','physical energy dissipation','quantum entanglement','independent replication','whole repository tests'],
 'arithmetic':'Actual pinned CWM core and provenance-preserving T/U extension. No pi, trig, matrix exponential, Taylor/Pade/Cayley, or floating reference run.'}
(ROOT/'evidence/certificate.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
