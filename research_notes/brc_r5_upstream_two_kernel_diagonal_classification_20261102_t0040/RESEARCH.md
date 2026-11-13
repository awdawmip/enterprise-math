# R5: exact two-parameter upstream-kernel classification via triangular Bernstein certificates

**Research date:** 2026-11-02 (Asia/Shanghai). **Status:** `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. This is a finite auxiliary **two-law stopping** model with exact positive rational kernels and real behavioral probabilities; it does not identify its scalar observers with native Enterprise X6 coordinates.

## 1. Frozen science, current normative sources and frontier

Preserved immutable task-science inputs: GLOBAL_KNOWLEDGE_V1 `main@a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `main@86149263e38c22292c9def1e0f69092efa1be77e`. Immediately preceding immutable author-side frontier: Enterprise Math `640f267e209f362a80f898c20c4bc7d262e7ca0a`, `research_notes/brc_r5_upstream_j_mixture_adaptive_gap_20261101_t2340/{RESEARCH.md,VERIFY.py,EXACT_OUTPUT.txt,NEXT_TASK.md}`. Its one-parameter B-to-A upstream mixture has an adaptive all-real separation gap `29(1−lambda)` for `lambda<1`, and actual-image equality at the source-independent endpoint.

**Current normative (NOT scientific pins):** GLOBAL_KNOWLEDGE_V1 `main@17f89e662766cb9df23cf056437c156a4a5c3530`, Enterprise Math `main@94953c41b7f0a128aeb810717dbe691ae8504b90`. Read the current global `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, mathematical/code/temporal/BRC and EM activity rules, `projects/enterprise-math/00_EM_TASK_RESEARCHER_BOOTSTRAP.md`, P000 startup projection and canonical original (projection's `canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` verified), ACTIVE worldview, EM `AGENTS.md`, `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `research_priorities/research_method.json`, heartbeat and joint-relation observer contracts. P000 and protected worldview are untouched. Current authenticated GitHub user `awdawmip` has project repository write access but is not thereby an authenticated native research owner; native read query returned `CONTROL_QUOTA` and service states `research_authority_granted=false` and `executor_binding_configured=false`.

**Mother question:** Find a finite strictly positive two-law stopping model for which FULL-history and seedless time/likelihood-ratio (LR) policies have **equal four-observer convex hulls but different actual real policy images**. Local question: can making both A-source and B-source upstream J transition mechanisms independently tunable yield a genuine positive interior with that property?

## 2. Complete construction and BRC typed use

The four-vector is `O=(e_P,e_Q,T_P,T_Q)` with `e_P=P(final answer P)`, `e_Q=Q(final answer Q)`, and `T_P,T_Q` expected integer stopping time under each law. Four labeled initial sources under P/Q are `A1=A2=(1/8,1/8)`, `B=(1/4,1/8)`, `C=(1/2,5/8)`; each measure totals one. Genuine shared decision keys are `I=(t=1,P/Q LR=1)`, `J=(2,2)`, `K=(3,8/5)`, `L=(4,12/5)`; C has separate decision `(1,4/5)`. Every trajectory visits any decision key at most once. Answer actions are taken with the same P/Q behavioral probability (each actor uses a single real coin), with FULL allowed to distinguish hidden provenance, and LR constrained to a single coin for each shared `(time,LR)` key.

From A1/A2, at I stop with answer P at time1 according to `p_i`, otherwise nature produces a time2 Q answer with P/Q probabilities `(1/2,3/4)` and J arrival with `(1/2,1/4)`; at J stop answer P according to `q_i`, otherwise continue. B initially is already at J and stops answer P at time2 with `q_B`, otherwise continues. C at `(1,4/5)` stops answer Q at time1 with `r` or answer P at time3 with `1−r`.

For each A-source reaching and continuing J, a **law-independent** nature coin chooses conditional **A-kernel with probability `u`** and **old B-kernel with probability `1−u`**. B chooses A-kernel with `v` and old B-kernel with `1−v`, where `0<u,v<1`; boundary values are used as polynomial interpolation only. A-kernel: at time3 natural Q termination with conditional P/Q probabilities `(3/5,1/2)`; residual masses `(2/5,1/2)`, then time3 natural P termination with `(1/2,1/2)`; residual to shared K using behavioral coin `k`, which answers P at time3 or continues. After K continuation, time4 natural Q termination P/Q `(1/4,1/2)`; residual goes to shared L, whose behavioral coin `l` answers P at time4 or Q at time5. Old B-kernel: at time4 natural terminal-vs-L branching with P/Q probabilities `(2/5,1/2)` and `(3/5,1/2)` respectively. Immediate terminal answer is P with chance `1/4`, Q with chance `3/4` under each law. L uses the same answer/time choice as in A-kernel. Every listed conditional nature edge is strictly positive for interior `u,v`; all P/Q terminal masses are normalized exactly by `VERIFY.py`.

