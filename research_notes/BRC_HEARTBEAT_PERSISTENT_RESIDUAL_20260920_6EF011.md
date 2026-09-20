# Heartbeat World: persistent residuals rather than a zero-residual gate

Event-ID: brc-heartbeat-persistent-residual-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Researcher-ID: EM-DIRECT-6EF011
Status: RESEARCH_CANDIDATE; same-author derivations and tests, no independent review or admission.
Source snapshot: enterprise-math@8880affa44bd655676cde16c48cebabc1aaf9067.
Inherited executable head: 7f6272e (the supplied stage14 bundle).

## User-directed correction and scope

The user explicitly asked us to study imperfections, residuals and apparent
irregularity as potential dynamical structure, and restated the goal of proving
that absolute zero does not exist. The correction changes the research question:
a failed nilpotent closure is not a reason to discard the nonzero residual.
Neither every numerical error nor every irregularity is thereby a physical law.
The absolute-zero statement is retained as a goal to prove, not used as its own
premise. The protected worldview file and P000 are unchanged.

The native six-axis chart, separate time/frame and auxiliary residual typing
come from definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md at the source snapshot.
The newer remote clock/log note at a6f6ba7c1ebfa33b8773fef1b02582c5f3002601 was
also read; it is a distinct stage14 variant, not silently substituted for the
supplied executable history. Its nonnilpotent frontier is consistent with this
continuation. Existing stage14 matrix and X6Clock code is reused unchanged.

## Exact nonzero residual law

Put c=a-1, P_D(t)=sum_(j<D)binom(t,j)c^j and E_D(t)=a^t-P_D(t).
Pascal's identity proves, over the integers and modulo any N,

    E_D(0)=0,
    E_D(t+1)=a E_D(t)+c^D binom(t,D-1).

Thus the omitted part has a causal recurrence even when no positive power of c
vanishes. Its formal generating function is c^D z^D/((1-az)(1-z)^D), with no
analytic convergence assumption. For a2,D6, errors at t6..12 are exactly
1,8,37,130,386,1024,2510. Their structure is not floating-point noise.

An exact feedback realization uses v_j(t)=c^j a^t modN, j0..5. The first five
updates are v_j'=v_j+v_(j+1); the final update is v5'=a v5 rather than v5'=v5.
Its formerly omitted boundary flux is b_t=c v5=c^6 a^t. If J=I+upper_shift,
B=J+c e5 e5^T, so det B=a. In the rotating frame A_t=R^(t+1) B R^(-t), the
six-beat monodromy is B^6. This feedback is not an extra spatial axis and is
not a force/energy claim. A matrix jump costs O(6^3 log t) scalar modular work;
ordinary scalar modular exponentiation is still cheaper.

## Persistent source, temporary cancellation and finite-resolution zero

For gcd(a,N)=1,

    b_(t+1)=a b_t,
    gcd(b_t,N)=gcd(c^6,N).

If c^6 is initially nonzero modulo N it never vanishes. Accumulated E_6 can
nevertheless be zero at particular times. Since Delta^D E_D(t)=c^D a^t,
a unit a and nonzero c^D forbid D+1 consecutive zero residual observations.
For six terms the maximum silent window is six, attained by t0..5.
This is an exact observable-specific temporal law, not a universal thermal law.
Nonunit multiplication2 modulo8 gives2,4,0 and shows why reversibility matters.

The carry process a y_t=N q_t+y_(t+1), for unit radix a>=2 and0<y0<N, gives

    y0/N=sum_(t<T)q_t/a^(t+1)+y_T/(N a^T).

The last term is strictly positive at every finite T. If L is the smallest
integer with a^L>=N, every L consecutive carry digits contain a nonzero digit.
For N18446743979220271189,a2, a512-step run has168 nonzero digits, longest zero
run63, and positive final remainder4140704218633781679. None of this required
computing the period. Positive finite tails may converge to zero and do not
establish a parameter-independent gap.

A residual1 at a huge odd modulus is not necessarily a small wave error:
choosing character s=(N-1)/2 yields phase pi-pi/N. The exact factorization
exp(2pi i s a^t/N)=exp(2pi i s P_D(t)/N)exp(2pi i s E_D(t)/N) retains the coupling.
It is unsafe to delete or independently randomize the second factor merely
because an arithmetic relative-error observer calls it small.

## Separate, conditional cooling theorem

No temperature or energy observable has yet been derived from b_t or the X6
coordinates. Arithmetic nonzero, a nonzero fluctuation, and positive temperature
are different assertions. In standard quantum mechanics a stationary ground
state can have nonzero variances; zero-point variance alone cannot prove T>0.
The stronger user goal is not replaced by a claim that a display cannot show0.

