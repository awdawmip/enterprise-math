    discovery_file = compact_discovery_artifact(discovery_obj, discovery_sha)
    write_json(outdir / "R063_STAGE1_DISCOVERY_PHASE_FROZEN.json", discovery_file)

    # BRUTE VERIFICATION PHASE starts only after discovery_file exists and is hashed.
    mandatory_ver = run_mandatory_verification(discovery_obj)
    anti = source_anti_hardcode_scan(script_path, discovery_obj)
    general = run_general_regression(max_n)
    sparse = run_sparse_suite()
    mult = multiplicative_audit()
    square = square_scope_regression()
    nonsquare = nonsquare_certificate(discovery_obj, mandatory_ver)
    root_count = root_count_orbit_certificate(discovery_obj, max_n)

    mismatches: List[Dict[str, object]] = []
    if mandatory_ver["mismatch_count"]:
        mismatches.append({"scope": "MANDATORY", "count": mandatory_ver["mismatch_count"]})
    if general["rootset_mismatch_count"] or general["support_mismatch_count"] or general["count_formula_mismatch_count"] or general["path_cardinality_mismatch_count"]:
        mismatches.append({"scope": "GENERAL", "smallest": general["smallest_mismatch"]})
    if sparse["mismatch_count"]:
        mismatches.append({"scope": "SPARSE", "smallest": sparse["smallest_mismatch"]})
    if not mult["all_signed_multiplication_maps_surjective"]:
        mismatches.append({"scope": "MULTIPLICATIVE_SURJECTIVITY"})
    if not square["pass"]:
        mismatches.append({"scope": "STAGE0_SQUARE_REGRESSION"})
    if not anti["pass"]:
        mismatches.append({"scope": "SOURCE_ANTI_HARDCODE", "audit": anti})

    mandatory_by_n = {d["N"]: d for d in discovery_obj["witnesses"]}
    positive_ok = all(mandatory_by_n[N]["support"] for N in MANDATORY_POSITIVE)
    negative_ok = all(not mandatory_by_n[N]["support"] for N in MANDATORY_NEGATIVE)
    n13 = next(x for x in nonsquare["mandatory_rows"] if x["N"] == 13)
    irrational_discrete = (not radical_length(13)["is_integer_length"] and bool(n13["ordered_nonnegative_component_roots"]))
    all_gaussian_channel_multiplicity_one = all(
        rr["gaussian_derivation_channel_count"] == 1
        for d in discovery_obj["witnesses"] for rr in d["root_records"]
    )
    mult_sep = mult["multiplicity_separation_witness"] is not None

    gates = {
        "DISCOVERY_PHASE_INDEPENDENT_OF_BRUTE_TARGET_FIBER": anti["pass"],
        "SUM_OF_TWO_SQUARES_SUPPORT_CLASSIFIED_FROM_FACTORIZATION": positive_ok and negative_ok and general["support_mismatch_count"] == 0,
        "GENERAL_GAUSSIAN_ROOT_GENERATOR_EXACT_OR_FALSIFIED": general["rootset_mismatch_count"] == 0 and sparse["mismatch_count"] == 0,
        "NO_EXTRA_COMPONENT_ROOTS": general["rootset_mismatch_count"] == 0 and sparse["mismatch_count"] == 0,
        "NO_MISSING_COMPONENT_ROOTS": general["rootset_mismatch_count"] == 0 and sparse["mismatch_count"] == 0,
        "ROOT_COUNT_FACTOR_CERTIFICATE_CLASSIFIED": general["count_formula_mismatch_count"] == 0,
        "NONSQUARE_NATIVE_TRACE_PATHIFICATION_EXACT": general["path_cardinality_mismatch_count"] == 0 and positive_ok,
        "IRRATIONAL_NATIVE_LENGTH_WITH_DISCRETE_PATH_FIBER_CLASSIFIED": irrational_discrete,
        "ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED": all_gaussian_channel_multiplicity_one and mult_sep,
        "MULTIPLICATIVE_ROOT_PROVENANCE_CLASSIFIED": mult["all_signed_multiplication_maps_surjective"] and mult_sep,
