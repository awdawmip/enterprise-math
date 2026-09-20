# BRC-Shor: an order-blind wave entrance and its measured contraction boundary

Event-ID: brc-shor-order-blind-ensemble-20260920-6EF011
Researcher-ID: EM-DIRECT-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE; same-author proofs/checks, no independent review or admission.
Read source: enterprise-math@80542befe28c34228acc582492e11a3f84c78a97.

## What changed

The previous chat stage10 samples eigenphase j/r after exact classical order preparation.
This stage does NOT call that preparation. Write f(x)=a^x mod N, Q=2^m, n=ceil(log2 N).
Uniform n-bit seed s defines a normalized wave with signs (-1)^(s dot f(x)). Averaging
its density matrix over seeds gives exactly [f(x)=f(z)]/Q, the actual reduced first-
register state. This is a Hadamard-basis ensemble, not a discovered spectral grid. One
wave amplitude sign needs one modular power and one parity. It needs no factors,
period or Q-entry table. The seed is frozen for each complete sample; no hard seed is
rejected in favor of an easy one. Arbitrary later joint-register operations are out of scope.

A dense integer QFT fallback now produces complete outputs without any order call.
The numerical single-output law has TV <=12m/2^p, with p selected before randomness.
Twiddles use inherited directed Dyadic roots unchanged plus certified integer recurrence.
All phase, butterfly and sampling arithmetic is integer/exact rational. Numerical
residual is uniform over seeds; averaging preserves it. This is NOT a cheap simulator:
each output explicitly uses Q-1 modular multiplies, mQ/2 butterflies, and O(Q) storage.
The compact wave descriptor is not passed off as compact evaluated state.

## A stronger exact theorem: product-wave ensembles force the spectral grid

For odd r<Q/2, every fully product pure vector in the range of the true reduced
rho is a spectral phase wave v_x=C*z^x with z^r=1. Every exact convex ensemble
of fully product pure states representing rho must therefore use these r waves
with total weight1/r each (up to global phases and duplicate components).

Proof, including zero amplitudes: range(rho) consists of r-periodic fibre-constant
vectors. A nonzero product support meets both exponent halves because each half
has length Q/2>r, so its highest bit is free. Its support consequently repeats
modulo Q/2 and is invariant under an r-shift there; coprimality forces full support.
Write v_x=C product c_j^(x_j). Adjacent ratios at x=2^j-1 and x+r must agree.
Since the latter is even, this forces c_j=c_0^(2^j); periodicity gives c_0^r=1.
Every positive ensemble member lies in range(rho), by testing ker(rho) and using
positivity. The first r matrix entries give the r Fourier moment equations, forcing
uniform weights. A complete argument is preserved in PROOF.md section11.

Thus the reduced rho itself IS fully separable. The entanglement diagnosed in the
cheap Walsh/cyclic ensemble is a choice of representation, not intrinsic for all
ensembles. However, requiring an exact fully product replacement brings back the
unknown spectral grid. This does not rule out approximate/low-but-nonzero-rank
ensembles, different tensor layouts, output-only representations, or direct samplers,
and is not a computational lower bound. No global novelty claim or independent
admission is made. Q8,r2 and Q4,r3 give boundary product-support counterexamples.
83979 support subcubes,20160 exact phase candidates,853 spectral products and853
Fourier-weight constraints passed; all are reference theorem checks, not hidden
period inputs to the candidate.

## Stronger, costed tests before attempting wave compression

For an exponent cut x=u+2^ell v, a four-corner defect is the XOR of the four modular
outputs f(u,v),f(u',v),f(u,v'),f(u',v'). A rank-one sign wave requires seed dot defect=0.
Finding d independent defects gives a deterministic upper fraction2^(-d) of separable
seeds. On N18446743979220271189,a2,m128,ell64, this run found64 independent defects in
64 rectangles:256 modular powers,4.346339ms construction and3.856470ms exact replay.
Thus only seed0 can be separable across this particular cut. This does NOT say all
such waves require exponential approximate rank or that all representations fail.

For a stronger quantitative observer, the mean Schmidt purity of these seed waves is
exactly the probability that a uniform four-corner defect vanishes. Known degenerate
rectangles have mass d0=1/L+1/H-1/(LH). On nondegenerate rectangles, the fixed16384-
trial SystemRandom test found0 vanishing XORs, using65536 modular powers in1.137518190s.
All raw draws are retained and were replayed exactly in1.047817762s. Under the stated
IID sampling model, the99% upper bound on nondegenerate hit probability is7/16384.
Mean purity is therefore at most approximately0.0004272460937500001.

If F_D is best squared overlap with a rank<=D normalized approximation on this cut,
F_D^2<=D*purity. Markov then bounds the fraction of seeds with F_32>=0.99 by0.01394947.
Thus the outer99%-confidence result excludes such rank32 approximations for at least
98.605% of the seed population, not for any specified seed. This is a restriction on
this ensemble and cut; it is not an order/factoring lower bound.

