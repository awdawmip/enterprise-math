# Stage228–230: exact all-real minimax intervals and the first multitie optimal-face proof

**Status:** `PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`. **Model:** external finite ternary-IID sequential decision problem, **not** a theorem about P000-native X6 Cell evolution. This note preserves the Stage227 author-side frontier and does not claim formal canonical Task ownership, Source Result, or independent Driver acceptance.

## 1. Frozen model and universal certificate

At most `N=14` observations are allowed. Under the two hypotheses the IID symbol laws are

\[
P=(3,1,20)/24,\quad Q=(2,2,20)/24.
\]

An arbitrary randomized stopping/decision policy may depend on the **entire ordered history** and its private randomness. Let `eP=Pr_P(decide Q)`, `eQ=Pr_Q(decide P)`, and `tP,tQ` be the corresponding expected observation counts. The target is

\[
V_{14}(\alpha)=\inf_{e_P,e_Q\le\alpha}\max(t_P,t_Q).
\]

At count-state `s=(n,a,b)` (`a` counts symbol 0, `b` counts symbol 1, the remainder counts symbol 2), every ordered prefix has likelihood ratio `Q(prefix)/P(prefix)=2^(a+b)/3^a`. For `K>0` define the exact rational Bellman function

\[
B_K(s)=\min\left\{ K\frac{2^{a+b}}{3^a}\ [\text{decide P}],\quad K\ [\text{decide Q}],\quad 1+\sum_{j=0}^2 P_j B_K(s+j)\ [\text{continue}]\right\}
\]

(the continue action is not offered when `n=14`). Write `H_K=B_K(0,0,0)`. Conditioning on the first action, and expressing each Q-weighted error in P-prefix units, proves for **every** full ordered-history randomized policy

\[
 t_P+K(e_P+e_Q)\ge H_K, \qquad V_{14}(\alpha)\ge H_K-2K\alpha. \tag{1}
\]

No count-state sufficiency for arbitrary policies is presumed in deriving this inequality; the count-state recursion is a dual lower bound. Each witness below follows only Bellman-minimizing actions and has `eP=eQ=alpha`, `tP>tQ`, so equality holds in (1) for its `alpha`.

Every exact computation here uses rational numbers (`fractions.Fraction`). The **independent primal checker** visits unmerged ordered observation histories with two positive integer P/Q prefix branch masses; only on stopping is the common denominator `24^14` applied. This preserves the typed distinction between observation histories and a count-state reduction, and reuses the BRC-compatible integer branch/provenance technique within this **external** auxiliary model.

## 2. Stage228: ordinary two-tie interval

Parent author frontier (Stage227):

\[
\alpha_{227}=\frac{938194997485383047}{2629465015396073472},\quad
V_{227}=\frac{511508195322329735}{54780521154084864}.
\]

Exact dual:

\[
K_{228}=\frac{22177458672696}{263038955731},\quad
H_{228}=\frac{238775201049969851829137}{3435471315090760605696}.
\]

Exhaustive 680-state Bellman enumeration has exactly two ties `T=(4,2,2)` (decide Q / continue), `Z=(14,0,0)` (decide P / Q), with **1,238** other strictly positive action gaps. Let `u=0` mean continue at `T`, `u=1` mean Q, and `z=0` mean P at `Z`, `z=1` Q. Since `T` already has nonzero symbol-0 and symbol-1 counts, it cannot be an ancestor of `Z`; `Z` is terminal. Thus all observation-vector mixed `u z` coefficients vanish identically. The exact four-corner suffix DP and unmerged DFS agree on all `(eP,eQ,tP,tQ)` observations (**18,472 total DFS visits**).

The equal-error relation is

\[
z_{228}(u)=\frac{122517476704498297}{204800000000000000}
-\frac{3845995475577}{204800000000000000}u.\tag{2}
\]

The two endpoint values belong to `[0,1]`; `eP=eQ` increases strictly, while `tP-tQ` stays positive by endpoint inequalities and affinity. Consequently **for every real**, including irrational, `0<=delta<=263038955731/876488338465357824`:

\[
\boxed{V_{14}(\alpha_{227}+\delta)=V_{227}-\frac{44354917345392}{263038955731}\delta}.\tag{3}
\]

Right endpoint:

\[
\alpha_{228}=\frac{7157865803545}{20061226008576},\quad
V_{228}=\frac{3902476678009}{417942208512}.
\]

The exact `tP-tQ` margins at the left/right ends are respectively `16735238759687725/18260173718028288` and `383048707249/417942208512`.

## 3. Three **null Bellman pivots** are NOT new minimax stages

The exact affine-suffix Bellman breakpoint scanner identifies three decreasing positive `K` values before the next change to the **root-supported** face:

