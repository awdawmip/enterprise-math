# R257 — Unbounded future-safe provenance memory for positive BRC balance queries

**Date:** 2026-10-24. **Classification:** author-side mathematical proof, exact formal BRC example, **UNREVIEWED**. This is not a formal Task Result, R193-native theorem, or verified heartbeat dynamics.

## Provenance, fixed control, and scope

GLOBAL_KNOWLEDGE_V1 read and held at main **a59ee98ae1ce03ed11bfeeb73dc026a35adf04d2**. The project P000 projection is ACTIVE_LOCKED, original P000 Git blob **770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc** verified. Enterprise Math Source read snapshot **198677c40e0f8e7795ccc9229a872fc591e9272f**. The source docs/PORTABLE_RESEARCH_PROTOCOL.md and existing Affine/ControlPacket interfaces were read. This work consumes R256 at author draft commit **b2f5560ce85c5ff63a2e3e9bfff658ff4a10ce49**; the R256 regular-language query theorem is not repeated.

Research activity **RA-EMR4-20261024-1730-R257BAL** was registered and read back at main commit adfaccbee407da0f4dbbd13aff8e54cdef791c56; local contributor label EM-DIRECT-R257A4 is not an authenticated native Researcher-ID. No formal CLAIM is inferred. Native control dispatch request #6268 returned inner FAILED/TimeoutExpired. Original R193 source-token/observer/temporal-port semantics and legal six-axis heartbeat action mapping are still unverified. This is a declared *formal* positive-weight BRC model; time-step is a selector composition, not an empirically defined heartbeat interval. Signed D values below are **source-history counters**, not signed branch masses. The auxiliary signed affine displacement is not a final six-nonnegative-field Cell address.

## Frozen positive BRC and exact observer

Control Q={0,1,2}. Each q has exactly two distinct selector edges a=0,1 of positive weight 1 and path multiplicity 1. Edge triples (target q_a, linear sign eta_a, translation b_a) are:

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

The formal X6 affine effect is
\[
F_{\epsilon,k}(z)=\operatorname{diag}(\epsilon,\epsilon,1,1,1,1)z+k e_1,\quad \epsilon=\pm1,\ k\in\mathbb Z.
\]
The chronological BRC effect law is
\[
(q,\epsilon,k)\xrightarrow{a}(q_a,\eta_a\epsilon,\eta_a k+b_a),\qquad (q,\epsilon,k)_0=(0,1,0).
\]
A word w is observed through its complete terminal/effect triple O(w)=(q,epsilon,k), **not** through its ordered selector history. If two words have the same O and the same suffix u is appended, their new complete effects/terminals stay equal, because the edge law is a deterministic function of the current q and next selector. The underlying BRC path mass always remains positive.

Study the exact provenance Boolean query B(w)=1 iff the numbers of 0 and 1 selectors in w agree, with the associated integer counter D(w)=#0(w)-#1(w). A fixed final-time Boolean output can be stored in one bit, but the question here is how much **additional pathwise online state** besides the known complete O and current prefix length m is necessary to answer B(wu) accurately for every future common selector suffix u.

## Theorem A: exact positive joint transport

Let J_m(q,eps,k,d) be the positive integer count of all length-m selector words whose joint state is (O,D)=(q,eps,k,d). Initialize J_0(0,1,0,0)=1; all other entries zero. Every source edge a contributes

\[
\boxed{J_{m+1}(q_a,\eta_a\epsilon,\eta_a k+b_a,d+1-2a)\mathrel{+}=J_m(q,\epsilon,k,d).}\tag{1}
\]

**Proof.** The empty word satisfies the initial condition. Every nonempty word has a unique last edge a and unique prefix; chronological affine composition updates O exactly, and D(wa)=D(w)+1-2a updates the source count exactly. Conversely each recurrence summand represents exactly one valid positive path extension. Induction on m proves the complete joint histogram. Summing over d gives the complete endpoint/effect histogram; d=0 gives exactly the balanced source query count per effect fiber. Because every state has two selectors, the sum of all counts is exactly 2^m. There is no signed-weight or phase cancellation.

At depth m, q has 3 choices, eps 2, k at most 2m+1 possibilities, and d at most m+1 possibilities due to fixed parity. Hence <=6(2m+1)(m+1) joint atoms. One transition computes each next layer in O(m²) integer additions and layers through depth T in O(T³) integer additions; one final layer uses O(T²) counters. This is **arithmetic-operation** complexity; counts have at most T+1 bits, so bit complexity is not silently equated with operation count.

## Theorem B: an explicit unbounded future-distinguishable complete-effect fiber

Define three-letter words A=000 and B=101. Direct table composition gives

\[
O(A)=O(B)=(0,1,-1),\qquad D(A)=3,\ D(B)=-1.
\tag{2}
\]

