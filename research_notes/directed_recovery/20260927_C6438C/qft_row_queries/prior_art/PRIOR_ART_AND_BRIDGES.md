# Prior art and concrete bridges for native QFT sampling

Status: AUTHOR_LITERATURE_READING_AND_SYMBOLIC_SYNTHESIS / SHARED_CONTEXT /
NOT_ADMITTED. Activity `RA-CAAAC604CB513AEA8BBC1DFC`.
Observed date: 2026-09-27 Asia/Shanghai.

The most useful immediate route is **amplitude-query sampling**, followed by
an explicit search for structure in the amplitude query. Computing every
Gram matrix is not necessary to generate the readout. This principle already
has direct prior art; the project contribution must be stated as a proved
composition with its actual native instrument, not as the first conversion
of quantum sampling into a classical Markov process.

Two concrete mechanisms are developed below: (A) a persistent work label with
two complete-row queries per round; (B) contraction of the ordered native
matrix product with a small, exact target-label branching program. A CT
overlap estimator is a useful diagnostic alternative, and sparse Fourier/MPO
results delimit conditional extensions. None currently proves polynomial
classical Shor simulation for arbitrary inputs.

Throughout, `TV(P,Q)=1/2 sum_x |P(x)-Q(x)|`. Several cited papers call the
unhalved L1 distance total variation; their constants must be converted.
Write `t` for readout width, `D` for internal carrier size, and `L=2^t` for a
Fourier domain. `D=6` is permitted only after the existing full-61 forward and
inverse invariant-subspace certificate. Residual modes are never discarded.

## 1. Primary sources actually read

Only the primary papers below support the scientific claims. The separate
professional database receipt supplied routing metadata, not full-text
evidence. Reading depth is deliberately explicit; neither an abstract nor
this review is an independent verification of an entire paper.

### A. Bravyi, Gosset and Liu: the closest antecedent

