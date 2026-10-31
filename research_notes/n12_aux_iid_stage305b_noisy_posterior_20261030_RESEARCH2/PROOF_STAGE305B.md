# Stage305-B — noisy revelation, two-visit exact repair, and a third-moment obstruction

**Author status (2026-10-30):** `PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

**Input pins:** `GLOBAL_KNOWLEDGE_V1 main@8a90490344dbf310db7764d8c53cb8274f0cd904` (verified `main` branch); Enterprise Math control `main@5256fc460df9a8dd3cc0945999ac56830d42582b` (verified `main` branch); exact previous scientific frontier Stage304-B `3ab137c9f602101564cc0fce2be1c87d301d02a4`, `research_notes/n12_aux_iid_stage304b_source_revelation_20261030_RESEARCH2/PROOF_STAGE304B.md`, blob `f058746b171a313c8bd7b31b2388fe720df0fc08`. Project original `p000_reality_foundation.json` blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488` (`ENTERPRISE_MATH_P000_REALITY_FOUNDATION_V5`); ACTIVE Heartbeat X6/time and mandatory joint-observer/residual constraints were read at the frozen project pin. Direct research is portable author mathematics, not execution under a native Task CLAIM.

## 1. Typed positive-rational model and observation language

We work **outside the P000-X6 native dynamics** with a finite BRC-style positive branch family. Let the original externally existing source be a fair bit `S∈{0,1}`. Conditional on `S=s`, three independent devices produce:

- a persistent *old* label `J` with `Pr(J=1|S=0)=1/8`, `Pr(J=1|S=1)=7/8`;
- a later noisy revelation `W` with `Pr(W=S|S)=3/4`;
- the immutable first F-output `Y1 ~ Bern(p_s)`, with `p_0=1/4` and `p_1=3/4`.

All four variables are retained as separate provenance fields. Their 16 branch masses are strictly positive rational numbers. The unnormalized prefix mass is

`w_{s,j,w,y}=(1/2) Pr(J=j|S=s) Pr(W=w|S=s) Pr(Y1=y|S=s)`.

The physical prefix is **shared identically** by the ideal process and all three repairs below; repair starts only after `W,Y1` become known. The repair controller can read `(J,W,Y1)` but **not** `S`. The external examiner can read `(W,Y1)`, previous actions and outputs; it cannot read `S` or `J` during the subsequent two rounds. In each subsequent round it chooses an `F` visit or an `H` visit, possibly randomized using independent private coins; `H` yields an independent fair bit and never updates belief about `S`. Under the ideal process, every `F` visit is a new conditionally independent `Bern(p_S)` bit. Action labels and output order are always retained. At the **end**, the audit observer may additionally read `J_old`, `S` or both, without changing which actions were available earlier.

Observers:

- `O_W=(W,Y1, ordered actions/outputs)`;
- `O_J=(J_old,W,Y1, ordered actions/outputs)`;
- `O_S=(S,W,Y1, ordered actions/outputs)`;
- `O_SJ=(S,J_old,W,Y1, ordered actions/outputs)`.

Risk `R_O(Q) = sup_{π} TV(Law_O(P^π),Law_O(Q^π))`, with `TV(P,Q)=1/2 Σ|P-Q|`. The supremum ranges over all randomized public-history causal policies `π`, including all deterministic history trees. The source-conditioned model has no signed amplitudes, `X6` increments, phase or native `E` triadic dynamics.

Write `h=(j,w,y)`; `m_h=Σ_s w_{s,h}`, `u_h=Pr(S=1|h)=w_{1,h}/m_h`, `\bar p_h=(1-u_h)/4+3u_h/4=1/4+u_h/2`. The full eight histories and posterior values are:

| `(J,W,Y1)` | `m_h` | `u_h` |
|---|---:|---:|
| 000, 111 | `1/4` each | `1/64`, `63/64` respectively |
| 001, 010, 101, 110 | `3/32` each | `1/8`, `1/8`, `7/8`, `7/8` respectively |
| 011, 100 | `1/16` each | `9/16`, `7/16` respectively |

