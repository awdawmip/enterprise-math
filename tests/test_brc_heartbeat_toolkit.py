from fractions import Fraction as Q
import itertools
from enterprise_math.brc_transport import Affine, eye
from enterprise_math.brc_histogram import WeightHistogram
from enterprise_math.brc_residue_port import ResidueLayout, ResiduePacket, block_swap, fiber_moments
from enterprise_math.brc_residue_quotient import certify_port_quotient, refine_port_partition, QuotientMomentPacket
from enterprise_math.brc_contact_horizon import ContactState, DIRECTIONS, ZERO, contact_class_count, contact_push


def x(n): return (n,0,0,0,0,0)


def cycle(layout, start=0):
    f=block_swap(layout,0,1,0,start)
    g=block_swap(layout,0,2,1,start+1)
    return f.then(g).then(f.at(start+3)).then(g.at(start+4))


def test_macro_residue_quotient_and_micro_rejection():
    layout=ResidueLayout((4,1,1,1,1,1)); c=cycle(layout)
    groups=refine_port_partition((c,),mode='effects')
    assert groups==((x(0),x(3)),(x(1),x(2)))
    assert certify_port_quotient(c,groups,mode='effects').equality_checks==2
    f=block_swap(layout,0,1,0)
    try: certify_port_quotient(f,groups,mode='effects')
    except ValueError: pass
    else: raise AssertionError('macro quotient must not be reused inside the cycle')


def test_six_axis_macro_reduces_4096_to_64():
    layout=ResidueLayout((4,)*6); edges=[]
    for r in layout.ports():
        delta=tuple(4 if a in (0,3) else -4 for a in r)
        edges.append((r,r,1,Affine(eye(6),delta),1))
    packet=ResiduePacket.from_edges(layout,0,36,edges)
    groups=refine_port_partition((packet,),mode='effects')
    assert len(groups)==64 and {len(g) for g in groups}=={64}


def test_quotient_moment_execution():
    layout=ResidueLayout((4,1,1,1,1,1)); c=cycle(layout)
    groups=refine_port_partition((c,)); q=QuotientMomentPacket.compile(c,groups)
    measure={x(-3):Q(1,3),x(0):Q(1,6),x(5):Q(1,2)}
    full=fiber_moments(layout,measure); small=q.aggregate(full)
    assert q.apply(small,start=0)==q.aggregate(c.moment_action(full))


def test_contact_horizon_counts_and_weighted_return():
    assert [contact_class_count(h) for h in range(7)]==[2,14,86,378,1290,3654,8990]
    dist={ContactState.encode(ZERO,4):WeightHistogram.from_counts({Q(1):1})}
    moves=[(d,Q(1,12),1) for d in DIRECTIONS]
    for _ in range(4): dist=contact_push(dist,moves)
    mass=sum((h.total_mass for s,h in dist.items() if s.contact),Q(0))
    assert mass==Q(11,576)
    assert sum((h.total_mass for h in dist.values()),Q(0))==1


def test_contact_current_bit_is_not_future_safe():
    a=ContactState.encode(x(1),2); b=ContactState.encode(x(2),2)
    assert not a.contact and not b.contact
    assert a.advance(x(-1)).contact and not b.advance(x(-1)).contact