| Null pivot | Exact K | Newly tied state | Root-reachable on an optimal policy? | Effect on all four observations |
|---|---|---|---|---|
| A | `6036090840/71836823` | `(8,4,3)` Q/C | No | exactly zero |
| B | `1197047160/15307309` | `(7,4,3)` Q/C | No | exactly zero |
| C | `3096792/41015` | `(11,6,4)` Q/C | No | exactly zero |

At each K the global Bellman table has 680 states, 1,238 strictly positive alternative-action gaps, and the displayed tie plus terminal `Z` tie. The optimal reachability DAG contains only 115 count-states and excludes the new tied state. Full four-corner rational suffix DP plus independent ordered integer DFS gives the **zero vector** for the new tie's coefficient, and zero increment in the balanced error interval. **17,644 ordered DFS visits per null pivot** were performed. These pivots must not be misreported as new positive-length optimality intervals; they are a reusable counterexample to the shortcut `every state-level Bellman tie => new primal breakpoint`.

The scanner treats every Bellman value as an exact affine function `A+B*K` while its minimizing-action region remains fixed. It chooses the correct lower-K action at ties, locates the largest strictly lower positive root of any alternative gap, then recomputes all 680 Bellman values at the candidate. The three zero-impact transitions, their root-line contacts, and absence of intermediate action crossings are checked in the executable certificate. After skipping the null pivots the next **effective** root kink is exactly `K=72`, not the first raw state-level candidate. Stage numbering here counts **nontrivial primal intervals**: Stage229 corresponds to `K=72`.

## 4. Stage229: first degenerate multitie face, solved by a finite exact polytope

At `K229=72` the root dual value is

\[
H_{229}=\frac{6344018522161}{104485552128},
\quad H_{229}=H_{228}+2\alpha_{228}(72-K_{228}).
\]

There are four tied count-states:

- `A=(12,1,0)` — continue/P;
- `B=(13,1,0)` — continue/P;
- `C=(13,1,1)` — continue/Q;
- `Z=(14,0,0)` — P/Q.

The Bellman enumeration checks 680 states and **1,236** strictly positive gaps. Unlike earlier stages, **A is an ancestor of B and C**, and one cannot assert that all mixed randomization coefficients vanish. The exact bilinear `A*B` interaction in the observation vector `(eP,eQ,tP,tQ)`, holding `C=Z=0`, is

\[
\left(\frac{244140625}{34828517376},-\frac{244140625}{26121388032},
\frac{244140625}{1451188224},\frac{244140625}{2176782336}\right)\ne0.\tag{4}
\]

The `A*C` mixed term is also nonzero. Treating the four coins as a single affine line without checking these interactions would be invalid. We instead use an **exact 16-corner convex-hull argument**:

**Markovization lemma.** At a fixed count-state `(n,a,b)`, every ordered history reaching it has the same P/Q prefix likelihood ratio. Therefore an arbitrary full-history randomized policy's conditional probabilities of selecting each action given that state are *identical under P and Q*. Replacing it by the corresponding count-state randomized policy preserves the P- and Q-occupancy measures and, by finite DAG induction, both errors and both expected stopping times. If a policy is Bellman-tight, its visited actions must minimize the Bellman value. Since the only choices are the four ties above, its observation vector belongs to the convex hull of the `2^4=16` deterministic count-state tie policies: independent coins on a finite acyclic decision graph expand as a convex combination of those deterministic policies. Every convex combination conversely is implementable using a single external random seed at the root.

**Exact corner verification.** All 16 corner observations were computed twice: exact rational suffix DP and a separate unmerged integer P/Q branch-mass DFS (**67,816 total DFS visits**); values coincide entrywise. All 16 corners satisfy `tP>tQ`, so the inequality persists throughout the hull. None has `eP=eQ` by itself. Intersecting the 15-dimensional mixing simplex with `eP-eQ=0`, a linear objective `eP` attains its extremes at a simplex edge joining opposite error-difference signs. The exact program checks **all 64 such intersecting edges**; this is exhaustive, not a heuristic sample.

The minimum balanced error is exactly the Stage228 endpoint `alpha228`. The two extremizing policies are mixtures of deterministic four-bit policies, where the bits in order denote the decisions at `A,B,C,Z` (0 = C,C,C,P; 1 = P,P,Q,Q):

- Left: `0000` and `0001`, with weights `125559035173/312500000000` and `186940964827/312500000000`. Its observation is `(alpha228,alpha228,V228,tQ_left)`.
- Right: `1110` and `1111`, with weights `76535597673/312500000000` and `235964402327/312500000000`. Its observation is

\[
\left(\frac{2406332872015}{6687075336192},\frac{2406332872015}{6687075336192},
\frac{3719078240509}{417942208512},\frac{422740996345}{52242776064}\right).\tag{5}
\]

Both are dual tight and satisfy strictly positive `tP-tQ`. Their convex mixture realizes **every real balanced error** between the two endpoints. Since (1) supplies a universal lower bound for *all* ordered-history policies, this proves, for all real `0<=delta<=15283203125/5015306502144`:

