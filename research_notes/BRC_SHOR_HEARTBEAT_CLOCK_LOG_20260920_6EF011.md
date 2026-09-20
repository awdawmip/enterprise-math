# Heartbeat World–Shor: six-axis residual closure and an implicit large-support sampler

Event-ID: brc-shor-heartbeat-clock-log-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; no independent review, Lean, Working Truth or Foundation admission.
Parent standalone head: f191b42fb22029467f0b2e737068f74460caf2ca.
Heartbeat source: enterprise-math@7e04b0ddda4d90170534ef520179b2e5d3d684a2.

## Actual use of Heartbeat World

The user explicitly proposed applying Heartbeat World at the contraction bottleneck.
We used its signed native-X6 chart, separate time/frame, integer monodromy and finite
residual-group discipline, not merely a six-dimensional drawing. The existing
heartbeat_residual_holonomy.py first203 lines are used unchanged as a pinned source
excerpt (full source blob2b66743c3f4cd52263aa6e15c00d7837008fb8ad). Matrix power,
monodromy, determinant, Smith and torsion routines are executed. The old stage10
CoherentPhaseSampler and stage6 Dyadic numerical engine are also unchanged.

Let C=I+J with J the six-axis lower shift, J^6=0, and let R cycle the six native axes.
The declared macrostep A_t=R^(t+1) C R^(-t) is a native permutation after five ordered
single-axis integer shears. Its six-beat monodromy is C^6, and
z_x=R^x(binom(x,0),...,binom(x,5)). The readout covector rotates with the frame.
Time is not a seventh spatial field; output addresses use the existing zigzag codec.
A periodic six-beat arithmetic program is chosen here, not imposed as a world axiom.
Macrosteps are charged integer computations, not proof of free physical parallelism.

For d=a-1, evaluation w_d=(1,d,...,d^5) has the EXACT defect
  w_d C z - a w_d z = -d^6 z5 mod N.
Thus the six-jet ring (Z/N)[T]/T^6 evaluates to the original modular action iff d^6=0.
This is an observer-compatible ring quotient, not an uncontrolled finite truncation.
The first missing orbit value is at exponent6, with defect d^6. The six coordinates
have increasing bit lengths; low dimension alone is not a complexity argument.

## The phase entrance that actually removes the large-support table

If d^nu=0 for nu<=6 and gcd(N,(nu-1)!)=1, the FINITE modular logarithm
  L=sum_(j=1..nu-1) (-1)^(j+1)d^j/j
and its finite exponential are inverse on the nilpotent ideal. Division is an exact
modular inverse, not a real logarithm. Formal identities modulo total degree nu
prove a^x=a^y iff L(x-y)=0 mod N. The square-zero branch needs no inverses and uses L=d.

The stronger six-beat extension starts from beta=a^6. For gcd(N,6)=1 and an admitted
nilpotent residual d=beta-1, put W=log(beta)/6, u=exp(W), tau=a/u. Then
  tau^6=1, u^6=beta, a=tau*u.
Find h=ord(tau) by testing only the four divisors1,2,3,6. These bounded clock tests
are explicit and are NOT a generic search for the original period. Coprimality of
h and N gives
  a^x=a^y iff h|(x-y) AND N|W(x-y).
Pure a^6=1 is handled directly without inverse6. Other nonunit-clock cases use only
the separately proved direct branch or refuse.

Draw independent j uniform in Z/h and s uniform in Z/N, then freeze
  theta=j/h+sW/N mod1
throughout one full output. Character orthogonality exactly reproduces the original
reduced first-register density, without enumerating its spectral components. The
inherited sampler gives a complete m-bit QFT outcome with per-output numerical TV
at most m*(4/2^b+1/2^p). Each new outcome has fresh phase and readout randomness. The
benchmarks request epsilon1/1000. No rare-parent-mass divisions or difficult-seed
rejection occurs. The scope is uniform exponent input, unit a, ideal QFT, corrected
numeric bit labels and an UNCONDITIONED second register, not arbitrary joint operations.

This is an exact spectral entrance for a STRUCTURED EASY family: its original period
can also be obtained as h*N/gcd(N,W), and gcd(N,L)=gcd(N,d) on the direct branch. We do
not compute that period in the production sampler, but do not claim to have bypassed
generic order complexity. It is consistent with the earlier product-wave rigidity:
this parameterization produces exactly the original spectral grid.

An additional native residue-state implementation constructs
  zbar_x=tau^x R^x(binom(x,0),...,binom(x,5)) mod N,
with covector for d'=u-1. Its one-beat map is tau*A_t mod N; its six-beat map is C^6.
It reads the ORIGINAL a^x exactly, including at huge time indices. This is a modular
quotient representative, not recovery of the entire unbounded raw-world coordinate.
Future raw-coordinate access would require retained carry information.

