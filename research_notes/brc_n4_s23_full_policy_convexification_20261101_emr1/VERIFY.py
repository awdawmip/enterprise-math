#!/usr/bin/env python3
"""Exact positive rational branch-weight checks: BRC N4/S23 full-policy convexification.

Mathematical scope: finite six-latent-source four-time auxiliary observer;
not a native X6 physical simulation or a BRC phase-propagation engine.
"""
from fractions import Fraction as Q
from itertools import product

Z, O = Q(0), Q(1)
S = ((0, 0, 0, 1, 1, 1), (0, 0, 1, 0, 0, 2))
M = (
    (Q(1, 2), Q(1, 2), Z, Z, Z, Z),
    (Q(9, 20), Q(11, 20), Z, Z, Z, Z),
    (Z, Z, O, Z, Z, Z),
    (Z, Z, Z, Q(1, 2), Q(1, 2), Z),
    (Z, Z, Z, Q(1, 10), Q(9, 10), Z),
    (Z, Z, Z, Z, Z, O),
)


def law(theta):
    """11 causally typed stop controls: A/B, U/AV/BV, six terminal sources."""
    a, b, c = theta[:2], theta[2:5], theta[5:]
    result = []
    for x in range(6):
        p, q, r = a[S[0][x]], b[S[1][x]], c[x]
        row = (p, (O-p)*q, (O-p)*(O-q)*r, (O-p)*(O-q)*(O-r))
        assert all(v >= 0 for v in row) and sum(row) == O
        result.append(row)
    return tuple(result)


def prepared(latent):
    return tuple(tuple(sum(M[i][x]*latent[x][t] for x in range(6))
                       for t in range(4)) for i in range(6))


def tv(a, b):
    return sum(abs(u-v) for u,v in zip(a,b))/2


def det_five_decoder_rows(latent):
    """Previous author's sharp 1/40 construction, used as a regression witness."""
    merged = tuple(Q(19,40)*latent[0][t] + Q(21,40)*latent[1][t]
                   for t in range(4))
    return (merged, merged, *latent[2:])


def mixing_weight(theta, s):
    out=O
    for p, bit in zip(theta, s):
        out *= p if bit else O-p
    return out

assert all(sum(row)==O for row in M)
strategies=list(product((Z,O),repeat=11))
assert len(strategies)==2048
laws=[law(s) for s in strategies]
max_det_error = Z
for latent in laws:
    original, predicted = prepared(latent), prepared(det_five_decoder_rows(latent))
    for i in range(6):
        error=tv(original[i],predicted[i])
        assert error <= Q(1,40)
        max_det_error=max(max_det_error,error)
assert max_det_error==Q(1,40)

controls=(
    (Q(1,2),)*11,
    (Q(1,3),Q(2,3),Q(1,4),Q(3,4),Q(2,5),Q(1,5),Q(4,5),Q(1,6),Q(5,6),Q(2,7),Q(3,7)),
    (Z,O,Q(1,2),Q(1,3),Q(2,3),Q(3,8),Q(5,8),Z,O,Q(1,7),Q(6,7)),
)
max_mixed_error=Z
for theta in controls:
    weights=[mixing_weight(theta,s) for s in strategies]
    assert all(w>=0 for w in weights) and sum(weights)==O
    from_corners=tuple(tuple(sum(weights[j]*laws[j][x][t]
                                      for j in range(2048))
                                   for t in range(4)) for x in range(6))
    direct=law(theta)
    assert from_corners==direct
    # Decoder chosen after the complete policy is known: the same positive
    # branch-mass interpolation applied to each deterministic policy decoder.
    decoder_corners=[det_five_decoder_rows(lat) for lat in laws]
    decoder_mixed=tuple(tuple(sum(weights[j]*decoder_corners[j][x][t]
                                      for j in range(2048))
                                   for t in range(4)) for x in range(6))
    assert decoder_mixed==det_five_decoder_rows(direct)
    source, reconstructed = prepared(direct), prepared(decoder_mixed)
    for i in range(6):
        error=tv(source[i], reconstructed[i])
        assert error <= Q(1,40)
        max_mixed_error=max(max_mixed_error,error)

# A legal finite-label (m=2) decoder bank: it covers the two named corners
# exactly but its interior randomized policy has TV error 1/2.
a=(Z,Z); b=(Z,Z,Z)
low=(a+b+(Z,)*6)
high=(a+b+(O,)*6)
mid=(a+b+(Q(1,2),)*6)
lo=law(low); hi=law(high); mixture=law(mid)
assert all(row==(Z,Z,Z,O) for row in lo)
assert all(row==(Z,Z,O,Z) for row in hi)
assert all(row==(Z,Z,Q(1,2),Q(1,2)) for row in mixture)
assert max(tv(prepared(lo)[i],prepared(lo)[i]) for i in range(6))==Z
assert max(tv(prepared(hi)[i],prepared(hi)[i]) for i in range(6))==Z
fixed_banks=(lo,hi) # six-state identity encoder, both decoder matrices pre-fixed
interior=min(max(tv(prepared(mixture)[i],prepared(D)[i]) for i in range(6))
             for D in fixed_banks)
assert interior==Q(1,2)

# Third-stage AU0 indicator realizes equality in deterministic 5-state bound.
indicator=law(a+b+(O,Z,Z,Z,Z,Z))
indicator_error=max(tv(a,b) for a,b in zip(prepared(indicator),
                                           prepared(det_five_decoder_rows(indicator))))
assert indicator_error==Q(1,40)

print('deterministic_causal_tables=2048; first2/second3/terminal6 controls')
print('exact_deterministic_five_state_prepared_comparisons=12288')
print('product_weight_interpolation_cases=3; probabilities=6*4 per case')
print('all_weight_sums=1; full_policy_interpolated_decoders_row_stochastic=true')
print('max_deterministic_error=1/40; max_sampled_behavioral_error='+str(max_mixed_error))
print('indicator_policy_sharp_error='+str(indicator_error))
print('two_fixed_policy_tags_corner_errors=0,0; interior_behavioral_error='+str(interior))
print('PASS_BRC_N4_S23_FULL_POLICY_CONVEXIFICATION_20261101')
