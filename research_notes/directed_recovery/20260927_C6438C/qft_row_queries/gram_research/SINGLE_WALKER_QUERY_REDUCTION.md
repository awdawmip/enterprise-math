# One persistent work label reduces exact readout sampling to row queries

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC. P000 and the actual typed BRC rule
are unchanged. This is a domain-specific composition of the existing native
two-arm instrument, not a new universal BRC family or a claim of first discovery
of amplitude-query sampling. The parent coordinates sources and publication.

## 1. Exact interface and the remaining problem

At prefix h of length i retain the raw, unnormalized complete real row
v_h(w), including all signs and residual coordinates. D=61, or D=6 only
after actual complete-word invariant-subspace admission. Let M_h=sum_w
||v_h(w)||^2>0. The already source-bound two-H4 identity is

    v_(h,sigma)(z) = [v_h(z) + sigma T_h v_h(P_i^-1 z)]/2,

where sigma=+1 for readout 0 and -1 for readout 1. P_i is the actual typed
modular permutation, and T_h is the actual ordered native feedback word.
T_h is orthogonal. Different feedback words need not commute. No hidden
order, factor, ideal QFT matrix, or renormalized amplitude is an input.

The required query interface supplies the entire v_h(w), not a single
preparation-path contribution, with its raw exact denominator. Query cost,
certificate size, exact integer bit lengths, and native gate work are charged.

## 2. Exact persistent-label theorem

Maintain one latent label W with conditional law

    Pr(W=w | h) = ||v_h(w)||^2/M_h.

Initially h is empty and W=1. For each round:

1. Independently draw a fair auxiliary bit C. Set Z=W if C=0 and Z=P_i W
   if C=1, using an actual typed requested column.
2. Query x=v_h(Z), y=T_h v_h(P_i^-1 Z). Write S=||x||^2+||y||^2.
3. Draw sigma with probabilities

       Y_sigma(Z)=||x+sigma y||^2/(2S).

4. Append its readout bit to h and retain the same proposed label W'=Z.

The proposal law is q_h(z)=S(z)/(2M_h), because P_i is bijective and T_h
preserves the full norm. At a proposed label S>0: either x is the nonzero
sampled row or y is an invertible image of it. The parallelogram identity
gives Y_++Y_-=1, so these are actual rational probabilities. Crucially,

    Pr(sigma,Z=z | h) = q_h(z)Y_sigma(z)
      = ||x+sigma y||^2/(4M_h)
      = ||v_(h,sigma)(z)||^2/M_h.                    (1)

Summing (1) over z gives the exact native readout probability. Conditioning
on any positive-probability chosen sigma gives the required new norm law
for W'. This proves the invariant by induction over the complete history.
Sharing the same latent label across rounds is allowed: the induction
conditions on the observed prefix, and each new auxiliary/terminal draw is
fresh. The query oracle is determined by that prefix and its label, not by
an additional selected latent path. Zero-mass outcomes are never chosen.

Thus the complete readout string and terminal work-label marginal are exact
for the actual instrument. W is an auxiliary classical sampler variable,
not a physical trajectory assertion. It neither reveals a hidden order nor
reconstructs a full state. No independent norm sampler must be rebuilt after
a measurement, and no global M_h is needed by the algorithm.

## 3. Random-source and small-denominator accounting

The prototype may reuse the inherited exact rational choose(p,rng) interface:
it compares a uniform integer below p.denominator to p.numerator. Auxiliary
coins consume additional software-random calls, so a shared seed is not a
same-trajectory contract with the old simulator. Seeded pseudorandom tests
exercise execution; exact distributional claims require the usual fresh
conditional-uniform source contract.

For an implementation from unbiased bits, clear x and y to a common positive
dyadic denominator and integer rows X,Y. Then the draw has numerator
A=||X+Y||^2 and denominator Q=2(||X||^2+||Y||^2), with 0<=A<=Q. To draw
uniformly below Q, use k=ceil(log2 Q) bits and reject integers >=Q. Expected
attempts are less than 2 (or exactly 1 at powers of two), independently of
the parent mass and the selected branch probability. A cap of R attempts
fails with probability at most 2^-R per nontrivial draw. Report failure as
an extra outcome; do not silently restart until a preferred history appears.
Over t rounds its failure probability is at most t*2^-R. This bound concerns
random-bit rejection, not the row-query budget, whose failure probability
has no analogous uniform guarantee.

Full signed quadratic observers must compute A and Q from actual rows. The
use of a rational conditional norm observer is inherited; it does not erase
the stored signed state. An exact arithmetic implementation has no division
by the exponentially small global prefix mass. Its rational bit cost is
still charged. Approximate point rows are not covered by this theorem.

If the compiled native instrument is within epsilon TV of its intended
ideal readout law, the exact sampler inherits that same bound. A capped
random-source implementation adds at most t*2^-R on the enlarged output
space. Neither epsilon nor this TV statement is a new ideal-reference run.

