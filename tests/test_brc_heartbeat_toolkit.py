from fractions import Fraction as Q
from enterprise_math.brc_residue_port import ResidueLayout, block_swap, fiber_moments
from enterprise_math.brc_residue_quotient import refine_port_partition, certify_port_quotient, QuotientMomentPacket
from enterprise_math.brc_contact_horizon import ContactState, contact_class_count, DIRECTIONS, ZERO, contact_push
from enterprise_math.brc_histogram import WeightHistogram

def x(n): return (n,0,0,0,0,0)

def test_heartbeat_brc_toolkit_smoke():
    layout=ResidueLayout((4,1,1,1,1,1))
    f=block_swap(layout,0,1,0)
    g=block_swap(layout,0,2,1,1)
    cycle=f.then(g).then(f.at(3)).then(g.at(4))
    groups=refine_port_partition((cycle,))
    assert groups==((x(0),x(3)),(x(1),x(2)))
    assert certify_port_quotient(cycle,groups,mode='moment2').equality_checks==2
    try:
        certify_port_quotient(f,groups,mode='moment2')
    except ValueError:
        pass
    else:
        raise AssertionError('unsafe micro quotient accepted')
    q=QuotientMomentPacket.compile(cycle,groups)
    state=q.aggregate(fiber_moments(layout,{x(0):Q(1,2),x(1):Q(1,2)}))
    assert len(q.apply(state,start=0))==2
    assert [contact_class_count(h) for h in range(4)]==[2,14,86,378]
    d={ContactState.encode(ZERO,2):WeightHistogram.from_counts({1:1})}
    moves=[(v,Q(1,12),1) for v in DIRECTIONS]
    d=contact_push(contact_push(d,moves),moves)
    assert sum((w.total_mass for s,w in d.items() if s.contact),Q(0))==Q(1,12)
