# Bounded independent main-paper algebra and endpoint review

Reviewed: `FIXED_TRIANGLE_MULTIPLE_FLUX_AND_FROBENIUS_TERMINAL.md`, with
the explanatory sentence after (7) corrected during review. Scope:
(6)-(11), H-only final extension, canonical primitive degrees, combined
terminal source, and residual (21). Status: PASS WITH ONE EXPOSITION
CORRECTION APPLIED / SCALAR COMPARISON OPEN. No prime was instantiated;
neither the main checker nor any frozen checker was read or executed.

The first read found the statement that the canceled odd identity was
the H identity with R_O/2 substituted for R_H. That was incorrect because
the t derivative changes the x-derivative and logarithmic-derivative
coefficients. The parent replaced it with the correct equation

    xR_O'+R_O/2+k(12x-3)R_O/(4x-3)
                                 =(1-4x)^2(D_O z-B_O).

The displayed polynomial fluxes (6),(7) and their consequences were
already correct. The replacement sentence was checked against the
independent coefficient expansion. No other correction was needed.

The new independent `check_main_paper_algebra.py` passed 18 exact checks.
It verifies both all-coefficient polynomial identities, the explicit
canceled rows, all six endpoint polynomial values, the combined sources
(10),(11), U_0,V_0,T_1, the combined terminal V_(m-1), the final H
coefficient, and all g factors in (21). It imports no main or frozen
checker. The following finite endpoint arguments accompany those checks.

- For 0<=k<=m-2, D_H factors satisfy k+2<=m,
  3k+4<=N-2 and 3k+5<=N-1. The D_O factors satisfy
  2k+3<=2m-1, 6k+7<=p-6 and 6k+11<=p-2. All are positive
  and less than p, with remaining constant factors powers of 2 and 3.
  Thus both recurrences may divide by D on their asserted finite window.
- The H flux has degree at most 3k+6<=N; the O flux has degree at most
  6k+11<=p-2. Both vanish at their lower endpoint and lie inside the
  unique zero-at-zero canonical primitive range. Consequently neither
  (8) nor (9) discards a Frobenius term on this window.
- At the H-only final index k=m-1, the flux degree is at most
  N+3<=p-1 because m>=2. The I_c(f_m) denominators are at most
  N+3 and are therefore units. Independently reducing coefficients gives
  D_H(m-1)=15/4, a unit under the frozen p>3 premises. The extra H-only
  relation is legal and does not define the forbidden next J moment or
  beta value. In particular it cannot by itself construct T_(m+1).
- The six source combination factors are correct. At c=1/2 the H
  boundary factor is 2c=1, producing the first term of (10); the odd
  factor is 8(c/2)=2, producing the first term of (11). The c=1 and
  c=1/4 endpoints respectively combine to -9k-86/3 and 144k+656/3.
- The terminal odd correction was already independently proved in
  `O_MOMENT_FROBENIUS_TERMINAL_REVIEW.md`. Combining its three values
  with the literal coefficients 8,8/3,20/3 gives exactly
  V_(m-1)=(16^m-19)/3-2^(1-m), including every Frobenius term.
- In (21), the independent Gauss product identity gives
  sum a_k T_k=T_m/g+flux_T and
  sum a_k W_k=W_m/g+flux_W. Multiplication by the original coefficients
  g and 2 gives T_m+2W_m/g+g flux_T+2 flux_W. These are exactly the
  displayed endpoints and sources. The defect 1/(g a_m), derived from
  sum a=1/g, has not been omitted or normalized to 1. The unchanged
  triangle includes both j endpoints, all a_k are units through m,
  and the OLD-R source keeps D_m and its r=1 lower endpoint.

The separate tau carrier retains its literal boundary -tau and the
original scalar retains +6tau. No coefficient flux replaces it. Thus
(21) is an exact identity for the unchanged residual with all requested
endpoints and normalization factors. This review supplies no evidence
that the residual vanishes; the scalar comparison, LIFT, weighted p^3,
period normalization and full native X6 remain OPEN.
