# BRC-Shor: sparse measured-output readout with a certified missing-mass residual

Event-ID: brc-shor-sparse-readout-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; no independent researcher review, Lean, Working Truth or Foundation admission.
Source: enterprise-math@157350f30dc299597d356a0b1460ef3254e55686. Local parent48cf59fc5d0d8e620d8bb5f2aa51310ac65a319c.

## Result and exact scope

This stage produces complete large-register measurement outcomes without first
computing the period AND without a Q-entry wave/output array, when its explicitly
bounded spectral list captures enough probability. It is an output-sparsity route,
not a general solution of single-wave tensor contraction. It bypasses the stage12
wave-bank contraction by analytically averaging to the existing exact character
oracle BEFORE searching frequencies. All earlier wave histories are retained.

The state is the standard uniform exponent state, a is a unit, Q=2^m, the QFT is
ideal, the second register unconditioned, and integer bit reversal corrected.
Only this fixed final first-register measurement is preserved. New production
arithmetic is integer/Fraction; no period/factor/recurrence finder is imported.
The existing characteristic_numerator, collision_mass and certified twiddle
constructor are executed unchanged. IntegerQFT.transform is not used by the new
sampler. The cosine table has131072 entries in recorded practical runs, independent
of Q but charged; it is not a free primitive.

## Useful equations and acceptance certificate

Let chi(d)=E exp(2*pi*i*d*K/Q). Reuse the exact identity
  Q chi(d)=(Q-d)[a^d=1]+d[a^(Q-d)=1], 0<d<Q.
Each call costs two modular powers. At L=2^t,h=Q/L,
  Pr(K modL=y)=1/L+(L-1)/L E_J[chi(hJ)cos(2*pi*yJ/L)],
where J is uniform on1..L-1. A bounded low-bit-residue tree searches large-mass
frequencies by sharing long-range probes across its current nodes. This is not
shortening the coherent path length. Practical search is heuristic; missed peaks
cause a failure of final certification rather than a silent wrong distribution.

Freeze the discovered support F, then use independent fixed-count probes for
simultaneous pointwise lower masses l_k<=P(k). Numerical cosine/character/product
rounding is bounded by4/2^b+2/D_root+3/D. Hoeffding and rescaled Maurer-Pontil
empirical Bernstein bounds use H=ceil(log2(8|F|/delta)); their union allocation
includes both inequalities, both tails and every frequency. Exact small supports
use no statistical claim. Every endpoint is rounded outward with integers.

For Z=sum l_k>0, q(k)=l_k/Z gives P=Zq+(1-Z)R for some probability R. Therefore
  TV(P,q)<=1-Z.
The missing-mass residual includes omitted frequencies, search mistakes and both
numerical/statistical margins. Only Z>=1-epsilon releases a law and samples.
No rare-prefix division, seed rejection or retry-until-success is involved.
The guarantee is that an incorrect accepted certificate occurs with probability
at mostdelta over the fresh certification experiment. Acceptance itself need not
be likely; conditional coverage given an arbitrarily rare acceptance is not
asserted. Fixed benchmark PRNG seeds are reproduction, not an IID proof.
A compiled-law batch is IID conditional on its law only; a conservative comparison
to independent true samples adds delta+batch_size*epsilon. No strong batch bound
is claimed at the coarse experimental precision.

A conservative polynomial guarantee under an approximate-sparsity promise is
proved in PROOF.md: disable heuristic early refusal/neighborhood replacement,
keep sufficiently many nodes and use sufficiently large Hoeffding budgets.
Those sufficient budgets can be much larger than the practical defaults.
Schwarz--Van den Nest arXiv1310.6749 is explicit prior art for sparse-output
simulation; the current specialized tree/certificate is not claimed globally new.

## A deterministic stop on the genuine hard modulus

The true reduced density has largest eigenvalue <=ceil(Q/r)/Q, where r is used
only in the proof. Thus any output probability is at most this value. An actual
K_W=W certificate gives r>=W, and EVERY law supported on at mostK outcomes obeys
  TV(P,q)>=max(0,1-K*ceil(Q/W)/Q).
This is a bound on explicit output support, not on the number of parameters of an
implicit distribution, not on every wave representation, and not on factorization.

For N18446743979220271189,a2,m128,W2^24,K64, the inherited collision computation
uses4096 residue keys,8191 modular multiplications and one inverse. It certifies
TV>=262143/262144 for every64-point output law. Three measured refusals took
median2.315284ms and occurred before randomness or cosine-table allocation.
More precision cannot repair this support limitation. No hard-instance samples
or hidden period computation were produced.

