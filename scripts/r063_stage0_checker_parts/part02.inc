    return rank


def lex_unrank(n: int, k: int, rank: int) -> List[int]:
    total = comb(n, k)
    if not (0 <= rank < total):
        raise ValueError("rank out of range")
    if k == 0:
        return []
    out: List[int] = []
    prev = 0
    rem_rank = rank
    for i in range(k):
        remaining = k - i - 1
        x = prev + 1
        while x <= n:
            block = comb(n - x, remaining)
            if rem_rank < block:
                out.append(x)
                prev = x
                break
            rem_rank -= block
            x += 1
        else:
            raise ArithmeticError("unrank failed")
    return out


def path_id(a: int, b: int, positions: Sequence[int]) -> str:
    pos = ",".join(str(x) for x in positions) if positions else "EMPTY"
    return f"{SECTOR}-T{a}-{b}-X_i_POS-{pos}"


def path_branch_certificate(a: int, b: int) -> Dict[str, object]:
    n = a + b
    cardinality = comb(n, a)
    sample_ranks = sorted(set((0, cardinality // 2, cardinality - 1)))
    samples: List[Dict[str, object]] = []
    for rank in sample_ranks:
        positions = lex_unrank(n, a, rank)
        replay_rank = lex_rank(n, a, positions)
        if replay_rank != rank:
            raise ArithmeticError("rank/unrank mismatch")
        samples.append({
            "rank": rank,
            "X_i_positions_1_based": positions,
            "path_id": path_id(a, b, positions),
            "rank_roundtrip": replay_rank,
        })
    first = lex_unrank(n, a, 0)
    last = lex_unrank(n, a, cardinality - 1)
    compressed = {
        "coefficient_extraction": f"[u^{a} v^{b}](uX_i+vX_j)^{n}",
        "coefficient_markers": "u,v commute",
        "path_generators": "X_i,X_j noncommute",
        "word_length": n,
        "word_length_semantics": "PATH_LETTER_COUNT_ONLY_NOT_NATIVE_LENGTH",
        "fiber_cardinality": cardinality,
    }
    cert_core = {
        "a": a,
        "b": b,
        "compressed": compressed,
        "first_positions": first,
        "last_positions": last,
        "samples": samples,
    }
    return {
        **cert_core,
        "first_ranked_path_id": path_id(a, b, first),
        "last_ranked_path_id": path_id(a, b, last),
        "certificate_sha256": sha256_obj(cert_core),
    }


def branch_map_to_json(branches: Mapping[Pair, List[Dict[str, object]]]) -> Dict[str, object]:
    return {f"{a},{b}": channels for (a, b), channels in sorted(branches.items())}


def normalize_discovery_for_json(discovered: Mapping[str, object]) -> Dict[str, object]:
    out = dict(discovered)
    c2 = dict(out["C2"])
    c2["branches"] = branch_map_to_json(c2["branches"])
    out["C2"] = c2
    c3 = dict(out["C3"])
    c3["raw_branches"] = branch_map_to_json(c3["raw_branches"])
    c3["canonical_branches"] = branch_map_to_json(c3["canonical_branches"])
    out["C3"] = c3
    c4 = dict(out["C4"])
    c4["branches"] = branch_map_to_json(c4["branches"])
    out["C4"] = c4
    return out


def run_general_regression(max_r: int = REGRESSION_MAX_R) -> Dict[str, object]:
    rows: List[Dict[str, object]] = []
    checker_mismatches: List[Dict[str, object]] = []
    c2_failures: List[Dict[str, object]] = []
    for r in range(1, max_r + 1):
        N = r * r
        c2 = set(c2_rootset(r))
        c3 = set(c3_rootset(r))
        c4 = set(c4_rootset(N))
        brute = set(brute_norm_fiber(N))
        c3_missing = sorted(brute - c3)
        c3_extra = sorted(c3 - brute)
        c4_missing = sorted(brute - c4)
        c4_extra = sorted(c4 - brute)
        if c3_missing or c3_extra or c4_missing or c4_extra:
            checker_mismatches.append({
                "r": r,
                "N": N,
                "C3_missing": [list(x) for x in c3_missing],
                "C3_extra": [list(x) for x in c3_extra],
                "C4_missing": [list(x) for x in c4_missing],
                "C4_extra": [list(x) for x in c4_extra],
            })
        c2_missing = sorted(brute - c2)
        c2_extra = sorted(c2 - brute)
        if c2_missing or c2_extra:
            c2_failures.append({
                "r": r,
                "N": N,
                "missing": [list(x) for x in c2_missing],
                "extra": [list(x) for x in c2_extra],
            })
        row = {
            "r": r,
            "N": N,
            "brute_branch_count": len(brute),
            "C2_exact": c2 == brute,
            "C3_exact": c3 == brute,
            "C4_exact": c4 == brute,
            "fiber_sha256": sha256_obj([list(x) for x in sorted(brute)]),
        }
        rows.append(row)
    rows_sha = sha256_obj(rows)
    smallest = checker_mismatches[0] if checker_mismatches else None
    first_c2 = c2_failures[0] if c2_failures else None
    return {
        "schema": "R063_STAGE0_GENERAL_SQUARE_REGRESSION_V1",
        "r_range": [1, max_r],
        "tested_r_count": max_r,
        "C3_mismatch_count": sum(1 for x in checker_mismatches if x["C3_missing"] or x["C3_extra"]),
        "C4_mismatch_count": sum(1 for x in checker_mismatches if x["C4_missing"] or x["C4_extra"]),
        "combined_checker_mismatch_count": len(checker_mismatches),
        "smallest_mismatch": smallest,
        "C2_first_failure": first_c2,
        "C2_failure_count": len(c2_failures),
        "rows_sha256": rows_sha,
        "row_certificate": "ALL_R_ROWS_REGENERATED_IN_MEMORY_THEN_HASHED; OMITTED_FROM_ARTIFACT_TO_KEEP_CERTIFICATE_COMPRESSED",
        "strong_result": "C3_AND_C4_EXACT_FOR_ALL_TESTED_SQUARES" if not checker_mismatches else "REGRESSION_COUNTEREXAMPLE_PRESERVED",
    }


def source_hardcode_scan(script_path: Path, roots: Sequence[Pair]) -> Dict[str, object]:
    part_dir = script_path.with_name("r063_stage0_checker_parts")
    if part_dir.is_dir():
        part_files = sorted(part_dir.glob("part*.inc"))
        source = script_path.read_text(encoding="utf-8") + "".join(p.read_text(encoding="utf-8") for p in part_files)
        scanned_files = [script_path.name] + [f"{part_dir.name}/{p.name}" for p in part_files]
    else:
        source = script_path.read_text(encoding="utf-8")
        scanned_files = [script_path.name]
    hits: List[str] = []
    for a, b in roots:
        if a == 0 or b == 0:
            continue
        for pattern in (f"({a}, {b})", f"({a},{b})", f"[{a}, {b}]", f"[{a},{b}]"):
            if pattern in source:
                hits.append(pattern)
    return {
        "scanned_files": scanned_files,
        "nontrivial_discovered_pair_literal_hits": sorted(set(hits)),
        "pass": not hits,
    }


def component_root_rows(discovered: Mapping[str, object], verification: Mapping[str, object]) -> Tuple[List[Dict[str, object]], Dict[str, object]]:
    r = discovered["scalar_root"]["r"]
    N = discovered["input"]["N"]
    roots = [tuple(x) for x in discovered["generated_component_roots"]]
    c2_branches = discovered["C2"]["branches"]
    c3_raw = discovered["C3"]["raw_branches"]
    c3_can = discovered["C3"]["canonical_branches"]
    c4_branches = discovered["C4"]["branches"]
    rows: List[Dict[str, object]] = []
    total = 0
    for a, b in roots:
        path = path_branch_certificate(a, b)
        card = path["compressed"]["fiber_cardinality"]
        total += card
        row = {
            "components": [a, b],
            "alpha": f"{a}+{b}J",
            "norm_certificate": {"a2_plus_b2": a * a + b * b, "target_N": N, "pass": a * a + b * b == N},
            "native_length": r,
            "trace_id": f"T_{{{a},{b}}}^(ij)",
            "path_fiber": path,
            "candidate_membership": {
                "C2": (a, b) in c2_branches,
                "C3": (a, b) in c3_can,
                "C4": (a, b) in c4_branches,
            },
            "derivation_multiplicity": {
                "C2": len(c2_branches.get((a, b), [])),
                "C3_raw_scaled_square": len(c3_raw.get((a, b), [])),
                "C3_canonical": len(c3_can.get((a, b), [])),
                "C4_factor_allocation": len(c4_branches.get((a, b), [])),
                "native_path_multiplicity": card,
            },
            "derivation_channels": {
                "C2": c2_branches.get((a, b), []),
                "C3_raw_scaled_square": c3_raw.get((a, b), []),
                "C3_canonical": c3_can.get((a, b), []),
                "C4_factor_allocation": c4_branches.get((a, b), []),
            },
            "downstream_BRC_projection_not_used_for_discovery": {
                "path_formal_witness_count": card,
                "N_BRC_terminal_multiplicity": card,
                "Boolean_BRC_support": 1,
            },
        }
        rows.append(row)
    total_cert = {
        "N": N,
        "r": r,
        "ordered_nonnegative_branch_count": len(rows),
        "one_sector_total_path_cardinality": total,
        "branch_certificate_sha256s": [x["path_fiber"]["certificate_sha256"] for x in rows],
    }
    total_cert["total_certificate_sha256"] = sha256_obj(total_cert)
    return rows, total_cert


def build_discovery_tree(discovered: Mapping[str, object], verification: Mapping[str, object], rows: Sequence[Mapping[str, object]], total_cert: Mapping[str, object], discovery_sha: str) -> Dict[str, object]:
    r = discovered["scalar_root"]["r"]
    N = discovered["input"]["N"]
    c3 = discovered["C3"]
    c4 = discovered["C4"]
    return {
        "schema": "R063_STAGE0_SQRT2500_DISCOVERY_TREE_V1",
        "input": {"N": N},
        "scalar_root": discovered["scalar_root"],
        "phase_separation": {
            "discovery_snapshot_sha256_before_brute": discovery_sha,
            "brute_verifier_called_after_snapshot": True,
            "no_brute_data_flow_back_into_discovery": True,
        },
        "tree": {
            "integer_factorization": {
                "r": factor_rows(r),
                "N": factor_rows(N),
            },
            "C2_unscaled_square_channels": {
                "beta_pairs": discovered["C2"]["canonical_beta_pairs"],
                "component_roots": [list(x) for x in sorted(discovered["C2"]["branches"].keys())],
            },
            "C3_scaled_square_channels": {
                "divisor_routes": c3["divisor_routes"],
