# CM24 directed local mathematical review of frozen draft 19b59309

Date: 2026-10-11. Reviewer: the existing `six_row_evidence_review` assistant, with Root's direction and the author's context disclosed. This is a directed/shared-context local mathematical check, not blind review, not a Source formal DR identity, not native acceptance, and not a new claim/task/branch. No professional query, remote write, registration, grant, or Source mutation was made.

**The frozen base-map and derivative-norm increment has no blocking mathematical defect in the checked scope.** The erroneous termwise factor from the earlier script is corrected in this draft and can be falsified independently at p=19 and p=37. The local result determines a square after taking the norm; it does not identify the divided truncation G_p or prove UR. Until the separate global check is complete, the independently checked polynomial below is denoted P-tilde, the normalized pullback of the inherited S. Its identification with a particular period-source polynomial remains a separate requirement.

## Fixed inputs and reproducibility

The complete frozen author draft, script and results were copied without alteration into `input-snapshot-19b59309/`, along with the fixed primary sources and normalization report. `INPUT_MANIFEST_19b59309.json` records 11 full-byte copy/readback checks, total 4,567,750 bytes, SHA-256 and Git blob pins for every file. This is a byte-integrity count, not a count of mathematical theorems read.

| Frozen author input | Bytes | SHA-256 |
| --- | ---: | --- |
| Draft | 14059 | `19b59309b7acc37fb2fa2681ae63273886edf81a960932a697e1eec6267e0772` |
| Author script | 6026 | `300dbfcc57746e989c86ef8a804335b79708f8224bc71ad33df7349e53a1e209` |
| Author results | 11439 | `84bc13b9ab1c05f3809a9023d6449e77677ff5adcdc3e6b3ddbce4020ef9181d` |

The earlier script version actually read during this review was 5350 bytes, SHA `a8d7426e8a33432d2495616134cfd07d6dba3e0442b7ceba371eefb0dbef2ed2`; it had already removed the erroneous termwise factor. The currently frozen version additionally records the initial failed run. This review does not misreport either corrected version as still containing the original error.

Independent reproducer: `check_fiber_norm.py`, with output `FIBER_NORM_RESULTS.json`. Run:

```
PYTHONDONTWRITEBYTECODE=1 python /workspace/em-owner-resume-20261011/cm24-directed-review-20261011/check_fiber_norm.py
```

The actual run passed 17 exact symbolic assertions and checked all 12 irreducible quadratic quotient rings for p=13,19,37,43, retaining the six geometric lifts for each prime. It constructs the inherited polynomial from binomial coefficients rather than the author's recurrence, and computes in quadratic quotient rings rather than enumerating the author's finite-field pairs. The finite cases corroborate the algebraic arguments; they do not replace an all-prime proof or the inherited CM supersingularity input.

## Marked base map and six distinct lifts

Betina–Lecouturier's fixed v3 TeX, lines 620–662, and the actual fixed PDF page 20 were read. The PDF text extraction is saved as `BETINA_FIXED_PDF_PAGE20.txt`; the PDF has 22 pages, 258570 bytes and SHA `03117b4ce827afdbd61c21464c9a40b693f330a79e687590d6f4ec26ad1705fe`. Its H is the marked full-level-3 base Hauptmodul with w=z/(1-z), not an unmarked Hesse parameter. Maier's small coordinate and the author's selected marking must remain explicit. The selected h=(H+3)/3 differs from Maier's h_M=(h+2)/(h-1); equality of j does not discard their marking or normal-coordinate difference.

Exact rational simplification independently gives

\[
t=H(H^2+9H+27)=27(h^3-1),\qquad
X=t+54+729/t=27h^6/(h^3-1).
\]

The selected j-sheet is j=(t+27)(t+243)^3/t^3. The exact correspondence is

\[
R(J,X)=J^2-JX(X^2-126X+2944)+X(X+192)^3.
\]

It vanishes under that substitution. At X=216 it is J²−4834944J+14670139392, whose discriminant is 2^19·3^6·13²·19². Hence the j-pair collides modulo 13 and 19, while the H-to-X map below remains unramified. No rational single-valued j(X) is inferred.

The X=216 fibre is f(h)=h^6−8h^3+8, with discriminant 2^21·3^6. In H it is (H+3)^6−216((H+3)^3−27), with discriminant 2^21·3^36. The general fibre discriminant is 3^12X^5(X−108)^3. The derivative relative to H, including dh/dH=1/3, is

\[
X_H=27h^5(h^3-2)/(h^3-1)^2.
\]

On the fibre, h≠0, h³≠1,2 and the numerator is coprime to f. This proves six distinct unramified lifts in every characteristic p≥5, including the two j-collision primes.

For the target lanes p≡13,19 mod24, p≡1 mod3 and (2/p)=−1. Writing u=h³ gives u²−8u+8=0; u^p=8−u, N(u)=8 and N(u−1)=1. Since u^((p²−1)/3)=8^((p−1)/3)=1, all three cube roots of each u lie in F_(p²). None lies in F_p. Thus the six lifts form three Frobenius pairs. Their full-level labels remain available: N(h)=2r with r³=1, and t^p=729/t.

The independent finite calculation factors f into three irreducible quadratics. For example, with a primitive cube root ζ and the unique F_p root c of c³−6c−8, these are h²−cζ^i h+2ζ^(2i), i=0,1,2. The trace cubic has discriminant −864. The script checks the factors, irreducibility and Frobenius in each quotient ring; it does not confuse a choice of ζ with the residue-lane label.

