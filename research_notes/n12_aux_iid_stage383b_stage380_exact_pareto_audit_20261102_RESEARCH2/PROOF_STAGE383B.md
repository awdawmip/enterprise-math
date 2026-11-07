# Stage383-B — Exact independent local audit of the Stage380 Pareto wedge and active-budget lemma

**Research2; 2026-11-02; portable author-side audit.** The scientific inputs remain pinned to GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, and original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Normative rules are read from current canonical main, not scientific pins. Parent: Stage382-B `ad1aefb5ec5053cdde6ce7a2496ff4b5f641078f` and Stage380-B `2187681feaf8b93caeb05eff1ba97eab35a08a51`, PR #1736.

## The exact conditional theorem audited

Assume the *original unsimplified* four-channel Bernoulli/BRC auxiliary problem:

- `B_k(z)=z^k(1-z)^(3-k)`, `w=(1,3,3,1)`, `m=(61,21,9,9)`.
- `r_k(x,y)=(4 B_k(x)+B_k(y))/5-m_k/160`.
- `D(a,z)=1/2 ∑_k w_k |B_k(a)-B_k(z)|`.
- `b(x,y)=5/32 ∑_k w_k |r_k(x,y)|`.
- `c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256`.
- Minimize `T=33/1024+c(P)+c(Q)` with `b(P)+b(Q)≤B*=2β*+11/5000` over `[0,1]^4`.

**Inherited hypothesis, not re-proved here:** Stage379 localizes each global minimizer (after source permutation) to
`P∈(0.2308,0.2345)×(0.55,0.56)` and
`Q∈(0.2365,0.239]×(0.57566,0.57574)`.

**Audited conclusion:** Every global minimizer satisfying that localization has `r0(P)≤0≤r1(P)`, `r1(Q)≥0`, active joint budget `b(P)+b(Q)=B*`, and hits at least one of `r0(P)=0`, `r1(P)=0`, `r1(Q)=0`. Within this wedge, BOTH complete original budgets equal `3[4x(1-x)+y(1-y)]/16−45/256`. The proof below treats all residual faces and the Q cost cusp with their actual one-sided derivatives.

## 1. Full original comparison signs, not a collapsed model

`B'_0=-3(1-z)^2`, `B'_1=(1-z)(1-3z)`, `B'_2=z(2-3z)`, `B'_3=3z²`. Thus each component is monotone on each of the declared x/y intervals; an endpoint enclosure is a continuous-interval certificate. An independently coded exact `Fraction` evaluation establishes 31 strictly fixed signs in the 32 comparisons obtained from the original `(source,coordinate,anchor,k)` combinations. The only varying cost comparison is `(Q,y,3/4,k=2)`, where `δ(y)=9/64−y²(1−y)` changes sign at `α=(1+√13)/8`. The derived cost polynomial identity is exact, including at the cusp:

`c(x,y)=5157/32768−189x/256+93x²/128−61x³/256+33y²/512−29y³/512+(21/512)|δ(y)|`.

Consequently `c_x=−3(1−x)(63−61x)/256<0`; for `y<α`, `c_y=3y(1−y)/64>0`; for `y>α`, `c_y=3y(18−25y)/256>0`. At `α`, both one-sided y derivatives are strictly positive. This includes the P box (entirely below α) and both Q cusp branches.

Exact endpoint enclosures of all four *original* residuals give `r2(P)>293311743/78125000000>0`, `r2(Q)>3773345362813/625000000000000>0`, `r3(P)<−108106291/10000000000<0`, `r3(Q)<−4474752060597/625000000000000<0`, and `r0(Q)<−6195795737187/625000000000000<0`. These hold over the complete closed rectangles, including corners.

Since `∑_k w_k r_k = 0` exactly, the full four-channel budget on both boxes is

`b=(15/16)r2+(5/16)max(r0,0)+(15/16)max(r1,0)`.

This representation follows from the four absolute values and is valid on zero faces by continuity; it is not a reduction of the original observation set.

## 2. Exact directional reductions of every disallowed residual sector

For P with `r0>0`, increasing x gives `c_x<0`. If `r1<0`, its one-sided `b_x=−3(2x−1)^2/4<0`, with `−b_x≥845883/4000000`. If `r1>0`, `b_x=−3x²/4<0`, with `−b_x≥998787/25000000`. At `r1=0`, increasing x enters `r1>0` (`r1_x>0`), hence the latter one-sided derivative applies. In every such case a feasible local improvement exists in the original domain.

