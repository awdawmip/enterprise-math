# R143 — Exact prefix-pair integer elimination for the tied-phase S23 observer

Date: 2026-11-14 (Asia/Shanghai).
Status: AUTHOR-SIDE EXACT DERIVATION / NOT_REVIEWED.
Object: external scalar tied-phase mechanical-word observer, not a native X6 evolution or BRC–Shor operation.
Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Predecessors: R137B (Farey gap feasibility), R139B (extremal word), R140 (finite threshold tests), R142 (Farey support filter); the proof below is a separate elementary derivation.

## 1. Problem

For integers K,m >=1 and 0<theta<1, define
\[
S_i^{(K)}(\theta)=\lfloor(K+i)\theta\rfloor-\lfloor(K+i-1)\theta\rfloor,\qquad 0\le i<m.
\]
Given ANY specified binary word w of length m, decide w in V(K,m), and produce an exact rational theta if it is present. In particular, K can have arbitrarily many decimal digits. This is a query about one given word; the size of the full language W_m is a separate output-size parameter.

Put s_0=0, s_j=sum_{i=0}^{j-1}w_i and L=K-1.

## 2. R143.1 — Integer-elimination theorem, K>=2

For each 0<=i<j<=m put h=j-i, d=s_j-s_i, and define integers
\[
B_{ij}=L(d-1)+i s_j-j(s_i+1),\qquad
A_{ij}=L(d+1)+i(s_j+1)-j s_i.
\]
Define the two **integer** extremal bounds
\[
N_{\min}=\max\left(0,\max_{i<j}\{\lfloor B_{ij}/h\rfloor+1\}\right),
\qquad
N_{\max}=\min\left(L-1,\min_{i<j}\{\lceil A_{ij}/h\rceil-1\}\right).
\]

**Theorem.** For every K>=2, m>=1, and binary w,
\[
\boxed{w\in V(K,m)\quad\Longleftrightarrow\quad N_{\min}\le N_{\max}.}
\]
The decision requires O(m^2) exact integer operations on operands with O(log(K+m)+log m) bits. No Farey cells or parameter events are enumerated.

**Proof.** Let N=floor(L theta). Because 0<theta<1 and L>=1, N is an integer with 0<=N<=L-1. For the prescribed floor differences to equal w, for all 0<=j<=m we must have
\[
s_j\le (L+j)\theta-N<s_j+1.
\]
Equivalently, with
\[
\ell_j(N)=(N+s_j)/(L+j),\quad u_j(N)=(N+s_j+1)/(L+j),
\]
we need a common theta in the open interval
\[
\max_j\ell_j(N)<\theta<\min_j u_j(N),
\]
and one such point exists iff max_j ell_j(N)<min_j u_j(N). (Taking an interior point removes any lower-endpoint equality issue.)

The pairwise condition ell_i(N)<u_j(N), for each i<j, gives
\[
(j-i)N < A_{ij}.
\]
The reverse condition ell_j(N)<u_i(N) gives
\[
(j-i)N > B_{ij}.
\]
The diagonal inequalities are automatic. Consequently all lower/upper intervals overlap strictly iff every B_{ij}/h<N<A_{ij}/h. For integer N these are precisely N>=floor(B_{ij}/h)+1 and N<=ceil(A_{ij}/h)-1. Intersect with 0<=N<=L-1 to obtain N_min<=N_max, as claimed.

For an allowed N, ell_0(N)=N/L>=0 and u_0(N)=(N+1)/L<=1. Thus the midpoint constructed below automatically lies in (0,1). QED.

## 3. R143.2 — Rational witness and short exclusion certificate

When N_min<=N_max, choose N=N_min, set
\[
\ell=\max_{0\le j\le m}\frac{N+s_j}{L+j},\qquad
u=\min_{0\le j\le m}\frac{N+s_j+1}{L+j},\qquad
\boxed{\theta=(\ell+u)/2}.
\]
Then 0<theta<1 and S^{(K)}(theta)=w exactly. Because the maximum/minimum are attained among fractions with denominator at most L+m, the reduced witness denominator is at most 2(L+m)^2. The bit length of the rational witness is O(log(K+m)).

When N_min>N_max, retain the indices i,j (or the boundary 0/L-1) attaining each extremum, together with their exact numerator and denominator. **At most two prefix-pair witnesses** certify the absence of every integer N, hence the absence of the word. After these pair indices are supplied, verification requires only a constant number of integer arithmetic comparisons and the w prefix sums. This is a compact exact negative certificate rather than a failed bounded search.

## 4. R143.3 — K=1 boundary

For L=0, N=floor(0 theta)=0 and the j=0 equation is tautological. The word is realized iff
\[
\boxed{
\max\bigl(0,\max_{1\le j\le m}s_j/j\bigr)
<
\min\bigl(1,\min_{1\le j\le m}(s_j+1)/j\bigr).
}
\]
Its interval midpoint is a rational witness. This special case uses O(m) exact rational comparisons; in particular w_0=1 is impossible.

## 5. Mathematical significance and limits

- The exact query complexity is quadratic in the word length and logarithmic in the coefficient, improving the direct single-word decision route over full Farey decomposition.
- It tests *any* binary word, including words outside the Sturmian language. It does not assume the conjectural formula T(m)=E(m).
- It supplies compact positive and negative certificates usable to isolate missing members of the R142 avoidant family.
- To derive a uniform formula for T(m), it remains to control the two extremal bound envelopes simultaneously for every w in the avoidant family and every K>=E(m). A finite verification, by itself, does not settle this infinite statement.

## 6. Verification and provenance

The accompanying \`check_r143.py\` independently enumerates all rational change parameters of the original floor observer for 1<=m<=9, 1<=K<=25, checking midpoint and event values. It tests all 2^m binary words against the pairwise integer criterion. It also reconstructs large-K positive witnesses from original floors, and checks the predicted extremal threshold boundary on 5<=m<=13 using independently generated finite languages.

Observed result: \`R143_PREFIX_INTEGER_ELIMINATION_PASS\`.
- 24,528 exhaustive binary-word memberships at 2<=K<=25, 1<=m<=9;
- 1,022 memberships at K=1, 1<=m<=9;
- 1,200 huge/small coefficient positive witness checks (up to K=10^80+139);
- 2,228 exact threshold-boundary word checks, m=5,...,13.

The finite runs corroborate the stated theorem; its universal domain is supported by the algebra above. Independent review: NOT_REVIEWED.

## 7. Next work

For the avoided words A_m of R142, extract which prefix pairs achieve N_min and N_max near E(m); prove a uniform upper-envelope dominance lemma or produce an exact counterexample. Preserve each candidate's full word, K, the two extremizing pairs and the pair-bound certificate. Test changes in the active pair identities instead of rescanning chronological theta events.
