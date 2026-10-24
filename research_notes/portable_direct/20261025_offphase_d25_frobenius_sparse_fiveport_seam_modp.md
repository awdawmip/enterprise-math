# D25/LIFT — sharp Frobenius seam and invertible sparse five-port jet over F_p

2026-10-25 · TASK_RESEARCH · PORTABLE AUTHOR-SIDE MATHEMATICS · **UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT / NOT_INDEPENDENT_REVIEW**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. The **scientific frozen source pin remains `c47e13e4aba0e006366f989d6334d443f6333ae3`**. This note is a derived finite-characteristic coefficient observer on the already published original WZ factor jet; it is not a claim to the original WZ proof or a Source-owned Task execution.

## Exact antecedent and typed setting

Let `p=6m+1 >=13` be prime, `n=2m`, and work in `F_p[[z]]` with **coefficient reduction modulo p**, not numerical evaluation of a truncated integer series modulo `p^D`. From the exact source-labeled all-precision factor-jet construction (see `20261025_offphase_d25_source_factor_jet_all_precision.md`), the two source channels are

```
Q_p(z) = 2m C(z) F_U(z) + (3z/220) B(z) F_sigma(z)

F_U(z) = (1+t z)^(-1)
     * prod_{k=2}^{n} (1-z/k)^2
     * prod_{j=1}^{p-2} (1+z/j)^2
     * prod_{j=1}^{n-1} (1+z/j)^(-1),

F_sigma(z) = P_base(z)
     * prod_{j=1}^{p-1} (1+z/j)^2.
```

Here `P_base(z)` is **exactly** the prior note's `F_sigma(z)` with only its displayed full-range `j=1,...,p-1` squared factor omitted; all original first-tail factorial, Wilson-reflection, Fermat-quotient, and scalar transfer factors stay untouched. Explicitly, `P_base(z)` equals

```
prod_{(c,e)=(-1,2),(2,2),(5,2),(8,1),(11,1)} (1+z/c)^(-e)
* (1+a z)^(-2) * (1+b z)^(-3)
* prod_{j=1}^{n-1} (1-z/j)^2
* prod_{j=1}^{5} (1+z/j)
* prod_{j=1}^{4} (1+2z/j) * (1+2z)
* prod_{j=1}^{2} (1+z/j)^(-2)
* prod_{j=1}^{n+4} (1+z/j)^(-1).
```

The parameters are `t=q_p(108)`, `a=q_p(2)`, `b=q_p(3)`; `C(z)` is the exact old-edge rational factor and `B(z)` the four-tail rational sum, both unchanged from that earlier source. All displayed constants inverted are p-units for the allowed primes, hence reduction is well-defined.

## Theorem — common five-port Frobenius factor, sharp seam, exact inverse

Define the short-source channels

```
K_U(z) = (1+t z)^(-1)
    * prod_{k=2}^{n} (1-z/k)^2 * (1-z)^(-2)
    * prod_{j=1}^{n-1} (1+z/j)^(-1),

K_sigma(z) = P_base(z),
H_p(z) = 2m C(z) K_U(z) + (3z/220) B(z) K_sigma(z).
```

These are formal series over `F_p`. Then for **every** such prime and **every** coefficient degree,

```
Q_p(z) = (1-z^(p-1))^2 H_p(z)   in F_p[[z]].
```

Writing `q_d=[z^d]Q_p(z)`, `h_d=[z^d]H_p(z)`, with negative subscripts equal to zero, gives the exact **three-shift forward rule**

```
q_d = h_d - 2 h_(d-(p-1)) + h_(d-2(p-1)) (mod p),
```

and the **explicit inverse**, still for all finite degrees and with no illegal `d^{-1}`,

```
h_d = sum_{ell>=0} (ell+1) q_(d-ell(p-1)) (mod p).
```

The shift law is sharp. Since `C(0)=-2` and the four-tail channel has an explicit leading factor `z`,

```
h_0 = -4m = 2/3 (mod p).
q_d = h_d for every 0 <= d < p-1.
q_(p-1) - h_(p-1) = -2h_0 = -4/3 (mod p) != 0.
```

