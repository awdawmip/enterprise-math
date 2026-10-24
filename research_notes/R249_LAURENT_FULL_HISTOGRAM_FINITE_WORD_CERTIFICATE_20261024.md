# R249 — Laurent finite-word certificate for full positive-BRC weight/effect histograms

**Author-side exact finite-model theorem — NOT a native X6 heartbeat theorem, Source Result, Working Truth or Foundation admission.**

## Question and precise scope

R248 proved full-effect-histogram all-future decidability when the reachable joint (weight,effect) key set is finite, but its positive one-state {I6,T1} loop already generates infinitely many translation effects: H_m(X)=(1+X)^m. This note gives a **strictly weaker sufficient condition than finite reachable keys** for a restricted translation-only BRC family.

Let S be n finite nonspatial control states, Σ a finite set of reusable packet letters, and π:S→C the declared terminal control observer. Every letter is a finite positive BRC edge collection (source s, target t, rational weight w>0, X6 integer translation T_delta with delta∈Z^6, positive integer branch count k). Exact alternatives sum multiplicities; serial .then multiplies w and k and composes translations, which add integer X6 vectors. The observation is the coalesced full histogram indexed jointly by (π(t), path weight w, total translation delta). This is **not** a path-ID/provenance-complete observation, degree≤2 moment compression, or proof of any physically legal X6 heartbeat. Serial packet count does not equal heartbeat time.

## Key-preserving Laurent embedding

Let P be the finite set of rational primes that divide the numerator or denominator of any edge weight. Positive rational products have unique valuation vectors ν(w)=(v_p(w))_{p∈P}∈Z^P. Set

R=Q[ Y_p^{±1} (p∈P), X_1^{±1},...,X_6^{±1} ],  K=Frac(R).

Associate to a weight/effect key the monomial χ(w,delta)=∏_{p∈P} Y_p^{v_p(w)} ∏_{i=1}^6 X_i^{delta_i}. The fundamental theorem of arithmetic and independent X6 translations imply χ is **injective**; χ(wv,delta+epsilon)=χ(w,delta)χ(v,epsilon). Laurent negative exponents retain reciprocal weights and negative native-chart translations.

For each letter a define M_a(s,t)=Σ_{edges s→t} k χ(w,delta) ∈R. Then, by induction on any finite word u, the coefficient of χ(W,Delta) in the t component of e_s M_u is **exactly** the coalesced positive BRC multiplicity of branches ending at t with full joint key (W,T_Delta): alternatives add, serial composition multiplies counts and keys. Let beta_c be the column indicator of final observed control label c. Equality of every polynomial e_s M_u beta_c and e_t M_u beta_c is thus *equivalent* to exact joint-key histogram equality for u.

## Theorem R249.1 (all-future iff length≤n−1)

For **any** two initial control states s,t under the declared translation-only, positive rational-weight finite-control packet family,

  [for every word u∈Σ*, H_s(u)=H_t(u)]
  iff
  [for every u with |u|≤n−1, H_s(u)=H_t(u)].

**Proof.** View the row difference α=e_s−e_t in K^{1×n}; this signed row is only an external *comparison certificate*, never a signed BRC path. Put W_j=span_K{α M_u:|u|≤j}. The recursion W_{j+1}=W_j+Σ_a W_j M_a holds by finite-word concatenation. If a stage stabilizes, W_{j+1}=W_j, every generator preserves W_j and all subsequent spans are the same. Otherwise dimension rises strictly. As dim_K K^n=n and W_0 has dimension1 when s≠t (0 if identical), W_{n−1} must already have stabilized. Hence any beta_c which annihilates all α M_u for |u|≤n−1 annihilates the invariant span and all future α M_u. The coefficient embedding equates this with all-future exact full-histogram equality. The other implication is immediate. QED.

Algorithm: enumerate the finitely many words of length≤n−1 and compare exact Laurent polynomials per control observation; alternatively build a K-linear row span with exact fraction-field Gaussian elimination and test each beta_c. No polynomial *bit-complexity* assertion is made; factoring large rational weights and multivariate expressions may be expensive. For comparing systems A and B via a disjoint union use n=n_A+n_B. Finite rational translation offsets can be cleared by a common denominator, still without claiming physical Cell admissibility.

