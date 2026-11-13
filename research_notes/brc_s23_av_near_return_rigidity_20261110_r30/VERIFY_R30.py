#!/usr/bin/env python3
"""R30: exact near-return source-suffix rigidity, optional R27 audit."""
import argparse
import csv
import json
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path

DEN = 10**24
L = Fraction(262204504569236716045286, DEN)
U = Fraction(262204504569236716045287, DEN)
MID = (L + U) / 2
M, H = 128, 164
J = (25339, 168319, 10899111)


def frac(x):
    return x - (x.numerator // x.denominator)


def dist(x):
    f = frac(x)
    return min(f, 1-f)


def nearest(x):
    return (x + Fraction(1, 2)).numerator // (x + Fraction(1, 2)).denominator


def arcs(theta):
    return sorted((frac(s * theta), s) for s in range(M))


def owner(theta, source, ordered=None):
    ordered = arcs(theta) if ordered is None else ordered
    rank = bisect_right(ordered, (frac(source * theta), M)) - 1
    return rank % M


def template(theta):
    ordered = arcs(theta)
    buckets = {i: [] for i in range(M)}
    for r in range(1, H + 1):
        buckets[owner(theta, -r, ordered)].append(r)
    return ordered, buckets


def coefficients_abs(q, p, sign):
    return (-sign*p, sign*q)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--regimes', type=Path)
    parser.add_argument('--events', type=Path)
    parser.add_argument('--certificate', type=Path)
    args = parser.parse_args()
    assert (args.events is None) == (args.regimes is None)

    # No d <= m+H-1 changes integer part on the open enclosure.
    for d in range(1, M + H):
        assert (d*L).numerator//(d*L).denominator == (d*U).numerator//(d*U).denominator
    candidates = [(dist(d*x),d) for x in (L,U) for d in range(1,M+H)]
    mu, arg_d = min(candidates)
    assert arg_d == 164 and mu > 0

    t_l, b_l = template(L)
    t_u, b_u = template(U)
    t_m, b_m = template(MID)
    assert [s for _,s in t_l] == [s for _,s in t_u] == [s for _,s in t_m]
    assert b_l == b_u == b_m
    assert all(b_m.values())
    assert sum(bool([r for r in v if r<=163]) for v in b_m.values()) == M-1
    missing = [i for i,v in b_m.items() if not any(r<=163 for r in v)]
    assert missing == [M-1] and t_m[-1][1] == 61
    last_offsets = sorted(-min(rs) for rs in b_m.values())
    expected_offsets = list(range(-164,-97))+list(range(-61,0))
    assert last_offsets == expected_offsets

    sample = []
    for j in J:
        k = nearest(j*MID)
        deviation = max(abs(j*L-k),abs(j*U-k))
        assert deviation < mu
        for x in (L,MID,U):
            order = arcs(x)
            for r in range(1,H+1):
                assert owner(x,j-r,order) == owner(x,-r,order)
        sample.append({'j': j, 'nearest_integer':k,'max_deviation':str(deviation),
                       'ratio_to_mu':str(deviation / mu)})

    checked_rows = checked_events = 0
    skipped_switch_regime = 0
    if args.regimes:
        with args.regimes.open() as f:
            regimes = list(csv.DictReader(f,delimiter='\t'))
        with args.events.open() as f:
            event_map = {int(r['n']):(int(r['delta_A']),int(r['delta_B']))
                         for r in csv.DictReader(f,delimiter='\t')}
        for row in regimes:
            q,j = int(row['i']),int(row['j'])
            if not (q>H and q<j):
                continue
            kq, kj = nearest(q*MID), nearest(j*MID)
            deviation = max(abs(j*L-kj),abs(j*U-kj))
            assert deviation < mu
            assert abs(q*kj-j*kq)==1
            e_sign = 1 if q*MID>kq else -1
            v_sign = 1 if j*MID>kj else -1
            assert e_sign == -v_sign
            # If there are no events before the horizon, no amplitude comparison is needed.
            n0,n1 = int(row['n0']),int(row['n1'])
            positions = [q+j-r+1 for r in list(range(98,165))+list(range(1,62))
                         if n0<=q+j-r+1<=n1]
            assert len(positions)==int(row['events'])
            if not positions:
                skipped_switch_regime+=1
                continue
            e_l,e_u = e_sign*(q*L-kq),e_sign*(q*U-kq)
            v_l,v_u = v_sign*(j*L-kj),v_sign*(j*U-kj)
            if e_l < v_l and e_u < v_u:
                amp = coefficients_abs(q,kq,e_sign)
            elif v_l < e_l and v_u < e_u:
                amp = coefficients_abs(j,kj,v_sign)
            else:
                raise AssertionError(f'uncertified amplitude choice q={q},j={j}')
            actual = {n:a for n,a in event_map.items() if n0<=n<=n1}
            assert set(actual)==set(positions), (q,j,len(actual),len(positions))
            for n in positions:
                assert actual[n]==amp,(q,j,n,actual[n],amp)
            checked_rows+=1
            checked_events+=len(positions)
        assert checked_rows==47 and checked_events==6016

    cert={'claim':'near-return suffix rigidity for m=128,H=164, all theta in (L,U)',
          'L':str(L),'U':str(U),'mu_lower':str(mu),'mu_attaining_d':arg_d,
          'template_last_offset_set':{'block1':[-164,-98],'block2':[-61,-1]},
          'missing_at_H163':{'arc_rank':127,'historical_cut_source':61},
          'sample_j':sample,'r27_positive_regimes_crosschecked':checked_rows,
          'r27_positive_events_crosschecked':checked_events,
          'r27_zero_event_regimes_without_amplitude_claim':skipped_switch_regime}
    if args.certificate:
        args.certificate.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
    print('PASS_R30_NEAR_RETURN_RIGIDITY')
    print('mu_lower=',mu,'attained_d=',arg_d)
    print('last_offsets=',len(last_offsets),'two_blocks=[-164,-98],[-61,-1]')
    print('samples=',len(J),'historical_arcs=',M,'minimum_suffix=',H)
    print('r27_regimes_crosschecked=',checked_rows,'r27_events_crosschecked=',checked_events)


if __name__=='__main__':
    main()
