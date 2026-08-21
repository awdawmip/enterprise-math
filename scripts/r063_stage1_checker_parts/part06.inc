                "support_matches": row["verification"]["support_matches"],
            }
            for row in mandatory_ver["rows"]
        ],
    }

def source_anti_hardcode_scan(script_path: Path, discovery: Mapping[str, object]) -> Dict[str, object]:
    part_dir = script_path.with_name("r063_stage1_checker_parts")
    if part_dir.is_dir():
        source = script_path.read_text(encoding="utf-8") + "".join(
            p.read_text(encoding="utf-8") for p in sorted(part_dir.glob("part*.inc"))
        )
    else:
        source = script_path.read_text(encoding="utf-8")
    scan_surface = source[:source.index("def source_anti_hardcode_scan")]
    hits: List[str] = []
    for row in discovery["witnesses"]:
        if row["N"] not in set(MANDATORY_POSITIVE + MANDATORY_NEGATIVE):
            continue
        for a, b in (tuple(x) for x in row["ordered_nonnegative_component_roots"]):
            if a == 0 or b == 0:
                continue
            # (1,1) is an unavoidable structural literal for the ramified Gaussian prime 1+J,
            # not a seeded target root.  Audit all other nontrivial mandatory roots literally.
            if (a, b) == (1, 1):
                continue
            for pattern in (f"({a}, {b})", f"({a},{b})", f"[{a}, {b}]", f"[{a},{b}]"):
                if pattern in scan_surface:
                    hits.append(f"N={row['N']}:{pattern}")
    discovery_segment = source[source.index("def discover_general"):source.index("def discovery_freeze_payload")]
    forbidden = [x for x in ("brute_norm_fiber(", "a*a+b*b==", "a^2+b^2") if x in discovery_segment]
    suspicious_names = [x for x in ("EXPECTED_ROOT", "MANDATORY_ROOTS_BY_N", "ROOT_TABLE", "BRUTE_ROOT_TABLE", "KNOWN_ROOTS") if x in scan_surface]
    return {
        "mandatory_nontrivial_root_literal_hits": sorted(set(hits)),
        "allowed_structural_literal_exceptions": ["(1,1) only as the ramified Gaussian prime 1+J; never as a target-root table entry"],
        "suspicious_root_table_identifier_hits": suspicious_names,
        "discovery_function_forbidden_scan_hits": forbidden,
        "pass": not hits and not forbidden and not suspicious_names,
    }

def run_mandatory_verification(discovery_obj: Mapping[str, object]) -> Dict[str, object]:
    rows = []
    for d in discovery_obj["witnesses"]:
        rows.append({
            "N": d["N"],
            "discovery_snapshot_sha256": sha256_obj(discovery_freeze_payload(d)),
            "verification": verify_one(d["N"], d),
        })
    return {"rows": rows, "mismatch_count": sum(not x["verification"]["exact_set_equality"] for x in rows)}

def run_general_regression(max_n: int) -> Dict[str, object]:
    h = hashlib.sha256()
    mismatches: List[Dict[str, object]] = []
    support_mismatches = count_mismatches = path_mismatches = 0
    representable = 0
    total_roots = 0
    for N in range(1, max_n+1):
        d = discover_general(N, detailed=False)
        freeze_sha = sha256_obj(discovery_freeze_payload(d))
        # Phase barrier: brute starts only after d and freeze_sha exist.
        brute = brute_norm_fiber(N)
        got = tuple(tuple(x) for x in d["ordered_nonnegative_component_roots"])
        if got:
            representable += 1
            total_roots += len(got)
        if got != brute:
            mismatches.append({
                "N": N, "factorization": d["factorization"],
