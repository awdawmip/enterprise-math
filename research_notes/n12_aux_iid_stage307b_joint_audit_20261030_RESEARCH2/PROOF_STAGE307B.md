# Stage307-B.1 — exact all-horizon source/J audit and a certified public–joint tradeoff

**Scientific status:** PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This note solves the *joint-audit* part of Stage307-B and a strict, certified portion of the Pareto question. It does **not** solve Stage306-B's two-real-variable algebraic public minimizer or the complete Pareto frontier. It is an external finite positive-branch BRC observer model, not a native P000 X6 theorem.

**Fixed input:** GLOBAL_KNOWLEDGE_V1 main `2a62d4bc3e5188d71a51f2b832fd0a94950a03df` (canonical bootstrap/manual, ACTIVE worldview, P000 V4 original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, role and math/BRC policies); Enterprise Math main `902ddf2a69c5b369e19d961751af144c7d94072e` (P000 V5 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, X6/time, joint-preservation, portable research); predecessor immutable Stage306-B `e6801c19582e0a91be182fb49561f685b08cc403`. The two P000 sources are distinguished by repository/version, not conflated. Source ownership was not confirmed: native owner list returned CONTROL_QUOTA; Sites gateway `research_authority_granted=false`. No CLAIM or admission is inferred.

## 1. Frozen model and exact positive branch table

Let S be fair on {0,1}. Given S=s, J,W,Y are mutually independent; P(J=s|S=s)=7/8, P(W=s|S=s)=3/4, and P(Y=1|S=s)=p_s with p_0=1/4,p_1=3/4. J and S are hidden from the public examiner, who does see G=(W,Y). For each private history h=(J,W,Y), the compressor chooses one real t_h in [0,1] and locks it through all n future F visits; its F outputs are conditionally IID Bern(t_h) given h. The ideal F outputs are conditionally IID Bern(p_S). Operation H yields an independent fair bit. At every round the public examiner may adaptively choose F or H from the visible history, never from hidden S,J. The terminal **joint** audit additionally reads the original S,J; the public audit does not. Both retain G and complete ordered actions/outputs.

Write a_h=P(S=0,h), b_h=P(S=1,h), m_h=a_h+b_h. Exact branch accumulation gives (a_h,b_h) numerators over 256:

| (J,W,Y) | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 256a_h | 63 | 21 | 21 | 7 | 9 | 3 | 3 | 1 |
| 256b_h | 1 | 3 | 3 | 9 | 7 | 21 | 21 | 63 |

Every original branch has strictly positive rational mass. All source-label provenance is retained before taking the declared public quotient.

Define `D_n(u,v)=TV(Bern(u)^⊗n,Bern(v)^⊗n)` and `D_n=D_n(1/4,3/4)`.

## 2. The all-adaptive reduction (both audit scopes)

For fixed t_h and a fixed public history-dependent H/F policy, independently presample n potential F bits and n independent fair H bits. The complete experiment (S,J,G,F_1,...,F_n,H_1,...,H_n) maps to the actual adaptive trace by **one common Markov kernel**: the kernel uses the policy and consumes the next unused bit of the chosen operation. Conditional on (S,J,G), this is true in both the ideal and locked-rate systems. Therefore TV contracts under this kernel, including when the final output retains S,J. Policy F at every round is legal and reveals all n potential F bits. Tensoring an independent H sequence changes no TV. Hence, for every fixed rate table, the maximum TV over **all randomized public-history adaptive H/F policies** is exactly the corresponding always-F audit TV. This is not an enumeration-only inference.

## 3. General n theorem: exact joint (S,J) audit minimax

The always-F joint risk for rate table t is

`T_n(t)= Σ_h [a_h D_n(p_0,t_h)+b_h D_n(p_1,t_h)]`.

The TV triangle inequality implies, for arbitrary positive a,b and any t,

`a D_n(p_0,t)+b D_n(p_1,t) ≥ min(a,b) D_n(p_0,p_1)`.

For a>b, subtracting the lower bound leaves at least `(a-b)D_n(p_0,t)`; the symmetric case has at least `(b-a)D_n(p_1,t)`. Equality is attained by choosing the rate of the more likely S. Since n≥1 makes `D_n(p_s,t)=0` iff t=p_s and every table row has a≠b, the minimizing table is **unique**:

`t_h^MAP=p_0 if a_h>b_h; else p_1.`

The table has `Σ_h min(a_h,b_h)=7/64`. Thus, over the *entire continuum* of locked deterministic real rates and simultaneously over all adaptive public policies,

**`T_n^* = (7/64) D_n,qquad n≥1.`**

For the symmetric Bernoulli pair the exact closed formula is

`D_n = 4^(-n) Σ_{0≤k<n/2} binom(n,k)(3^(n-k)-3^k)`,

