# Fair-bit samplers and computable countable kernels: the converse certificate

2026-10-15 UTC. FIXED LOCAL PAPER APPENDIX / PENDING DISTINCT BOUNDED REVIEW.
This appendix is separate from the already fixed forward sampler certificate.
It is not a Native Result, Task terminal outcome, or new operational admission.

Same Task `RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION`,
publication `TP2-C6F364B0E01C124DB7E9`, Researcher `EM-N-DEA587`, prior own
contribution identity `EM-DVR-F27A61`, and run `RUN-d226418286530d5099e4a5c9`.
Root `EM-DVR-FBF223` supplied the finite-tree total-mass formulation and the
random-access normalization clarification. The current executor developed
the explicit uniformity, type and observation boundaries below. Original
author `EM-NCASDIST1-3F7A91` retains the inherited effective-class theorem.
All old authority holds and the original scientific owner remain unchanged.
Exposure is `DIRECTED_SHARED_CONTEXT_NONBLIND`, not clean-room independence.

## 1. Exact promise and conclusion

Let `S` be one public effective probabilistic program, with finite effective
public input `(N,z)`. Its random resource is an independent fair-bit tape;
all deterministic operations are computable. Every terminating execution
returns a natural number `k`, or an effectively encoded countable finite
output with decidable code equality. Output codes, rather than undecidable
semantic equivalence classes of codes, index the probability distribution.

On a specified input domain `D`, assume that `S(N,z)` halts with probability
one. The domain and this almost-sure termination promise need not be
decidable. No bound on expected time, expected random bits, or convergence
rate is supplied. For each promised input define

`p(N,z,k) = Pr[S(N,z) returns k]`.

**Theorem.** There is a single deterministic public algorithm, uniform in
`(S,N,z,k,n)`, which on every promised input returns a rational `q` such that

`|q - p(N,z,k)| ≤ 2^(-n)`.

The approximation algorithm is guaranteed to halt only on this promise
domain; it does not decide whether an arbitrary probabilistic program is
almost surely terminating. The probability vector is nonnegative and has
total mass exactly one on `D`.

## 2. Finite-tree normalization

Normalize the program so an elementary transition makes at most one fresh
fair-bit request. A normal sequential random tape already has this form.
If the source interface permits computable random access to independent
tape positions, maintain a finite address-to-bit cache. The first query to
a previously unqueried address consumes one new independent fair bit;
repeated queries return its cached value. Adaptive choices of addresses are
permitted. Independence of the not-yet-observed coordinates proves by finite
induction that this normalization has the original query/value joint law.

The cache belongs to the declared state scope. If tape addresses persist
across calls, the cache must persist across those calls too; one may not
erase shared random state and resample it independently. A permitted finite
initial cache is retained. An unavailable infinite preassigned environment,
factor-correlated tape, noncomputable random source, or oracle address
operation is not introduced by this normalization.

For an integer `t≥0`, explore the full binary computation tree for at most
`t` normalized steps and at most `t` fresh-bit queries per path. Deterministic
steps have one successor; a fresh-bit request has two successors, each of
half the parent's mass. A halted path is retained as a leaf and not expanded.
Nonhalting cut-off paths are retained only as residual mass. The finite tree
is computable exactly with rational weights. No simulation of a single
nonhalting branch is allowed to monopolize the construction.

Let `A_t` be the total mass of halted leaves and `L_t(k)` the mass of halted
leaves labelled `k`. Distinct halted leaves represent disjoint cylinders:
halting prevents a shorter successful transcript from also being expanded
into another halting leaf. Thus exact finite summation neither double-counts
overlapping bit prefixes nor assumes a finite output alphabet.

As the two budgets increase, every previously represented halting event
remains represented with the same total cylinder mass. Therefore

`0 ≤ L_t(k) ≤ L_(t+1)(k) ≤ p(N,z,k)`,
`0 ≤ A_t ≤ A_(t+1) ≤ 1`.

Every terminating run uses finitely many steps and fresh queries, so it
appears at some finite budget. The union of these halted-cylinder events
is the entire halting event. Continuity of probability from below and the
almost-sure termination promise give

`lim_t A_t = 1`,  and  `lim_t L_t(k) = p(N,z,k)`.

## 3. A terminating point-probability approximation algorithm

