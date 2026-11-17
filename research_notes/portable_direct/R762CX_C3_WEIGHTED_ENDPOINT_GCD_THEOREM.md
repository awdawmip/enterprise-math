# R762CX — Exact three-adic endpoint compression for weighted three-Port N-BRC

**Task**: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\` · publication \`TP2-8B7E13C5904A2D6F1142\` · researcher \`EM-X6-3050F6\` · 2026-11-17.
**Predecessor**: R762CVb / R762CW, PR #2623 / #2626, latter at \`683e8ab67ddb766e230518bcdefc47df6e803652\`.
**Frozen scientific inputs**: P000 V5 at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`; taskbook at \`e3f42efac29a2da2d95be391f3231a664e2fade0\`.
**Claim type**: exact author proof for a conditional positive N-BRC **candidate** kernel; independent review **NOT_REVIEWED**. No native \`TRIADIC_CLOSURE_E\` event admission.

## 1. Typed branch model and observers

Fix one of the 40 signed-X6 mixed-sign candidate sectors from R762CVb (20 three-axis supports × 2 minority sign classes). It has three *named Port positions* indexed by \`Z/3Z\`, not three spatial coordinates or a native plane. Choose an orientation of this three-state *combinatorial* cycle; relabeling that reverses orientation also exchanges \`p,q\`. A positive N-BRC step has \`p\` independently identified source branches from \`i\` to \`i+1\` and \`q\` independently identified source branches from \`i\` to \`i-1\`, with integers \`p,q>=1\`. Divide by the common gcd of \`p,q\` for normalized endpoint laws, hence assume \`gcd(p,q)=1\`. This assumption does not replace signed Force-Port incidence with a positive mass.

Let \`R=Z[S]/(S^3-1)\`, \`T=p S+q S^2\`, \`D=p+q\` and \`T^t=C_t(0)+C_t(1)S+C_t(2)S^2\`, with \`C_0=(1,0,0)\`. These coefficients are exact positive N-BRC path multiplicities, with \`sum_i C_t(i)=D^t\`. The *named terminal-Port marginal observer* is \`mu_t(i)=C_t(i)/D^t\`. The stronger *source-word observer* records the sequence of clockwise/counterclockwise choices (or each microbranch identity); these are different declared observation languages.

## 2. Exact divisibility theorem

**Theorem 1 (all coprime positive weights, every finite horizon).** For every \`t>=1\`,
\`\`\`
gcd(C_t(0),C_t(1),C_t(2)) =
    1                          if 3 does not divide D,
    3^floor((t-1)/2)           if 3 divides D.
\`\`\`
At \`t=0\` the gcd is 1. In particular, the exact reduced common denominator of all three normalized endpoint probabilities at time \`t\` is
\`\`\`
Q_t = D^t / gcd(C_t(0), C_t(1), C_t(2)).
\`\`\`

**Proof, primes other than 3.** Any common prime factor \`ell\` of the three coefficients divides their sum \`D^t\`, so \`ell|D\`. Since \`gcd(p,q)=1\`, \`p\` is invertible modulo \`ell\`; when \`D=0 (mod ell)\`, the branch operator reduces to \`p(S-S^2)\`. The exact group-algebra identity
\`(S-S^2)^3 = -3(S-S^2)\`
shows that, for \`ell != 3\`, none of its positive powers vanish in \`F_ell[S]/(S^3-1)\`. Thus no \`ell != 3\` divides all three coefficients. When \`3\` does not divide \`D\`, the sum also excludes a common factor 3.

**Proof, the 3-adic lower bound.** Assume \`3|D\`, so \`p,q\` are units modulo 3. Let \`N=1+S+S^2\`. Direct multiplication gives \`T^2 = p^2 N +3U\` for an integral \`U\in R\`; this holds because \`T^2\equiv p^2N (mod 3)\`. Also \`NT=DN\`. Consequently
\`T^{t+2}=p^2D^tN+3UT^t\`.
Starting with \`t=1,2\`, induction proves all coefficients of \`T^t\` are divisible by \`3^floor((t-1)/2)\` for every \`t>=1\`.

**Proof, sharpness.** Work entirely in the exact algebraic integer ring \`A=Z[z]/(z^2+z+1)\`; write \`tau=1-z\`, so \`tau^2=-3z\`. Reduction modulo \`tau\` is \`F_3\`, and \`z\equiv1 (mod tau)\`. Evaluation \`S\mapsto z\` sends \`T\` to
\`lambda=p(z-z^2)+Dz^2=p z tau+D z^2\`.
Since \`3|D\` and \`3\nmid p\`, the first summand has exactly one factor \`tau\` and the second at least two. Thus \`lambda\` has exact \`tau\`-valuation 1.

For odd \`t=2m+1\`, if every \`C_t(i)\` were divisible by \`3^(m+1)\`, then \`lambda^t\` would have \`tau\`-valuation at least \`2m+2\`, contradicting its exact valuation \`2m+1\`. Hence the common 3-power is at most \`3^m\`.

For even \`t=2m\` with \`m>=1\`, suppose all \`C_t(i)\` were divisible by \`3^m\`, and set \`B=T^{2m}/3^m\in R\`. The value \`B(z)=lambda^{2m}/3^m\` is a unit modulo \`tau\`. But the augmentation \`B(1)=D^{2m}/3^m\` is divisible by 3; because \`z\equiv1 (mod tau)\`, this implies \`B(z)\equiv B(1)\equiv0 (mod tau)\`, contradiction. Therefore the maximum common 3-power is exactly \`3^(m-1)\`. Together with the lower bound this proves the formula. This uses formal algebraic integers only; no numerical trigonometric or classical-pi calculation. QED.

## 3. Sharp endpoint seed budget versus full path provenance

Fix a time horizon \`h>=0\` and an initial Port \`i\`. A deterministic *time-layered* realization has \`M\` equiprobable initial hidden seeds, follows legal non-self Port edges with no later randomness, and reproduces the **one-time named terminal-Port distribution at each t=0,...,h**. It need not reproduce conditional transition probabilities or joint path-word probabilities.

**Theorem 2 (sharp seed budget).** The minimum \`M\` is exactly \`Q_h\`. The sequence \`Q_0|Q_1|...|Q_h\` is divisibility-increasing. The conclusion is equivariant under cyclic rotation of the three Port labels; reversing their chosen orientation simultaneously exchanges \`p\` and \`q\`.

**Proof, lower bound.** Each terminal distribution from \`M\` equiprobable deterministic seeds has coordinates in \`(1/M)Z\`. Theorem 1 makes \`Q_h\` its exact common reduced denominator, hence \`Q_h|M\`.

**Proof, construction.** Write \`M=Q_h\`, \`a_t(j)=M C_t(j)/D^t\`; these are integers for all \`t<=h\`, because the prime-power formula for \`Q_t\` implies \`Q_t|Q_h\`. At successive times, the weighted BRC transition gives a *fractional* feasible transport from integer margins \`a_t\` to \`a_{t+1}\` along only the two non-self edges of each Port. The bipartite network has an integral incidence matrix, so an integral transport with identical margins exists. More explicitly, if \`a=(a0,a1,a2)\`, \`b=(b0,b1,b2)\` and \`z=f_(2->0)\`, all integer transports are obtained from
\`\`\`
f_(0->1)=b1-a2+z,     f_(0->2)=a0-b1+a2-z,
f_(1->0)=b0-z,        f_(1->2)=a1-b0+z,
f_(2->0)=z,           f_(2->1)=a2-z,
max(0,a2-b1,b0-a1) <= z <= min(a2,a0-b1+a2,b0).
\`\`\`
The interval is nonempty by feasibility of the original rational BRC coupling and has integer endpoints. Choose an integer \`z\`; pair incoming and outgoing particles at each time layer to make \`M\` legal deterministic paths. Use those paths as equally weighted initial seeds. This matches every time marginal and proves attainment. A cyclic relabeling copies the same construction. QED.

**Theorem 3 (provenance separation).** If the observer additionally demands the entire \`h\`-step directional source-word law, its sharp equiprobable initial seed budget is \`D^h\`. The all-clockwise word has probability \`p^h/D^h\`, with \`gcd(p,D)=1\`, so its reduced denominator already forces \`D^h|M\`. A tape of all \`D^h\` individual positive BRC microbranch words attains this bound. Hence marginal-only compression can save a factor
\`D^h/Q_h = 3^floor((h-1)/2)\` when \`3|D\` and \`h>=1\`; otherwise the factor is 1. The saved data is precisely outside the weaker *one-time* observer, and source-word provenance must be retained if later events can query it. QED.

## 4. Concrete finite example

For \`(p,q)=(1,2)\`, \`D=3\` and \`Q_h=3^h/3^floor((h-1)/2)\` for \`h>=1\`. The first endpoint path vectors are
\`\`\`
t=0  (1,0,0),        Q=1
t=1  (0,1,2),        Q=3
t=2  (4,4,1),        Q=9
t=3  (9,6,12),       Q=9          versus 27 source words
t=4  (24,33,24),     Q=27
t=5  (90,72,81),     Q=27         versus 243 source words
t=6  (225,252,252),  Q=81.
\`\`\`
This contains a genuine two-step plateau: increasing the terminal horizon from 2 to 3, or from 4 to 5, requires no extra *equiprobable initial seeds* for the endpoint-only observer. Source-word information continues to grow at every step. For \`p=q=1\`, \`D=2\` and \`Q_h=2^h\`, recovering R762CW.

## 5. Verification, boundaries and next native problem

\`R762CX_VERIFY.js\` uses arbitrary-precision integer arithmetic, explicitly typed source branches and the above integer-transport formula; no numerical floating-point propagation, matrix exponential, Taylor, trigonometry or physical-time interpretation. Its author-side exhaustive check covers each coprime \`1<=p,q<=14\` and every \`0<=h<=20\`: exactly **127 weight pairs**, **2,667** gcd/mass checks, **2,667** horizon denominator checks and **26,670** integer transport checks. Reproduce with \`node R762CX_VERIFY.js\`; compare JSON output with \`R762CX_EVIDENCE.json\`. These finite tests support the stated universal hand proof but are not an independent review.

The signed Cell/Link/Port event-licensing predicate and V17/V29/V39 transport remain to be sourced. The current result is an exact conditional **positive N-BRC kernel** theorem, not a claim of physical sampling, an energy/force cancellation rule or a full signed-residual quotient.

**Next question**: determine whether an authenticated native \`TRIADIC_CLOSURE_E\` event can select the directional source word (or oriented path-area residue). If so, the endpoint-only \`Q_h\` compression is observationally unsafe; construct a legal suffix witness and identify the minimal native observer-safe repair. If the native event language sees only independent time marginals, construct the exact descent certificate with the actual legal update map.
