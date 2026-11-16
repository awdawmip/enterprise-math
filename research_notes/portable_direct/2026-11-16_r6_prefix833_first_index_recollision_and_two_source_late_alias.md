# PREFIX-833 — First-difference-index recollision criterion and arbitrarily late two-source re-aliasing

**Date:** 2026-11-16. **Status:** AUTHOR_PROVED / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific input:** \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Antecedent: PREFIX-832 all-time Q trace formula and actual counterexample.

## Declared model and observer

Let \(p=q\geq1\). Initially \(p\) distinguishable, unmarked sources with positive integer removal weights \(w_1,\ldots,w_p\) fill capacity, and the distinguished marked source is absent. \(Q=R+A\) sums each legal removal with source weight, marked removal with \(b>0\), and marked insertion with \(a>0\). Histograms \(Y_l(t)\) record positive integer total mass at occupancy \(l\) after \(t\) operations. The two profiles compared have the same number \(p\) of initial sources and the same \(a,b\). Differences of positive observations may be signed; they are not physical amplitudes. Define
\[
\Delta_d=e_d(A)-e_d(B),\quad \Delta_0=0,\quad \Delta_{p+1}=0,\quad
n=\min\{1\leq d\leq p:\Delta_d\ne0\},\quad \lambda=ab>0.
\]
Distinct multisets ensure that \(n\) exists. The state model is a scoped positive BRC auxiliary readout, not an independently licensed native X6 Cell/Link/Port event.

## Theorem 833.1 — A lower-index observer distinguishes every later time except at most one

For every \(t\geq n+1\) with \(t-n\) odd,
\[
\boxed{\Delta Y_{p-n+1}(t)=n!\Delta_n\binom{t-1}{n-1}\,a\,\lambda^{(t-n-1)/2}\ne0.}
\]
For \(t=n\), \(\Delta Y_{p-n}(n)=n!\Delta_n\ne0\). For \(t\geq n+2\) with \(t-n\) even,
\[
\boxed{\Delta Y_{p-n}(t)=n!\binom{t-1}{n-1}a\lambda^{(t-n-2)/2}
\left[b\Delta_n+\frac{(n+1)(t-n)}{n}\Delta_{n+1}\right].}
\]
Consequently the two complete histograms differ at **every** \(t\geq n\), except possibly one \(t=T\). Such an exceptional time requires \(\Delta_{n+1}\ne0\) and
\[
T=n-\frac{nb\Delta_n}{(n+1)\Delta_{n+1}}\in\mathbb Z,\quad T\geq n+2,\quad T\equiv n\pmod2.
\]
If \(p=n\), they never re-alias after initial separation. For every \(t\geq n-1\), the ordered two-frame observer \((Y(t),Y(t+1))\) distinguishes the profiles.

**Proof.** Apply the exact PREFIX-832.1 difference sum with occupancy \(p-n+1\). The only possible terms have \((d,m)=(n-1,0)\) or \((n,1)\); the former vanishes by minimality of \(n\). The latter gives the first boxed expression. In occupancy \(p-n\), only \((d,m)=(n,0)\) and \((n+1,1)\) occur. For \(t=n\), the second is illegal; for \(t\geq n+2\) it contributes and binomial-factor simplification yields the second boxed expression. Its bracket is affine in \(t\) with nonzero constant \(b\Delta_n\), so it vanishes at most once. At the opposite parity the first box is nonzero. Every two consecutive frames from \(n-1\) onward include a time with a forced difference. QED.

This improves the \(t\geq D\) eventual-separation window of PREFIX-832, where \(D\) was the **largest** differing coefficient index: the single-exception theorem holds already from the **first** divergence step \(n\).

## Theorem 833.2 — Necessary and sufficient algebraic test for the exceptional full-histogram equality

Fix a candidate \(T\geq n+2\) with \(T\equiv n\pmod2\). Let
\[
K_T=\{k:n\le k\le\min(p,T),\ k\equiv T\pmod2\}.
\]
Then \(\Delta Y_l(T)=0\) for **all** occupancies \(l\) if and only if, for every \(k\in K_T\),
\[
\begin{cases}
\Delta_T=0,& k=T\le p,\\
bk\Delta_k+(k+1)(T-k)\Delta_{k+1}=0,& k\le T-2.
\end{cases}
\]
The first-index \(k=n\) equation gives the candidate \(T\) in Theorem 833.1. Remaining equations check other potentially visible bins. The criterion uses exact integer arithmetic and can reject false candidate re-aliasing.

