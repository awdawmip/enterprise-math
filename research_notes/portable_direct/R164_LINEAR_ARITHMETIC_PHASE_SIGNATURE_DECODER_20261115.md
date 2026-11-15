# R164 — Linear-arithmetic exact verification and inversion of finite-Sturmian phase signatures

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / NOT_REVIEWED. Research scope: external finite-Sturmian tied-phase scalar observer. Frozen scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Reused R162: f451da2665923179eed166c488a1e8063222ca29 (two-to-one theorem) and R163: 54a95c767f40d8a96f99108acf81d19b31d85472 (quadratic-arithmetic decoder). Current P000 and information-preservation contracts are retained. No native-X6 embedding or native BRC dynamical operation is claimed.

## 1. Exact mathematical model

For a binary word $w=w_1\cdots w_m$ of any length $m\ge1$, let $p_0=0$ and $p_j=\sum_{k=1}^j w_k$. Define its exact slope support

\[
\alpha_w=\max\left(0,\max_{0\le i<j\le m}\frac{p_j-p_i-1}{j-i}\right),\quad
\beta_w=\min\left(1,\min_{0\le i<j\le m}\frac{p_j-p_i+1}{j-i}\right).
\]

The word is admitted if $\alpha_w<\beta_w$. Put $A_w=\min_i(p_i-i\alpha_w)$ and $B_w=\max_i(p_i-i\beta_w)$. For reduced fractions $\alpha_w=a/b$, $\beta_w=c/d$ with $b,d>0$, set $U=b(1+A_w)$ and $V=d B_w$. The exact phase signature is $S_m(w)=(a/b,c/d,U,V)$.

## 2. R164A — an exact O(m) signature certificate

Fix arbitrary reduced rationals $0\le\alpha=a/b<\beta=c/d\le1$, integers $U,V$, and an m-bit word w. Compute signed integers

\[
X_i=b p_i-a i,\qquad Y_i=d p_i-c i,\qquad 0\le i\le m.
\]

**Theorem.** The signature of w equals $(\alpha,\beta,U,V)$ if and only if:

1. $\min_i X_i=U-b$ and $\max_i Y_i=V$.
2. $\max_i X_i-\min_i X_i\le b$ and $\max_i Y_i-\min_i Y_i\le d$.
3. Either $\alpha=0$, or there are indices $0\le i<j\le m$ with $X_j-X_i=b$.
4. Either $\beta=1$, or there are indices $0\le i<j\le m$ with $Y_i-Y_j=d$.

These conditions are checked by a single scan using the global extrema of X,Y, the minimum of X over earlier indices, the maximum of Y over earlier indices, and two directed-witness flags. The certificate takes O(m) exact integer arithmetic operations and O(1) auxiliary storage.

**Proof.** Condition 1 identifies $x_\alpha=U/b=1+\min_i(p_i-i\alpha)$ and $x_\beta=V/d=\max_i(p_i-i\beta)$. Condition 2 implies both endpoint points $(\alpha,x_\alpha)$ and $(\beta,x_\beta)$ satisfy every closed prefix strip $p_i\le x+i\theta\le p_i+1$; the range of each endpoint's prefix residues is at most 1. Their connecting chord lies in the convex intersection of those strips.

For each $i<j$, the affine difference $p_j-p_i-(j-i)\theta$ belongs to $[-1,1]$ at both endpoints, and has nonzero slope $-(j-i)$. Consequently it lies strictly in $(-1,1)$ throughout the open interval $(\alpha,\beta)$. Thus every $\theta$ in that interval is admissible, and the true support contains it.

When $\alpha>0$, the directed witness $X_j-X_i=b$ is exactly $p_j-p_i-(j-i)\alpha=1$, attaining the lower support boundary. Similarly, when $\beta<1$, $Y_i-Y_j=d$ is $(j-i)\beta-(p_j-p_i)=1$, attaining the upper boundary. Domain endpoints 0 and 1 require no factor witness. Hence the true slope support is exactly $(\alpha,\beta)$. The first condition then identifies the exact A,B,U,V.

