# R142 — Quantitative Farey-support screening for fixed-phase S23 eventual saturation

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT THEOREM / NOT_REVIEWED.
Scientific input pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Type: external scalar tied-phase Sturmian observer, not a native Heartbeat X6 operation.
Predecessors: R137B Farey gap/exact word correspondence, R138 \`D_g>=min(b,d)\`, R139 permanent individual-gap coefficient \`max(2,bd-D_g+2)\`, and R141 Farey-support construction. Sources are the immutable commits R139 \`419b3f1f0b732cb945a51b3b9e33406449fe6b81\` and R141 \`45077e19e3bdf96f2f3842333c2d485476d20e3c\`.

## 1. Definitions

Let m>=5 and K>=2 be integers. Let
\[
S_i^{(K)}(\theta)=\lfloor(K+i)\theta\rfloor-\lfloor(K+i-1)\theta\rfloor,\quad
0\le i<m,\quad 0<\theta<1.
\]
Write V(K,m) for the realized binary words and W_m for the finite Sturmian language. For a word w=w_0...w_{m-1} in W_m put s_0=0 and s_j=sum_{i<j}w_i. Define
\[
\alpha_w=\max\left(0,\max_{0\le i<j\le m}{s_j-s_i-1\over j-i}\right),\qquad
\beta_w=\min\left(1,\min_{0\le i<j\le m}{s_j-s_i+1\over j-i}\right).
\]
Thus the possible slopes for a freely chosen intercept form I_w=(alpha_w,beta_w), with rational endpoints of denominator at most m.

Define the *slope-support denominator*
\[
q_*(w)=\min\{q\ge1:\ \exists p,\ 0\le p\le q,\ \gcd(p,q)=1,\quad
\alpha_w\le p/q\le\beta_w\}.
\]
It is finite, since both support endpoints are order-m rationals (0/1 and 1/1 included).

For each Farey-intercept gap g representing w, let b_g,d_g be its two adjacent order-m slope denominators and D_g the R138 exact offset. The gap's permanent activation threshold and the earliest permanently active selected representation are
\[
T_g=\max(2,b_gd_g-D_g+2),\qquad U_w=\min_{g:W(g)=w}T_g.
\]

## 2. Quantitative theorem

**Theorem R142.1 (denominator-controlled permanent representation).** For every m>=5 and w in W_m,
\[
\boxed{U_w\le q_*(w)(m-1)+2.}
\]
More precisely, each reduced p/q in the closed slope-support interval provides an open order-m Farey cell adjacent to p/q and an intercept gap representing w whose threshold is at most q(m-1)+2. Above that threshold the original one-parameter observer has an explicitly constructible rational phase witness for w.

**Proof.** The prefix inequalities s_j <= rho+j theta < s_j+1 show that the free-intercept slope set equals the open interval I_w. Because its endpoints are in F_m, if p/q is in its closure then at least one adjacent order-m Farey cell lies inside I_w. On that cell, any w-realizing intercept lies in a nonempty intercept gap with the same word throughout the cell. One neighboring slope denominator is q and the other, say d, is <=m. The R138 offset inequality gives D_g>=min(q,d). Therefore
\[
b_gd_g-D_g\le qd-\min(q,d)\le q(m-1).
\]
For d>=q, the second bound reads q(d-1)<=q(m-1); for d<q it reads d(q-1)<=q(m-1). R139 now gives T_g<=q(m-1)+2, so the minimum U_w obeys the claimed bound. The R137B strict integer-interval condition, followed by the midpoint reconstruction in R140, supplies rational witnesses at every K>=T_g. QED.

## 3. Uniform critical-family localization

Set
\[
E(m)=(m-2)\lfloor(m-1)/2\rfloor+1,\qquad
n(m)=\lfloor(m-3)/2\rfloor,\qquad H(m)=n(m)(m-1)+2.
\]
For both parities of m, direct integer algebra gives the exact identity
\[
\boxed{E(m)-H(m)=\lfloor(m-2)/2\rfloor>0.}
\]

**Corollary R142.2 (all-length screening theorem).** For every integer m>=5 and each w in W_m with q_*(w)<=n(m),
\[
\boxed{\forall K\in\mathbb Z,\ K\ge H(m):\quad w\in V(K,m).}
\]
Consequently any possible obstruction to the conjectured global equality T(m)=E(m) must belong to the explicitly defined *Farey-avoidant family*
\[
\mathcal A_m=\{w\in W_m:q_*(w)>n(m)\}.
\]
Equivalently, if some K>=E(m) misses a word, its closed slope-support interval contains **no** reduced fraction of denominator at most n(m). This conclusion applies to all m, without a finite-length ceiling.

**Proof.** Substitute q_*(w)<=n(m) in R142.1 and use the displayed identity. QED.

This is a genuine infinite-family subresult. It does not assert that the remaining avoidant patterns are present at all K>=E(m), which is the unresolved global conjecture. The exact m=4 exception T(4)=4 from R140 is outside the m>=5 statement.

## 4. Constructive certificate

For an admissible intercept gap between \`p-j*theta\` and \`q-k*theta\` over the Farey cell a/b<theta<c/d, write L=K-1. Feasibility is equivalent to an integer N with
\[
(L+k)a/b-q<N<(L+j)c/d-p.
\]
The smallest admissible candidate is \`N=floor((L+k)a/b-q)+1\`. A rational phase is the midpoint of
\[
\left(\max(a/b,(N+p)/(L+j)),
\min(c/d,(N+q)/(L+k))\right).
\]
At K>=T_g the interval is nonempty; direct exact floors of the generated theta recover w. No original chronological event scan in K is required.

## 5. Exact verification (finite regression, distinct from the theorem)

The accompanying independent local checker \`check_r142.py\` uses Python unbounded integers and \`Fraction\`, reconstructs all order-m Farey gaps and prefix-defined slope intervals, checks the known Sturmian totient count, and verifies R142.1/R142.2 for **every** word and m=5,...,30.

Aggregate: 26 lengths; 24,976 word records; 19,654 words certified by the denominator filter; 5,322 avoidant words; 1,396 words with representative horizon U_w>E(m). All 1,396 belong to the avoidant family. A separate 2,604 exact rational witness checks at m=5,7,10,12,16,20 evaluate the **original floor-difference observer** at both K=E(m) and K=E(m)+10^40+17.

Selected rows (m; all words; permanently certified by filter; avoidant; U_w>E):
- 5: 24; 12; 12; 8.
- 10: 136; 80; 56; 14.
- 16: 498; 336; 162; 34.
- 20: 944; 708; 236; 64.
- 24: 1,586; 1,204; 382; 88.
- 30: 3,018; 2,462; 556; 160.

The verifier returns \`R142_SUPPORT_DENOMINATOR_FILTER_PASS\`. Its table and coverage are in \`verification_r142.csv\`. The mathematical all-m statement uses the R138/R139 author-side predecessor lemmas; independent mathematical admission remains NOT_REVIEWED.

## 6. Next mathematical step

Classify the avoidant family A_m by the two Farey endpoints and the possible intercept gaps, then prove or refute the required all-K coverage on A_m. A targeted test should focus on denominators just above n(m), especially the two-neighbor alternation where no single gap is yet permanently available at E(m). Reuse R139B's exact last disappearance of 10^(m-2)1 and its complement as sharp lower-bound witnesses. Preserve all source/future-observer typing before any native X6 transfer.
