#!/usr/bin/env python3
"""Exact R5 cost-inert / optimizer-active gap check, using PR #2379 companion modules.

Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551
Place the two imported source modules on PYTHONPATH. Exact integer arithmetic.
"""
from itertools import combinations
from random import Random
import json
from VERIFY_R5_COST_SPECTRA import frozen, closed_points
from VERIFY_R5_OPTIMAL_WITNESSES import optimum_counts_spectrum

INERT = (0,1,7,14,15,17,18,19,20,21,22,23,24)
ACTIVE = (15,17)
ALL = (1 << 28) - 1
EXPECTED_HEX = {
    15: "9249249249249249249249249249249249249249249249249249249249249249249249249249249249249249249249249248892122490842248912491222112924891111124924491111111222249249249244492488912108922491124448922491224889124924892490891222444489244892224924",
    17: "9249249249249249249249249249249249249249249249249249249249249249249249249249249249249249249249249248892122490842248912491222112924891111124924491111111222249249249244492488912244922491124421122491224889124924892490891222444489244892224924",
}

def validate_mask(old, new, center_hex, budget=293, expected_cost=741):
    bits = int(center_hex, 16)
    indices = [i for i in range(len(old)) if (bits >> i) & 1]
    assert len(indices) == budget and bits >> len(old) == 0
    new_dist = [min(abs(new[t] - new[j]) for j in indices)
                for t in range(len(old))]
    old_dist = [min(abs(old[t] - old[j]) for j in indices)
                for t in range(len(old))]
    assert max(new_dist) == 2 and sum(new_dist) == expected_cost
    assert max(old_dist) == 3
    return {"budget": budget, "cost": sum(new_dist),
            "old_uncovered": [t for t,d in enumerate(old_dist) if d > 2],
            "hex_mask": center_hex}

def brute_counts(x):
    answer = {}
    for k in range(1, len(x)+1):
        costs = []
        for chosen in combinations(range(len(x)), k):
            dist = [min(abs(x[t]-x[i]) for i in chosen)
                    for t in range(len(x))]
            if max(dist) <= 2:
                costs.append(sum(dist))
        if costs:
            b = min(costs)
            answer[k] = (b, costs.count(b))
    return answer

def main():
    x,cuts = frozen()
    masks = list(dict.fromkeys([0, ALL] +
             [m for i in INERT for m in (1 << i, ALL ^ (1 << i))]))
    spectra = {m: optimum_counts_spectrum(closed_points(x, cuts, m))
               for m in masks}
    none,full = spectra[0],spectra[ALL]
    assert none[214] == (1064,71400940037117596391178240000)
    assert full[214] == (1064,4573020854769248525038387200000)
    assert none[292] == full[292] == (744,247939829006869892620615680)
    assert none[315] == full[315] == (675,402907218691036544772341760000)
    assert none[954] == full[954] == (0,1)
    result = {"status":"PASS_EXACT_R5_INERT_CUT_OPTIMIZER_RESIDUAL",
              "science_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
              "cut_results": {}, "witnesses": {}}
    for cut in INERT:
        single = spectra[1 << cut]
        omit = spectra[ALL ^ (1 << cut)]
        assert set(none).issubset(set(single))
        assert set(omit) == set(full)
        assert all(none[k][0] == single[k][0] and
                   none[k][1] <= single[k][1] for k in none)
        assert all(omit[k][0] == full[k][0] and
                   omit[k][1] <= full[k][1] for k in omit)
        low = [k for k in none if none[k][1] != single[k][1]]
        high = [k for k in omit if omit[k][1] != full[k][1]]
        expected = list(range(293,315)) if cut in ACTIVE else []
        assert low == high == expected, (cut,low,high)
        result["cut_results"][str(cut)] = {
            "none_to_single_changed_budgets": low,
            "all_except_to_all_changed_budgets": high}
        if cut in ACTIVE:
            witness = validate_mask(x,closed_points(x,cuts,1<<cut),
                                    EXPECTED_HEX[cut])
            assert witness["old_uncovered"] == ([194] if cut == 15 else [245])
            assert single[293][0] == witness["cost"]
            result["witnesses"][str(cut)] = witness
    rng = Random(20261114)
    checked = 0
    for n in range(3,9):
        for trial in range(20):
            small = [0]
            for _ in range(n-1):
                small.append(small[-1] + rng.randint(1,4))
            assert brute_counts(small) == optimum_counts_spectrum(small)
            for j in range(n-1):
                if small[j+1]-small[j] == 3:
                    y = [value-int(index>j)
                         for index,value in enumerate(small)]
                    assert brute_counts(y) == optimum_counts_spectrum(y)
                    checked += 1
    assert checked == 139
    result["independent_small_closed_cases"] = checked
    result["review_status"] = "NOT_REVIEWED"
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__ == "__main__":
    main()
