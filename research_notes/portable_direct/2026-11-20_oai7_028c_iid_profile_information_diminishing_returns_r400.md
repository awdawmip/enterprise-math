# OAI7-028-C r400 — Exact redundancy identity and diminishing returns of shared iid residue-profile information

Date: 2026-11-20. Status: author-side mathematical proof and exact finite check; not an independent/native Result review or Task closure.

## Provenance and task scope

Task: `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`. Original Researcher `EM-EMF6D046-5A2844` and previous contributors remain attributed. Driver-side derivation follows the pinned external `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a` `coverage-transfer.tex` and `schedule.tex`, and the already saved Enterprise Math r396@9725b1dab7c8d8fa293bab5f2eec54896020e729 and r398@23f2057225777f77409504e19c319e1e9c488176. The Gaussian objects are *external* to the protected Enterprise Math P000 native axes; no X6/Port translation is claimed.

## Theorem (exact information redundancy, concavity and a two-sample certificate)

Let `A` be any finite random variable and let `W_1,W_2,...` be conditionally iid on a common finite alphabet `W`, with conditional one-step law `q_a(w)=P(W_1=w|A=a)`. Write `B_n=(#\{j<=n:W_j=w\})_{w\in W}`, `\bar q(w)=E_A q_A(w)`, and `J_n=I(A;B_n)`, using natural logarithms. Define the unconditional two-sample law
`Q_2(u,v)=E_A[q_A(u)q_A(v)]`. Then:

1. **Exact redundancy identity.** For every integer `n>=1`,
   \[
   \boxed{J_n=n I(A;W_1)-\sum_{j=2}^{n}I(W_j;W_1,\dots,W_{j-1}).}
   \]
   The empty sum is zero. The subtracted term is the total correlation of the ordered sample; it is neither the ordering entropy nor an independent randomization cost.

2. **Diminishing returns.** The nonnegative increments `\Delta_n=J_{n+1}-J_n` are nonincreasing with `n`. In particular,
   \[
   0\le J_{n+1}-J_n\le J_n-J_{n-1}\quad(n\ge2).
   \]
   Hence the exact information about `A` retained by the unordered histogram is a monotone concave sequence in sample count.

3. **Two-sample certified upper bound.** For every `n>=2`,
   \[
   \boxed{J_n\le n I(A;W_1)-(n-1)I(W_1;W_2)\le n I(A;W_1).}
   \]
   Both quantities subtracted/charged in the first bound are explicit from `q_a`:
   \[
   I(A;W_1)=\mathbb E_A D_{\rm KL}(q_A\Vert\bar q),
   \quad I(W_1;W_2)=
   D_{\rm KL}(Q_2\Vert\bar q\otimes\bar q).
   \]
   A second simultaneous upper bound is `J_n<=H(V)`, where `V=q_A` denotes the exact law type (r396). Thus the minimum of the two bounds is a valid certificate, without enumerating all `\binom{n+|W|-1}{|W|-1}` histograms.

4. **Exact predictive decomposition.** If `B_0` is empty and `\widehat q_{j}(w)=E[q_A(w)|B_j]`, then
   \[
   \boxed{J_n=\sum_{j=0}^{n-1}\mathbb E_{A,B_j}
   D_{\rm KL}(q_A\Vert\widehat q_j).}
   \]
   The summands are nonnegative and nonincreasing in `j`. This is a representation of the actual information cost, not an assumption about a posterior inference algorithm.

### Proof

For each fixed histogram `B_n=b`, every ordering of the corresponding multiset has conditional probability proportional to `\prod_w q_a(w)^{b_w}`; hence its conditional distribution, given `A=a,B_n=b`, is uniform and independent of `a`. Therefore `I(A;B_n)=I(A;W_1,...,W_n)`, as in r398.

Conditional iid implies `H(W_1,...,W_n|A)=nH(W_1|A)`. Subtract this from `H(W_1,...,W_n)=nH(W_1)-\sum_{j=2}^n I(W_j;W_1,...,W_{j-1})` to get (1).

