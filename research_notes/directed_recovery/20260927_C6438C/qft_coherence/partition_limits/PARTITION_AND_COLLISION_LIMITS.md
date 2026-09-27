# What preparation samples can and cannot certify cheaply

Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC.
Current project source supplied by the coordinating author:
`e8c5726a22d78c8d3623611afd33f4fe76b46321`.
Canonical global-knowledge lease, checked by the coordinating author:
`f44ed5959c92e6e088c61c102951d1ab2c5e98d4`.

This is new symbolic work. No new numerical propagation, ideal-reference
execution, factor/order query, or scientific arithmetic experiment is claimed.
The prepared-label law and complete native instrument are the existing ones.
All stated black-box lower bounds explicitly restrict the information supplied
to an algorithm; they are not lower bounds for arithmetic Shor simulation.

## 1. The certificate under investigation

At depth i the exact raw history fields satisfy

    mu(z) = sum_h ||v_h(z)||^2,             sum_z mu(z)=1.

The next work permutation is P. The other arm applies the actual full
orthogonal feedback T_h, in its original order. Define

    nu(z)=mu(P^-1 z),
    L=sum_(h,z) |<v_h(z), T_h v_h(P^-1 z)>|,
    F(mu,nu)=sum_z sqrt(mu(z)nu(z)).

For any fixed work-label partition C with cells B, put

    p_B=mu(B),       q_B=nu(B),       F_C=sum_B sqrt(p_B q_B).

Cauchy--Schwarz first over histories and then over labels in a cell gives

    L <= F(mu,nu) <= F_C <= 1.                              (1)

Consequently replacing the local bit score by a fresh fair bit at every
history of this layer has exact-reference averaged joint-kernel cost L/2,
bounded by F_C/2. Across declared replaced layers the costs add by the
already established reference-kernel argument. This is a *joint* bound,
including the next latent label; it is not merely a final-bit marginal bound.

Both p and q can be sampled from independent preparation walks: obtain W
from mu and evaluate the cell of W or P W. However, this does not imply that
a useful partition can be discovered or its small fidelity certified cheaply.
Equation (1) uses full internal norms and permits noncommuting T_h; none of
the arguments below discards residual coordinates or replaces native phases.

Dependencies read in this round:

- `sep27-qft-approx/README.md`;
- `sep27-qft-approx/observer_contracts/PROJECTIVE_AND_COHERENCE_BOUNDS.md`;
- `sep27-qft-approx/structured_approx/WORK_MARGINAL_PRUNING_AND_BARRIER.md`.

## 2. A distribution-free sample lower bound, even with known pairing

The oracle model is deliberately precise. The algorithm knows a finite label
carrier and the entire permutation P, may evaluate P and P^-1 at arbitrary
labels, and receives at most m independent samples from an unknown mu. It
has arbitrary computation and private randomness. It receives no membership,
point-probability, amplitude, hidden-support description, or other input
correlated with the unknown choice below. Samples from nu give no extra kind
of information: applying known P^-1 turns each into one mu sample. Every
such independent draw counts toward m.

Let s be positive and even. Labels are pairs (j,b), j in {1,...,s}, b in
{0,1}, and P(j,b)=(j,1-b). Consider these two priors on *uniform s-point*
distributions; thus even the exact support size and flatness are supplied:

- D0: independently choose fair hidden signs xi_j; mu is uniform on the s
  labels (j,xi_j). Its support and its P image are disjoint, so F=0.
- D1: choose a uniform subset I of s/2 pair indices; mu is uniform on all
  (j,0),(j,1) for j in I. This support is P-invariant, so F=1.

Let E be the event that the m observed pair indices j are all distinct.
Conditional on E, the complete ordered transcript has the same law under
both priors: the indices are a uniform ordered distinct tuple from s indices,
and their observed bits are independent fair bits. The hidden signs in D0
have not previously been exposed; averaging the random subset I in D1 gives
the same distinct-index tuple distribution.

