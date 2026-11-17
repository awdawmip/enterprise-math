# R762DD — Integral open X6 path-area cocycle and sharp parity repair

Date: 2026-11-17. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; author EM-X6-3050F6 using existing session MCP-4b2d70a97f594366a7c94a0f8b45df38. Independent review NOT_REVIEWED.

## Frozen scientific provenance

Frozen taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Predecessors: R762CH closed-X6 path area, Draft PR #2575@1c860018c4399e1b7497192ef818e3567390d2e2; R762DC bounded pair diagnostics, Draft PR #2641.

P000 fixes six native spatial axes, native three-force stability, PERP_E / 120-degree relation and an affine signed Cell torsor. Fifteen pair-area coordinates below describe *history/provenance*, not additional spatial axes or native two-dimensional planes. No actual licensed TRIADIC_CLOSURE_E event is assumed.

## Definitions — arbitrary signed X6 paths

Fix a chosen native chart anchor. A possibly *open* primitive X6 path is a finite word $H=(d_1,\ldots,d_m)$, each $d_t\in\{\pm e_1,\ldots,\pm e_6\}\subset\mathbb Z^6$. For $i\ne j$ put

\[
v_i(H)=\sum_t d_{t,i},\qquad
B_{ij}(H)=\sum_{p<t}d_{p,i}d_{t,j},\qquad
A_{ij}(H)=B_{ij}(H)-B_{ji}(H)\quad(i<j).
\]

Thus $A(H)$ is an alternating rank-15 integral path-provenance array, and $v(H)$ is the signed Cell displacement. On closed histories, $B_{ij}$ for $i<j$ is exactly R762CH's $C_{ij}$.

## Theorem 1 — exact open-path cocycle and central extension

For **all** (open or closed) signed native unit-step words $H,K$,

\[
\boxed{v(HK)=v(H)+v(K),\qquad A(HK)=A(H)+A(K)+v(H)\wedge v(K),}
\]
where $(v\wedge w)_{ij}=v_iw_j-v_jw_i$. In particular the path map $\Phi(H)=(v(H),A(H))$ takes concatenation to the associative integral two-step nilpotent group law

\[
(v,a)\star(w,b)=(v+w,a+b+v\wedge w).
\]

Its identity is $(0,0)$, inverse is $(-v,-a)$, and $(0,a)$ is central. Under any signed axis permutation $P$, $v\mapsto Pv$ and $A\mapsto(\wedge^2P)A$.

**Proof.** Split the ordered pair sum at the concatenation boundary:
$B_{ij}(HK)=B_{ij}(H)+B_{ij}(K)+v_i(H)v_j(K)$.
Subtract the same equation with $(i,j)$ reversed to obtain the boxed law. The cocycle identity follows by bilinearity, because $(v\wedge w)+(v+w)\wedge z=v\wedge(w+z)+(w\wedge z)$. The inverse works because $v\wedge(-v)=0$, and the signed permutation identity follows from relabeling every native step. QED.

## Theorem 2 — exact parity image and closed-loop realization

For every signed native step word H and all $i<j$,

\[
\boxed{A_{ij}(H)\equiv v_i(H)v_j(H)\pmod 2,\qquad
B_{ij}(H)=\frac{A_{ij}(H)+v_i(H)v_j(H)}2.}
\]

Conversely **every** $(v,A)\in\mathbb Z^6\times\mathbb Z^{15}$ with those fifteen parity congruences occurs for at least one signed native unit-step path.

**Proof.** A single native step has exactly one nonzero coordinate, so $d_{t,i}d_{t,j}=0$ for $i\ne j$. Expanding $v_iv_j$ and discarding its zero diagonal terms gives $v_iv_j=B_{ij}+B_{ji}$, while $A=B_{ij}-B_{ji}$. Solve these two equations for $B_{ij}$ to obtain both claims.

