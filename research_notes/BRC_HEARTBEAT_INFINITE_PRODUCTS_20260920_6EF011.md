# Heartbeat: infinite products, persistent correlation phase and finite-action cooling

Event-ID: brc-heartbeat-infinite-products-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author proofs/checks, no independent review, Lean or admission.
Source read: enterprise-math@c334ee8832d8c3b0bcc2f4d077d62ed071ed86ba; global@273ea47fb9773b32e8bc40fbfcbef51cf5c51bdd.
Standalone parent: afdc4ac; inherited Stage19 code retained unchanged.

## Main advance

Studied the actual infinite-product problem rather than asserting that every
finite positive remainder has a positive limit. With fresh full-rank baths,
x_j=(1-d_C mu_j)sin^2(theta_j), the inherited joint spectral certificate is
Omega_n>=lambda_0 product(1-x_j)I. Its limit is positive iff sum x_j is finite,
equivalently iff sum[-ln(1-x_j)] is finite. This is classical product analysis
applied to the declared channel. A proved future loss sum R gives the integer-
rational tail interval P_K max(0,1-R)<=P_infinity<=P_K. No tail is inferred from
finite data. Exhaustion of the lower certificate is NOT proof of actual cooling:
a stationary full-rank state remains unchanged while this bound can tend to zero.

## A nonvanishing residual need not approach a stationary state

In a common bath eigenbasis, the exact correlation-block multiplier is
z_j=cos^2(theta_j)+i cos(theta_j)sin(theta_j)delta_j. Its squared modulus is
(1-u_j)(1-(1-delta_j^2)u_j). The squared loss lies between u_j and2u_j. Absent a
finite zero multiplier, positive limiting magnitude is equivalent to sum u_j<infinity.
Phase is an additional ordered variable and need not converge.

For tau=diag(3/4,1/4), choose theta_k=2atan(1/k), k>=2, using exact rational
cosines/sines. The lower off-diagonal mode is
z_k=((k^2-1)^2+i k(k^2-1))/(k^2+1)^2.
The magnitude tends to R>0, but arg z_k=atan(k/(k^2-1)) has a divergent sum with
increments tending to zero. Therefore the complex products have an entire circle
of limit points and do not converge. An explicit full-rank two-qubit state
Omega_0=tau tensor I/2+(1/16)X tensor X realizes it; marginals remain fixed,
while joint X-X and Y-X correlations rotate. This is NOT heat generation or a
claim of entanglement; the initial correlation is a declared preparation resource.
The analytically solved reset sector is not asserted to be the arbitrary full
interacting autonomous loop.

The executed8191-contact prefix gives rigorous infinite-modulus enclosure
[0.110108966807253743,0.110156040603501459] (display rounded; exact rational endpoints
in raw data). The inherited spectral-floor multiplier has infinite-limit interval
[0.320768520623858338,0.320846852374926436]. These are analytic-tail certificates,
not visual extrapolations. The exact product has a252254-bit common denominator;
three-run median compute time934313280ns, excluding module startup. Normalized
mode real parts at31,127,511,2047,8191 contacts are approximately
-0.122428,-0.0156595,+0.105016,+0.0539873,-0.0845233. A fixed joint observable is
one quarter of these values. The infinite-circle assertion is proved analytically,
not by the number of observed sign changes.

Balanced +theta,-theta pairs and unbalanced +theta,+theta pairs have identical
scalar loss and final mode magnitudes, but different phases and long-time states.
Bath eigenbasis changes likewise require ordered matrix information; they cannot
be silently collapsed into this scalar mode formula.

## Nonzero calibration errors do not destroy the conclusion

For factors of modulus<=1, per-contact errors eta_k imply a uniform all-time
product difference <=sum eta_k. If their sum is less than R, the perturbed mode
has liminf modulus>=R-sum eta_k and cannot converge, because opposite ideal
subsequences remain separated. Its exact limit set need not remain a circle.
For fixed bath gap, mode derivative versus theta has modulus<=1. Thus arbitrary,
possibly correlated angle errors <=1/(100k^2) have total product error<=0.01.
Exact perturbed half-angle tangents1/k +/-1/(200k^2) realize nonzero such errors.
Six separately frozen2047-contact runs verify exact prefix bounds. The analytic
certificate proves perturbed liminf modulus>0.10010 for the entire allowed error
class, not only those runs. Nothing is forced to perfect closure or zero error.

## Finite action, countably many contacts, and a real time budget

For serial SWAP interactions H_int=g(t)SWAP, let contact action
A=sum integral |g(t)|dt/hbar. Finite A makes sum sin^2(theta_j) finite, hence the
spectral product remains strictly positive even for countably infinitely many
contacts with individually full-rank baths. Every trace-norm accumulation point
of the finite retained SC state inherits this floor. Arbitrary intermediate SC
unitaries do not remove it. This rules out hiding infinitely many effective resets
inside finite action; it is a theorem for this declared protocol class.