The public prefix `g=(W,Y1)` has masses `Pr(g=00)=Pr(g=11)=5/16`, `Pr(g=01)=Pr(g=10)=3/16`. Its posterior `u_g=Pr(S=1|g)` is respectively `1/10,1/2,1/2,9/10`; the conditioned private-label probability `α_g=Pr(J=1|g)` is `1/5,1/2,1/2,4/5`.

## 2. Common-kernel minimax lemma for two future rounds

**Lemma 305.1 (all F is sharp for the declared observer set).** Consider any repair whose distribution of its *two potential future F bits*, conditional on the full shared prefix `(S,J,W,Y1)`, is fixed before the examiner's choices and does not depend on how the examiner chooses H/F. This includes the three models below, with any explicitly declared feedback law for successive F observations. Assume H innovations and policy coins are common independent fair/random sources. Then for each `O∈{O_W,O_J,O_S,O_SJ}`,

`sup_π TV(P_O^π,Q_O^π) = TV(P_O^{FF},Q_O^{FF})`.

**Proof.** Pre-generate the pair of potential F innovations, and independently the fair innovations that a policy may consume at H visits. A common stochastic kernel (same for ideal and repair) takes the prefix, those innovations and the examiner's coins to the ordered action/output trace. This kernel uses only `(W,Y1)`, the visible action history and generated outputs for action selection, and reproduces the repair's conditional law even when its second F parameter is updated after observing the first F output. Data processing bounds policy TV by the TV of the prefix plus both potential F innovations, with the requested terminal audit fields appended. The FF policy uses both F innovations directly and preserves their order and each retained prefix/audit field, attaining that bound. Randomized policies use the same common kernel with their private coins. QED.

In particular, there are `8` local deterministic choices for two rounds at each of four public `(W,Y1)` histories: `2` choices for the second action and `2^2` choices for the final action conditional on the second output. Hence `8^4=4096` complete deterministic public policy trees; their exact maxima can also be checked by independent local TV calculations.

## 3. Posterior-mean IID freeze: positive rational, sharp failure

**Interface M:** the controller reads `h`, computes `\bar p_h` once, then each post-revelation F call uses a fresh conditionally independent `Bern(\bar p_h)` coin. It does not update after the first new F output. The prefix remains exact.

**Theorem 305.2.** The exact two-round all-adaptive worst-case risks are

`R_W(M)=R_J(M)=651/16384`, and `R_S(M)=R_SJ(M)=3255/32768`.

**Proof.** Fix `h`, let `u=u_h`. The ideal potential F pair has distribution

`P_h=(1-u) Bern(1/4)^{⊗2}+u Bern(3/4)^{⊗2}`.

For `t=\bar p_h`, `Q_h=Bern(t)^{⊗2}`. Writing `v=u(1-u)(3/4-1/4)^2=u(1-u)/4`, the ordered differences `P_h-Q_h` for `00,01,10,11` are `(v,-v,-v,v)`. Therefore conditional TV is exactly `2v=u(1-u)/2`. The signs are the same for every `h`, so marginalizing `J` cannot cause cancellation in any fixed public `(W,Y1)` fiber. The full weighted sum is `Σ_h m_h u_h(1-u_h)/2=651/16384`, both for O_W and O_J. The remaining source-tagged sums are exact finite rational sums over all 64 fully labelled FF paths and give `3255/32768` for either O_S or O_SJ; the executed Fraction program checks every term and all 4096 policies. Lemma 305.1 proves the stated supremum. QED.

Thus getting **every single next F marginal** exactly correct after a noisy revelation does *not* preserve the two-visit joint law: the missed conditional covariance is `v>0` on every positive history. This is an explicit positive-rational failure, not a finite-grid approximation.

## 4. Two different exact repairs, and what their auditors retain

**Interface B (sequential Bayes):** choose the next F rate `\bar p_h`; after observing an actual F bit `z`, update `u_h` by Bayes' formula using `p_0,p_1`, then use `1/4+u_{h,z}/2` for the next F. H visits do not update the posterior. By the chain rule, this simulates the exact ideal *mixture* distribution of any visible F sequence. For the two future rounds:

`R_W(B)=R_J(B)=0`, whereas `R_S(B)=R_SJ(B)=651/8192`.

