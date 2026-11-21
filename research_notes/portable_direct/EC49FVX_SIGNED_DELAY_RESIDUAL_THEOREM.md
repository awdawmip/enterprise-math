# EC49FVX — Signed second-order certificate-gap spectrum and exact delayed residual reconstruction

**Line:** EC49AS, frozen BRC16943. Portable continuation of EC49FVW.  
**Immutable parent:** awdawmip/enterprise-math@6277ba7443de4d469cbfb7e49628ae2ab3e4f9cb:research_notes/portable_direct/EC49FVW_SECOND_ORDER_RESIDUAL_SPECTRUM_THEOREM.md.  
**Frozen scientific constants:** U=4822040484/8132285009, Gamma=141024/1653649, and the original 11-row projective test.  
**Status:** AUTHOR_PROVED / EXACT_FINITE_RESIDUE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.  
**Scope:** exact arithmetic of certified rational phase candidates in the frozen Bernoulli-derived auxiliary observation. No native X6 physical transfer or P000 change is asserted.

## Certificate and signed residual coordinates

For positive h,n, retain the complete frozen predicate

\[
C_{11}(h,n)\iff (h\bmod 10,n\bmod 10)\in P_{10}\quad\text{and}\quad9h+10n\not\equiv0\pmod {11}.
\]

The mask P10 has exactly 44 classes; the companion verifier rebuilds them from the eleven projective rows of EC49FVW and checks 12,100 original cases rather than postulating the mask.

Let S_H contain reduced fractions h/q with 0<h<q<=H, C11(h,q-h). For H>32, EC49FVU/EC49FVW establish that the actual nearest certified neighbors of the missing anchor 1/2 are

\[
x_-={q_--1\over2q_-},\qquad x_+={q_++1\over2q_+},\qquad
q_\pm=H-r_\pm(H),\quad0\le r_\pm(H)\le5.
\]

The exact left and right distances are

\[
L(H)={1\over2}-x_-={1\over2(H-r_-)},\qquad
R(H)=x_+-{1\over2}={1\over2(H-r_+)}.
\]

Define the two auxiliary signed residual coordinates

\[
\rho(H)={r_-+r_+\over2},\qquad A(H)={r_+-r_-\over2}.
\]

They invert exactly as r_-=rho-A and r_+=rho+A. This is a coordinate change in the auxiliary certificate system, not a statement about the native six-dimensional geometry.

## Theorem 1 — A delayed single-sided residual recovers both sides

For sign s in {-1,+1}, let

\[
R_s=\{q\bmod220:\ q\ {\rm odd},\ C_{11}((q+s)/2,(q-s)/2)\}.
\]

Complete finite-field classification shows

\[
|R_-|=|R_+|=80,\qquad R_+=-R_-=R_-+168\pmod{220}.
\]

The maximum successive cyclic difference in either set is exactly 6. Therefore the 220-periodic deficit extensions obey

\[
\boxed{r_+(H)=r_-(H-168)\quad\text{for every integer }H.}
\]

The ordered pair sequence H -> (r_-(H),r_+(H)) has minimal period 220.

**Proof.** An integral determinant-one neighbor of 1/2 must have odd q and numerator (q+s)/2. Replacing q by q+220 increases both numerator and complement by 110, leaving the complete certificate invariant. Reconstructing the original projective rows gives two explicit 80-residue masks, and a complete 220-class check gives the reflection and shift identities and maximum cyclic gap 6; these are exact finite certificates, not sampled tendencies. The reflection is compatible with invariance of the 44-class mask under simultaneous residue negation and the mod-11 nonzero condition. The shift-168 equality is checked separately on the full mask. Because the allowed denominator set for the plus sign is the minus set translated by 168, the most recent admissible denominators below H and H-168 have equal deficits. The verifier checks all proper divisors of 220 for period reduction; none works. The inherited determinant-one neighbor theorem promotes these candidate deficits to the actual nearest certified fractions for H>32.

## Theorem 2 — Exact 14-state joint spectrum and signed moments

Across the full set of 220 height residues, the ordered pair takes exactly 14 states:

| (r_-,r_+) | Count | (r_-,r_+) | Count |
|---|---:|---|---:|
| (0,0) | 54 | (0,2) | 22 |
| (0,4) | 4 | (1,1) | 54 |
| (1,3) | 22 | (1,5) | 4 |
| (2,0) | 23 | (2,2) | 3 |
| (3,1) | 23 | (3,3) | 3 |
| (4,0) | 3 | (4,2) | 1 |
| (5,1) | 3 | (5,3) | 1 |

The signed coefficient has distribution

