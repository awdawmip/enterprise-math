# PREFIX-442 — Exact residue-sector BRC moments: rank, recovery, and failure threshold

2026-11-02. Parent scientific frontier: PREFIX-441. Independent author-side proof, exact BRC checks, no native CLAIM, no independent Review/Admission. Frozen source: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; original `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` has Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Current normative inputs: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, P000, ACTIVE Heartbeat X6, the observer-preservation rule, current portable research and BRC-only arithmetic methods, and account-level math/code/output policies.

## Population and observations

Take one chart-relative Cell in the *full* signed-six-axis X6 spatial torsor. Restrict a test population to ordered native words of a common length (n\ge0) using only (+e_1,-e_1). The count (k) of negative steps determines endpoint displacement ((n-2k,0,0,0,0,0)), and there are (inom nk) distinct allowed words. Let (c_k) be the nonnegative integer count of selected distinct words at that endpoint, (0\le c_k\leinom nk). This is a typed embedded observer family, retaining its X6 provenance.

For an integer residue-state count (q\ge1) and degree (d\ge0), declare
[
T_{r,j}=\sum_{\substack{0\le k\le n\\ k\equiv r\pmod q}}c_k(n-2k)^j,
\qquad 0\le r<q,\quad 0\le j\le d.
]
The (r) state records path-history residue, not a seventh spatial axis or physical heartbeat time.

## Theorem 1. Exact rank and complete recovery

Over the rationals the observation map has
[
\boxed{\operatorname{rank}(c\mapsto T)=\min(n+1,q(d+1)).}
]
Thus it uniquely determines every terminal multiplicity (c_0,\ldots,c_n) **if and only if**
[
\boxed{n+1\le q(d+1).}
]
Proof: permute columns by the residue (k\bmod q). Every block is a truncated Vandermonde matrix of rank (min(|K_r|,d+1)), with pairwise distinct evaluation points (x_k=n-2k). The residue-class sizes differ by at most one; their block ranks add to the displayed minimum. When (|K_r|\le d+1), construct the Lagrange basis (L_{r,k}(X)=\prod_{t\in K_r,t\ne k}(X-x_t)/(x_k-x_t)=\sum_j\lambda_{r,k,j}X^j). Then **the explicit exact inverse** is (c_k=\sum_j\lambda_{r,k,j}T_{r,j}). This also covers empty residue classes.

## Theorem 2. Positive native-path counterexamples whenever recovery fails

For every (q\ge1,d\ge0,n\ge q(d+1)), set (m=d+1), (k_t=qt) for (0\le t\le m). Construct source ensembles (E,O) by taking (inom mt) distinct words at (k_t), respectively for even or odd (t). Each side has exactly (2^d) words. All their (q(d+1)) observations (T_{r,j}) agree, yet
[
\boxed{T_{0,d+1}(E)-T_{0,d+1}(O)=(d+1)!(2q)^{d+1}>0.}
]
Proof: all (k_t) share residue zero, and the alternating binomial finite difference annihilates every polynomial of degree at most (d). Applying it to the degree (d+1) endpoint monomial gives the exact expression. For legality with distinct native words, partition the first (q(d+1)) step slots into (d+1) blocks of size (q). Distinct choices of (t) blocks yield (inom{d+1}{t}) distinct signed-step words with (qt) negatives, proving (inom n{qt}\geinom{d+1}{t}). This is an exact positive-unit-branch construction, not a signed virtual histogram.

The (2^d) witness size is an explicit uniform upper bound, not a claim of cardinality minimality: PREFIX-441 already gave the sharper three-word ((q,d)=(1,2)) witness for (n\ge4).

## Corollary. Quadratic parity ports and n=4 hybrid completion

For ((q,d)=(2,2)), the six parity-separated quadratic observations recover the complete endpoint histogram for every (n\le5); at (n=6) their rank is (6<7). A valid four-word per-side obstruction is (E=\{k=0:1,k=4:3\}) against (O=\{k=2:3,k=6:1\}), with equal sector moments through degree two and third-degree gap **384**. This construction continues for all (n\ge6).

At (n=4), PREFIX-441's three-word pair (A=(0,3,3)), (B=(1,1,4)) has equal (M_0,M_1,M_2) and parity mass (P_{even}), but
(T_{even,1}(A)-T_{even,1}(B)=8).
The five readouts ((M_0,M_1,M_2,P_{even},T_{even,1})) have the matrix, with columns ordered (k=0,1,2,3,4),
[
\begin{pmatrix}
1&1&1&1&1\\
4&2&0&-2&-4\\
16&4&0&4&16\\
1&0&1&0&1\\
4&0&0&0&-4
\end{pmatrix}
]
of determinant **-512**. They recover the entire (n=4) endpoint distribution using quadratic or lower degree readouts, an alternative to PREFIX-441's cubic-plus-parity completion.

## Theorem 3. Operation-closed signed-step BRC observation

Appending (+e_1) preserves the residue (r) and changes (x\to x+1); appending (-e_1) sends (r\to r+1\pmod q) and (x\to x-1). Consequently the exact future updates are
[
T'_{r,j}=\sum_{i=0}^j\binom jiT_{r,i}\quad (+e_1),\qquad
T'_{r,j}=\sum_{i=0}^j\binom ji(-1)^{j-i}T_{r-1,i}\quad (-e_1).
]
Any finite positive-rational alternatives and serial compositions of these typed control/affine edges preserve all declared sector moments through order (d). The fixed ((q,d)=(2,2)) carrier fits two finite control labels plus one second-order `MomentState` per label, under the existing typed affine-effect BRC semantics. This is an exact auxiliary path observation theorem; full endpoint recovery continues to require the horizon inequality at the resulting length.

## Verification, evidence, and continuation

The pinned and unchanged `signed_brc.endpoint_multiplicity` was actually invoked to verify available native six-axis path populations; its Git blob was checked. The author-side exact Fraction certificate passed **924** rank/recovery triples, **75** positive-word finite-difference witness instances, **40** future step-port closure instances, and the exact n=4 determinant and n=6 cubic witness. A compact reproducer and its captured execution log are published alongside this note; its narrower suite checks 300 rank cases and 32 witness cases. The full-length proof and original longer checker/log are retained in the accompanying full evidence archive. Finite runs corroborate the universal symbolic proofs.

Native researcher-session creation returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`); live task enumeration returned `CONTROL_QUOTA`. Active owner and formal CLAIM remain unconfirmed. The original upstream `ControlPacket`/`MomentState` source was read at frozen blobs `44def6b8ac787e798d3cc2c6be16f873f91b9db8` and `be1debe367263931bd5e93fd750be3ed54624fe1`; the actual directly run class integration remains a specific next unit.

**PREFIX-443:** Directly run the previously published `prefix440_native_brc_integration.py` against unchanged frozen upstream BRC classes. Build the two-state signed-step packet, match the typed `moment_action` with these exact sector updates, and test whether one-state coalescence reproduces the n=6 failure. Quantify serialization, bit costs and horizon before claiming an engineering improvement.