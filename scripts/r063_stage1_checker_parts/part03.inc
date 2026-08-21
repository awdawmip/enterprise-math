    if k == 0:
        return []
    out: List[int] = []
    prev = 0
    rem = rank
    for i in range(k):
        remaining = k-i-1
        x = prev+1
        while x <= n:
            block = comb(n-x, remaining)
            if rem < block:
                out.append(x)
                prev = x
                break
            rem -= block
            x += 1
        else:
            raise ArithmeticError("unrank failure")
    return out

def bigint_sha256(value: int) -> str:
    if value < 0:
        raise ValueError
    b = value.to_bytes(max(1, (value.bit_length()+7)//8), "big")
    return hashlib.sha256(b).hexdigest()

def path_certificate(a: int, b: int, include_decimal: bool = True) -> Dict[str, object]:
    n = a+b
    card = comb(n, a)
    out = {
        "components": [a, b],
        "compressed_polynomial": f"[u^{a} v^{b}](uX_i+vX_j)^{n}",
        "path_letter_count": n,
        "path_letter_count_semantics": "NOT_NATIVE_LENGTH",
        "cardinality_bit_length": card.bit_length(),
        "cardinality_sha256_unsigned_big_endian": bigint_sha256(card),
    }
    if include_decimal:
        ranks = sorted(set((0, card//2, card-1)))
        samples = []
        for rank in ranks:
            pos = lex_unrank(n, a, rank)
            back = lex_rank(n, a, pos)
            if back != rank:
                raise ArithmeticError("combinadic roundtrip mismatch")
            samples.append({"rank": rank, "X_i_positions_1_based": pos, "rank_roundtrip": back})
        out["first_positions"] = lex_unrank(n, a, 0)
        out["last_positions"] = lex_unrank(n, a, card-1)
        out["rank_unrank_samples"] = samples
        out["exact_path_cardinality"] = card
    return out

def discover_general(N: int, detailed: bool = False) -> Dict[str, object]:
    """DISCOVERY PHASE ONLY. Uses integer/Gaussian factorization; never brute target scanning."""
    if N < 1:
        raise ValueError("N must be positive")
    signed_channels, meta = gaussian_signed_root_channels(N, detailed=detailed)
    signed_roots = tuple(sorted(signed_channels))
    roots = tuple(sorted(z for z in signed_roots if z[0] >= 0 and z[1] >= 0))
    shapes = tuple(sorted({tuple(sorted(z)) for z in roots}))
    count_cert = factor_count_certificate(N)
    if len(signed_roots) != count_cert["r2_signed_ordered"]:
        raise AssertionError("factor root count mismatch inside discovery")
    if len(roots) != count_cert["ordered_nonnegative_component_root_count_formula"]:
        raise AssertionError("ordered nonnegative count mismatch inside discovery")
    if len(shapes) != count_cert["unordered_component_shape_count_formula"]:
        raise AssertionError("shape count mismatch inside discovery")
    root_records: List[Dict[str, object]] = []
    for a, b in roots:
        channels = signed_channels[(a, b)]
        root_records.append({
            "components": [a, b],
            "alpha": f"{a}+{b}J",
            "norm_certificate": a*a+b*b,
            "gaussian_derivation_channel_count": len(channels),
            "gaussian_derivation_channels": channels if detailed else None,
            "trace_id": f"T_{{{a},{b}}}^(ij)",
            "native_length": radical_length(N),
            "path": path_certificate(a, b, include_decimal=detailed),
        })
    return {
        "schema": "R063_STAGE1_GENERAL_DISCOVERY_V1",
        "phase": "DISCOVERY_ONLY_BEFORE_BRUTE",