where the middle term for even n is absent because it cancels. Therefore `D_1=D_2=1/2`, `D_3=D_4=11/16`, and `D_n→1` by the elementary binomial law of large numbers (or a Chernoff bound). In particular:

**`T_3^* = (7/64)(11/16)=77/1024`**, strictly larger than the Stage306 one-F optimum `7/128`, and `lim_n T_n^*=7/64`.

Scope note: the theorem assumes a single deterministic real rate per h, fixed for n visits, with no fresh random rate mixture, hidden-S reading or parameter reset. It does not assert the same minimax for an enlarged implementation class.

## 4. Exact public observer at the uniquely joint-optimal table

Call the public always-F risk `P_n(t)`. For G=00 and G=11, the unique MAP table sets both J rates to the majority source rate; in each outer fiber the minority source posterior is 1/10 and the fiber mass is 5/16. Thus each outer fiber contributes `(5/16)(1/10)D_n=D_n/32`. For G=01 and G=10 the MAP table's J mixture equals the ideal S mixture exactly, so these fibers contribute zero. Hence:

**`P_n(t^MAP)=D_n/16`, and specifically `P_3(t^MAP)=11/256.`**

By Stage306-B's certified continuum feasible point, `P_3^*≤0.007558267237944884 < 1/128 < 11/256`. Consequently **no rate table jointly minimizes the public and (S,J) audit risks**.

## 5. Exact quantitative public–joint outer tradeoff inequality

Let `d_h=D_n(t_h,t_h^MAP)`. The weighted triangle proof gives

`T_n(t)-T_n^* ≥ Σ_h |a_h-b_h| d_h.`

The public TV reverse triangle inequality and data processing through deletion of S,J give

`P_n(t) ≥ P_n(t^MAP)-Σ_h m_h d_h.`

Since the exact branch table has `min_h |a_h-b_h|/m_h=1/8`, every real locked-rate table satisfies the certified one-sided Pareto **outer bound**

**`T_n(t) ≥ (7/64)D_n + (1/8)max{0, D_n/16-P_n(t)}.`**

In particular, when n=3 and `P_3(t)≤1/128`, one obtains `T_3(t)≥163/2048`, whereas the joint minimax equals `154/2048`. This is a rigorous strictly positive `9/2048` joint penalty for the entire near-public-optimal band, not an assertion of the complete frontier.

An exact feasible tradeoff witness sets the outer G=00 rates to `(t_{J=0},t_{J=1})=(1/4,1/2)`, outer G=11 rates to `(1/2,3/4)`, and leaves the middle fibers at t^MAP. It yields **`(P_3,T_3)=(3/128,165/2048)`**, compared with the joint-MAP point **`(11/256,77/1024)`**. The first point is feasible but is **not claimed Pareto-efficient**.

## 6. Executed verification, reuse, and limits

`REPRO_STAGE307B.py` uses only standard-library `fractions.Fraction`. It reconstructs all 16 positive source/label/side-signal branches, the 8-row exact table, the closed-form D_n values for n=1,...,9, the unique MAP table and both claimed 3-visit points. For each point and each audit scope it enumerates all 128 deterministic public binary-history H/F policies within each of the four G fibers (512 policies per observer) and checks that all-F attains the fiber maximum. Actual stdout ends `STAGE307B_TAGGED_ALL_HORIZONS_AND_PARETO_EXACT_PASS`. General n and continuous-domain claims are **proved above** and not inferred from the n≤9 finite checks.

BRC reuse decision: `REUSE_APPLIED` to typed finite positive-rational explicit-branch accumulation and declared observer quotients in `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json` (blob `f375a059fa4af8c6eefaddb4d4a8689a0c063674`). A total-only mass summary cannot recover S/J joint TV, so the full branch labels and their conditional ports must be retained. The simple independent rational verifier does not claim native X6 execution. It neither modifies the protected P000 premise nor proves the external probabilistic model is an X6/BRC dynamics theorem.

Author identity: this ChatGPT automation's local portable-research author context (GitHub authenticated login `awdawmip`); NOT a native service session/researcher/CLAIM, NOT independently reviewed or admitted. The native Sites gateway returned `research_authority_granted=false`; current owner lookup returned `CONTROL_QUOTA` and hence no authoritative active owner was established.

## 7. Exact next question

Stage307-B.2: derive an isolating, globally excluding algebraic certificate for Stage306's two-rate public minimizer `d(x,y)`, including testing `r_0=r_1=0`; then seek a *sharp* public–joint Pareto frontier instead of only the outer bound/feasible points supplied here. Native P000-X6 joint-observer transfer needs a separately typed mapping of six-axis paths, triadic closure, time and Cell addressing and is not inferred from this external model.
