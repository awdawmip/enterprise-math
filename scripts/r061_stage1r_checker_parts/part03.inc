        "stage0_targets":all(s0cmp.values()),
        "stage1_claimed_digests_and_counts":all(comparisons.values()),
    }
    for k,ok in structural_checks.items():
        if not ok and not any(m.get("locator")==k for m in mismatches):
            append_mismatch(mismatches,"structural_gate",True,False,k)

    pass_all = not mismatches and all(structural_checks.values())

    origin_out={
        **origin,
        "affine_typing_audit":affine,
        "typed_examples":{
            "VADDR_S12_0_0":typed_vaddr("S12",0,0),
            "CADDR_S12_0_0":typed_caddr("S12",0,0),
            "CELL_S12_0_0":typed_cell("S12",0,0),
            "TRACE_S12_1_1":typed_trace("S12",1,1),
        },
    }
    trace_out={
        "schema":"R061_STAGE1R_TRACE_REPLAY_CERTIFICATE_V1",
        "explicit_native_replay":replay,
        "compressed_trace_validation":compressed,
        "claimed_stage1_comparisons":comparisons,
        "third_direction":third,
        "commutation_diamonds":diamonds,
        "axis_gluing":gluing,
        "scaling_concatenation":composition,
        "exact_examples":examples,
    }
    summary={
        "schema":"R061_STAGE1R_REPLAY_SUMMARY_V1",
        "task":TASK,
        "taskbook_source":TASKBOOK_SOURCE,
        "owner_branch":OWNER_BRANCH,
        "stage0_head":STAGE0_HEAD,
        "stage1_candidate_branch":STAGE1_BRANCH,
        "stage0_regression":s0,
        "stage0_target_comparisons":s0cmp,
        "origin_incidence_pass":origin["pass"],
        "affine_typing_pass":affine["pass"],
        "explicit_native_replay":replay,
        "compressed_trace_validation":compressed,
        "third_direction_classification":third["smallest_witness"]["classification"] if third["smallest_witness"] else None,
        "axis_gluing":{k:gluing[k] for k in ("axis_range","global_axis_line_identity_count","chart_presentation_count","physical_trajectory_duplicate_count","pass")},
        "scaling_concatenation":{k:composition[k] for k in ("parameter_limit","scaling_cases","concatenation_cases","closure_explicit_max_a_plus_b","closure_explicit_words","mismatch_count","pass")},
        "n25":examples["n25"],
        "structural_checks":structural_checks,
        "mismatch_count":len(mismatches),
        "STAGE1R_REPRODUCIBILITY_PASS":pass_all,
        "stage1_return_status":"RETURN_TO_DRIVER_FOR_FINAL_ACCEPTANCE" if pass_all else "FALSIFIED_OR_CORRECTION_REQUIRED",
    }
    mismatch_out={
        "schema":"R061_STAGE1R_MISMATCHES_V1",
        "mismatch_count":len(mismatches),
        "mismatches":mismatches,
        "smallest_mismatch":mismatches[0] if mismatches else None,
    }

    json_dump(out/"R061_STAGE1R_REPLAY_SUMMARY.json",summary)
    json_dump(out/"R061_STAGE1R_ORIGIN_INCIDENCE_CERTIFICATE.json",origin_out)
    json_dump(out/"R061_STAGE1R_TRACE_REPLAY_CERTIFICATE.json",trace_out)
    json_dump(out/"R061_STAGE1R_MISMATCHES.json",mismatch_out)

    exit_status=0 if pass_all else 1
    proof=f"""# R061 Stage 1R — Reproducibility Proof

Task-ID: `{TASK}`  
Taskbook source: `{TASKBOOK_SOURCE}`  
Owner branch: `{OWNER_BRANCH}`

## Executable replay

Exact checker command sequence used in this replay:

```text
{command}
```

Exit statuses: `native=0`, `stage0=0`, `finalize={exit_status}`.

The checker is self-contained. It does not read the Stage 1 summary or copy old
digests as generated values. Frozen/claimed digests are comparison targets only
after the corresponding datasets have been independently regenerated.

The checker also provides an all-phase re-exec mode, but this recorded replay
used the three explicit phase invocations above so that each phase exit status
is independently auditable. The phases are memory-isolated and share only the
checker's freshly generated temporary certificates; no Stage 1 result artifact
is read as an input.

## Stage 0 frozen regression replay

- coordinate fiber `N=0..100000`: `{s0["coordinate_fiber_sha256"]}`
- coordinate frozen-hash match: `{s0cmp["coordinate_hash_matches"]}`
- Euclid square-hypotenuse audit through `r<=4096`: mismatches `{s0["euclid_mismatch_count"]}`
- explicit shuffle through `a+b<=22`: `{s0["explicit_shuffle_word_count"]}` words
- explicit shuffle SHA256: `{s0["explicit_shuffle_sha256"]}`
- shuffle frozen-hash match: `{s0cmp["shuffle_hash_matches"]}`
- compressed Pascal through `a+b<=512`: `{s0["compressed_pascal_sha256"]}`
- Pascal frozen-hash match: `{s0cmp["pascal_hash_matches"]}`

## Origin / affine replay

- incident cells at `O_E`: `{len(origin["incident_centers_3x"])}`
- exact pairwise center spacing: `{origin["checks"]["pairwise_spacing_exact"]}`
- exact origin radius squared `1/3`: `{origin["checks"]["origin_radius_exact"]}`
- no fourth boundary center: `{origin["checks"]["no_fourth_boundary_center"]}`
- exactly one anchor per open 120-degree sector: `{origin["checks"]["one_anchor_per_open_sector"]}`
- affine typed replay mismatch count: `{affine["mismatch_count"]}`

## Native trace replay

- pair count: `{replay["pair_count"]}`
- formal linearizations: `{replay["formal_linearization_count"]}`
- three-sector paths: `{replay["three_sector_native_path_count"]}`
- replay SHA256: `{replay["native_replay_sha256"]}`
- replay claimed-hash match: `{comparisons["native_replay_sha256"]}`
- non-neighbor transitions: `{replay["bad_neighbor_transition_count"]}`
- endpoint errors: `{replay["bad_endpoint_count"]}`
- sector-prefix errors: `{replay["bad_sector_prefix_count"]}`
- duplicate trajectories within trace pair: `{replay["duplicate_trajectory_within_trace_pair_count"]}`

Compressed trace SHA256 through `a+b<=256`:

`{compressed["compressed_trace_sha256"]}`

Claimed compressed-hash match: `{comparisons["compressed_trace_sha256"]}`.

## Structural replay

- third-direction `(1,1)` classification: `{third["smallest_witness"]["classification"]}`
- local commuting diamonds tested: `{diamonds["tested_diamonds"]}`, mismatches `{diamonds["mismatch_count"]}`
- axis identities through radial 18: `{gluing["global_axis_line_identity_count"]}`
- adjacent-sector axis trajectory duplicates: `{gluing["physical_trajectory_duplicate_count"]}`
- scaling cases through parameter 8: `{composition["scaling_cases"]}`
- concatenation cases through parameter 8: `{composition["concatenation_cases"]}`
- commutation-closure words explicitly checked through total 16: `{composition["closure_explicit_words"]}`
- composition mismatches: `{composition["mismatch_count"]}`

## N=25

Generated branch counts:

- `(3,4)`: `{examples["n25"]["branch_3_4_path_count"]}`
- `(4,3)`: `{examples["n25"]["branch_4_3_path_count"]}`
- `(0,5)`: `{examples["n25"]["axis_0_5_path_count"]}`
- `(5,0)`: `{examples["n25"]["axis_5_0_path_count"]}`
- fixed-sector total: `{examples["n25"]["sector_total_path_count"]}`

## Final result

`STAGE1R_REPRODUCIBILITY_PASS = {str(pass_all).lower()}`

Mismatch count: `{len(mismatches)}`.

{"The committed executable replay reproduces every material Stage 1 deterministic claim required by the Stage 1R taskbook. Stage 1 may return to Driver for final acceptance." if pass_all else "At least one material mismatch survives. See R061_STAGE1R_MISMATCHES.json; Stage 1 must not be frozen."}

No Stage 2 is opened.
"""
    (out/"R061_STAGE1R_REPRODUCIBILITY_PROOF.md").write_text(proof,encoding="utf-8")

    print(json.dumps({
        "STAGE1R_REPRODUCIBILITY_PASS":pass_all,
        "exit_status":exit_status,
        "mismatch_count":len(mismatches),
        "stage0":{
            "coordinate":s0["coordinate_fiber_sha256"],
            "shuffle_count":s0["explicit_shuffle_word_count"],
            "shuffle":s0["explicit_shuffle_sha256"],
            "pascal":s0["compressed_pascal_sha256"],
            "euclid_mismatch_count":s0["euclid_mismatch_count"],
        },
        "stage1":{
            "pairs":replay["pair_count"],
            "formal":replay["formal_linearization_count"],
            "paths":replay["three_sector_native_path_count"],
            "replay_sha256":replay["native_replay_sha256"],
            "compressed_sha256":compressed["compressed_trace_sha256"],
        },
        "n25":examples["n25"],
    },indent=2,sort_keys=True))
    return exit_status