For requested precision `n≥0`, search `t=0,1,2,...` until the decidable
rational test

`1 - A_t ≤ 2^(-n)`                                           (C1)

holds. Return `q=L_t(k)`.

All mass not yet assigned to halted outputs is at most `1-A_t`. Even if it
were all eventually assigned to `k`, it could increase that label's mass
by no more than this quantity. Hence at every stage

`p(N,z,k) ∈ [L_t(k), L_t(k)+1-A_t]`.

At a stage satisfying (C1) the returned rational has the required error.
Because `A_t↑1` on the promise domain, such a finite stage exists. Every
individual finite-tree stage terminates, so the sequential search also
terminates on every promised input. The same search budget works for all
individual labels at that precision, although no finite enumeration of
all possible labels is needed to answer one query.

This proves uniform computability from the sampler code and promised input,
not merely separate computability of each real number `p_k`. No expected-
time assumption appears. The search derives a probability-of-completion
bound as needed; its existence does not imply an inexpensive bound or a
decision algorithm for the almost-sure termination promise.

The promise is essential to this argument. Without it, the cut-off residual
can include permanently nonhalting mass, and the search need not terminate.
In particular, this proof must not be applied to an arbitrary terminating
subdistribution by silently renormalizing its unknown total mass.

## 4. Exact representation equivalence on the declared promise domain

The separate forward certificate proves that a uniformly computable,
nonnegative countable point-probability description with total mass one
can be turned into a public fair-bit exact almost-sure sampler. This
appendix proves the converse under precisely the effective finite-output
and almost-sure termination promises. Composition gives effective changes
of description between:

1. normalized uniformly computable countable probability kernels; and
2. public fair-bit sampler programs promised to halt almost surely,
   with effective countable finite output codes.

Both changes preserve the output probability kernel extensionally. Neither
asserts equality of running time, consumed bit strings, implementation trace,
or an unselected stronger observer. Reconstructing a sampler from its law
need not reproduce the original sample on the same private tape.

For a state-dependent operational use, `z` must still carry the complete
declared conditioning state, including every persistent cache, shared latent
choice and future-relevant residual. Apply the correspondence to the true
conditional kernel given that state and retain the same effective updates.
The forward certificate's joint-law composition proof then applies. If
additional trace data are selected for observation, they must be included
in the effective countable output/state type with the corresponding law;
they cannot be inferred from equality of a smaller marginal.

This statement is narrower than arbitrary continuous distributions, semantic
quotients with undecidable output equality, or completed infinite-limit
observations. Those types are not silently assigned effective natural-number
labels by the theorem.

## 5. What this resolves for the current Source boundary

The inherited machine-readable `G_effect-dist^eff` contract explicitly uses
public effective sampling, an explicit random tape, almost-sure termination,
and finite explicit terminal presentation codes. The current RRBF7 return
retains these hypotheses. For any sampler fitting that fair-bit contract,
computable normalized countable output probabilities follow from the present
proof. Conversely, the forward unit realizes the stated computable kernel
interface. One must therefore not invent an extra need for a supplied tail
rate or expected-time bound when moving between these two descriptions.

The three-source bounded comparison in the forward unit also located only
the assumption and inlining of an existing sampler, rather than either of
these representation-conversion arguments. This appendix is a new explicit
interface result within this local evidence chain, not a literature-priority
claim for a classical computability fact. It does not rerun the inherited
emulator proof or any saved scientific checker.

Task lines 87–89 allow correctly typed stochastic-kernel declarations, and
lines 99–103 still require every licensed mechanism and the relevant
support-bearing terminal behavior to be covered. This appendix removes a
potential description-level obstacle for the exact public fair-bit/countable
interface. It does **not** prove that every licensed operational resource
has that interface. It also does not turn a finite code for a c.e. quotient
into a finite explicit support-bearing matrix: point probabilities of the
code are different from an unavailable completed module-support observer.

The remaining all-resource/terminal-observation inclusion is unchanged.
No admitted escape, objective-specification gap, new singularization mechanism,
efficiency statement, Native mathematical acceptance or parent closure is
asserted. This appendix remains in the same Task and run; Task and parent
are OPEN. This work used paper reasoning and local document/pin handling
only: no finite-tree experiment, random sample, old checker or new scientific
program was executed.

Researcher-ID: EM-N-DEA587 / RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION
