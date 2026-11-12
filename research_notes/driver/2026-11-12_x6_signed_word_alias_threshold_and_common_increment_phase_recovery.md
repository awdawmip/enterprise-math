# X6 signed-step alias threshold and registered two-phase recovery

Date: 2026-11-12 (Asia/Shanghai)  
Scientific classification: exact auxiliary mathematical theorem / scoped candidate coordinate-and-observer model.  
Scientific authoring lane: RESEARCH_DRIVER; this note is NOT a Source-native Result, independent DR, TASK completion, or P000 promotion.

## 1. Scientific source, domain, and improvement

This note continues the pre-existing exact result at research_notes/driver/2026-11-12_x6_unregistered_positive_microsteps_sharp_depth_alias_threshold.md (Git blob 56a896fd2f24741dd6d9a43b90f56b488e631c6c), which assumed unknown **positive-only** native microsteps. The P000 V5 signed X6 Cell torsor, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, instead provides **twelve signed primitive coordinate adjacency directions**, so signed-step modeling is a direct, separately typed next question.

The statements below are about raw signed charts, the min-zero relative observer, and *candidate* signed-permutation phase actions. They preserve ordered native word/branch provenance outside the endpoint observer, and do not prescribe a Heartbeat force or time evolution law. The common-increment theorem names a specific correlation hypothesis rather than silently assuming all probes represent independent physical histories.

Let \(n\ge2\), \(D=(1,\ldots,1)\in\mathbb Z^n\), and
\[
q(z)=z-\min_i(z_i)D.
\]
Fix a known signed permutation \(g\), put \(\varepsilon=gD\), and assume \(\varepsilon\) has exactly \(k\in\{1,\ldots,n-1\}\) negative signs. Fix \(r=q(z_0)\); the original raw chart is \(z_0=r+hD\) with integer hidden common depth \(h\). Let
\[
\mathcal W_M=\left\{b\in\mathbb Z^n:
 b=\sum_{\ell=1}^{M}\sigma_\ell e_{i_\ell},\
 \sigma_\ell\in\{-1,+1\},\ i_\ell\in\{1,\ldots,n\}\right\}
\]
be the set of **net occurrence displacements** reachable by a word of exactly \(M\) signed primitive steps. The observer reads
\[
Y_g(h,b)=q(gr+h\varepsilon+b),\quad b\in\mathcal W_M.
\]
The actual ordered word is not identified with \(b\).

## 2. Exact two-word difference lemma

