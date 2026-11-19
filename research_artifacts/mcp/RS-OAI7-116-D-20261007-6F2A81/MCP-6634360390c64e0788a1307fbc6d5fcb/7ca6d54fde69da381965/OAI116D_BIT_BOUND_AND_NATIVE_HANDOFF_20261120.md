# OAI116-D | Proven bounded bit cost, source boundary, handoff

Status: own-session author-level mathematical result, **not independent review or working-truth admission**. Task \`RS-OAI7-116-D-20261007-6F2A81\`; explicit characteristic-zero division-free formulas, rational coefficient cost model.

## Results

1. **Rational generator construction.** At \(d=2ns^2\) (for \(ns\ge2\)), the pinned external generator has entries
\[
(T_i)_{r,q}=\frac{(-1)^{r-q-1}}{r\,i^{r-q}}\quad(0\le q<r<d), \qquad 0\text{ otherwise}.
\]
The integer \(M=d!(n!)^d\) clears every denominator. Its bit length is at most \(d\log_2 d+dn\log_2n+1\) (take \(0\log0=0\)), polynomial in \(n,s\).

2. **Full binary-encoded rational formula evaluation.** For at most \(s\) total formula-tree gates, scalar leaves \(p/q\) with \(|p|,q\le2^H\), assign each subtree denominator \(K=\prod_{\text{scalar leaves}}q\cdot M^{\#\text{variable leaves}}\) and integral numerator matrix \(Z\). For addition \(Z=Z_AK_B+Z_BK_A\); for ordered multiplication \(Z=Z_AZ_B\). Set \(U=\max(H,\lceil\log_2 M\rceil)\), \(W=U+\lceil\log_2d\rceil+2\). Induction by subtree gate count \(k\) proves \(|Z_{ab}|\le2^{kW}\) and \(K\le2^{kU}\). Thus \(O(sd^3)\) schoolbook integer matrix operations, \(O((sW)^2)\) bit work per integer multiplication, suffice. Construction, evaluation, input encoding, and arbitrary-field oracle evaluation have separate cost statements.

3. **Explicit rational-labelled DAGs.** If an acyclic branching program has \(m\) vertices, \(E\) explicit affine-labelled edges, and coefficient height \(H\), take \(D\) as the product of all coefficient denominators and \(C=DM\). Each evaluated edge has an integral numerator over \(C\). Compute exact-length path layers \(\ell=0,\dots,m-1\), with integer recurrence
\[
Z_{v,\ell+1}=\sum_{e:v\to w}(C L_e(T))Z_{w,\ell}.
\]
The source output is \(\sum_{\ell<m}Z_{\mathrm{src},\ell}/C^\ell\). Because a DAG path has length \(<m\), the algorithm has \(O(mEd^3)\) integer matrix operations and polynomial operand heights. No monomial enumeration or DAG-to-formula unrolling is needed.

4. **Shared-circuit counterexample to size substitution.** The \(k+1\)-gate squaring DAG \(g_0=x_1,\ g_{j+1}=g_jg_j\) computes \(x_1^{2^k}\). A strictly triangular \(d\)-matrix satisfies \(T_1^d=0\). Therefore for \(2^k\ge d\), this nonzero circuit vanishes on the formula-sized nilpotent tuple. At \(n=1,k=10\), the incorrectly substituted bound \(d=2n(k+1)^2=242\) is smaller than \(1024\). This rules out that **specific substitution**, not all potential circuit hitting sets.

5. **Finite check.** Direct exact fractions give \(([T_1,T_2]e_0)_3=-1/24\) for \(d=4,6\); for \(d=3\) the vector vanishes. The sample only checks ordered-word sensitivity, not the external independence or multiplicity theorem.

## Source and continuation

Pinned original: \`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a\`, \`build/formula-systems.tex\` (blob 8a0db831dd4a7142ece2b935de0ba256ef5e30fc), \`build/construction.tex\` (blob 0abc841a6a0263f050c93ea926cc6c0cece05e53), \`build/introduction.tex\` (blob bbbfbd3ff0bf7ed812cf20d23734ed9dac4bc4d6). These are external, not accepted Enterprise Math results.

Companion detailed derivation: \`OAI116D_RATIONAL_BIT_BUDGET_AND_CIRCUIT_BOUNDARY_20261120.md\` in the same Source publication.

Minimum remaining obligation: test the proof assumptions at the exact external lemma boundaries and separate rational bit execution from arbitrary characteristic-zero field oracle cost; no unrestricted circuit result or native X6/BRC correspondence has been established. Preserve original external manuscript and separate independent review.