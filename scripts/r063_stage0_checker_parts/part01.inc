    roots, _ = gaussian_norm_root_records(M)
    return tuple(sorted(roots))


@lru_cache(maxsize=None)
def gaussian_canonical_beta_pairs(M: int) -> Tuple[Pair, ...]:
    return tuple(sorted((a, b) for a, b in gaussian_norm_root_set(M) if a >= b >= 0))


def oriented_pairs(a: int, b: int) -> Tuple[Tuple[str, Pair], ...]:
    if a == b:
        return (("DIRECT", (a, b)),)
    return (("DIRECT", (a, b)), ("SWAP", (b, a)))


def discover_c2(r: int, detailed: bool = False) -> Dict[str, object]:
    branches: Dict[Pair, List[Dict[str, object]]] = defaultdict(list)
    beta_records, beta_meta = gaussian_norm_root_records(r) if detailed else ({}, {})
    betas = gaussian_canonical_beta_pairs(r)
    for m, n in betas:
        a0 = m * m - n * n
        b0 = 2 * m * n
        for orientation, pair in oriented_pairs(a0, b0):
            channel: Dict[str, object] = {
                "beta": [m, n],
                "beta_norm": r,
                "orientation": orientation,
                "alpha_before_orientation": [a0, b0],
            }
            if detailed:
                channel["beta_gaussian_factor_channels"] = beta_records.get((m, n), [])
            branches[pair].append(channel)
    return {
        "operator": "C2_UNSCALED_SQUARE_LIFT",
        "beta_norm": r,
        "beta_factorization": beta_meta if detailed else None,
        "canonical_beta_pairs": [list(x) for x in betas],
        "branches": branches,
    }


def c3_channel_is_canonical(h: int, m: int, n: int) -> bool:
    if n == 0:
        return h == 1 and m == 1
    if m <= n:
        return False
    return gcd(m, n) == 1 and ((m - n) & 1) == 1


def discover_c3(r: int, detailed: bool = False) -> Dict[str, object]:
    factors = factor_integer(r)
    divisors = divisors_from_factorization(factors)
    raw: Dict[Pair, List[Dict[str, object]]] = defaultdict(list)
    canonical: Dict[Pair, List[Dict[str, object]]] = defaultdict(list)
    divisor_routes: List[Dict[str, object]] = []

    for k in divisors:
        h = r // k
        beta_records, beta_meta = gaussian_norm_root_records(h) if detailed else ({}, {})
        beta_pairs = gaussian_canonical_beta_pairs(h)
        if detailed:
            divisor_routes.append({
                "k": k,
                "h": h,
                "identity": f"{r}={k}*{h}",
                "h_gaussian_factorization": beta_meta,
                "canonical_beta_pairs": [list(x) for x in beta_pairs],
            })
        for m, n in beta_pairs:
            a0 = k * (m * m - n * n)
            b0 = 2 * k * m * n
            is_canonical = c3_channel_is_canonical(h, m, n)
            primitive_kind = (
                "CANONICAL_AXIS" if is_canonical and n == 0 else
                "CANONICAL_PRIMITIVE_EUCLID" if is_canonical else
                "NONCANONICAL_SCALED_SQUARE_DERIVATION"
            )
            for orientation, pair in oriented_pairs(a0, b0):
                channel: Dict[str, object] = {
                    "k": k,
                    "h": h,
                    "m": m,
                    "n": n,
                    "identity": f"{r}={k}*({m}^2+{n}^2)",
                    "orientation": orientation,
                    "alpha_before_orientation": [a0, b0],
                    "gcd_m_n": gcd(m, n),
                    "opposite_parity": bool((m - n) & 1),
                    "canonical": is_canonical,
                    "classification": primitive_kind,
                }
                if detailed:
                    channel["beta_gaussian_factor_channels"] = beta_records.get((m, n), [])
                raw[pair].append(channel)
                if is_canonical:
                    canonical[pair].append(channel)

    return {
        "operator": "C3_SCALED_SQUARE_LIFT",
        "scalar_root_factorization": factor_rows(r),
        "divisors": list(divisors),
        "divisor_routes": divisor_routes if detailed else None,
        "raw_branches": raw,
        "canonical_branches": canonical,
        "canonical_rule": (
            "axis: h=1,m=1,n=0; nondegenerate: m>n>0, gcd(m,n)=1, "
            "opposite parity; orientation retains ordered components"
        ),
    }


def discover_c4(N: int, detailed: bool = False) -> Dict[str, object]:
    records, metadata = gaussian_norm_root_records(N)
    branches: Dict[Pair, List[Dict[str, object]]] = defaultdict(list)
    for z, channels in sorted(records.items()):
        a, b = z
        if a >= 0 and b >= 0:
            branches[z].extend(channels if detailed else [{}])
    return {
        "operator": "C4_GAUSSIAN_FACTORIZATION_FIRST",
        "norm_factorization": metadata if detailed else None,
        "branches": branches,
    }


def c2_rootset(r: int) -> Tuple[Pair, ...]:
    return tuple(sorted(discover_c2(r, detailed=False)["branches"].keys()))


