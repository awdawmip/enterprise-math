def nonsquare_certificate(discovery_obj: Mapping[str, object], mandatory_verification: Mapping[str, object]) -> Dict[str, object]:
    verified = {x["N"]: x["verification"] for x in mandatory_verification["rows"]}
    rows = []
    for d in discovery_obj["witnesses"]:
        N = d["N"]
        if N not in MANDATORY_POSITIVE + MANDATORY_NEGATIVE:
            continue
        roots = []
        total = 0
        for rr in d["root_records"]:
            a, b = rr["components"]
            card = rr["path"]["exact_path_cardinality"]
            total += card
            roots.append({
                "components": rr["components"],
                "trace_id": rr["trace_id"],
                "native_length": rr["native_length"],
                "compressed_polynomial": rr["path"]["compressed_polynomial"],
                "exact_path_cardinality": card,
                "path_letter_count": a+b,
            })
        rows.append({
            "N": N,
            "factorization": d["factorization"],
            "support": d["support"],
            "support_reason": d["support_criterion"],
            "ordered_nonnegative_component_roots": d["ordered_nonnegative_component_roots"],
            "unordered_component_shapes": d["unordered_component_shapes"],
            "root_paths": roots,
            "one_sector_total_path_cardinality": total,
            "post_freeze_brute_verification": verified[N],
        })
    n13 = next(x for x in rows if x["N"] == 13)
    return {
        "schema": "R063_STAGE1_NONSQUARE_PATH_FIBER_CERTIFICATE_V1",
        "mandatory_rows": rows,
        "irrational_discrete_witness_N13": {
            "native_length": radical_length(13),
            "integer_addressed_root_count": len(n13["ordered_nonnegative_component_roots"]),
            "one_sector_total_path_cardinality": n13["one_sector_total_path_cardinality"],
            "classification": "IRRATIONAL_SCALAR_NATIVE_LENGTH_WITH_EXACT_DISCRETE_INTEGER_ADDRESSED_PATH_FIBER",
        },
        "negative_support_policy": "EMPTY_INTEGER_ADDRESSED_NATIVE_ROOT_AND_PATH_FIBER; DO_NOT_PATCH_WITH_IRRATIONAL_COMPONENT_COORDINATES",
    }

def root_count_orbit_certificate(discovery_obj: Mapping[str, object], max_n: int) -> Dict[str, object]:
    rows = []
    for d in discovery_obj["witnesses"]:
        cc = d["root_count_certificate"]
        rows.append({
            "N": d["N"], "factorization": d["factorization"],
            "generated_signed_root_count": d["signed_gaussian_root_count"],
            "generated_ordered_nonnegative_root_count": len(d["ordered_nonnegative_component_roots"]),
            "generated_unordered_shape_count": len(d["unordered_component_shapes"]),
            **cc,
        })
    return {
        "schema": "R063_STAGE1_ROOT_COUNT_AND_ORBIT_CERTIFICATE_V1",
        "theorem": (
            "If any q=3 mod4 has odd exponent then r2(N)=0. Otherwise "
            "r2(N)=4*product_{p=1 mod4}(e_p+1). "
            "Ordered nonnegative count = r2/4 + indicator(N square). "
            "Unordered shape count = (ordered_nonnegative + indicator(N=2*s^2))/2."
        ),
        "orbit_explanation": {
            "generic_positive_ordered_root": "4 sign variants per ordered orientation",
            "axis": "two ordered nonnegative orientations, four signed roots total",
            "equal_components": "one ordered nonnegative root, four sign variants",
