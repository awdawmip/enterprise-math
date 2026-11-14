# R143 — Convex interval projection, exact single-word membership and residue-class permanent thresholds

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE MATHEMATICAL PROOF / NOT_REVIEWED.
Science pin retained: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Parent: R142 (immutable science \`f55fb7edb04520ff3cb11d9a2baa756017c70d14\`).
Scope: **external scalar fixed-phase S23 / finite mechanical words only**. The polygon below is a parameter-space representation, not a native Enterprise Math plane, X6 Cell identity, or observer-safe quotient of the Heartbeat World.

## 1. Setting

Fix integers m >= 1 and K >= 2. Put L=K-1. The binary word at 0<theta<1 is
\[
S_i^{(K)}(\theta)=\lfloor(L+i+1)\theta\rfloor-\lfloor(L+i)\theta\rfloor,\quad 0\le i<m.
\]
For a proposed w=(w_0,...,w_{m-1}) in {0,1}^m let s_0=0 and s_j=sum_{i<j}w_i.

Define
\[
\alpha=\max\left(0,\max_{0\le i<j\le m}\frac{s_j-s_i-1}{j-i}\right),\qquad
\beta=\min\left(1,\min_{0\le i<j\le m}\frac{s_j-s_i+1}{j-i}\right).
\]
If alpha >= beta, w is not a finite Sturmian (free-intercept) word and is absent at every K. Otherwise the free-intercept slope interval is (alpha,beta). Put
\[
\ell(t)=\max_{0\le j\le m}(s_j-jt),\quad
u(t)=\min_{0\le j\le m}(s_j+1-jt),\quad
u_\alpha=u(\alpha),\quad \ell_\beta=\ell(\beta).
\]
All quantities are rational and computable exactly from w. In particular, alpha in [0,1), beta in (0,1] and their reduced denominators are at most m, except the denominator-1 boundary conventions.

## 2. Exact interval-projection theorem

**Theorem R143.1.** For every m>=1, K>=2 and w with alpha<beta, define
\[
A_L=L\alpha-u_\alpha,\qquad B_L=L\beta-\ell_\beta .
\]
Then
\[
\boxed{w\in V(K,m)\quad\Longleftrightarrow\quad
\lfloor A_L\rfloor+1<B_L.}
\]
The least integer strictly above A_L is the explicit witness index
\[
N=\lfloor A_L\rfloor+1.
\]
Set
\[
t_{\rm low}=\max\left(0,\max_{0\le j\le m}\frac{N+s_j}{L+j}\right),\quad
t_{\rm high}=\min\left(1,\min_{0\le j\le m}\frac{N+s_j+1}{L+j}\right).
\]
Under the boxed condition t_low<t_high, and
\(\theta=(t_{\rm low}+t_{\rm high})/2\) is an exact rational witness producing precisely w.

**Proof.** Consider the open convex polygon
\[
C_w=\{(t,r):0<t<1,\ s_j<r+jt<s_j+1\quad(0\le j\le m)\}.
\]
Its projection to the t-axis is (alpha,beta), by eliminating r from the prefix inequalities. At fixed t its r-section is the nonempty open interval (ell(t),u(t)). Both ell and u are continuous and nonincreasing in t (each is the max/min of finitely many affine functions of slopes -j<=0). For L>=1 the linear functional \(f_L(t,r)=Lt-r\) therefore has image exactly the open interval
\[
f_L(C_w)=(L\alpha-u(\alpha),\,L\beta-\ell(\beta))=(A_L,B_L).
\]
Indeed, its lower and upper values at each t are Lt-u(t) and Lt-ell(t), respectively; both strictly increase with t, and continuity/convexity makes the total image one interval.

A fixed-phase word w occurs at some parameter theta iff the line \(Lt-r=N\) with integer N meets C_w: if so, r=Lt-N in (0,1), hence N=floor(Lt), and all prefix-floor differences equal w. Conversely, an occurrence at a boundary parameter is right-continuous in theta: all finitely many floors floor((L+j)theta), 0<=j<=m, remain unchanged for a sufficiently small positive theta increment. Choose the increment avoiding every integer boundary; it gives a point in C_w on some integer line. Thus the strict polygon criterion loses no original occurrences.

An integer lies in (A_L,B_L) exactly when floor(A_L)+1<B_L. Solving the strict prefix inequalities after substituting r=Lt-N gives the stated interval (t_low,t_high). Taking its rational midpoint completes the witness. QED.

**Boundary K=1.** L=0 pins r=0 on the polygon boundary, so K=1 is intentionally separate. Directly, w occurs for K=1 iff the interval
\[
\max(0,\max_{1\le j\le m}s_j/j)<\min(1,\min_{1\le j\le m}(s_j+1)/j)
\]
is nonempty (with the evident inclusive-left convention when the maximum is 0). The permanent-threshold results below only require K>=2; for complete languages T(m)>=2 already because K=1 has S_0=0 identically.

## 3. Exact eventual threshold without scanning K

Write alpha=a/b in lowest terms, b>=1, delta=beta-alpha>0, and h=u_alpha-ell_beta. For each residue r=0,...,b-1 define
\[
f_r=\{r\alpha-u_\alpha\},\qquad
C_r=\frac{1-f_r-h}{\delta},\qquad
M_r=r+b\left\lfloor\frac{C_r-r}{b}\right\rfloor.
\]
Keep M_r only when M_r>=1. Then

**Theorem R143.2 (exact last absence and permanent word threshold).**
\[
\boxed{\operatorname{LastBadL}(w)=\max(\{0\}\cup\{M_r:M_r\ge1\}),\qquad
T_w=\operatorname{LastBadL}(w)+2.}
\]
For every integer K>=T_w, w is present. If T_w>2, w is absent at K=T_w-1. Thus T_w is the least permanent presence threshold among K>=2.

**Proof.** Theorem R143.1 says
\(w\in V(L+1,m)\iff L\delta+h>1-\{L\alpha-u_\alpha\}\).
For L congruent to r modulo b, the fractional part is exactly f_r, since b alpha is an integer. Therefore failures in that residue class are *precisely* the positive integers L=r+qb satisfying L<=C_r. Their largest positive member, when one exists, is M_r. This gives the last absence over all b classes. After that last absence, every K>=LastBadL+2 is present; the preceding coefficient is absent when LastBadL>=1. QED.

**Corollary R143.3.** Each fixed word has residue-wise monotone occurrence: for any L>=1,
\(w\in V(L+1,m)\Rightarrow w\in V(L+b+1,m)\),
where b is the reduced denominator of its *left support endpoint* alpha. This is a word-specific coefficient step, which may be considerably smaller than a global LCM.

**Corollary R143.4 (exact finite reduction of global T).** For the complete finite Sturmian language W_m and m>=1,
\[
T(m)=\max_{w\in W_m}T_w .
\]
This is an exact finite formula valid for every m. It computes the real permanent **word** saturation threshold by one residue scan per word and never iterates over K up to T(m).

## 4. Costs, verification, and research frontier

Given a word of length m, computing alpha and beta from all prefix pairs takes O(m^2) exact rational comparisons; the envelope endpoints take O(m); b<=m, so R143.2 takes at most m residue steps. Rational sizes are polynomial in m; membership at a specified K additionally uses O(log K) input bits. An existing complete W_m enumeration therefore yields an exact T(m) computation without a coefficient sweep. This is independent of Farey-intercept gap enumeration *per coefficient*.

The companion checker independently constructs W_m from Farey cell/intercept cuts; for 310 pairs (m=1..10,K=2..32) it compares the R143 projection test with exact chronological event enumeration, including jumps of floor((K-1)theta). For m=2..20 it evaluates all 5,452 word thresholds through residue classes and verifies the reconstructed T(m) against R136/R140 benchmark values. At m=5..20 the maxima match E(m)=(m-2)floor((m-1)/2)+1 and are attained by the two complementary extremal patterns, as finite evidence.

Next scientific obligation: use the compact support-endpoint formulas to prove or refute \(T(m)=E(m)\) for all m>=5, for example by showing that every *other* word's projected interval has width >1 at L=E(m)-1 and treating the two extremal words by their exact residue condition. This width separation holds in the tested m=5,7,10,12,16,20 but is presently a candidate lemma, not a proven all-m assertion.

Original frozen input and source provenance stay unchanged. There is no claimed formal Task ownership, native X6 mapping, independent review, or mathematical acceptance arising from this author-side research note.
