# Auxiliary four-label BRC: all-round second-2 absorption theorem

**Author-side mathematical note, 2026-10-23. NOT REVIEWED, NOT ADMITTED, NOT NATIVE X6.** This result concerns the specified positive-mass four-hidden-label auxiliary observer. It has not been transferred to the P000 native six-spatial-dimensional Cell dynamics. The proof below is algebraic and does **not** depend on the previously unreviewed N31/N32 all-round single-pulse assertions.

## Fixed model

Hidden labels are 0,1,2,3. Independent samples in rounds with public action 0 or 2 have respective nonnegative **weights** (to be divided by 3)

\[
q_0=(0,1+z,1-z,1),\qquad q_2=(1,1,0,1),\qquad 0\le z\le1.
\]

The good occupied-label sets are

\[
\mathcal G=\{\{0,1\},\{1,2\},\{1,3\},\{2,3\}\}.
\]

With \(D_t\) the set of labels observed in rounds 1 through \(t\), set
\[
\delta_t=\Pr(D_t\in\mathcal G), \quad \delta_0=0,\quad
\Delta_t=\delta_t-\delta_{t-1},\quad M_t=\max_{0\le s\le t}\delta_s,
\]
\[
R_t=\sum_{j=2}^t[\Delta_j]_+-M_t,\qquad [x]_+=\max(x,0).
\]
This is the historical positive-variation residual, not a function of the final counts alone.

## THEOREM (strict multi-2 final decrement)

For every \(n\ge4\), every \(z\in[0,1]\), and every word \(p\in\{0,2\}^n\) containing **at least two action-2 symbols**,
\[
\boxed{\delta_n(p;z)-\delta_{n-1}(p_{1:n-1};z)<0.}
\]
Consequently \(R_n(p;z)=R_{n-1}(p_{1:n-1};z)\). Moreover, if the second 2 first occurs at position \(\tau\), then for **every** extension and \(n\ge\tau\),
\[
\boxed{R_n=R_{\tau-1}.}
\]
Residual accumulated before the second 2 need not vanish; it simply cannot grow again.

### Exact occupancy formula for arbitrary words

Let \(a\) be the number of 2 symbols, \(b\) the number of 0 symbols, \(n=a+b\). For a good pair \(\{i,j\}\), the probability of observing exactly that pair equals

\[
\prod_{r=1}^n(p_{r,i}+p_{r,j})-\prod_{r=1}^np_{r,i}-\prod_{r=1}^np_{r,j}.
\]
Products commute, so one-time occupancy \(\delta_n=N(a,b;z)/3^{a+b}\) depends on counts only (unlike \(R_n\)). Summing the four good pairs gives the **exact and exhaustive** cases:

For \(a,b\ge1\),
\[
\boxed{N(a,b;z)=(2^a-3)(1+z)^b+2^a(2+z)^b+2^b+(2-z)^b-2.}\tag{1}
\]

For \(a=0,b\ge1\),
\[
\boxed{N(0,b;z)=2^b+(2+z)^b+(2-z)^b-2(1+z)^b-2(1-z)^b-2.}\tag{2}
\]

For \(b=0,a\ge1\),
\[
\boxed{N(a,0;z)=2^{a+1}-4.}\tag{3}
\]
The empty word has \(\delta_0=0\).

### Proof of strict negativity, all n

Put \(U=1+z\), \(V=2+z\), \(W=2-z\). Then \(1\le U\le2\), \(V\ge U\), \(W\ge1\), and \(V+W=4\).

For an old prefix with \(a,b\ge1\), append action 0. The increment numerator on denominator \(3^{a+b+1}\) is

\[
E_0=N(a,b+1)-3N(a,b)
=(3-2^a)(2-z)U^b-2^a(1-z)V^b-2^b-UW^b+4.\tag{4}
\]

When \(a\ge2,b\ge1\), the bounds
\[
(2-z)U^b\ge(2-z)(1+z)=2+z-z^2\ge2,
\quad
UW^b\ge(1+z)(2-z)=2+z-z^2\ge2
\]
imply, term by term,
\[
\boxed{E_0\le-2-0-2-2+4=-2<0.}\tag{5}
\]

If the appended action is 2, its numerator is
\[
E_2=N(a+1,b)-3N(a,b)
=(6-2^a)U^b-2^aV^b-2^{b+1}-2W^b+4.\tag{6}
\]
For \(a\ge2,b\ge1\), the first two terms are bounded by
\[
(6-2^{a+1})U^b\le-2U^b\le-2,
\]
and thus
\[
\boxed{E_2\le-2-4-2+4=-4<0.}\tag{7}
\]

