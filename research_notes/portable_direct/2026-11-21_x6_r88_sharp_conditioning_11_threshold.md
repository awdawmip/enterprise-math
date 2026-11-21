# X6 R88 — Exact 11-fold conditioning threshold and sharp all-lattice separation in four-readout BRC

Date: 2026-11-21 (Asia/Shanghai).
Status: SYMBOLIC_AUTHOR_PROOF + EXACT_FRACTION_AUTHOR_CROSSCHECK / NOT_INDEPENDENTLY_REVIEWED.
Mode: independent portable research; no claim of native Task CLAIM/PROGRESS, physical X6 transfer, or canonical mathematical acceptance.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
Direct predecessor: R86 (absolute nine-core theorem), R87 (paired rays and full-lattice tie counts). This R88 proof does **not** invoke R86's finite atlas coverage and does not enumerate the infinite lattice.

## Exact domain and statement

Use exactly the R86/R87 **conditional positive-count degree-four BRC star-histogram observer**, with one unknown additive offset and four strictly positive readout weights `w=(A,B,C,D)`. It is not an identification of native P000 signed Cell/Link/named Port or entire three-force event/time state.

For nonzero integer differences `a=(x,y,z)`, identify `a` and `-a`; define
```text
q(a) = max(x⁺+y⁺+z⁺, (-x)⁺+(-y)⁺+(-z)⁺)
Z(a) = (0, 2x+6y+12z, 6x+24y+60z, 14x+78y+252z)
g_ij(a) = |Z_i-Z_j|/2
F(a;w) = max_{i<j} g_ij(a)/(w_i+w_j).
```
Let `s=(10,-5,1)`, `t=(9,-5,1)`, `m=min(A,B,C,D)`, `M=max(A,B,C,D)`, `κ=M/m≥1`, `d=min(A,C)+min(B,D)`. Here `q(s)=11`, `q(t)=10`, and `F(s;w)=1/d`.

**Theorem R88 (sharp full-lattice conditioning/separation).** For every positive real `w` and each integer difference `a` not equal to `±s`:

1. If `a=ks` for an integer with `|k|≥2`, then `F(a;w)/F(s;w)=|k|≥2`.
2. Otherwise, `F(a;w)/F(s;w)≥12/(κ+1)`.

For every integer Port budget `p≥11`, define the *reference-relative second direction cost*
```text
B_p(w) = min { F(a;w)/F(s;w) : a ∈ ℤ³, q(a)≤p, a≠0, a≠±s }.
```
Then the following bounds are **exact as worst-case infima** over all positive weights of anisotropy at most `R≥1`:
```text
inf_{M/m≤R} B_p(w) =
    12/(R+1)                  for 11≤p≤21,
    min(2, 12/(R+1))          for p≥22.
```
In particular, for every `p≥11` and every weight vector with `M/m<11`, `s` is the **unique** global minimizing unoriented integer difference for the full feasible lattice. The constant 11 is optimal: at `w=(1,1,11,11)`, `s` ties with `t`; for `w=(1,1,R,R)` and `R>11`, `t` strictly beats `s`. This is a global uniform-condition-number guarantee, **not** a necessary condition at each individual weight vector.

## Proof: exact mod-6 gap obstruction

Write
```text
u = x+3y+6z,
v = 3x+12y+30z,
h = 7x+39y+126z.
```
The within-parity channel gaps are
```text
g_13(a)=|v|,                       g_24(a)=|h-u|
                                     = 6|x+6y+20z|.
```
If `g_24(a)>0`, its integer divisibility gives `g_24(a)≥6`.
If `g_24(a)=0`, then `x=-6y-20z`, hence `v=-6(y+5z)`; either `g_13(a)≥6`, or `y=-5z, x=10z` and `a=zs`.
Consequently every nonzero direction outside the integral line `ℤs` has
```text
max(g_13(a), g_24(a)) ≥ 6.                         (R88-1)
```
This divisibility lemma holds on the **unbounded** integer lattice; no finite enumeration or R72/R86 coverage certificate is needed.

Write `e=min(A,C)`, `E=max(A,C)`, `f=min(B,D)`, `G=max(B,D)`. Then `d=e+f`. Since `E,G≤M` and `e,f≥m`,
```text
max(A+C, B+D) = max(e+E, f+G) ≤ d+(M-m).
```
By (R88-1),
```text
F(a;w) ≥ 6/max(A+C,B+D) ≥ 6/[d+M-m].
```
Dividing by `F(s;w)=1/d` and using `d≥2m`, obtain
```text
F(a;w)/F(s;w) ≥ 6d/[d+M-m] ≥ 12m/(M+m) = 12/(κ+1).
```
For integral multiples `a=ks`, linearity of all six gaps yields the first case. Thus for `κ<11` every other feasible direction has strictly larger objective. In particular uniqueness is established without any appeal to a nine-vector candidate list.

## Proof of sharpness, Port cases, and boundary

Exact substitution gives
```text
g(s)=(1,0,1,1,0,1),    g(t)=(0,3,6,3,6,3)
```
in channel-pair order (12,13,14,23,24,34).
For every real `R≥1`, the weights `w_R=(1,1,R,R)` satisfy
```text
F(s;w_R)=1/2,  F(t;w_R)=6/(R+1),
F(t;w_R)/F(s;w_R)=12/(R+1).
```
Since `q(t)=10`, this attains the nonmultiple bound for all `p≥11`.
When `11≤p≤21`, the only feasible nonzero integral multiple of `s` up to sign is `s` itself, so this gives the first exact infimum. For `p≥22`, `2s` is feasible with `q(2s)=22` and ratio exactly 2 for **every** `w`; together with the nonmultiple witness, this gives the second formula.

At `R=11`, the `t` witness ties `s` at `1/2`; at larger `R`, `t` gives a strictly smaller cost. Hence 11 is the sharp universal anisotropy threshold. The stronger all-lattice sevenfold tie classification on this particular wall at `p≥125` is established separately in R87.

## Independent author-side exact check, status and next problem

Reproduction: `python3 research_notes/portable_direct/x6_r88_sharp_conditioning_verify.py > /tmp/r88.json`.
The Python stdlib `Fraction` cross-check exhausts all **47,305** unoriented nonzero integer differences with `q≤30`, at **11** exact positive integer weight tuples: **520,355 direction/weight pairs**. It verifies (R88-1), the two exact ratio inequalities, uniform uniqueness where `κ<11`, and `t` equality for weights `(1,1,R,R)`. Companion certificate: `research_notes/portable_direct/x6_r88_sharp_conditioning_results.json`. All local assertions passed on 2026-11-21. The **universal** theorem is the symbolic integer/divisibility proof above; the finite check is independent corroboration by the same author, not external peer review.

This supplies a rigorous and computationally inexpensive robust-observer region in the conditional BRC model. Next: characterize nonuniform weight chambers where `s` remains strictly best even for `κ≥11`, including first noncore tie walls, and test separately whether a source-defined native P000 named-Port whole-triadic observer preserves future operations on histogram fibers. Original R063 native six-file benchmark is still pending.
