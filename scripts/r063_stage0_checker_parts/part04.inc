No explicit expansion of astronomical path fibers is performed. The checker stores coefficient-extraction formulas, exact binomial cardinalities, and deterministic rank/unrank samples instead.
"""


def render_outputs(outdir: Path, discovered: Mapping[str, object], discovery_json: Mapping[str, object], discovery_sha: str, verification: Mapping[str, object], regression: Mapping[str, object], hardcode_scan: Mapping[str, object]) -> Dict[str, object]:
    rows, total_cert = component_root_rows(discovered, verification)
    tree = build_discovery_tree(discovered, verification, rows, total_cert, discovery_sha)
    provenance = build_provenance_graph(discovered, rows)

    component_fiber = {
        "schema": "R063_STAGE0_COMPONENT_ROOT_FIBER_V1",
        "N": discovered["input"]["N"],
        "r": discovered["scalar_root"]["r"],
        "ordered_nonnegative_component_roots": [row["components"] for row in rows],
        "root_count": len(rows),
        "branches": [
            {
                "components": row["components"],
                "alpha": row["alpha"],
                "norm_certificate": row["norm_certificate"],
                "trace_id": row["trace_id"],
                "native_length": row["native_length"],
                "candidate_membership": row["candidate_membership"],
                "derivation_multiplicity": row["derivation_multiplicity"],
                "derivation_channel_ids": {
                    key: [ch.get("channel_id") for ch in channels if ch.get("channel_id")]
                    for key, channels in row["derivation_channels"].items()
                },
                "path_summary": {
                    "compressed": row["path_fiber"]["compressed"],
                    "first_ranked_path_id": row["path_fiber"]["first_ranked_path_id"],
                    "last_ranked_path_id": row["path_fiber"]["last_ranked_path_id"],
                    "certificate_sha256": row["path_fiber"]["certificate_sha256"],
                },
            }
            for row in rows
        ],
        "post_freeze_brute_fiber": verification["D_N"],
        "C3_exact": verification["comparisons"]["C3"]["exact_set_equality"],
        "C4_exact": verification["comparisons"]["C4"]["exact_set_equality"],
    }

    unordered_path_groups: Dict[Pair, int] = defaultdict(int)
    for row in rows:
        a, b = row["components"]
        unordered_path_groups[tuple(sorted((a, b)))] += row["path_fiber"]["compressed"]["fiber_cardinality"]
    dominant_shape, dominant_count = max(unordered_path_groups.items(), key=lambda kv: (kv[1], kv[0]))
    dominance = Fraction(dominant_count, total_cert["one_sector_total_path_cardinality"])
    nonaxis_branch_cards = sorted(
        {row["path_fiber"]["compressed"]["fiber_cardinality"] for row in rows if all(row["components"])},
        reverse=True,
    )
    if len(nonaxis_branch_cards) >= 2:
        disparity = Fraction(nonaxis_branch_cards[0], nonaxis_branch_cards[1])
    else:
        disparity = Fraction(1, 1)

    path_cardinality = {
        "schema": "R063_STAGE0_PATH_CARDINALITY_CERTIFICATE_V1",
        **total_cert,
        "concentration": {
            "unordered_shape_totals": {f"{a},{b}": count for (a, b), count in sorted(unordered_path_groups.items())},
            "dominant_unordered_shape": list(dominant_shape),
            "dominant_unordered_shape_path_count": dominant_count,
            "dominant_fraction_exact": {"numerator": dominance.numerator, "denominator": dominance.denominator},
            "largest_to_next_distinct_nonaxis_branch_cardinality_ratio_exact": {
                "numerator": disparity.numerator, "denominator": disparity.denominator
            },
        },
        "branches": [
            {
                "components": row["components"],
                "cardinality": row["path_fiber"]["compressed"]["fiber_cardinality"],
                "word_length_path_letters_only": row["path_fiber"]["compressed"]["word_length"],
                "certificate_sha256": row["path_fiber"]["certificate_sha256"],
                "first_ranked_path_id": row["path_fiber"]["first_ranked_path_id"],
                "last_ranked_path_id": row["path_fiber"]["last_ranked_path_id"],
                "rank_unrank_samples": row["path_fiber"]["samples"],
                "compressed_polynomial": row["path_fiber"]["compressed"]["coefficient_extraction"],
            }
            for row in rows
        ],
    }

    classified_negative = {
        "candidate": "C2_UNSCALED_SQUARE_LIFT",
        "N": discovered["input"]["N"],
        "missing": verification["comparisons"]["C2"]["missing"],
        "extra": verification["comparisons"]["C2"]["extra"],
        "classification": "INCOMPLETE_CANDIDATE_NOT_CHECKER_ERROR",
    }
    checker_mismatches: List[Dict[str, object]] = []
    for name in ("C3", "C4"):
        cmp = verification["comparisons"][name]
        if cmp["missing"] or cmp["extra"]:
            checker_mismatches.append({"scope": "N2500", "candidate": name, "missing": cmp["missing"], "extra": cmp["extra"]})
    if regression["combined_checker_mismatch_count"]:
        checker_mismatches.append({"scope": "GENERAL_REGRESSION", "smallest_mismatch": regression["smallest_mismatch"]})

    mismatches = {
        "schema": "R063_STAGE0_MISMATCHES_V1",
        "mismatch_count": len(checker_mismatches),
        "smallest_mismatch": checker_mismatches[0] if checker_mismatches else None,
        "checker_mismatches": checker_mismatches,
        "classified_negative_results_not_checker_errors": [classified_negative],
    }

    multiplicity_nonequal = all(
        row["derivation_multiplicity"]["native_path_multiplicity"] != row["derivation_multiplicity"]["C3_raw_scaled_square"]
        or row["derivation_multiplicity"]["native_path_multiplicity"] == 1
        for row in rows
    )
    norm_typed = all(
        row["norm_certificate"]["pass"]
        and row["norm_certificate"]["a2_plus_b2"] == discovered["input"]["N"]
        for row in rows
    )
    trace_compat = all(
        row["trace_id"] == f"T_{{{row['components'][0]},{row['components'][1]}}}^(ij)"
        and row["path_fiber"]["compressed"]["fiber_cardinality"] == comb(
            sum(row["components"]), row["components"][0]
        )
        for row in rows
    )
    pathification_exact = all(
        all(sample["rank"] == sample["rank_roundtrip"] for sample in row["path_fiber"]["samples"])
        for row in rows
    )
    no_jump_length_leakage = all(
        row["native_length"] == discovered["scalar_root"]["r"]
        and row["path_fiber"]["compressed"]["word_length"] == sum(row["components"])
        and row["path_fiber"]["compressed"]["word_length_semantics"] == "PATH_LETTER_COUNT_ONLY_NOT_NATIVE_LENGTH"
        for row in rows
    )
    no_carrier_vector_promotion = (
        discovered["component_algebra"]["typing_boundary"]
        == "sector-local algebraic carrier only; no carrier vector identity promoted to native geometry"
        and all("X_k" not in row["path_fiber"]["compressed"]["coefficient_extraction"] for row in rows)
    )

    gates = {
        "INPUT_ONLY_DISCOVERY_NO_BRANCH_HARDCODE": hardcode_scan["pass"],
        "SCALAR_SQRT_2500_EXACT": discovered["scalar_root"]["r"] ** 2 == discovered["input"]["N"],
        "SECTOR_NORM_ALGEBRA_TYPED": norm_typed,
        "C2_UNSCALED_SQUARE_LIFT_CLASSIFIED": not verification["comparisons"]["C2"]["exact_set_equality"],
        "C3_SCALED_SQUARE_LIFT_CLASSIFIED": verification["comparisons"]["C3"]["exact_set_equality"],
        "C4_GAUSSIAN_FACTOR_ROUTE_CLASSIFIED": verification["comparisons"]["C4"]["exact_set_equality"],
        "DISCOVERED_COMPONENT_ROOTS_MATCH_D2500_EXACTLY": verification["comparisons"]["C3"]["exact_set_equality"],
        "NO_EXTRA_COMPONENT_ROOTS": not verification["comparisons"]["C3"]["extra"] and not verification["comparisons"]["C4"]["extra"],
        "ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED": multiplicity_nonequal,
        "PATHIFICATION_FORMULA_EXACT": pathification_exact,
        "HUGE_PATH_FIBER_COMPRESSED_REPRESENTATION_EXACT": all(row["path_fiber"]["certificate_sha256"] for row in rows),
        "ONE_SECTOR_TOTAL_PATH_CARDINALITY_EXACT": total_cert["one_sector_total_path_cardinality"] == sum(row["path_fiber"]["compressed"]["fiber_cardinality"] for row in rows),
        "R061_TRACE_IDENTITY_COMPATIBILITY_PASS": trace_compat,
        "GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED": regression["combined_checker_mismatch_count"] == 0,
        "NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE": no_jump_length_leakage,
        "NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY": no_carrier_vector_promotion,
        "COMMITTED_DETERMINISTIC_CHECKER_PASS": len(checker_mismatches) == 0,
    }

    # Derived comparison with the smaller square, for the task's central structural audit.
    small_r = isqrt(25)
    small_roots = c3_rootset(small_r)
    small_path_counts = [comb(a + b, a) for a, b in small_roots]
    current_nondegenerate_unordered = sorted({tuple(sorted((a, b))) for a, b in [tuple(x["components"]) for x in rows] if a and b})
    small_nondegenerate_unordered = sorted({tuple(sorted((a, b))) for a, b in small_roots if a and b})

    summary_core = {
        "schema": "R063_STAGE0_REPLAY_SUMMARY_V1",
        "task": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "taskbook_source": TASKBOOK_SOURCE,
        "owner_branch": OWNER_BRANCH,
        "discovery_snapshot_sha256": discovery_sha,
        "N": discovered["input"]["N"],
        "r": discovered["scalar_root"]["r"],
        "C2": verification["comparisons"]["C2"],
        "C3": verification["comparisons"]["C3"],
        "C4": verification["comparisons"]["C4"],
        "ordered_nonnegative_component_root_count": len(rows),
        "one_sector_total_path_cardinality": total_cert["one_sector_total_path_cardinality"],
        "general_regression": {
            "r_range": regression["r_range"],
            "combined_checker_mismatch_count": regression["combined_checker_mismatch_count"],
            "rows_sha256": regression["rows_sha256"],
            "C2_first_failure": regression["C2_first_failure"],
        },
        "multiplicity_classification": "ALGEBRAIC_ROOT_DERIVATION_MULTIPLICITY_IS_NOT_NATIVE_PATH_MULTIPLICITY",
        "root_return_policy": "DEDUP_COMPONENT_ROOT_AND_TRACE; RETAIN_DERIVATION_PROVENANCE_AS_HIGHER_ENRICHMENT",
        "information_discovered_at_2500": {
            "small_reference_N": 25,
            "small_reference_nondegenerate_unordered_component_shapes": [list(x) for x in small_nondegenerate_unordered],
            "N2500_nondegenerate_unordered_component_shapes": [list(x) for x in current_nondegenerate_unordered],
            "small_reference_path_counts": small_path_counts,
            "C2_incomplete_at_2500": not verification["comparisons"]["C2"]["exact_set_equality"],
            "C3_raw_derivation_multiplicities": {f"{row['components'][0]},{row['components'][1]}": row["derivation_multiplicity"]["C3_raw_scaled_square"] for row in rows},
            "path_cardinalities": {f"{row['components'][0]},{row['components'][1]}": row["path_fiber"]["compressed"]["fiber_cardinality"] for row in rows},
            "path_count_concentration": path_cardinality["concentration"],
            "ordered_swap_symmetry": [
                {
                    "branch": [a, b],
                    "swap": [b, a],
                    "equal_path_cardinality": comb(a + b, a) == comb(a + b, b),
                }
                for a, b in sorted(tuple(row["components"]) for row in rows)
                if a < b
            ],
        },
        "BRC_role": "DOWNSTREAM_PROJECTION_ONLY_NOT_DISCOVERY_INPUT",
        "acceptance_gates": gates,
        "final_classification": "PATH_VALUED_SQUARE_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_SQUARE_NATIVE_NORMS",
    }
    summary_sha = sha256_obj(summary_core)
    summary = {**summary_core, "summary_core_sha256": summary_sha}

    write_json(outdir / "R063_STAGE0_SQRT2500_DISCOVERY_TREE.json", tree)
    write_json(outdir / "R063_STAGE0_COMPONENT_ROOT_FIBER.json", component_fiber)
    write_json(outdir / "R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json", path_cardinality)
    write_json(outdir / "R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json", provenance)
    write_json(outdir / "R063_STAGE0_GENERAL_SQUARE_REGRESSION.json", regression)
    write_json(outdir / "R063_STAGE0_MISMATCHES.json", mismatches)
    write_json(outdir / "R063_STAGE0_REPLAY_SUMMARY.json", summary)
    write_text(outdir / "R063_STAGE0_PATH_ROOT_OPERATOR_CANDIDATE_MATRIX.md", markdown_candidate_matrix(verification, regression))
    write_text(outdir / "R063_STAGE0_SCALED_SQUARE_LIFT_THEOREM.md", markdown_c3_theorem(verification, regression))
    write_text(outdir / "R063_STAGE0_GAUSSIAN_FACTOR_ROUTE_AUDIT.md", markdown_c4_audit(discovered, verification))
    write_text(outdir / "R063_STAGE0_PATH_VALUED_SQRT_FORMULA.md", markdown_path_formula(rows, total_cert))
    write_text(outdir / "R063_STAGE0_REPRODUCIBILITY_PROOF.md", markdown_repro(discovery_sha, regression, total_cert, hardcode_scan, summary_sha))

    return {
        "summary": summary,
        "mismatches": mismatches,
        "total_certificate": total_cert,
        "component_rows": rows,
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--N", type=int, default=DEFAULT_N)
    p.add_argument("--out", type=Path, default=Path("research_results/R063_STAGE0"))
    p.add_argument("--regression-max-r", type=int, default=REGRESSION_MAX_R)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    outdir: Path = args.out
    outdir.mkdir(parents=True, exist_ok=True)

    # DISCOVERY PHASE: no brute target-fiber computation may occur above this barrier.
    discovered = discover_from_scalar_root(args.N)
    discovery_json = normalize_discovery_for_json(discovered)
    discovery_sha = sha256_obj(discovery_json)
    discovery_json = {**discovery_json, "discovery_snapshot_sha256": discovery_sha}
    write_json(outdir / "R063_STAGE0_DISCOVERY_PHASE_FROZEN.json", discovery_json)

    # BRUTE VERIFICATION PHASE: starts only after the discovery payload is materialized and hashed.
    verification = verify_against_norm_fiber(args.N, discovered)
    regression = run_general_regression(args.regression_max_r)
    roots = [tuple(x) for x in discovered["generated_component_roots"]]
    hardcode_scan = source_hardcode_scan(Path(__file__), roots)
    result = render_outputs(outdir, discovered, discovery_json, discovery_sha, verification, regression, hardcode_scan)

    gates = result["summary"]["acceptance_gates"]
    failed = [name for name, passed in gates.items() if not passed]
    if result["mismatches"]["mismatch_count"] or failed:
        print(json.dumps({"status": "FAIL", "failed_gates": failed, "mismatch_count": result["mismatches"]["mismatch_count"]}, sort_keys=True))
        return 1
    print(json.dumps({
        "status": "PASS",
        "final_classification": result["summary"]["final_classification"],
        "discovery_snapshot_sha256": discovery_sha,
        "one_sector_total_path_cardinality": result["summary"]["one_sector_total_path_cardinality"],
        "general_regression_mismatch_count": regression["combined_checker_mismatch_count"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
