# D25 original 216 endpoint: universal third-digit correction 5p³

2026-11-03 Asia/Hong_Kong. AUTHOR-DERIVED / PROVED BY INTEGER FACTORIALS / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. TASK_RESEARCH lane chatgpt-research-onhour-enterprise-math-20260923. No maintenance-lane session or source authority is used.

Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, immutable scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Parent remains Delta_p-R_p=0 mod p for p mod24 13/19. This unit directly refines the original 216 endpoint in the preceding exact minimal two-state recurrence. Existing higher-strip mod p⁴ reflection is retained; this note proves the specific final coefficient's universal closed value.

## Theorem: sharp original endpoint congruence

For every prime p≥5, set

b_k=binom(2k,k)^2 binom(3k,k)/216^k,
W(n)=sum_{k=0}^n (6k+1)b_k.

Then v_p(b_{p-1})=3, and the leading divided coefficient is *independent of p*:

b_{p-1}/p³ ≡ -1 (mod p).

Consequently the signed terminal observer satisfies

**W(p-1)-W(p-2) ≡ 5p³ (mod p⁴).**

This precisely repairs the mod p⁴ endpoint of the mod p³ two-state certificate. It is an all-prime algebraic conclusion and does not require CM inertness. The original full-target mod p³ question remains OPEN.

### Proof

Put C2=binom(2p-2,p-1) and C3=binom(3p-3,p-1). Legendre's formula gives v_p(C2)=v_p(C3)=1 for each p≥5. Thus v_p(b_{p-1})=2+1=3.

For the leading units, Wilson's theorem and the residue blocks give

(2p-2)!/p ≡ (p-1)!(p-2)! ≡ -1 (mod p).

The factors p and 2p in (3p-3)! contribute 2p², while the remaining residues consist of two complete nonzero blocks and the final 1,...,p-3. Hence

(3p-3)!/p² ≡ 2[(p-1)!]²(p-3)! ≡ -1 (mod p),

because (p-3)!≡-1/2 mod p.

Therefore

C2/p = [(2p-2)!/p]/[(p-1)!]² ≡ -1 (mod p),

C3/p = [(3p-3)!/p²]/
        {[(p-1)!][(2p-2)!/p]} ≡ -1 (mod p).

Fermat's theorem ensures 216^(p-1)≡1 mod p. Therefore

b_{p-1}/p³ = (C2/p)^2(C3/p) / 216^(p-1) ≡ (-1)^2(-1)=-1 mod p.

Finally the endpoint weight is 6(p-1)+1=6p-5, and (6p-5)(-1)≡5 mod p. Multiplying by p³ yields the claimed p⁴ congruence. QED.

## Independent full-source arithmetic

An original-binomial integer algorithm checked the divided endpoint b_(p-1)/p³=-1 modulo p for **all 166 primes 5≤p≤1000**. An independent coefficient-ratio algorithm computed original W(p-1) and W(p-2) modulo p⁴ for **11 target primes** p=13,19,37,43,61,67,109,139,181,373,1171. Every difference was 5p³ mod p⁴. The checker and the finite JSON result are published with this proof.

Concrete exact target-class witnesses (all numbers modulo p⁴):

p=13, p⁴=28561, W(12)=19786, W(11)=8801, full third-digit (W(12)-13)/13³=9 mod13.
p=19, p⁴=130321, W(18)=82327, W(17)=48032, third-digit 12 mod19.
p=373, p⁴=19356878641, W(372)=11832087049, W(371)=11572611464, third-digit 228 mod373. The terminal difference is 259475585=5*373³.

Thus the stronger proposed statement W(p-1)=p mod p⁴ for *all* target primes is refuted already by p=13 and p=19; this is a precision-specific observation, not a claim about possible stronger conditional families. The original p³ statement is unchanged.

## Research continuation and strict boundaries

The new exact method carrier is the final third digit of the original signed coefficient, tagged by index k=p-1, its factorial valuation 3, source original-216 and the observation 'truncate one term'. A mod p³ projection deletes it only with the exact stated observer bound. This is the BRC/useful-coordinate interpretation; it is not native Heartbeat X6 or the same-class H0/B0 Frobenius.

Next action remains to attack the *original p³ second digit* (6AD-1)/p+h²+E=0 mod p uniformly, now knowing precisely that a one-term rational Gosper antidifference does not exist and that the terminal p⁴ digit requires +5. Explore a parameterized WZ/two-state CM intertwiner with checks at 13,19,373. Original p373 native H0/B0 issue #1559 remains NOT_EXECUTED and PENDING_OWNER; this separate benchmark requires actual [X]U, rank, semilinear Frobenius, odd signed observer and independent replication.

On this author-side surface no new Source session, claim, run, checkpoint, Result, Driver review or mathematical admission is claimed. Old Research recovery #6632 is historical read-only success; old dispatch #6633 was definitively FAILED_UPSTREAM_CODE_REVIEW_REQUIRED. Global rules read a27e1a68f7746578368b8cc860a6f94a01c720cf; Enterprise Math original control head at research start 84cb80025bd64c7d66f84b4634217416439474a1; frozen source unaffected. No scheduler/notification changes.