Uniformly deleting input paths is also not this algorithm: keeping B ofQ paths
and normalizing gives, after averaging subsets,
  rho_B=lambda*rho+(1-lambda)I/Q, lambda=(B-1)/(Q-1),
hence the measured law is lambda*P+(1-lambda)*Uniform. Twelve exhaustive subset
checks verify this distinction. The new tree probes correlations at hJ, including
large separations, and truncates only the final output after measuring its defect.

## Executed progress, including failures

Frozen main plan:6 cases*3 repeats=18 records. Twelve compilations released96 full
outputs;3 N509 low-budget cases failed the mass residual;3 hard-modulus cases were
deterministically rejected. Small moduli with a huge output register are NOT hard
factoring benchmarks. No CPU pinning, no hosted execution, all work local.

Main median compile times and whole-law TV upper bounds:
- N23,a2,m10,K64:0.108713113s, bound0.0303907394.
- N23,a2,m64,K64:5.719464106s, bound0.1699676514.
- N23,a2,m128,K64:9.266506297s, bound0.1631832123.
- N71,a2,m64,K128:5.660501724s, bound0.2150506973.
- N509,a16,m32,K128:0.858101759s, all refuse, median residual0.4770002365.
The128-bit N23 run uses505843 exact character calls (median), NOT2^128 states.
Reference periods are computed only AFTER candidates. For large Q, references
evaluate the finite selected support at high precision using the period formula;
no full Q array is constructed even by those checks.

A separate fixed higher-precision diagnostic N23,m128,K64,1048576 certification
probes FAILED target0.1: residual69149/524288, support actually contained only
0.8930126454 mass. Improving certification alone did not repair discovery.
A separately frozen neighborhood refinement uses the top12 discovery anchors
plus offsets-2..2, resulting in56 distinct tested frequencies, with fresh fixed
certification. It PASSED at residual103305/1048576 (<0.09852), with38 positive
sampling weights; post-run actual TV is0.0733400842454 and support mass0.9605592443.
Time25.215737489s,1531890 character calls/3063780 modular powers. This is one
separate diagnostic, not a three-run median or a blind holdout performance claim.
No period was used to select the anchors or neighboring frequencies.

Three additional predeclared factor demonstrations compile64-bit outputs at N21,
35,77 (base2), then use continued fractions and gcd. Sixteen outputs per case give
verified factors(3,7),(5,7),(7,11). The tested returning exponents6,12,30 occur ONLY
in postprocessing and are not claimed minimal by that code. These tiny moduli are
functional closed-loop checks, not competitive factorization. Their compilation
costs9.699112219/15.608258921/8.220473140s are fully charged.

All new bounded checks passed:10332 exact character comparisons,6970 coset mass
checks,192 high-precision phase checks,5921 exact positive-submeasure inequalities,
1794 output-support bounds,57 exact binomial coverage grids,12 input-thinning
identities,1000 output-support draws,7 invalid/resource checks,poisoned-order
routine and pre-randomness refusal tests. New candidate AST has no float/complex
literal or arithmetic / operator. All15 available main-run pointwise-bound/law
checks, both diagnostics and3 factor-law checks covered their references. Same
author, no independent research review or Lean/full-project verification.

Main timings preserve their exact V1 source; optional neighborhood code and its
resource guard are recorded separately. Tool timeouts kept completed JSONL rows
and resumed only missing repetitions. A final AST audit initially flagged pathlib
slash syntax in the demonstration wrapper, not numerical floating arithmetic;
joins were changed and the complete checks rerun. No failure was erased.

## Research endpoint

Output work is O(m*K*n_discovery+K*n_certification+2^phase_bits) integer updates
plus at most2(m*n_discovery+n_certification) modular powers, and O(K+m+2^phase_bits)
integer storage. Configured K/probe counts need not suffice for a given input.
Dense state dependence has been removed in the accepted sparse cases, but the
sparsity requirement remains; no new general Shor/order/factoring speedup is made.

Next: an implicit, efficiently sampleable large-support frequency representation
that retains long-range coherence without enumerating peaks or supplying r.
The hard-case bound excludes merely enlarging a small explicit list. Existing
wave-mixture, fixed-observer and residual tools remain valid alternatives.

Publication is a research checkpoint only. The cumulative bundle preserves all
prior main history and the separate cloud-wavepacket branch. Full code, exact
proofs, frozen plans, failed runs and raw results are delivered on the requested
Drive surface; actual upload and hash readback are recorded after delivery.
