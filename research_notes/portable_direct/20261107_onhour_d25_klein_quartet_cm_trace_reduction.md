# D25 / SECOND-DIGIT-LIFT — signed Klein-quartet reduction and elliptic trace count

Date: 2026-11-07 Asia/Hong_Kong. Author-side TASK_RESEARCH, ordinary-control lane chatgpt-research-onhour-enterprise-math-20260923; never the maintenance lane. Publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Prior immutable author-side research frontier f77c5707d7a62ee3d3d59a8cbe5295b1e32ad1ff, especially 20261107_onhour_d25_pfaff_sextic_torus_port.md and 20261107_onhour_d25_inert_quadratic_sextic_bucket_balance.md. All statements below are for an auxiliary finite-field observer; they do not change P000 native X6/Heartbeat World.

## Objective and exact definitions

The frozen mother objective is W_p = sum_{0<=n<p} (6n+1)(2n)!(3n)!/[216^n(n!)^5] ≡ p (mod p^3), for primes p≡13,19 (mod 24). The previous independently derived Pfaff bridge gives S_m = sum_{k=0}^m binom(m,k)binom(2m+k,k) ≡ -sum_{x∈F_p} f(x)^m (mod p), with p=6m+1 and f(x)=x^5(x+1)^2(2x+1). A proof of S_m≡0 for all target p remains an unfinished first-digit subgoal.

This note proves a genuinely new orbit reduction on the p≡13 (mod 24) branch. Let p≡13 (mod 24) be prime; then m=(p-1)/6 is even, (−1/p)=1, (2/p)=−1. Put X=F_p\{0,−1,−1/2}; for x∈X put v(x)=f(x)^m∈μ_6(F_p), a(x)=(x(x+1)/p)∈{±1}, b(x)=((2x+1)/p)∈{±1}. Here (·/p) is the Legendre symbol, and the original x-index, orbit, sixth-root phase and signed weight remain recorded.

## Theorem A — exact four-point signed transfer (PROVED)

The two rational maps
s(x)=−1−x,    q(x)=−x/(2x+1)
preserve X, are commuting involutions, and generate a Klein four-group with product r=s∘q=−(x+1)/(2x+1). They satisfy the exact rational identities
f(sx)/f(x)=((x+1)/x)^3,
f(qx)/f(x)=−(2x+1)^(−9),
f(rx)/f(x)=((x+1)/x)^3(2x+1)^(−9).

Raising these ratios to m and using m even, 3m=(p−1)/2, 9m=3(p−1)/2, and Euler's criterion gives
v(sx)=a(x)v(x),    v(qx)=b(x)v(x),    v(rx)=a(x)b(x)v(x)
for every x∈X. For every four-element orbit O_x={x,sx,qx,rx}, this proves the exact finite-field equality
**SUM(O_x)=v(x)(1+a(x))(1+b(x)).**
Hence an orbit cancels precisely when a(x)=−1 or b(x)=−1; when a(x)=b(x)=1 it contributes 4v(x), with its original nonzero sixth-root sign/phase.

The only nontrivial exceptional orbit in X has size two: r-fixed points solve 2x²+2x+1=0 (discriminant −4), giving two F_p points. At such an x, x(x+1)=−1/2, so a(x)=(−1/2/p)=−1. Also (2x+1)²=−1; since p≡5 (mod 8), any square root of −1 is a quadratic nonsquare, giving b(x)=−1. Thus the unique two-point orbit has total v zero. Both s- and q-fixed points, x=−1/2 and x=0 respectively, were explicitly removed from X.

It follows, without dropping any original signed contributions, that
**SUM_{x∈X} v(x) = 4 SUM_{one representative x of each surviving 4-orbit} v(x)** in F_p,
where 'surviving' means a(x)=b(x)=1. This is a certified reduction of the first-digit Pfaff observer to a strict 4-orbit subpopulation, not a proof that its remaining weighted sum vanishes.

## Theorem B — exact integer count of all surviving quartets (PROVED)

