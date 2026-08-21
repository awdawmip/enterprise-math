        prime_typing = []
        for pr in d["gaussian_prime_typing"]["prime_typing"]:
            row = [pr["prime"], pr["exponent"], pr["type"]]
            if "pi" in pr:
                row += [pr["pi"], pr["pi_conjugate"], pr["allocation_range"]]
            prime_typing.append(row)
        witnesses.append({
            "N": d["N"],
            "factorization": d["factorization"],
            "gaussian_prime_typing": prime_typing,
            "support": d["support"],
            "blocking_inert_prime_exponents": d["support_criterion"]["blocking_inert_prime_exponents"],
            "signed_gaussian_root_count": d["signed_gaussian_root_count"],
            "ordered_nonnegative_component_roots": d["ordered_nonnegative_component_roots"],
            "unordered_component_shapes": d["unordered_component_shapes"],
            "native_length": radical_length(d["N"])["exact_expression"],
            "root_records": roots,
            "full_discovery_payload_sha256": sha256_obj(discovery_freeze_payload(d)),
        })
    return {
        "schema": "R063_STAGE1_DISCOVERY_PHASE_FROZEN_V1",
        "task": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "taskbook_source": TASKBOOK_SOURCE,
        "owner_branch": OWNER_BRANCH,
        "phase": "ALL_MANDATORY_DISCOVERY_MATERIALIZED_BEFORE_ANY_BRUTE_VERIFICATION",
        "discovery_snapshot_sha256": discovery_sha,
        "artifact_representation": "COMPRESSED_REQUIRED_FIELDS; FULL_IN_MEMORY_DISCOVERY_HASHED_BEFORE_BRUTE",
        "support_criterion": "every q == 3 (mod 4) has even exponent",
        "raw_channel_encoding": "[unit, [[split_prime, pi_exponent, conjugate_exponent], ...]]",
        "path_rule": "[u^a v^b](uX_i+vX_j)^(a+b); exact cardinality binom(a+b,a); a+b is path-letter count, not native length",
        "BRC_role": "DOWNSTREAM_ONLY_NOT_DISCOVERY_INPUT",
        "typing_boundary": "Z[J] sector-local only; no carrier vector identity promoted",
        "witnesses": witnesses,
    }

def compact_sparse_artifact(sparse: Mapping[str, object]) -> Dict[str, object]:
    rows = []
    for row in sparse["rows"]:
        path_rows = row["path_cardinality_compressed"]
        rows.append({
            "N": row["N"],
            "factorization": row["factorization"],
            "support": row["support"],
            "root_count": row["root_count"],
            "discovery_snapshot_sha256": row["discovery_snapshot_sha256"],
            "path_certificate_count": len(path_rows),
            "path_certificates_sha256": sha256_obj(path_rows),
            "max_path_cardinality_bit_length": max((x["bit_length"] for x in path_rows), default=0),
        })
    return {
        "suite": sparse["suite"],
        "max_N": sparse["max_N"],
        "mismatch_count": sparse["mismatch_count"],
        "smallest_mismatch": sparse["smallest_mismatch"],
        "rows_sha256": sha256_obj(sparse["rows"]),
        "rows": rows,
    }

def compact_mandatory_verification(mandatory_ver: Mapping[str, object]) -> Dict[str, object]:
    return {
        "mismatch_count": mandatory_ver["mismatch_count"],
        "rows_sha256": sha256_obj(mandatory_ver["rows"]),
        "rows": [
            {
                "N": row["N"],
                "discovery_snapshot_sha256": row["discovery_snapshot_sha256"],
                "exact_set_equality": row["verification"]["exact_set_equality"],