Under D0 the index samples have support s; under D1 they have support s/2.
Their collision probabilities therefore satisfy

    Pr_D0(E^c) <= binom(m,2)/s,
    Pr_D1(E^c) <= binom(m,2)/(s/2)=m(m-1)/s.

Two laws with a common conditional distribution on E have total variation
at most the larger probability of E^c: decompose each into its E and E^c
parts and use the triangle inequality. Hence

    TV(transcript_D0, transcript_D1) <= min(1,m(m-1)/s).      (2)

Arbitrary adaptive queries of known P and arbitrary postprocessing cannot
increase this distance. An adaptive sample budget bounded by m can be padded
with unused draws, so (2) still applies.

Suppose a procedure emits an upper certificate F<beta, for any fixed beta<1,
with false-acceptance probability at most alpha on *every* D1 instance, and
emits it with probability at least rho averaged over D0. Then

    rho-alpha <= m(m-1)/s.                                 (3)

In particular, rho>=1-alpha with alpha<1/2 requires
m(m-1)>=(1-2alpha)s. Reliable distribution-free discovery of this separation
therefore costs Omega(sqrt(s)) samples. This lower bound already allows
unbounded computation, exact known P, adaptive partition selection and the
flatness/support-size promise. It is not just a failure of one estimator.

The family is an opaque-label information model. It is **not** asserted to be
the reverse-square modular preparation family for an efficiently described
N,a. An arithmetic character, an explicit circuit description, or a public
number-theoretic witness may reveal information absent from this oracle.
Equation (2) must not be imported as a lower bound for algorithms using that
additional structure, or as a cryptographic hardness claim.

## 3. Learning a small partition can cost more than detecting separation

Stay in D0, where the fine-label fidelity is exactly zero. Allow a partition
C into at most K cells to be chosen using the entire m-sample training
transcript and private randomness. No independence of C from those training
samples is assumed. Condition on that transcript and randomness. Let V be
the set of observed pair indices and v=|V|<=m. The unseen orientations remain
independent fair signs; C is now a fixed function of all labels independent
of those unseen signs.

For a cell B let d_B=p_B-q_B. Its contribution from pair j is 1/s times a
signed vector which has one +1 and one -1 at the cells of its two endpoints,
or is zero when those endpoints share a cell. Write d=d_seen+d_unseen.
The seen contribution satisfies ||d_seen||_1<=2v/s. Every unseen pair has
mean-zero contribution, independent of other unseen pairs, with squared
Euclidean norm at most 2/s^2. Therefore

    E ||d_unseen||_2^2 <= 2(s-v)/s^2,
    E ||d_unseen||_1 <= sqrt(2K(s-v))/s.

As sqrt(p_B q_B)>=min(p_B,q_B), F_C>=1-TV(p,q). It follows that

    E F_C >= 1-v/s-sqrt(K(s-v)/(2s^2))
          >= 1-m/s-sqrt(K/(2s)).                           (4)

This expectation includes the random hidden distribution and training. More
explicitly, Markov's inequality on TV(p,q) yields, for beta<1,

    Pr[F_C<=beta] <= min(1,(m/s+sqrt(K/(2s)))/(1-beta)).     (5)

Thus if m=o(s) and K=o(s), a partition learned from these samples has
fidelity tending to one in probability, although the true fine-label fidelity
is zero on *every* instance. To obtain a constant chance of a constant-below-one
partition bound, the displayed necessary tradeoff forces m of order s or K
of order s, up to constants. It does not claim these costs are sufficient.

There is no contradiction with the birthday-scale bound (2). Detecting that
two opaque supports do not overlap can be cheaper than learning a small
function that separates them. If all xi_j were independently supplied, the
two-cell partition c(j,b)=b xor xi_j would certify F_C=0 immediately, but its
s-bit definition and discovery cannot be treated as free.