## Executed large-support outputs and honest cost

The direct-jet plan and later clock-extension plan are separately frozen. Together:
69 candidate runs,51 successful batches,204 complete outputs,18 explicit refusals;
69 additional structure-aware classical comparator runs. All run serially with GC,
three repeats per case and no CPU pinning. Candidate arithmetic is integer/Fraction.
The comparator uses the SAME admissibility certificate, a gcd-derived period, and the
SAME inherited phase sampler. It too is polynomial on these families.

Clock-extension medians (milliseconds), four complete outputs per run:
- N49,a2,m12: total4.680003, comparator2.125708; clock3, period21.
- N7^6,a2,m34: total7.665658, comparator8.467388; clock3, period50421.
- N1000003^6,a=N-1000004,m240: admission0.050016, native setup1.144978,
  phase setup1.084517, four-output readout59.810318, total62.108045;
  comparator90.810358. Period2000030000180000540000810000486 is POST-RUN evidence.
- Same120-bit N with a constructed three-cycle times(1+1000003),m240:
  total64.520416, comparator35.538000; post-run period3000045000270000810001215000729.
- N(2^61-1)^6,a=N-2^61,m732 (366-bit modulus): total313.274562,
  comparator223.475741. This is a deliberately structured prime-power input,
  NOT a366-bit hard factorization achievement.

The240-bit readout uses23 root intervals at280-bit internal precision; its deterministic
single-law TV bound is15/32768 (<0.001). It has zero statevector/explicit-peak entries
and no generic order call. Scalar phase coordinates encode on the order of10^30 modes
without listing them. The original period is easy in this class; timings do not establish
an asymptotic advantage over the appropriate classical algebraic baseline.

## Genuine hard-input failure and next arithmetic barrier

For the previous N18446743979220271189,a2,m128, beta64 gives d63 and
  d^6=62523502209 !=0 mod N, gcd(d,N)=1.
The clock bridge refuses before RNG or phase setup (median0.023004ms total). Since d
is a unit, NO positive power can vanish: increasing the finite-jet depth cannot fix
this selected representation. This is not a lower bound for all Heartbeat descriptions
or all factoring algorithms. A squarefree N has no nonzero nilpotents, so this family
there only handles a^6=1, not a generic large-order base.

The next missing unit is a genuinely nonnilpotent, reversible residual/semisimple
cycle with an affordable dual readout. A finite-dimensional monodromy description by
itself is not enough: even ordinary a^(x+1)=a*a^x is already a one-variable recurrence.
Preserve the positive bounded-clock/nilpotent adapter; do not mistake it for a solution
of the remaining hard-input contraction.

## Wrong collapses checked

Equal branch count does not identify residue groups: the existing radix heartbeat at
12 binary beats has (Z/4)^6, whereas a4096-point Shor QFT uses Z/4096. The former has64
classes killed by2 and the latter only2. A six-axis carry matrix with columns
B_i e_i-e_(i+1) and final B5 e5 instead has Smith factors(1,1,1,1,1,prod B_i).
Our sampler retains the original cyclic Fourier modulus, not six independent digit QFTs.

For N49,a2,Q1024, erasing the three-state clock changes the measured law by TV0.6634005.
Ignoring the rotating readout frame changes an exact example from8 to7. Unjustified
six-term truncations have measured TV0.6631 at N7 and0.8414 at N23. None is made safe
by an appeal to microscopic ambiguity or uncomputed paths.

## Validation and sources

Passed322224 exact coherence-pair checks across the direct and clock branches,
12240 jet/modpow checks,2448 ring-quotient products,101 exact formal log/exp/binomial
identities, six monodromy intertwiners,390 original-base native residue steps,24 huge-time
native readouts, and9 whole small-output laws against separate modular-fibre FFT references.
Whole-law errors are below the inherited numerical bounds. Generic order routines were
poisoned in both adapters; resource/refusal/AST/carry/frame checks also passed.
All138 candidate/comparator records were postchecked. Initial negative test N27,a4
was incorrect (depth3 only needs inverse2); the fixture was corrected to N81,a4, and
its original failure log is retained. No production rule was weakened to satisfy it.
Same author throughout; no independent research review, full-project tests or Lean.

The nilpotent logarithm, Fourier character identities and normalizer-style simulation
have classical antecedents. Primary context includes official Sage p-adic logarithm
documentation, Mathlib.RingTheory.Nilpotent.Exp (background only; not a finite-ring
Lean proof), and Van den Nest arXiv1201.4867. No global novelty or new top-level BRC
family is asserted. P000 and the Heartbeat World definition remain unchanged.

Full derivations, code, raw runs and all prior histories are in the cumulative standalone
bundle. This note is durable research evidence, not mathematical admission. The complete
bundle will be delivered to the user-requested Drive folder; future upload hashes are
recorded separately rather than fabricated in this note.
