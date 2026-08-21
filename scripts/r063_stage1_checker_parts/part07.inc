                "discovery_set": [list(x) for x in got],
                "brute_set": [list(x) for x in brute],
            })
        if d["support"] != bool(brute):
            support_mismatches += 1
        cc = d["root_count_certificate"]
        shapes = len(d["unordered_component_shapes"])
        if (cc["ordered_nonnegative_component_root_count_formula"] != len(got)
                or cc["unordered_component_shape_count_formula"] != shapes):
            count_mismatches += 1
        for a, b in got:
            card = comb(a+b, a)
            if card <= 0 or bigint_sha256(card) != path_certificate(a, b, include_decimal=False)["cardinality_sha256_unsigned_big_endian"]:
                path_mismatches += 1
        row = {
            "N": N,
            "support": d["support"],
            "root_count": len(got),
            "signed_root_count": d["signed_gaussian_root_count"],
            "freeze_sha256": freeze_sha,
        }
        h.update(canonical_json_bytes(row) + b"\n")
    return {
        "schema": "R063_STAGE1_GENERAL_REGRESSION_V1",
        "N_range": [1, max_n],
        "tested_N_count": max_n,
        "representable_N_count": representable,
        "total_ordered_nonnegative_roots": total_roots,
        "rootset_mismatch_count": len(mismatches),
        "support_mismatch_count": support_mismatches,
        "count_formula_mismatch_count": count_mismatches,
        "path_cardinality_mismatch_count": path_mismatches,
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "rows_sha256": h.hexdigest(),
    }

def run_sparse_suite() -> Dict[str, object]:
    rows = []
    mismatches = []
    for N in SPARSE_SUITE:
        if N < 1 or N > 10**9:
            raise AssertionError("sparse suite out of range")
        d = discover_general(N, detailed=False)
        freeze_sha = sha256_obj(discovery_freeze_payload(d))
        brute = brute_norm_fiber(N)
        got = tuple(tuple(x) for x in d["ordered_nonnegative_component_roots"])
        if got != brute:
            mismatches.append({"N": N, "factorization": d["factorization"], "discovery_set": got, "brute_set": brute})
        path_comp = []
        for a, b in got:
            card = comb(a+b, a)
            path_comp.append({
                "components": [a, b],
                "bit_length": card.bit_length(),
                "sha256_unsigned_big_endian": bigint_sha256(card),
            })
        rows.append({
            "N": N, "factorization": d["factorization"], "support": d["support"],
            "root_count": len(got), "discovery_snapshot_sha256": freeze_sha,
            "path_cardinality_compressed": path_comp,
        })
    return {
        "suite": list(SPARSE_SUITE),
        "max_N": max(SPARSE_SUITE),
        "rows": rows,
        "mismatch_count": len(mismatches),
        "smallest_mismatch": min(mismatches, key=lambda x: x["N"]) if mismatches else None,
    }

def signed_rootset(N: int) -> Tuple[Gaussian, ...]:
    return tuple(sorted(gaussian_signed_root_channels(N, detailed=False)[0]))

def multiplicative_audit() -> Dict[str, object]:
    rows = []
    all_surjective = True
    multiplicity_diff_witness = None
    for i, A in enumerate(MULT_BASE):
        for B in MULT_BASE[i:]:
            RA = signed_rootset(A)
            RB = signed_rootset(B)
            RAB = set(signed_rootset(A*B))