def c3_rootset(r: int) -> Tuple[Pair, ...]:
    return tuple(sorted(discover_c3(r, detailed=False)["canonical_branches"].keys()))


def c4_rootset(N: int) -> Tuple[Pair, ...]:
    return tuple(sorted(discover_c4(N, detailed=False)["branches"].keys()))


def exact_scalar_root(N: int) -> int:
    if N < 0:
        raise ValueError("negative N")
    r = isqrt(N)
    if r * r != N:
        raise ValueError("Stage 0 path-valued square-root discovery requires square N")
    return r


def attach_channel_ids(prefix: str, branches: MutableMapping[Pair, List[Dict[str, object]]]) -> None:
    counter = 0
    for pair in sorted(branches):
        channels = branches[pair]
        channels.sort(key=canonical_json_bytes)
        for channel in channels:
            channel["channel_id"] = f"{prefix}-{counter:04d}"
            counter += 1


def discover_from_scalar_root(N: int) -> Dict[str, object]:
    """DISCOVERY PHASE.  No brute target-norm enumeration is reachable here."""
    r = exact_scalar_root(N)
    c2 = discover_c2(r, detailed=True)
    c3 = discover_c3(r, detailed=True)
    c4 = discover_c4(N, detailed=True)

    attach_channel_ids("C2", c2["branches"])
    attach_channel_ids("C3R", c3["raw_branches"])
    attach_channel_ids("C3C", c3["canonical_branches"])
    attach_channel_ids("C4", c4["branches"])

    c3_roots = tuple(sorted(c3["canonical_branches"].keys()))
    c4_roots = tuple(sorted(c4["branches"].keys()))
    if c3_roots != c4_roots:
        raise AssertionError("discovery-only C3/C4 disagreement")

    discovery = {
        "schema": "R063_STAGE0_DISCOVERY_PHASE_FROZEN_V1",
        "task": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "taskbook_source": TASKBOOK_SOURCE,
        "owner_branch": OWNER_BRANCH,
        "phase": "DISCOVERY_PHASE_ONLY_NO_BRUTE_TARGET_FIBER",
        "input": {"N": N},
        "scalar_root": {
            "r": r,
            "certificate": f"{r}^2={N}",
            "factorization_r": factor_rows(r),
            "factorization_N": factor_rows(N),
        },
        "component_algebra": {
            "carrier": "Z[J]/(J^2+1)",
            "norm": "N_E(a+bJ)=a^2+b^2",
            "typing_boundary": "sector-local algebraic carrier only; no carrier vector identity promoted to native geometry",
        },
        "C0": {
            "operator": "ORDINARY_SCALAR_SQRT",
            "output": r,
            "retains": ["exact scalar radius/root", "squared native norm magnitude"],
            "loses": ["component-root identity", "component ordering", "algebraic derivation provenance", "native trace identity", "native path multiplicity"],
        },
        "C2": c2,
        "C3": c3,
        "C4": c4,
        "generated_component_roots": [list(x) for x in c3_roots],
        "discovery_invariant": "C3_CANONICAL_ROOT_SET_EQUALS_C4_FACTORIZATION_ROOT_SET_BEFORE_BRUTE_VERIFICATION",
    }
    return discovery


def brute_norm_fiber(N: int) -> Tuple[Pair, ...]:
    """BRUTE VERIFICATION PHASE ONLY."""
    out: List[Pair] = []
    for a in range(isqrt(N) + 1):
        b2 = N - a * a
        b = isqrt(b2)
        if b * b == b2:
            out.append((a, b))
    return tuple(out)


def verify_against_norm_fiber(N: int, discovered: Mapping[str, object]) -> Dict[str, object]:
    """BRUTE VERIFICATION PHASE.  Called only after discovery is frozen/hashed."""
    brute = brute_norm_fiber(N)
    brute_set = set(brute)
    candidate_sets = {
        "C2": set(discovered["C2"]["branches"].keys()),
        "C3": set(discovered["C3"]["canonical_branches"].keys()),
        "C4": set(discovered["C4"]["branches"].keys()),
    }
    comparisons: Dict[str, object] = {}
    for name, got in candidate_sets.items():
        comparisons[name] = {
            "generated": [list(x) for x in sorted(got)],
            "missing": [list(x) for x in sorted(brute_set - got)],
            "extra": [list(x) for x in sorted(got - brute_set)],
            "exact_set_equality": got == brute_set,
        }
    return {
        "phase": "BRUTE_VERIFICATION_AFTER_DISCOVERY_FREEZE",
        "N": N,
        "D_N": [list(x) for x in brute],
        "D_N_sha256": sha256_obj([list(x) for x in brute]),
        "comparisons": comparisons,
    }


def lex_rank(n: int, k: int, positions: Sequence[int]) -> int:
    if k == 0:
        if positions:
            raise ValueError("k=0 requires empty positions")
        return 0
    if len(positions) != k:
        raise ValueError("wrong combination size")
    rank = 0
    prev = 0
    for i, x in enumerate(positions):
        if x <= prev or x > n:
            raise ValueError("invalid combination")
        remaining = k - i - 1
        for y in range(prev + 1, x):
            rank += comb(n - y, remaining)
        prev = x