These inequalities also explain why an arbitrary small hash partition can
be uninformative: it merges opposite support mass. They do not constrain an
algebraically specified low-cost character which correctly encodes the
unseen orientations by a theorem rather than by training samples.

## 4. A collision certificate that avoids learning a partition

There is a conditional improvement matching the square-root lower bound for
constant accuracy. Suppose an **independent proof or input promise** says
mu is uniform on an unknown set S of exactly s labels. Let P be any known
permutation, not necessarily the pair flip. Then

    F=|S intersection P S|/s,
    C=Pr[X=P Y]=|S intersection P S|/s^2=F/s                (6)

for independent X,Y from mu.

For m>=2 iid samples define the symmetric kernel

    h(x,y)=(1[x=P y]+1[y=P x])/2,
    U=binom(m,2)^-1 sum_(j<k) h(X_j,X_k).

The diagonal j=k is excluded. E U=C, so Fhat=sU is unbiased. Put
g(x)=E_Y h(x,Y)=[mu(P x)+mu(P^-1 x)]/2. On S, 0<=g(x)<=1/s,
E g=C, and therefore Var g<=F/s^2. Also 0<=h<=1 gives Var h<=C.

Expanding the covariance of the unordered-pair sum, disjoint pairs have
zero covariance and pairs sharing one index have covariance Var g. Hence

    Var U = 2 Var h/[m(m-1)]
          + 4(m-2) Var g/[m(m-1)],
    Var(Fhat) <= 2sF/[m(m-1)] + 4F/m.                     (7)

The equality for Var U follows just by counting: there are binom(m,2)
diagonal terms and 6 binom(m,3) ordered pairs sharing an index in the variance
of the sum. No asymptotic normal or Poisson approximation is used.

If F>=epsilon>0, Chebyshev applied to the event U=0 gives

    Pr[U=0] <= 2s/[m(m-1)epsilon] + 4/(m epsilon).          (8)

Take any integer m>=2 satisfying

    m^2 >= 16s/epsilon,       m >= 16/epsilon.

Since m(m-1)>=m^2/2, (8) is at most 1/2. In B independent predeclared
batches, accept the upper certificate F<epsilon only if every batch has
zero directed P collision. The false-acceptance probability for F>=epsilon
is at most 2^-B. For F=0, all batches pass with probability one. A sufficient
sample budget is

    O((sqrt(s/epsilon)+1/epsilon) log(1/alpha)),             (9)

using a predetermined B with 2^-B<=alpha. No numerical logarithm or square
root is needed to validate the integer budget inequalities.

The statistic does not require m^2 modular-permutation evaluations. Given
label frequencies f, its directed-pair numerator is

    sum_y f(y) f(P y) - sum_j 1[X_j=P X_j].

The subtraction removes self-pairs at fixed points. It can be evaluated
using at most m calls to P and an exact dictionary or sorting pass; for a
zero-collision test, scanning pairs through the dictionary suffices. Every
label-generation call, permutation call, exact comparison and count remains
charged. The variance analysis accounts for the correlations between sample
pairs; pretending there are m(m-1) independent observations would be wrong.

For the bounded-error task F=0 versus F>=a positive constant, (9) has
birthday-scale sqrt(s) samples, matching (2) up to confidence factors. It
can thus improve on learning an explicit separating partition in the model
of (4). It still becomes exponential when s grows exponentially in the
input bit width. No such collision algorithm has been executed in this unit.

## 5. Flatness is a real premise, not something zero collisions prove

For a general mu the collision probability is
C=sum_z mu(z)nu(z), whereas F=sum_z sqrt(mu(z)nu(z)). A known overlap-support
bound K gives only F<=sqrt(K C) by Cauchy--Schwarz. In particular F=sC is
false without the flatness promise, even on a known two-element support:
for P swapping the labels and mu=(1-delta,delta),

    C=2delta(1-delta),       F=2sqrt(delta(1-delta))=sqrt(2C).

