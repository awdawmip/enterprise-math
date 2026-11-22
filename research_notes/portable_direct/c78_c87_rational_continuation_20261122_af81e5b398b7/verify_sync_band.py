"""Exact finite checks for the C78 synchronization-band necessity lemma.

Universal proof: the parent task's NATIVE_SYNC_BAND_PACKING.md.
This script checks finite endpoint/index cases and explicit constants.
It does not enumerate full large inventories or certify the universal theorem
by sampling. All readouts use the original finite rational F_3 product.
"""

from fractions import Fraction as Q
from functools import cache
from pathlib import Path
import json


V_VALUES = (16, 17, 32, 64, 128, 256, 576, 1152, 2304)
H_VALUES = (Q(1, 16), Q(1, 32), Q(1, 64))


def product_error(k, m, n):
    assert 0 <= m <= n
    coefficient = Q(abs(k*(16-9*k*k)), 64)
    shift = Q(5*k, 8)
    return coefficient/2 * ((Q(m)+shift)**-2-(Q(n)+shift)**-2)


def main():
    # Incremental exact original product: F_3(n)=prod(4j+3)/(4(j+3)).
    prefix = [Q(1)]
    for j in range(1, max(V_VALUES)+1):
        prefix.append(prefix[-1]*Q(4*j+3, 4*(j+3)))

    @cache
    def rho(v, w):
        assert 2 <= w <= v
        return 4*prefix[v]/prefix[w-1]

    constant_checks = {}

    def check(name, lhs, relation, rhs):
        accepted = {"<": lhs < rhs, "<=": lhs <= rhs, "=": lhs == rhs,
                    ">": lhs > rhs, ">=": lhs >= rhs}[relation]
        assert accepted, (name, lhs, relation, rhs)
        constant_checks[name] = {"lhs": str(lhs), "relation": relation,
                                 "rhs": str(rhs), "passed": True}

    check("lower_endpoint_power", 256*Q(1, 2)**9, "=", Q(1, 2))
    check("lower_endpoint_separation", Q(1, 2), "<", Q(15, 16)**4)
    check("upper_endpoint_separation", Q(9, 10)*256*Q(2, 3)**9, ">", Q(17, 16)**4)
    check("outer_upper_power", 256*Q(9, 16)**15, "<", Q(1, 16))
    check("outer_lower_power", Q(1, 2)*256*Q(1, 8)**15, "=", Q(1, 2**38))
    check("outer_lower_power_target", Q(1, 2**38), ">", Q(1, 2**64))

    # E_k(m,n) takes product endpoints m,n. At rho_3(V,W), m=W-1.
    check("E3_product_m12_n16", product_error(3, 12, 16), "<", Q(1, 10))
    check("E3_rho_V16_W12_uses_m11_n16", product_error(3, 11, 16), "<", Q(1, 10))
    check("E3_W12_uniform_upper", Q(195, 128)/(12+Q(7, 8))**2, "<", Q(1, 10))
    check("E5_V16_uniform_upper", Q(1045, 128)/(16+Q(17, 8))**2, "<", Q(1, 2))
    check("tail_K_bound", 1+Q(7, 3)*Q(5, 2), "=", Q(41, 6))
    check("F1_ratio_fourth_power", Q(16)**3, "=", Q(8)**4)
    check("F1_ratio_loose_fourth_power", Q(8)**4, "<=", Q(32)**4)

    k1 = Q(4815+90, 4)
    k2 = Q(475260+34485, 32)
    check("K1_plus_K2", k1+k2, "=", Q(548985, 32))
    check("K_sum_integer_bound", k1+k2, "<", Q(17156))
    check("single_step_constant", 60+Q(17156, 64), "=", Q(5249, 16))
    check("single_step_330", 60+Q(17156, 64), "<", Q(330))
    check("b1_step_condition_at_64", Q(1, 64), "<=", Q(1)/(2*Q(75, 4)))

    m0 = 32*Q(41, 6)*448**2*2**16
    packing_m = 330*m0
    check("M0_simplification", m0, "=", Q(2009*2**32, 3))
    check("packing_M_simplification", packing_m, "=", Q(110*2009*2**32))

    # Every residue modulo12 is represented once. Adding12 to V increases
    # these cleared-denominator margins by32,24,144 respectively.
    residue_checks = []
    for v in range(16, 28):
        lo, hi = v//3, 3*v//4
        margins = (8*v-16*lo-3, 24*hi-16*v-5, 144*lo+108-36*v)
        assert all(x > 0 for x in margins)
        next_margins = (8*(v+12)-16*((v+12)//3)-3,
                        24*(3*(v+12)//4)-16*(v+12)-5,
                        144*((v+12)//3)+108-36*(v+12))
        assert tuple(b-a for a, b in zip(margins, next_margins)) == (32, 24, 144)
        ulo = (lo+Q(11, 8))/(v+Q(19, 8))
        uhi = (hi+Q(11, 8))/(v+Q(19, 8))
        assert ulo <= Q(1, 2) and uhi >= Q(2, 3)
        assert Q(9)/(lo+Q(3, 4)) <= Q(36, v)
        residue_checks.append({"V": v, "V_mod_12": v % 12,
                               "W_lo": lo, "W_hi": hi,
                               "cleared_positive_margins": list(margins),
                               "margins_increment_per_12": [32, 24, 144]})

    def first(v, threshold, strict):
        """First legal W satisfying rho>threshold or rho>=threshold."""
        left, right = 2, v+1
        while left < right:
            middle = (left+right)//2
            value = rho(v, middle)
            accepted = value > threshold if strict else value >= threshold
            if accepted:
                right = middle
            else:
                left = middle+1
        return left

    row_checks = []
    difference_samples = set()
    for v in V_VALUES:
        wlo, whi = v//3, 3*v//4
        assert rho(v, wlo) < Q(15, 16)
        assert rho(v, whi) > Q(17, 16)
        difference_samples.update((v, w) for w in (wlo, wlo+1, whi-1)
                                  if 2 <= w < v)
        for h in H_VALUES:
            lower, upper = 1-h, 1+h
            begin = first(v, lower, False)
            after = first(v, upper, True)
            count = after-begin
            assert wlo < begin <= after <= whi
            assert count >= 0
            assert rho(v, begin-1) < lower
            assert rho(v, after) > upper
            if count:
                assert lower <= rho(v, begin) <= upper
                assert lower <= rho(v, after-1) <= upper
            else:
                assert rho(v, begin) > upper
            lower_bound = h*v/18-1
            assert count > lower_bound
            strong = h*v >= 36
            if strong:
                assert count >= h*v/36
            difference_samples.update((v, w) for w in (begin-1, begin, after-1)
                                      if wlo <= w < whi)
            row_checks.append({
                "V": v, "h": str(h), "K": count,
                "W_interval": [begin, after-1] if count else None,
                "first_rho_ge_1_minus_h": begin,
                "first_rho_gt_1_plus_h": after,
                "strict_lower_bound_hV_over_18_minus_1": str(lower_bound),
                "strong_condition_hV_ge_36": strong,
                "strong_lower_bound_hV_over_36": str(h*v/36) if strong else None,
                "threshold_neighbors_checked": True,
            })

    for v, w in sorted(difference_samples):
        actual = rho(v, w+1)-rho(v, w)
        predicted = rho(v, w)*Q(9, 4)/(w+Q(3, 4))
        assert actual == predicted > 0
        assert actual <= Q(36, v)

    counting_boundary_checks = []
    for h in H_VALUES:
        a = Q(144)/h
        c = max(64, -((-a.numerator)//a.denominator))
        first_v, last_v = (c+3)//4, c//2
        rows = last_v-first_v+1
        assert Q(rows) >= Q(c, 8)
        assert h*first_v >= 36
        assert Q(first_v//3) >= Q(c, 16)
        guaranteed_per_row = h*c/144
        assert guaranteed_per_row*rows >= h*c*c/1152
        counting_boundary_checks.append({
            "h": str(h), "c": c, "V_interval": [first_v, last_v],
            "row_count": rows, "row_count_lower": str(Q(c, 8)),
            "per_row_lower": str(guaranteed_per_row),
            "whole_band_lower": str(h*c*c/1152),
        })

    result = {
        "scope": "Finite exact endpoint/index and constant checks. Universal theorem is proved in the parent NATIVE_SYNC_BAND_PACKING.md.",
        "arithmetic": "Python arbitrary-precision integers and fractions.Fraction; no floating point",
        "original_product": "F3(n)=product_{j=1}^n (4j+3)/(4(j+3)); rho3(V,W)=4 F3(V)/F3(W-1)",
        "prefix_maximum": max(V_VALUES),
        "constant_checks": constant_checks,
        "residue_checks": residue_checks,
        "row_checks": row_checks,
        "row_parameter_cases": len(row_checks),
        "difference_samples": [{"V": v, "W": w} for v, w in sorted(difference_samples)],
        "difference_sample_count": len(difference_samples),
        "counting_boundary_checks": counting_boundary_checks,
        "rho_values_evaluated": rho.cache_info().currsize,
        "M0": str(m0), "packing_M": str(packing_m),
        "all_checks_passed": True,
    }
    output = Path(__file__).with_name("sync_band_checks.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({
        "status": "PASS",
        "constant_checks": len(constant_checks),
        "residue_classes": len(residue_checks),
        "row_parameter_cases": len(row_checks),
        "difference_samples": len(difference_samples),
        "rho_values_evaluated": rho.cache_info().currsize,
        "rows": [{"V": r["V"], "h": r["h"], "K": r["K"]} for r in row_checks],
        "M0": str(m0), "packing_M": str(packing_m),
    }, indent=2))


if __name__ == "__main__":
    main()
