# X6 Unit198 — Frozen signed-BRC exact coefficient convolution

Status: **AUTHOR_PROVED / EXACT_PINNED_PYTHON_EXECUTED / CHECKER_CERTIFICATE_GITHUB_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is not Native PROGRESS, Result admission, an R063 benchmark, or production integration.

Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2. Historical Research lane chatgpt-research-onhour-enterprise-math-20260923; current protected writer authority not claimed. Frozen science 59538f585d037d09ef687b28715c4bc1a3f9fe03, historical comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3.

## Original pinned kernel

Exact file: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py at commit fd2bcff10ca6e147348b6c1236027fc0d2877df3. Original Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 and SHA256 6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4. Lines 35–39 enumerate six-part weak compositions, 42–53 give integer endpoint multiplicity, and 56–76 calculate positive-rational weighted endpoint mass. Original is time-independent; every event is one signed P000 X6 axis step.

Let \(z\in\mathbb Z^6\), \(L\geq0\), \(u_i,v_i\in\mathbb Q_{>0}\), \(a_i=\max(z_i,0)\), \(b_i=\max(-z_i,0)\). If \(L<\sum_i(a_i+b_i)\) or the difference is odd, the exact result is zero. Otherwise \(K=(L-\sum_i(a_i+b_i))/2\). The original formula is

\[
E_L(z)=L!\sum_{k_1+\cdots+k_6=K}
\prod_{i=1}^6\frac{u_i^{a_i+k_i}v_i^{b_i+k_i}}{(a_i+k_i)!(b_i+k_i)!}.
\]

## Exact algorithm and proof

Define \(P=L!\prod_i u_i^{a_i}v_i^{b_i}/(a_i!b_i!)\), \(q_i=u_iv_i\), \(c_{i,0}=1\), and

\[
c_{i,k+1}=\frac{q_i}{(a_i+k+1)(b_i+k+1)}c_{i,k}.
\]

Let \(D_0(0)=1,D_0(t)=0\) for \(t>0\). For \(i=1,\ldots,6\), compute truncated rational convolution

\[
D_i(t)=\sum_{j=0}^{t}D_{i-1}(t-j)c_{i,j}\quad(0\leq t\leq K).
\]

**Theorem:** For every admissible input, \(E_L(z)=P D_6(K)\).

*Proof.* The recurrence implies \(c_{i,k}=q_i^ka_i!b_i!/((a_i+k)!(b_i+k)!)\). Inductively \(D_i(t)\) is the coefficient of degree \(t\) of \(\prod_{r=1}^i\sum_{k=0}^Kc_{r,k}x^k\). The degree-K term enumerates precisely the original six-part weak compositions with identical factors. Multiplying by P restores the pinned factorial weights term by term. No rounding, path-sign cancellation or new observer quotient is involved. Invalid length/parity inputs return zero. QED.

At fixed dimension six, the coefficient method needs at most \(6K\) rational coefficient recurrences plus \(3(K+1)(K+2)\) rational multiply-add contributions. The original sum enumerates exactly \(\binom{K+5}{5}\) compositions. At \(K=25\) this is **150 coefficient recurrences and at most 2,106 multiply-adds**, compared with **142,506 original composition terms**. These are \(O(K^2)\) versus \(\Theta(K^5)\) **arithmetic-operation counts**, not full bit-complexity or wall-clock benchmarks. Input representation, rational normalization, factorial cost, intermediate operand size and memory still matter.

## Reproducible execution

The exact original Python source was read and its byte content verified by Git blob SHA before direct import. Three weights profiles (uniform, nonuniform positive integer and nonuniform positive rational) were tested on deterministic signed endpoints including parity/zero cases and longer walks to \(K=13\). Independently, a five-step full signed-axis weighted recurrence verified all **2,668** endpoint states and the total-mass identity. Unweighted origin returns \(E_0=1,E_2=12,E_4=396\) were also checked.

**3,112 exact Python Fraction comparisons, zero mismatches.** A separate \(K=26\) DP-only result is not verified against the original producer. No original R063 six-file benchmark rerun, no source modification and no speed claim.

Executed checker: research_checks/X6_UNIT198_PINNED_WEIGHTED_BRC_COEFFICIENT_DP_CHECK_20261121.py, commit b5d9c65730b439fc8a510e37e29b82a2a69baf58, Git blob 910409e5da10b771d285d997fbfc26108be52e2a, SHA256 463bb16b0758767004e16c9a30b2fed955fc5829180f266f03f4c5f8eeaa2ab7.

Actual results: research_checks/X6_UNIT198_PINNED_WEIGHTED_BRC_COEFFICIENT_DP_RESULTS_20261121.json, commit 66d2a92a706fea978df9e592566bc2637034fb52, Git blob cbc86abce55fac5ad94b65319db5e007a1f892d3, SHA256 7d4517706b5b4afc7da7db3d0a1e66d599cb98ae6f43e769fdd5e4afd282f019.

Reproduce in a checkout containing the pinned commit with Python, or point PINNED_SOURCE_FILE to bytes of the pinned source; the checker rejects a mismatched blob.

## Exact unresolved obligations

The real production consumer calling this historical weighted endpoint kernel has not been identified. The original LP011/LP019 erroneous commit:path:line remain unknown. This coefficient algorithm does not preserve individual ordered-path provenance and is not a remedy for an order-sensitive future consumer without separate state. Current same-lane Native semantic Units175–198 and historical Units149–152 remain separate authorization/Activity obligations. Independent Driver review is pending.

Next research: identify a real historical direct consumer at a pinned commit:path:line and its actual K/validation/benchmark contract; only then measure any original-vs-new runtime under the unchanged object, not as a replacement for R063. Continue precise LP011/LP019 provenance and reconcile original Native requests without replay.
