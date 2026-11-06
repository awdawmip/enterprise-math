# D25 / SECOND-DIGIT-LIFT — Exact D8 signed-orbit balance criterion

2026-11-07, Asia/Hong_Kong. TASK_RESEARCH logical lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded: chatgpt-hourly-enterprise-math-20260921. Frozen Source publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. The original216 mother objective is W_p ≡ p mod p³ for every prime p ≡ 13,19 mod24. P000 is unchanged; the following is an auxiliary finite-field observer, not native X6 or an execution of the p=373 H0/B0 benchmark.

## Reused frontier and chosen unfinished unit

Reuse the proved Pfaff–character bridge S_m ≡ -∑_x f(x)^m (mod p), branch-dependent signed Klein-four orbit laws, the prior two-point three-valued tau observer, quadratic/sextic bucket structure and Gauss/Clausen third-digit formulas. The new scientific unit **composes** these into an exactly labeled dihedral-eight *integer* signed-orbit count, compressing the first-digit proof to one equality on about p/8 objects, with a checked counterexample to orbitwise cancellation. Three-valued two-point character arithmetic itself is not claimed as a new mechanism.

Applied BRC interface T0_BRC: source-valued orbit and signed/phase readout retaining each y, f, Legendre (a,b), sixth-root value, dihedral group operation and original integer multiplicity. This is COMPOSE_APPLIED (Pfaff + Klein + reciprocal-character pair); positive-weight branch mass would erase the sign. No new general-purpose tool is introduced or admitted.

## Definitions and rational identities

Let p=6m+1>3 be prime with p ≡ 13 or 19 mod24, χ the Legendre character, and y=2x+1. Put X=F_p\{0,1,-1} and

v(y) = [2^{-7} y(y-1)^5(y+1)^2]^m
     = [x^5(x+1)^2(2x+1)]^m ∈ μ₆(F_p).

Set a(y)=χ(y²-1), b(y)=χ(y), δ=χ(-1)=(-1)^m, and c=2^{-m}. Here χ(2)=-1, so c³=-1. Define s(y)=-y, q(y)=y^{-1}, T(y)=(y-1)/(y+1). The generators form an order-eight dihedral group: s and q commute, T²=sq=-1/y, sTs=T^{-1}. These are all well-defined on X.

Direct substitution into f gives

v(sy)=a(y)v(y),   v(qy)=δ b(y)v(y),
f((Ty-1)/2) f((y-1)/2)
 = -2^{-7}y³[(y-1)/(y+1)]⁶,

and hence v(Ty)v(y)=δ c b(y). The sign ports obey
(a(Ty),b(Ty))=(δ b(y),a(y)),
(a(sy),b(sy))=(a(y),δ b(y)),
(a(qy),b(qy))=(δ a(y),b(y)).

## Theorem 1: an exact source-preserving D8 orbit formula (PROVED)

For p≡13 mod24, the two solutions y²=-1 form a unique two-element orbit whose signed sum is zero; all other orbits have eight elements. There are (p-5)/8 size-eight orbits plus this exceptional pair. For p≡19 mod24 all orbits have size eight, (p-3)/8 of them. Proof: other potential fixed points arise only at y=0 or ±1 (excluded) or from quadratics of discriminant 8 (nonsquare because χ(2)=-1); y²=-1 has two roots exactly in the 13-branch.

For p≡13: δ=1. Every Klein-four orbit K has constant (a,b) and sum_K v = v(y)(1+a)(1+b). T exchanges a and b. Thus an eight-orbit O either has no (+,+) points, and sum_O v=0, or all eight are (+,+). In the latter case its two Klein suborbits have values u=v(y) and w=v(Ty), with uw=c; hence

sum_O v=4(u+c/u).

The exceptional two-orbit has a=b=-1 and contributes zero.

For p≡19: δ=-1. Every Klein-four orbit has one (+,+) point and its total is 2v at that point. Each eight-orbit has exactly two (+,+) points. Given one y, the other is z=qT(y). Because b(Ty)=a(y)=1, v(z)=-v(Ty), so u=v(y), w=v(z) satisfy uw=c and

