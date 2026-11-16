# R216 — Autocorrelation spectrum and first distinguishing horizon for Green-J principal ideal cardinalities

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Scope and immutable scientific provenance

Observer algebra: the finite chronological paired-event monoid \(J_{m,k,L}\) from R200–R215, over \(A=[m]\times(\{0\}\cup[k])\), \(m\ge1,k\ge0,L\ge1\), alphabet size \(a=m(k+1)\). State \(F(w)\) retains the order of last appearances of selected sources and the last \(\min(L,|w|)\) complete paired events. This is a typed finite observer algebra; it does not simulate native physical BRC propagation.

Frozen scientific input: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Direct antecedents: R213 Green ideal membership at \`26bccd30c4afb00bf143acd7627eff9cdf954693\`, R214 quotient at \`1b7508f9f7f5b70f79052b7966f21221ba1f1ecf\`, and R215 KMP/Stirling cardinalities at \`71e9d86c4fea71a0ff1b2da66fe2b5656998a68b\`. Original R215 bytes are retained.

P000's six native spatial axes, twelve signed directions and independent time, as well as the ACTIVE residual-fidelity worldview, are unchanged. The principal-ideal cardinalities below are specified readouts; preservation of full BRC effects and provenance remains separately typed.

## Theorem 1 — Rational avoidance generating function determined by the border spectrum

Fix a nonempty short event word \(u\in A^h\), \(1\le h<L\). For every shift \(0\le d<h\), set \(c_d=1\) when \(u[0:h-d]=u[d:h]\), and \(0\) otherwise. In particular \(c_0=1\). Define the border/autocorrelation polynomial

\[
C_u(z)=\sum_{d=0}^{h-1}c_dz^d.
\]

Let \(A_u(n)\) count length-\(n\) alphabet words avoiding \(u\) as a contiguous factor, including \(A_u(0)=1\), and set \(A_u(z)=\sum_{n\ge0}A_u(n)z^n\). Then the following *formal power series identity* holds over integers for every alphabet size \(a\ge1\):

\[
\boxed{A_u(z)=\frac{C_u(z)}{z^h+(1-az)C_u(z)}}.\tag{1}
\]

**Proof.** Define \(F(z)\) as the generating series of words whose *first* occurrence of \(u\) ends at the very last position. Each word avoids \(u\), or has a unique prefix of this kind followed by an arbitrary suffix. Hence

\[
1=(1-az)A_u(z)+F(z). \tag{2}
\]

All words ending in \(u\) have generating series \(z^h/(1-az)\). Split such a word after the unique prefix ending at its first occurrence. If the final occurrence overlaps this first occurrence, its starting offset is a unique \(d<h\), possible exactly when \(c_d=1\); the appended \(d\) letters are uniquely determined by \(u\). If it does not overlap, the continuation is an arbitrary word followed by \(u\), counted by \(z^h/(1-az)\). Therefore

\[
\frac{z^h}{1-az}=F(z)\left(C_u(z)+\frac{z^h}{1-az}\right). \tag{3}
\]

Solving (3) for \(F\) and substituting in (2) gives (1). Denominators have constant coefficient \(1\), so all manipulations are valid in \(\mathbb Z[[z]]\). QED.

## Theorem 2 — Exact recurrence without an alphabet-size loop

Write \(D(z)=z^h+(1-az)C_u(z)=\sum_{i=0}^{h}d_iz^i\), extend \(c_i=0\) for \(i\ge h\), and note \(d_0=1\). Then

\[
d_i=c_i-a c_{i-1}+\mathbf1_{i=h},\quad1\le i\le h,
\]

\[
\boxed{A_u(n)=c_n-\sum_{i=1}^{\min(h,n)}d_i A_u(n-i)}.\tag{4}
\]

This follows directly from \(D(z)A_u(z)=C_u(z)\). A naive border builder takes \(O(h^2)\) symbol comparisons; a prefix-function builder takes \(O(h)\). All avoidance coefficients through \(n=L-1\) require \(O(hL)\) integer operations and \(O(h+L)\) integer storage, with no multiplicative factor \(a\) in the recurrence. This improves the explicit-letter \(O(a h L)\) KMP-DP work term of R215 for the same scalar query. Arithmetic bit costs remain dependent on \(L\) and \(a\): \(0\le A_u(n)\le a^n\), hence for \(a\ge2\) each count fits in at most \(\lceil n\log_2 a\rceil+1\) bits, while \(|d_i|\le a+1\). No measured time advantage is asserted.

For the original observer monoid, R215 gives for short \(u\) of support size \(r\):

\[
|J_LuJ_L|=T_r(L)+\sum_{n=0}^{L-1}(a^n-A_u(n)),
\]

where \(T_r(L)\) is R215's exact Stirling-fibre sum. Thus the recurrence directly replaces its pattern-automaton subroutine without changing full-state semantics.

## Theorem 3 — Equality for all cutoffs and the first distinguishing horizon

Let \(u,v\in A^h\) be two nonempty words of the same length \(h\) and with the same number \(r\) of selected (non-neutral) source tags. Fix the alphabet \((m,k)\); vary the observer-tail cutoff \(L>h\), treating the same two literal words as short states of \(J_{m,k,L}\).

The principal right ideals have equal cardinality at every such cutoff (R215). The principal **two-sided** ideal cardinalities agree for every cutoff \(L>h\) **if and only if** \(C_u=C_v\):

\[
\boxed{\left(\forall L>h:\ |J_LuJ_L|=|J_LvJ_L|\right)\iff C_u(z)=C_v(z)}.\tag{5}
\]

If the first unequal coefficient of \(C_u,C_v\) occurs at shift \(d\in[1,h-1]\), then the avoidance counts first differ in degree \(h+d\), where

\[
A_u(h+d)-A_v(h+d)=c_d(u)-c_d(v)\in\{-1,+1\}. \tag{6}
\]

The two-sided ideal counts therefore first differ by exactly one at \(L=h+d+1\). They agree for the earlier cutoffs \(h<L\le h+d\).

**Proof.** Let \(D_u=z^h+(1-az)C_u\), and \(D_v\) analogously. Subtracting (1) gives

\[
\boxed{A_u(z)-A_v(z)=\frac{z^h(C_u(z)-C_v(z))}{D_u(z)D_v(z)}}.\tag{7}
\]

Both denominators are units of \(\mathbb Z[[z]]\) with constant coefficient \(1\), so the first nonzero degree and coefficient are as stated. Since both words have the same source support *cardinality* \(r\), the full-sector term \(T_r(L)\) cancels in the difference of their two-sided ideal sizes. Taking cumulative differences through length \(L-1\) yields the exact threshold and unit difference. When \(C_u=C_v\), (7) makes their avoidance sequences equal. Conversely if the two-sided cardinalities are equal at all cutoffs, successive cumulative sums yield equality of all avoidance coefficients; (7) then forces \(C_u=C_v\) in the integral formal-power-series domain. QED.

**Exact witness.** In the two-letter alphabet \(A=\{0,1\}\), set \(m=1,k=1,h=2\), \(u=11\), \(v=10\). Both have selected-source support size 1, while \(C_{11}=1+z\) and \(C_{10}=1\). Their avoidance sequences begin respectively \(1,2,3,5,8\) and \(1,2,3,4,5\), first differing at length 3. In \(J_{1,1,4}\), R215's full calculation yields \(|J(11)J|=20\), \(|J(10)J|=21\) and both right ideals of size 19. At \(L=3\) the two-sided cardinalities coincide. Border-spectrum equality is a cardinality property; additional composition/observer preservation requires a separate congruence proof.

## Exact verification and reproducibility

The standalone Python 3 standard-library verifier \`R216_border_spectrum_exact_check.py\` independently compares (4) against a prefix-automaton DP and exhaustive literal-word enumeration. Evidence \`R216_verification.json\` records **330 exhaustive pattern models**, **916,710 enumerated literal input words**, **3,515 same-border pair checks**, **3,484 first-distinguishing-coefficient pair checks**, and **8 cases over the full X6 84-letter event alphabet** against independent automaton DP through length 28. It also recomputes the two-sided-ideal witness at cutoffs \(L=3,4\). All executed assertions passed.

The symbolic proofs cover arbitrary admissible \(m,k,L,u,v\); finite tests corroborate the explicit recurrences and witness. Tests are abstract exact integer observer combinatorics, not native physical propagation. **Independent Review=NOT_REVIEWED; native installed BRC EffectHistogram integration=NOT_EXECUTED.**

## Open mathematical and engineering frontier

1. Use R214's support-grouped 21-bit full-state code to extract \(r\) and \(T_r\) with partial decoding; give preprocessing, bit-complexity and output-recovery costs.
2. Determine the *future-composition-closed syntactic congruence* for the intermediate language of principal-ideal cardinalities. A border-spectrum equality at fixed \(L\) does not alone establish this stronger quotient.
3. Execute a real typed \`EffectHistogram\` BRC integration, preserving signed/port/source branch identities, exact positive rational weights, multiplicities and R203 joint cross moments, and measure runtime/serialization rather than infer it from arithmetic-operation counts.

No new formal Task CLAIM, accepted Result, independent Review or Foundation promotion is asserted by this independent research output.
