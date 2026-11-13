#!/usr/bin/env python3
"""R762T: exact integer V27/V29 local count repair and closed-network witness.

No floating point, no random sampling. All nonnegative counts and changes follow
V29 primitive PASS/TRANSFER grammar. No native TRIADIC_CLOSURE_E is assumed.
"""
import itertools
import json
from pathlib import Path

N = 4
U = (-2, -4, -3, 10)
ORIENTED = (0, 1, 2)


def zeros():
    return [0] * N


def matrix():
    return [[0] * N for _ in range(N)]


def calc_u(m, ri, ro):
    return [sum(m[i]) - sum(row[i] for row in m) + ri[i] - ro[i] for i in range(N)]


def calc_io(m, ri, ro):
    return ([sum(m[i]) + ri[i] for i in range(N)],
            [sum(row[i] for row in m) + ro[i] for i in range(N)])


def min_boundary(m, u):
    w = [u[i] - sum(m[i]) + sum(row[i] for row in m) for i in range(N)]
    return ([max(v, 0) for v in w], [max(-v, 0) for v in w], w)


def main():
    m = matrix()
    for i,j in zip(ORIENTED, ORIENTED[1:] + ORIENTED[:1]):
        m[i][j] += 1
    ri, ro, w = min_boundary(m, U)
    assert w == list(U)
    assert ri == [0, 0, 0, 10] and ro == [2, 4, 3, 0]
    I, O = calc_io(m, ri, ro)
    assert I == [1, 1, 1, 10] and O == [3, 5, 4, 0]
    assert tuple(calc_u(m, ri, ro)) == U
    assert sum(ri) + sum(ro) == 19
    assert sum(I) - sum(O) == 1

    # Fixed M/u has a nonnegative common-mode fiber.
    for shift in itertools.product(range(3), repeat=N):
        iri = [a + d for a,d in zip(ri, shift)]
        iro = [a + d for a,d in zip(ro, shift)]
        assert tuple(calc_u(m, iri, iro)) == U
        assert sum(iri) + sum(iro) == 19 + 2 * sum(shift)

    # All four-choose-three directed 3-cycles (two orientations each).
    cycles = 0
    for triple in itertools.combinations(range(N),3):
        for order in [triple, (triple[0], triple[2], triple[1])]:
            cm = matrix()
            for a,b in zip(order, order[1:]+order[:1]):
                cm[a][b]+=1
            a,b,w2=min_boundary(cm,U)
            assert w2 == list(U) and sum(a)+sum(b) == 19
            assert tuple(calc_u(cm,a,b)) == U
            cycles+=1
    assert cycles == 8

    coordinate_tests = 0
    for target in range(-10, 11):
        admissible = [(a,b) for a in range(21) for b in range(21) if a-b==target]
        assert admissible
        best = min(a+b for a,b in admissible)
        assert best == abs(target)
        assert admissible.count((max(target,0), max(-target,0))) == 1
        assert sum((a+b)==best for a,b in admissible)==1
        coordinate_tests+=1

    # A is target Cell; B is paired environment Cell.
    cells = {"A": {"M":matrix(),"Ri":zeros(),"Ro":zeros()},
             "B": {"M":matrix(),"Ri":zeros(),"Ro":zeros()}}
    def charge():
        return sum(sum(calc_u(v['M'],v['Ri'],v['Ro'])) for v in cells.values())
    primitive_events=0
    for _ in range(10):
        cells['B']['Ro'][0]+=1
        cells['A']['Ri'][3]+=1
        primitive_events+=1
        assert charge()==0
    for a,k in [(0,2),(1,4),(2,3)]:
        for _ in range(k):
            cells['A']['Ro'][a]+=1
            cells['B']['Ri'][1]+=1
            primitive_events+=1
            assert charge()==0
    assert primitive_events == 19
    for a,b in [(0,1),(1,2),(2,0)]:
        cells['A']['M'][a][b]+=1
        assert charge()==0
    assert cells['A']['M']==m and cells['A']['Ri']==ri and cells['A']['Ro']==ro
    assert tuple(calc_u(m=cells['A']['M'],ri=cells['A']['Ri'],ro=cells['A']['Ro']))==U
    assert sum(calc_u(cells['B']['M'],cells['B']['Ri'],cells['B']['Ro']))==-1
    assert charge()==0

    evidence={
        "schema":"EM_R762T_V27_V29_RECONCILIATION_EXACT_V1",
        "arithmetic":"exact nonnegative integer V29 PASS/TRANSFER",
        "model_scope":"4 local V29 ports; fixed directed 3-cycle M and target u; abstract two-Cell network with explicitly permitted directed connectors",
        "target_u":list(U), "passage_M":m,
        "v27_reported_I":[0,0,0,10],"v27_reported_O":[2,4,3,0],
        "v27_reported_I_and_O_are_valid_as_boundary_Rin_Rout":True,
        "literal_I_O_compatible_with_M":False,
        "repaired_Rin":ri,"repaired_Rout":ro,
        "reconstructed_I":I,"reconstructed_O":O,
        "network_cell_A_contrast":list(U),
        "network_cell_B_scalar_contrast":-1,
        "network_total_charge":charge(),
        "primitive_PASS_count":3,
        "matched_TRANSFER_count":19,
        "center_boundary_L1_minimum":19,
        "local_cycle_orientations_tested":cycles,
        "coordinate_minimality_target_values_tested":coordinate_tests,
        "common_mode_shifts_checked":3**N,
        "checks":"PASS",
        "not_tested":"physical TRIADIC_CLOSURE_E admission, actual V17 frame connection, V27 20-triad scoring implementation",
    }
    output=Path(__file__).with_name('R762T_V27_V29_TYPED_RECONCILIATION_EVIDENCE.json')
    output.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(evidence,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