By chain rule, `\Delta_n=I(A;W_{n+1}|W_1,...,W_n)=H(W_{n+1}|W_1,...,W_n)-H(W_1|A)`. Exchangeability of the entire mixture of iid sequences gives
`H(W_{n+2}|W_1,...,W_n)=H(W_{n+1}|W_1,...,W_n)`.
Adding the conditioning variable `W_{n+1}` can only lower entropy, so `\Delta_{n+1}<=\Delta_n`. Nonnegativity follows from conditional mutual information, proving (2).

Every term in the total correlation from (1) obeys
`I(W_j;W_1,...,W_{j-1})>=I(W_j;W_1)=I(W_1;W_2)`,
where the final equality uses exchangeability. This proves (3). The formulas for the two one-/two-sample quantities follow by their finite joint distributions, and the law-type cap is data processing `A->V->B_n`.

Conditionally on `B_j`, the predictive law of `W_{j+1}` is `\widehat q_j`; conditionally on `A,B_j`, it is `q_A`. Substitution into `I(A;W_{j+1}|B_j)` yields (4), and the monotonicity of the expected terms is (2). All zero-probability terms are interpreted with the standard `0\log 0=0` convention. QED.

## Exact rational finite witness

Take `A\in\{0,1\}` equiprobable, `W_j\in\{0,1\}` and `q_0=(1/4,3/4)`, `q_1=(3/4,1/4)`. Then `\bar q=(1/2,1/2)` and the unconditional two-sample probability matrix is exactly

\[
Q_2=\frac1{16}\begin{pmatrix}5&3\\3&5\end{pmatrix}.
\]

Thus
\[
I(A;W_1)=\log2-h_2(1/4)\approx0.130812035941137,\quad
I(W_1;W_2)=\frac58\log(5/4)+\frac38\log(3/4)\approx0.0315839424019633.
\]
For `n=3`, exact enumeration of all eight words with rational probabilities gives
\[
I(A;B_3)\approx0.3094253663557904
\quad\text{and}\quad
3I(A;W_1)-2I(W_1;W_2)\approx0.3292682230194843.
\]
The bound is strict, and the discarded dependence is positive. The exact rational mass table, rather than the displayed logarithmic decimals, certifies the finite probability identity.

## Application to the pinned Gaussian coverage experiment

At each **fixed exact start** in `schedule.tex`, let `A=A_{i+1}` be the random later checkpoint time, and `W_j` the residue profile of the `j`th independent continuation displacement, conditional on `A`. The shared profile histogram `B_{n_i}` is defined before the independent signed-subset selection `S`. Since `F_S(Y)` is a deterministic function of `A` for fixed `S`, data processing yields

\[
\mathbb E_S I(F_S(Y);B_{n_i})
\le I(A;B_{n_i})
\le \min\left\{H(V_i),\,
n_i\mathbb E_A D_{\rm KL}(q_A\Vert\bar q)
-(n_i-1)D_{\rm KL}(Q_2\Vert\bar q\otimes\bar q)\right\}.
\]

This is a concrete additional, **two-sample** sufficient certificate for the r396 information-aware shared conditioning hypothesis. It uses the *same* original conditional iid continuations, terminal marginal and Chernoff proof; no alternative sampler, separate signed-coordinate time or independent Gaussian-native embedding is introduced.

The certificate is potentially loose when `n_i` is large; the actual joint law may saturate well below it. The next decisive Gaussian step is to obtain genuinely uniform-in-exact-start bounds for the law mixture `q_A` and pair law `Q_2`, compare the displayed minimum with the source's `\eta_i\delta_i\beta_{i+1}s_iL_*/16` budget, and retain the original geometric/conditional-coverage hypotheses. Nothing here changes the original Gaussian theorem's correctness or proves improved schedule constants.

## Review / persistence boundary

This note reports a Driver-side author derivation and elementary exact-mass recomputation. Its mathematical content is reproducible from the formulas above. It is *not* independent of the prior r396/r398 research context, is not an accepted native Result or formal review disposition, and does not assert Task or mother-objective completion. Source/Activity association, if needed, must preserve actual project authorities and old contributor IDs.
