# OAI7-142-C: auxiliary-prime numerical-E bit-cost ledger
Date: 2026-11-21. Task RS-OAI7-142-C-20261007-6F2A81; source preliminary at openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a / preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/.
Evidence mode: arithmetic audit of source formulas; NOT_REVIEWED, not an admission of the preprint, its companion Hecke theorem, or the unverified implementation lemmas.

## Input and declared dependent parameters
Binary prime p, dense F_p polynomial degree n, L=ceil(log_2 p), N0=(n+1)L, B=20+(n+1)(L+1), q prime <= n. In the large-p branch p>B^200000, the algebraic reduction takes auxiliary primes ell_q that pass congruence and non-qth-power tests. E=max(2,max ell_q) is a **numeric** bound, not log E.

The manuscript's Section 09 derives:
  Indexed bit cost: O(B^201000 + B^41 E^10).
  After conservative quadratic addressing overhead: O(B^500000 + B^100 E^20).
These are conditional on the mathematical correctness of the underlying algebraic procedures and size lemmas in Sections 02–08. The section explicitly accounts for the cyclotomic algebra dimension ell-1 and states each field table entry at O(ell^10 B^40), with at most B entries.

## Exact exponent arithmetic
Section 10, using its separately cited external Hecke zero-free theorem, claims ell_q <= c0 B^20000000 with an *absolute* c0. Therefore E<=max(2,c0 B^20000000) <= C B^20000000 for absolute C>=max(2,c0), since B>=20. Consequently:
   B^100 E^20 <= C^20 B^(100+20*20000000)=C^20 B^400000100.
The other term B^500000 is dominated for B>=1, yielding O(B^400000100).
For all n>=0 and L>=1, 1<=N0 and B=20+(n+1)(L+1) <=20+2N0<=22N0. Hence
   O(B^400000100) = O(N0^400000100) subset O(N0^10^12).
The unknown magnitude of the absolute constant affects the multiplicative constant but is not a gap in asymptotic polynomiality; upward search does not need to know c0 in advance.

## Source-dependent cost branches and questions
- Small p<=B^200000: source charges O(B^201000) sequential bits; no ell table needed.
- Large p: scalar instructions O(B^40), one NormSolve O(B^2000), one splitting call O(B^20000); <=B^4 splitting calls, so O(B^20004), with table O(B^41 E^10).
- Sequential indexed-address overhead is bounded by squaring whole indexed-work budget; this is intentionally loose and yields the stated B^500000 + B^100 E^20.
- Trial division and modular-power tests of each ell have bit cost involving numeric ell; the O(ell^10 B^40) table allotment dominates the naive upward search. Treating these calls as polynomial only in log ell would be a modeling error.
- The analytic input is an explicitly stated **uniform fixed-width zero-free strip** for all involved Hecke characters, independent of conductor and height. That external theorem is not proved in the cited factoring paper. Without an independently valid such theorem or alternative polynomial bound E=poly(B), the unconditional polynomial-time claim is unresolved.
- Additional independent auditing should focus on the source's claimed B^2000 NormSolve and B^20000 split bounds, including large divisor circuits, interpolating grids, and whether a hidden representation expands in numeric p or E. The formulas above are an internally correct exponent *accounting reduction*, not an audit of each implementation lemma.

No integer factorization or primitive-root oracle introduced in this ledger. No change to P000 or research ownership; no formal CLAIM, Result or independent Driver mathematical review is asserted here.