\[
\boxed{V_{14}(\alpha_{228}+\delta)=V_{228}-144\delta}.\tag{6}
\]

The maximal endpoint among **all** Bellman-tight balanced policies at K=72 is

\[
\boxed{\alpha_{229}=\frac{2406332872015}{6687075336192}},\quad
\boxed{V_{229}=\frac{3719078240509}{417942208512}}.\tag{7}
\]

**Strict right of this fixed support.** If equality in (1) at any `alpha>alpha229` were possible, compactness of finite-horizon randomized policy probabilities gives an attaining policy, and equality forces `eP=eQ=alpha`, `tP=max(tP,tQ)` and Bellman-tight actions. The 16-corner hull would then contain a balanced point beyond its exactly enumerated maximum `alpha229`, contradiction. Thus the same `K=72` lower supporting line is strictly below the attainable value immediately to the right (indeed at any such `alpha` for which the value is finite). This is **not** an independent Driver admission claim.

## 5. Stage230: subsequent ordinary two-tie interval

Exact support and contact:

\[
K_{230}=\frac{43416}{607},\qquad
H_{230}=\frac{478645280887949}{7927841267712}
=H_{229}+2\alpha_{229}(K_{230}-72).
\]

The only Bellman ties are `T=(11,1,0)` (continue/P) and `Z=(14,0,0)` (P/Q), with 680 states and 1,238 positive gaps. The two states are not ancestor-related because T has already observed symbol 0 while Z has none, and Z is terminal, so the two-coin mixed coefficient is zero. Four-corner exact DP/ordered integer DFS agreement uses **16,210 DFS visits**.

Define `u=0` to continue at T and `u=1` to decide P; define `z` as the Q-probability at Z. The exact balanced-coin law is

\[
z_{230}(u)=\frac{235964402327}{312500000000}+\frac{40139}{320000}u,\quad 0\le u\le1.\tag{8}
\]

Both coin endpoints lie in `(0,1)`, the common error increases strictly, and the P-minus-Q expected-length margins at endpoints are respectively `337150269749/417942208512` and `614896242623/835884417024`, both positive. Thus for all real `0<=delta<=65205078125/40122452017152`:

\[
\boxed{V_{14}(\alpha_{229}+\delta)=V_{229}-\frac{86832}{607}\delta}.\tag{9}
\]

New endpoint:

\[
\boxed{\alpha_{230}=\frac{14503202310215}{40122452017152}},\quad
\boxed{V_{230}=\frac{7243830309143}{835884417024}}.\tag{10}
\]

## 6. Validation scope and next question

The runnable `REPRO_STAGE228_230.py` performs the full exact Bellman checks, rational DP + independent unmerged ordered integer DFS, three null-pivot reachability checks, `K=72` all 16 corner observations, all 64 error-hyperplane vertices, endpoint equalities, strict length margins and exact neighboring dual contacts. It returned `STAGE228_230_AUTHOR_EXACT_PASS 155430`. This number counts all visited ordered DFS nodes including 18,472 (Stage228), 52,932 (three null pivots), 67,816 (Stage229), and 16,210 (Stage230). It is a **finite exhaustive mathematical certificate** for this declared N=14 model and these support faces, not a general proof about infinite horizons, other distributions, P000 X6 dynamics or physical nature. Separate implementations cross-check arithmetic, **not** authorship independence.

The next exact dual **candidate only**, not a proved primal interval:

\[
K_{231}=\frac{33912}{479},\quad H_{231}=\frac{5990704895603323}{100097158938624}.
\]

Its ties are `(10,1,0)` P/continue and terminal `(14,0,0)` P/Q; the 680-state scan gives 1,238 strict positive gaps. The exact contact `H231=H230+2*alpha230*(K231-K230)` is checked. The smallest uncompleted question is to calculate its four P/Q-error/time corners with both exact methods, solve its balanced coins and prove Stage231's nontrivial interval or a precise rational obstruction. Preserve the multitie-polytope method when ties become ancestral; do not treat a state-level Bellman kink as a primal stage without root-reachability/positive-width verification.

## 7. Provenance and authority

This turn read the current canonical `GLOBAL_KNOWLEDGE_V1 main@3bd42cf2b5db2c2c0223a384e367aeefaa4ff3a3` and Enterprise Math `main@978a2622d1f25389f8edd6e7bc1ac8a36be5424d` with P000 projection and original project P000 V5 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, mandatory X6/time and joint-observer constraints, and applicable portable research protocols. Predecessor proof immutable author commit: `8673e646772812ff0052d71cf251f558da395f93`; existing Draft PR #1571 is the author-side evidence handoff only.

At this turn native task-owner lookup failed `CONTROL_QUOTA`; prior authoritative status reports `research_authority_granted=false`. No native CLAIM, Source Result, Driver acceptance, or X6 correspondence was obtained. Status: `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`; local scientific identity is a local provenance label until a separately authorized activity/session registry confirms it.
