# PREFIX-663-R6 — Sixteenfold wider BRC variance edge-maximizer strip

Date: 2026-11-10 (Asia/Shanghai). Researcher-ID: `EM-DIRECT-B3D89A / TASK_RESEARCH`; Research-Activity-ID: `RA-DAF861B6073C1E68895EECB3`.
Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem 663.1 (sixteenfold continuous-strip extension)
For the frozen 189-layer BRC two-information-direction statistical-observer model, put
`μ(p,z)=E[Y]`, `H(p,z)=E[Y²]/2`, `W(p,z)=2H(p,z)-μ(p,z)²` and `V_q(p,z)=q²W(p,z)-qμ(p,z)`.
Let `ε=2^(-17)=1/131072`, `J=[607/4096,609/4096]`, `R=[0,ε]×J`. For **every** real `q∈[12,24]` and `(p,z)∈R`,
```
∂_p V_q(p,z) < -4126.
```
Using the PREFIX-660 boundary theorem, let `z_*(q)` be the unique stationary edge maximizer on `J`, with `∂²_z V_q(0,z)<-12800000`. Then `(0,z_*(q))` is the unique maximizer of `V_q` on `R`, and, writing `M_q=V_q(0,z_*(q))`,
```
M_q-V_q(p,z) >= 4126*p + 6400000*(z-z_*(q))²
```
with strict inequality away from the maximizer. This is a **16×** area expansion over PREFIX-662's `p≤2^(-21)` rectangle and an **8192×** expansion over PREFIX-661's `p≤2^(-30)` rectangle. The PREFIX-660 exact brackets for `M_12` and `M_24` remain valid on this enlarged strip.

## Proof
Let `A_n(k)` be frozen surviving signed-path multiplicities and `f_n(k)=A_n(k)/binom(n,k)∈[0,1]`. The original `wide(n,k)` predicate is applied without changing any frozen scientific inputs. For `s_n(p)=Σ_k A_n(k)p^k(1-p)^(n-k)`, Bernstein differentiation gives
```
s_n''(p)=n(n-1) E[Δ² f_n(K)],  K~Binomial(n-2,p).
```
Because `|Δ² f_n(k)|≤2` and `P(K≥1)≤(n-2)p`,
```
|s_n''(p)| ≤ n(n-1)(|Δ² f_n(0)| + 2(n-2)p).
```
The exact three-coordinate count recurrence in PREFIX-662 gives
```
A=Σ n(n-1)|Δ² f_n(0)|              = 13800,
B=2Σ n(n-1)(n-2)                    = 617937012,
C=Σ(n+1)n(n-1)|Δ² f_n(0)|           = 485400,
E=2Σ(n+1)n(n-1)(n-2)                = 93926425824,
```
where `n=2,...,188`. The moment kernels for `μ` and `H` are nonnegative, bounded respectively by 1 and `n+1`. Exact edge support yields `0≤μ_p(0,z)≤225`. Therefore, on `0≤p≤ε`, uniformly in `z∈J`, set
```
U2=A+Bε;  H2=C+Eε;  U1=225+Aε+(B/2)ε²;
|μ_pp|≤U2, |H_pp|≤H2, |μ_p|≤U1.
```
The frozen clocks stop by layer 189, hence `0≤μ≤378`. With `W=2H−μ²`,
```
|W_pp| ≤ 2H2+2U1²+756U2 =: K_W.
```
For all `12≤q≤24`,
```
|∂²_p V_q| ≤ 576K_W+24U2 =: K.
```
Exact integer/Fraction arithmetic at `ε=2^-17` now gives
```
εK = 5479707930572204387915303313/75557863725914323419136 < 72524.
```
PREFIX-661 certifies `∂_p V_12(0,z)<-76650` and `∂_p V_24(0,z)<-306490` for all `z∈J`. Since `∂_p V_q(0,z)/q=qW_p(0,z)-μ_p(0,z)` is affine in `q`, the endpoint inequalities imply `∂_p V_q(0,z)<-76650` throughout `q∈[12,24]`. Integration in `p` gives
```
∂_p V_q(p,z)<-76650+εK<-4126.
```
Integrate once more in `p`, then apply PREFIX-660's edge strong concavity in `z` to obtain the stated stability inequality and uniqueness. QED.

## Verification, reuse and next unit
The attached Python certificate re-evaluates the **189 exact low-count recurrence rows** under the frozen integer-bisection predicate, verifies the support and budgets, and proves the new rational inequality. Expected result `ALL_CHECKS_PASS 570`; the predicate checks contribute to this count. Its rational loss is recorded exactly in the accompanying JSON. A separate local Python reproduction of the same recurrence and bounds also passed 570 checks. This is a model-internal statistical-observer theorem, not a physical native spatial or 96-port dynamics claim.

**BRC tool resolution:** `COMPOSE_APPLIED` — signed-path multiplicity with justified low-count Bernstein projection; all other coefficients remain represented by the existing `[0,1]` coefficient envelope. Scientific predecessors: PREFIX-660, 661, 662 (frozen pin unchanged). Independent review and formal Result admission remain pending.

**Next discriminating question:** use first positive-count Bernstein coefficient layers or tighter kernel envelopes to certify `p≤2^-16`; separately exclude portions of the full symmetry-reduced chamber `0≤p≤z≤1/2` by interval upper bounds against the moving boundary optimum. The parent objective is still the full-domain global variance maximum.
