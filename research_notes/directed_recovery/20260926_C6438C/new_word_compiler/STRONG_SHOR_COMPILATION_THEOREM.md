# Variable native words: uniform requested-accuracy Shor simulation

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED.
EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.

This theorem describes a new algorithm whose primitive alphabet and complete
61-mode carrier stay fixed while finite word length varies. It does not change
or retroactively strengthen the published fixed K33 implementation. Its runtime
uses only complete actual H4/sign/swap words, certified modular permutations,
the inherited terminal instrument and exact quadratic software readout. An
algebraic target observer is a compiler certificate, never a state propagator.

## 1. Effective compilation hypothesis and its discharge

For every integer m>=2 and rational delta>0, the compiler must return a finite
determinant-positive actual word W_m together with a replayable complete-carrier
certificate

    ||W_m - (R(-2*pi/2^m) direct_sum I_59)||_op < delta.

The target is defined algebraically: r_2=1 and r_m is the unique positive root
of r_(m-1)*x^2+2*x-r_(m-1)=0. Its two-plane entries are the symbolic rational
functions c=(1-r_m^2)/(1+r_m^2), s=2r_m/(1+r_m^2). The inverse phase block is
[[c,s],[-s,c]]. No trigonometric or ideal-matrix propagation is required.

`FIXED_ALPHABET_DENSITY.md` proves that the fixed native alphabet is dense in
SO(61). Its primitive identities are separately bound by
`NATIVE_REFLECTION_PAIR_CERTIFICATE.json.gz`. Enumerate all finite words and
refine sound algebraic target intervals by a fair dovetail. For a strict
Frobenius approximation better than delta, a sufficiently fine interval
eventually certifies its strict squared error bound. Density supplies such a
word; every finite pair of word and interval depth is eventually visited.
Thus the unbounded algorithm terminates. A bounded invocation may correctly
return PARTIAL with a continuation cursor; it has not disproved existence.

`EFFECTIVE_COMPILER_CLOSURE.md` specifies the error observer and termination
argument in detail. The actual implementation and bounded execution evidence
are separate artifacts: this theorem alone is not a report of their execution.
Increasing a proof interval's resolution is an explicit observer parameter.
It changes neither old target32/vector64 records nor any native gate weight.
The target is fixed before search and independent of measured outputs.

## 2. A global error budget covering every mode and gate occurrence

Let t>=2 be even and let 0<epsilon<=1 be rational. The inverse-QFT phase of
index m occurs t-m+1 times, for m=2,...,t. Set

    M = t*(t-1)/2,
    delta = epsilon/M.

Compile each required m to strict operator error below delta. Exact quarter
turns can use zero error. A more economical allocation may use individual
positive deltas satisfying sum_m (t-m+1)*delta_m <= epsilon; it is not needed
for termination. No phase is replaced by an uncontrolled fixed tail unless
that replacement itself passes the requested full-carrier certificate.

For a controlled direct sum, the norm of the difference is exactly the norm
on the controlled block. Tensoring identity spectators or work registers
does not change that norm. Every native and comparison factor is orthogonal
(unitary after complexification), so the telescoping product identity gives

    ||U_actual - U_ideal||_op <= sum_occurrences delta_m <= epsilon.

This estimate holds on arbitrary residual-bearing input, including all 59
complement modes. It does not assume that the actual circuit remains in the
principal two-plane. Complete-carrier error certification is essential here.

For normalized initial states, state-vector distance is at most epsilon.
Pure-state trace distance is at most this vector distance, and any common
measurement or deterministic postprocessing contracts it. Therefore

    TV(P_actual, P_ideal) <= epsilon

for the entire terminal classical joint distribution of the augmented
realified comparison circuit, hence also for its raw control readout and any
fixed CF/gcd output map. After summing the retained internal labels, that ideal
control marginal is the standard Shor law. Extra internal labels are not
claimed to be extra ordinary Shor outputs. The ideal object is used only in
this proof; it is never executed to generate an actual sample.

The inherited full-control/streaming equivalence is algebraic for arbitrary
complete orthogonal phase maps with controls on retained labels. Terminal
measurements can be deferred through subsequent classically controlled maps;
the H4 spectator returns by the existing even-round invariant. Consequently
the same bound holds for the streaming implementation, without a sqrt
normalization, mode reset, or deletion of signed residuals.

