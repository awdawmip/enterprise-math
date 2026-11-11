# R730 — exact BRC support interval for admitting one conflict-port triad

Date: 2026-11-12. Parent: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen scientific inputs: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Direct dependency: R728 candidate port-conflict model, Draft PR #2110, author commit \`b825881b426fbced70ea0c38ec6146ac7815f688\`. The separately authored R729 named-S3 observer work in PR #2112 is not duplicated here.

## Declared object and count

At one selected X6 Cell, retain distinguishable source IDs, six original signed axis-family labels and port provenance. The following counts only the candidate three-*distinct-axis* source-incidence partitions, independently of the unresolved native \`TRIADIC_CLOSURE_E\` and V29/V39 event predicates. This is an exact finite nonnegative source-branch BRC combinatorial carrier; its multiplicities never erase labeled source IDs.

Let \`a=(a0,...,a5)\` be nonnegative integer source counts with \`sum a_i=3m\`. Old port-conflict hypergraph \`H\` contains every three-distinct-axis triple except \`012,013,014,015\`: axes 0 and 1 share a candidate exclusive port, and 2,3,4,5 have separate ports. Let \`T={0,1,k}\`, where \`k\` is any of 2,3,4,5. Opening exactly this candidate incidence produces \`H+T\`. Each branch partitions all distinguishable source IDs into \`m\` unordered triples.

Define the provenance-weighted branch polynomial
\[
 F_{a,k}(z)=\sum_{P\text{ is }(H+T)\text{-admissible}}z^{n_T(P)}
 =\sum_{s=0}^{m} C_s(a,k) z^s,
\]
where \`n_T(P)\` is the number of triples of type \`T\`. Distinguish \`F(1)\` (total count) from the full \`C_s\` histogram (retained provenance).

## Theorem 1 — sharp *contiguous* support of the new type

Put \`B=a0+a1\`, and
\[
s_{\min}=\max(0,B-m),\qquad
s_{\max}=\min\left(a0,a1,a_k,m,\ \{m-a_j:j\in\{2,3,4,5\}\setminus\{k\}\}\right).
\]
If \`a_k>m\` or \`s_min>s_max\`, then \`F=0\`. Otherwise
\[
 \boxed{\quad C_s(a,k)>0\quad\Longleftrightarrow\quad
 s\in\{s_{\min},s_{\min}+1,\ldots,s_{\max}\}\quad}.
\]
In particular, every integer between the lower and upper bounds occurs, with no internal gaps. For \`m=0\`, the zero vector has \`F=1\` and the formula gives \`s=0\`.

**Proof.** The R728 exact edge-admission transfer identity gives
\[
 C_s(a,k)=\frac{(a0)_{\underline{s}}(a1)_{\underline{s}}(a_k)_{\underline{s}}}{s!}
 L_H(a-s(e_0+e_1+e_k)).
\]
For integral \`0<=s<=min(m,a0,a1,a_k)\`, the prefactor is strictly positive. The residual branch partition has \`m-s\` triples, block populations \`B-2s\`, \`a_k-s\` and \`a_j\` for \`j\notin\{0,1,k\}\`. By R728's proved complete port-block matching criterion, its labeled partition count is positive if and only if each residual block count is at most \`m-s\`. Those inequalities reduce exactly to
\[
 s\ge B-m,\quad a_k\le m,\quad s\le m-a_j\ (j\notin\{0,1,k\}).
\]
Combining with the nonnegative-source constraints yields the stated integer interval, and the block construction guarantees a partition for *every* integer therein. QED.

**Consequence.** If \`B>m\` and the interval is nonempty, the first new branch appears at order \`B-m\`, even when all smaller orders contribute zero. In this exact finite model, the minimum required number of previously forbidden port-triples is explicitly computable without enumerating partitions.

## Theorem 2 — equal totals with arbitrarily different compulsory new-triple depths

For all integers \`m>=1\` and \`1<=r<=m\`, set \`k=2\` and
\[
a^{(m,r)}=(m,r,m,m-r,0,0).
\]
Then \`s_min=s_max=r\` and
\[
 \boxed{F_{a^{(m,r)},2}(z)=(m!)^2 z^r}.
\]

**Proof.** The conflicting block contains \`m+r\` sources, hence every admissible partition uses at least \`r\` new \`012\` triples. Axis 1 has exactly \`r\` sources, hence no partition can use more than \`r\`. After those \`r\` triples, the remaining \`m-r\` triples must all be \`023\`. Distinguishable source IDs on axes 0,2 can each be bijectively paired with the appropriate axis-1 or axis-3 IDs, yielding exactly \`m!\` independent matchings in the two companion families: \`(m!)^2\` total. Equivalently insert \`s=r\` in the exact transfer formula:
\[
\frac{(m)_{\underline r}\,r!\,(m)_{\underline r}}{r!}
 ((m-r)!)^2=(m!)^2.
\]
QED.

For example, at \`m=4\`, \`a^{(4,1)}=(4,1,4,3,0,0)\` and \`a^{(4,4)}=(4,4,4,0,0,0)\` both give the same old count \`F(0)=0\` and the same fully opened count \`F(1)=576\`, but their branch polynomials are \`576z\` and \`576z^4\`. An allowed *candidate observer* that caps the number of newly opened triple types at one returns 576 vs 0. Thus the pair of before/after total counts loses an exactly specified future-relevant multiplicity-order residual. The cap is a declared observer test, **not** a claimed V29/V39 law.

## Verification and limits

The adjacent Python 3 standard-library verifier exhausts **8,708** six-family occupation vectors with \`m=1..4\`, and each of four \`k\` choices: **34,832** exact configurations. An independent source-ID pivot recurrence evaluates \`L_H\` and \`L_{H+T}\`; it checks both the interval support versus positive exact transfer coefficients and the identity \`L_{H+T}=\sum_s C_s\`. It also checks all \`1<=r<=m\` for \`m=1..8\`. Output marker \`R730_EXACT_SUPPORT_AND_HIDDEN_ORDER_PASS\`; machine-readable counts are in the companion JSON.

The polynomial supplies an exact provenance-preserving branch-count observable for the *candidate* port-exclusion hypothesis. To apply it to the locked native physical model, extract the real legal Cell/Link/Port event, the actual \`TRIADIC_CLOSURE_E\` incidence predicate, V29 PASS/TRANSFER or V39 flow j, native sign/port/branch identity and update order at the same frozen science pin. No native physical trajectory, stability acceptance or actual port-opening event was asserted by this verification.

Next discriminating question: Is the actual native admissible triad-incidence graph locally describable by \`H+T\` for at least one lawful event? If yes, measure whether the event's source-branch observer retains \`n_T\` or only \`F(1)\`; if not, record one exact counterevent with its admissibility witness and reformulate the incidence graph. Preserve R728 and R729 as independently sourced existing candidate results.