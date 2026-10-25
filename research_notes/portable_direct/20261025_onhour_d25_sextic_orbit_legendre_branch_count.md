# D25/LIFT: exact sixth-root involution orbit criterion for the low-rank Legendre zero

2026-10-25 | TASK_RESEARCH / author-side exact derivation | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is NOT a Source-native checkpoint, Result, independent review, native benchmark or the all-prime JT2 theorem.

Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Scientific target is the original second digit (Delta_p-R_p mod p), not the already accepted UR/JT0 first digit. The immutable input read was current D25 taskbook (blob 53a3ef039325534e3715add837f0eee332289984); prior author-only Clausen third-digit jet is \`research_notes/portable_direct/20261025_onhour_d25_clausen_three_band_local_jet_joint.md\`.

## Exact new theorem: finite-field zero iff integer orbit balance

Let p=6m+1 prime, p=13 or 19 mod 24. Let L0 = sum_{j=0}^m 2^{-j} C(m,j) C(2m,j) in Z_(p), the exact previously retained low-rank coefficient. In F_p set S = F_p minus {0,-1,-1/2} and K(x) = x^(4m) (x+1)^m (x+1/2)^(2m). Fix any primitive sixth root zeta in F_p and put iota(x) = -(2x+1)/(2(x+1)) (extended by iota(-1)=infinity, iota(infinity)=-1).

For all x in S, K(x)^6=1; iota preserves S, has no fixed point, and K(x)K(iota(x))=-1. Thus every unordered two-cycle has values exactly one of O={1,-1}, A={zeta,zeta²}, B={zeta^4,zeta^5}. Let nO,nA,nB count these *integer* orbits. Then

    nO + nA + nB = (p-3)/2;
    L0 = -(nA-nB) (zeta+zeta²)  (mod p);
    (zeta+zeta²)^2 = -3 (mod p).

Since |nA-nB| <= (p-3)/2 < p and zeta+zeta² is a unit,

    L0 = 0 (mod p)  <=>  nA = nB as ordinary integers.

Changing zeta to its conjugate swaps A/B, preserving equality. **This proves only equivalence, not the still-open all-target theorem nA=nB or L0=0.**

## Exact proof

The identity L0 = [X^(2m)](1+X)^m(X+1/2)^(2m) follows by binomial expansion. Multiply that polynomial by X^(4m). Its monomial degrees range from 4m to 7m, so the ONLY positive multiple of p-1=6m within this interval is 6m. Summing over x in F_p picks out that coefficient with factor -1, and the three zero branches contribute 0; hence L0 = -sum_{x in S} K(x) (mod p).

Let G(x)=x^4(x+1)(2x+1)^2, so K(x)=2^(-2m)G(x)^m. Directly,

    G(x) G(iota(x)) = (1/32) [x(2x+1)/(x+1)]^6.

On S the bracket is a nonzero p-unit; raising to m and using p-1=6m yields K(x)K(iota(x))=2^(-9m)=2^(-3m)=(2/p)=-1 because p=13,19 mod 24. The only fixed points solve 2x²+4x+1=0, discriminant 8, a nonsquare in these classes. The involution pairs S into (p-3)/2 genuine disjoint orbits. Writing K(x)=zeta^j, the partner has label 3-j modulo 6; pair sums for O,A,B are 0,s,-s, where s=zeta+zeta² has square -3. Summation proves the congruence and integer-count equivalence.

## Derived exact first-derivative observer, not compressible to counts

D0 = sum_{j=0}^m j 2^(-j) C(m,j) C(2m,j), the previously preserved first Clausen moment. Differentiate the same *finite* generating polynomial in a parameter z:

    B(z) = [X^(2m)] (1+X)^m (X+z/2)^(2m);
    D0 = B'(1) = m [X^(2m)](1+X)^m (X+1/2)^(2m-1).

Orthogonality gives

    D0 = -m sum_{x in S} K(x)/(x+1/2) (mod p).

Per unordered orbit {x,y=iota(x)}, since y+1/2=-x/[2(x+1)], an equivalent signed position-weighted port is

    D0 = -2m sum_orbits [ K(x)/(2x+1) - (x+1) K(y)/x ] (mod p).

The bracket is independent of which orbit representative is named x (it equals half the symmetric pair contribution). This is actual BRC typed reuse: sextic-labeled signed orbit counts suffice for L0 zero, but not for D0 or the original divided third-digit observer. Collapsing to nA+nB or total positive mass erases nA-nB; collapsing labels/positions erases D0. Preserve separate original Clausen cutoff, Frobenius and provenance ports.

## Exact finite checks, and incompleteness

An independent checker, with only integer modular arithmetic, verified each step, all orbit coverings, zero/derivative character-moment identities, weighted per-orbit observer, and binomial L0,D0 independently for **all 52 target primes p<=1200 plus p=19963 (53 primes)**. Zero identity mismatches. Observed nA=nB in these 53 cases only. Samples (p,nA,nB,nO,D0): (13,2,2,1,7); (19,4,4,0,1); (211,32,32,40,42); (19963,3280,3280,3420,6798). Finite evidence neither proves orbit balance uniformly nor completes JT2. No native Hasse/[X]U benchmark was run.

NEXT SCIENTIFIC UNIT: Find an all-target category-switching bijection or use the exact D=-24 CM / finite-field Jacobi-sum theorem to establish integer nA=nB, then carry the independent D0 first moment and full Clausen signed p² cutoff into previously derived joint LIFT residual. Failing a uniform theorem, test for an exact contrary orbit-count witness, preserving all source provenance. Original Delta_p-R_p, kappa/Frobenius directions, pinned native benchmark, Source admission and independent Driver review remain outstanding.

## Control/identity provenance

Research ordinary conversation fixed as \`chatgpt-research-onhour-enterprise-math-20260923\`, not maintenance \`chatgpt-hourly-enterprise-math-20260921\`. Read-only Gateway version 0.6.11 source control 5112b02283d53205fc96651c61b204ee41bf28da; Site status lacked Researcher write authority. Some previous request IDs read as CONTROL_REQUEST_NOT_FOUND by this client; that does not establish an empty queue. No new session, CLAIM, run, native checkpoint, freeze or review is claimed. The separate support issue #1539 remains the proper authority-binding recovery path. Neutral GitHub publication is only author evidence; it does not obtain Source research rights or alter original scheduler, phase or notification settings.