**Strict limitation:** arbitrary nontranslation affine linear parts act nontrivially on prior displacements. Their semidirect-product effects generally do not commute; this Laurent reduction and n−1 statement have NOT been proved for those effects, signed/complex amplitudes, hidden path-label readouts or unrestricted native X6 dynamics.

## Sharp concrete three-state witness

Take one unit-weight unit-count packet a with edges 0→2/I6, 1→0/I6, 2→2/T_(1,0,0,0,0,0), and merge all terminal state labels. Its matrix is
M=[[0,0,1],[1,0,0],[0,0,X_1]].
For α=(1,-1,0), beta=(1,1,1)^T, we have α beta=0, α M beta=0, but α M² beta=X_1−1≠0. The shortest distinguishing word has length 2 = n−1; one more word has difference X_1(X_1−1).

## Why infinite support and equal total mass do not refute the theorem

In R248's one-state two-branch packet, full histograms (1+X)^m are Q-linearly independent as polynomials with increasing degrees, but the single row over the **field K=Q(X)** spans dimension one. Infinite coefficient support is compatible with finite *field-linear control rank*.

It is crucial NOT to put rational **weight as a coefficient**. One source state with two paths of weights 1 and 3 and another source state with two paths of weight 2 have equal path count 2 and equal total weighted mass 4, yet different full weight histograms. Their faithful prime-key polynomials are 1+Y_3 versus 2Y_2. The coarse evaluation Y_p→p collapses both to 4. Thus the prime valuation variables are needed to retain the full BRC (weight,effect) key.

## Exact evidence and research boundaries

The attached author-side `R249_verify.py` uses independent exact direct positive-joint-histogram and Laurent coefficient-dictionary evaluators. Local cold rerun reproduces its `R249_EXACT_REPORT.json`: 36 deterministic-seed models and 1,620 complete direct-versus-Laurent observations over words length0..3; the three-state shortest-length2 example (symbolic reachable row ranks 1,2,3); the coarse-weight collision; and R248's infinite-support family for m=0..12 (m12 support13, count4096). These finite checks are cross-checks; the arbitrary-word result follows from the proof, not their numerical coverage.

Source contracts actually read: global main@dfafd755b5cb9241523471b98b264f366e14d09b, P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (ACTIVE_LOCKED); enterprise-math main@f96092408f9747e8cdc499bd7b2a950901506bd5; `src/enterprise_math/brc_transport.py` blob be1debe367263931bd5e93fd750be3ed54624fe1; `src/enterprise_math/brc_control_port.py` blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8. Reuse: T0_BRC_AFFINE_EFFECT_TRANSPORT / brc.affine_effect_transport, algebraic interface used (REUSE_APPLIED); no original enterprise_math runtime import, R193 provenance embedding or physical rule test.

**Prior art/novelty:** Field-based weighted-automaton equivalence is classical; Stefan Kiefer, *Notes on Equivalence and Minimization of Weighted Automata* (2020), https://arxiv.org/abs/2009.01217 ; Nathanaël Fijalkow, *A polynomial time algorithm for the equivalence problem of weighted automata over a field* (2019), https://games-automata-play.github.io/blog/equivalence_weighted_automata/. This note is a typed BRC specialization and is *not* asserted novel without further literature screening.

**Control status:** Native `em_control_tasks`: CONTROL_QUOTA; native `em_session_start`: STATIC_READONLY_SCOPE_DENIED / operation_sent=false. No live owner/CLAIM verified, no authenticated native Researcher session, no accepted Result or independent Driver review. This file is a noncanonical author-side GitHub draft; it does not simulate a research activity, alter P000/worldview, or bypass native authority. Google Drive must not be used as an alternate route around that denial.

**Next R250:** For one nontrivial invertible/singular affine linear part, prove a faithful finite representation or find a bounded-word failure; independently execute exact `ControlPacket.from_edges/then` in a pinned package and resolve R193 branch provenance/native admissibility.
