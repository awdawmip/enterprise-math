            counts = Counter(gmul(x, y) for x in RA for y in RB)
            surj = set(counts) == RAB
            all_surjective &= surj
            pos = tuple(sorted(z for z in RAB if z[0] >= 0 and z[1] >= 0))
            provenance = []
            for z in pos:
                m = counts[z]
                path_mult = comb(z[0]+z[1], z[0])
                provenance.append({
                    "component_root": list(z),
                    "multiplicative_derivation_pair_count": m,
                    "native_path_multiplicity": path_mult,
                    "equal": m == path_mult,
                })
                if multiplicity_diff_witness is None and m != path_mult:
                    multiplicity_diff_witness = {
                        "A": A, "B": B, "AB": A*B, "component_root": list(z),
                        "multiplicative_derivation_pair_count": m,
                        "native_path_multiplicity": path_mult,
                    }
            rows.append({
                "A": A, "B": B, "AB": A*B,
                "signed_root_counts": [len(RA), len(RB), len(RAB)],
                "multiplication_result_set_equals_AB_signed_rootset": surj,
                "total_multiplication_pairs": len(RA)*len(RB),
                "returned_root_provenance": provenance,
            })
    return {
        "schema": "R063_STAGE1_MULTIPLICATIVE_ROOT_PROVENANCE_V1",
        "base_inputs": list(MULT_BASE),
        "pair_audit_count": len(rows),
        "all_signed_multiplication_maps_surjective": all_surjective,
        "surjectivity_theorem": (
            "For representable A,B, every split-prime exponent allocation for AB can be decomposed "
            "prime-wise into valid allocations for A and B; ramified/inert factors are fixed, and units distribute. "
            "Hence signed Gaussian root multiplication is surjective onto the AB signed root fiber."
        ),
        "rows": rows,
        "multiplicity_separation_witness": multiplicity_diff_witness,
        "classification": "MULTIPLICATIVE_DERIVATION_PROVENANCE_IS_HIGHER_ENRICHMENT_NOT_NATIVE_PATH_MULTIPLICITY",
    }

def square_scope_regression() -> Dict[str, object]:
    rows = []
    for N in (25, 2500):
        d = discover_general(N, detailed=False)
        freeze = sha256_obj(discovery_freeze_payload(d))
        v = verify_one(N, d)
        path_total = sum(comb(a+b, a) for a, b in (tuple(x) for x in d["ordered_nonnegative_component_roots"]))
        row = {
            "N": N, "discovery_snapshot_sha256": freeze, "verification": v,
            "rootset_sha256": sha256_obj(d["ordered_nonnegative_component_roots"]),
            "one_sector_total_path_cardinality": path_total,
        }
        rows.append(row)
    n2500 = next(x for x in rows if x["N"] == 2500)
    return {
        "rows": rows,
        "N2500_rootset_hash_matches_frozen_stage0": n2500["rootset_sha256"] == STAGE0_N2500_ROOTSET_SHA256,
        "N2500_path_total_matches_frozen_stage0": n2500["one_sector_total_path_cardinality"] == STAGE0_N2500_TOTAL_PATH,
        "pass": all(x["verification"]["exact_set_equality"] for x in rows)
                and n2500["rootset_sha256"] == STAGE0_N2500_ROOTSET_SHA256
                and n2500["one_sector_total_path_cardinality"] == STAGE0_N2500_TOTAL_PATH,
    }

