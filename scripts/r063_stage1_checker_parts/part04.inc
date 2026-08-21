        "N": N,
        "factorization": factor_rows(N),
        "gaussian_prime_typing": meta,
        "support": bool(roots),
        "support_criterion": support_reason(factor_integer(N)),
        "signed_gaussian_root_count": len(signed_roots),
        "signed_gaussian_roots": [list(z) for z in signed_roots] if detailed else None,
        "ordered_nonnegative_component_roots": [list(z) for z in roots],
        "unordered_component_shapes": [list(z) for z in shapes],
        "root_count_certificate": count_cert,
        "root_records": root_records,
        "BRC_role": "DOWNSTREAM_ONLY_NOT_DISCOVERY_INPUT",
        "typing_boundary": "Z[J] is sector-local component algebra; no carrier vector identity is promoted to native geometry",
    }

def discovery_freeze_payload(d: Mapping[str, object]) -> Dict[str, object]:
    return {
        "N": d["N"],
        "factorization": d["factorization"],
        "support": d["support"],
        "ordered_nonnegative_component_roots": d["ordered_nonnegative_component_roots"],
        "unordered_component_shapes": d["unordered_component_shapes"],
        "signed_gaussian_root_count": d["signed_gaussian_root_count"],
        "root_count_certificate": d["root_count_certificate"],
    }

def brute_norm_fiber(N: int) -> Tuple[Pair, ...]:
    """BRUTE VERIFICATION PHASE ONLY."""
    out: List[Pair] = []
    for a in range(isqrt(N)+1):
        b2 = N-a*a
        b = isqrt(b2)
        if b*b == b2:
            out.append((a, b))
    return tuple(out)

def verify_one(N: int, discovery: Mapping[str, object]) -> Dict[str, object]:
    brute = brute_norm_fiber(N)
    got = tuple(tuple(x) for x in discovery["ordered_nonnegative_component_roots"])
    return {
        "N": N,
        "phase": "BRUTE_AFTER_DISCOVERY_FREEZE",
        "discovery_set": [list(x) for x in got],
        "brute_set": [list(x) for x in brute],
        "missing": [list(x) for x in sorted(set(brute)-set(got))],
        "extra": [list(x) for x in sorted(set(got)-set(brute))],
        "exact_set_equality": got == brute,
        "support_matches": bool(got) == bool(brute),
    }

def mandatory_discovery_object() -> Dict[str, object]:
    Ns = tuple(sorted(set(MANDATORY_POSITIVE + MANDATORY_NEGATIVE + ANCHORS)))
    rows = [discover_general(N, detailed=True) for N in Ns]
    return {
        "schema": "R063_STAGE1_DISCOVERY_PHASE_FROZEN_V1",
        "task": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "taskbook_source": TASKBOOK_SOURCE,
        "owner_branch": OWNER_BRANCH,
        "phase": "ALL_MANDATORY_DISCOVERY_MATERIALIZED_BEFORE_ANY_BRUTE_VERIFICATION",
        "witnesses": rows,
    }



def compact_discovery_artifact(discovery_obj: Mapping[str, object], discovery_sha: str) -> Dict[str, object]:
    witnesses = []
    for d in discovery_obj["witnesses"]:
        roots = []
        for rr in d["root_records"]:
            roots.append({
                "components": rr["components"],
                "raw_channels": [
                    [ch.get("unit"), [[x["prime"], x["pi_exponent"], x["conjugate_exponent"]] for x in ch.get("split_prime_allocations", [])]]
                    for ch in rr["gaussian_derivation_channels"]
                ],
                "path_polynomial": rr["path"]["compressed_polynomial"],
                "exact_path_cardinality": rr["path"]["exact_path_cardinality"],
            })