sum_O v=2(u+c/u).

Both identities conserve the original signed source and integer orbit multiplicity.

## Theorem 2: exactly one integer balance is equivalent to first-digit cancellation (PROVED)

The map u↦c/u has no fixed point on μ₆ because u²=c would give 1=u⁶=c³=-1. Its three two-element orbits include the pair {u,-u} solving u²=-c (zero sum); the other two pairs are negatives of each other and have nonzero opposite sums. Therefore

{u+c/u : u∈μ₆} = {0,+t,-t}, with t≠0.

Choose t as the numerically smaller positive residue of the nonzero pair solely to orient signs. For each size-eight orbit classify its exact sum as 0,+d t,-d t (d=4 for p≡13, d=2 for p≡19); include the exceptional size-two zero orbit in N0. Write N+, N-, N0 for the corresponding **ordinary integer** orbit counts. The previously established Pfaff bridge gives

S_m := ∑_{k=0}^{m} binom(m,k)binom(2m+k,k)
    ≡ -d t (N+ - N-) (mod p).

There are fewer than p orbits, so |N+-N-|<p. This yields the exact all-primes equivalence

S_m ≡ 0 (mod p)  ⇔  N+ = N- as ordinary integers.

The equality N+=N- itself remains open for arbitrary target p. This is a sharper one-difference observer than the prior six-bucket criterion and requires only about p/8 fully labeled orbits.

## Executed discriminating test

The accompanying standalone stdlib checker independently reconstructs the original integer Pfaff sum, enumerates every D8 orbit, verifies the orbit products and formulas, root-image {0,±t}, exact counts and the count identity. Results: all **312** target primes p≤10000 (157 p≡13, 155 p≡19), zero failures. The expected equality N+=N- was observed in all 312 finite tests.

| p | total orbits | N+ | N- | N0 |
|---:|---:|---:|---:|---:|
| 13 | 2 | 0 | 0 | 2 |
| 19 | 2 | 1 | 1 | 0 |
| 43 | 5 | 2 | 2 | 1 |
| 61 | 8 | 1 | 1 | 6 |
| 67 | 8 | 2 | 2 | 4 |
| 373 | 47 | 5 | 5 | 37 |

For p=373, the original 370 nonbranch points form 46 eight-orbits and one vanishing exceptional pair. Among the 11 paired surviving Klein quartets, 1 entire eight-orbit cancels; the other 10 yield exactly five +13 and five -13 modulo373. This is a source-labeled **ten-orbit finite certificate** for the existing first-digit observation, not the native divided-power/Frobenius experiment.

A useful counterexample to the candidate shortcut "every D8 orbit vanishes": at p=19 there are two size-eight orbits, with sums 12 and 7 modulo19 (both nonzero); they cancel **across** orbits. For p=373 there are 10 individually nonzero orbits. Thus the specific local cancellation proposal is refuted while the mother conjecture remains open.

## Next unit, dependencies and source recovery

Next exact mathematical action: seek a source-preserving *inter-orbit* involution or character/trace identity forcing N+=N- for every target p, test its action on the two p19 and ten p373 nonzero orbits, and only then combine with the already established Gauss second-jet and signed Clausen p²/p³ boundary. Retain the original frozen inputs, exact p373 benchmark (#1559), and explicit original sign/valuation/source data.

Native gateway checked this turn: CONFIGURED_NOT_LIVE_VERIFIED; research_authority_granted=false. em_status and receipt read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false). Original request onhour11-20261106-1400-exact-research-lane-continuation retained without reissue; old revision22 is historical, and session/claim/run are NOT_VERIFIED. Operator must verify dedicated Site backend client, reviewed version and secure credential before original receipt/Source continuation. Native #1559 still PENDING_OWNER / NOT_EXECUTED. This GitHub author-side proof/checker is **AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED**; activity REGISTER_PENDING / SYNC_DEBT.