[How to simulate quantum measurement without computing marginals](https://arxiv.org/pdf/2112.08499),
PRL 128, 220503 (2022), arXiv v2. Read Algorithm 2, its induction proof,
adaptive-measurement note [28], and supplementary Lemma 1/proof.

For `m` gates, each acting on at most `k` qubits, their exact sampler needs
at most `m 2^k` prefix-amplitude evaluations. It resamples only the active
gate's basis block; monomial gates can update the label deterministically.
The amplitude backend remains part of the cost. Adaptive measured controls
are explicitly allowed. Their approximate construction uses a globally
defined prefix-state approximation `phi_j`, and evaluates the next gate on
that approximation, not arbitrary unrelated approximate numbers. The stated
bound is L1 at most `16 sum_j epsilon_j` for the relevant prefix L2 errors,
thus TV at most `8 sum_j epsilon_j` in this note's convention. This is a
sampling reduction, not an efficient amplitude oracle for general circuits.

### B. Kalachev et al.: implemented block sampling with an amplitude backend

[Pilot-Wave Simulator](https://arxiv.org/pdf/2510.24218v2),
[Quantum 10, 2173 (2026)](https://quantum-journal.org/papers/q-2026-07-23-2173/).
Read Section 2, Algorithm 1, invariant-block proof, and the introduction's
scope/prior-work statements; performance sections were not independently
audited. The paper traces the sampling principle to SEQCSim and BGL, uses
tensor contractions for requested amplitudes, and bounds candidate updates
by an actual invariant block size. Its common-gate case uses at most two
amplitude calls per gate. It explicitly does not improve the complexity of
an individual amplitude contraction. This is particularly close to the
proposed split between our sampler and row-query backend. Its large QAOA
examples do not establish anything about this project's modular arithmetic
or its exact rational word certificates.

### C. Van den Nest: CT access and overlap estimation

[Simulating quantum computers with probabilistic methods](https://arxiv.org/pdf/0911.1624).
Read the CT definition, Section 4 Lemma 3 and Theorem 3 with their proofs.
CT access includes both sampling squared amplitudes and evaluating arbitrary
amplitudes in polynomial time. Theorem 3 estimates overlaps with an
efficiently row/column-computable sparse operator of norm at most one.
Lemma 3 partitions according to which of two squared amplitudes is larger,
obtaining bounded ratio estimators. CT is an access guarantee, not a synonym
for a short state-preparation circuit. Applying a measurement does not, just
by naming the resulting state CT, establish efficient updated access. The
row-level estimator in Section 4 below is a direct project specialization
with a separately displayed proof.

### D. Schwarz and Van den Nest: sparse output is a promise

[Simulating Quantum Circuits with Sparse Output Distributions](https://arxiv.org/pdf/1310.6749).
Read Definition 1, Theorems 1 and 5, Sections 4–6's sparsity/marginal
mechanism, and the discussion of Shor; not every later proof was checked.
For a CT input to a QFT on a selected register, an output distribution with
L1 tail at most `epsilon` outside an unknown `s`-element set admits a
randomized `poly(n,s,1/epsilon,log(1/delta))` reconstruction. It lists
`O(s/epsilon)` outcomes and approximates the distribution to `O(epsilon)`
L1, with failure at most `delta`. Theorem 5 finds heavy Fourier weights
without knowing their locations, in time polynomial in inverse threshold.
Neither result promises a sparse output for general Shor. Also, their
Theorem 1's ideal QFT hypothesis does not automatically include our complete
noncommuting native phase words and residual carrier.

### E. Griffiths–Niu and Browne: terminal QFT and its input burden

[Griffiths and Niu, Semiclassical Fourier Transform](https://arxiv.org/pdf/quant-ph/9511007).
Read the terminal-measurement construction and circuit identity, including
its phase ordering. It preserves the final measurement distribution through
adaptive single-qubit operations; it does not supply a classical description
of an arbitrary entangled input. The project's existing streaming ordering
is consistent with this distinction.

[Browne, Efficient classical simulation of the semi-classical QFT](https://arxiv.org/pdf/quant-ph/0612021).
Read the product-input argument, MPS extension and Shor discussion. A supplied
MPS with polynomial bond dimension permits efficient terminal-QFT simulation;
local measurement does not create the missing entanglement representation.
The input generated by modular exponentiation must itself meet that
representation condition. These papers cannot justify deleting a work-label
sum or replacing a vector-valued residual word by a scalar phase.

### F. Tensor contraction and QFT-MPO compression

[Markov and Shi, Simulating quantum computation by contracting tensor networks](https://arxiv.org/pdf/quant-ph/0511069).
Read the main theorem/representation section and contraction-width statements,
not the complete graph-theoretic proof. For a `g`-gate constant-local-dimension
network with suitable width `w`, the bound is `g^{O(1)} exp(O(w))`.
Constructing or certifying the contraction order is part of the route.
No small width for modular exponentiation follows merely from the small
internal phase carrier.

[Chen, Stoudenmire and White, Quantum Fourier Transform Has Small Entanglement](https://arxiv.org/pdf/2210.08468).
Read Theorem 1, the MPO/application discussion, input-compression cost, and
the definitions and argument in Appendix J; its complete special-function
proof/finite-size assumptions were not independently verified. The core QFT
after removing bit reversal has rapidly decaying operator Schmidt values.
The paper treats both average and worst-case truncation errors, with
`O(n exp(-chi log(chi/3))/sqrt(chi))` scaling for its stated error quantities.
Average normalized Frobenius error is not by itself a worst-input TV bound.
Converting dense length-`L` data to an MPS can still cost `O(L)` even with a
small final bond. Its ideal-QFT MPO is a structural guide here, not an
admitted replacement for actual native words.

### G. Sparse FFT has a different input oracle

[Hassanieh, Indyk, Katabi and Price, Nearly Optimal Sparse Fourier Transform](https://people.csail.mit.edu/haitham/Papers/SFFT_STOC12.pdf).
Read the problem definition, precision caveat, main guarantees and algorithm
interface; the full hashing/filter proof was not independently checked.
With point access to a length-`L` scalar signal and the stated precision
assumptions, the exactly `s`-sparse Fourier case takes `O(s log L)` time;
the general approximation takes `O(s log L log(L/s))`, with constant success
probability and an L2/L2 approximation guarantee. This is not a TV guarantee
without an additional norm argument. Neither efficient modular powers nor a
Gram recursion immediately supplies the required scalar Fourier signal and
sparsity promise. Cost of constructing that oracle cannot be excluded.

## 2. Mechanism A: exact two-arm coupling from complete row queries

This project-specific composition was derived in parallel by the parent and
audit author; I checked the joint-distribution induction. The detailed local
statement is [SINGLE_WALKER_QUERY_REDUCTION.md](../gram_research/SINGLE_WALKER_QUERY_REDUCTION.md).
Its relation to BGL/Pilot-Wave is an antecedent relationship, not a claim that
our expression appears verbatim in those papers.

For a fixed actual measured prefix `h`, let the unnormalized row be
`v_h(w) in R^D`, `M_h=sum_w ||v_h(w)||^2>0`. The existing two-native-H4
certificate gives, for sign `sigma=+1/-1`,

    v_(h,sigma)(z) = (v_h(z) + sigma T_h v_h(P_i^-1 z))/2.

`P_i` is the actual typed permutation with typed inverse, and `T_h` is the
actual complete ordered orthogonal feedback. Preserve that time order;
different `T_h` need not commute. All formulas use raw rows, including their
exact common denominator, so that no square-root normalization is needed.

Maintain one latent label with `Pr(W=w | h)=||v_h(w)||^2/M_h`. Initially
`W=1`. Independently choose a fair coin and set `Z=W` or `Z=P_i W`.
Query the two complete rows and form

    x=v_h(Z), y=T_h v_h(P_i^-1 Z), S=||x||^2+||y||^2,
    Pr(sigma | Z,h) = ||x+sigma y||^2/(2S), W_next=Z.

The proposal has probability `q_h(z)=S(z)/(2M_h)` and a sampled proposal
necessarily has `S>0`. The parallelogram identity makes the two sign
probabilities sum to one. Most importantly,

    q_h(z) Pr(sigma | z,h) = ||v_(h,sigma)(z)||^2/M_h.

Summing over `z` gives the correct readout probability; conditioning on that
readout gives the required invariant for `W_next`. Induction proves the
entire raw readout law and the appropriate conditional work law. No marginal
mass, Gram matrix, rejection of rare histories or refreshed SQ sampler is
required. The latent label is computational bookkeeping, not an extra
physical measurement or a license to treat its one preparation path as the
complete amplitude. Feedback depends on the recorded measured prefix, not
on the private latent trajectory.

**Access and complexity.** Exact sampling uses `2t` top-level complete-row
queries, one application of the relevant actual feedback per round, typed
`P_i/P_i^-1` queries, and exact rational Bernoulli sampling. The total cost is
the sum of those operations and all recursive/query-preprocessing work.
This is TV zero relative to the actual compiled instrument, under ideal
independent classical random bits. It is not a claim about physical random
source quality. If an integer fraction has denominator `b`, uniform integer
rejection below `b` gives fewer than two expected trials of `ceil(log2 b)`
random bits; the denominator bit length remains charged. A seed replay is
only a reproducible test.

The naive row recurrence has two parents per query and can require
exponentially many distinct `(depth,label)` nodes, even for proportional
internal rows. A memo table of `J` rows pays `J D` scalar slots, while a Gram
table of `J_G` matrices pays `J_G D^2`; neither `J` nor `J_G` is currently
uniformly polynomial. A shorter object name does not compress an orbit.

**New local robustness observation (symbolic).** Suppose, at every reachable
`(h,z)`, the approximate queried pair satisfies

    ||(x_tilde,y_tilde)-(x,y)||_2 <= rho_i ||(x,y)||_2, rho_i<1.

Normalizing the pair changes it by at most `2 rho_i` in L2. The orthogonal
two-arm transform followed by sign observation therefore changes the local
Bernoulli law by at most `2 rho_i` in TV. Couple the two processes until their
first disagreement; the proposal kernel from the shared latent label is
identical. Uniform guarantees on the true-reachable pairs give full joint
transcript TV at most `2 sum_i rho_i`. The approximate algorithm must still
define a finite fallback at an off-support or zero approximate pair, such as
an explicit FAILURE outcome or a fixed transition. That case can arise only
after the first disagreement and is included in the same bound. Otherwise
an error path could stall, and a completed-sampler claim would be unjustified.
This does not require normalizing the global state or bounding the
probability of a rare history. It does require a **relative pair-norm
certificate**; unrelated fixed absolute errors on tiny rows do not establish
it. The audit author cross-checked this proposition and its fallback boundary.
No approximate oracle was executed here; the current exact typed route can
avoid this approximation entirely.

## 3. Mechanism B: an exact ordered matrix product times a target predicate

The following is a proved symbolic bridge, cross-checked by the audit author,
not an implemented general small-width construction.

Fix one actual history of length `i`. Let its successive signs be
`sigma_1,...,sigma_i` and ordered feedback matrices be `T_1,...,T_i`.
Expanding only the two-arm algebra gives

    v_h(w) = 2^-i sum over s in {0,1}^i with F_i(s)=w:
                   B_i(s_i) ... B_1(s_1) e0,
    B_j(0)=I, B_j(1)=sigma_j T_j,
    F_i(s)=P_i^{s_i} ... P_1^{s_1}(1).

All denominators are the actual word denominators in these matrices. This
representation retains the complete D-vector; no ideal Fourier factor is
substituted. The ordered weight alone is an exact matrix product with bond
dimension at most D. **The predicate `F_i(s)=w` is the remaining large part.**
Small bond dimension of the weight alone does not give a small contraction.

Assume this exact predicate is supplied as a constructible deterministic
read-once branching program in the same bit order, with at most `B` states
per layer and a known accepting set. Its width, construction and certificate
cost must all be counted. Keep one D-vector `a_{j,q}` at each live state.
Start with e0 at the start state. For each bit transition `q --s--> q'`, add

    a_(j,q') += B_j(s) a_(j-1,q).

Sum accepting-state vectors and multiply by `2^-i`. Every address string
travels one deterministic path, so it contributes exactly once iff accepted.
That proves equality with the row above, including all cancellations and
noncommuting factor order.

With explicit dense matrices the contraction costs `O(i B D^2)` arithmetic
operations and `O(BD)` working scalar slots. With actual native-word action,
the more appropriate bound is `O(B sum_j (C_apply(T_j)+D))`, plus branching
program construction, transitions and exact arithmetic bit cost. Coupling
this oracle with Mechanism A uses at most two such contractions per round;
in a uniform width-B dense model this is `O(t^2 B D^2)` arithmetic work,
plus preprocessing/certification, for one exact readout. Queries may share
verified subcomputations, but the bound does not assume free caching.

No order or factor is an input to this theorem. Nevertheless the obvious
branching program tracks every reachable modular residue and may have
exponential width in `log N`; accepting that program without charging it
would hide the original problem. Likewise, a Jacobi-character color can
give a valid necessary test, but its class generally contains many unequal
residues. Replacing exact equality by such a color requires a separate
proof that every accepted contribution is valid or that omitted differences
are unobservable for the requested quantity. A cheap character by itself
does not supply that proof.

This is a focused tensor-network target: discover and certify a compact
representation of the modular equality predicate *compatible with temporal
matrix order*. It is more specific than compressing the ideal QFT. A
meet-in-the-middle oracle can supply a valid intermediate tradeoff even when
the resulting width/list size remains exponential; report that cost rather
than calling it a polynomial closure.

## 4. CT/SQ collision estimation: useful, but now secondary for sampling

For diagnostic estimation of the conditional branch probability, suppose
we already have efficient exact access to the current complete row and can
independently sample `q(w)=||v_h(w)||^2/M_h`. Generate `z` from the mixture
of `q` and `P_i q`, as above, and evaluate

    X(z) = 2 <v_h(z), T_h v_h(P_i^-1 z)> /
                (||v_h(z)||^2+||v_h(P_i^-1 z)||^2).

Orthogonality gives `|X|<=1` and
`E[X]=c=<v_h,(P_i tensor T_h)v_h>/M_h`.
Thus `p0=(1+c)/2`. Hoeffding gives an explicit sufficient sample count
`m_i >= (1/(2 eta_i^2)) log(2/delta_i)` to estimate `p0` within `eta_i`
with failure at most `delta_i`; clip the estimate to [0,1]. If the oracle
assumptions hold uniformly for all queried histories, sequential coupling
gives transcript TV at most `sum eta_i + sum delta_i`. Equal allocation
`eta_i=epsilon/t, delta_i=delta/t` costs
`O(t^3 epsilon^-2 log(t/delta))` sample/row queries and gives TV at most
`epsilon+delta`, with the per-query native arithmetic separately charged.

This is independent of the number of occupied work rows at the estimator
interface. It is not independent of the cost of constructing SQ access.
Unlike Mechanism A, estimating many independent X values at a fixed prefix
does require fresh conditional row samples. Exact bit generation already
has the stronger persistent-label alternative; do not add Monte Carlo error
merely because the CT result exists. The estimator remains useful for
auditing probabilities or when a separately certified SQ representation is
available.

## 5. What sparse Fourier and low-bond QFT can and cannot add

For an ideal QFT input of the form
`L^-1/2 sum_x |x>|a^x mod N>`, joint computational-basis sampling and
amplitude evaluation are easy given actual modular-power access: sample x,
evaluate its label, and compare. This is compatible with the CT-input
premise. It is **not** a sparse-output premise and is not a CT-access proof
for every measured prefix. On an exactly periodic coset with `r|L`, the
Fourier output is uniform on r locations; any distribution supported on s
locations has TV at least `1-s/r`. This elementary case alone prevents a
uniform small-sparsity inference. For periods not dividing L the exact
finite-window distribution differs; no flatness assertion is substituted.

Even efficient evaluation of a collision predicate such as
`[a^u mod N = a^v mod N]` does not give its sparse Fourier description. Using
the hidden order to define coordinates modulo r, or supplying the support of
the Fourier peaks as input, would assume information the algorithm is meant
to find. Output sparsity, Fourier sparsity of a scalar signal, and low matrix
rank of a correlation kernel are different promises.

For completeness, our norm-to-TV conversion for a scalar sparse-FFT route is
as follows. Let `||a||_2=1`, let its recovered approximation b obey
`||a-b||_2<=rho<1`, and normalize b. Reverse triangle inequality gives
`||a-b/||b||||_2<=2rho`; measurement then gives TV at most `2rho`.
If a sparse Fourier routine gives `rho<=C tau` from a certified L2 tail tau,
the resulting sampler has TV at most `2 C tau` on successful reconstruction.
A failure event of probability delta adds at most delta to unconditional
TV. To achieve small delta one needs a valid confidence amplification or
verification procedure; simply taking a majority of arbitrary recovered
complex vectors is not a proof. This conversion does not establish the
missing scalar-signal access or sparsity for our native residual-valued
instrument. The cited Fourier algorithms also use ideal Fourier arithmetic;
they have not been admitted as actual BRC executions here.

For an MPS/MPO route, a *supplied* compact exact state or tensor network with
a certified small contraction width can implement the row oracle of
Mechanism A. The exact native T_h acts on the internal leg and can be kept
in temporal order. The modular arithmetic/equality tensors must stay in the
network; their width and construction cannot be charged to an unspecified
preprocessing step. A dense state converted to a low-bond MPS after
enumerating its `2^t` entries has already paid exponential input cost.

Approximate MPS/MPO contractions would need an explicit norm certificate
which entails the desired sampling error. Average operator error, a plotted
discarded singular-value curve, and pointwise small amplitudes do not alone
give such a certificate for all Shor inputs or all rare measured prefixes.
The exact native carrier codec is a valid constant-dimensional reduction;
it proves no corresponding small width of the work-label network.

## 6. Continuation and evidence boundaries

The next independent executable research target is the **complete-row
oracle**, not another full readout histogram. Compare the new memoized
recurrence and meet-in-the-middle contraction on the same actual bank,
retaining full row denominators, ordered feedback, typed inverse columns,
and all D coordinates. Count top-level queries separately from expanded
query nodes, base labels, scalar slots and certificate/bit work. A tiny
number of top-level calls is not the total query complexity.

Then attempt the exact branching-program predicate criterion in Section 3
on bounded inputs. Any reduced state partition must establish the requested
equality language or an explicitly weaker but sufficient observation
equivalence. A negative width or query-growth result is useful evidence.

This note contains literature reading and symbolic derivations only. It does
not execute a numerical ideal QFT, replace the native alphabet, certify new
phase approximations, claim a uniform factoring runtime, or supply an
independent admission. Separate actual experiments must keep their own
source/word bindings. Existing Stage95 demand/collision/suffix work and the
published direct-carrier integration remain acknowledged prior project work.

The professional query is documented in `KQB_EXECUTION_NOTE.md`. Its two
accepted jobs returned bounded PARTIAL metadata payloads; the envelope's
FAILED status and the first rejected turn identifier are retained. Official
full-text reading above is separate. Root owns canonical archival and
publication; local files are not yet a canonical archive.

Global-Knowledge-Sync: main@f44ed5959c92e6e088c61c102951d1ab2c5e98d4 /
GLOBAL_KNOWLEDGE_V1. Parent verified the current lease/startup guard; P000
and ACTUAL_TYPED_BRC_ONLY remain unchanged.