For **admissible source-dependent FULL policies**, the twelve coins are `(p1,p2,q1,q2,qB,r,k1,k2,kB,l1,l2,lB)`; FULL may additionally distinguish any available nature history, but our explicit source-dependent witnesses already belong to FULL. LR coins are `(p,q,r,k,l)` with the equalities `p1=p2=p`, `q1=q2=qB=q`, `k1=k2=kB=k`, `l1=l2=lB=l`. Each LR real observation is multi-affine in its five behavioral probabilities, so its convex hull is **exactly** the hull of the `2^5=32` deterministic LR vertices (no requirement that the actual real LR image itself be convex).

**BRC reuse:** positive labeled exact rational P/Q branch mass is the carrier; source, kernel-choice, path and conditional-law labels remain distinct until the declared four-coordinate observer is computed. The `N·O` signed facet below is a dual comparison **of completed positive-flow observables**, *not* a signed BRC branch mass. The safe source quotient at `u=v` is certified for these four observers and the whole remaining conditional time/answer future, not assumed from equal aggregate initial masses. There is no claim of native X6, BRC–Shor, or heartbeat residual arithmetic.

## 3. Main theorem: equal convex hull if and only if source kernels coincide

**Theorem (all real u,v in the closed interpolation square).** Let `F(u,v)` denote the full four-observer actual real image (including all allowed history-dependent FULL policies), and `R(u,v)` the corresponding seedless LR actual real image. For all `u,v∈[0,1]`:

1. If `u=v`, then **`F(u,u)=R(u,u)` as actual real sets**, and therefore their convex hulls are equal.
2. If `u>v`, define

   `N_>(u,v) = (3270−275u−1195v, 2256+80u−1256v, 615+100u+635v, −672+70u−658v)`.

   Take LR deterministic reference `(p,q,r,k,l)=(0,1,1,0,1)` (lexicographic bit index 13), and the admissible FULL deterministic witness `(p1,p2,q1,q2,qB,r,k1,k2,kB,l1,l2,lB)=(0,0,1,1,0,1,1,1,0,1,1,1)`. Then for every real LR policy `x`:

   `N_>(u,v)·O_LR(x) ≤ N_>(u,v)·O_LR(0,1,1,0,1)`, whereas

   `N_>(u,v)·[O_FULL(witness)−O_LR(0,1,1,0,1)] = (735/8)(u−v)>0`.

3. If `u<v`, define

   `N_<(u,v) = (3270−490u−980v, 2256−392u−784v, 615+245u+490v, −672−196u−392v)`.

   Take LR reference `(1,1,1,0,1)` (index29) and FULL witness `(0,0,0,0,1,1,0,0,1,1,1,1)`. Every LR real observation lies at or below the reference on `N_<`, while the FULL witness exceeds it by `(735/8)(v−u)>0`.

It follows that **`conv(F(u,v)) = conv(R(u,v)) ⇔ u=v`** on the entire square, and whenever equal, the actual real images are equal as well. For every `u≠v`, the corresponding explicit FULL witness W satisfies the certified quantitative bound

`dist_infinity(W,conv(R(u,v))) ≥ (735/8)|u−v| / ||N_{>/<}(u,v)||_1 ≥ (245/18168)|u−v|`.

Here `||N_>||_1=6813−165u−1158v≤6813`, `||N_<||_1=6813−441u−882v≤6813`; their first three coefficients are strictly positive and fourth strictly negative throughout the closed square. These are explicit **lower bounds** on the full signed support gap, not claims to have maximized over every FULL history policy. Thus the **strictly positive** interior `(0,1)^2` has no solution to the mother counterexample within this specific two-parameter mechanism.

## 4. All-real exact LR facet certificate

Set `S_>={(u,v):0≤v≤u≤1}` and map `[0,1]^2∋(s,t)↦(u,v)=(s+(1−s)t,s)`; similarly `S_<` via `(u,v)=(s,s+(1−s)t)`. Each is covered by the closed unit square. For fixed deterministic LR bits `b`, `O_b(u,v)=U_b+u V_b+v W_b`: every finite path reaches the upstream J mixture at most once. The two normals are affine in `(u,v)`, so the LR facet slacks after the triangle substitution

`D_b(s,t)=N(u,v)·[O_LR(facet;u,v)−O_LR(b;u,v)]`

are real bivariate polynomials of degree at most **2 in each** of `s,t`. Each has an **exact tensor degree-(2,2) Bernstein representation**

