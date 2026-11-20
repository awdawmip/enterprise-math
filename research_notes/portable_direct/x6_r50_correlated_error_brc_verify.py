#!/usr/bin/env python3
"""R50 exact conditional BRC path-count and correlated error certificates.

References R44 named whole-triad transition grammar, R47 root mass identities.
State updates use named Port branches; Fraction is only the exact coefficient ring.
"""
from fractions import Fraction as Q
from itertools import product
import json


def successor(state, event, port=None):
    a, b, occupancy, rotated = state
    if event == 'R':
        return (a, b, 0, rotated) if occupancy != 0 else None
    if event == 'T':
        if rotated or occupancy != 0 or ((a < 0) == (b < 0)):
            return None
        selected = a if a >= 0 else b
        owner = 1 if a >= 0 else 2
        return (a, b, owner if selected == 0 else 0, 1)
    if event == 'A':
        if a >= 0 or (port == 0 and occupancy != 0):
            return None
        return (port, b, 1 if port == 0 else occupancy, rotated)
    if event == 'B':
        if b >= 0 or (port == 0 and occupancy != 0):
            return None
        return (a, port, 2 if port == 0 else occupancy, rotated)
    raise ValueError(event)


def root_brc_mass(p, alpha, beta, word):
    # Actual labelled BRC carrier: enumerate each distinct named serial history,
    # retaining its identity until projecting to the declared F,R,T observer.
    frontier = [((-1, -1, 0, 0), Q(1), ())]
    for letter in word:
        later = []
        for state, weight, trace in frontier:
            if letter == 'F':
                for source, scalar in (('A', alpha), ('B', beta)):
                    for i in range(p):
                        dest = successor(state, source, i)
                        if dest is not None:
                            later.append((dest, weight * scalar, trace + (source + str(i),)))
            else:
                dest = successor(state, letter)
                if dest is not None:
                    later.append((dest, weight, trace + (letter,)))
        frontier = later
    names = [trace for _, _, trace in frontier]
    assert len(set(names)) == len(names)
    return sum((weight for _, weight, _ in frontier), Q(0)), len(names)


def masses(p, alpha, beta, bias=Q(0)):
    return tuple(root_brc_mass(p, alpha, beta, w)[0] + bias
                 for w in ('F', 'FT', 'FF', 'FRF'))


def C(q):
    return q*q - q - 1


def contrast(q, z):
    x, y, d, h = z
    return (d - h) - C(q) * ((x-y) - (x-h)/q)


def norm(q):
    c = C(q)
    # coefficient L1 norm in (x,y,d,h), exact correlated-error envelope.
    return 1 + c + abs(Q(c, q)-1) + c*(1-Q(1,q)) if q >= 2 else Q(2)


def paired_error_feasible(z, target, eta):
    # Common unknown bias has a simultaneous intersection iff oscillation <=2eta.
    residual = [v-t for v,t in zip(z,target)]
    return max(residual)-min(residual) <= 2*eta


def certified_eta(p, alpha, beta):
    S, P = alpha+beta, alpha*beta
    if p == 1:
        return P/Q(2)
    return min(S/Q(4*(p+1)), C(p)*P/Q(2))


def tests():
    weights = [(Q(1),Q(1)),(Q(1),Q(2)),(Q(2),Q(3)),(Q(1,2),Q(3,2))]
    biases = [Q(-4),Q(0),Q(7,3)]
    cases = variants = rivals = masses_checked = 0
    for p, (a,b), bias in product(range(1,9), weights, biases):
        raw = masses(p,a,b)
        S, P = a+b, a*b
        assert raw == (p*S,(p-1)*S,2*(p*p-1)*P,2*p*P)
        masses_checked += 4
        exact = tuple(t+bias for t in raw)
        eta = certified_eta(p,a,b)/3
        assert eta>0
        for signs in product((-1,1),repeat=4):
            z=tuple(v+sign*eta for v,sign in zip(exact,signs))
            assert paired_error_feasible(z,raw,eta)
            for q in range(1,41):
                if q == p:
                    continue
                if p == 1:
                    assert (z[2]-z[3]) < -2*eta
                elif q == 1:
                    assert (z[2]-z[3]) > 2*eta
                else:
                    # Any q fit must satisfy |L_q(z)|<=eta*norm(q).
                    assert abs(contrast(q,z)) > eta*norm(q), (p,q,a,b,bias,eta,z)
                rivals += 1
            variants += 1
        cases += 1
    # Concrete finite-candidate bound for p=3, alpha=1, beta=2, zero bias,
    # unperturbed central readout with per-channel eta=1/10.
    p,a,b,eta=3,Q(1),Q(2),Q(1,10)
    x,y,d,h=masses(p,a,b)
    s=x-y;k=x-h;e=d-h
    m=s-2*eta
    E=max(Q(0),e+2*eta)
    qcap=(k+2*eta+2*E)/m
    assert (x,y,d,h)==(9,6,32,12)
    assert qcap==Q(94,7) # 13 3/7
    return {
      'schema':'X6_R50_CORRELATED_ERROR_BRC_V1',
      'status':'PASS',
      'p_range':'1..8',
      'positive_weight_pairs':[[str(x),str(y)] for x,y in weights],
      'common_biases':[str(v) for v in biases],
      'source_parameter_cases':cases,
      'full_named_path_root_coefficients_checked':masses_checked,
      'bounded_noise_vertex_observations':variants,
      'rival_port_contrast_exclusions':rivals,
      'candidate_q_test_range':'1..40; universal q exclusion follows symbolic proof',
      'arithmetic':'R44 named-branch positive BRC carrier; exact Fraction coefficient ring',
      'correlated_error_contrast_norm':'q=1:2; q=2:3; q>=3:2(q^2-q-1)',
      'example':{'p':3,'alpha':1,'beta':2,'root':list(map(str,(x,y,d,h))),
                 'eta':str(eta),'upper_bound_on_any_q_ge_2':str(qcap),
                 'integer_q_ge_2_must_be_at_most':int(qcap)},
      'verification':'exact finite rooted BRC path enumeration and all 16 box vertices; independent universal symbolic proof in R50 paper',
      'review':'AUTHOR_CHECK_NOT_INDEPENDENTLY_REVIEWED',
      'native_P000_link':'NOT_ESTABLISHED; conditional R44 graph'
    }


if __name__ == '__main__':
    print(json.dumps(tests(),indent=2,ensure_ascii=False,sort_keys=True))
