# R063 Stage 1 — General Gaussian root theorem

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
