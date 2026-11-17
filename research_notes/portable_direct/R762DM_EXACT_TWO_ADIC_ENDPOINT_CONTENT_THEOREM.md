# R762DM — Exact 2-adic content and optimal equal-seed cost of paired-triad endpoint area

Date: 2026-11-18 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Author identity: `EM-X6-3050F6`, original SID `MCP-4b2d70a97f594366a7c94a0f8b45df38`. Independent review: `NOT_REVIEWED`.

## Frozen scientific inputs, observer and scope

Frozen taskbook: `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md@e3f42efac29a2da2d95be391f3231a664e2fade0`. Frozen P000 V5: `p000_reality_foundation.json@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Reuse R762DD open-path cocycle, R762DI signed six-step three-axis paired block `c70993410d204fa9468f9755465d2002dfe36f6d`, R762DJ/DK `fbd9a7cec4720528be9e7eee510770448d6a43e5`, and R762DL `377a733229fcc1fdb35d191e89bf3968b8addb89`.

The native ambient space has six signed axes and one independent time dimension. The present exact *candidate* calculation fixes three of the six axes, with all other native axes still present in the ambient ontology. Every six-step paired-triad Cell-return block has 36 named positive unit-weight alternatives. For endpoint *normalized* area modulo Q, each block's exact BRC group-ring distribution is a monomial translate of P² with

\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ,
\quad R_Q=\mathbb Z[X^{\pm1},Y^{\pm1},Z^{\pm1}]/(X^Q-1,Y^Q-1,Z^Q-1).
\]

The physical area modulus `q>=2` corresponds to `Q=q/gcd(q,2)`, since the paired closed-block area is even. Observe *only* the final area modulo q after k complete blocks. No statement here licenses these Cell-return paths as primitive `TRIADIC_CLOSURE_E` force-balance events, nor erases source names for a future observer that can read them.

## Theorem — exact 2-primary group-ring content, every exponent

Let `Q=2^a` for integer `a>=1`, `d=Q/2`. For `n>=0`, let `c_Q(n)` denote the greatest common divisor of **all** integral coefficients of `P^n` in `R_Q`, including zero coefficients; `c_Q(0)=1`. Then

\[
\boxed{c_Q(n)=2^{e_a(n)},\qquad
e_a(n)=\max\left(0,\left\lfloor\frac{n}{2^{a-1}}\right\rfloor-1\right).}
\]

This is an exact coefficient-content identity, not only an onset or lower bound. It strengthens the `2^{floor(n/Q)}` divisibility bound in R762DL, retaining the same first onset `n>=Q`.

For the original k-block endpoint distribution, `n=2k` and the irrelevant monomial translation preserves content. The **minimum** number of equally likely deterministic initial BRC seeds representing that *specific endpoint law* is therefore

\[
\boxed{M_q(k)=\frac{36^k}{2^{\max(0,\lfloor 2k/2^{a-1}\rfloor-1)}}\quad
\text{when }Q=q/\gcd(q,2)=2^a.}
\]

For `Q=1`, R762DL already gives `M_q(k)=1`. For composite Q with odd factors, R762DL gives `M_q(k)=36^k`; for `Q=3^a`, its exact 3-adic valuation remains a separate open target (apart from previously solved special cases).

### Proof of the lower 2-adic bound

Work in `R_Q`. Put `d=2^{a-1}`, `T=(XYZ)^d`, `H=1+T` and `U=1+X^d+Z^d`. Since `T^2=1`, for all `j>=1`,
\[
H^j=2^{j-1}H.
\]

In characteristic 2, Frobenius and the six-term support of P give
\[
P^d\equiv P(X^d,Y^d,Z^d)=(1+T)(1+X^d+Z^d)=HU\pmod{2R_Q}.
\]
The equality in the middle holds in the order-two subgroup of `R_Q`: its six monomials are exactly `1,X^d,Z^d,(XYZ)^d,Y^dZ^d,X^dY^d`.
Thus some `B\in R_Q` satisfies `S:=P^d=HU+2B`.

Let `n=dm+r`, `0<=r<d`. For `m>=1`, binomial expansion and the displayed identity for powers of H yield the **integral identity**
\[
S^m=2^{m-1}H\big((U+B)^m-B^m\big)+2^mB^m.
\]
Therefore `2^{m-1}` divides every coefficient of `P^{dm+r}=S^mP^r` when `m>=1`. For `m=0` the lower bound is the trivial exponent zero.

### Proof of sharpness, including every boundary case

Reduce modulo 2 and put `W_m=(U+B)^m-B^m`. The algebra `R_Q/2R_Q` is the group algebra of a finite 2-group. Its augmentation ideal is nilpotent, equivalently its elements of augmentation 1 are units. Since `aug(U)=3\equiv1\pmod2` and `aug(B)=b\in\mathbb F_2`,
\[
aug(W_m)=(b+1)^m-b^m=1\in\mathbb F_2.
\]
So `W_m` is a unit modulo 2 for every `m>=1`.

It suffices to prove `HP^r\neq0\pmod2` for each `0<=r<d`. Apply the ring homomorphism `Y=Z=1` from `R_Q/2R_Q` onto `\mathbb F_2[X]/(X^Q-1)`. There `H\mapsto1+X^d=(1+X)^d` and `P\mapsto3(1+X)=1+X`. Consequently
\[
HP^r\longmapsto (1+X)^{d+r}\neq0,
\]
since `\mathbb F_2[X]/(X^Q-1)\cong\mathbb F_2[t]/(t^Q)` with `t=X+1`, and `d+r<Q`. Thus the reduction of `2^{-(m-1)}P^{dm+r}` is `HW_mP^r\neq0`; at least one coefficient has 2-adic valuation exactly `m-1`. When `m=0`, the same specialization shows `P^r\mod2\neq0` because `r<Q`.

Finally `c_Q(n)\mid 6^n`; only 2 and 3 can divide it. If `Q=2^a>=2`, the quotient `R_Q/3R_Q` is reduced after extension to an algebraic closure (3 is coprime to Q). The six distinct monomials in P give a nonzero element in this reduced ring, so `P^n\neq0\mod3` for all n. Hence 3 never divides `c_Q(n)`. Combining this with the exact 2-adic exponent proves the displayed formula. QED.

## Explicit endpoint consequences

| physical q | normalized Q | exact `v_2(G_Q(k))` | first compressed k |
|---:|---:|---|---:|
| 4 | 2 | `2k-1` | 1 |
| 8 | 4 | `max(0,k-1)` | 2 |
| 16 | 8 | `max(0,floor(k/2)-1)` | 4 |
| 32 | 16 | `max(0,floor(k/4)-1)` | 8 |
| 64 | 32 | `max(0,floor(k/8)-1)` | 16 |

The arithmetically exact seed saving relative to all `36^k` named paths is a factor `2^{e_a(2k)}`. This is only a final-area probability-law compression, *not* a proof of lawful lossy compression of an ongoing signed Cell/Link/Port dynamics. Observing intermediate areas, the source branch, or actual licensed `TRIADIC_CLOSURE_E` events may require larger state.

## Author verification and limits

`R762DM_VERIFY.py` performs independent exact group-ring convolutions of the six monomials using arbitrary-precision integer coefficients; checks support mass `6^n`, whole-coefficient gcd, the stated exponent for every tested exponent (odd and even), and the 36-way paired block / shifted `P^2` equivalence. Tested `(Q,n_{\max})=(2,26),(4,26),(8,26),(16,26),(32,34)`: 138 complete Q/n configurations, 329,802 nonzero coefficient entries, four direct 36-way shift checks, all PASS. `R762DM_EVIDENCE.json` records parameters, sample results and finite-test coverage. This is *author* verification; the universal result above is established by the algebraic proof. Independent review: `NOT_REVIEWED`.

## Next unresolved unit

The exact `3`-adic exponent of `G_{3^a}(k)` remains open for arbitrary `a,k`; previous R762DJ solves Q=3. A second independent dependency is the authentic source-pinned `TRIADIC_CLOSURE_E` signed Cell/Link/Port event predicate with V17/V29/V39 transport, required to test whether the endpoint-area observer is sufficient for actual legal future operations. Reuse the immutable Science pins and original claim; do not replay completed R762CA–DL research.
