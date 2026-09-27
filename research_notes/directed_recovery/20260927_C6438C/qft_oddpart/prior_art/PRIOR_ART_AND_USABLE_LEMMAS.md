# Prior art and usable compression conditions

Status: source reading, symbolic derivation and shared-context static review.
No new scientific arithmetic or ideal-QFT reference was executed here. The
actual query evidence is separate from the mathematical claims below. The
general efficient classical simulation problem remains open.

## 1. What was actually searched and read

The existing QFT/MPS and weighted-bisimulation provider records were inspected
and reused as routing evidence. They are PARTIAL/CONFLICT, not comprehensive
negative searches. The earlier quartic query is unrelated. One new Scholar
task searched `"Shor" "decision diagram" "simulation"`, n=8. Issue 2497
returned eight metadata records, child PARTIAL, outer FAILED. No second
query or retry was sent. Request, intake, complete readbacks and validated
execution receipt are in this directory. The metadata/status extraction is
canonically archived at GK `ed11167f4102d004e010643d74c00f0c658556a0`.

The following primary material was actually opened and read beyond an
abstract. Page numbers are PDF pages; READING_EVIDENCE.json binds the local
reading copies. Those full papers and extracted texts are reading material,
not part of the proposed research publication.

* **Dang, Hill and Hollenberg, Optimising matrix product state simulations
  of Shor's algorithm**, arXiv:1712.07311v4, published in Quantum 3, 116
  (2019). Read abstract and Sections 4–5, especially pages 4–7. For
  r=2^s q with q odd, their MPS arrangement isolates the low control bits
  and makes the post-work-measurement bond depend on q. Their dynamic
  construction detects the appropriate split from Schmidt ranks; it does
  **not** require advance knowledge of r. The modular state still has
  an r-dependent cost before measurement. Thus odd-part-dependent Shor
  simulation is prior art, not a novelty claim for this project.
  [Official preprint](https://arxiv.org/pdf/1712.07311v4)
  [Published article](https://quantum-journal.org/papers/q-2019-01-25-116/).

* **Pohlig and Hellman, An improved algorithm for computing logarithms over
  GF(p) and its cryptographic significance**, IEEE TIT 24 (1978), 106–110.
  Read Sections III–IV, printed pages 108–110. The paper resolves logarithms
  in prime-power components, recovers exponent digits, and recombines with
  CRT. Its original setting has a prime field and known factorization of
  p−1; modular multiplications are the operation unit. It does not supply
  free factorization or arbitrary subgroup order. Section 4 below derives
  the exact cyclic-subgroup adaptation needed here and charges its inputs.
  [Author-hosted original](https://ee.stanford.edu/~hellman/publications/28.pdf)
  [DOI](https://doi.org/10.1109/TIT.1978.1055817).

* **Kiefer, Notes on Equivalence and Minimization of Weighted Automata**,
  arXiv:2009.01217v1. Read Section 1 and Sections 3–4, especially Theorems
  3.6 and 4.3. Forward/backward conjugacy preserves all word values;
  minimum realization dimension equals Hankel rank. The stated minimization
  cost is O(|Sigma| n^3) field operations for an already explicit n-state
  automaton. These notes expose classical results rather than claiming
  their invention. They do not show that our exponentially sized residue
  realization can be built or minimized in poly(log N) time.
  [Author's manuscript](https://arxiv.org/pdf/2009.01217v1).

* **Kimura, Fujita and Wille, Scoring-based Static Variable Ordering for
  Decision Diagram-based Quantum Circuit Simulation**, arXiv:2512.01186v1
  (preprint). Read Sections II–IV and V.C–VI. Scalar-equivalent subgraphs
  are shared under a fixed variable order. The proposed ordering is
  explicitly heuristic; the paper allows exponentially many nodes and
  floating-point discrepancies. Its Shor experiments demonstrate practical
  ordering effects, not a polynomial state-size theorem or an exact
  weighted-collision recurrence. This is the relevant new provider hit
  actually followed to primary text; the seven other hits remain metadata.
  [Official preprint](https://arxiv.org/pdf/2512.01186v1).

The older BGL, CT-state, sparse-output and QFT-MPO routes already have their
scope discussion in `sep27-qft-research/prior_art/PRIOR_ART_AND_BRIDGES.md`.
They were not re-queried or relabelled as new findings. This bounded reading
does not establish absence of other prior art.

## 2. Consequence for this project's novelty and hard gap

The project's distinctive object is the **complete signed matrix**
Gamma_h(z)=sum_w v_h(w)v_h(zw)^T for a fixed actual native feedback history,
including all admitted carrier residuals. It is different from the ideal
Shor MPS state, but that difference alone does not prove a new asymptotic
simulation result. The already proved q-residue contraction and the new
typed small-odd-part discovery should be described as source-bound exact
algorithms with charged discovery and validation costs.

The unresolved step is a *constructible* small representation of the actual
weighted histories when q is large. A short product formula, one small
matrix Gamma, a small physical carrier, a low-rank ideal QFT, or observed
decision-diagram sharing is not itself such a representation certificate.

## 3. A precise weighted-automaton bridge worth pursuing

The following is a direct symbolic certificate criterion, not executed
native code and not an assertion that certificates exist cheaply.

Let an exact layered computation have rational column state space V_j,
initial alpha, and ordered transition maps A_(j,c):V_j -> V_(j+1), where
c is an allowed local label (for example a pair of preparation bits).
Let B map the final state to all requested signed matrix entries, not just
a trace. Suppose one supplies linear maps Q_j:V_j -> F^(k_j), compressed
maps Ahat_(j,c), and Bhat satisfying

    Q_(j+1) A_(j,c) = Ahat_(j,c) Q_j  for every j,c,
    B = Bhat Q_i.

Then every original ordered word value equals

    B A_(i-1,c_(i-1)) ... A_(0,c_0) alpha
      = Bhat Ahat_(i-1,c_(i-1)) ... Ahat_(0,c_0) Q_0 alpha.

Proof is induction on the layer using the displayed intertwining equality.
It never reverses noncommuting operators. Summing any prescribed collection
of words preserves the equality by linearity. The same criterion may be
restricted to certified reachable subspaces, provided those subspaces and
their closure are also verified. Merely observing equality on one reached
vector is insufficient for future words.

For a cut j, form a prefix/suffix matrix H_j whose entries are the complete
scalar word outputs, stacking the requested output coordinates as needed.
Any k_j-dimensional such realization factors H_j through that space, hence
rank(H_j)<=k_j. This is the finite layered counterpart of the cited Hankel
criterion. It is a limitation on this representation class, not a universal
classical running-time lower bound.

**Proposed next certificate target.** Find Q_j with k_j << q D^2 directly
from a restricted actual history class and verify the displayed identities
against admitted native actions and all required output rows. Charge the
description length, construction, exact arithmetic bit lengths and replay.
For generic q-residue states the original dimension is already O(q D^2),
so black-box minimization after constructing that state does not solve the
large-q bottleneck. A matrix whose columns merely span one already computed
Gamma has not preserved every future target and feedback query.

A further sufficient special case is a homogeneous block with compressed
transition A. Matrix power and geometric-sum doubling evaluate sums over
that block in logarithmically many matrix products. The identity

    S_(2m)(A)=S_m(A)+A^m S_m(A)

uses no inverse of I−A, so it covers eigenvalue one. However materialized
rational powers can have bit length linear in m; an arithmetic-operation
bound alone is not a bit-complexity result. Layer-dependent feedback lacks
one fixed A unless an additional exact certificate supplies it.

This complements, rather than replaces, the author's concrete leading-zero
contraction in `../weighted_structure/WEIGHTED_ODD_PART_STRUCTURE.md`: that
case obtains cheap point values from interval counts even though the cyclic
correlation matrix has rank q. Its actual native noncommutation example also
rules out simply importing a common ideal phase root into the direct words.

## 4. Charged target addressing: cyclic Pohlig–Hellman specialization

Assume the unit b modulo N has **certified exact** order R=2^s q, q odd, and
z is a verified unit target. These are paid premises. A mere return exponent
is insufficient for exact modular-collision aggregation.

Use g2=b^q, y2=z^q, gq=b^(2^s), yq=z^(2^s). Then g2 has exact order 2^s
and gq exact order q. For s>0 define eta=g2^(2^(s−1)), which has order two.
In a composite modulus eta need not be the residue −1.

Recover r2 one binary digit at a time. With lower j digits x_j already
chosen, form

    d_j=(y2 g2^(−x_j))^(2^(s−1−j)).

Accept digit zero if d_j=1, one if d_j=eta; otherwise the target fails this
component. Update x_(j+1)=x_j+digit*2^j. At j=s−1 the equality is an exact
residual test, so the completed chain gives y2=g2^r2. For s=0 instead require
y2=1 and take the trivial residue modulo one.

Recover rq by a paid q-step table of powers of gq and look up yq, or by a
separately certified BSGS algorithm with its table/verification costs. For
q=1 the requirement is yq=1. No factorization of q is needed for the linear
table route. Further smooth-q speedups would need paid factorization data.
CRT yields the unique 0<=r<R with these two residues.

If both exact projected equalities have the **same reconstructed r**, they
already imply z=b^r even in a noncyclic unit group. Indeed x=z b^(−r) has
x^(2^s)=x^q=1, and Bezout for gcd(2^s,q)=1 gives x=1. An additional typed
b^r=z check is a useful implementation cross-check, not a missing algebraic
premise. This explicitly adopts the correction in the companion note §8.

With straightforward binary lifting, the two-primary part costs O(s^2)
group multiplications plus inversions and exponentiation overhead; the odd
table costs O(q), reusable only with a bound source/base/order. All residues
have O(log N) bits, and typed arithmetic, storage, source checks and receipts
remain charged. No claim of poly(log q) target discovery follows.

**Same-information comparator.** Once this work yields an exact order of the
Shor base, an ordinary classical order postprocessor receives it too. It can
test parity, compute the half-power and gcd candidates without running the
quantum measurement simulator. A bad base still need not split N. If the
known odd part came from a squared base, the original base's two-primary
order is recoverable by paid repeated squaring of its odd-power residue.
One cannot count the discovery cost for the comparator while treating it as
free preprocessing for the simulator.

## 5. Bounded static reviews performed in this unit

Read `../period_discovery/typed_odd_part.py` SHA256
`188defd9307e461e8617243f76a8b6109309d6ac6b1834a71511172b58a6618c`,
checker SHA256 `ab4c674f58241cd1c1c0e2246e62565c6d2400abd8e39cd62b1a2174010135b0`,
and its summary. No material defect found: n squarings remove the two part;
the first odd return is exact q; the first square return of b^q recovers s.
PARTIAL retains no claimed order. Canonical JSON replay distinguishes bool
from int and rejects nonstring keys. Dynamic native cache-call deltas are
explicitly outside semantic authentication. The author's bounded execution
is not a new execution by this reviewer.

The N97 example uses 18 modular column requests versus 96 for its baseline,
but its recorded setup/replay-inclusive digit work is 26,925 versus 16,567.
This is a column-count gain, not a measured total-work gain on that example.

The companion weighted-structure note's general g/M formula, suffix phase
indexing, 4^−K factor, full cyclic rank example and actual Q/W commutator
were also checked symbolically; no material defect was found. This is a
shared-context author review, not independent admission.

## 6. Next useful bounded research outputs

1. Execute the leading-zero Count-weight contraction against the complete
   matrix interface, including original modular target, signed negative
   displacements and the applicability mass. Its symbolic gain is history
   dependent; a rare cheap branch alone is not an efficient sampler.
2. Implement the paid cyclic target-address routine with exact component
   bindings, or reuse the current actual implementation if completed by the
   team. Report setup and certificate replay alongside the modular calls.
3. Seek a certificate of the layered quotient criterion for a nonzero,
   noncommuting actual history family. A positive result must supply the
   quotient cheaply; a negative rank result must state its representation
   class. Do not infer all-algorithm impossibility from full cyclic rank.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1.