When the appended action 2 is only the **second** such action, \(a=1,b\ge2\), use \(U\le2\) and the convexity bound
\[
V^b+W^b\ge2((V+W)/2)^b=2^{b+1}.
\]
Equation (6) yields
\[
\boxed{E_2(1,b;z)\le4\cdot2^b-2\cdot2^{b+1}-2^{b+1}+4
=4-2^{b+1}<0\quad (b\ge2).}\tag{8}
\]

It remains to check prefixes consisting exclusively of 2 symbols (\(b=0\)). From (3), adding a 2 gives
\[
N(a+1,0)-3N(a,0)=8-2^{a+1}<0\qquad(a\ge3).\tag{9}
\]
Adding a first 0 instead gives
\[
N(a,1)-3N(a,0)=2^a(2z-3)+11-4z.\tag{10}
\]
For \(a\ge3\) its slope in \(z\) is \(2^{a+1}-4>0\), so its maximum on \([0,1]\) is \(7-2^a\le-1<0\). Equations (5), (7), (8), (9), (10) cover **all** possible final actions of a length \(n\ge4\) word containing two or more action 2 symbols. This proves strict negative \(\Delta_n\). It follows immediately that \(M_n=M_{n-1}\) and \([\Delta_n]_+=0\), hence \(R_n=R_{n-1}\).

### Complete small-round boundary audit

At \(n=2\), the only word already containing two 2s is 22, for which \(\delta_1=0\), \(\delta_2=4/9=M_2\), so \(R_2=R_1=0\).

At \(n=3\), all words containing two 2s are 220, 202, 022 and 222. For 220,
\[
\delta_3(220)=\frac{11+4z}{27},\qquad
\Delta_3(220)=\frac{4z-1}{27}.
\]
If \(z>1/4\), the positive increment raises the previous maximum \(\delta_2(22)=4/9\) by exactly the same amount; hence it does not raise \(R_3\). If \(z\le1/4\), its increment is nonpositive. For 202 and 022 the appended second 2 has numerator \(4(z-1)\le0\), and for 222 the third increment is zero. Hence in all cases \(R_3=R_2\).

For \(n\ge4\), strict negativity already proved makes each later residual increment zero. If the second 2 arrives at \(\tau=2\) or 3, the exceptional checks apply first. If \(\tau\ge4\), strict negativity applies immediately. This proves the absorbing theorem for every possible \(\tau\). QED.

## Meaning and exact limits

This is a uniform symbolic proof for every word length, every binary action order, and every real \(z\in[0,1]\), within **this** four-label positive-mass observer. It explains without finite Bernstein classifications why multiple action-2 pulses cannot create new residual. It does not claim that every zero-pulse word has a unimodal occupancy curve; nor does it settle all effects of a *first* 2 in positions 1,2,3 or re-establish the previously unreviewed historical peak bound for first 2 at positions \(\ge4\). No unconditional full-word rebound classification, no new \(L_{\min}\) bound, and no native X6 transfer are inferred.

## Verification and provenance

Separate exact 16-state occupancy-mask dynamic programming and the independent count closed formula were cross-checked using Python standard-library fractions (no floats). The complete standalone checker is the sibling file verify_two_pulse_absorption.py, with captured verification_report.json. All words of lengths 1..8 were checked at nine rational parameters, and all two-pulse count classes up to n=80 at the same parameters. This finite audit is *not* the universal proof; the complete algebraic case split above is the proof.

Snapshot: GLOBAL_KNOWLEDGE_V1 main@abed76a9c866347d9c3b3ba2844853229a4e8c22; enterprise-math main@af2df115aa4f2641452c5a788dab0a4cf57f594b. P000 projection's canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc was verified. Context-only prior unreviewed author manuscript: c080c43ac34563bf1d5a549a1456fcf7103a993f.

The native em_control_tasks request failed with CONTROL_QUOTA. Attempting an own native RESEARCHER session yielded STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Thus owner and formal session/claim remain unverified; publication of this note is solely an unreviewed research frontier and must not be treated as canonical Result/Driver review.

**Next discriminating mathematical unit:** prove all-parameter unimodality of the no-2 sequence \(\delta_n(0^n;z)\) or construct an exact counterexample, and settle first-2 positions 1/2/3. Then assemble (not merely assert) a full arbitrary-word, all-round classification; keep the native P000 observer bridge as a separate open obligation.
