# Exact affine-in-horizon compression of S23/AV multistep risk

2026-11-09. Author-side mathematical result; independent review pending.
Researcher-ID: EM-DIRECT-3BF369; Activity: RA-EE04B3C6EE09E96DDAAF4586.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: r15 PROOF.md at ae35ded416213bf15886a7b28a40e271c103ada0, in PR #1777.

## Theorem: minimal maximal constant-increment affine encoding

Let theta be irrational. Given consecutive maximal integer risk-constant blocks [s_i,e_i], i=1,...,B, with distinct neighboring values F(n)=A_i+B_i*theta, write D(n)=F(n)-F(n-1). At a block transition n=s_i (i>1), D has coefficient pair (A_i-A_{i-1},B_i-B_{i-1}); within a block, for s_i<n<=e_i, the pair is (0,0). This exhausts all m<n<=N.

Merge consecutive increment positions sharing the same pair (dA,dB), giving maximal ranges [l,r]. For each range emit the six integers (n0=l-1,n1=r,A0,B0,dA,dB), where (A0,B0) is the original F(l-1) coefficient pair. Every integer n0<=n<=n1 has the EXACT value

    F(n) = (A0+(n-n0)*dA) + (B0+(n-n0)*dB)*theta.

Adjacent records share one endpoint with identical reconstructed values. Because theta is irrational, equality of integer affine coefficient pairs is equivalent to equality of their values. Hence these are uniquely maximal runs of constant increment and have the minimum record count among piecewise constant-increment encodings with only shared consecutive endpoints.

Proof: Within a source constant block all successive differences vanish, and at each jump the difference is the new minus previous exact affine pair; this determines the complete difference sequence. Telescoping produces the displayed formula. Equal successive differences merge, while unequal differences require a new run boundary. An equality (a+b*theta)=(c+d*theta) with different integer pairs would make theta rational, contradiction. QED.

An already sorted table yields the event list and maximal increments with O(B) arithmetic steps and O(J) output space using a streaming cursor. The supplied simple implementation uses binary-search anchor lookup, O(B+J log B) arithmetic operations and O(B+J) memory, independent of horizon N apart from integer bit length and source generation costs.

## Finite S23/AV certificates

Scope: frozen auxiliary 79-bin circle observer, fixed history m=128 and uniform initial phase. The certified interval for theta used in the exact upstream r15 verifier is

    262204504569236716045286/10^24 < theta <
    262204504569236716045287/10^24.

The upstream r15 exact nonenumerating generator was re-executed. Exact source-table SHA-256 for L<=2,000,000: f9dd46e0e9e70b8871717b9d24a7f3361c4228f8894bef00d50458086cebb548 (94,239 bytes). Its table byte-matched the prior r14 TSV. Exact source-table SHA-256 for L<=10^12: 82a0ffdc13e5743cec32eec6985b3e31ae9cf30b8233de7aa04e1755f141245d (389,512 bytes).

New compression outcomes:
- L<=2,000,000: 3,426 risk-constant blocks -> **102 exact affine runs** (50 zero and 52 positive, 13 unique increment pairs); 3,677 output bytes; SHA-256 26707bc77d7b7267495df34045f1c5111a2d21cb7c8222e83e65775897b013e1.
- L<=10^12: 9,698 blocks -> **298 exact affine runs** (148 zero and 150 positive, 23 unique increment pairs); 15,356 output bytes; SHA-256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6.
- Terminal risk coefficients at L=10^12 remain (-4017401528447,15321634290944), i.e. R=A+B*theta.

The actual exact Python codec checked every source block start/end, interior-neighbor and compressed run boundary, plus fixed-seed random horizons: 13,535 distinct queries for 2M and 20,142 for 1T; coefficient pairs agreed in every check. Algebraic reconstruction of ALL integer horizons follows from the proved complete-difference partition and the upstream certified complete block table, not from the random tests.

## Contrasting family and BRC semantics

The previously proved r15 near-rational family theta*=1/2+sqrt(2)/10^12, m=128, n<=10^11 has exact R=(2theta*-1)(n-128). Its 99,999,999,873 singleton constant-risk blocks admit ONE six-integer run: (128,100000000000,0,0,-1,2). This converts the pre-existing theorem, rather than newly proving the near-rational law.

The compressed coefficients retain the EXACT scalar risk observable at all declared horizons, with phase/gap branch provenance preserved in the upstream labelled Farey source for operations that need it. This is an auxiliary BRC-inspired observer calculation, not a native X6 dynamics transfer. No formal Task CLAIM, independent review or mathematical admission is asserted.

## Follow-on unit

Emit maximal constant-increment runs directly during Farey rank/select event traversal; group long nearly rational Farey epochs without scanning every neighbor; validate against both the frozen S23/AV 298-run output and the near-rational one-run example. Measure total bit cost, original input conversion, output and precision refinement. Keep S23/AV capacity plateau 413 as a separate geometric frontier.
