# Audit of the preceding consecutive-cover proof

Scope: author collaboration on the v11 proof at
`research_notes/portable_direct/riesel_seven_cover_20261124/finite/proof.md`,
current observed source `a88e3e001275269cae93c40d77e6984b1ef2970f`.
The local candidate is `/workspace/scratch/0814b15dd923/v11_refinement_work/proof.md`.

## Audit conclusion

No mathematical defect was found in Theorems A/B or the bound
`(27/64)*2^b` at their stated scopes. The main universal obligations close as
follows:

1. The alternating dyadic-ternary covers include k=1 correctly; the two
   modulus-three rows use distinct explicit order-108 primes.
2. Every dyadic private cell avoids both final rows even at j=k. The lifted
   cells retain privacy because their common period is coprime to 35.
3. The step k to k+1 retains the same *literal* phase at every common prime.
   Its removed/added orders are precisely `54*2^k,72*2^k,216*2^k`, including
   the special first step. This proves stabilization against any finite set
   of observed primes once the minimum order exceeds B_N.
4. Fixing root lifts modulo observed prime powers is compatible with E:
   dictionary primes are completely removed from E; every observed absent
   prime has root residue zero. This handles arbitrary finite powers, not
   only squarefree observations.
5. The common-factor argument for private terms proves both exact minima.
   Irredundancy alone is not used as a substitute for global minimality.
6. The old differences 60,36,72 preserve all inactive R1/R2 coordinates,
   while the initial k=0 member is correctly restricted to R1.
7. The strict inequality defining j_N gives the displayed observer bound
   with the correct ranges b>=7 in R1 and b>=8 in R2.

The new construction in `permanent_ternary_proof.md` is an improvement rather
than a correction. It preserves both ternary side rows and raises the minimum
changed order to `72*2^k`, giving `(9/16)*2^b` under the same ranges. The older
43-coordinate observation and its residue are unchanged historical results;
the new construction selects a different stabilized residue when applied to
that modulus, so it does not settle whether cost eight occurs in the old
43-coordinate fiber.

Checks and proof review here are shared-context collaboration. No independent
project Review, formal acceptance, new native BRC execution, or source mutation
is claimed.
