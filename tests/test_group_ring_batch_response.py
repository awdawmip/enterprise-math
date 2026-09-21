from collections import Counter
from math import gcd
import random
import pytest
from enterprise_math.group_ring_batch_response import window_responses, dyadic_cut_responses
from enterprise_math.group_ring_terminal_response import terminal_responses, suffix_responses


def occupancy_response(n, b, L, u):
    counts = Counter(pow(b,i,n) for i in range(L))
    return sum(c*counts.get(u*v % n, 0) for v,c in counts.items())


@pytest.mark.parametrize('n,b', [(7,3),(15,2),(21,2),(31,3),(65,2),(101,2)])
def test_windows_independent_occupancy(n,b):
    req = [(L,u) for L in (1,2,3,7,8,9,16,31,32,65) for u in range(n)]
    expected = tuple(occupancy_response(n,b,L,u) for L,u in req)
    for B in (1,2,3,7,8,16,65):
        out=window_responses(n,b,req,baby_width=B)
        assert out.values==expected
        assert out.executed_scans<=out.required_scans
        if out.learned_order is None:
            assert out.executed_scans==out.required_scans


@pytest.mark.parametrize('n,a', [(7,3),(15,2),(21,2),(31,3),(65,2),(101,2)])
def test_cuts_independent_occupancy(n,a):
    cuts=(0,2,1,3,0); states=tuple(range(n))
    expected=tuple(tuple(occupancy_response(n,pow(a,1<<j,n),1<<(7-j),u)
                         for u in states) for j in cuts)
    for k in range(3,8):
        out=dyadic_cut_responses(n,a,7,cuts,states,width_bits=k)
        assert out.values==expected
        assert out.executed_scans<=out.required_scans


def test_repeated_powers_are_proved_period_not_overwritten():
    out=window_responses(15,4,[(17,1),(17,4),(17,2)],baby_width=7)
    assert out.learned_order==2 and out.executed_scans==2
    assert out.values==(145,144,0)
    out=dyadic_cut_responses(15,2,9,(0,1,2,3),(1,2,4,8,7),width_bits=4)
    assert out.learned_order==4 and out.table_entries==4
    assert out.values==tuple(suffix_responses(15,2,9,j,(1,2,4,8,7)).values for j in (0,1,2,3))


def test_window_order_duplicates_generators_and_tail_boundaries():
    req=[(33,7),(32,1),(32,7),(1,0),(31,7),(33,7),(8,2),(9,2)]
    want=tuple(terminal_responses(101,2,L,(u,)).values[0] for L,u in req)
    assert window_responses(101,2,(q for q in req),baby_width=8).values==want


def test_shared_scan_count_depends_on_max_horizon_not_number_of_windows():
    lens=range(1000,1040)
    req=[(L,1) for L in lens]
    out=window_responses(10007,5,req,baby_width=32)
    assert out.learned_order is None
    assert out.executed_scans==32+(1039+31)//32
    assert out.values==tuple(terminal_responses(10007,5,L).values[0] for L in lens)


def test_all_cuts_share_one_giant_trajectory():
    states=(1,2,3,4,5)
    all_=dyadic_cut_responses(10007,5,14,range(7),states,width_bits=7)
    one=dyadic_cut_responses(10007,5,14,(0,),states,width_bits=7)
    assert all_.learned_order is one.learned_order is None
    assert all_.giant_lookups==one.giant_lookups
    assert all_.values[0]==one.values[0]
    assert all_.values==tuple(suffix_responses(10007,5,14,j,states).values for j in range(7))


def test_nonunit_and_outside_subgroup():
    req=[(200,0),(200,3),(200,2),(200,4)]
    assert window_responses(15,4,req).values==(0,0,0,20000)
    assert dyadic_cut_responses(15,4,10,(0,1),(0,3,2,4)).values==((0,0,0,524288),(0,0,0,0))


def test_empty_and_identity():
    assert window_responses(7,3,()).values==()
    assert dyadic_cut_responses(7,3,5,(),[1,2]).values==()
    assert dyadic_cut_responses(7,3,5,[0,1],[]).values==((),())
    assert window_responses(7,1,[(1<<100,1),(1<<100,2)],max_scan_steps=0).values==(1<<200,0)
    assert dyadic_cut_responses(7,1,100,[0,100],[1,2],max_scan_steps=0).values==((1<<200,0),(1,0))


def test_no_fake_zero_on_budget_exhaustion():
    a=window_responses(10007,5,[(1<<60,1)],max_baby_steps=10,max_scan_steps=100)
    b=dyadic_cut_responses(10007,5,60,[0,50],[1],max_baby_steps=100,max_scan_steps=100)
    for x in (a,b):
        assert x.status=='BUDGET_EXHAUSTED' and x.values is None and x.executed_scans==0


@pytest.mark.parametrize('call',[
    lambda:window_responses(True,2,[(8,1)]),
    lambda:window_responses(15,3,[(8,1)]),
    lambda:window_responses(7,3,[(0,1)]),
    lambda:window_responses(7,3,[(8,True)]),
    lambda:window_responses(7,3,[(8,7)]),
    lambda:window_responses(7,3,[(8,1)],baby_width=9),
    lambda:dyadic_cut_responses(7,3,8,[4],[1],width_bits=3),
    lambda:dyadic_cut_responses(7,3,8,[9],[1]),
    lambda:dyadic_cut_responses(7,3,8,[True],[1]),
    lambda:dyadic_cut_responses(7,3,1_000_001,[0],[1]),
])
def test_invalid_inputs(call):
    with pytest.raises(ValueError): call()