Define the integer quadratic-character trace
t_p = SUM_{x∈F_p} ( x(x+1)(2x+1) / p ).
This equals #E(F_p)−(p+1), where E is the auxiliary elliptic curve y²=x(x+1)(2x+1) and #E includes its point at infinity. Its three finite roots {0,−1,−1/2} have Legendre cross-ratio 1/2, giving j(E)=1728; no native CM/H0/B0 experiment is implied.

On X, the integer character sums satisfy
SUM_X a(x)=−2
(the full nondegenerate quadratic character sum is −1, with excluded x=−1/2 contributing +1),
SUM_X b(x)=−2
(the full linear character sum is 0, with excluded x=0,−1 contributing 1 each),
SUM_X a(x)b(x)=t_p
(the excluded three roots have zero product character).
Therefore the exact integer number M of surviving INPUTS x∈X is
M=1/4 SUM_X (1+a(x))(1+b(x)) = (p−7+t_p)/4.
All such x lie in four-element orbits, so the exact number of surviving **quartets** is
**C_p=(p−7+t_p)/16.**
The unique exceptional two-point orbit vanishes and is not counted among survivors. Consequently
**t_p ≡ 7−p (mod 16) for every prime p≡13 (mod 24)**,
as an exact integer consequence of the orbit partition. This is a scoped elliptic-trace congruence, not an assertion for all residue classes.

The number of zero-sum regular quartets is (p−5)/4−C_p. The full nonbranch population size p−3 equals four times the regular orbit count plus the exceptional two points.

## Reproducible finite computation

A separate independent Python 3 stdlib checker computes the original S_m from integer binomial recurrence, f and v from modular exponentiation, both transformations, exact two/four-point orbits, Legendre signs, signed orbit sums, and t_p as an *integer* character sum. The checker was executed locally on **all 157 primes p≡13 mod24 with p<=10000**, with zero failed assertions. Representative (p, t_p, C_p, zero-sum regular quartets, S_m mod p):

- (13, −6, 0, 2, 0)
- (37, 2, 2, 6, 0)
- (61, 10, 4, 10, 0)
- (109, −6, 6, 20, 0)
- (373, −14, 22, 70, 0)
- (397, −38, 22, 76, 0)
- (421, −30, 24, 80, 0).

At p=373, **22 nonzero signed 4-orbits, 70 zero-sum regular 4-orbits, and one zero-sum 2-orbit** partition the 370 nonbranch x. The 22 remaining signed phase contributions sum to zero modulo 373 in the executed test; deriving their total cancellation for every target prime is still open. The existing p≡19 mod24 branch has odd m and needs a separately typed transform: q then acts with factor −b, so the above p≡13 four-orbit cancellation theorem is not silently promoted to that branch.

## Provenance, BRC and continuation

The exact observer retains x, original f(x), the sixth-root v, quadratic pair (a,b), orbit representative, signed contribution, and integer multiplicity. The quartet reduction is an observer-safe *reorganization*, not erasure of joint/signed information; it can be compared with BRC residual classification without claiming an executable native BRC operator or replacing the native same-original-class experiment. No independent mathematical acceptance/review is asserted.

Highest author-side earlier source: f77c5707d7a62ee3d3d59a8cbe5295b1e32ad1ff. Mother objective remains OPEN. Next distinct scientific unit: study the complete signed survivor sum 4Σ_survivors v(x) for the p≡13 branch via CM quartic trace / character-orbit coupling, then separately construct an admissible odd-m branch for p≡19. A discriminating test is to seek a second involution on the **surviving** quartets that reverses v; verify its actual action at p=13,37,373 (or preserve a counterexample), without assuming that a pure cardinality match proves signed cancellation.

Source recovery is separate: original target_request_id onhour11-20261106-1400-exact-research-lane-continuation retained. On 2026-11-06T21:00:48Z the Site gateway reported CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; em_status returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Historical checkpoint revision 22 remains historical. Session/claim/run NOT_VERIFIED; do not replay mutation or borrow maintenance-lane identity. Native p373 original-class H0/B0 divided-power/Frobenius/κ independent reproduction remains issue #1559 NOT_EXECUTED/PENDING_OWNER. This Markdown and its checker/continuation are an author-side evidence checkpoint, with statuses AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED; REGISTER_PENDING / SYNC_DEBT for native registration.
