# D25 / SECOND-DIGIT-LIFT — complementary odd-m signed Klein orbit for p≡19 (mod 24)

Date: 2026-11-07 Asia/Hong_Kong. Same authorized author-side TASK_RESEARCH lane chatgpt-research-onhour-enterprise-math-20260923; unrelated maintenance lane chatgpt-hourly-enterprise-math-20260921 is excluded. Frozen Source publication TP2-B6F4FC938FF94941C1B7, scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. This unit follows the read-back author-side p≡13 mod24 quartet checkpoint at e76c613c266d6e3b2d3020314460124db99e8237. P000 Heartbeat native X6 is unchanged; all group operations here are in an auxiliary finite-field observer.

## Exact input and mother objective

For a prime p≡19 mod24 write p=6m+1; then m is odd, (−1/p)=−1, (2/p)=−1. Define X=F_p\{0,−1,−1/2}, f(x)=x^5(x+1)^2(2x+1), v(x)=f(x)^m ∈ μ_6(F_p), a(x)=(x(x+1)/p) ∈ {±1}, b(x)=((2x+1)/p) ∈ {±1}. Reuse the previously proved exact coefficient bridge
S_m=sum_{k=0}^m binom(m,k)binom(2m+k,k) ≡ −sum_{x∈X}v(x) (mod p).
The frozen mother target is Original216 W_p≡p mod p³, for p≡13,19 mod24. The first-digit S_m cancellation and the third-digit signed Gauss/Clausen boundary remain the relevant open goals.

## Theorem C: exact odd-m signed quartet port (PROVED)

On X use the commuting involutions s(x)=−1−x and q(x)=−x/(2x+1), and r=sq=−(x+1)/(2x+1). The rational identities
f(sx)/f(x)=((x+1)/x)^3,
f(qx)/f(x)=−(2x+1)^(−9),
f(rx)/f(x)=((x+1)/x)^3(2x+1)^(−9)
hold identically. Since m is odd and 3m=(p−1)/2, they imply
**v(sx)=a(x)v(x), v(qx)=−b(x)v(x), v(rx)=a(x)b(x)v(x).**
For any 4-point orbit O_x={x,sx,qx,rx}, its exact signed sum is
**sum_{z∈O_x}v(z)=v(x)(1+a(x)−b(x)+a(x)b(x)).**

Unlike the even-m p≡13 branch, no full quartet vanishes termwise here: for (a,b) ∈ {±1}², the multiplier is +2 except at (−1,+1), where it equals −2. Each nonzero v yields a nonzero orbit sum in F_p. This is a strictly scoped noncancellation theorem for this particular quartet grouping, not an obstruction to global cancellation across different quartets.

There are no fixed points on X: s and q fix only the excluded branch points −1/2 and 0, and r fixes roots of 2x²+2x+1 whose discriminant −4 is nonsquare when (−1/p)=−1. Hence every orbit in X has exactly four elements and there are precisely (p−3)/4 such quartets.

## Theorem D: exactly one representative of each Legendre-sign pair per orbit (PROVED)

Direct substitution gives
a(sx)=a(x),  b(sx)=−b(x),
a(qx)=−a(x), b(qx)=b(x).
Consequently the four elements of every quartet have exactly the four sign pairs (+,+), (+,−), (−,+), (−,−), once each. Let
R_p={x∈X : a(x)=b(x)=+1};
then **|R_p|=(p−3)/4** as an exact integer, with one representative per quartet. Choosing that representative in Theorem C yields the lossless signed first-digit observer
**S_m ≡ −2 SUM_{x∈R_p} v(x) (mod p).**

The auxiliary integer elliptic-character trace t_p=SUM_{x∈Fp}(x(x+1)(2x+1)/p) is exactly zero. This follows from s(x)=−1−x, which sends g=x(x+1)(2x+1) to −g, while (−1/p)=−1; zero roots contribute zero. The zero trace also follows by summing ab over each complete quartet, one of each pair. Here E:y²=g(x) has j=1728, but no native H0/B0/Frobenius benchmark is being claimed.

This is a new branch-specific exact reduction: **every** quartet contributes a nonzero ±2v amplitude, yet one carefully typed (+,+) source point from each quartet suffices to reconstruct the entire sum. The even-m p≡13 branch instead has signed quartet cancellations and a CM-trace-controlled surviving subpopulation, as already proved in the preceding checkpoint.

## Executed finite-field verification

A separate stdlib script evaluated all **155 primes p≡19 (mod 24) with p<=10000**. All assertions passed: group action, absence of exceptional orbits, one sign-pair representative per quartet, precise signed multiplier, zero elliptic trace, equality to original integer Pfaff S_m by modular binomial recurrence. Representative (p, #quartets, S_m mod p, t_p):
(19,4,0,0), (43,10,0,0), (67,16,0,0), (139,34,0,0), (163,40,0,0), (211,52,0,0), (331,82,0,0), (379,94,0,0).
The observations S_m=0 on these 155 inputs remain finite evidence only. The exact one-representative reduction and t_p=0 have complete general proofs.

## Proof scope / next unit / operational debt

Source-preserving BRC-compatible labels: full original x, v(x) signed sixth-root phase, a(x), b(x), orbit, selected (+,+) representative, rational map and finite-field operation, integer orbit multiplicity. No removal of original-class native residue, original 373 experiment, or project X6 world properties is implied.

Together the two branch-specific formulas are:
p≡13 mod24: S_m=−4 SUM_{surviving 4-orbit reps}v(x), with #survivors=(p−7+t_p)/16 and a unique vanishing exceptional 2-orbit;
p≡19 mod24: S_m=−2 SUM_{x∈R_p}v(x), with |R_p|=(p−3)/4 and t_p=0.
Both are modulo p and retain the required signed residue. These define a concrete next test: seek a character pairing among the remaining representative phases, or a finite elliptic-character trace identity forcing their total cancellation, while keeping the already validated p² Gauss/Clausen boundary formula available for the p³ mother problem. Do not infer full first-digit or full W_p theorem from these observer reductions.

Native status as observed 2026-11-06T21:00:48Z: Site CONFIGURED_NOT_LIVE_VERIFIED; research_authority_granted=false; em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH operation_sent=false. Original request onhour11-20261106-1400-exact-research-lane-continuation remains unchanged/unknown. Researcher session, CLAIM, run, formal Result are NOT_VERIFIED; independent review/admission UNREVIEWED/NOT_ADMITTED; native same-original-class p373 #1559 NOT_EXECUTED/PENDING_OWNER. GitHub author-side evidence only, REGISTER_PENDING / SYNC_DEBT.
