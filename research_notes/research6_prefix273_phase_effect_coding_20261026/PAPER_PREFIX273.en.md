# PREFIX-273: Exact Cut Criterion and Sharp One-Probe Coding for Z2 Phase-BRC Effects

Author-side conditional algebraic result, 2026-10-26. Neither physical legality of arbitrary coherent probes nor native heartbeat evolution is established.

## Frozen source and interpretation

Global knowledge main 0dec749285c0aa4befb49b4d72a846d6ab3f2f78; Enterprise Math scientific inputs b622bf7e0c6164a53d621cb96faa2fdce2533821. The P000 startup projection matches the P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. The ACTIVE worldview, portable-research protocol, heartbeat BRC-only arithmetic constraint, six-axis native-time contract, and PREFIX-272 continuation were consulted.

Consider k *source-labelled branches* with known magnitudes m_i in positive rationals and unknown Z2 phase signs s_i. The ordered-path-pair phase-BRC formal effect for a declared rational control c is
\[
I_c(s)=\sum_{i,j}c_i c_jm_im_js_is_j=(\sum_i c_i m_i s_i)^2.
\]
This equality uses the ordered (i,j) signed-character role sum; it never identifies positive weighted path mass with signed amplitude. A formal control family C is not thereby a native-legal set of physical operations. k is not the number of native spatial axes.

## Theorem 1: all-order exact future separation test

The family (I_c)_{c in C} distinguishes every sign state modulo one global sign if and only if for every sign assignment s and every nonempty proper subset F of branch labels, at least one c in C makes both partial signed sums nonzero:
\[
A=\sum_{i\in F}c_i m_i s_i\ne0,\qquad
B=\sum_{j\notin F}c_jm_js_j\ne0.
\]
To prove the claim, any two states s,t distinct modulo global sign differ precisely by flipping a nonempty proper subset F. Their two sums are A+B and B-A. The exact ordered-path-pair BRC difference is 4AB. Thus a future output separates that pair precisely when one permitted probe has both partial sums nonzero. This proves necessity and sufficiency without assuming linear independence of observed effects.

Equivalently, put u(s)=(s_i s_j)_{i<j} and let the row of E corresponding to c have entry E_{c,ij}=2c_i c_jm_im_j. The observation contains the constant sum_i c_i²m_i² plus E u(s). Hence finite-state separation is exactly
\[
\ker E\cap\{u(s)-u(t):t\ne\pm s\}=\{0\}.
\]
Full column rank is sufficient, *not* necessary for avoiding this finite set of sign-cut secants.

A minimal warning against a support-only criterion: for k=3, m=(1,1,1), and the sole global probe c=(1,1,1), the pair-interaction support is the complete triangle; yet s=(1,1,-1) and t=(1,-1,1) both give intensity 1 and are not global flips. An effect-support graph being connected does not imply phase recovery. The k−1 lower bound for separate unit pair probes in PREFIX-272 does not generalize to arbitrary coherent multi-branch queries.

## Theorem 2: a single integer-normalized probe is sufficient, at sharp cost

For k>=2 define positive integer effective branch coefficients
\[
w=(1,2,4,\ldots,2^{k-2},2^{k-1}-1).
\]
With known nonzero rational m_i, choose formal c_i=w_i/m_i. Put M=2^{k-1} and S=sum w_i=2^k-2. The possible intensities of this single probe are *exactly*
\[
\{4j^2: j=0,\ldots,M-1\},
\]
and each is realized by exactly one phase sign orbit modulo global reversal.

Proof: subset sums of the first k−1 binary coefficients uniquely realize integers 0..M−1. Including the final coefficient M−1 realizes M−1..2M−2. The only repeated subset sum is M−1, where the two subsets (all preceding coefficients versus the last alone) are complementary. Every sign assignment has sum S−2t for t the sum of coefficients carrying negative signs. Equal squared sums arise only for equal or complementary subsets, precisely the global sign equivalence. There are 2^{k−1} distinct values 4j².

The resource bound is sharp. For any *strictly positive integer* effective coefficients w_i whose one-probe squared signed sum distinguishes all 2^{k−1} orbits, the integer signed sum has parity S and absolute value at most S. There are at most floor(S/2)+1 such magnitudes. Therefore S≥2^k−2, attained by the construction. The all-plus intensity S² forces a maximum intensity at least (2^k−2)² for any separating positive-integer one-probe design. This is a normalized integer-resource theorem, not a scale-free lower bound when arbitrary rational rescaling is admitted. For the optimum construction, distinct intensities are the squares of the even integers and their closest gap is 4; absolute additive measurement error strictly less than 2 suffices for unique nearest-codeword recovery in those units.

For six *branch labels*, the coefficients (1,2,4,8,16,31) encode 32 global-phase classes into one intensity in {0,4,16,...,3844}. Fewer queries are exchanged for exponential coefficient and readout range; no native physical cost or speedup claim follows.

## Verification and native-transfer boundary

The attached Python program computes every term of the ordered labelled (i,j) rational BRC sum. It checked all sign assignments for k=2..10 against the exact codeword set, 86,360 (sign, nontrivial cut) pairs for k=2..8 against the 4AB identity, exhaustive minimal integer total weights for k=2,3,4, the connected-support counterexample, and rational magnitude compilation (1/2,2/3,5/4,7/6). All checks passed. The statements for arbitrary k follow from the proofs rather than finite extrapolation.

The selected source's X6 contract still has fixed_heartbeat_program=null, and its self-consistent-instant schema requires model_law_id without itself defining a global update H_n -> H_(n+1). The Stage46 port-update model is a scoped candidate. Neither the original Stage46 source import nor an actual native Cell/Port/phase/time/boundary/triadic-closure experiment has been run here. The new arbitrary-control probe is formal until a real lawful effect interface and its resource semantics are supplied.

Native task inventory returned CONTROL_QUOTA and native execution registration returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false; owner/CLAIM were not verified. GitHub account awdawmip has repository push permission and only an explicit author-side research note/activity is proposed. Its local self-allocated Researcher-ID and session label are not service-issued execution authority. Formal Result, independent Driver review, and Foundation admission remain pending.

## Next discriminating experiment

Find a genuinely versioned native model law or legally supported Stage46 phase-BRC future-effect set. Record full native Cell/Port, material/field momentum, phase, source and history, boundary, independently typed time and P000 triadic consistency. Compile actually permitted probes into the rows E and apply Theorem 1; produce an exact type obstacle where compilation is impossible. Import and compare the original Stage46 ordered-pair kernel before any native-transfer assertion. If separation fails, return a source-labelled witness pair and legal future context. Treat any partial interface as a constrained test, never as the full heartbeat law.

Status: AUTHOR_SIDE_EXACT_CONDITIONAL_THEOREMS / RATIONAL_CHECK_PASS / NO_NATIVE_TRANSFER / NOT_ADMITTED.
