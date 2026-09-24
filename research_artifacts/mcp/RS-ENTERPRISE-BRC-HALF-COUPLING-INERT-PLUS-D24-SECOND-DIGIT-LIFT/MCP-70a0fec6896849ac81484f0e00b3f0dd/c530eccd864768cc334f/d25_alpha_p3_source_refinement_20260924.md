# D25 exact source refinement: raw d=3 coefficient through one additional p-adic digit

Status: `PROVED_SOURCE_P3_REFINEMENT / STRICT_REDUCTION / NOT_A_RESULT / UNREVIEWED / LIFT_OPEN`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`

Consumed canonical frontier: the Source-published alpha bridge at the current D25 checkpoint, which proves
`alpha_p = G_T - D_p(t) - E_p(t) (mod p)`
for every target prime `p == 13 or 19 (mod 24)`, with the branch, valuation band, harmonic-deformation term, finite quadratic tail and finite-Gauss source provenance retained.

This unit does not recompute `alpha_p` modulo p. It lifts that same source coefficient one p-adic digit farther, because the remaining companion scalar `Lcomp_p` is a product-second-digit observer and cannot safely consume only the mod-p raw coefficient.

## 1. Exact coefficient expansion through p^3

Write `p=6r+1`, `n=2r=(p-1)/3`, and
`A_j=(1/3)_j(2/3)_j/(j!)^2`.

The exact d=3 source coefficient is
`H_{3,p-1}(t)=sum_{j=0}^n C_j t^j`,
with
`C_j=A_j * product_{q=j+1}^{3j}(1-p/q)`.

All `q` in this product satisfy `1<=q<=p-1`, so they are p-units. Put

`h1_j = H_{3j}-H_j = sum_{q=j+1}^{3j} 1/q`,

`h2_j = H^{(2)}_{3j}-H^{(2)}_j = sum_{q=j+1}^{3j} 1/q^2`.

Expanding the finite product exactly to second order in p gives

`product(1-p/q)
 = 1 - p h1_j
   + p^2/2 * (h1_j^2-h2_j)       (mod p^3)`.

Therefore, with

`F_n(t)=sum A_j t^j`,

`D_p(t)=sum A_j h1_j t^j`,

`M_p(t)=1/2 * sum A_j (h1_j^2-h2_j) t^j`,

one has the uniform all-target identity

`BOX 1: H_{3,p-1}(t)
       = F_n(t) - p D_p(t) + p^2 M_p(t)   (mod p^3)`.

No finite-prime computation is used in this derivation.

## 2. The finite quadratic tail is p-divisible before reduction

Let

`B_k=(1/6)_k(1/3)_k/(k!)^2`,

`G_n(lambda)=sum_{k=0}^n B_k lambda^k`,

and use the frozen branch
`t=(2-sqrt(2))/4`, so `4t(1-t)=1/2`.

The classical quadratic transformation gives equality of the infinite formal series
`_2F1(1/3,2/3;1;t)=_2F1(1/6,1/3;1;4t(1-t))`.

For the finite defect

`T_p(t)=G_n(4t(1-t))-F_n(t)`,

every t-coefficient of degree `<=n` is exactly zero, because such a coefficient cannot receive a contribution from a hypergeometric term with index `>n`.

A surviving degree `>n=2r` can only come from `k>r`. For every `r<k<=2r`, `(1/6)_k` contains exactly the single factor `6r+1=p`, whereas `(1/3)_k`, `k!`, and all remaining factors are p-units. Hence `v_p(B_k)=1` on the entire contributing high band. Consequently

`T_p(t) in p Z_(p)[t]`

as an exact finite polynomial statement. Define

`E_p(t)=T_p(t)/p`.

Thus, at the frozen target,

`BOX 2: F_n(t)=G_n(1/2)-p E_p(t)`,

with `E_p` retained as the labelled high-band/finite-cutoff correction, not absorbed into an untyped scalar.

## 3. One-more-digit raw source coefficient

Let

`S_p := G_n(1/2)`.

The accepted supersingular source facts give `p | H_{3,p-1}(t)` and `p | S_p`. Define the one-digit-deeper p-adic source quotients

`alphaHat_p := H_{3,p-1}(t)/p  (mod p^2)`,

`GThat_p := S_p/p                  (mod p^2)`.

Combining BOX 1 and BOX 2 and dividing by p yields

`BOX 3:
 alphaHat_p
 = GThat_p - D_p(t) - E_p(t) + p M_p(t)    (mod p^2)`.

Reducing BOX 3 modulo p recovers exactly the previously canonical relation
`alpha_p=G_T-D_p-E_p`.
The new information is the explicit first lift
`p M_p(t)` together with the one-digit-deeper finite-Gauss quotient `GThat_p` and the unchanged labelled quadratic-tail correction.

This closes the raw `a_raw(p-1)` coefficient port through the precision needed to enter a p^3 product comparison:

`a_raw(p-1)
 = p [GThat_p-D_p-E_p+p M_p]       (mod p^3)`.

It does not compute the normalized companion coefficient.

## 4. Consequence for the remaining companion problem

The durable source decomposition remains

`b_raw(p-1)=a_raw(p-1)+c_p J_p`,

`Lcomp_p=(c_p alpha_p J_p-1)/p (mod p)`,

`TRAW_p=alpha_p^2+Lcomp_p (mod p)`.

BOX 3 proves that lack of one-more-digit information in the raw d=3 coefficient is no longer a legitimate blocker: its p^3 source expansion is explicit in the existing finite-Gauss carrier plus `D_p,E_p,M_p`.

The unresolved datum is now narrower and source-typed: the actual normalized Gauss-Manin companion coefficient `J_p` (or an exact invariant proved equivalent to the divided comparison scalar). This unit does **not** replace `J_p` by the ordinary derivative of the finite coefficient polynomial. The canonical coordinate warning remains binding.

## 5. BRC information audit

Population: target primes `p == 13 or 19 (mod 24)`, with `p=6r+1`.

Observer: the raw d=3 coefficient through `p^3`, equivalently `H/p mod p^2`, only as input to the companion/product second-digit observer.

Preserved coordinates: the selected `sqrt(2)` branch, exact p-adic valuation bands, first harmonic deformation `D_p`, second harmonic/moment correction `M_p`, the `r/2r` finite quadratic-tail boundary `E_p`, and the finite-Gauss source quotient `GThat_p`.

Safe compression proved here: the raw source coefficient port may be replaced at this observer by
`(GThat_p,D_p,E_p,M_p)` through BOX 3.

Unsafe compression: reduce `alphaHat_p` to `alpha_p` before the companion p^3 product is formed; discard the quadratic tail; or identify the Gauss-Manin source coefficient with an ordinary derivative without a source-coordinate proof.

`BRC_REUSE_RESOLUTION = COMPOSE_APPLIED + STRICT_REDUCTION_APPLIED`.

## 6. Deterministic regression/falsification

An independent exact checker works in `(Z/p^3 Z)[s]/(s^2-2)` at `t=(2-s)/4`. It reconstructs the exact `C_j`, `A_j`, `B_k` recurrences, harmonic sums through the required orders and verifies BOX 1, p-divisibility of the finite quadratic tail, BOX 3, and the source divisibilities.

It was executed for all 166 target primes below 5000 with zero failures. This finite run is regression/falsification only; Sections 1-3 are the proof.

## 7. Narrow next action

Compute the **actual normalized d=3 Gauss-Manin companion coefficient** one p-adic digit deeper and form `Lcomp_p`, substituting the proved BOX 3 rather than recomputing the raw coefficient. The source representative/local-coordinate transport must be derived explicitly; do not substitute `d H_{3,p-1}/d lambda` unless the coordinate identity is proved. Then seek the one-order-deeper finite-Clausen/endpoint bridge to the frozen LIFT target.

External source boundary: Chisholm--Deines--Long--Nebe--Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), DOI 10.3390/math1010009, especially the exact d=3 coefficient formulas and Section 5 companion setup.