## 4. A concrete row-query recurrence and honest resource parameter

For an append-only retained history, memoize (depth,label), with value a
complete D-vector and its raw denominator:

    V_0(w) = e0 if w=1, otherwise 0;
    V_(i+1)(z) = [V_i(z)+sigma_i T_(h[:i]) V_i(P_i^-1 z)]/2.       (2)

All modular inverses/columns use the existing typed lazy permutation proof.
All feedback products use the actual word in temporal order. All signed
sums use the source-bound positive-path/sign-endpoint observer. A zero row
can skip a linear action; no unknown residual is dropped. Append-only history
makes cached earlier queries valid; a fork must bind a different history.

Let J count all distinct memoized row queries actually requested, let L_i
be the length of the i-th full feedback word, and let B bound exact integer
bit lengths. The stored scalar count is J*D, rather than Gram's J_G*D^2.
Each non-base query has two parents, at most one feedback action and D signed
additions. Each sampling round has two top-level row queries plus native
feedback/quadratic observations. A polynomial bound on J, L_i, B and typed
column cost would therefore give a polynomial exact sampler. The theorem
does not supply a polynomial bound on J. Comparing J and J_G requires actual
query accounting; the factor D is not a universal overall speedup.

No complete work-amplitude map is initialized or required by this interface.
Its memo can nevertheless eventually materialize the entire orbit at many
depths. Replacing the name of such a cache is not support compression.

## 5. Why low row rank and simple probabilities do not bound J

Take the inherited first i highest-power multipliers. Their preparation
labels are a^[2^(t-i)j], 0<=j<2^i. For the analysis-only order r, they are
distinct exactly when r/gcd(r,2^(t-i))>=2^i. In this case even a single
depth-i row query expanded naively by (2) produces 2^i distinct depth-zero
labels and 2^(i+1)-1 nodes across its binary recursion tree. Memo equality
alone does not merge these nodes. This is a statement about this explicit
query recursion, not a lower bound on every possible row oracle.

In particular, choose the all-zero readout prefix, so every T_h is identity.
All occupied internal rows are proportional to e0: row rank is one. Yet
the above recursion has the same exponential query tree. Its conditional
bits are fair before collisions, and a structural certificate can bypass
them, but rank alone is insufficient to discover that certificate or to
answer the amplitude query by the naive recursion. All residual coordinates
remain part of the interface even in this special zero-residual countercase.

Likewise |S-S|<=2|S|-1 for a consecutive interval in an exponent group does
not make the difference set bounded independently of |S|. A description of
such an interval is useful only if its image under actual modular powers,
membership, and signed ordered word sums can be queried compactly. No
membership oracle or discrete logarithm is supplied for free.

## 6. A checkable alternate parameter: certified preparation multiplicity

At prefix length i, a row is a signed sum over preparation addresses
e in {0,1}^i with product_j P_j^e_j(1)=w. Its coefficient is 2^-i times
the ordered product of sigma_j^e_j T_j^e_j applied to e0. This product order
retains noncommutation. If an oracle can enumerate all such addresses with
a completeness certificate, using polynomial overhead and at most kappa
addresses per requested label, the row can be obtained with O(i*kappa)
native vector actions, plus the exact signed sums and certificate cost.

The certificate must establish that no address was omitted. Merely finding
one modular preimage does not suffice after collisions. When labels are
collision-free there is at most one address, but recovering it can still
require nontrivial modular-power membership/address work. A short support
description or kappa=1 therefore does not prove an efficient row oracle.
This conditional criterion is compatible with future meet-in-the-middle or
algebraic coloring certificates; it does not use the unknown order as input.

## 7. Relation to estimation and prior work

The same mixture has bounded score
X=2<x,y>/(||x||^2+||y||^2) in [-1,1], with E X=G/M. It permits additive
conditional-probability estimation if row norm sampling and point queries
are already available. Directly sampling Y=(1+X)/2 as in section 2 is
stronger for this native two-arm use: the persistent joint label supplies
the next norm sample automatically, without approximating the expectation.
This removes the particular recursive-SQ-maintenance bottleneck, not the
point-query bottleneck.

The parallel literature audit identifies amplitude-query gate-by-gate
sampling in Bravyi--Gosset--Liu, arXiv:2112.08499 (PRL 128, 220503), and
later pilot-wave simulation. That audit owns the direct source comparison.
This note claims only the explicitly proved specialization (1) for the
source-bound real Kraus branches and all retained native residual coordinates.
It does not claim a new general sampling principle or efficient Shor
dequantization. Current proof, native implementation and bounded execution
must be reported separately.

Global-Knowledge-Sync: main@f44ed5959c92e6e088c61c102951d1ab2c5e98d4 / GLOBAL_KNOWLEDGE_V1
