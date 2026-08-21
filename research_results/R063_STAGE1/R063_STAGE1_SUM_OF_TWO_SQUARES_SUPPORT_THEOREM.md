# R063 Stage 1 — Sum-of-two-squares support theorem

For a positive integer `N`, factor it in `Z` as

`N = 2^e2 * product p_i^e_i * product q_j^f_j`

with `p_i == 1 (mod 4)` and `q_j == 3 (mod 4)`.

Then the integer-addressed native component-root fiber is nonempty **iff** every `f_j` is even.

The discovery gate uses only this factorization.  If an inert prime `q == 3 (mod 4)` occurs to odd exponent, no Gaussian integer can have norm `N`: from `q | a^2+b^2`, the fact that `-1` is not a quadratic residue mod `q` forces `q|a,b`, removing `q^2` at a time.  Hence the norm valuation of every inert prime is even.

Conversely, when all inert exponents are even, the Gaussian construction exists: inert primes contribute fixed integer factors, `2` contributes `(1+J)^e2`, split primes contribute freely allocated conjugate exponents, and a unit completes the Gaussian factorization.

Therefore

`GRoot_E(N) != empty <=> every q == 3 mod 4 has even exponent`.

This is a discovery theorem, not a brute search criterion.