For the tagged formula, conditional on `h`, the simulator's pair is the source-pooled `P_h` independent of the real, still-existing `S`; the ideal pair conditional on `S=s` is `Bern(p_s)^⊗2`. Let `D_2=TV(Bern(1/4)^⊗2,Bern(3/4)^⊗2)=1/2`. The tagged TV at `h` is `2u(1-u)D_2=u(1-u)`; summing gives `651/8192`. Thus a predictive posterior is sufficient for **pooled** public traces but not for auditing the association of old source and future results.

**Interface T (private-label two-moment repair):** keep the original persistent J and, using only J and public `(W,Y1)`, assign the following positive rational locked F rate for the two future visits:

| public `(W,Y1)` | `t(J=0,g)` | `t(J=1,g)` |
|---|---:|---:|
| `00` | `9/40` | `3/5` |
| `01` or `10` | `1/4` | `3/4` |
| `11` | `2/5` | `31/40` |

Let `α=Pr(J=1|g)` and `u=Pr(S=1|g)`. The following *both* hold for each of the four public histories:

`(1-α)t_0+αt_1=(1-u)p_0+up_1`;

`(1-α)t_0²+αt_1²=(1-u)p_0²+up_1²`.

For two Bernoulli outputs with a shared latent rate, the exact ordered four-path probabilities are determined by the first two moments (`P11=m2`, `P10=P01=m1-m2`, `P00=1-2m1+m2`). The two equations imply identical joint laws conditional on every public `g`. Hence **for every publicly adaptive two-round policy, `R_W(T)=0`**. This is an explicit rational hidden-label repair with fixed conditional IID outputs: sequential posterior updating is *not* necessary for this two-visit public observer and this particular prefix distribution.

The same repair carries distinguishable latent source/history relations. Exact terminal-audit minimax values over the same 4096 policies are

`R_J(T)=111/1600`, `R_S(T)=5487/102400`, `R_SJ(T)=549/6400`.

These are finite exact summation results, not assertions that T is optimal for any of the tagged metrics. In particular, the auditor is reading the *original* J; replacing it with a reconstructed new source label would change the observation language. The numbers demonstrate strict failure of source/audit preservation despite `R_W=0`.

## 5. A third F visit detects the missing moment

**Theorem 305.3 (finite-horizon obstruction).** Extend Interface T unchanged to **three** subsequent IID F visits. Its first two conditional public moments still match the ideal for every `g`, but the third moment discrepancy `Δm_3=m_3^ideal-m_3^T` is:

`Δm_3(00)=63/16000`, `Δm_3(01)=Δm_3(10)=0`, `Δm_3(11)=-63/16000`.

Consequently, the complete ordered **public** three-F distribution has sharp exact discrepancy

`TV(P^{FFF}_{O_W},Q^{FFF}_{O_W})=63/6400`.

**Proof.** For a shared-rate mixture, a specific ordered triple with k successes has mass `E[T^k(1-T)^{3-k}]`, a polynomial in moments through order three. When moments of orders 0,1,2 agree, each of the eight ordered words has signed difference `±Δm_3` (the sign depends on k). Therefore the conditional TV is `4|Δm_3|`. Direct substitution into the four displayed rational rate rows yields the claimed third moments. Only `g=00,11` contribute; each has mass `5/16`, so `2·(5/16)·4·(63/16000)=63/6400`. QED.

This finite example exposes a *horizon-dependent* residual: the same private one-bit J plus locked rate repairs **all** two-visit public traces but fails by an explicit third-moment gap at three visits. It does **not** prove impossibility for every alternative 1-bit repair at horizon three; that is a separate Stage306-B optimization problem.

## 6. Optional exact optimal single locked rate under J-auditing

**Theorem 305.4.** Allow any real parameter `t_h∈[0,1]` for each full controller history `h`, but require the two future F emissions to be IID conditional on that fixed `t_h`. The observer reads `J` terminally (`O_J`); S stays hidden. The sharp optimum over **all such rules** and all adaptive policies is

`R^*_{fixed-IID,J}= -89/64 + sqrt(142)/16 + 3sqrt(2)/8 + sqrt(22)/32 ≈ 0.0310540338727043765`.

