# Jacobi torus selector: author self-review

Status: **AUTHOR_SELF_REVIEW_PASS / PURE_SYMBOLIC / REUSE_IDENTIFIED / NOT_NEWLY_EXECUTED / NOT_ADMITTED**.

This review binds JACOBI_TORUS_SELECTOR.md at SHA-256 **30fc0de14df7eef7f43c30838fbe1dd47c60db85982ac5d92bfc0c863d2cdf2f**. It is the author's own symbolic check, not independent admission. No scientific module, Jacobi primitive, sample generator or native observer was executed.

## Domain and pointwise guarantee

The domain is explicitly N=pq for distinct odd primes p,q congruent to 3 modulo 4. The factors appear only in the proof. The program may use the filter without knowing them, but the theorem's domain promise cannot be inferred from N congruent to 1 modulo 4 or from a Jacobi value alone. Both-factor-1-mod-4 inputs and repeated-prime inputs are outside this guarantee.

For a regular discriminant, Jacobi -1 forces opposite local Legendre symbols and hence opposite torus types. At each split Blum component, the group order is twice an odd integer. An even power-of-two exponent has gcd 2 with that order: its positive solutions are only the two excluded eigenvalues, while its negative congruence has no solutions. This proves the split obstruction pointwise.

Only the nonsplit prime can divide either signed main return divisor. Since N is squarefree with exactly two factors, that divisor is 1 or that prime, never N. For a fixed accepted k, the pair of positive/negative main divisors has only the patterns (1,1), (r,1), (1,r), where r is the nonsplit prime. The proof excludes a simultaneous signed hit at that one component in odd characteristic. None of these facts guarantee a hit.

## Probability normalization and boundaries

The split and nonsplit trace counts S_r=(r-3)/2 and U_r=(r-1)/2 normalize trace parameters rather than eigenvalues. Conditional uniformity within the admitted CRT product is correctly stated; further conditioning on opposite type produces the two orientations S_p U_q and U_p S_q.

Expanding

    Z=(p-3)(q-1)+(p-1)(q-3)
      =2*((p-2)*(q-2)-1)

gives the acceptance ratio (R-1)/(2R), R=(p-2)(q-2). It does not give equal orientation weights unless the displayed counts happen to agree. The unconditional all-residue acceptance is D/(pq), with D=Z/4, and possible setup factors remain outside this conditional-return experiment.

If p=3, S_p=0, U_p=1 and distinct q>3 has S_q>0. Thus exactly one orientation survives; no division by a zero orientation count occurs. The symmetric q=3 case is covered. The source never extends this argument to p=q=3.

In the norm-one group, division by U_r cancels the inverse-pair factor 1/2. For even E, both exceptional eigenvalues are removed from positive roots and neither is a negative root. The signed probabilities are therefore (d-2)/(r-1) and h/(r-1), respectively. Their union equals (gcd(2E,r+1)-2)/(r-1), not a denominator r+1 or the full-family r-2.

Putting r+1=2^t*m with m odd gives the stated piecewise negative probability and the union cap (2^t-2)/(r-1). Weighting rho_q by p-split/q-nonsplit and rho_p by the reverse orientation is correct. The r=3 small case follows from t=2 and has union rate one. None of these calculations supplies a free conditional sampler or estimates a new experiment.

## Costs, second-clock boundary and reusable source

E+2 is generally not a power of two. Its odd factors can admit a split-torus return, so the scalar translated union may saturate across two components. Only the marked main-E branch retains the pointwise guarantee. The note explicitly forbids transferring no-saturation to the second clock or to an elliptic discriminant. Both-sign correlations and adaptive schedules remain separate obligations.

The entire 12678-byte typed_jacobi.py source was read at SHA-256 ce7168c8724d1fff216b903f09cdaf7fe16c8074c48488f7b26fb80584060402. The entire 11931-byte JACOBI_FINAL_BIT_PROOF.md was read at SHA-256 fc51f6feb6134b2d1443efd9751f26621478a25512cc2d3784ae63045c5c7161. The source's generic typed_jacobi_trace accepts an integer numerator and odd positive denominator, binds actual Arithmetic.divide records, and retains sign/shift wiring and the terminal gcd. Reusing that terminal gcd for regularity is legitimate only with its complete bound certificate and linked typed numerator producer.

The O(n^3) conservative digit bound is the frozen proof's canonical-input Jacobi bound. It is not a new measured selector cost. The source also contains square-schedule and final-bit functions with additional instrument hypotheses; these are explicitly excluded from this selector's reuse. Importing or verifying those other interfaces would be a different scientific action.

A future implementation must count parameter generation, Delta construction, Jacobi filtering and rejected candidates, actual trace propagation, chosen readouts, exact-factor division, any replay validation, binding and retained evidence. No source-level shortcut makes these interfaces free. The note correctly keeps unexpected saturated outcomes even when the theorem predicts their absence under its domain promise.

The proof is a useful factor-blind sign-conditioning component, with a precise failure event and conditional law. The odd-order obstruction and total-cost selection problem remain unsolved. There is no new native execution, global factoring advantage or Shor closure claimed. A separate peer/parent review should accompany any later scientific use or publication.

Global-Knowledge-Sync: author actual canonical read lease main@4ae9f3f / GLOBAL_KNOWLEDGE_V1.