Thus discarding the full-range factorial products first ceases to preserve the raw coefficient at the **first Frobenius degree p-1**; the exact shift/inverse pair retains that structural residue without manufacturing an additional primitive state. At degree `2(p-1)`, `q_{2(p-1)}=h_{2(p-1)}-2h_{p-1}+h_0`.

**Proof.** In the polynomial ring `F_p[z]`, inversion permutes the nonzero residues and

```
prod_{j=1}^{p-1} (1+z/j) = prod_{a in F_p^*}(1+a z) = 1-z^(p-1).
```

Remove the `j=p-1` factor `1+z/(p-1)=1-z` to obtain

```
prod_{j=1}^{p-2}(1+z/j) = (1-z^(p-1))/(1-z).
```

Both divisions are legitimate in `F_p[[z]]` because the divisors have constant coefficient 1. Substitute into each *original source-labeled port*; a common factor `(1-z^(p-1))^2` is extracted from the old-edge channel and from each of the four distinct tail terms, without collapsing their input provenance. The forward coefficients follow by multiplication. The formal identity

```
(1-X)^(-2) = sum_{ell>=0} (ell+1) X^ell
```

at `X=z^(p-1)` proves the inverse. Finally `C(0)=-2`, `-4m = 2/3` because `6m=p-1=-1 (mod p)`, and `p>=13` ensures `-4/3` nonzero. QED.

## Exact finite-field regression (author-side)

Checker: `20261025_offphase_d25_frobenius_sparse_fiveport_seam_check.py`. It independently constructs the full `j=1..p-2` / `j=1..p-1` original factors and the reduced factors with finite-field triangular multiplication/inverse; independently checks old-edge `F_U`, first-tail `F_sigma`, and complete rational five-port `Q_p`; checks both forward and inverse coefficient rules, including degrees beyond `p^2`.

| p | Degree cutoff D | h_(p-1) | q_(p-1) | q_(p-1)-h_(p-1) |
|---:|---:|---:|---:|---:|
|13|171|3|6|3|
|19|63|3|8|5|
|31|93|6|15|9|
|37|111|34|8|11|
|43|129|42|12|13|
|61|183|60|18|19|

**6/6 PASS** across full/direct and compressed source products, both scalar ports and inverse reconstruction. The `(p,D)=(13,171)` case crosses indices `d=p` and `d=p^2=169`. Computation is corroborative only; the above algebra is the all-prime proof of this **mod-p coefficient** statement.

## Scope, observer, and next action

BRC applicability: `COMPOSE_APPLIED` as a **source-labeled external arithmetic jet observer**, not a positive-weight BRC mass law. Carrier is the ordered five-port provenance with the old edge, four individual tails, p-valuation distinctions and coefficient jets kept separate before the shared Frobenius operator acts. Scalar aggregation remains lossy for possible CM/DP or native-X6 future observers. The forward map here is invertible on the **full F_p jet**, not on truncated p-adic numerical values. In particular **a coefficient congruence modulo p cannot be substituted for the all-D p-adic congruence modulo p^D**; the missing higher coefficient lifts are a separate obligation. No assertion about the underlying same-prime CM/DP class, three-dimensional native slice, Lean admission or total LIFT closure follows.

**New contribution:** exact common Frobenius factor, sharp universal degree-`p-1` defect `-4/3`, and reversible sparse transfer for the original five labeled WZ ports. **Inherited/not recredited:** original WZ identity, Wilson normalization, source-factor jets of arbitrary p-adic precision. Native Source ownership, continuation, writer/provenance and independent review remain unresolved; this Git evidence is only `PORTABLE / UNREVIEWED / NOT_ADMITTED`. The separate UR V2 four-file bundle is still not authenticated: historical target **94,687 bytes** and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; no substitute bytes or re-proof are asserted.

Next precise authorized action: recover the original UR V2 bytes and reconcile their actual writer/request in the original allowed Source context. Once canonical continuation and winning claim permit, checkpoint the existing proof/provenance. The mathematical D25 next obstruction remains the independently sourced same-prime original-class CM/DP representative and its genuine semilinear transfer, not another scalar WZ jet precision increment.
