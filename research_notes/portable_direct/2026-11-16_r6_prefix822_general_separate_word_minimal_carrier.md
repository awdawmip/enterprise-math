# PREFIX-822 — 全容量具名来源操作的精确最小整数观察载体

Date: 2026-11-16 (Asia/Shanghai). Independent portable R6 TASK_RESEARCH auxiliary result; frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Predecessors: PREFIX-818–821. Evidence status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED. This note records source-side auxiliary research, without a native shared X6 CLAIM.

## Model

Let q≥1 be integer capacity. A source state is a named subset S of {0,...,m−1} of size ≤q. Source 0 is marked, with removal weight b=β₀≥0 and addition weight a>0. Other removal weights βᵢ≥0. R deletes one present named source i with multiplicity βᵢ, summing alternatives. A adds source 0 if absent and capacity allows, with multiplicity a. All words in the separately selectable alphabet {R,A}, including the empty word, are observable through the exact cardinality histogram Yₗ, 0≤l≤q. Initial populations are arbitrary integer vectors (physical count populations are nonnegative). Q=R+A is a *different, less discriminating* operation language.

Define M_{z,k,h}=Σ mass(S)e_h(βᵢ:i∈S\{0}) for marked indicator z∈{0,1}, unmarked source count k≤q−z and h=0,...,k. Out-of-range moments are zero. The conditional moment space has

N=T(q)+T(q−1)=(q+1)², T(k)=(k+1)(k+2)/2.

The exact integer maps are

