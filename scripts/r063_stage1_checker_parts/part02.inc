    allocations = product(*ranges) if ranges else [()]
    roots: Dict[Gaussian, List[Dict[str, object]]] = defaultdict(list)
    for alloc in allocations:
        z = base
        alloc_rows: List[Dict[str, object]] = []
        for (p, e, pi), t in zip(split, alloc):
            z = gmul(z, gpow(pi, t))
            z = gmul(z, gpow(gconj(pi), e-t))
            if detailed:
                alloc_rows.append({"prime": p, "pi_exponent": t, "conjugate_exponent": e-t})
        for unit_name, unit in UNITS:
            w = gmul(unit, z)
            if gnorm(w) != N:
                raise ArithmeticError("Gaussian norm construction error")
            channel = {
                "unit": unit_name,
                "split_prime_allocations": alloc_rows,
                "pre_unit_value": list(z),
                "value": list(w),
            } if detailed else {}
            roots[w].append(channel)
    return dict(roots), meta

def r2_from_factorization(N: int) -> int:
    factors = factor_integer(N)
    if not support_from_factors(factors):
        return 0
    count = 4
    for p, e in factors.items():
        if p % 4 == 1:
            count *= (e+1)
    return count

def is_square(N: int) -> bool:
    r = isqrt(N)
    return r*r == N

def is_equal_component_square(N: int) -> bool:
    return N % 2 == 0 and is_square(N//2)

def factor_count_certificate(N: int) -> Dict[str, object]:
    r2 = r2_from_factorization(N)
    axis = is_square(N)
    equal = is_equal_component_square(N)
    ordered_nonnegative = (r2//4 + (1 if axis else 0)) if r2 else 0
    unordered_shapes = ((ordered_nonnegative + (1 if equal else 0))//2) if ordered_nonnegative else 0
    return {
        "r2_signed_ordered": r2,
        "axis_shape_present": axis,
        "equal_component_shape_present": equal,
        "ordered_nonnegative_component_root_count_formula": ordered_nonnegative,
        "unordered_component_shape_count_formula": unordered_shapes,
        "r2_formula": "0 if inert odd exponent; otherwise 4*product_{p=1 mod4}(e_p+1)",
        "ordered_nonnegative_formula": "r2(N)/4 + 1_{N is a square}",
        "unordered_shape_formula": "(ordered_nonnegative + 1_{N=2*s^2})/2",
    }

def radical_length(N: int) -> Dict[str, object]:
    factors = factor_integer(N)
    outside = 1
    inside = 1
    for p, e in sorted(factors.items()):
        outside *= p ** (e//2)
        if e % 2:
            inside *= p
    if inside == 1:
        expr = str(outside)
    elif outside == 1:
        expr = f"sqrt({inside})"
    else:
        expr = f"{outside}*sqrt({inside})"
    return {
        "squared_native_length": N,
        "is_integer_length": inside == 1,
        "radical_outside": outside,
        "squarefree_radicand": inside,
        "exact_expression": expr,
    }

def lex_rank(n: int, k: int, positions: Sequence[int]) -> int:
    if k == 0:
        if positions:
            raise ValueError("k=0 with nonempty positions")
        return 0
    if len(positions) != k:
        raise ValueError("wrong combination size")
    rank = 0
    prev = 0
    for i, x in enumerate(positions):
        remaining = k-i-1
        for y in range(prev+1, x):
            rank += comb(n-y, remaining)
        prev = x
    return rank

def lex_unrank(n: int, k: int, rank: int) -> List[int]:
    total = comb(n, k)
    if not 0 <= rank < total:
        raise ValueError("rank out of range")