Both are loops of control 0 with linear sign 1 and translation -1, so concatenating h of these blocks yields the same complete terminal/effect O=(0,1,-h), independently of the order of blocks.

For every prefix length m>=3 let h=floor(m/3), r=m-3h in {0,1,2}. Construct h+1 words

\[
\boxed{w_j=A^jB^{h-j}1^r,\quad 0\le j\le h.}\tag{3}
\]

A trailing selector 1 starting from q=0 moves to q=2, stays q=2 if repeated, multiplies the current affine sign by +1 and shifts translation by -1 each time. Thus *all* words (3) have the **identical full-effect observation**

\[
O(w_j)=(q_r,1,-h-r),\quad q_0=0,\ q_1=q_2=2.
\tag{4}
\]

Yet their provenance counters are pairwise distinct:

\[
\boxed{D(w_j)=4j-h-r.}\tag{5}
\]

For each j choose the distinguishing suffix u_j=1^{D(w_j)} if D(w_j)>=0, and u_j=0^{-D(w_j)} otherwise. Its counter contribution is -D(w_j), so B(w_j u_j)=1. For every i != j,

\[
D(w_i u_j)=D(w_i)-D(w_j)=4(i-j)\ne0,
\quad B(w_i u_j)=0.
\tag{6}
\]

All complete-effect observations O(w_i u_j) are still equal for fixed j, because they started in the same O fiber and were extended by the same suffix u_j. Therefore any annotation which is pathwise correct under **all** future operations must separate all h+1 words (3). This proves an intrinsic all-future query-information lower bound even with the *complete* six-axis formal affine effect available.

Let b_m denote the minimal worst-fiber number of fixed-width extra annotation bits at prefix length m, with m and O already known, for all-future balance-query fidelity. Equations (3)-(6) prove the lower bound

\[
b_m\ge\left\lceil\log_2(\lfloor m/3\rfloor+1)\right\rceil.
\]

Conversely maintaining the exact signed counter D suffices for all futures by the recurrence D(wa)=D(w)+1-2a. At known length m it belongs to the m+1-element set {-m,-m+2,...,m}, hence can be encoded in ceil(log2(m+1)) bits. Therefore the **proved bound is**

\[
\boxed{
\left\lceil\log_2(\lfloor m/3\rfloor+1)\right\rceil
\le b_m\le\left\lceil\log_2(m+1)\right\rceil,\quad m\ge3.
}\tag{7}
\]

In particular b_m=Theta(log m), and **no finite-state query monitor** combined with this declared exact effect observation can preserve balance-query truth for every future suffix at arbitrarily large prefix lengths. Equation (7) is an asymptotically sharp order, **not** a formula for the exact b_m and **not** a theorem about the unknown actual R193 source grammar or an arbitrary weighted-linear observer.

**Small explicit certificate (m=6).** Words 101101, 000101, 000000 share O=(0,1,-2) but have D=-2,2,6. All currently answer "not balanced", so even remembering the **current** Boolean answer is insufficient: their future suffix behavior differs, requiring at least 2 extra bits in this fiber.

## Exact evidence and validation scope

R257_verify.py is an author-side Python exact-integer dynamic program and exhaustive small-word cross-check; R257_independent.cpp is a separately written exact C++17 implementation with boost::multiprecision::cpp_int. Both independently check all depths 0..48 for positive counts summing to 2^m, exhaustively compare direct enumeration of all 8,191 selector words at depths 0..12 to joint DP, and test the full-effect and distinguishing suffix certificates for m=3,6,12,24,48. Both reported **PASS**. The depth-48 count is 281474976710656 positive paths, represented in 7681 nonzero joint atoms. The infinite-horizon conclusion rests on the explicit proof (2)-(7), not the finite checks. These programs are *not* the original enterprise_math module.

## Status, reuse and one next research unit

BRC was concretely used: serial affine effect law + alternatives retaining positive path multiplicity; added source-counter product monitor. Reuse state **REUSE_APPLIED** for the typed affine/histogram laws. The new provenance query requires **EXTEND_EXISTING_TOOL** if native correspondence is ever established; **REUSE_EXECUTED** of original native package is not claimed. The resulting mathematical statement is author-side, not formal Source Result or independent Driver/Steward acceptance. Live owner and winning CLAIM not established, because the actual control-dispatch inner receipt was FAILED/TimeoutExpired.

**R258 next:** retrieve the real R193 path-label and observer/time-port grammar at an immutable source pin and prove a word-preserving or explicitly quotienting bridge. If the actual query is regular, compute its future-safe right-congruence/minimal monitor; if it demands unbounded memory, build an exact same-effect fiber with pairwise distinguishing admissible suffixes. Run Source-matched actual ControlPacket.from_edges/then/EffectHistogram on exact small inputs when available; distinguish native execution, physical legitimacy and author-side mathematical correctness. Preserve P000 ACTIVE_LOCKED and do not convert this sample into unverified R193/native claims.
