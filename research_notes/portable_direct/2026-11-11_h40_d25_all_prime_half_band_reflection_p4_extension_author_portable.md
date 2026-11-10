# D25/LIFT — Exact all-prime half-band reconstruction through p⁴

**2026-11-11 · TASK_RESEARCH author-side theorem · AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

Frozen scientific source: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. This new result extends the earlier [p≡1 (mod 6) half-band theorem](https://github.com/awdawmip/enterprise-math/blob/e6b55e31df25dda46e73a3e1ab137d124039a43b/research_notes/portable_direct/2026-11-11_h40_d25_half_band_reflection_prime_character_author_portable.md) to **every prime p≥5**, reusing the previously author-proved p² reflection lemma. Original Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; mother objective OPEN.

## All-prime theorem (HB4*)

Let p≥5 be prime, b=⌊p/3⌋ and c=(p−1)/2. Define
\[
a_k={(2k)!(3k)!\over216^k(k!)^5},\qquad
W_p=\sum_{k=0}^{p-1}(6k+1)a_k,\qquad
L_p=\sum_{k=0}^{c}(6k+1)a_k.
\]
For b<j≤c let \(A_j=a_j/p\), which is a p-adic unit, and
\[
D_p(j)=2H_{2j-1}+3H_{3j-p-1}-5H_{j-1}-Q_p(216)\pmod p,
\]
with \(H_n=\sum_{r=1}^n r^{-1}\pmod p\) and Fermat quotient \(Q_p(216)=(216^{p-1}-1)/p\pmod p\). Then
\[
\boxed{W_p\equiv L_p+
p^2\sum_{j=b+1}^{c}\frac{(1+6p-6j)(1+pD_p(j))}{36j^3A_j}
+p^3\sum_{j=1}^{b}\frac{6j-1}{18j^3a_j}\pmod{p^4}.}\tag{HB4*}
\]
The middle sum uses modulus p² and high-reflection repair uses modulus p. All denominators are p-units. This theorem covers p≡1,5 (mod6); the prior one is recovered by b=2m,c=3m when p=6m+1.

**Proof.** For 0≤k<p, Legendre's formula yields \(v_p(a_k)=\lfloor2k/p\rfloor+\lfloor3k/p\rfloor\). Thus for any p≥5 the ranges [0,b], [b+1,c], [c+1,⌊2p/3⌋], [⌊2p/3⌋+1,p−1] have valuations 0,1,2,3 respectively. Reuse the proved all-prime p² reflection identity R2 from [this immutable author proof](https://github.com/awdawmip/enterprise-math/blob/597ec5477d44563ac7073328183bac472ebd42ab/research_notes/portable_direct/2026-11-11_h40_d25_reflection_p2_harmonic_lift_author_portable.md). If b<j≤c, the floor pair is q₂=0,q₃=1, giving \(a_{p-j}/p^2\equiv(1+pD_p(j))/(36j^3A_j)\pmod{p^2}\). If 1≤j≤b, both floors vanish, giving \(a_{p-j}/p^3\equiv-1/(18j^3a_j)\pmod p\). Reindex the complete omitted half: \(W_p-L_p=\sum_{j=1}^{c}(1+6p-6j)a_{p-j}\). Substitute both normalized identities, retaining the middle \(6p\) term at the target precision; reduce the p³-band weight mod p. This gives HB4*. □

Reducing modulo p³ gives the exact all-prime identity
\[
\boxed{W_p\equiv L_p+p^2\sum_{j=b+1}^{c}\frac{1-6j}{36j^3A_j}\pmod{p^3}.}\tag{HB3*}
\]
This is a prime-independent observer-preserving structural compression; it does not yet prove the arithmetic supercongruence \(W_p\equiv \chi_{-3}(p)\,p\pmod{p^3}\) for arbitrary p, where \(\chi_{-3}(p)=1\) for p≡1(mod3) and -1 for p≡2(mod3).

## Complete finite validation

Exact integer modular recurrence and direct factorial-coefficient crosschecks for p=5,7,11,13,19,31,73,157,373. Exhaustive prime enumeration **all 1,227 primes 5≤p≤10000**: every high reflected coefficient matches R2 to its required digit and every reconstructed W matches the full weighted sum mod p⁴. This comprises **956,066** middle reflected indices (each mod p²) plus **1,911,516** uppermost reflected indices (each mod p), a total of **2,867,582 exact reflection comparisons**, and 1,227 whole-sum identities.

Sample exact values (columns \(p,L_p\bmod p^4,\text{middle}\bmod p^2,\text{highest repair}\bmod p,W_p\bmod p^4\)):
- (5,220,16,0,620)
- (11,1199,67,6,2651)
- (13,24687,75,5,19786)
- (157,249127600,23177,96,584354000)
- (373,7176413322,68898,278,11832087049)

All computations use modular inverses over p^r for the source recurrence, not floating point. The standalone checker and per-prime exact JSON certificate accompany the portable research package. The earlier independent 1,227-prime finite character check agrees with the p³ reductions but remains an empirical bounded claim.

**BRC observer discipline.** Population: full index-labeled p-adic weighted coefficients. Readout and allowable future action: weighted sum mod p⁴, followed by precision reduction modp³. The middle two-digit and outer one-digit residuals are explicit repair coordinates for the index reflection; their different valuations, signed weights and provenance are retained. There is no native H0/B0 Frobenius execution claim or new Source CLAIM.

**Next mathematical step:** seek a finite paired-WZ/telescoping certificate for the all-prime HB3* lower-half-plus-reciprocal-middle expression, with separate p≡1 and p≡2(mod3) target residues. Authentic original-class H0/B0 remains a separately authorized native Source task. Historical UR V2 four-file 94,687-byte SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 original remains unlocated; completed UR mathematics is not to be repeated.
