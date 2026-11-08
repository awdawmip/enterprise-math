# PREFIX-577 R6: exact 28-dimensional integral reachable realization for the passive gate-pair observer

Date: 2026-11-08 UTC. Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_PROVED / EXACT_INTEGER_POLYNOMIAL_VERIFIED / UNREVIEWED / NOT_ADMITTED**.
Provenance: next independent author-side increment after the degree-28 scalar generating-function theorem at commit `a3e9f095d92bd31d2ffcd6b3a40ccb733b137751`. This note is NOT a Source Task CLAIM, checkpoint, native CM experiment, Result, independent Driver review, or Foundation promotion.

## Object, observer and theorem

Keep the native 96 ports and their six distinct tagged actions each (576 original edges), six native spatial reward axes and separate temporal order, root zero. Sample each original tagged action uniformly. At reset native port 9, observe only the time to first gate and the accumulated rewards on axes five and six. The inherited **exact, label-derived passive** quotient has 37 classes. Its nongate weighted transition operator is `C(x,y)` over `Z[x,y]` and its gate-exit column is `g(x,y)`, where weights are `x^R5*y^R6`. The quotient reset class of native port 9 is `o=8`.

Write `R_n=e_o^T C^n` as a *full 37-component polynomial row* and `s_n=R_n g`. Let `Q(t,x,y)=sum_{k=0}^{28} q_k(x,y)t^k` be the exact published degree-28 scalar denominator, with `q_0=1`, odd `q_k=0`, `q_2=-8`, and `q_28=-3962711310336*x^5*y^5`. All 15 even coefficient polynomials are in the inherited `GENERIC_DEGREE28_CERTIFICATE.json`.

**New strengthened operator identity**, checked exactly in `Z[x,y]^37` *before applying the gate column*:

```text
R_28 + sum_{k=1}^{28} q_k(x,y) * R_(28-k) = (0,...,0) [37 components].
```

Form `B` as the 28-by-37 matrix whose rows are `R_0,...,R_27`. Define the explicit 28-by-28 polynomial companion `S` by `S[i,i+1]=1` for `0<=i<27`, `S[27,j]=-q_(28-j)` for `0<=j<28`, and all other entries zero. The vector identity proves, *over the integer polynomial ring*:

```text
B C = S B.
b = B g.
s_n = e_0^T S^n b  for every n >= 0.
F(z,x,y) = (z/6) e_0^T (I_28 - (z/6) S)^(-1) b.
```

Thus there is an **explicit integral polynomial 28-dimensional reachable linear realization**, preserving every passive nongate quotient-class future output in the reachable reset orbit, not merely the scalar gate count. Over `K=Q(x,y)`, `R_0,...,R_27` form a basis of the reachable row space. This is a linear weighted/signed representation; it is not a new positive Markov-chain partition or a lossless representation of original action-conditioned operations.

## Proof of exact dimension, independent witnesses

`prove_krylov28.py` computes all 29 rows as sparse exact integer bivariate polynomials, then verifies each of the 37 components of `sum_{k=0}^{28} q_k R_(28-k)` vanishes identically. The 28-by-37 matrix `B` has a nonzero 28-by-28 minor at `(x,y)=(2,3)` over `F_1000000007`. Exact pivot columns:

```text
[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,22,23,24,25,28,29,30,31]
det = 817959641 (mod 1000000007).
```

This proves the 28 rows are independent over `Q(x,y)`. Since the exact vector identity makes this span stable under right multiplication by `C`, all reachable rows belong to the same free 28-generator module. The previously independently verified original-96-port scalar Hankel determinant remains `595325725 (mod 1000000007)` at `x=2,y=3`; it proves that **no smaller linear realization of this scalar gate observer** exists over `Q(x,y)`.

`verify_krylov28_native.py` independently regenerates all original 576 tagged edges, then compares the native 96-port and the explicit 28-state companion predictions for **73 coefficients at each** of `(x,y)=(2,3),(3,2),(7,11),(1,1)` modulo `1000000007`: all **292** comparisons passed. The universal theorem follows from the exact symbolic vector identity; modular tests are independent implementation regression checks.

The reset scope is essential. The same degree-28 polynomial fails to annihilate the gate output from native port 6 at length 28: its exact modular residual for `x=2,y=3` is **288982959 mod 1000000007**. The six initial native ports with nonzero residuals at this specialization are `6,7,28,29,30,31`. Keep full 96-port labels, all six reward axes, and native action-conditioned operators for other declared observations.

## Artifacts, standing frontier and next action

A self-contained portable research ZIP was created, independently extracted, and both new validation scripts re-executed successfully. The ZIP includes the exact theorem, two runnable stdlib Python scripts, new JSON proof certificate, inherited frozen native kernel, prior exact degree-28 coefficient certificate, passive 37-class quotient certificate, and manifest.

New certificate SHA-256: `92bdc3be45e576c3b2bcedf73e1a8eefab4086a9d13f70f86144a6564f454c86`.
ZIP SHA-256: `74e9deecabfbb0fcbe98b4aa4994a0b179b22e0a29a3b5b8483f4e5992d46d86`.

BRC integration: `REUSE_EXECUTED` on the original tagged native carrier and 37-class passive exact quotient. The exact intertwiner `BC=SB` certifies the declared future-operation descent; the native kernel remains authoritative for observers outside the identified factor.

Separate canonical D25 publication `TP2-B6F4FC938FF94941C1B7` retains original-class H0/B0 divided powers, `[X]U mod p^2`, Frobenius direction/eta and native CM validation as unfinished; no canonical task execution authority was obtained. The previously requested UR V2 original four-file bundle remains a provenance recovery obligation: length 94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; do not replace it with a reconstructed artifact.

**Next discriminating scientific step:** compute the exact `K`-linear reachable space for other original native initial ports, and a joint minimal passive representation for multiple starting ports; test which port-level initial-condition directions still require more than 28 states. Preserve the declared observer and action-label boundary.