A common numerical bound needs common bath quality. If d_C mu_j>=nu>0,
convexity gives -ln f_j<=(-ln nu)sin^2(theta_j)<=(-ln nu)|theta_j|. Hence
lambda>=lambda_0 exp[-(-ln nu)A]. At strength capG and elapsed timeT,
A<=GT/hbar. With a specified rank-g target ground projector,
p_exc>=(d_S-g)d_C lambda_0 exp[-(-ln nu)GT/hbar]. If the FINAL target is Gibbs at
a fixed excitation gapDelta, then
T_temperature>=Delta/[k_B(ln(1/(g d_C lambda_0))+(-ln nu)GT/hbar)]>0.
This is a conditional inverse-time floor, not a universal third-law derivation,
not a proof that P000 supplies a uniform purity floor, and not a fixed minimum
positive temperature for unlimited resources. Pure baths, hidden initial resources,
returning correlated environments and unbounded strength change the premises.
One almost-pure full-rank bath already shows why finite action alone supplies no
UNIFORM floor across all possible bath preparations.

## The physically bounded fine-contact limit keeps coherence, not free dissipation

Fix total action and split it into n contacts with tan(theta_n/2)=1/n. The total
sin^2 strength is <=4/n, but the total coherent angle tends to2. The channel tends
to conjugation by exp(-i2tau), not thermal reset; its delta1/2 mode tends to exp(i).
A trace/diamond-norm telescoping estimate is proved, with full-state distance
<=12/n+2/(3n^2). At n4096 the exact mode squared magnitude is0.9982924751290584,
with loss<=0.001708984375. Thus subdividing bounded interaction does not manufacture
finite damping. The old sqrt(dt) prescription has divergent action/strength unless
compensation or another explicitly different protocol is supplied.

## Zero limit with finite extracted heat: a retained boundary, not a contradiction

A second explicit commuting qubit experiment has p_0=1/3, fixed c3/5,s4/5,
and fresh bath excitations e_j=(16j+23)/[16(j+2)(j+3)]>0. Exact substitution gives
p_j=1/(j+3)>0 and p_j->0; thermal temperature isDelta/[k_B ln(j+2)]. Total extracted
heat tends toDelta/3, not infinity. Contact action n acos(3/5), fresh-copy count
and bath cooling requirements do diverge. This does NOT say total reservoir
preparation energy or free energy stays finite. At1024 contacts actual p=1/1027,
while the conservative spectral floor is about1.40369e-447; its smallness is not
misidentified with the actual temperature. Assigning durations2^-j produces a
formal finite accumulation time but requires divergent strength and action.
The strong zero-temperature goal is retained; its physical preparation assumptions
are not obtained by assuming the goal or discarding the valid zero-limit example.

## Executed evidence and scope

6607 finite checks passed:1360 exact mode-loss identities and1360 comparisons,
32 full inherited reset trajectories,32 marginal and32 relative-observer checks,
512 exact cooling recurrences/positive bath/finite heat/floor comparisons each,
320 bath-budget inequalities and320 angle bounds,256 telescoping products,
plus balanced pulses, different bath bases, tail intervals, fine partitions and
input/resource boundaries. New production uses integer/Fraction arithmetic and
executes inherited min_floor_step/reset unchanged. No new general BRC family or
Shor speedup is asserted.

Frozen main36 records, three repeats over12 configurations; an additional6-run
nonzero-error diagnostic was separately frozen.100-digit sequential reference
products,81 modular exact-product checks, saved medians and all36 raw main rows
were replayed without replacing timings. No CPU affinity. Computation timings
are certificate evaluation, not physical cooling durations. Finite tests do not
establish an infinite limit; the written proofs and analytic tail assumptions do.

Primary background: Ziman et al.quant-ph/0110164; Ciccarello et al.2106.11974;
Masanes--Oppenheim Nat Commun8,14538/1412.3828; Freitas et al.1911.06377;
Vu--Saito2408.04576v4/PRX15,041029. Classical infinite products, repeated-interaction
limits and resource third laws are prior art; global novelty is not claimed.

Next: derive an admissible native bath/preparation/interaction-budget class from
a finite autonomous supply, or extend the full noncommuting memory kernel with
certified tails. Do not assume the harmonic diagnostic proves this for arbitrary
interacting dynamics. Preserve phase correlations, all nonzero tails and the
strong goal's unresolved physical bridge. The cumulative standalone bundle retains
all prior history and is not the full Enterprise Math repository. Cloud upload
and immutable publication receipts must be verified separately.
