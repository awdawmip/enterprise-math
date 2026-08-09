# P025 Supplement 29 — Certificate Rank Gain After Shared-Prime Coupling

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 27–28  
Hard block: `NONE`

## 1. Stage 27 must pass through the prime-to-block map

Supplement 27 gives, for independent pairwise-coprime blocks, the certificate precision-rank gain

\[
\operatorname{rank}[L;H]-\operatorname{rank}L.
\]

Supplement 28 shows that with shared primes the block values already lie in `im B`, where `B` is the block-by-prime derivative coefficient matrix. Therefore both relations and certificates must first be pulled back to the fine prime-coordinate domain.

Declared relations become

\[
LBx=0,
\]

and block-linear certificates become

\[
HBx.
\]

## 2. P025-T82 — exact shared-prime certificate rank gain

Let

\[
K=\ker_{\mathbb Q}(LB).
\]

The certificate family on relation-adapted fine coordinates is

\[
HB|_K.
\]

Exactly as in Supplement 27,

\[
\boxed{
\Delta_H^{(B)}
=
\operatorname{rank}_{\mathbb Q}
\begin{pmatrix}
LB\\HB
\end{pmatrix}
-
\operatorname{rank}_{\mathbb Q}(LB).
}
\]

This is the independent certificate dimension visible **after** shared-prime coupling and declared relations have both been imposed.

## 3. P025-T83 — residual certificate-fiber rank

Supplement 28 gives compressed relation-state rank

\[
\boxed{
r_{\rm comp}
=
\operatorname{rank}B-\operatorname{rank}(LB).}
\]

Therefore the residual rank invisible to the exact certificate vector is

\[
\boxed{
r_{\rm residual}
=
r_{\rm comp}-\Delta_H^{(B)}.}
\]

Consequently

\[
\boxed{
0\le\Delta_H^{(B)}\le r_{\rm comp}.}
\]

No number of certificate outputs can recover directions already lost when fine prime coordinates were mapped through `B`.

## 4. Recovery of Stage 27

When non-unit blocks are pairwise coprime, the active rows of `B` have disjoint support and full row rank. On that active row space, multiplication by `B` preserves the relevant row-rank increments. Hence

\[
\Delta_H^{(B)}
=
\operatorname{rank}[L;H]-\operatorname{rank}L,
\]

recovering Supplement 27.

Thus Stage 29 is a strict generalization, not a competing formula.

## 5. Shared-prime example `2+4=6`

Supplement 28 gives

\[
B=
\begin{pmatrix}
1&0\\
4&0\\
3&2
\end{pmatrix},
\qquad
L=(1,1,-1),
\qquad
LB=(2,-2).
\]

The compressed relation-state rank is

\[
2-1=1.
\]

Take certificate `t_2`, with block row

\[
H=(1,0,0).
\]

Then

\[
HB=(1,0),
\]

and the augmented derivative matrix has rank two. Therefore

\[
\boxed{\Delta_H^{(B)}=1.}
\]

This single certificate is already complete for the rank-one compressed state.

Adding `t_4`, `t_6`, or many other linear outputs cannot raise the gain above one.

## 6. P025-N11 — certificate outputs cannot undo shared-prime collapse

Take blocks `(4,8)` with no declared relation. There are two block outputs, but

\[
B=
\begin{pmatrix}4\\12\end{pmatrix}
\]

has rank one because both depend on the same fine coordinate `x_2`.

Even if the certificate family reports **both exact block values**,

\[
H=I_2,
\]

one gets

\[
HB=B
\]

and therefore

\[
\boxed{\Delta_H^{(B)}=1,}
\]

not two.

The relation

\[
t_8=3t_4
\]

was created by shared prime-coordinate coupling before the certificate language was declared. Exact certificate outputs can expose that one remaining direction but cannot recreate an independent second direction that never existed in `im B`.

## 7. Certificates that vanish on the derivative image

For the same `(4,8)` system, the block-linear certificate

\[
\ell(t_4,t_8)=-3t_4+t_8
\]

is nonzero as a formal row in block space but satisfies

\[
HB=0.
\]

Hence

\[
\boxed{\Delta_H^{(B)}=0.}
\]

This is a sharper redundancy test than merely checking whether `H` lies in the row span of declared relations: a certificate can also become redundant because it vanishes on the prime-to-block image itself.

## 8. Architectural consequence

The full precision-rank accounting order is now

\[
\boxed{
\text{fine prime coordinates}
\xrightarrow{B}
\text{derivative image}
\xrightarrow{L}
\text{relation state}
\xrightarrow{H}
\text{certificate state}.
}
\]

Corresponding ranks are removed in that same order:

\[
\boxed{
\begin{aligned}
r_{\rm block}&=\operatorname{rank}B,\\
r_{\rm relation}&=\operatorname{rank}B-\operatorname{rank}(LB),\\
\Delta_H&=\operatorname{rank}[LB;HB]-\operatorname{rank}(LB),\\
r_{\rm residual}&=r_{\rm relation}-\Delta_H.
\end{aligned}}
\]

This prevents a common architecture error: counting certificate rows in a formal block space that contains directions already forbidden by shared prime-coordinate structure.

## 9. Prior-art / ownership boundary

Restricted-map rank, stacked-matrix rank gain, and image-kernel linear algebra are standard mathematics. P025 does not claim them.

The project-side result is the corrected precision-accounting interface for arithmetic-derivative blocks with overlap. It should be relayed to A3/P023 as a reusable relation-state tool rather than kept as abc-specific terminology.

## 10. Executable assets

Added:

- `src/enterprise_math/shared_prime_certificate_rank.py`
  - `HB` certificate pullback;
  - exact shared-prime rank gain;
  - residual rank and completeness flags.
- `tests/test_shared_prime_certificate_rank.py`
  - pairwise-coprime recovery;
  - `2+4=6` rank-one certificate completion;
  - relation-row redundancy;
  - `(4,8)` identity-output gain collapse;
  - certificate vanishing on `im B`.

## 11. Next frontier

No hard block exists. Continue with:

1. define exact joint preimage access costs for shared-prime matrix images;
2. seek finite HNF/SNF-based response summaries for those costs;
3. connect the rank-accounting stack to A3 relation-state precision formally;
4. test adaptive certificate selection using rank gain plus access cost, while keeping rank and proof cost distinct;
5. freeze this Stage-18–29 generation for validation/Relay before opening further mathematics.