**Proof.** Conditional on `h` let `u=u_h`. The ideal ordered pair masses are `a=(9-8u)/16` for 00, `b=(1+8u)/16` for 11 and `c=3/16` for each mixed word. The fixed-IID pair has masses `(1-t)^2, t^2, t(1-t), t(1-t)`. Define `t_0=1-√a` and `t_1=√b`. For `0<u<1`, `t_0<t_1`, both in `[1/4,3/4]`. On `[t_0,t_1]` both diagonal discrepancies are nonnegative and both mixed discrepancies are nonpositive; TV there is `2[t(1-t)-c]`, a concave function, minimized at an endpoint. For `t<t_0` the 11 event supplies a lower bound `b-t²≥b-t_0²`; for `t>t_1` the 00 event supplies `a-(1-t)²≥a-(1-t_1)²`. Thus an endpoint is globally optimal. Comparing the two endpoint values gives `R_0-R_1=2(√a-√b)(1-√a-√b)`, which selects `t_0` when `u≤1/2` and `t_1` when `u≥1/2`. The resulting exact per-history minimum is

`r_*(u)=v-3/2+(1/2)√(9-8v)`, where `v=min(u,1-u)`.

There are three symmetric posterior groups: `v=1/64` of combined mass `1/2`, `v=1/8` of combined mass `3/8`, and `v=7/16` of combined mass `1/8`. Weighting `r_*` by these masses gives the displayed radical expression. Lemma 305.1 establishes simultaneous optimality for all future policies using one locked parameter per full history. Endpoints `u=0,1` follow by continuity. QED.

This improves on the forced one-step calibrated mean rate (`651/16384≈0.0397338867`) when auditing J, but the exact public-only observer can do better using Interface T (zero). Consequently, **observer type, time horizon and permitted parameter updates are all part of the compression theorem**.

## 7. Actual verification and scientific boundary

`REPRO_STAGE305B.py` uses exact `fractions.Fraction` arithmetic for all branch probabilities and output TV, and symbolic `sympy` only to cross-check the radical closed form. It constructs the 16 positive prefix branches, enumerates all 8 local deterministic history trees per public prefix, exhaustively maximizes over `8^4=4096` full deterministic policies for each of the 3 repairs × 4 observers, checks all displayed rational risks, verifies first/second/third moment equalities and computes all 32 public FF-three-bit paths. Actual executed stdout is preserved in `REPRO_STAGE305B_EXECUTED_STDOUT.txt`, terminating in `STAGE305B_NOISY_POSTERIOR_MOMENT_EXACT_PASS`. The proof establishes the arbitrary randomized policy extension by common-kernel data processing, and the arbitrary-real locked-rate optimum by the algebraic argument—not by grid search.

BRC applicability: branch identity `S,J,W,Y1`, ordered operation labels, positive rational mass, source-conditioned versus source-pooled observations, and explicit retained/erased residual are declared. The mathematics is compatible with the **information-preservation discipline** of BRC but does not evaluate a typed native BRC amplitude/kernel or prove a P000-X6 realization. The required native commuting mapping remains open: signed six-component chart-relative displacements, individually typed one-axis steps, provenance/multiplicity and triadic E closures, native 3-dimensional slice with explicit third coordinate, time distinct from the six axes, and registered lossless six-nonnegative-field Cell addressing. P000 remains unchanged; no physical law, novel general information-theory principle, formal native Result or independent Driver acceptance is claimed.

**Authority checked on 2026-10-30:** Sites status `research_authority_granted=false`, `write_relay_enabled=false`, `backend_connected=false`; bounded native owner/task read returned `CONTROL_QUOTA`. The true active owner is therefore `UNVERIFIED`. This document is direct portable researcher-authored proof/verification, not a live Source CLAIM/Result. Main vs branch publication and local activity checkpoint statuses must be reported from real post-write receipts rather than inferred from this text.

**Next exact mathematical question:** Stage306-B: for noisy `(W,Y1)` prefix and persistent J with rates permitted to depend on `(J,W,Y1)` but remaining conditionally IID, determine the **sharp** horizon-three public minimax TV over all real choices of two rates per public history; decide whether the exhibited `63/6400` is optimal or strictly improvable, and separately characterize the source/J joint-audit tradeoff. Continue the independent typed native X6/BRC commuting-square proof only with a declared native carrier and operation.