Absence of observed collisions does not establish a uniform distribution or
justify substituting (6). In an actual depth-i preparation walk there are
2^i equally likely addresses, but labels can have different address counts.
Its nonzero masses are multiples of 2^-i. This alone gives the valid but
weaker deterministic relation F<=2^i C: whenever mu(z)nu(z)>0 its square root
is at least 2^-i, so sqrt(mu(z)nu(z))<=2^i mu(z)nu(z).

Uniformity with s=2^i follows if address-to-label injectivity has separately
been certified. Proving that injectivity by enumerating all addresses would
erase the claimed setup saving. If a public arithmetic witness proves it,
one must also compare against direct separation/character consequences of
that same witness, rather than unnecessarily running a collision estimator.

## 6. Marginal fidelity does not determine the actual sampler error

For a fully dyadic local counterexample use four labels, P=(1 2)(3 4),
T=I, and one normalized field with each row norm 1/2. All four label masses
are 1/4, so mu=nu and F=1.

- Set all rows to e0/2. Each two-arm pair is aligned, L=1, and replacing the
  deterministic plus bit with a fair bit changes the joint law by 1/2.
- Set rows at labels 1,3 to e0/2 and rows at 2,4 to e2/2. Here e2 is a
  retained residual coordinate of the full D>=3 carrier. Each paired inner
  product is zero, L=0, and the fair replacement is exact.

Both have the same mu, P and every partition fidelity. This is a local
native-carrier counterexample with exact dyadic coordinates, not a claim
that the standard modular work-1 program reaches either field. It shows
that a failure to certify small F does not prove large actual coherence or
large TV. Conversely, the first field shows why a distribution-free fair
replacement cannot simply ignore the absence of a certificate.

Likewise, a coarse F_C close to one can mean only that the partition merged
disjoint labels: the D0 family has F=0 yet obeys (4). These are three distinct
notions: partition-bound failure, fine-fidelity certification cost, and actual
sampling error. None is a general classical simulation lower bound.

## 7. A sharper obstruction inside the actual Shor preparation family

Unlike the opaque-label model, the following calculation applies directly to
the standard reverse-square work schedule. It uses the unknown order only
as an analysis variable; no order is passed to any algorithm or oracle.
Let ord_N(a)=r=2^s q with q odd, and index the next round by i=0,...,t-1.
At depth i, after i preparation choices, put L=2^i and e=t-i-1. The parent
preparation label is

    a^[2^(e+1) K] mod N,       K uniform on {0,...,L-1},

and the next multiplier is a^(2^e). Suppose e>=s, so this next step still
precedes the final s rounds. Both multipliers generate the same odd-order
subgroup H of size q. In coordinates b=a^(2^(e+1)), the next multiplier is
b^j with j=(q+1)/2 modulo q, because 2j=1 modulo q.

Write L=vq+u with 0<=u<q. In these q coordinates, mu assigns (v+1)/L to
I={0,...,u-1} and v/L to its complement. If U is uniform on H, the exact
distance is

    TV(mu,U) = u(q-u)/(qL) <= q/(4L).                      (10)

Since P preserves U, the triangle inequality already gives
TV(mu,P_*mu)<=q/(2L). Here the particular shift j permits an exact answer.
As q is odd, an interval of length at most (q-1)/2 and its translate by
(q+1)/2 are disjoint. Apply this either to I or to its complement. Hence,
with d=min(u,q-u),

    |I symmetric_difference (I+j)|=2d,
    TV(mu,P_*mu)=d/L <= (q-1)/(2L).                        (11)

There are exactly d mismatched coordinates of each orientation. The
Hellinger identity 1-F=(1/2)sum_z(sqrt(mu(z))-sqrt(nu(z)))^2 therefore gives

    F(mu,P_*mu) = 1-(d/L)(sqrt(v+1)-sqrt(v))^2.             (12)

