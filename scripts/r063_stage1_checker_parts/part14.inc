    p.add_argument("--max-n", type=int, default=DEFAULT_MAX_N)
    return p.parse_args()

def main() -> int:
    args = parse_args()
    if args.max_n < 20000:
        raise SystemExit("--max-n must be at least 20000 for Stage 1")
    outdir: Path = args.out
    outdir.mkdir(parents=True, exist_ok=True)
    result = build_outputs(outdir, args.max_n, Path(__file__))
    failed = [k for k, v in result["summary"]["acceptance_gates"].items() if not v]
    status = {
        "status": "PASS" if not failed and result["mismatches"]["mismatch_count"] == 0 else "FAIL",
        "failed_gates": failed,
        "mismatch_count": result["mismatches"]["mismatch_count"],
        "final_classification": result["summary"]["final_classification"],
        "general_regression_rows_sha256": result["summary"]["general_regression"]["rows_sha256"],
        "mandatory_discovery_snapshot_sha256": result["summary"]["mandatory_discovery_snapshot_sha256"],
    }
    print(json.dumps(status, sort_keys=True))
    return 0 if status["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