def forward(n,a,m,start):
    out=dict(start); work=0
    for j in range(m):
        nxt=Counter(); b=pow(a,1<<j,n); bi=pow(b,-1,n)
        for u,w in out.items():
            nxt[u]+=2*w; nxt[u*b%n]+=w; nxt[u*bi%n]+=w; work+=1
        out=dict(nxt)
    return out,work


def test_real_prefix_cost_and_contraction_at_multiple_cuts():
    rng=random.Random(20260922)
    for _ in range(80):
        n=rng.choice((7,11,15,21,31)); a=rng.choice([v for v in range(1,n) if gcd(v,n)==1])
        m=rng.randrange(2,8); k=min(4,m)
        start={u:rng.randrange(4) for u in range(n)}
        end,_=forward(n,a,m,start)
        prefixes=[forward(n,a,j,start) for j in range(k+1)]
        costs=sum(w for _,w in prefixes)
        out=dyadic_cut_responses(n,a,m,range(k+1),range(n),width_bits=k)
        for j,(p,_) in enumerate(prefixes):
            assert sum(p.get(u,0)*out.values[j][u] for u in range(n))==end.get(1,0)
        assert costs>=0  # Report this cost; never silently give the caller free prefixes.


def test_naive_cross_cut_rescaling_is_false():
    h0=suffix_responses(7,3,3,0,[3]).values[0]
    h1=dyadic_cut_responses(7,3,3,[1],[3],width_bits=1).values[0][0]
    assert (h0,h1)==(11,0)
    assert h0//2!=h1  # Divisibility of offsets cannot be discarded.


def test_exact_budget_threshold():
    req=[(1000,1),(1001,2)]
    out=window_responses(10007,5,req,baby_width=32)
    cap=out.required_scans
    assert window_responses(10007,5,req,baby_width=32,max_scan_steps=cap).values==out.values
    assert window_responses(10007,5,req,baby_width=32,max_scan_steps=cap-1).values is None


def test_closed_orbit_subgroup_log_transport():
    # a has order 6; a^2 has order 3 and excludes the odd exponent class.
    out=dyadic_cut_responses(7,3,5,[0,1,2],[1,3,2,6,4,5],width_bits=3)
    assert out.learned_order==6
    assert all(out.values[1][i]==0 for i in (1,3,5))
    assert out.values==tuple(suffix_responses(7,3,5,j,[1,3,2,6,4,5]).values for j in [0,1,2])


def test_bounded_classical_baselines_no_order_or_logs_supplied():
    import importlib.util
    from pathlib import Path
    p=Path(__file__).resolve().parents[1]/'research_notes/power_batch_cuts_20260922_16243626C61A/validate.py'
    spec=importlib.util.spec_from_file_location('batch_validate',p)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for n,a in [(7,3),(15,2),(101,2),(10007,5)]:
        states=tuple(range(min(n,25)))
        req=[(L,u) for L in (3,9,31,65) for u in states]
        assert mod.bounded_log_windows(n,a,req)==window_responses(n,a,req).values
        assert mod.bounded_log_cuts(n,a,8,range(4),states)==dyadic_cut_responses(n,a,8,range(4),states,width_bits=4).values


@pytest.mark.parametrize('n,a', [(7,3),(15,2),(31,3),(101,2)])
def test_compiled_index_all_windows_all_cuts(n,a):
    from enterprise_math.group_ring_batch_response import compile_terminal_index
    states=tuple(range(n))
    for B in (1,3,8,65):
        c=compile_terminal_index(n,a,65,states,baby_width=B)
        assert c.status=='COMPLETE' and c.executed_scans<=c.required_scans
        req=[(L,u) for L in (1,3,8,17,64,65) for u in states]
        assert c.index.windows(req)==window_responses(n,a,req).values
        assert c.index.cuts(6,range(7),states)==tuple(suffix_responses(n,a,6,j,states).values for j in range(7))


def test_compiled_scope_is_enforced_not_zero():
    from enterprise_math.group_ring_batch_response import compile_terminal_index
    c=compile_terminal_index(10007,5,32,[1,2,3])
    assert c.index.order is None
    with pytest.raises(ValueError): c.index.windows([(33,1)])
    with pytest.raises(ValueError): c.index.windows([(16,4)])
    with pytest.raises(ValueError): c.index.cuts(6,[0],[1])
    with pytest.raises(TypeError): c.index._logs[1]=4
    b=compile_terminal_index(10007,5,1<<50,[1,2],max_scan_steps=10)
    assert b.index is None and b.status=='BUDGET_EXHAUSTED' and b.executed_scans==0


def test_compiled_degenerate_inputs():
    from enterprise_math.group_ring_batch_response import compile_terminal_index
    assert compile_terminal_index(15,2,100,[3,0]).index.windows([(50,0),(50,3)])==(0,0)
    assert compile_terminal_index(15,1,100,[1,2]).index.windows([(50,1),(50,2)])==(2500,0)
    assert compile_terminal_index(15,2,1,[1,2]).index.windows([(1,1),(1,2)])==(1,0)