For q=1, u=d=0 and F=1, as the preparation label and P are both trivial in
this subgroup. For q>1, formula (12) also covers v=0; if L<=q/2 it gives
F=0, the early no-collision regime. In the opposite regime L>=q, v>=1 and

    1-F = d/[L(sqrt(v+1)+sqrt(v))^2]
        <= d/(4vL) <= q/(8vL) = O(q^2/L^2).               (13)

These square roots are symbolic analysis, not a newly permitted primitive
evaluator. The weaker rational consequence F>=1-q/(2L) follows from (11)
and is sufficient for the obstruction.

Every partition satisfies F_C>=F. Thus when the preparation interval is
long compared with q, **even knowing the exact marginal** cannot make this
norm-only partition certificate give a small per-layer error allowance:
its bound F_C/2 is near 1/2 for all partitions. Better sampling, more colors
or an exact marginal table cannot remove this loss. A substantially sharper
certificate in this region must use actual signed/internal coherence or
other information beyond these two unconditional label marginals.

For example, with n=ceil(log2 N), default t=2n, and i=n+k while e>=s,
q<2^(n-s) implies the conservative bound

    F_C >= F > 1-2^(-s-k-1).

This is a directly relevant range of the actual schedule, not an arbitrary
opaque distribution. It still gives no lower bound on actual L, readout TV,
factoring probability or the cost of an algorithm using a stronger invariant.

For the final rounds e<s the geometry changes. The parent support is
contained in H_e=<a^(2^(e+1))>, whereas a^(2^e) is not in H_e: an equality
a^(2^e)=a^(2^(e+1)k) would imply r divides 2^e(1-2k), contradicting its
two-adic valuation s>e. These two subgroup cosets are disjoint, so the
fine-label fidelity is zero. For the usual t>=s there are exactly s such
terminal rounds; for arbitrary t the statement covers min(s,t) rounds.
This agrees with the certified suffix mechanism. A coarse partition obtains
zero only when it separates those cosets; an arbitrary merging of cells
need not preserve this zero-fidelity conclusion.

## 8. Whole-algorithm consequence and the useful structural escape

For a native depth-i preparation sample, count up to i requested modular
columns to create the label, plus P evaluation and partition/collision work.
A sample budget m therefore does not mean O(m) bit operations. Multiply by
actual typed arithmetic costs and include source admission, certificate
construction, confidence amplification, word precision and storage. For a
constant-budget collision certificate on s=2^i flat labels, the sample count
alone is of order 2^(i/2). The current exact/approximate sampler still must
pay for all uncertified rounds and any exact fallback. A saved local row
query is not automatically a saving in complete factoring cost.

The promising escape is additional *computable structure*, such as a
Gaussian quartic character whose value is proved to encode relevant cosets.
That can make a small partition informative without learning a hidden table;
it lies outside the information model of (2)--(5). Its multiplication law,
composite-modulus definition, source admission and per-label bit cost still
need proof. A supplied witness also benefits ordinary arithmetic methods:
the previously published same-witness trial-division and balanced-semiprime
comparators remain mandatory for any claimed factoring advantage. There is
no claim here that four colors solve the unstructured case or that verifying
a supplied witness is the same as discovering one.

Concrete output of this unit: two explicit information/representation bounds
(2) and (4), the conditional finite-batch collision certificate (8), and the
exact standard-Shor singleton fidelity formula (12). The last result shows
that when L is much larger than the odd part q before the final s rounds,
even exact marginal access and arbitrarily many partition colors cannot
make this norm-only certificate small. Progress in that regime must use
additional signed or internal-vector coherence information, rather than
only refining work-label partitions. Structured partitions or cheap flatness
witnesses remain useful in their proved regimes; a few preparation samples
do not reveal all useful interference structure without further assumptions.

Global-Knowledge-Sync: main@f44ed595 / GLOBAL_KNOWLEDGE_V1