\`\`\`
(RM)_{0,k,h}=(h+1)M_{0,k+1,h+1}+b M_{1,k,h}
(RM)_{1,k,h}=(h+1)M_{1,k+1,h+1}
(AM)_{0,k,h}=0
(AM)_{1,k,h}=a M_{0,k,h}
Y_l=M_{0,l,0}+M_{1,l−1,0}.
\`\`\`

The proof works for all nonnegative integer β, with a>0, independently of the number of unmarked branches. For the *named-state minimality transfer*, require at least q+1 unmarked branches with pairwise distinct positive integer removal weights.

## Theorem 822.1 — exact separate-word observer kernel and all-capacity linear minimum

In the N-dimensional moment space, the kernel of all future cardinality-histogram observations for all finite R/A words is exactly the one-dimensional span of the *primitive* integer vector K:

\`\`\`
K[M_{0,q,0}]=-1,
K[M_{0,q,1}]=-b,
K[M_{1,q−1,0}]=+1,
all other entries zero.
\`\`\`

Words of length ≤q+1 already determine the same kernel. When the distinct-weight condition above holds, the minimal rational linear carrier for **all** named-state integer initial mass populations and all R/A words has dimension **(q+1)²−1**.

### Proof

Direct substitution gives RK=AK=CK=0. In particular, the only possibly nonzero R output is (RK)_{0,q−1,0}=−b+b=0; the top-size count is (CK)_q=−1+1=0. Therefore K is invisible at every future word.

Conversely, let v have zero histogram after every R/A word. For any k≤q−1 and 0≤h≤k, observe the cardinality k+1−h after A followed by h removals. Its exact weighted-path count equals

Y_{k+1−h}(Rʰ A v)=a·h!·(M_{0,k,h}+b M_{0,k,h−1}), M_{0,k,−1}=0.

All terms from other initial k have the wrong final cardinality. Since a>0, induction over h forces every M_{0,k,h}=0 for k≤q−1.

Pure removal from initial total cardinality n gives, for 0≤h≤n,

Y_{n−h}(Rʰ v)=h!·(M_{0,n,h}+M_{1,n−1,h}+b M_{1,n−1,h−1}).

For n≤q−1, the first term already vanishes. Induction over h now gives all M_{1,k,h}=0 for k≤q−2. Only top-row x_h=M_{0,q,h} (h=0..q) and y_h=M_{1,q−1,h} (h=0..q−1) can remain. Their pure-removal observations satisfy

x_h+y_h+b y_{h−1}=0 (h=0,...,q), y_{−1}=y_q=0.

Apply the first argument to Rv: all words Rʰ A R also have zero outputs, whence (Rv)_{0,q−1,h}=0 and

(h+1)x_{h+1}+b y_h=0 (h=0,...,q−1).

The first two equations give x₀=−y₀ and x₁=−b y₀. For h=1 the pure-removal equation forces y₁=0; induction yields y_h=0 (h≥1) and x_h=0 (h≥2). At q=1 only the two boundary equations are needed. Hence v=y₀ K. Every word invoked above has length ≤q+1.

For transfer to named-state mass vectors, in each (z,k) block select k+1 distinct positive unmarked weights. The coefficient vectors of the polynomials ∏_{i≠j}(1+βᵢt), obtained by omitting one of these k+1 indices, are independent: evaluating at t=−1/βⱼ isolates the j-th polynomial. Different (z,k) blocks have disjoint support; thus the named-source mass→conditional-moment linear map has full rational row rank N. The N−1-dimensional observer image is attained by genuine named-state initial mass directions, and no lower-dimensional rational linear observer can preserve all output words. QED.

## Corollary 822.2 — nonnegative integer realization attaining that minimum

Define an integer projection P which retains every moment coordinate except M_{1,q−1,0} and replaces two slots by

u=M_{0,q,0}+M_{1,q−1,0},   v=M_{0,q,1}+b M_{1,q−1,0}.

Its kernel over the integers is ℤK. Define section S on the N−1 coordinates by inserting zero at the removed position and placing u,v in the corresponding original unmarked positions. Both P and S have **nonnegative integer** matrices, and PS=I. Since RK=AK=CK=0, their exact descendants are

R_red=PRS,  A_red=PAS,  C_red=CS,

with PR=PRSP, PA=PASP and C=CSP. Their matrices are nonnegative integral; induction over arbitrary words gives exact infinite-horizon output preservation. The kernel generator K is primitive, so the integer quotient is torsion-free. This is an explicitly observer-safe, nonnegative integer carrier with (q+1)²−1 coordinates, attaining the rational-linear minimum. No assertion of minimality among arbitrary nonlinear codings is made.

## Proposition 822.3 — combined-only invisible directions and a boundary witness

For a>0 and **b>0**, the one-step annihilated invisible subspace ker(C)∩ker(Q) has dimension exactly ceil(q/2). To prove this write x_k=M_{0,k,0}, y_k=M_{1,k,0}. From Qv=0 every higher-degree coordinate is determined by h! inverse recurrences:

\`\`\`
M0[k,2s]   = (ab)^s x[k−2s] / (2s)!
M0[k,2s+1] = −b(ab)^s y[k−2s−1] / (2s+1)!
M1[k,2s]   = (ab)^s y[k−2s] / (2s)!
M1[k,2s+1] = −a(ab)^s x[k−2s−1] / (2s+1)!
\`\`\`

Cv=0 gives x₀=0, x_{k+1}=−y_k. The top marked equations (Qv)_{1,q−1,h}=aM_{0,q−1,h}=0 impose exactly y_{q−2}=y_{q−4}=...=0. Thus precisely ceil(q/2) of y₀,...,y_{q−1} are free, giving that many independent Q-killed invisible directions. This is a rigorous **lower bound** for the full future-Q observer kernel.

A new genuine boundary appears at b=0. For q=4,a=1, exact rational elimination of [C;CQ;...;CQ²⁴] gives Q-only rank **21** at b=0 and **23** at b=1, whereas the separate-word rank is **24** for either b. The combined-only rank is therefore parameter-sensitive even though the separate-word minimum is unchanged.

## Exact computation / verification

The attached executable Python checker uses arbitrary-precision integers and prime-field Gaussian elimination modulo 1,000,000,007. It scans q=1..10, a∈{1,2}, b∈{0,1,3} (60 instances), and verifies separate-word modular rank N−1 and the projected one-step/word recurrence. The positive-b Q-only modular ranks match N−ceil(q/2) in this window; at b=0 they match T(q)+2(q−1). These patterns remain **open as universal characterisitic-zero rank formulas**, apart from the proved Q-killed subspace bound. A separate exact Fraction elimination confirms the q=4 rational ranks 21 and 23. The checker also independently constructs all 98 named basis states for q=1..4, checks the original R/A moment law, and compares all words of length ≤4 to the (N−1)-coordinate reduced carrier: 3,332 exact assertions; all pass.

Arithmetic semantics: integer path counts and exact rational arithmetic; modular rank proves characteristic-zero rank lower bounds, while the general R/A theorem supplies the matching universal upper bound. No floating tolerances or unexecuted native X6 experiments are presented as evidence.

## Next scientific frontier

Prove or refute a complete characteristic-zero formula for the combined-only Q observer rank at arbitrary q, including the b=0 singular case. Determine which individually addressable unmarked source operation exposes K and how many retained named-source moments are then necessary. Native X6 Cell/Link/Port triadic admission and the relation between formal word depth and actual event-time remain independent frozen-scope research questions.

Sources: \`p000_reality_foundation.json\`, \`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json\`, \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, prior PREFIX-818–821. Scientific inputs remain pinned; current operating rules were read separately.
