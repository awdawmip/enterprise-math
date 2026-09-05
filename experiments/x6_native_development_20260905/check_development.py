"""Primary exact self-check; finite checks do not replace the proofs."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import random
import x6_development as x

ROOT=x.Cell()
EVENTS=tuple(x.Event(v,w,s) for v in range(4) for w in x.neighbours(v) for s in (-1,1))
counts=Counter()

def need(p,name):
    if not p: raise AssertionError(name)
    counts[name]+=1

def serial(c):
    return [[s.chart,*s.move.positive_decode()] for s in c.syllables]

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def mv(a,v): return tuple(sum(a[i][j]*v[j] for j in range(3)) for i in range(3))

# All short signed event histories, not just all distinct endpoints.
h=hashlib.sha256(); profile=[]
for length in range(4):
    ends=set(); ret=0; carr=Counter()
    for digits in product(range(24),repeat=length):
        p=x.PacketPath(ROOT,tuple(EVENTS[i] for i in digits))
        e=p.endpoint; ends.add(e); ret+=e==ROOT; carr[e.carrier_readout()]+=1
        h.update((json.dumps(serial(e),separators=(',',':'))+'\n').encode())
        need(p.event_count==length,'ordered_history_length')
        need(e.multiply(e.inverse())==ROOT,'endpoint_inverse')
    profile.append({'length':length,'histories':24**length,'endpoints':len(ends),'returns':ret,'carrier_points':len(carr)})

# Existing exact atlas matrices are reused, not rewritten.
for g in x.GROUP:
    for v in range(4):
        for a,b in product(range(-3,4),repeat=2):
            m=x.LocalMove(a,b)
            need(m.rotate(v,g).gauge_squared()==m.gauge_squared(),'local_gauge_rotation')
            if not m.zero:
                c=x.Cell((x.Syllable(v,m),))
                need(c.rotate(g).carrier_readout()==mv(x.atlas.rotation_matrix(g),c.carrier_readout()),'carrier_equivariance')

rng=random.Random(60905)
def random_cell():
    c=ROOT
    for _ in range(rng.randrange(1,15)):
        c=c.push(rng.randrange(4),x.LocalMove(rng.randrange(-5,6),rng.randrange(-5,6)))
    return c
for _ in range(600):
    a,b,c=random_cell(),random_cell(),random_cell()
    g,hg=rng.choice(x.GROUP),rng.choice(x.GROUP)
    need(a.multiply(b).multiply(c)==a.multiply(b.multiply(c)),'associativity')
    need(a.rotate(g).rotate(hg)==a.rotate(x.brc.compose(hg,g)),'rotation_action')
    need(a.multiply(b).rotate(g)==a.rotate(g).multiply(b.rotate(g)),'rotation_multiplication')
    need(a.multiply(b).carrier_readout()==tuple(i+j for i,j in zip(a.carrier_readout(),b.carrier_readout())),'carrier_homomorphism')
    need(sum(a.carrier_readout())%2==0,'fcc_parity')
    f=a.flat_quotient_address()
    need(a.carrier_readout()==(-f[0]+f[1],-f[0]-f[2],f[1]-f[2]),'flat_address_inverse')

for aa in product(range(-4,5),repeat=2):
    for bb in product(range(-4,5),repeat=2):
        need(x.local_triangle_certificate(x.LocalMove(*aa),x.LocalMove(*bb)),'local_triangle_integer_certificate')

# Local elementary circles, diamonds, inverse events, incidence typing.
for v in range(4):
    ns=x.neighbours(v)
    tri=x.PacketPath(ROOT,tuple(x.Event(v,w) for w in ns))
    need(tri.endpoint==ROOT and tri.event_count==3 and tri.occupied_packet_count==3,'triangle_revisit_not_empty_history')
    for w in ns:
        ev=x.Event(v,w,weight=Fraction(2,3))
        back=x.PacketPath(ROOT,(ev,ev.reversed()))
        need(back.endpoint==ROOT and back.event_count==2 and back.occupied_packet_count==2,'backtrack_counts')
        need(back.summary().weight==Fraction(4,9),'inverse_does_not_erase_weight')
        need(ev.move.gauge_squared()==1 and ev.reversed().move.gauge_squared()==2,'directed_gauge_asymmetry')
    for a,b in permutations(ns,2):
        p=x.PacketPath(ROOT,(x.Event(v,a),x.Event(v,b)))
        q=x.PacketPath(ROOT,(x.Event(v,b),x.Event(v,a)))
        need(p != q and p.endpoint==q.endpoint,'commuting_diamond_full_witnesses')
        inc=x.elementary_vertex(ROOT,v,a,b)
        try: x.PacketPath(inc,())
        except TypeError: counts['incidence_not_packet']+=1
        else: raise AssertionError('incidence promoted to packet')

# 3-4-5 interface: 35 ordered words, one endpoint, count/mass 35, seven events.
letters=[x.Event(0,1)]*3+[x.Event(0,2)]*4
paths=[]
from itertools import combinations
for chosen in combinations(range(7),3):
    positions=set(chosen)
    paths.append(x.PacketPath(ROOT,tuple(x.Event(0,1 if i in positions else 2) for i in range(7))))
obs=x.endpoint_masses(paths)
need(len(paths)==35 and len(obs)==1 and next(iter(obs.values()))==(35,Fraction(35)),'brc_345_exact')
need(all(p.event_count==7 and p.endpoint.gauge_terms()==(25,) for p in paths),'345_length_not_event_count')

# Exact information-loss witnesses and the global inverse-gluing obstruction.
a,b=x.Event(0,1),x.Event(2,3)
p=x.PacketPath(ROOT,(a,b)); q=x.PacketPath(ROOT,(b,a))
need(p.summary()==q.summary() and p.endpoint!=q.endpoint,'six_count_summary_not_endpoint')
suffix=(a.reversed(),b.reversed())
need(x.PacketPath(ROOT,q.events+suffix).endpoint==ROOT and x.PacketPath(ROOT,p.events+suffix).endpoint!=ROOT,'future_return_separates_equal_counts')
for u,v in permutations(range(4),2):
    seam=x.PacketPath(ROOT,(x.Event(u,v),x.Event(v,u)))
    need(seam.endpoint!=ROOT and seam.endpoint.carrier_readout()==(0,0,0),'carrier_zero_not_native_return')
    need(x.step_move(u,v).gauge_squared()==1 and x.step_move(v,u,-1).gauge_squared()==2,'reciprocal_seam_gauge_obstruction')

# Targeted false-claim witnesses; these are not injected-code mutation tests.
negative_guards={
 'unreduced_histories_define_distinct_cells': x.PacketPath(ROOT,tuple(x.Event(0,w) for w in x.neighbours(0))).endpoint==ROOT,
 'six_counts_define_endpoint': p.endpoint!=q.endpoint,
 'carrier_defines_endpoint': x.PacketPath(ROOT,(x.Event(0,1),x.Event(1,0))).endpoint!=ROOT,
 'loop_is_empty_path': tri.event_count!=0,
 'symmetric_native_gauge': x.step_move(0,1).gauge_squared()!=x.step_move(0,1,-1).gauge_squared(),
 'boolean_is_multiplicity': next(iter(obs.values()))[0]!=1,
 'constant_gauge_after_reciprocal_glue': x.step_move(0,1).gauge_squared()!=x.step_move(1,0,-1).gauge_squared(),
}
need(all(negative_guards.values()),'targeted_false_claims_refuted')

result={'status':'PASS_EXACT_SELF_CHECK_NOT_NATIVE_PROMOTION_NOT_LEAN','counts':dict(counts),
        'short_history_digest':h.hexdigest(),'profiles':profile,'negative_guards':negative_guards,
        'source_module':'x6_development.py','seed':60905}
Path('verification_primary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
