# Perfect Prime AP HCM0 — exact m=5 three-layer support exhaustion

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **FINITE EXACT EVIDENCE ONLY — HCM0 REMAINS OPEN**

## Result

For `m=5`, `n=4`, tree-cofactor degree `D=2m-1=9`, exhaust every support on exactly three distinct actual layers

\[
c_s=m^2s=25s,\qquad s\in\{0,1,2,3,4\},
\]

and every positive multiplicity triple

\[
\alpha=(a,b,c),\qquad 1\le a,b,c\le5,\qquad a+b+c=9.
\]

There are

- `binom(5,3)=10` three-layer supports;
- `19` admissible multiplicity triples per support;
- `190` exact mixed coefficients in total.

Every one of the 190 coefficients is nonzero and has the pure-shift target sign

\[
\boxed{(-1)^n=+1.}
\]

Thus

\[
\boxed{
190/190\text{ actual }m=5\text{ triple-support cells have the correct strict sign.}
}
\]

No actual-layer three-support obstruction occurs at `m=5`.

## Balanced sample

For support layers `(0,1,2)`, actual shifts `(0,25,50)`, and multiplicity `(3,3,3)`, the exact coefficient is

\[
\frac{606281913837168436546787482311248779296875}
{2130095297450584815801682840209259311560647444027632266554642894848}>0.
\]

## Verification

Paired exact checker:

`research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/actual_triple_support_exact_check_20260904.py`

Arithmetic: Python `fractions.Fraction` only.

The canonical newline serialization

`support | multiplicity | exact numerator/denominator`

of all 190 cells has digest

`sha256:638992a2e805c29ef85a188c96a4114f160bccf0e98599f6a776d979d8ed61c2`.

## Interpretation

This finite boundary sharply contrasts with the exact arbitrary-shift obstruction at

\[
m=7,\quad(c_0,c_1,c_2)=(0,2,5),\quad\alpha=(1,5,7),
\]

which has the wrong sign. The actual `m^2` block structure therefore continues to survive a strictly stronger exact test than the previously proved two-support theorem.

This exhaustion does **not** establish an all-`m` three-support theorem and does not imply HCM0. It is evidence for the actual-grid mechanism isolated in the Pascal/Hausdorff and two-scale-grid checkpoints.

No Result-ID is frozen.