`D_b(s,t)=Σ_{i=0}² Σ_{j=0}² C_{ij}(b) B_i²(s) B_j²(t)`, `B_i²(x)=binom(2,i)x^i(1−x)^(2−i)`.

All 9 coefficients for each deterministic LR bit string are computed exactly from the 3×3 grid `(0,1/2,1)²`; for a univariate degree≤2 polynomial with values `(f0,fhalf,f1)`, its Bernstein controls are `(f0,2 fhalf−(f0+f1)/2,f1)`. `VERIFY.py` enumerates **all 32 bit strings in each triangle** and verifies **all 2×32×9=576 rational controls are nonnegative** (156 and 176 zero controls respectively); no floating tolerances or unexamined LR policies. Since every Bernstein basis function is nonnegative on `[0,1]`, the proposed reference LR vertex maximizes the signed support throughout its entire real parameter triangle. Because each LR behavioral observation is a convex combination of its 32 deterministic observations by multi-affinity, this proves the asserted bound for **all real LR behavioral probabilities**, not only deterministic strategies.

For the FULL witness minus the LR reference, the code compares **all nine** tensor Bernstein controls against the exact polynomial `(735/8)(u−v)` (or reverse difference) after the appropriate triangle map, proving those algebraic identities on the full real triangle. The polynomial-degree argument is essential: no finite point sampling is used as a universal conclusion without it.

## 5. The diagonal is actual-image Markovization, not merely hull equality

At `u=v=w`, J has the **same full conditional P/Q mixture kernel** for all source histories arriving at J. At each K or L decision key, conditional future transitions and final answer/time rules are also source independent. In particular each arrival fiber at a genuine key `(t,r)` has the exact positive relation `dP=r dQ` under both laws. Given **any** FULL real history policy, aggregate its Q arrival/action mass by action at the next key; choose the LR action coin equal to `Q(action)/Q(total)`, arbitrary on zero-Q-mass keys. The corresponding P action mass is automatically `r` times its Q mass. The source-independent conditional kernels then propagate the same terminal-answer and stopping-time P/Q flows to the next keys. Induction through the finite acyclic graph I,J,K,L, plus separate C, matches all four observers. Conversely every LR policy is an admissible FULL policy. Hence `F(w,w)=R(w,w)` for all **real** `0≤w≤1`.

For additional reproducible checks, `VERIFY.py` implements explicit Q-mass Markovization for arbitrary twelve source-only behavioral coins and executes 9 exact rational tests at `w=1/4,1/2,3/4`; these finite cases check formulas but **the universal proof is the fiberwise induction**. Full policies may use more history than the twelve source-only bits; this does not weaken the diagonal induction, nor the off-diagonal explicit witness, which is a member of FULL by construction.

## 6. Concrete strictly-positive instances, verification, and next question

At `(u,v)=(3/4,1/4)`, the first FULL witness exceeds the **whole LR hull** in the signed direction by `735/16`, with `||N_>||_1=25599/4`, giving an exact `L∞` distance lower bound `35/4876`. At `(1/4,3/4)`, the second witness gives the same support margin `735/16`, `||N_<||_1=24165/4`, and distance lower bound `49/6444`. At `(1/2,1/2)` every nature route is strictly positive and, by the induction above, the two **actual** real images coincide.

`VERIFY.py` is standalone Python 3 standard library `fractions.Fraction`: it computes mass-normalized P/Q flow, 576 exact LR Bernstein control signs, 18 full-vs-LR witness identity controls, 3 sample gap/norm/distance calculations, and 9 rational diagonal Markovization tests. Its actual run is preserved in `EXACT_OUTPUT.txt`. The exhaustive finite 32-vertex calculation is a **universal** result only because the explicitly proved multi-affinity and degree-(2,2) exact interpolation cover the full real policy/parameter domains. All proof steps can be independently checked from the source; no symbolic algebra library, scipy solver, floating sample, or independent reviewer is assumed in the final trust basis.

**Scientific outcome:** independent tuning of both A and B at the J kernel **does create a new two-dimensional strictly positive parameter family**, but full four-hull equality still occurs only on the **source-blind diagonal**, where the actual real images are equal as well. This is a precise exclusion of *this construction*, while the original mother objective remains open for other upstream topologies or observers.

**Next smallest unit:** Add a genuinely independent early source route feeding a shared key, rather than making all existing sources mixtures of the same two J kernels. First seek a parameter point with complete all-signed four-hull equality using 32 LR reference vertices and exact rational convex combinations/Farkas separators; if it passes, prove (non)membership of a specific actual real FULL observer via exact semialgebraic means. Preserve exact BRC source labels and truthful owner/claim/admission state. Do not repeat the now classified `(u,v)` family.