## Pullback normalization and concrete old-formula failures

Set p=6m+1, A=(H+3)^6 and B=(H+3)^3−27. For the inherited monic degree-m S(X)=∑s_kX^(m−k), the exact normalized pullback is

\[
\widetilde P(H)=27^{-m}(h^3-1)^mS(X(H))
=27^{-2m}\sum_{k=0}^m s_k A^{m-k}B^k
=\sum_{k=0}^m s_k A^{m-k}B^k.
\]

The last equality uses 27^(2m)=3^(p−1)=1, for p≥5. It has degree 6m=p−1 and leading coefficient 1 in H. The k=0 term has degree 6m; every k>0 term has smaller degree 6m−3k. No per-k factor 27^−k belongs in this H expression.

The independently reconstructed older erroneous expression ∑s_k27^−kA^(m−k)B^k fails to vanish on the CM fibre:

| Prime | Quotient ring | Wrong-expression remainder | Correct-expression remainder |
| --- | --- | --- | --- |
| 19 | F_19[h]/(h²−8h+2) | 8+10h | 0 |
| 37 | F_37[h]/(h²−22h+2) | 24+27h | 0 |

All three branches fail at both these primes. At p=13, 27≡1, so the erroneous factor is invisible; a p=13-only regression would miss the defect. The frozen author draft now gives the correct normalization and retains the old failure honestly.

An exact elliptic-factor check gives R(1728,X)=(X²−576X−1728)². At p=19,

\[
S(X)=X^3+6X^2+5X+12=(X-7)(X^2+13X+1),
\]

and the quadratic is the reduction of X²−576X−1728. Thus the supersingular j=1728 images are actually present in this pullback input. They cannot be omitted merely because a generic-j factorization excludes the elliptic point. The linear X=216≡7 factor is separate. This check by itself does not certify the full supersingular population at every prime.

The draft's endpoint and simple-root argument is algebraically sound for the inherited binomial/hypergeometric S: S(0)=108^m binom(2m,m) and S(108)=108^m binom(3m,m) are nonzero because 3m<p. The Gauss equation has invertible leading coefficient away from its endpoints; a double root there forces all Taylor coefficients to vanish, since the degree m<p. Therefore the pullback has 6m distinct finite roots. Identifying precisely these roots with the entire modular supersingular population additionally consumes the correctly normalized Sakai supersingular equivalence. That external/theorem input, and any identification with the polynomial used in a period formula, are separate from the local rational calculation and are not manufactured by a degree count.

## Derivative and norm: exactly the finite conclusion

At any of the six lifts with S(216)=0,

\[
\widetilde P'(H_i)=U_iS'(216),\qquad
U_i=27^{-m}(u_i-1)^mX_H(H_i)\ne0.
\]

The selected lift and directed H parameter determine the first derivative. Taking the F_(p²)/F_p norm yields

\[
N(\widetilde P'(H_i))=N(U_i)S'(216)^2,
\qquad N(U_i)=-2^7 3^6r_i^2.
\]

This follows from N(u−1)=1, N(u−2)=−4, N(h)=2r and 27^(2m)=1; every multiplier is nonzero. The independent calculation recovers the same squared derivative from all three pairs:

| p | S'(216) | Recovered S'(216)² from each pair |
| --- | ---: | ---: |
| 13 | 9 | 3 |
| 19 | 8 | 7 |
| 37 | 33 | 16 |
| 43 | 23 | 13 |

The norm observer is invariant under changing a nonzero tangent's sign, since p+1 is even. It recovers only S'(216)² after retaining the branch multiplier. An expression involving the inverse (p+1)-power therefore produces an inverse-square quantity. Recovering a directed tangent from the globally normalized polynomial or additional orientation data uses extra information, and comparing it with G_p uses an additional divided-normal/p-adic calculation. None is supplied by the norm alone. This is a precise observer limitation, not a global impossibility theorem.

## Isolated higher-curve cusp note and unfinished boundary

The fixed source says, literally, that base H has “a pole of order 1” at [1]_Γ(3), and later that H viewed on X “has a double pole at c'.” The actual PDF page 20 contains both sentences. They refer to different curves, and the base map proof above consumes only the first.

An independently reproducible conditional cusp-width calculation deserves preservation before a later period comparison: under the standard map z→z, if the cusp c' is represented by 1/p and σ=[[1,0],[p,1]], then

\[
\sigma T^n\sigma^{-1}=
\begin{pmatrix}1-np&n\\-np^2&1+np\end{pmatrix}.
\]

For p≠3, the minimal positive n satisfying Γ(3) is 3; adding Γ0(p) adds no condition because the lower-left entry is already divisible by p. Thus both widths are 3 and the relative ramification index would be 1. The script verifies widths at 13,19,37,43; the matrix argument gives the general conditional computation. The identification of this standard map/representative with every marking and forgetful convention in the paper must be checked fully before interpreting the apparent discrepancy. This review does not declare Betina's theorem false, and does not use the conditional discrepancy to reject the base-map or norm increment.

Next requirement for the period route is a precise marked-curve, cusp/forgetful-map and directed-normal identification, followed by a comparison with the divided truncation G_p at the actual inherited CM lift. Until that comparison is established, the parent UR target remains OPEN. Nothing in this local report proves native Working Truth, novelty, mathematical target completion, or an arithmetic increase in congruence precision. The modular curves and finite fields retain their external type; they are not promoted to native physical space or causality.
