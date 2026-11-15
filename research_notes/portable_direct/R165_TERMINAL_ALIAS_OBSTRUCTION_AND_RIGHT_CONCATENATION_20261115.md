# R165 — Terminal-alias impossibility, complete adjacent-swap form, and right-concatenation obstruction

Date: 2026-11-15 (Asia/Shanghai). Research status: AUTHOR_PROVED / NOT_REVIEWED.
Research scope: the **external finite-Sturmian tied-phase scalar observer**, not a native-X6 or typed-BRC dynamical theorem.
Scientific input remains frozen at \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Dependencies: R162 two-preimage theorem (commit \`f451da2665923179eed166c488a1e8063222ca29\`); R164 exact signature certificate and decoder (commit \`991d99ab20b7669ecf1465eba01e87851855381e\`). P000 and joint-observer information-preservation remain in force.

## Model and notation

For an admitted length-\(m\) binary word \(w\), let \(p_i=\sum_{k=1}^{i}w_k\), \(p_0=0\). Its open slope support \((\alpha,\beta)\) satisfies the factor strip bounds and \(\alpha<\beta\). Put
\[
 A=\min_{0\le i\le m}(p_i-i\alpha),\qquad
 B=\max_{0\le i\le m}(p_i-i\beta),\qquad
 S_m(w)=(\alpha,\beta,U,V),
\]
where \(\alpha=a/b\), \(\beta=c/d\) are reduced, \(U=b(1+A)\), \(V=dB\).
The closed prefix strips at \((\theta,x)\) are
\(p_i\le x+i\theta\le p_i+1\).
R162 proves that two words with the same signature differ at exactly one prefix position \(j\in\{1,\ldots,m\}\), by exactly one, and share the chord
\[
 x(\theta)=1+A+\frac{B-1-A}{\beta-\alpha}(\theta-\alpha).
\]
That chord has slope \(-j\), and its \(j\)-th prefix readout is a constant integer.

## R165A — Last-bit collisions are impossible at every length \(m\ge2\)

**Theorem.** For all \(m\ge2\), distinct admitted length-\(m\) words with the same \(S_m\) differ by an **internal adjacent transposition** \(01\leftrightarrow10\). The terminal-prefix alternative \(j=m\) from R162 is possible only at \(m=1\), where \(S_1(0)=S_1(1)=(0,1,1,0)\).

**Proof.** Suppose \(m\ge2\) and two words share a signature but differ only at the last bit. Write \(l=m-1\), let \(v\) denote their common length-\(l\) prefix, let their last prefix sums be \(p_m^-=q-1\), \(p_m^+=q\), and use the shared chord \(x(\theta)=q-m\theta\). Denote the signature support by \((\alpha,\beta)\), with \(\Delta=\beta-\alpha>0\); set \(x_\alpha=q-m\alpha=1+A\), \(x_\beta=q-m\beta=B\). Hence
\[
                   x_\alpha-x_\beta=m\Delta. \tag{1}
\]

First we show that \(v\)'s own slope support is exactly \((\alpha,\beta)\). Its support contains this interval because the original two words restrict to the same prefix. If \(\alpha>0\), the lower endpoint of the word ending in 0 has a directed factor witness \(z_k(\alpha)-z_i(\alpha)=1\) with \(i<k\), where \(z_i(\theta)=p_i-i\theta\). For that word \(z_m(\alpha)=A\) is a **minimum**, so index \(m\) cannot be the later maximum \(k\), and being the last index it cannot be the earlier index \(i\). Thus this lower endpoint is already witnessed inside \(v\). For \(\alpha=0\), the domain boundary is already the prefix lower boundary. Similarly, if \(\beta<1\), the upper endpoint of the word ending in 1 has a directed witness \(z_i(\beta)-z_k(\beta)=1\) with \(i<k\). There \(z_m(\beta)=B\) is a **maximum** and cannot serve as later minimum \(k\), nor as earlier \(i\), hence this upper endpoint is witnessed in \(v\). For \(\beta=1\), it is the prefix domain boundary. Therefore \((\alpha_v,\beta_v)=(\alpha,\beta)\).

Let \(r_i\), \(0\le i\le l\), be the prefix sums of \(v\), and \(g(\theta)=\max_{i\le l}(r_i-i\theta)\). Because the same chord satisfies all closed prefix strips, \(x_\alpha,x_\beta\) are feasible intercepts for \(v\) at its support endpoints.

If \(v\) contains both symbols, its prefix residue range equals 1 at **both** endpoints. Indeed at an interior lower/upper boundary the corresponding directed witness forces range 1. At \(\alpha=0\), exact lower support 0 forces the whole word \(v\) to contain at most one 1; as \(v\) is nonconstant, it contains exactly one 1, and its residue range at 0 is 1. Dually, at \(\beta=1\), \(v\) contains exactly one 0 and its residue range there is 1. Endpoint feasible intercepts are consequently unique, so
\[
                    x_\alpha=g(\alpha),\qquad x_\beta=g(\beta).
\]
For each prefix \(i\le l\) we have
\(r_i-i\beta\ge r_i-i\alpha-l\Delta\).
Taking maxima yields
\[
                  x_\beta=g(\beta)\ge g(\alpha)-l\Delta
                         =x_\alpha-l\Delta. \tag{2}
\]
Thus \(x_\alpha-x_\beta\le l\Delta\), contradicting (1), because \(m=l+1\).

If \(v=0^l\), its support is \((0,1/l)\), its unique endpoint feasible intercepts are \(x_\alpha=1,x_\beta=0\), and \(x_\alpha-x_\beta=l\Delta=1\), again contradicting (1). If \(v=1^l\), its support is \(((l-1)/l,1)\), with the same endpoint intercept difference \(l\Delta=1\), giving the same contradiction. The cases exhaust all prefixes. Hence no \(j=m\) collision exists for \(m\ge2\). By R162, every remaining pair is one internal \(01\leftrightarrow10\) transposition. For \(m=1\), direct evaluation gives the stated two-word fiber. QED.

## R165B — An exact adjacent-swap criterion and fast rejection certificate

For a given **admitted** word \(w\) of length \(m\ge2\) with known signature \(s=(a/b,c/d,U,V)\), define
\[
D=bc-ad>0,\quad N=dU-bV,\quad j=N/D,\quad q=(U+aj)/b.
\]
A second preimage exists **if and only if** all the following hold:

1. \(D\mid N\) and \(1\le j<m\).
2. \(b\mid(U+aj)\), and \(p_j\in\{q-1,q\}\).
3. \(w_j\ne w_{j+1}\). Form \(\widetilde w\) by swapping those two neighboring bits.
4. The four exact endpoint-extremum, residue-range and directed-boundary-witness conditions of **R164A** hold for \(\widetilde w\) and the *same* proposed signature \(s\).

The necessity of (1)–(3) follows from the integer fixed-\(j\) chord and R165A. R164A makes (4) precisely the equality \(S_m(\widetilde w)=s\), proving sufficiency. The modular checks cost \(O(1)\) exact operations on the given signature; the subsequent exact R164A scan costs \(O(m)\) arithmetic operations and \(O(1)\) additional storage (besides the input and optional output word). The condition is constructive even when the candidate fails.

The index \(j\) is the exact location of the **one local order bit** required to restore identity in a two-preimage fiber.

## R165C — The scalar signature is not a right-concatenation congruence

Take \(w=01\) and \(v=10\). Direct exact computation gives
\[
  S_2(01)=S_2(10)=(0,1,1,0).
\]
Appending the **same** bit \(0\), however, yields
\[
  S_3(010)=(0,2/3,1,0),\qquad
  S_3(100)=(0,1/2,1,1).
\]
Both extended words are admitted and their signatures differ. Thus there is no universally defined update map \(F\) with
\(S_{m+1}(wz)=F(S_m(w),z)\)
on all admitted words and their admitted one-bit extensions. Exact future-safe compression for the operation of right concatenation must retain enough information to distinguish at least this collision.

Some collisions persist under the same operation. For example,
\[
 S_6(101001)=S_6(100101)=(1/3,1/2,3,1)
\]
and
\[
 S_7(1010010)=S_7(1001010)=(1/3,1/2,3,1).
\]
This separates *possible* continuation survival from universal congruence and motivates a finer classification of operation-safe fibers. These scalar results do not assert a native BRC time-step, native X6 embedding or universal minimal-memory claim.

## Exact validation and evidence

The attached standalone \`R165_terminal_alias_check.py\` uses Python \`Fraction\` as an exact independent \(O(m^2)\) signature oracle and enumerates **all** binary strings of lengths 1–14: 32,766 candidates. It obtains 114 two-preimage classes, with one terminal class at \(m=1\) and zero terminal classes for every \(2\le m\le14\). It cross-checks the stated modular candidate test against all observed fibers and the explicit concatenation examples. Its accompanying \`R165_verification.json\` records per-length counts, integer rational tuples and the pass marker \`R165_TERMINAL_ALIAS_EXACT_PASS\`. These are author-side finite corroborations; R165A rests on the preceding symbolic argument. Independent mathematical review: NOT_REVIEWED.

## Actual operational status and next question

At 2026-11-15T01:05:17Z, native read request \`em-r1-20261115-0902-s23-task-read-r165\` returned SUCCEEDED and \`NO_CANONICAL_PUBLICATION_DIRECTORY\` for the exact topic \`RS-S23-AV\` at Source \`23e8a6256a91316e38a949d317156085aabc49ce\`. The read explicitly does not provide an owner projection. This note is an independent non-overwriting portable research artifact; it does not establish CLAIM, formal Result, Review or Foundation admission. Research Activity association is separately pending permission/identity reconciliation.

**Next scientific question:** characterize precisely which double fibers remain double after appending a specified bit, by an endpoint-witness update rule. Seek an exact finite-state repair automaton for the local order bit under repeated admissible concatenation, with explicit observer/operation horizon and information cost.
