        "SQUARE_SCOPE_R063_STAGE0_REGRESSION_PASS": square["pass"],
        "GENERAL_INTEGER_REGRESSION_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED": general["rootset_mismatch_count"] == 0,
        "NO_BRC_ROOT_DISCOVERY_LEAKAGE": all(d["BRC_role"] == "DOWNSTREAM_ONLY_NOT_DISCOVERY_INPUT" for d in discovery_obj["witnesses"]),
        "NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY": all("no carrier vector identity" in d["typing_boundary"] for d in discovery_obj["witnesses"]),
        "NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE": all(
            rr["path"]["path_letter_count_semantics"] == "NOT_NATIVE_LENGTH"
            for d in discovery_obj["witnesses"] for rr in d["root_records"]
        ),
        "COMMITTED_DETERMINISTIC_CHECKER_PASS": not mismatches,
    }

    mismatch_obj = {
        "schema": "R063_STAGE1_MISMATCHES_V1",
        "mismatch_count": len(mismatches),
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "mismatches": mismatches,
    }

    summary_core = {
        "schema": "R063_STAGE1_REPLAY_SUMMARY_V1",
        "task": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "taskbook_source": TASKBOOK_SOURCE,
        "owner_branch": OWNER_BRANCH,
        "mandatory_discovery_snapshot_sha256": discovery_sha,
        "source_anti_hardcode_audit": anti,
        "mandatory_verification": compact_mandatory_verification(mandatory_ver),
        "general_regression": general,
        "sparse_suite": compact_sparse_artifact(sparse),
        "square_scope_regression": square,
        "multiplicative_audit_summary": {
            "pair_audit_count": mult["pair_audit_count"],
            "all_signed_multiplication_maps_surjective": mult["all_signed_multiplication_maps_surjective"],
            "multiplicity_separation_witness": mult["multiplicity_separation_witness"],
        },
        "irrational_discrete_witness_N13": nonsquare["irrational_discrete_witness_N13"],
        "acceptance_gates": gates,
        "mismatch_count": len(mismatches),
        "final_classification": "PATH_NORM_ROOT_OPERATOR_COMPLETE_EXACTLY_ON_SUM_OF_TWO_SQUARES_SUPPORT",
    }
    summary = {**summary_core, "summary_core_sha256": sha256_obj(summary_core)}

    write_json(outdir / "R063_STAGE1_REPLAY_SUMMARY.json", summary)
    write_json(outdir / "R063_STAGE1_ROOT_COUNT_AND_ORBIT_CERTIFICATE.json", root_count)
    write_json(outdir / "R063_STAGE1_NONSQUARE_PATH_FIBER_CERTIFICATE.json", nonsquare)
    write_json(outdir / "R063_STAGE1_GENERAL_REGRESSION.json", {**general, "sparse_suite": compact_sparse_artifact(sparse)})
    write_json(outdir / "R063_STAGE1_MISMATCHES.json", mismatch_obj)
    write_text(outdir / "R063_STAGE1_GENERAL_GAUSSIAN_ROOT_THEOREM.md", markdown_gaussian_theorem())
    write_text(outdir / "R063_STAGE1_SUM_OF_TWO_SQUARES_SUPPORT_THEOREM.md", markdown_support_theorem())
    write_text(outdir / "R063_STAGE1_MULTIPLICATIVE_DERIVATION_AUDIT.md", markdown_multiplicative(mult))
    write_text(outdir / "R063_STAGE1_REPRODUCIBILITY_PROOF.md", markdown_repro(summary))
    write_text(outdir / "R063_STAGE1_FINAL_CLASSIFICATION.md", markdown_final(summary))

    return {"summary": summary, "mismatches": mismatch_obj}

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=Path("research_results/R063_STAGE1"))