A supplementary comparison uses cyclic characters exp(2 pi i s f(x)/2^n), which also
represent the correct reduced density without r. The purity defect changes from XOR
to alternating addition modulo2^n. Reusing the recorded rectangles gives0 hits again.
Spending0.005 on each of the two bases gives a simultaneous99% bound excluding rank32,
squared-overlap0.99 carriers for at least98.405% of seeds in EACH tested family.
Two exact cyclic defects already have gcd1 with2^64, excluding rank-one waves for
all nonzero cyclic seeds. A cyclic full-output sampler is not implemented in this stage.

## Executed finite evidence and comparison

Passed:199 exact reduced-density ensembles;199 independent direct-fibre/QFT ensemble
checks;48 whole-wave fixed-point checks;5 complete approximate ensemble laws;118 exact
four-path purity identities;5 deterministic seed-rank witnesses;126 exact binomial-
coverage grids;20 large(521-bit modulus/1042-bit exponent) succinct phase queries;
98 high-precision twiddle checks;70 additional cyclic-purity checks; poisoned order-
routine tests and pre-seed resource refusal. Candidate AST audits exclude float/complex
literals and true division. Reference arrays alone use numpy/mpmath. No Lean/full-project
or independent-researcher validation has occurred.

Whole-law TV against small direct modular-fibre references: N7,a2,m6,2.93467e-7;
N15,a2,m8,0; N21,a2,m8,8.07664e-7; N23,a2,m10,1.13486e-6;
N35,a2,m8,8.85409e-7. All are below the proved uniform bound. These are full mixture
comparisons over every seed, not finite sample histograms.

Frozen benchmark:3 inputs*3 repetitions*2 methods,2 outputs per run,epsilon0.001.
18 complete runs and36 full output samples;one additional128-bit-register preflight
failure. No CPU pinning; serial execution. Median TOTAL milliseconds for two outputs,
order-blind Walsh / previous spectral method INCLUDING its classical order preparation:
N23,a2,m10:16.200389/2.155849; N71,a2,m14:228.150229/2.341872;
N509,a16,m18:5162.963793/3.246140. Every register here satisfies Q>=N^2.
The new method is much slower; its advantage is removing the order prerequisite from
this reference interface, not improving performance. N509 stores262144 output weights
and131072 twiddles, with2359296 butterflies per sample. N64,a2,m128 can evaluate wave
signs and compression certificates but the dense full-output readout refuses its budget.

Counterexamples: resampling a seed per exponent gives the wrong uniform law; selecting
only seed0 gives delta0. At N15,a2,Q256 their TVs are63/64 and3/4. A seed1 rectangle at
exponents0,1,2,3 has signs(-1,1,1,1) and determinant-2. A small one-frequency wave formula
cannot be applied to it. Cheap ensemble entry and cheap coherent readout are different
requirements.

## Reuse and honest research endpoint

T0_BRC action/provenance and P023 observer equivalence are COMPOSE_APPLIED through the
exact reduced-density identity. Finite-character orthogonality is REUSE_APPLIED; stage6
Dyadic is REUSE_EXECUTED unchanged. The new positive four-path observable is an
application-local diagnostic around signed phase waves, not a replacement of those
waves by positive branch masses. HJW ensembles, Hadamard phases, Fourier sampling and
purity/rank/concentration tools are prior art. Bounded source searches do not prove
novelty. Primary references: Hughston-Jozsa-Wootters,PLA183(1993)14-18;
IBM Quantum Learning Quantum query algorithms; Van den Nest arXiv0911.1624.
General black-box Fourier-sampling lower bounds(Aaronson-Chen1612.05903) are not imported
as a lower bound for modular exponentiation.

Next: search for an approximately valid or nonproduct ensemble whose seed law is
available without r AND whose limited amplitude interactions can be contracted
without a dense table. Exact fully product replacements under the proved odd-period
window must be recognized as the original unknown spectral ensemble, not a new entrance. Use the four-path
observer to reject unsuitable low-rank proposals cheaply, retaining all prior successful
readout and negative-witness work. No general classical Shor speedup is established.

## Continuity and delivery

The locally supplied coherent-sampler history728f2cd and the separately published cloud
wavepacket historyc8f0d39 share c0bc60c but differ in stage10. Both are retained as
separate named branches in the cumulative bundle, never silently overwritten or treated
as the same experiment. The cloud bundle's2510b4d... SHA256 was verified from actual
Drive raw bytes. The previous chat stage10 delivery debt is retained until the cumulative bundle
containing its exact history has an actual verified cloud receipt. This note alone
does not establish that upload; the later publication evidence records it. Source
persistence is not mathematical acceptance. New upload hashes and readbacks are external
publication receipts; a bundle cannot include its own future hash. Full code remains on
the user-requested Drive surface; this is a standalone reproducer, not the full EM repo.
