# R5 — Causally coupled I→J diamond: complete four-observer hull/image classification

**Research date:** 2026-11-02 (Asia/Shanghai). **Scientific status:** author-side analytical proof and executed exact-rational checks; `UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. This is a result about the precisely declared auxiliary two-law stopping model, not a P000 or X6 theorem.

**Frozen scientific inputs, retained:** GLOBAL_KNOWLEDGE_V1 `main@a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `main@86149263e38c22292c9def1e0f69092efa1be77e`. **Current behavioral-rule reads (separate):** global `main@8bc411955836722942ed70a399aa502efa1b7a54`; Enterprise Math `main@d5d2fe19b8cfd3d8702a8e7f1ebd7113b1fc1093`. P000 global original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches the global startup projection; ACTIVE worldview read and unchanged. Consulted `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, current portable research protocol, research method, mathematics/conclusion policies, BRC and joint-observer-preservation rules.

**Scientific predecessor:** immutable Enterprise Math commit `e7adc789498258e54c91c11dc9050f190c7c5727`, `research_notes/brc_r5_source_separable_zonotope_20261102_t0440/RESEARCH.md` and `NEXT_TASK.md`. That result classifies exogenously arriving, independently acting sources. This note permits the upstream stop/continue action at I to change the source composition actually reaching J.

## 1. Exact two-measure model and BRC provenance

Two probability measures P and Q govern a finite stopping/terminal-answer tree. Let `O=(e_P,e_Q,T_P,T_Q)`, where `e_P=P(final answer P)`, `e_Q=Q(final answer Q)` and T are expected terminal integer times. Terminal *decisions* to stop answer P. Natural terminal answers use strictly positive Bernoulli probabilities for P/Q under each law. Behavioral randomization is seedless and local to a time–likelihood-ratio key; the FULL observer may condition on the entire source-labelled past.

Choose real `0<a<1`, `0<r<1`, and six parameters `0<p_B,q_B,p_I,q_I,p_E,q_E<1`. At the root, a *natural* branch leads to decision key `I=(time 1, LR 1)` with probability a under BOTH P and Q; the other natural branch, probability `b=1-a`, bypasses I and reaches `J=(time 2, LR 1)`. At I, stop with probability x and answer P at time 1, or continue. On continue, a natural branch of P/Q probability r reaches J at time 2; the complementary natural branch of probability 1-r terminates at time 2, with terminal answer-P probabilities p_E (under P) and q_E (under Q). At J, stop and answer P at time 2, or continue to a time-3 terminal natural answer. The time-3 answer-P probabilities are `(p_B,q_B)` after the bypass route and `(p_I,q_I)` after the I route. They can differ; no decisions occur after J. All modelled natural branches have positive P and Q probabilities.

Every *individual* history arriving at I or J has likelihood ratio 1, because all pre-terminal natural branch probabilities coincide under P and Q; the two J histories really occupy the same LR decision key. The history/source labels `B` (bypass) and `I` (through continue at I) remain distinguishable to FULL. At J the BRC-style positive P/Q carriers are `m_B^P=m_B^Q=b` and `m_I^P=m_I^Q=a r(1-x)`. The latter depends on upstream action x. Carrying only their sum loses the route-conditioned terminal-answer kernels unless an exact observer-safe quotient is proved. Signed normals below are dual readouts, not signed physical probability mass.

Let `S_1=(1,0,1,1)`, `S_2=(1,0,2,2)` and `A_t(p,q)=(p,1-q,t,t)`. Define four *four-dimensional* rational/real vectors

```
E = r A_3(p_I,q_I) + (1-r) A_2(p_E,q_E)
V = a E + b A_3(p_B,q_B)
B = a (S_1 - E)
C = b (S_2 - A_3(p_B,q_B))
D = ar (S_2 - A_3(p_I,q_I))
```

B is the upstream I stop-vs-continue observer effect; C and D are the bypass and I-origin J stop-vs-continue effects, respectively. All source weights remain nonnegative; the signed vector differences arise only after applying the declared observer.

FULL uses x,u,v independently in [0,1], where u is the J stop probability on bypass, v the J stop probability after I. Seedless LR uses x,y in [0,1] and the SAME y for both histories reaching J:

```
O_FULL(x,u,v) = V + xB + uC + (1-x)vD
O_LR(x,y)    = V + xB + y[C + (1-x)D].
```

This is a genuinely causally coupled diamond: x changes the mass of I-origin J arrivals. Both maps are multi-affine in their behavioral parameters, hence each support maximum over the respective unit cubes is attained at deterministic binary parameter vertices. FULL contains every LR observation by choosing u=v=y.

## 2. Theorem: exact all-signed support formula and hull/image classification

**Theorem (real parameters, all signed directions).** For every n in R^4, put `β=n·B`, `c=n·C`, `d=n·D`, and `t_+=max(0,t)`. Then

```
h_FULL(n) = n·V + max(c_+ + d_+, β+c_+)
h_LR(n)   = n·V + max((c+d)_+, β+c_+)
Δ(n)      = max(c_+ + d_+, β+c_+) - max((c+d)_+, β+c_+) >= 0.
```

Furthermore, on the declared open natural-parameter domain, the following are equivalent:

1. The FULL and LR **four-observer convex hulls** are equal.
2. Their **actual real four-observer images** are equal.
3. The two J-origin natural terminal kernels agree: `p_B=p_I` and `q_B=q_I`.

When these two kernels differ, there is an explicitly constructible signed normal and a FULL deterministic witness with a strictly positive support advantage. For rational input parameters the normal, advantage and witness are rational, and the witness has a certified nonzero distance to the LR convex hull.

**Proof of the support formula.** At x=0, FULL independently optimizes uC+vD, contributing c_++d_+; at x=1, the I-origin J route is unreachable, and optimizing u contributes β+c_+. At x=0, LR must use one y for C+D, contributing (c+d)_+; at x=1 it contributes β+c_+. Multi-affinity proves these two x endpoints attain the global support optima. Since c_++d_+≥(c+d)_+, the displayed Δ is nonnegative for every signed n.

**Proof of sufficiency and actual-image equality.** If the J terminal kernels agree, write `Z=S_2-A_3(p_B,q_B)`. Then `C=b Z` and `D=ar Z` with b,ar>0. For any FULL x,u,v, define

```
y = [b u + ar(1-x)v] / [b + ar(1-x)] ∈ [0,1].
```

Its denominator is strictly positive. Substitution into O_LR gives exactly O_FULL, coordinate by coordinate. Reverse inclusion is immediate (take u=v=y), proving equality of **actual** observer images and thus their hulls. This is an exact observer/future-terminal-horizon fiber-constancy certificate; it does not erase path provenance before this test.

**Proof of necessity and constructive separation.** The third and fourth coordinates of C and D are respectively `(-b,-b)` and `(-ar,-ar)`, so C and D are nonzero. For them to lie on the same nonnegative ray, dividing by the strictly positive b and ar makes their time coordinates both -1, forcing equality of their first two coordinates. This is equivalent to `p_B=p_I`, `q_B=q_I`. When kernels differ, C and D are linearly independent. Select indices i<j with `H=C_i D_j-C_j D_i≠0` and define a normal supported on those coordinates by

```
n_i=(D_j+C_j)/H,   n_j=(-D_i-C_i)/H.
```

Direct substitution gives `n·C=1` and `n·D=-1`. Put β=n·B. The support formula yields the exact paired identity

```
Δ(n)  = clamp(-β,0,1)
Δ(-n) = 1-clamp(-β,0,1)
Δ(n)+Δ(-n)=1.
```

Thus at least one of n,-n has Δ≥1/2. Its maximizing FULL deterministic observation W obeys

```
dist_inf(W,conv(LR_image)) ≥ Δ / ||n||_1 ≥ 1/(2||n||_1) > 0.
```

The distance bound follows from the signed support inequality and the L1/L-infinity dual norm. This proves the contrapositive of convex-hull equality, completing all implications. The argument applies to **all real** parameter values in the declared domain; rationality is only required to make the constructed certificate rational. □

## 3. A fixed all-positive two-law family with explicit uniform gap

Fix six strictly interior natural terminal probabilities:

```
p_B=3/4, q_B=1/4;
p_I=1/4, q_I=3/4;
p_E=q_E=1/2;
0<a<1, 0<r<1.
```

For the **fixed** signed normal `n=(-7,-5,0,0)` the provenance effects satisfy

```
β=-a(1+3r) <0;    c=2(1-a)>0;    d=-4ar<0;
β+c < c+d  (because (β+c)-(c+d)=-a(1-r)<0).
```

It follows from the support formula, without sampling, that

```
h_FULL(n)=n·V+2(1-a)
h_LR(n)  =n·V+max(0,2(1-a)-4ar)
Δ(n)     =min(2(1-a),4ar) >0
```

for **every** real 0<a,r<1. The explicit FULL maximizing action is x=0,u=1,v=0; its exact L-infinity distance to conv(LR) is at least `min(2(1-a),4ar)/12`. Both natural branch pairs at the root and after I remain strictly positive throughout this open square.

### Exact rational instance and **sharp** witness distance

Take a=r=1/2. The provenance-aware affine components (coordinates eP,eQ,TP,TQ) are

```
V=( 9/16,  9/16, 11/4,11/4)
B=( 5/16, -3/16, -3/4,-3/4)
C=( 1/8,  -3/8,  -1/2,-1/2)
D=( 3/16, -1/16, -1/4,-1/4).
```

All four LR deterministic vertices `(x,y)=(0,0),(0,1),(1,0),(1,1)` are respectively

```
(9/16,9/16,11/4,11/4), (7/8,1/8,2,2),
(7/8,3/8,2,2),       (1,0,3/2,3/2).
```

They have affine rank 3 in the effective coordinates (eP,eQ,T): the determinant of column vectors B,C,D restricted to these three coordinates is **-1/64**. FULL's deterministic strategy (x,u,v)=(0,1,0) gives

```
W=V+C=(11/16,3/16,9/4,9/4).
```

For n=(-7,-5,0,0), `n·W=-23/4` and `max_LR n·O=-27/4`. The support advantage is exactly 1; since ||n||_1=12, every LR real observation, and every convex combination thereof, lies at L-infinity distance at least 1/12 from W. The **actual** LR policy `(x,y)=(0,2/3)` yields

```
Y=(37/48,13/48,9/4,9/4)
||W-Y||_inf=1/12.
```

Therefore, *without any numerical optimizer*,

```
dist_inf(W,LR_image)=dist_inf(W,conv(LR_image))=1/12.
```

This witness demonstrates a four-observer gap, with the stronger precise fact that the LR affine rank here is 3 rather than 4. The general classification is observer-space/route scoped, and does not assert a restriction on other fully four-dimensional or higher-key constructions.

## 4. Exact execution and evidence scope

The accompanying `VERIFY.py` was actually executed with Python's standard `fractions.Fraction`. It computes terminal P/Q observations directly from the physical branches *independently* of the affine-coefficient formula, checks all binary deterministic FULL/LR vertices and selected interior behavioral points, evaluates both support expressions, constructs rational paired-separation normals, verifies the identical-kernel action-aggregation formula on rational interior inputs, and checks the exact sharp witness distance. It covers a 5×5 rational grid of (a,r), plus four additional kernel sets, with **2,154 asserted exact relations** in the executable program. The actual stdout is in `EXACT_OUTPUT.txt`, ending in `PASS_EXACT_R5_CAUSALLY_COUPLED_DIAMOND_COMPLETE_CLASSIFICATION`.

The universal real-domain claims derive from the analytical multilinear-support and normal/aggregation proofs above. The finite Fraction regressions check the executable model and exact instance, not an empirical extrapolation to all real inputs. No external literature or new-native X6 transfer is claimed here.

## 5. Authority, persistence boundary and continuation

The connected GitHub user can read/write repository material, and the exact R5 PR frontier was verified before author-side publication. At this run the native Site-scoped credential reported `research_authority_granted=false`, `write_relay_enabled=false`, `configured_access_scopes=[em:access,source:read,control:read]`; a bounded native task/owner read returned `CONTROL_QUOTA`. Therefore no formal owner, new CLAIM, Source Result, mathematical review, or research-authority promotion is inferred. This proof is a portable author-side candidate for independent review and task-machine intake, not a completed mother-objective Result.

**Next:** examine *two genuinely interacting upstream controls* that modify downstream provenance at more than one shared decision key, rather than merely adding a second independent diamond. First test all deterministic FULL vertices against the exact LR vertex hull using rational convex-combination or Farkas certificates. Only with complete hull equality established, test whether any FULL real observation lies outside the real seedless LR image. Preserve the finite positive P/Q paths and actual time–likelihood-ratio key equivalence. See `NEXT_TASK.md`.
