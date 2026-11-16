# PREFIX-826 — Exact minimal universal temporal recurrence for positive Q-only BRC source-count traces

**Date:** 2026-11-16. **Status:** AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Research line:** R6 independent portable auxiliary mathematics, following PREFIX-823/824/825. **Scientific freeze:** \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. No shared X6 Task CLAIM or native event permission is asserted.

## 1. Exact scope and theorem

Use the same marked-source BRC counting model as PREFIX-825. Capacity \`q>=1\`; a named unmarked subset \`S\`, a marked-source flag \`m in {0,1}\`, and \`|S|+m<=q\`. Each unmarked removal has its own nonnegative integer weight \`beta_i\`; marked removal has weight \`b>0\`; marked insertion has weight \`a>0\` when capacity allows. Let \`R\` and \`A\` be unnormalized positive counting operators and \`Q=R+A\`. For any finite integer mass distribution \`v\` on legal named states, let \`y_t=C Q^t v\`, where \`C\` returns the full vector of source-count totals \`(C_0,...,C_q)\`. Put \`lambda=ab>0\`.

**Theorem 826.1 (universal integer recurrence).** For every \`q>=1\`, every choice of unmarked removal weights and every initial mass distribution (integer, nonnegative integer or rational), the entire vector trace satisfies
\[
\boxed{\sum_{j=0}^{q}(-1)^{q-j}{q\choose j}\lambda^{q-j}\,y_{t+2j+1}=0\qquad(t\ge0).}
\]
Equivalently the transition operator on the complete conditional elementary-symmetric moment carrier satisfies
\[
\boxed{Q\,(Q^2-\lambda I)^q=0.}
\]
The operator statement means the explicitly defined moment-space realization \`L\` of \`Q\`, and the trace statement holds for named states through the exact moment map.

**Theorem 826.2 (sharp universal trace order).** Over the complete conditional-moment space, the least monic polynomial \`p\` for which \`C p(L)=0\` is exactly \`p(x)=x(x^2-\lambda)^q\`, of degree \`2q+1\`. The same sharpness holds on the full rational span of legal named-source states if there are at least \`q+1\` pairwise-distinct positive unmarked weights. No claim of sharpness is made for fewer sources or an observer with discarded count bins.

**Corollary 826.3 (exact arbitrary-time evaluation).** For each parity \`r in {1,2}\`, \`y_{r+2n}/lambda^n\` is a vector-valued polynomial in \`n>=0\` of degree at most \`q-1\`. Hence the \`2q\` vectors \`y_1,...,y_{2q}\` determine all \`y_t\` for \`t>=1\` (while \`y_0\` is a separate initial output). Define integer vectors
\[
d_{r,j}=\sum_{k=0}^{j}(-1)^{j-k}{j\choose k}\lambda^{j-k}y_{r+2k},\quad 0\le j<q.
\]
Then the exact, division-free evaluation formula is
\[
\boxed{y_{r+2n}=\sum_{j=0}^{\min(n,q-1)}{n\choose j}\lambda^{n-j}d_{r,j}\quad(n\ge0,\ r=1,2).}
\]
No floating point or rational arithmetic is required when the initial mass and weights are integers.

For \`q=5,a=2,b=3\` the recurrence specializes to
\[
y_{t+11}=30y_{t+9}-360y_{t+7}+2160y_{t+5}-6480y_{t+3}+7776y_{t+1}.
\]

## 2. Proof — upper annihilator

Write \`U[k,h]\` for unmarked-flag-absent elementary-symmetric moments and \`V[k,h]\` for marked-present moments, with \`0<=h<=k<=q\` for U, \`0<=h<=k<=q-1\` for V. All impossible indices are zero. PREFIX-825's exact named-state elementary-symmetric derivation gives
\[
(LU)_{k,h}=(h+1)U[k+1,h+1]+bV[k,h],
\quad
(LV)_{k,h}=(h+1)V[k+1,h+1]+aU[k,h].
\]
The dimension is \`(q+1)^2\`. Order the moment coordinates by \`k\`. For \`0<=k<q\` the diagonal block consists of \`k+1\` copies of
\[
D=\begin{pmatrix}0&b\\a&0\end{pmatrix},\qquad D^2=\lambda I.
\]
The last \`k=q\` diagonal block is the \`(q+1)\`-dimensional zero matrix. All other entries change \`k\` by exactly one. Since \`lambda>0\`, the three eigenvalues \`0,+\sqrt\lambda,-\sqrt\lambda\` are distinct; the zero eigenvalue is semisimple because it occurs in only the terminal diagonal block. For each nonzero eigenvalue a Jordan chain can cross at most \`q\` diagonal levels (\`k=0,...,q-1\`). Therefore the minimal polynomial divides \`x(x^2-\lambda)^q\`. This proves the operator annihilator over the reals; the displayed polynomial has integer coefficients and therefore is also the exact identity over the integer moment matrix. Apply \`C L^t\` and the named-moment map to obtain Theorem 826.1.

## 3. Proof — both nonzero eigenmodes and zero mode are observable

Consider the invariant \`2q\`-dimensional subspace spanned by the diagonal coordinates \`U[k,k],V[k,k]\` for \`k=0,...,q-1\`. On it, \`L=D+N\`, with \`D\` the same \`2x2\` block on every level and \`N\` the strictly triangular lowering map with nonzero coefficients \`k\`; \`D N=N D\`. Over the real quadratic extension, the eigenvectors of \`D\` for \`+\sqrt\lambda\` and \`-\sqrt\lambda\` each support a length-\`q\` Jordan chain under \`N\`. The count observer restricted to the lowest level \`U[0,0],V[0,0]\` is injective: these two coordinates occupy the distinct output bins \`C_0,C_1\`. Thus the endpoint of *each* length-\`q\` chain is visible and neither factor \`(x-\sqrt\lambda)^q\` nor \`(x+\sqrt\lambda)^q\` can be removed from the observer annihilator.

The vector supported on \`U[q,0]\` is a zero-eigenvector, since no derivative term enters it, and is visible in output bin \`C_q\`. Thus the factor \`x\` is also required. This proves least-observer-polynomial sharpness, including when \`lambda\` is a rational square (where the two nonzero factors can otherwise separate).

For explicit exact witnesses:
\[
C L(L^2-\lambda I)^{q-1}e_{U[q-1,q-1]}
=
2^{q-1}(q-1)!\times
\begin{cases}
\lambda^{q/2} e_{C_0},&q\ {\rm even},\\
a\lambda^{(q-1)/2}e_{C_1},&q\ {\rm odd}.
\end{cases}
\]
Also \`C(L^2-\lambda I)^q e_{U[q,0]}=(-\lambda)^q e_{C_q}\`. Both are nonzero for positive a,b. For the named-state transfer of sharpness, PREFIX-825 Section 4 proves that with at least \`q+1\` distinct positive unmarked weights, the legal named-state moment columns span the complete conditional-moment space over the rationals. Hence a polynomial annihilating all named-state trace outputs must annihilate the complete moment observer.

## 4. Proof — temporal polynomial and integer jump formula

Set \`z_n=y_{r+2n}\` for \`r=1\` or \`2\`. Theorem 826.1 gives \`(E-\lambda)^q z=0\` where \`E z_n=z_{n+1}\`. Because \`lambda!=0\`, setting \`w_n=z_n/\lambda^n\` gives \`\Delta^q w=0\`; hence \`w_n\` is a polynomial of degree at most \`q-1\`. Newton's exact forward-difference identity gives \`w_n=sum_j binom(n,j) Delta^j w_0\`. Multiplying through by \`lambda^n\` and clearing the denominators in the finite differences produces the displayed integer vectors \`d_{r,j}\` and the integer formula. Since \`binom(n,j)=0\` when \`j>n\`, all powers of \`lambda\` in the displayed sum are nonnegative integers.

The result is a temporal *annihilator* and exact future-evaluation method. Its degree \`2q+1\` is not the joint linear-state observation dimension \`d_Q(q)\` of PREFIX-823: storing enough distinct initial count-bin observations still requires vector data, and construction/precomputation/output/bit growth have their own costs.

## 5. Exact computation and reproducibility

The attached standard-library Python checker independently constructs the \`(q+1)^2\` exact integer moment operator and tests its annihilator on **every coordinate basis vector** for \`q=1,...,12\` and \`(a,b)=(1,1),(2,3),(3,2)\`. It verifies both sharpness witnesses for each configuration. Separately it enumerates all legal named-source basis states for \`q=1,...,6\`, with \`m=q+1\` named unmarked weights from two families and \`(a,b)=(1,1),(2,3)\`. It generates integer weighted branches directly without using the moment operator, then checks the universal recurrence and division-free reconstruction through \`4q+7\` steps.

Local exact result: **36** moment configurations, **2,454** annihilator basis tests, **36+36** sharpness witness tests, **24** named configurations, **1,860** named initial states, **204,612** scalar recurrence assertions, and **317,096** scalar interpolation assertions, all passed. Every arithmetic operation uses exact Python integers. See \`PREFIX826_R6_Q_ONLY_RECURRENCE_CHECK.py\` and \`PREFIX826_R6_Q_ONLY_RECURRENCE_RESULTS.json\`. These finite checks are implementation regression; the arbitrary-capacity statements above rely on their general proofs.

## 6. Boundary, research value, next question

This is the exact positive-count, unnormalized \`Q\` model, with all source-count bins and arbitrary named initial masses. It preserves the model's declared future observer; it is not an X6 Cell/Link/Port or physical-time dynamics theorem. Scientific P000 and native-event attribution remain separately typed and unchanged. A finite time step \`t\` here counts applications of \`Q\`, not elapsed physical time.

**New reusable tool:** after sampling \`y_1,...,y_{2q}\`, compute exact count traces at arbitrarily large iteration indices without repeated application of \`Q\`, using a short integer recurrence or binomial jump formula. When claiming performance, include the cost of producing these samples and the bit length of the result.

**Next:** finish the still-open positive minimal carrier realization for \`q>=5,b>0\`; study how the temporal recurrence behaves under separately addressable \`R,A\` words or additional individually addressable named sources, where \`Q\`-only compression is insufficient; and compare exact jump-evaluation total cost on sparse vs dense source distributions.

**Sources and provenance:** frozen task pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; PREFIX-823/824/825 exact papers at \`awdawmip/enterprise-math\`; \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, \`research_priorities/research_method.json\`. Account canonical main rules were read through the global bootstrap and manual. The project P000 V4 projection was verified against the original blob; the frozen Source P000 V5 was read at the scientific pin. No shared CLAIM, RA update, review admission, or Foundation promotion is asserted.