For any integer \(v\), there exist \(b,b'\in\mathcal W_M\) with \(b-b'=v\) if and only if
\[
\boxed{\|v\|_1\le 2M,\qquad \|v\|_1\equiv0\pmod2.}
\]
Indeed, concatenate an \(M\)-step word realizing \(b\) and the sign-reversed \(M\)-step word realizing \(-b'\): this is a signed primitive walk of length \(2M\) to \(v\). Conversely, an integer vector is reachable by exactly \(2M\) signed steps precisely when its \(\ell^1\) norm does not exceed \(2M\) and has the same parity; split that walk after \(M\) steps and reverse the sign of the second half. The reverse-direction pair padding realizes all larger matching-parity lengths.

Equality \(Y_g(h,b)=Y_g(h',b')\) holds if and only if there is an integer \(c\) with
\[
d\varepsilon+(b-b')=cD,\quad d=h-h'.
\]
Thus the necessary and sufficient criterion for two given depths to share *some* readout at length \(M\) is the existence of \(c\in\mathbb Z\) such that
\[
\boxed{(n-k)|c-d|+k|c+d|\le2M,\qquad
(n-k)|c-d|+k|c+d|\equiv0\pmod2.}
\]

## 3. Sharp signed-step depth threshold

**Theorem A.** Let \(m=\min(k,n-k)\). For any fixed \(r,g\) as above and any two distinct depths \(h,h'\), their attainable observer readout sets intersect if and only if
\[
\boxed{M\ge m\,|h-h'|.}
\]

**Proof.** The weighted absolute-value expression above satisfies
\[
(n-k)|c-d|+k|c+d|\ \ge\ 2m|d|
\]
for every real \(c\). Its integer minimum is achieved at \(c=d\) if \(k\le n/2\), or at \(c=-d\) if \(k\ge n/2\). At these choices the required difference vector has exactly \(m\) nonzero coordinates, each equal to \(+2d\) or \(-2d\); its \(\ell^1\) norm is \(2m|d|\), automatically even. The two-word lemma therefore gives an exact collision iff \(2M\ge2m|d|\). QED.

For unrestricted depths \(h\in\mathbb Z\) we obtain the stronger full-map statement:

**Corollary A1.** For \(M\ge0\), the map \((h,b)\mapsto Y_g(h,b)\) from \(\mathbb Z\times\mathcal W_M\) is injective precisely when
\[
\boxed{M<m=\min(k,n-k).}
\]
When \(M\ge m\), Theorem A with \(d=1\) supplies a depth collision. When \(M<m\), all nonzero \(d\) are excluded; fixed-depth collisions are also impossible because the difference \(cD=b-b'\) for \(c\ne0\) needs at least \(n\) primitive combined steps, whereas \(2M<2m\le n\).

**Fixed-depth caveat, with an exact positive result.** With \(h\) already known, recovery of the *net displacement* \(b\) from \(Y_g\) is unique iff \(M<F(n)\), where
\[
F(n)=\begin{cases}n/2,&n\text{ even},\\n,&n\text{ odd}.\end{cases}
\]
For equal depth, \(b-b'=cD\). The two-word lemma gives minimal nonzero \(|c|=1\) when \(n\) is even, and \(|c|=2\) when \(n\) is odd, yielding the stated threshold and exact witnesses. Thus for an arbitrary nonempty depth set \(H\subset\mathbb Z\), if \(\delta=\min\{|h-h'|:h\ne h',h,h'\in H\}\) (or \(+\infty\) for a singleton), then full \((h,b)\) recovery occurs precisely when
\[
M<\min(m\delta,F(n)).
\]
Ordered-path words can still be distinct even when their net displacement is unique.

For six native axes, the mixed-sign phase thresholds are therefore

| negative signs \(k\) | signed-word \(M_{\mathrm{crit}}\) | earlier positive-only \(M_{\mathrm{crit}}\) |
|---:|---:|---:|
| 1, 5 | 1 | 5 |
| 2, 4 | 2 | 8 |
| 3 | 3 | 3 |

An explicit X6 phase-one collision has \(\varepsilon=(-1,1,1,1,1,1)\): depth \(h=1\) with the signed word \(+e_1\) and depth \(h'=0\) with signed word \(-e_1\) yield the same relative readout \((0,1,1,1,1,1)\) when \(r=0\). The witnesses at \(M=m\) can always be chosen as distinct-axis all-plus versus all-minus words on the minority-sign coordinates, so each is individually **no-immediate-reversal compliant**. A common signed suffix extends ordinary signed-word collisions to every larger \(M\); additional transition restrictions must be checked at their own scope.

## 4. Independent phase probes versus one registered common displacement

For independent unknown signed words \(b_t\in\mathcal W_{M_t}\), sampled phase observations
\[
Y_t=q(g_t r+h\varepsilon_t+b_t)
\]
share the same hidden \(h\) but have independently variable net displacements. Theorem A yields:

**Theorem B (independent signed probes).** With unrestricted \(h\), the collection determines hidden depth uniquely if and only if at least one mixed-sign probe satisfies
\[
M_t<\min(k_t,n-k_t).
\]
If every probe is individually depth-ambiguous, all can collide simultaneously at the **same gap \(d=1\)** because their word choices are independent. There is no signed-word analogue of the positive-only divisibility-based joint rescue without additional restrictions.

For the signed triad candidate \(R(z_1,z_2,z_3,z_4,z_5,z_6)=(-z_3,z_1,z_2,z_4,z_5,z_6)\), at phase 1 \(k_1=1\), phase 3 \(k_3=3\). The previous positive-only independent probe pair \((M_1,M_3)=(5,3)\) was uniquely depth-recovering; in the unrestricted signed-word model it **does** have a simultaneous collision. At \(r=0\), take depths 1 versus 0 and the following net displacement witnesses:

- phase 1: \(b_1=(1,4,0,0,0,0)\) versus \(b_1'=(-1,4,0,0,0,0)\); common readout \((0,5,1,1,1,1)\);
- phase 3: \(b_3=(1,1,1,0,0,0)\) versus \(b_3'=(-1,-1,-1,0,0,0)\); common readout \((0,0,0,1,1,1)\).

These are distinct *candidate observer models*, not a contradiction in the positive-only theorem.

Now impose a **different, stronger correlation hypothesis**: both registered phase readouts share the *same unknown net signed displacement* \(b\) in the same registered axes,
\[
Y_t=q(g_t r+h\varepsilon_t+b),\qquad
Y_s=q(g_s r+h\varepsilon_s+b).
\]
The coordinate phase maps \(g_t,g_s\) and the initial relative chart \(r\) are known. Such a pair need not represent two time-separated physical events; it can be a controlled pair of phase reconstructions of one shared unknown increment.

**Theorem C (correlated common-increment recovery).** If
\(\varepsilon_t-\varepsilon_s\notin\mathbb ZD\), the two readouts uniquely determine the hidden integer depth \(h\), **for any \(b\in\mathbb Z^n\), at any word length, including unbounded signed-word uncertainty**. Explicitly, set
\[
w=Y_t-Y_s-(g_t-g_s)r,\quad
a=\varepsilon_t-\varepsilon_s.
\]
For any \(i,j\) with \(a_i\ne a_j\),
\[
\boxed{h=\frac{w_i-w_j}{a_i-a_j}.}
\]

**Proof.** Each min-zero normalization changes its raw argument by an integer multiple of \(D\). Hence
\(w=h(\varepsilon_t-\varepsilon_s)+\lambda D\)
for some integer \(\lambda\), because the **same \(b\)** cancels. Coordinate subtraction eliminates \(\lambda\) and gives the formula. Any other depth with the same readouts would have zero product with the nonzero quotient class of \(\varepsilon_t-\varepsilon_s\), which is impossible in the torsion-free quotient \(\mathbb Z^n/\mathbb ZD\). QED.

For two distinct *mixed-sign* patterns \(\varepsilon_t\ne\varepsilon_s\), their difference is necessarily non-diagonal, so this condition holds. For X6 \(R^1D=(-1,1,1,1,1,1)\) and \(R^3D=(-1,-1,-1,1,1,1)\), the shared-displacement two-phase observer determines \(h\) for arbitrary net signed paths. It need not determine \(b\) or the ordered word: for X6, even at known \(h\), \(M\ge3\) admits \(b-b'=D\) with two distinct signed words of length 3.

Theorem C concerns registration of a *common* unknown increment. A genuine evolving Heartbeat path will need its actual phase-to-phase transport/correlation law before Theorem C can be applied to time-separated readouts.

## 5. Exact computation audit

Using integer-only reachable-displacement sets by breadth-first signed unit-step recurrence, the six-axis single-phase check at all \(k=1,\ldots,5\) and lengths \(0\le M\le\min(k,6-k)\) examined depth choices 0 and 1: no input collision below the theorem's threshold, and a distinct-depth collision at each critical length. The \(M=3,k=3\) case also has a fixed-depth displacement alias; the explicit distinct-depth witness above remains valid.

For the same-unknown-displacement X6 two-phase case, enumerating all \(b\in\mathcal W_M\) and depths \(h=0,1,2,3\) at \(M=0,1,2,3,4\) covered 5,500 input records, with **zero cross-depth collisions**. Fixed-depth aliases appeared at \(M=3\) and \(4\), consistent with the separate net-displacement threshold. Exact example pairs at phases 1 and 3 were recomputed componentwise, without floating point. The universal claims are established by the algebraic proofs rather than these finite checks.

## 6. Mathematical integration and next discriminating unit

This result refines the previous positive-only X6 threshold by replacing a representation-specific semigroup with the P000-supported signed primitive coordinate alphabet. Under unrestricted signed words, early depth aliasing is sharper; under a *registered shared displacement*, two distinct phase-sign patterns recover depth without needing to know the displacement. These are compatible information theorems for different evidence/correlation interfaces.

Next independently executable scientific test: read an exact current Source-pinned Heartbeat/triadic update candidate, identify whether its admissible path language is positive-only, signed, no-backtracking, or state-constrained, and whether its phase readouts share a provably transported increment. Evaluate the relevant difference-set condition and preserve full ordered BRC path histories where future operations require them. Route the new theorem to a legally claimed X6 Researcher activity if/when such activity is current; do not replace the Researcher or backdate a Result.

Source lineage: P000 V5 signed native directions; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; previous X6 signed rotation/time and positive-only alias results. Existing authors and prior proofs retain independent provenance.