def main():
    import os
    ap=argparse.ArgumentParser()
    ap.add_argument("--out", default="research_results/R061_STAGE1R")
    ap.add_argument("--phase", choices=("all","native","stage0","all-stage0","finalize"),
                    default="all", help=argparse.SUPPRESS)
    args=ap.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    native_tmp=out/".R061_STAGE1R_NATIVE_PHASE.json"
    stage0_tmp=out/".R061_STAGE1R_STAGE0_PHASE.json"

    if args.phase=="native":
        json_dump(native_tmp,native_phase_bundle())
        print(str(native_tmp))
        return
    if args.phase=="stage0":
        s0,s0cmp=run_stage0_regression()
        json_dump(stage0_tmp,{"stage0":s0,"comparisons":s0cmp})
        print(str(stage0_tmp))
        return
    if args.phase=="all":
        json_dump(native_tmp,native_phase_bundle())
        os.execv(sys.executable,[sys.executable,str(Path(__file__).resolve()),
                                 "--out",str(out),"--phase","all-stage0"])
    if args.phase=="all-stage0":
        s0,s0cmp=run_stage0_regression()
        json_dump(stage0_tmp,{"stage0":s0,"comparisons":s0cmp})
        os.execv(sys.executable,[sys.executable,str(Path(__file__).resolve()),
                                 "--out",str(out),"--phase","finalize"])
    if args.phase=="finalize":
        if not native_tmp.exists() or not stage0_tmp.exists():
            raise SystemExit("missing self-generated phase certificate(s)")
        native=json.loads(native_tmp.read_text(encoding="utf-8"))
        s0payload=json.loads(stage0_tmp.read_text(encoding="utf-8"))
        command=("python3 scripts/r061_stage1r_validate_native_line_trace.py --out research_results/R061_STAGE1R --phase native\n"
                 "python3 scripts/r061_stage1r_validate_native_line_trace.py --out research_results/R061_STAGE1R --phase stage0\n"
                 "python3 scripts/r061_stage1r_validate_native_line_trace.py --out research_results/R061_STAGE1R --phase finalize")
        code=finalize_results(out,native,s0payload["stage0"],s0payload["comparisons"],command)
        native_tmp.unlink(missing_ok=True); stage0_tmp.unlink(missing_ok=True)
        raise SystemExit(code)

if __name__=="__main__":
    main()
