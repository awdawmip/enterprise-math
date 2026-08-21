        },
        "witness_rows": rows,
        "regression_scope": [1, max_n],
    }

def markdown_support_theorem() -> str:
    return """# R063 Stage 1 — Sum-of-two-squares support theorem

For a positive integer `N`, factor it in `Z` as

`N = 2^e2 * product p_i^e_i * product q_j^f_j`

with `p_i == 1 (mod 4)` and `q_j == 3 (mod 4)`.

Then the integer-addressed native component-root fiber is nonempty **iff** every `f_j` is even.

The discovery gate uses only this factorization.  If an inert prime `q == 3 (mod 4)` occurs to odd exponent, no Gaussian integer can have norm `N`: from `q | a^2+b^2`, the fact that `-1` is not a quadratic residue mod `q` forces `q|a,b`, removing `q^2` at a time.  Hence the norm valuation of every inert prime is even.

Conversely, when all inert exponents are even, the Gaussian construction exists: inert primes contribute fixed integer factors, `2` contributes `(1+J)^e2`, split primes contribute freely allocated conjugate exponents, and a unit completes the Gaussian factorization.

Therefore

`GRoot_E(N) != empty <=> every q == 3 mod 4 has even exponent`.

This is a discovery theorem, not a brute search criterion.
"""

def markdown_gaussian_theorem() -> str:
    return """# R063 Stage 1 — General Gaussian root theorem

Assume the factorization support criterion holds.  In `Z[J]`:

1. `2` is ramified through `1+J`;
2. every inert `q == 3 mod 4` contributes the fixed integer Gaussian factor `q^(f_q/2)`;
3. every split prime `p == 1 mod 4` is written canonically as `pi_p conjugate(pi_p)`;
4. for norm exponent `e_p`, choose every allocation `t=0..e_p` between `pi_p^t` and `conjugate(pi_p)^(e_p-t)`;
5. multiply by the four units.

Unique factorization proves **no extras** because every constructed Gaussian integer has norm `N`, and **completeness** because every Gaussian integer of norm `N` has exactly this prime-exponent structure.

Filtering the complete signed Gaussian root set to `a>=0,b>=0` gives the complete ordered nonnegative native component-root fiber.

Hence the factorization-first operator is exact on every positive integer `N`, returning an empty fiber exactly off sum-of-two-squares support.

For every returned `(a,b)`, the frozen R061 trace is `T_{a,b}^{(ij)}` and

`Lambda(a,b)=[u^a v^b](uX_i+vX_j)^(a+b)`,

with exact cardinality `binom(a+b,a)`.  The native length is the exact radical `sqrt(N)` (possibly irrational); `a+b` is only path-letter count.
"""

def markdown_multiplicative(audit: Mapping[str, object]) -> str:
    witness = audit["multiplicity_separation_witness"]
    return f"""# R063 Stage 1 — Multiplicative derivation audit

The Gaussian factorization layer has a compositional structure not visible in the scalar norm alone.

For representable `A,B`, signed Gaussian root multiplication is surjective onto the signed root fiber of `AB`.  Prime-wise, every split-prime exponent allocation for `AB` can be decomposed into valid allocations for `A` and `B`; ramified and inert contributions are fixed, while Gaussian units distribute across the factors.

The deterministic audit covers every unordered pair from `{list(MULT_BASE)}` and all signed root multiplication channels.  All `{audit['pair_audit_count']}` product audits are surjective: `{audit['all_signed_multiplication_maps_surjective']}`.