For realization, choose any signed coordinate path $H_0$ ending at the desired $v$. Its area $A^0$ obeys the same parity constraints. Consequently each $(A_{ij}-A^0_{ij})/2$ is an integer. The closed four-step loop $L_{ij}=(+e_i,+e_j,-e_i,-e_j)$ has $v=0$ and $A=+2e_{ij}$; the oppositely oriented loop $L_{ji}=(+e_j,+e_i,-e_j,-e_i)$ produces $A=-2e_{ij}$. Concatenate the required number of positive/negative loops independently for each pair. Theorem 1 gives exact additivity when the appended path is closed, so all fifteen coordinates can be adjusted with no change to v. QED.

**Consequences.** At every fixed $v$, exactly one of the $2^{15}$ parity assignments for the fifteen $A_{ij}$ is allowed; the full image in $\mathbb Z^6\times\mathbb Z^{15}$ is not a linear sublattice because its congruences involve products $v_iv_j$. For an open path, $A$ is **not** simply additive under concatenation; the $v\wedge w$ term is essential. On a closed path $v=0$, $A=2C$, recovering the additive closed-loop carrier of R762CH.

## Theorem 3 — sharp modulus to recover ordered pair areas

Fix $q\ge2$ and assume the endpoint displacement $v(H)$ is retained **exactly**. Retaining $A(H)\pmod m$ for a positive integer $m$ is sufficient to determine all ordered $B_{ij}(H)\pmod q$ over **every** signed native path if and only if

\[
\boxed{q\mid\frac{m}{\gcd(m,2)}.}
\]

The smallest possible modulus is

\[
\boxed{m_{\min}(q)=\begin{cases}q,&q\ {\rm odd},\\2q,&q\ {\rm even}.\end{cases}}
\]

**Sufficiency.** Fix $v$. Every admissible $A_{ij}$ has parity $v_iv_j$, so a difference between two admissible $A$ values congruent modulo m must be divisible by $\operatorname{lcm}(m,2)=2m/\gcd(m,2)$. Theorem 2 implies the corresponding ordered $B$ values differ by a multiple of $m/\gcd(m,2)$, hence coincide mod q whenever the boxed divisibility holds.

**Necessity.** Suppose $q\nmid m/\gcd(m,2)$ and put $t=m/\gcd(m,2)$. For any fixed axis pair $i<j$, take $H=B_{ij}^{\,t}$ and $K=L_{ij}^{\,t}$, with $B_{ij}=(+e_i,-e_i,+e_j,-e_j)$ and $L_{ij}$ as above. Both paths have identical endpoint $v=0$, time $4t$, and complete twelve-direction signed-step histograms. Their $A$ difference is $2te_{ij}\equiv0\pmod m$, but their ordered area $B_{ij}$ difference is $t\not\equiv0\pmod q$. Hence the proposed quotient fails on a common coarse fibre. The least m satisfying the criterion is q for odd q and 2q for even q. QED.

**State cost.** On any fixed $v$, the modulus $m_{\min}$ has exactly q parity-admissible residues per $A_{ij}$; the even-q factor two is a **congruence representation repair**, not an additional history bit on this parity-constrained population. If endpoint $v$ is omitted, this reconstruction theorem does not apply without an observer-safety proof.

## Exact author-side verification

Run: node R762DD_VERIFY.js > R762DD_EVIDENCE.json. The executable uses bounded integers with exact arithmetic. It checks **all 22,621** signed X6 native-step words of length 0 through 4 for parity and reconstruction; **21,025** ordered pairs of empty/two-step words for the cocycle; all **15** pair loop generators; and **75** sharp counterexamples for every modulus below $m_{\min}(q)$ for q=2,...,10. Local execution returned PASS. These finite checks support the code/example claims; the general theorems have independent algebraic proofs above. Independent mathematical review remains NOT_REVIEWED.

## Remaining native research frontier

Read and pin the authentic signed TRIADIC_CLOSURE_E Cell/Link/Port event predicate and licensed V17/V29/V39 rotations. Determine whether actual legal suffixes read the ordered $B$, alternating $A$, named Port/source histories, or further joint residuals. Apply the exact open-path cocycle and parity repair only under that legal observer language. The protected P000 and joint-relation observer-preservation contract remain unchanged.