**Proof.** Write a potential nonzero bin by \(k=p-l\). In PREFIX-832.1 its only possible pairs are \((d,m)=(k,0)\) and \((k+1,1)\), and both require \(t-k\) even. For \(k<n\) both coefficient differences vanish. For \(k=T\) only the first pair is legal. For \(k\le T-2\) the common positive factor \(k!\binom{T-1}{k-1}a\lambda^{(T-k-2)/2}/k\) leaves exactly \(bk\Delta_k+(k+1)(T-k)\Delta_{k+1}\). No other occupancy can differ. QED.

## Theorem 833.3 — Arbitrarily late single-frame re-aliasing with only two sources and a fixed operator

Fix the same operator for every example, \(a=1\) and \(b=2\), and set \(p=q=2\). For **every odd integer \(T\geq3\)** define
\[
A_T=(1,2T+1),\qquad B_T=(2,T+1).
\]
Both lists have positive integer weights. Their elementary differences are exactly
\[
(\Delta_1,\Delta_2)=(T-1,-1).
\]
Their complete histograms coincide at times **exactly \(t=0\) and \(t=T\)**; they differ at every other positive integer time. Indeed, with \(\lambda=2\),
\[
\Delta Y_1(1)=T-1,
\]
and for odd \(t\geq3\),
\[
\boxed{\Delta Y_1(t)=2(T-t)\,2^{(t-3)/2}.}
\]
For every even \(t\geq2\),
\[
\Delta Y_2(t)=(T-1)2^{(t-2)/2}\ne0,\qquad
\Delta Y_0(t)=-2(t-1)2^{(t-2)/2}\ne0.
\]
No profile using only \(p=1\) initial unmarked source can re-alias after its first difference, since \(\Delta_2=0\) and both parity witnesses of Theorem 833.1 are nonzero. Therefore **two** is the smallest source count permitting an arbitrarily late positive-time recollision, even with \(a,b\) held fixed. Maximum unmarked weight is \(2T+1\), so this explicit family has linear weight growth in the requested exceptional time.

Example \(T=3\): \(A=(1,7)\), \(B=(2,4)\). At \(t=3\) both histograms are \((0,44,0)\). At \(t=2\) they are \((14,0,8)\) and \((16,0,6)\); at \(t=4\) they are \((84,0,16)\) and \((96,0,12)\).

**Proof.** The coefficients follow from sums/products of the two weights. Substituting them into the exact formula gives all displayed identities; for \(p=2\), at odd times there is only the occupancy-1 possible nonzero bin. Minimality follows by setting \(\Delta_{p+1}=0\) when \(p=1\). QED.

## Verification, novelty scope, and next question

The accompanying exact standard-Python program independently evolves the legal named-subset/marked-flag transitions. It crosschecks the PREFIX-832 all-time formula and the new full-equality criterion for **7,100 unordered distinct multiset pairs with parameter choices**, covering \(p=1,2,3\), each weight from 1 through 5, \(a\in\{1,2\}\), \(b\in\{1,4,8,12,16\}\), and times \(0\leq t\leq12\): **92,300 full-histogram time comparisons**, 84,700 after first separation, including 42,110 forced opposite-parity checks. It also runs the fixed-operator witness at \(T\in\{3,5,7,11,21\}\), checking all frames through \(T+3\). All assertions passed with unbounded exact integers. These finite tests validate implementation and examples; the universal results use the proofs above.

Relation to PRIOR WORK: PREFIX-832 established eventual separation from the **last** differing \(D\) and exhibited one recollision. PREFIX-833 sharpens to the **first** differing \(n\), supplies a complete algebraic criterion, and constructs arbitrarily late recollisions with the minimum two sources and a fixed operator. The two-frame observer is a readout guarantee for a **fixed pair after its first separation**; it does not merge states safely under all future operations.

**Next discriminating questions:** Characterize the set of admissible positive-integer \((\Delta_d)\) satisfying the simultaneous full-equality equations for \(p\geq3\), including resource-optimal single-frame re-aliasing; determine the minimal extra observer that is forward-safe without knowing \(n\); and separately return to \(q\ge5,b>0\) minimal nonnegative Q carrier. Preserve the frozen source pin and native X6 licensing boundary.