A finite-resource quantum bridge can already be proved. Let system S have dS
levels and ground-space dimension g<dS. Let a finite bath/controller B have dB
levels. Start with full-rank product rhoS tensor rhoB, apply any joint unitary,
and discard B, without selected-outcome postselection or a free pure ancilla.
If muS and muB are the smallest eigenvalues, then

    rhoS' >= dB muS muB I,
    p_exc >= (dS-g)dB muS muB >0.

A sharper bound sorts all joint eigenvalues lambda_i increasingly. For
M=(dS-g)dB,

    p_exc >= sum_(i=1..M)lambda_i >0.

Proof: the pulled-back excited projector has rank M; its eigenbasis diagonal
weights lie in[0,1] and sum to M. The minimum is the sum of the M smallest
eigenvalues, attained by a suitable unrestricted unitary. Additional physical
restrictions can only raise this minimum. For spectra(2/3,1/3) and(3/4,1/4),
the coarse bound is1/6 and the sharp bound is1/4; all24 permutations and128
rational coherent unitaries were checked. This is standard spectral reasoning,
not a new universal third-law theorem.

Only for a diagonal noninverted two-level thermal target with fixed gap Delta
can it be translated as T=Delta/[kB log((1-p_exc)/p_exc)]. An actual physical
Heartbeat bridge must still derive the temperature observable and admissible
resource rules. A pure ground-state ancilla plus SWAP is a counterexample to
dropping the full-rank resource condition; ideal projective postselection is
outside the deterministic scope. Nonexistence of all physically realizable
zero-temperature states is stronger than the proved finite-resource statement.

A separately declared retention model p_(t+1)=q_t p_t+j_t with q_t>0,j_t>=0 has
p_T>=p0 product q_t>0 for every finite T. The exact value(9/10)^1000/3 is positive
although a12-decimal floor is0. This is a rational model demonstration, not an
observed physical heat leak or a derived universal cooling law.

## Executed results and current cost

Exact checks passed:53949 feedback steps;86730 residual recurrences;76110
finite-difference sources;46697 persistent nonzero fluxes;40979 silent-window
checks;486 carry identities and61322 carry-window checks;474 rotating-frame
jumps;784 spectral-bound cases;128 rational coherent-unitary cases;3240
retention checks and input/AST/pure-resource boundaries. No statistical
confidence claim is used by these finite tests. Same author, no Lean or
independent researcher review.

A frozen12-run plan used the genuine hard modulus and t6,64,1024,2^128+17,
three repetitions each. At the largest t, matrix feedback median4.710480ms
versus scalar pow0.013460ms. Both produce the same residue. No speed advantage
is claimed and no hard-modulus Shor sample is produced.

Four small full-law diagnostics use N7/15/23/71 and Q64/256/1024/1024.
Suppressing the residual gives TV approximately0.663106,0.921021,0.904026,0.878972.
Feedback restores the exact modular labels and hence the exact target law;
the reference-array measured difference is0. These bounded dense checks are
not large-register benchmarks or a generic compressed Fourier readout.

## Reuse, prior art and continuation

REUSE_EXECUTED: unchanged stage14 X6Clock/apply and vendor matrix routines
(source blob2b66743c3f4cd52263aa6e15c00d7837008fb8ad).
COMPOSE_APPLIED: BRC action/provenance and observer-bound residual preservation;
positive carry/thermal probabilities remain separate from phase interference.
Native geometry is not identified with an arbitrary physical Hamiltonian.

Primary context: Ticozzi--Viola, Scientific Reports4,5192(2014),
DOI10.1038/srep05192; Wu--Segal--Brumer, Scientific Reports3,1824(2013),
DOI10.1038/srep01824; Masanes--Oppenheim, Nature Communications8,14538(2017),
DOI10.1038/ncomms14538; Freitas et al., arXiv1911.06377. Binomial feedback,
radix expansions and spectral minimization are not claimed globally novel.

Next: a costed phase readout for the coupled jet/residual dynamics, retaining
its correlations. Separately construct the Heartbeat energy/temperature and
cooling-resource bridge before claiming physical nonexistence of absolute zero.
No background executor, mathematical admission or full Shor speedup is implied.

The cumulative bundle preserves the supplied stage14 and earlier main histories
plus cloud-wavepacket. Actual cloud delivery and source-activity publication
are attested only by subsequent external receipts, not by this note itself.
