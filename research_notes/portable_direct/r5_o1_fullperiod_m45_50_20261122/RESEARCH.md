# R5 scalar period: six additional maximal-period thresholds (45–50)

Date: 2026-11-22. Status: **AUTHOR_EXACT_FINITE_COMPUTATION / CONDITIONAL_ON_REPRODUCIBLE_INTEGER_ALGORITHM / NOT_REVIEWED**. Independent portable research; no formal Task CLAIM, Result or external review.

## Fixed scientific model and provenance

Scientific pin: `awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15`.
Research parent: `enterprise-math@9d2acb53a59a2790c499f6890424feb335a33de6`, `research_notes/portable_direct/r5_o1_first_contraction_m37_20261122/`. This is the exact five-event scalar partition model; it is a derived counting observer, not a replacement for P000 or X6.

Prices: all integers `p=214,...,314`. Multiplicities `a_p>=0`, total cost `N=sum p*a_p`. With fixed integer threshold `m>=1`, failure `E_i` imposes `sum_{p in S_i}a_p<m`. The five sets are:

- `S0={214,215,216,217,218}`;
- `S1={214,216,217,218,219,220,221}`;
- `S2={215,216,217,218,219,220,221}`;
- `S3={223,...,290}`;
- `S4={296,...,312}`.

The generating function for configurations satisfying at least one failure is `F_m(q)=R_m(q)/D(q)`, where `D(q)=product_{p=214}^{314}(1-q^p)` and `R_m` is the integer-polynomial numerator from exact, signed event inclusion–exclusion. Write `M_m(O_m(N))` for the smallest simultaneous coefficient period of the quasipolynomial components of degree at least two.

## Theorem: six additional exact periods

For **each** integer `m=45,46,47,48,49,50`, the strict minimum period is

```text
M_m(O_m(N)) = 229746052653717600.
```

Together with the parent finite-prefix theorem, the current recorded classification is: maximal period for `1<=m<=36` and `m=44,...,50`; exact contraction by a factor 43 for `37<=m<=43`. This document proves only the six newly examined thresholds; parent results retain their original proof/review status.

### Proof of upper bound

For a primitive `d`-th root of unity, the denominator has zero multiplicity `n_d=floor(314/d)-floor(213/d)`. Terms of degree at least two require a pole of order at least three. The entire candidate list with `n_d>=3` is `{1,...,34,36,37,38,39,43,44}` (40 orders); its least common multiple is exactly `L=229746052653717600`. Numerator cancellations can only reduce the poles. Therefore `M_m(O_m(N)) | L` for every positive integer `m`.

### Exact lower-bound certificates

Select `W={7,9,11,13,17,19,23,25,27,29,31,32,37,43}` with `lcm(W)=L`. For every `d in W`, the verifier chooses the first prime `P_d>=10001` with `P_d=1 mod d`, and a multiplicative element `w_d` of **exact order** `d` in `F_{P_d}`. It evaluates `R_m(w_d)` and its Euler derivative `(q d/dq)R_m(w_d)` using finite-field arithmetic on the *complete overlapping* core constraints and the two disjoint blocks.

For each of the 84 pairs `(m,d)`, the stored exact modular values satisfy

```text
R_m(w_d) != 0 mod P_d
OR
[n_d>=4 AND (q d/dq)R_m(w_d) != 0 mod P_d].
```

Because `R_m(q) in Z[q]` and `w_d` has exact order `d`, a nonzero modular value rules out divisibility by the cyclotomic polynomial `Phi_d`. When the zero-order value vanishes modulo `P_d` but the Euler derivative does not, it rules out divisibility by `Phi_d^2`. In characteristic zero, a corresponding primitive root thus retains a pole of order at least three, which forces `d` into the least coefficient period at degree at least two. Consequently `lcm(W)=L | M_m(O_m(N))`, matching the upper bound.

This argument is a finite exhaustive computational proof **subject to the correctness of the supplied exact evaluator**; the program enumerates every required `(m,d)` without interpolating untested thresholds.

### Exact signed intersection recurrence

The three overlapping core events are evaluated by seven-term inclusion–exclusion. Each intersection DP tracks a tuple of occurrence counts for precisely the participating events, capped at `m-1`. For a price belonging to several events, adding `r` copies increments **all** corresponding counters together. Multiplication of pairs `(f,qf')` uses `(fg,(qf')g+f(qg'))`. This preserves both signed overlap and derivative information.

Let `A_m` be the numerator of the union of the three core failures, `B_m` the failure numerator for `S3`, and `C_m` for `S4`. Since their price supports are disjoint,

```text
R_m = 1 - (1-A_m)(1-B_m)(1-C_m).
```

This equality is exact and is implemented by the parent verifier; no independence claim is made for the core events.

### Separate order-43 check and observed period revival

At primitive 43rd roots, every inclusion–exclusion term except the singleton `S1` contains one of the price multiples `215,258,301`, hence vanishes identically. Therefore `R_m(w)=P_{S1}(w)*sum_{r=0}^{m-1} h_r(w)` where `P_{S1}(w)=product_{p in S1}(1-w^p)` and `h_r` is the degree-`r` complete homogeneous polynomial in `{w^p:p in S1}`. This independent **single-event recurrence**, calculated separately from the five-event DP, matches every order-43 `R_m(w)` for `m=45,...,50`.

Using the exact 43-phase identity in the parent proof, `R_{m+43}(w)=R_m(w)` at primitive 43rd roots. The new nonzero zero-order residues at `m=45,...,50` are `8782,8662,8239,7185,8459,843` modulo `10321` (primitive root `w=3215`). These match `m=2,...,7` and confirm the post-contraction return through threshold 50.

## Verification and evidence

- `VERIFY_M45_50.py` regenerates all 84 modular order/threshold pairs using the parent versioned source `../r5_o1_first_contraction_m37_20261122/VERIFY_MODULAR.py`, checks exact witness coverage, recomputes both least common multiples, and checks the independent order-43 singleton formula.
- `CERTIFICATE_COMPACT.md` provides all 84 computed `(R_m(w_d),DR_m(w_d))` pairs in the fixed order `W`. The standalone author-side local assembly additionally yielded `sha256= b62ac75b453d42b603027ec8ec08a4c28fc08700935248dea0a8129ed3dcb048` for a 13,927-byte expanded JSON certificate (not claimed remotely published).
- Original exact computations used Python integer modular arithmetic, not floating point. 45, 46 and 47 were run as whole 14-order evaluations; 48 used 13 retained successful results plus a separate completed order-43 calculation; 49 and 50 were split into two complete seven-order computations each. All 84 valid witnesses were actually obtained. The order-43 recurrence was independently evaluated.
- Validation remains author-side. There is no independent mathematical review, Lean formalization or promoted Result.

## Next question

Determine the **next** threshold `m>50` where any required factor fails, and derive symbolic threshold-phase functions for candidate orders 29, 32 and 37. Where a modular witness vanishes, do not infer exact complex cancellation; derive a genuine cyclotomic divisibility identity or supply a different nonzero certificate. Continue preserving the five-event joint constraints, frozen input and the current P000/ACTIVE semantics.

## Source and scope

Source mathematical definitions: frozen R5 pin above; algorithm and earlier classification: parent commit `9d2acb53a59a2790c499f6890424feb335a33de6`, files `RESEARCH.md`, `EXTENSION_37_44.md` and `VERIFY_MODULAR.py`. Author-side computation and new finite lemma concern only this fixed scalar observer. Shared owner/CLAIM and Activity are separate control matters; this source file grants none.