## 3. Uniformity and why fixed-cutoff obstruction does not apply

Word selection depends only on (m,delta), not on N, the modular order, a hidden
factor, the selected base or a desired successful history. Thus the bound is
uniform over all legal bases at the same t and epsilon. Only finitely many
words are required for each finite call. Compilation is finite by Section 1;
work-state and native-word execution are finite at each fixed input.

The K33 obstruction at Source 28b3f7d3f98904781fe371f6c51bfb5b6974352e used
a width-independent finite family of actual phase products. Here increasingly
accurate words can have increasing length. A finite generating alphabet is
not a finite set of its words. The strictly positive contraction minimum in
that obstruction need not be uniform over the new word family.

This gives requested accuracy for every finite width. It does not assert a
single finite bank works at all widths, nor an efficient classical algorithm.

## 4. Original CF factor success with an inverse-polynomial attempt bound

For a composite N having at least two distinct odd prime factors, take
n=ceil(log2 N), t=2n and epsilon=1/(16n). Use the existing random-base policy
uniform on {2,...,N-2}, its gcd precheck, and its original CF postprocessor.
The proof at Source 1fb7ff99d205f9ca03772942be64f732553dcd86,
`completion/SUCCESS_AND_COMPLETION_THEOREM.md`, establishes ideal single-attempt
success at least 1/(8n): a good base has at least phi(r)/(4r)>=1/(4n) useful
mass, and good units plus immediate nonunit gcd successes supply the factor
one half. This is a bound for the existing CF policy, without added multiples.

The uniform terminal TV bound therefore gives

    P_actual(success in one attempt | previous failures) >= 1/(16n).

The condition requires fresh conditionally uniform base and readout randomness.
Specified test seeds or base lists demonstrate deterministic executions; they
do not establish this stochastic premise. The unknown order and useful ideal
readouts remain proof quantities, not compiler or sampler inputs.

For integer s>=1, take R=16*n*s attempts and stop on a verified factor. Each
block of 16n attempts fails with probability at most one half, so total retry
failure is at most 2^-s. This assertion is uniform in finite n and avoids the
astronomically small dyadic support bound needed for fixed K33.

For full recursive factorization, use the already implemented exact even,
perfect-power and prime certificates, product invariant and unresolved-leaf
accounting. Let n0 be the original input bit length and allocate
b=s+ceil(log2 n0) to each stochastic split node. Fewer than n0 such nodes can
occur. R_v=16*n_v*b at each node gives a union bound at most 2^-s for any retry
failure leaf, even when subsequent nodes depend on earlier successful splits.
All reported factors are verified independently of random assumptions.

Compilation and external-random-source interruptions are distinct from retry
failure and must remain explicit PARTIAL outputs. Exact unbiased rejection
sampling terminates almost surely, not with a deterministic fixed number of
random bits. No conditional deletion of interrupted outcomes is permitted.

## 5. Complete transcript accuracy needs its own budget

An attempt's terminal TV epsilon does not imply the same error for a record
containing arbitrarily many attempts. If conditional kernels at attempt j
are uniformly within epsilon_j at every matching history, the usual sequential
coupling gives transcript TV <= sum_j epsilon_j, capped at one. An independently
requested full-record accuracy eta therefore needs a total allocation, for
example epsilon_j<=eta/R for a fixed R, or a summable geometric allocation
when the number of attempted nodes is not fixed. Failure probability 2^-s is
not a transcript-TV claim.

## 6. Costs and exact closure scope

The compiler enumerates an exponentially branching word language and is only
a computable baseline. Density proves finite termination at each rational
tolerance but supplies no practical bound here. Actual word denominators and
certificate sizes grow with composition; work amplitudes may occupy order N
labels, and the current Wilson prime baseline has linear-in-N modular work.
Inverse-polynomial retry count does not make these costs polynomial in n.

The resulting mathematical algorithm is an all-finite-input, requested-accuracy
simulation under the declared BRC linear and quadratic-observer interface.
It is not an efficient classical factorization theorem, a derivation of the
physical Born rule, or an autonomous six-space-axis wiring construction.
No independent admission follows from author proof or artifact persistence.
The 61 carrier modes are computational labels; P000 remains unchanged.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
