from collections import defaultdict
from dataclasses import replace
from itertools import combinations, product
from math import gcd
from types import MappingProxyType
import random
import pytest

from enterprise_math.group_ring_sparse_identifiability import (
    sparse_ruler, difference_set, structural_alias, period_closures,
    collision_spectrum, collision_readouts, compile_sparse_codebook,
    verify_codebook, labeled_collision_gcd, ruler_order,
)
from enterprise_math.group_ring_affine_character import affine_collision_from_order


def brute_mass(support, weights, period):
    buckets = defaultdict(int)
    for x, w in zip(support, weights):
        buckets[x % period] += w
    return sum(w*w for w in buckets.values())


def brute_order(n, a):
    x = a % n
    for r in range(1, n+1):
        if x == 1:
            return r
        x = x*a % n
    raise AssertionError('unit order not found')


@pytest.mark.parametrize('H', [1,2,3,6,9,10,16,17,100,257])
def test_ruler_covers_all_differences(H):
    s = sparse_ruler(H)
    assert s[0] == 0 and s[-1] == H
    assert difference_set(s,H) == frozenset(range(1,H+1))
    assert period_closures(s,H) == tuple(range(1,H+1))+(0,)
    assert structural_alias(s,H) is None


def test_detection_is_not_identification():
    s = (0,4,5,6)
    closures = period_closures(s,6)
    assert all(closures[:-1])
    assert closures[2] == closures[5] == 6
    for w in product(range(1,4), repeat=4):
        assert brute_mass(s,w,3) == brute_mass(s,w,6)
    assert structural_alias(s,6) == (3,6)
    assert compile_sparse_codebook(6,s).status == 'UNIDENTIFIABLE_SUPPORT'


def test_missing_lag_can_still_identify():
    s = (0,1,5,7,9)
    assert difference_set(s,9) == frozenset(range(1,10))-{3}
    assert period_closures(s,9) == tuple(range(1,10))+(0,)
    assert compile_sparse_codebook(9,s).status == 'COMPLETE'


def test_monotone_on_sparse_marks_not_enough():
    s=(0,1,2,3,6);w=(1,2,3,4,7)
    spec=collision_spectrum(s,w,6)
    assert spec[1] == spec[2] == 157
    assert structural_alias(s,6) is None
    book=compile_sparse_codebook(6,s).codebook
    assert book.codes[1] != book.codes[2]


def test_closure_equals_complete_signature_exhaustive():
    for H in range(1,9):
        for mask in range(1,1 << (H+1)):
            s=tuple(x for x in range(H+1) if mask >> x & 1)
            D=difference_set(s,H);c=period_closures(s,H)
            sig=[tuple(d for d in D if d % r == 0) for r in range(1,H+2)]
            for i in range(H+1):
                if c[i]:
                    assert c[i] % (i+1) == 0
                    assert c[c[i]-1] == c[i]
                for j in range(H+1):
                    assert (c[i] == c[j]) == (sig[i] == sig[j])
                    if (j+1) % (i+1) == 0 and c[i]:
                        assert c[j] % c[i] == 0


def test_spectrum_matches_occupancy_and_affine_specialization():
    rng=random.Random(813)
    for H in range(1,30):
        s=tuple(x for x in range(H+1) if rng.randrange(3)) or (0,)
        w=tuple(rng.randrange(1,30) for x in s)
        assert collision_spectrum(s,w,H) == tuple(brute_mass(s,w,r) for r in range(1,H+2))
        dense=tuple(range(H+1));weights=tuple(3+2*x for x in dense)
        assert collision_spectrum(dense,weights,H) == tuple(
            affine_collision_from_order(H+1,r,3,2) for r in range(1,H+2))


@pytest.mark.parametrize('alphabet',['large','binary'])
def test_codebook_all_periods_and_actual_modular_orders(alphabet):
    for H in (1,3,6,9,16,31):
        book=compile_sparse_codebook(H,alphabet=alphabet).codebook
        assert verify_codebook(book)
        for r,code in enumerate(book.codes,1):
            inf=book.decode(code)
            assert inf.order == (r if r<=H else None)
            assert inf.lower_bound == r
        for n in range(2,31):
            for a in range(1,n):
                if gcd(a,n)!=1:continue
                r=brute_order(n,a)
                inferred=book.decode(book.observe(n,a))
                assert inferred.order == (r if r<=H else None)
                if r>H:assert inferred.lower_bound == H+1


def test_gcd_observer_not_always_exact_without_support_certificate():
    s=(0,4,5,6)
    assert labeled_collision_gcd(7,2,s,6).gcd_multiple == 6  # true order 3
    assert labeled_collision_gcd(7,3,s,6).gcd_multiple == 6  # true order 6
    assert labeled_collision_gcd(7,2,(0,1),1).gcd_multiple == 0


def test_ruler_order_all_small_units():
    for n in range(2,90):
        for a in range(1,n):
            if gcd(a,n)!=1:continue
            r=brute_order(n,a)
            for H in (1,2,3,7,16,32,64):
                value=ruler_order(n,a,H)
                assert value.order == (r if r<=H else None)


def test_binary_separation_probability_for_each_distinct_pair():
    s=(0,1,5,7,9);H=9
    all_spectra=[collision_spectrum(s,w,H) for w in product((1,2),repeat=len(s))]
    for i,j in combinations(range(H+1),2):
        nonzero=sum(row[i]!=row[j] for row in all_spectra)
        assert nonzero*4 >= len(all_spectra)


def test_codebook_rejects_forged_tables_and_bad_readouts():
    book=compile_sparse_codebook(9).codebook
    bad=dict(book._lookup);bad[book.codes[0]]=3
    with pytest.raises(ValueError):verify_codebook(replace(book,_lookup=MappingProxyType(bad)))
    with pytest.raises(ValueError):verify_codebook(replace(book,codes=book.codes[:-1]))
    with pytest.raises(TypeError):verify_codebook(None)
    with pytest.raises(TypeError):book._lookup[book.codes[0]]=3
    for values in ((),(True,),(-1,),(0,),(1,2)):
        with pytest.raises(ValueError):book.decode(values)


def test_explicit_resource_outcomes():
    assert compile_sparse_codebook(100,max_horizon=10).status=='BUDGET_EXHAUSTED'
    assert compile_sparse_codebook(100,max_work=1).status=='BUDGET_EXHAUSTED'
    assert compile_sparse_codebook(9,max_trials=0).status=='SEARCH_EXHAUSTED'
    c=compile_sparse_codebook(9,max_work=50)
    assert c.status=='BUDGET_EXHAUSTED' and c.codebook is None


@pytest.mark.parametrize('s', [(),(1,0),(0,0),(0,True),(-1,2),(0,7)])
def test_invalid_support(s):
    with pytest.raises(ValueError):collision_spectrum(s,(1,)*len(s),6)


@pytest.mark.parametrize('weights', [(1,),(1,0),(1,-1),(1,True),(1,1.0)])
def test_invalid_weights(weights):
    with pytest.raises(ValueError):collision_spectrum((0,1),weights,1)


@pytest.mark.parametrize('n,a',[(1,1),(4,2),(7,0),(7,7),(7,True)])
def test_nonunit_or_noncanonical_base(n,a):
    with pytest.raises(ValueError):collision_readouts(n,a,(0,1),((1,1),),1)
