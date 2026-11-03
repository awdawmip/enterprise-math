# PREFIX-468 — Closed rational generating function for reachable base BRC observations

Date: 2026-11-03 Asia/Shanghai. Research type: author-side analytic theorem + exact finite regression. Scientific source pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Continuation: PREFIX-467 (commit \`e90b07741a38a412ecf9fe161052ecd2353e5736\`); current applicable control rules read separately from main. Native owner/claim and independent mathematical review not established.

## Declared observer, native carrier and route

Use the P000 six-axis native affine X6 chart, with eleven signed unit-step symbols \(x=+E_1\) and \(\pm E_2,\ldots,\pm E_6\). Write \(a=+E_2,b=+E_3\); all ten non-\(x\) letters are always allowed. The first letter may be \(x\). A later \(x\) is legal exactly when the immediately preceding two letters are \(ab\). Word length is a separately typed ordered path parameter.

For a legal word retain its native endpoint \(s=\#x\), \(y_i=\#(+E_{i+1})-\#(-E_{i+1})\) for \(i=1,\ldots,5\), and the exact BRC weight-valuation coordinates of PREFIX-463/465. Put \(p_i=\min(\#(+E_{i+1}),\#(-E_{i+1}))\) and
\[
 A=p_2+2p_4+p_5,\qquad C=p_3+p_5.
\]
At fixed word length \(n\), the key \(f=(s,y_1,\ldots,y_5,A,C)\) determines the exact individual positive weight; a separate integer coefficient stores the multiplicity of words in each key. Let \(B_n\) denote the number of different reachable keys \(f\) among all legal words of length \(n\), counting each key once, not its mass. The future-history states \(q\) of PREFIX-467 are not included in \(B_n\). These coordinates are scope-typed observer coordinates, not a complete physical/phase state or a final nonnegative cell address.

## Theorem A — exact Parikh support of the gate

For every integer \(n\ge0\), a nonnegative 11-vector of step counts with sum \(n\) is realized by at least one legal ordered word if and only if
\[
 s\le 1+\min(a_+,b_+),
\]
where \(s=\#x\), \(a_+=\#a\), \(b_+=\#b\). For \(s=0\) the condition is automatic.

**Proof.** Except for a possible initial \(x\), each \(x\) must be immediately preceded by the two-letter block \(ab\). Such blocks serving distinct occurrences of \(x\) are disjoint; hence at least \(s-1\) copies each of \(a,b\) are needed. Conversely, for \(s\ge1\), construct \(x(abx)^{s-1}\) and append all remaining non-\(x\) letters in any order. The construction is legal, has the prescribed counts, and uses exactly \(s-1\) copies of each of \(a,b\). For \(s=0\), concatenate all non-\(x\) letters. QED.

## Theorem B — a closed generating function, valid at all lengths

Let \(G(z)=\sum_{n\ge0} B_n z^n\). As an identity of formal rational power series over \(\mathbb Q\),
\[
\boxed{G(z)=\frac{(1+2z^2)(1+z)^2(1+z-z^3)}{(1-z)^8(1-z^3)}}.
\]

**Proof.** Fix \(s\ge0\) and \(y\in\mathbb Z^5\). Every unordered step-count population above these coordinates is represented by five nonnegative cancellation counts \(p_i\), and its length is \(n=s+\|y\|_1+2\sum p_i\). Write \(t=\max(0,s-1)\) and \(y_i^+=\max(y_i,0)\). Theorem A becomes the pair of lower bounds
\[
 p_1\ge L_a:=\max(0,t-y_1^+),\quad
 p_2\ge L_b:=\max(0,t-y_2^+).
\]
Translate \(p_1=L_a+v_1,p_2=L_b+v_2,p_i=v_i\ (i=3,4,5)\). If \(r=\sum v_i\ge0\), the valuation pair is \((A,C)=(L_b+A',C')\) where \(A'=v_2+2v_4+v_5,\ C'=v_3+v_5\).

For fixed \(r\), the distinct pairs \((A',C')\) are exactly
\[
 S_r=\{(A',C')\in\mathbb Z^2:0\le C'\le r,\ 0\le A'\le 2r-C'\}.
\]
Indeed, after fixing \(C'=c\), select \(v_5=j\) from \(0\) through \(c\), \(v_3=c-j\); distribute the remaining \(r-c\) units among \(v_1,v_2,v_4\). Their \(v_2+2v_4\) values fill every integer from \(0\) to \(2(r-c)\), while \(j\in[0,c]\) fills the intervening integer translations. This covers precisely the stated interval. Consequently
\[
 b(r):=|S_r|=\frac{(r+1)(3r+2)}2,\qquad
 Q(z):=\sum_{r\ge0}b(r)z^{2r}=\frac{1+2z^2}{(1-z^2)^3}.
\]
The translations \(A\mapsto A+L_b\) are bijective for each fixed \(s,y\).

Put \(H(z)=\sum_{k\in\mathbb Z}z^{|k|}=(1+z)/(1-z)\). The two gated \(y\)-coordinates contribute
\[
 T_t(z):=\sum_{k\in\mathbb Z} z^{|k|+2\max(0,t-\max(k,0))}=z^t H(z)\quad(t\ge0).
\]
The equality follows by splitting \(k<0,0\le k<t,k\ge t\) into three geometric sums (the \(t=0\) case is \(H\)). The other three signed coordinates contribute \(H^3\). Since \(t=0\) for \(s=0\), and \(t=s-1\) for \(s\ge1\),
\[
 G(z)=Q(z)H(z)^3\Big(H(z)^2+\sum_{s\ge1}z^sT_{s-1}(z)^2\Big)
 =Q(z)H(z)^5\Big(1+\frac{z}{1-z^3}\Big).
\]
Simplifying denominators yields the boxed rational function. Distinct \(s,y\) have different keys, while each \(S_r\) counts each valuation key once; therefore the coefficient is exactly \(B_n\). QED.

## Corollaries — a finite linear recurrence and eventual quasipolynomial

Expand the numerator and denominator:
\[
 P(z)=1+3z+5z^2+6z^3+4z^4-z^5-4z^6-2z^7,
\]
\[
 D(z)=1-8z+28z^2-57z^3+78z^4-84z^5+84z^6-78z^7+57z^8-28z^9+8z^{10}-z^{11}.
\]
The identity \(D(z)G(z)=P(z)\) is an integer coefficient recurrence valid for every \(n\ge0\) with \(B_n=0\) at negative indices. For \(n\ge8\), the right-hand coefficient is zero and this is an order-11 homogeneous recurrence. There exists a degree-eight polynomial \(P_8(n)\in\mathbb Q[n]\) and a bounded rational period-three function \(c(n)\) such that \(B_n=P_8(n)+c(n)\) for every \(n\ge0\); this follows from partial fractions and
\((1-z)^8(1-z^3)=(1-z)^9(1+z+z^2)\).
The leading asymptotic is
\[
 \boxed{B_n=\frac{n^8}{10080}+O(n^7)}.
\]
Indeed the coefficient of the order-nine pole at \(z=1\) is \(4\).

The PREFIX-467 future-observer count \(N(n,1)=B_n+B_{n-2}\) for \(n\ge2\) now has the same rational series:
\[
 \sum_{n\ge0}N(n,1)z^n=(1+z^2)G(z)
\]
with the conventions \(B_{-1}=B_{-2}=0\). The full-history count \(F_n\) remains a separate problem.

## Exact executed evidence

The attached ECMAScript/BigInt program computes \(B_n\) from the integer polynomial identity through \(n=20\). Independently for every \(0\le n\le8\), it (i) enumerates every nonnegative 11-vector of total sum \(n\), filters it by Theorem A, projects it to the BRC key; and (ii) builds every reachable Parikh/DFA suffix-state combination by actual legal one-step transitions. The sets of reachable count vectors agree **elementwise**, and all unique BRC-key counts agree with the rational-series coefficients. The largest independent input slice has \(\binom{18}{10}=43758\) possible Parikh vectors, of which the program checks every one. All integers and equality tests are exact.

This verifies the declared finite scope of the certificate. The analytic derivation above proves the formula for every integer \(n\ge0\). The executable is a regression of a specified discrete BRC valuation-observer model, not a numerical physical-heartbeat experiment or an independent mathematical review.

## Reuse, governance, next question

Source boundaries: immutable scientific input \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; P000, ACTIVE X6 and joint-observer preservation; PREFIX-463/465/466/467 at their published immutable commits. No changes to P000 or other native axioms. Proposed next PREFIX-469: derive a rational series for the fully history-sensitive \(F_n=\sum_f|Q_n(f)|\) by classifying which base fibers admit suffix states 0 and 1; then derive explicit bit-width thresholds for exact finite-future codecs. Independently retain the arbitrary-degree X6 moment-rank problem from PREFIX-459/460.

Native service \`em_control_tasks\` returned \`CONTROL_QUOTA\`. Native \`em_session_start\` returned \`STATIC_READONLY_SCOPE_DENIED\`, \`operation_sent=false\`; no CLAIM, official Result/Review, or Admission was performed. Author source publication is a project research note under the established portable_direct path, not a controlled task state transition.