| A | -2 | -1 | 0 | 1 | 2 |
|---|---:|---:|---:|---:|---:|
| Count | 6 | 48 | 114 | 44 | 8 |

All moments here refer to the uniform ensemble H mod 220, not to a stochastic physical time process:

\[
\boxed{{\mathbb E}A=0,\quad {\rm Var}(A)={37\over55},
\quad{\rm Cov}(\rho,A)=0.}
\]

More completely,

\[
{\mathbb E}r_-={\mathbb E}r_+={123\over110},\quad
{\rm Var}(r_\pm)={16881\over12100},\quad
{\rm Cov}(r_-,r_+)={601\over12100}.
\]

The scalar-width spectrum of EC49FVW is recovered by projection: the counts of rho=0,1,2,3,4 are respectively 54,99,55,11,1. Zero covariance does not imply independence: rho=0 forces A=0. There are 54 negative-A and 52 positive-A heights despite an exactly zero signed mean, since frequency and signed magnitude are distinct observers.

**Proof.** Calculate both masks directly from the eleven original finite-field rows, then take the smallest backward deficit for each of the 220 heights. The full joint classification is the displayed 14-state table. Its exact rational moments are independently computed using Fraction arithmetic. The fixed 168 shift implies identical left and right marginal distributions, explaining the equality of their expectations/variances. Algebraically,

\[
{\rm Cov}(\rho,A)=\frac{{\rm Var}(r_+)-{\rm Var}(r_-)}4=0.
\]

The finite calculation is complete modulo the proved period, so the classification extends to every height, with actual nearest fractions identified under the inherited theorem when H>32.

## Theorem 3 — Signed midpoint displacement, exact formula, and lossy projection witness

The certified gap midpoint displacement from 1/2 is

\[
M(H)={x_-+x_+\over2}-{1\over2}={R(H)-L(H)\over2}.
\]

For every H>32 there is the exact rational factorization

\[
\boxed{H^2(R-L)=A(H){H^2\over(H-r_+)(H-r_-)}.}
\]

Hence the sign of the midpoint displacement equals sign(A), including exact zero, and

\[
\boxed{\left|H^2(R-L)-A\right|
\le2\left[\left({H\over H-5}\right)^2-1\right].}
\]

Along each residue class modulo 220, the rescaled displacement converges to that class's exact signed A. The scalar rho alone fails to preserve this observable:

| H | (r_-,r_+) | rho | A | H²(R-L) |
|---:|---|---:|---:|---:|
| 221 | (0,2) | 1 | +1 | 221/219 |
| 224 | (1,1) | 1 | 0 | 0 |
| 233 | (2,0) | 1 | -1 | -233/231 |

Thus the same second-order total-width coefficient rho=1 permits three different signed displacements. Keeping A along with rho recovers the two deficits and both exact gap endpoints at fixed H; retaining only rho is a lossy quotient for a signed midpoint observer.

**Proof.** Subtract the exact reciprocal formulas for R and L:

\[
R-L={r_+-r_-\over2(H-r_+)(H-r_-)}.
\]

The denominator is positive. Since 0<=r_±<=5 and |A|<=2, the multiplicative factor is in [1,(H/(H-5))²], giving the explicit error bound. The three example heights are independently checked against all reduced certified fractions q<=H, rather than only against the candidate determinant-one residue sets.

## Evidence, parent dependency, and next questions

The matching standard-library source EC49FVX_SIGNED_RESIDUAL_VERIFY.py and captured real execution output EC49FVX_SIGNED_RESIDUAL_OUTPUT.txt are in this same research_notes/portable_direct directory. Verification covers: the 12,100 direct finite-field comparison cases; full 220-class signed masks; 168-shift and reflection; period minimality; complete 14-state table; exact moments; sign and bound; and exhaustive reduced-Farey nearest-point enumerations for H=33,82,221,224,233,302. The output ends ALL PASS. These finite certificates yield infinite-height periodic consequences because the period is proved algebraically, and use exact rational/integer arithmetic.

The projective reduction from the frozen Bernoulli observation and the determinant-one actual-neighbor theorem remain cited parent obligations; the calculations in this file are not an independent review of those upstream bridges. No formal shared CLAIM, Result, Review, or Foundation admission follows from this author proof.

Next: classify analogous signed residual spectra for moving rational anchors a/b, especially gcd(b,110)>1; test whether one-sided delayed recodings persist. Continue separately on the global certified-gap conjecture lim_{H->infty} H G_max(H)=1, which is not implied by a fixed-anchor periodic certificate. Preserve joint signed residual information whenever a later observer can distinguish it.
