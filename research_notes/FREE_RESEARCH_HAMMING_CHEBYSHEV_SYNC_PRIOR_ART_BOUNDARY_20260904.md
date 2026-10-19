# Hamming–Chebyshev synchronization prior-art boundary

Status: `PRIOR_ART_AUDIT / FREE_RESEARCH / NOVELTY_NOT_CLAIMED`
Date: `2026-09-04`

## Classical/externally existing ingredients

- Farhi's binomial-row LCM identity:
  `lcm(choose(m,0),...,choose(m,m)) = lcm(1,...,m+1)/(m+1)`.
- Hong's observation that this identity is equivalent to an earlier identity of Nair.
- Kummer's carry interpretation of prime valuations of binomial coefficients.
- Chebyshev's `psi = log lcm(1,...,N)` identity and elementary binomial bounds.
- Möbius inversion, Legendre's factorial valuation formula, and Selberg's convolution identity.

Pinned mathlib already formalizes substantial supporting infrastructure: `Nat.lcmUpto`, `factorization_lcmUpto`, `Chebyshev.psi_eq_log_lcmUpto`, `choose_dvd_lcmUpto`, Pascal-row sums, and Kummer/Legendre factorization formulas.

## Project-specific content of the current bridge

No novelty is claimed for the classical equalities themselves. The project-specific research content is the typed identification of these equalities with the already-constructed #1159 finite Hamming/Krawtchouk spectral carrier:

1. the row entries are literal shell-zero eigenmode amplitudes `g_(m,k)(0)`;
2. their LCM is therefore a finite spectral synchronization clock;
3. the prime-direction identity `log_p N = v_p(N) + max_k v_p(g_(N-1,k)(0))` is interpreted as top-state winding plus maximal branch-recoalescence carry depth;
4. the normalized clock's discrete jump is the von Mangoldt flux;
5. the Möbius factorial product is interpreted as signed renormalization of opposite-corner Hamming path-fiber volumes;
6. the Selberg quadratic convolution is retyped as one/two-winding positive energy.

Any external novelty claim for those carrier interpretations remains unverified.
