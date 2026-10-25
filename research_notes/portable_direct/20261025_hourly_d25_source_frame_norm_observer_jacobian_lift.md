# D25/LIFT — finite local Jacobian criterion for source-framed quadratic norm observers

Date: 2026-10-25. Classification: **TASK_RESEARCH portable author proof, AUTHOR-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM / NO_NEW_NATIVE_CHECKPOINT**.

## Scope, provenance and first new question

Parent Objective D25/LIFT/JT2 remains **OPEN**. Existing Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Last previously authenticated native checkpoint is the historical commit `220ee1ba360f21152912d0b4c1abdf867a1e4496`; it grants no current Researcher claim/run authority.

Input consumed, not counted again: [the exact Cayley norm fiber and coordinate-repair theorem](https://github.com/awdawmip/enterprise-math/blob/94c7902036b0161661b442b03cddcbe1bb8576ab/research_notes/portable_direct/20261025_hourly_d25_cayley_norm_fiber_minimal_source_anchor.md). It proved that norm and first reduction leave a `p^(r-1)`-element fixed-frame ambiguity and that a suitable full *coefficient* removes it. The new problem here is to decide **for an arbitrary source-defined scalar observer** (in particular, any subsequently authenticated formula claiming to compute the original `kappa`) whether it preserves or collapses that ambiguity, with a necessary-and-sufficient test and an explicit finite-digit inversion.

All statements are elementary finite-ring *conditional* algebra. `a+bT` is a marked ordinary coefficient-ring model. No source identification with divided-power `H0/B0`, native Frobenius or physical coordinates is presumed.

## Theorem A — local two-observer Jacobian criterion (necessary and sufficient)

Let `p` be any odd prime, `r>=2`, `A=Z/p^r Z`, `R=A[T]/(T^2-2)`, with `sigma(T)=-T`. Fix `alpha=a+bT in R^times`; thus `N(alpha)=a^2-2b^2 in A^times`. Write `a0,b0` for the reductions modulo `p`.

For any polynomial `f in A[X,Y]`, define
[
G_f(u,v)=igl(u^2-2v^2, f(u,v)igr),qquad
J_f=2a_0,partial_Y f(a_0,b_0)+4b_0,partial_X f(a_0,b_0)pmod p.
]
The same statement holds for a rational `f=P/Q` whose denominator is a unit throughout the fixed residue disk (derivatives taken using the quotient rule).

Let `U_alpha={(u,v) in A^2:(u,v)=(a,b) mod p}`. Then
[
oxed{G_f: U_alpha longrightarrow G_f(a,b)+pA^2	ext{ is bijective}iff J_f
e0pmod p.}
]
Consequently, norm + first source reduction + one transverse scalar observer give complete finite-precision fixed-frame reconstruction. If `J_f=0 mod p`, even the full `p^r`-precision pair (norm, observer) loses at least one distinct fixed-frame element.

**Proof.** The Jacobian at the common residue is
[
D G_f(a_0,b_0)=
egin{pmatrix}2a_0&-4b_0\ f_X(a_0,b_0)&f_Y(a_0,b_0)end{pmatrix},
qquad det D G_f=J_f.
]
For any `z,w in U_alpha`, polynomial telescoping (or clearing the everywhere-unit denominator) gives
[
G_f(z)-G_f(w)=M(z,w)(z-w),qquad
M(z,w)equiv DG_f(a_0,b_0)pmod p.
]
If `J_f` is a unit, `M(z,w)` is invertible over `A`; hence equal outputs force `z=w`. The image lies in `G_f(a,b)+pA^2`, and both finite sets have exactly `p^{2(r-1)}` elements, proving surjectivity. Conversely if `J_f=0`, choose a nonzero `h in ker DG_f(a_0,b_0)` over `F_p^2`. The two distinct inputs `(a,b)` and `(a,b)+p^{r-1}h` have identical outputs modulo `p^r` by the exact highest-digit Taylor identity. This is an explicit collision, so bijectivity fails. QED.

**Constructive inversion.** For any prescribed norm/observer pair congruent to `G_f(a,b) mod p`, start at `z_1=(a0,b0)`. At each digit `k=1,...,r-1`, compute the two-coordinate discrepancy `e_k=(target-G_f(z_k))/p^k mod p` and solve the *single fixed* invertible 2x2 system `DG_f(a0,b0) d_k=e_k mod p`. Put `z_{k+1}=z_k+p^k d_k`. The exact first-order congruence gives the target through digit `k+1` and yields the unique source-framed pair mod `p^r`.

## Theorem B — exact scalar readout on the fixed-norm Cayley fiber

Use the previously established, exact Cayley parameter `t in pA`:
[
eta(t)=alpharac{1+tT}{1-tT}=a(t)+b(t)T,
]
[
a(t)=rac{a(1+2t^2)+4bt}{1-2t^2},
qquad
b(t)=rac{b(1+2t^2)+2at}{1-2t^2}.
]
Put `g(t)=f(a(t),b(t))` for the polynomial or locally-unit rational observer above. Then
[
oxed{g:pAlongrightarrow f(a,b)+pA	ext{ is bijective}iff J_f
e0pmod p.}
]
When transverse, it is also an exact `p`-adic isometry on that disk:
[
oxed{v_p(g(s)-g(t))=v_p(s-t)}
]
for distinct `s,t in pA`, where `v_p` is the truncated valuation of a nonzero residue modulo `p^r`.

**Proof.** Every denominator `1-2t^2` is a unit on `pA`, so polynomial divided differences give
[
g(s)-g(t)=(s-t)H(s,t),quad
H(s,t)equiv 4b_0 f_X(a_0,b_0)+2a_0f_Y(a_0,b_0)=J_fpmod p.
]
If `J_f` is a unit, `H` is a unit everywhere, proving isometry/injectivity. Source and target each have `p^{r-1}` elements, so it is onto. If `J_f=0`, compare `t=0` and `t=p^{r-1}`; their observations agree modulo `p^r`, while the Cayley elements differ because `2T alpha` is a unit. This proves necessity and supplies the concrete collapsed top-digit witness. QED.

The finite digit-reconstruction algorithm for a prescribed `y in g(0)+pA` is
[
t_1=0,quad
d_k=left(rac{y-g(t_k)}{p^k}mod pight)J_f^{-1}mod p,quad
t_{k+1}=t_k+p^kd_k,quad 1le k<r.
]
All divisions are of integers known to be divisible by `p^k` before reduction; no analytic limit, numerical approximation, or unverified experimental primitive is involved.

For a *vector* of scalar observers `(f_1,...,f_s)`, the norm fiber is separated exactly when **at least one** of the derivatives `J_{f_i}` is nonzero modulo `p`. If all vanish, `t=0` and `p^{r-1}` collide in every component. Thus extra redundant observers do not repair a shared tangent-blind projection.

### Geometric / BRC observer interpretation

The norm-tangent source direction is `(delta_a,delta_b)=(4b0,2a0)`. The norm differential `(2a0,-4b0)` annihilates it. The new necessary-and-sufficient source-readout condition is **transversality**: `df(4b0,2a0)!=0`. The carrier is the marked quadratic coefficient pair and its conjugation; the coarse readout is norm plus residue; the retained structural fiber has `p^{r-1}` possibilities. This theorem classifies whether a proposed downstream observer safely collapses that fiber; it does not equate an unmarked gauge class to a physically fixed `H0/B0` frame. BRC status: `COMPOSE_APPLIED` (exact inherited Cayley fiber + observer-preserving finite-ring Jacobian lift), not new native primitive.

## Exact p=373 witness and independent finite examples

Consume the previously verified *ordinary Hesse*, **not native CM**, candidate:
[
p=373,quad r=2,quad
alpha=92060+21788T,quad
N(alpha)=122102pmod{139129},quad
(a_0,b_0)=(302,154).
]
At `t=373`, the exact second point is
[
eta=43570+107951T,quad
N(eta)=122102,quad
etaequivalphapmod{373}.
]
For `f(u,v)=u`, `J_f=4(154)=243 mod 373` and observing `u(beta)=43570` reconstructs the unique parameter `t=373` by the displayed digit algorithm. For `f(u,v)=v`, `J_f=2(302)=231`. For a nonlinear observer `f(u,v)=u+v^2`, `J_f=4b_0(1+a_0)=148 mod 373`. All three are transverse.

By contrast, the actual **tangent-blind** linear observer
[
f_{m blind}(u,v)=302u-308v
]
has `J_f=0 mod 373`, and the two distinct source-frame coefficients above yield exactly the same norm and `f_blind=82937 mod 139129`. This is an exact collision, not a rounding error or mathematical rejection of the source object.

**Actually executed author integer verification**, via a standard-library-only local script (stored separately as a project checker): for `(p,r)=(13,2),(13,3),(19,2),(19,3),(373,2)`, exhaustively enumerate all `p^{2(r-1)}` lifts of a fixed source residue. For each transverse observer `u`, `v`, `u+v^2`, the pair (norm,observer) has exactly `p^{2(r-1)}` distinct outputs; these are respectively **169, 28561, 361, 130321, 139129**. For each case, exact Cayley norm checks and digit inversion for five distinct `t` samples succeed; the last-digit blind-observer collision is verified. At `p=373`, the historical pair and both derivative values agree exactly. This is author checking, not independent proof review; Theorems A/B are algebraic.

## Source boundary, unsatisfied native experiment and next discriminating action

The new theorem does **not** establish that original crystalline `kappa`, `Delta_p-R_p` or a native divided-power coefficient is a polynomial/rational observer of the displayed Hesse pair. Original same-prime/same-CM-class `H0/B0`, `[X]U mod p^2`, real rank, sigma direction, source-frame normalization, and a lawful original `omega+6 nabla_lambda omega` / `kappa` map remain missing. **Native CM experiment NOT_RUN. D25/LIFT/JT2 OPEN.**

When source-authenticated CM data arrive: (1) pin their actual fixed frame, Frobenius action and normalization; (2) derive, rather than assume, any scalar source observer formula `f(a,b)`; (3) calculate `J_f` modulo the same prime to determine if norm + that observer reconstructs the frame; (4) if transverse, use the explicit lift to compare the original `kappa` / `Delta_p-R_p`; if blind, retain a proven transverse marked port. If the real native model has rank >1 or lacks this quadratic form, this exact theorem is **not directly applicable**.

This portable note is `UNREVIEWED / NOT_ADMITTED`. Current native continuation attempt returned `INVALID_ARGUMENT: CONTROL_QUOTA` under MCP 0.6.11; `recovery_status` is advertised but not invocable in this host. This is not `NO_DISPATCH`. Do not infer a current winner, new session, run, Source checkpoint, Result or independent audit. Existing bounded control support: Enterprise Math Issue #1558. Scientific frozen pin above remains unchanged; no scheduler or notification change is part of this research.