Conversely, exact signature extrema yield condition 1, closed endpoint feasibility yields condition 2, and each non-domain support endpoint must be attained by a factor with the required index order, yielding conditions 3 and 4. QED.

## 3. R164B — exact linear-arithmetic decoder

For input signature $s=(a/b,c/d,U,V)$, set $D=bc-ad>0$, $H=bV-dU$. For each $i=0,\ldots,m$, perform integer Euclidean division

\[
U+ai=bq_i+r_i,\qquad0\le r_i<b,\qquad \sigma_i=iD+H.
\]

Build prefixes by the exact rules:

- $r_i>0$: choose $p_i=q_i$;
- $r_i=0,\sigma_i>0$: choose $p_i=q_i$;
- $r_i=0,\sigma_i<0$: choose $p_i=q_i-1$;
- $r_i=0,\sigma_i=0$: retain both $p_i=q_i-1$ and $p_i=q_i$.

At most one index has $\sigma_i=0$ because $D>0$, so at most two candidate prefix vectors arise. Reject any with $p_0\ne0$ or a bit difference outside $\{0,1\}$. Run the R164A linear certificate on each remaining word.

**Theorem.** For every integer length $m\ge1$ and every rational candidate signature s, this procedure returns exactly the full inverse fiber $S_m^{-1}(s)$, including empty fibers, with O(m) exact integer arithmetic operations.

**Proof.** For each actual preimage, the R162 common chord joins $(\alpha,U/b)$ and $(\beta,V/d)$; its slope is $H/D$. At $\theta=\alpha+\varepsilon$ for sufficiently small positive $\varepsilon$, the ith prefix reading is

\[
\frac{U+ai}{b}+\left(i+\frac HD\right)\varepsilon.
\]

Its forced integer floor is precisely the indicated $q_i$ or $q_i-1$. If the starting value is integral and its derivative vanishes, either adjacent integer prefix can satisfy the closed strip; at most one index has that ambiguity. The same one-sided chord argument used in R163 therefore includes every actual preimage among the two candidates. The exact R164A certificate then accepts precisely the words with signature s. Both candidate generation and certification are O(m) integer operations. QED.

Outputting m bits requires $\Omega(m)$ work, so this is optimal in the arithmetic-operation model for explicit output. This is not a unit-cost bit-time claim: operands have O(B+log(m+1)) bits when the input fields have B bits, and bit complexity also depends on integer multiplication/division costs. For valid finite-Sturmian signatures the numeric fields have polynomially bounded size in m, giving polynomial bit complexity.

## 4. Independent exact validation

Author-side Python program R164_linear_decoder_check.py uses Fraction only in an independently implemented O(m²) signature oracle. The proposed certificate and decoder use integers. The test exhaustively enumerates all 65,534 binary strings of lengths 1–15, including 1,906 admitted words, 1,760 distinct signatures, and 146 two-word fibers. The new certificate agrees with each admitted word's exact signature; the decoder returns the oracle's entire fiber for every observed signature. An additional 1,200 integer-perturbed-signature probes check every returned word against the independent oracle. All assertions pass. Reproducible marker: R164_LINEAR_DECODER_EXACT_PASS. Companion output: R164_verification.json. These are finite corroborations of the symbolic proofs.

## 5. Source and continuation

This reduces R163's O(m²) arithmetic bound to O(m) for the same fixed-length exact phase signature. R162's at-most-one identity repair bit remains sufficient. Future-safe removal of that bit for arbitrary BRC or native X6 operations requires a typed operation-specific preservation proof, not just the scalar signature fiber bound.

Next: a direct symbolic criterion for two candidate words both satisfying the four R164A clauses, and a controlled concatenation experiment tracking the repair bit and its minimal sufficient propagation under explicitly stated observer horizons.

Publication of this author-side research note does not itself create an immutable Task publication, active CLAIM, formal Result, independent Review, or Foundation admission.
