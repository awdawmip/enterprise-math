# D25 — uniform floor-centering of original 216/2304 half-endpoint jets

Date 2026-11-05. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, immutable science input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical conversation: \`chatgpt-research-onhour-enterprise-math-20260923\`. **AUTHOR-SIDE PROVEN EXACT IDENTITY / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM**.

## Directly consumed frontier

The source-aligned mother objective is \(\Delta_p-R_p=0\bmod p\) for \(p\equiv13,19\bmod24\), equivalently the still-open \(W_p\equiv V_p\bmod p^3\). The previously published author-side same-half-endpoint 2-jet certificate (commit \`2b3a5813e0afa4ca8f3997e1eeb771080719d1a8\`) proves an *exact equivalence*
\[
 K_p+\Xi_2+C_A=0\bmod p,
\]
where \(K_p\) is the carry from \(\Xi_0+p\Xi_1\), \(\Xi_2\) is the signed A−B second jet and \(C_A\) is the original 216 upper valuation-two shell. Uniform vanishing is not established. The earlier two-case centered-quarter B construction depended on \(p\bmod4\).

## New theorem: exact branch-free centering for all primes p>3

Write \(r_d(a)=\lfloor ap/d\rfloor\) for \(a\) coprime to \(d\), and \(h=\lfloor p/2\rfloor=(p-1)/2\). The original, source-labelled hypergeometric factors have the **exact multiset identities in rational numbers**
\[
\begin{split}
\{1/2,1/3,2/3\}
&=\{-h+p/2,\;-\lfloor p/3\rfloor+p/3,\;-\lfloor2p/3\rfloor+2p/3\},\\
\{1/2,1/4,3/4\}
&=\{-h+p/2,\;-\lfloor p/4\rfloor+p/4,\;-\lfloor3p/4\rfloor+3p/4\}.
\end{split}
\]
The multiset notation matters: the second/third factors can be permuted, but their Pochhammer product is invariant. This removes the p mod 4 case split **without changing the original coefficient or signed model provenance**.

Proof: Since \(p>3\) is coprime to 2,3,4, for each \(d\in\{2,3,4\}\) multiplication by \(p\) permutes the reduced residue classes of denominator \(d\). The right-side factors are exactly the fractional parts \(\{ap/d\}\), for \(a=1\) (d=2), \(a=1,2\) (d=3), and \(a=1,3\) (d=4). These sets are respectively \(\{1/2\}\), \(\{1/3,2/3\}\) and \(\{1/4,3/4\}\). Equality is over \(\mathbb Q\), not merely mod p.

For each source, use the resulting universal ordered tuple of integer center and rational p-shift:
\[
\begin{array}{l}
A:\quad (-h,1/2),\;(-\lfloor p/3\rfloor,1/3),\;(-\lfloor2p/3\rfloor,2/3),\\
B:\quad (-h,1/2),\;(-\lfloor p/4\rfloor,1/4),\;(-\lfloor3p/4\rfloor,3/4).
\end{array}
\]
Each pair \((m,c)\) denotes \(m+pc\), and does not introduce a new axiom.

## Exactly one half-interval zero and explicit support

For each integer \(0\le k\le h\), among the factors \(m+j\), \(0\le j<k\), there is **at most one zero**, because \(h\) itself first becomes zero only for \(k=h+1\), while \(\lfloor2p/3\rfloor>h\), \(\lfloor3p/4\rfloor>h\). Only the near-centers can vanish:
\[
r_A=\lfloor p/3\rfloor,\qquad r_B=\lfloor p/4\rfloor.
\]
The original A zeroth p-jet coefficient vanishes after \(k=r_A\), and B after \(k=r_B\). For \(r_A<k\le h\) (respectively \(r_B<k\le h\)), the coefficient acquires exactly one factor \(p/3\) (respectively \(p/4\)), and its first and second jet terms are, in the notation of the previous proof,
\[
S_{1,A}^{upper}=\sum_{k=r_A+1}^{h}(6k+1)R_{k,A}/3,\quad
S_{2,A}^{upper}=\sum_{k=r_A+1}^{h}(6k+1)R_{k,A}L_{k,A}/3;
\]
\[
S_{1,B}^{upper}=\sum_{k=r_B+1}^{h}(8k+1)R_{k,B}/4,\quad
S_{2,B}^{upper}=\sum_{k=r_B+1}^{h}(8k+1)R_{k,B}L_{k,B}/4.
\]
Here \(R\) is the zero-factor-deleted integer product divided by \(t_\nu^k(k!)^3\) and \(L\) is the exact logarithmic p-jet over the *nonzero integer factors*. All denominators are p-units for p>3. These formulas are identities for the signed source-labelled shell, not a claim that the shell sums themselves vanish.

Consequently the previous precise two-jet and carry identity is valid with **this single uniform formula** for all primes p>3; its proof does not depend on any p mod 4 split. The **frozen target** still only concerns the two congruence classes p≡13,19 mod24, and all-target cancellation remains unproved.

|p|h|rA|rB|zero-factor shifts|
|--:|--:|--:|--:|---|
|13|6|4|3|A 1/3; B 1/4|
|19|9|6|4|A 1/3; B 1/4|
|139|69|46|34|A 1/3; B 1/4|
|373|186|124|93|A 1/3; B 1/4|

## Executed check, retained observer, future operation

A Python integer-modular checker computed source-labelled \(S_{0,1,2}\) by the universal center formula and checked reconstruction against the **original 216/2304 half-endpoint rational recurrences** modulo p³ for **every one of the 667 primes 5≤p≤4999**. For all **166 frozen target-class primes** in the same range, both A and B jet triples matched the previously published p mod4 branch-dependent centers term by term at the observer level. **667 passed, zero failures.** A prior 301-prime run (p≤1999) also passed; only the wider 667-prime result is counted as current check. This is exact finite verification of implementations, not proof of all-prime cancellation.

The next WZ search can use one p-parametric factorial/jet family with signed A,B labels, near-zero positions rA/rB, p-adic valuation and carry retained. No extra case hypothesis on p mod4 is required; no quotient-erasure of the source labels, zero-factor provenance, or \(K_p\). From the BRC perspective the carrier is the labelled jet/zero-shell family and the future operation is taking the signed difference, the carry, then the terminal p-adic residual.

## Unfinished obligations and Source

Prove the still-open all-target \(K_p+\Xi_2+C_A=0\bmod p\) with a p-dependent terminating A↔B transform/WZ or produce an exact qualifying counterexample; attempt the uniform center expression before reintroducing case splits. Do not reprove accepted CM0/UR or Guo–Zudilin B p³ theorem, do not present finite scan as proof. The **native** original fixed-373 same-class H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius direction, eta, kappa, odd Hesse/Green readout and independent replication remain unexecuted, support **Issue #1559 OPEN / PENDING_EXECUTOR**.

The earlier exact same-lane Source read \`onhour11-20261105-1505-d25-own-read\` was read as \`SUCCEEDED / execution_authorized=false\`. No own authenticated native Researcher session, CLAIM/run, Source checkpoint or admitted Result is asserted. Previous author-only GitHub publication is consumed but not promoted to formal scientific admission. The maintenance conversation identity is never used.