For P with `r0<0,r1<0`, the complete budget simplifies in this sector to `b=15r2/16`, and `b_y=3 B'_2(y)/16≥21/625>0`. Decreasing y lowers both b and c. If `r0=0,r1<0`, use the one-sided direction `(dx,dy)=t(1/8,−1)`, `t>0`:

`dr0/dt=[B'_0(x)−2B'_0(y)]/10≤−2171883/40000000<0`,

`db/dt=3[B'_2(x)−2B'_2(y)]/32≤−652449/128000000<0`,

`dc/dt=c_x/8−c_y<0`.

The new state enters `r0<0`, retains `r1<0`, and remains within `[0,1]^2` for sufficiently small t. The strict margins use *conservative opposite endpoints* on the complete P rectangle. Thus the `r0(P)=0,r1(P)<0` nonsmooth boundary is also excluded.

On the Q box, `r0(Q)<0` holds everywhere. If `r1(Q)<0`, then `b=15r2/16` and `b_y=3 B'_2(y)/16≥1177877679/40000000000>0`; decreasing y improves b and c, with strictness preserved even if the Q coordinate was initially exactly at the cost cusp. The one-sided `c_y>0` on both sides ensures this.

These cases prove `r0(P)≤0≤r1(P)` and `r1(Q)≥0` without assuming the desired wedge formula in excluded sectors.

## 3. Active budget and strict face necessity

Inside that wedge `b=15(r1+r2)/16`; `B1+B2=z(1−z)` and `m1+m2=30` yield the claimed exact quadratic budget. If the budget were slack, increasing xP slightly would decrease the original c and keep original b feasible by continuity; thus equality holds.

Suppose `r0(P)<0<r1(P)` and `r1(Q)>0`. The original b and c are smooth locally and satisfy `b_x=3(1−2x)/4>0`. Define `λ(x)=−c_x/b_x=(1−x)(63−61x)/[64(1−2x)]`. Direct differentiation gives

`λ'(x)=[2+122x(1−x)]/[64(1−2x)²]`,

and `λ'(x)>1` whenever `378x(1−x)>62`. Since `x∈[0.2308,0.239]`, the minimum excess numerator is `15958919/3125000>0` (at x=0.2308). Moreover `xQ−xP>0.2365−0.2345=1/500`, and `b_x(Q)≥783/2000`.

Increase xQ and reduce xP by the unique amount required to preserve *the exact quadratic active budget*; the implicit-function theorem applies because both `b_x` are positive. The cost derivative along this feasible curve is

`d[c(P)+c(Q)]/dxQ=b_x(Q)[λ(xP)−λ(xQ)]<−783/1000000<0`.

The perturbation is within the original `[0,1]^4` even if xQ=0.239, since 0.239 is merely an auxiliary localization boundary, not a physical boundary. All relevant residual signs remain strict in this case. Contradiction establishes the three-face union.

## Reproduction, scope, and next question

The independent Python standard-library `Fraction` verifier `REPRO_STAGE383B.py` was run, all 32 audit sign ranges and eight original residual ranges were enclosable by exact interval endpoint monotonicity; 31 audit signs were strictly fixed and the sole cusp was isolated. The checker reconstructed exact signed cost coefficients and strict directional margins. Its machine-readable `CERTIFICATE_STAGE383B_EXACT.json` is **4786 UTF-8 bytes**, SHA256 **`c4e96b331fcbb5772423d36112e8106439e946e608774fdbee3d550928d82e0b`**, marker `STAGE383B_STAGE380_LOCAL_PARETO_AUDIT_PASS`. Run `python REPRO_STAGE383B.py` to regenerate. This is an exact author-side mathematical audit, not an independent Driver review.

**Scientific outcome:** The Stage380 local Pareto/wedge/active-budget implication is independently derived here from the original four-channel and labeled-cost expressions, conditional on inherited Stage379 localization. The priority remaining load-bearing question is an independent continuous-domain audit of Stage379 global localization (or an exact counterexample to its exclusion certificates), followed by a review of Stage381 uniqueness. The auxiliary-to-P000 X6 typed three-dimensional-slice observer bridge remains open.
