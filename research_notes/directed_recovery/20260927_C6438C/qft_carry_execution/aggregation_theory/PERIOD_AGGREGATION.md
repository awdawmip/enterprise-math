# Whole-period aggregation with a small odd part

Status: AUTHOR_SYMBOLIC_CANDIDATE / SHARED_CONTEXT / NOT_ADMITTED.
This is a new symbolic unit, not a native execution, new ideal reference,
or a general polynomial-time Shor simulation claim. It writes only this
directory. The parent supplied a fresh helper PASS and valid canonical
lease at `06788df022dbd11720132b4ed0882ce8e41b3b8a`; the unchanged bootstrap,
operating-manual and synchronization entries were also checked locally.
No remote write, scientific arithmetic execution or professional query is
performed here.

The consumed source is `sep27-qft-signed/DYADIC_CARRY_CORRELATION.md`, SHA256
`70b35a57ee0ffe628b2090f0ddeb0a7bce7eb076a03b627ca10ba8e1f815f3d1`,
including its exact full-carrier seed, chronology, modular alias discovery
cost and same-information classical comparator. Its two-carry coefficient
lemma is reused, not reproved or represented as a new result here.

## 1. Observable and the new question

Fix one actual readout prefix h of length i, L=2^i, and the actual unit
residue b=a^(2^(t-i)) mod N. At chronological round j let O_j=sigma_j T_j,
with the full admitted native feedback T_j. With n_j the bits of n from
most significant to least significant, the source defines the vector

    U(n)=O_(i-1)^n_(i-1) ... O_0^n_0 e0,
    C_h(d)=4^-i sum_(0<=n,n+d<L) U(n) U(n+d)^T.

All D carrier entries and signed terms are retained. D=6 is available only
through the existing full61 word-boundary admission; otherwise D=61.
No factors, hidden order or commutativity of O_j are assumed.

If an exact order R=ord_N(b) and a representative 0<=r<R with b^r=z have
actually been obtained and certified, the existing Gamma observable is

    Gamma_h(z)=4^-i sum_(0<=n,m<L, m-n=r mod R) U(n)U(m)^T.       (1)

This is the whole arithmetic progression of displacement coefficients,
including positive, zero and negative displacements where applicable.
The question is whether (1) can be contracted without outputting every
integer d in the finite alias set. Sections 4 and 5 charge the acquisition
of R and r; they are not free inputs to a claimed general algorithm.

## 2. Odd-part aggregation lemma

Write the certified exact order as R=2^s q, with q odd. First suppose
0<=s<=i, put H=i-s, and split

    n=2^s A+u,   m=2^s B+v,
    r=r0+2^s rH,
    0<=u,v,r0<2^s,   0<=rH<q.

The low-bit congruence has a unique overflow c in {0,1}:

    u+r0=v+2^s c.

Consequently the complete congruence in (1) is equivalent to the two
conditions

    u+r0=v+2^s c,    B-A=rH+c mod q.                        (2)

The sign of c in the second condition is positive: m-n equals
r0+2^s(B-A-c). This is important when joining the two contractions.

Build q full matrices M_e while processing the H high bits, in their
original chronological order. Initialize M_0=e0e0^T and all other M_e=0.
For the next pair of high bits x,y in {0,1}, with round operator O_j, use
fresh accumulators and add

    O_j^x M_e (O_j^y)^T   to   Mnew_(2e+y-x mod q).         (3)

After H layers, M_e is the sum of the actual ordered high-prefix outer
products with B-A=e mod q. This follows by appending a binary digit to
the two integer prefixes: the difference becomes 2e+y-x. The native
operation appends on the left of each vector, so no word is reordered.

Now initialize the two high-boundary carry states for the s low bits by

    X_c=M_(rH+c mod q),   c=0,1.                          (4)

Process only these s low bits using the source's reverse carry constraints
for adding r0, with the next actual operators O_H,...,O_(i-1). The high
carry is not forced to zero: both possibilities in (4) are needed for
modular wraparound. At the low boundary require carry zero as in the
source lemma, and return

    X_0 / 4^i.                                           (5)

Use fresh accumulators at every layer. If two seeds in (4) refer to the
same M_e, they have equal values but are separate state entries; mutable
aliasing and in-place accumulation are not part of the formula.

**Lemma.** Equations (3)--(5) equal the complete matrix (1).

**Proof.** Equation (3) partitions all high-prefix path pairs by their
integer difference modulo q, retaining their exact temporal vector
products. Equation (2) selects exactly the required high residue for each
possible low overflow, which gives (4). The inherited low-bit carry
contraction accepts exactly the low-prefix pairs with that overflow and
zero incoming carry. Every pair (n,m) satisfying (1) has one high residue
and one low carry path, so it is accepted once. Every accepted pair
satisfies (2), hence (1). The common factor 4^-i is the original two raw
amplitude factors. Nothing has been conditioned on a history probability.

There are at most four left/right native matrix terms per high residue
and at most four per low carry layer. The bound is

    O(q H + s) matrix-transition terms,
    O(q D^2) live rational scalar slots,                  (6)

including fresh accumulators up to a constant factor. This avoids the
number J of individual aliases. Unoccupied high residues may be stored
sparsely, but the bound does not presume they remain sparse.

Boundary cases are part of the statement:

- s=0: there is no low block; (5) simply selects M_r/4^i.
- s=i: the high block is empty, M_0=e0e0^T and other M_e=0.
- q=1: the high block has one matrix, updated by
  Mnew=(I+O_j) M (I+O_j)^T. Both low-boundary seeds equal M;
  each valid low pair still has a unique carry, so this is not double
  counting. The cost is O(i), regardless of R=2^s or J.
- i=0: use the original basis correlation directly.
- s>i: R>=2L. At most one representative of r modulo R lies in
  [-(L-1),L-1]. It is r if r<L, or r-R if R-r<L, otherwise none.
  The first two tests cannot both pass. Use the already proved single
  displacement contraction, or return zero. No q-state allocation is
  needed in this case.

As a useful q=1 check at r=0, the high block coherently sums arbitrary
high-bit pairs, while the low block pairs equal low bits. Thus this is
not the incoherent path-density matrix C_h(0); all period aliases remain.

## 3. BRC execution and bit-cost boundary

The proposed executor uses the already admitted full-word matrix action
columnwise and the existing signed observer. The residue/carry indices
are finite summation labels, not added physical dimensions. In particular,
no amplitude entry or residual is discarded between native words.

For a native word of length ell_j, one left/right matrix action requires
D vector actions on that word. A conservative scalar-operation bound is

    O(q D sum_(j<H) ell_j + D sum_(j>=H) ell_j
      + (q H+s) D^2).                                   (7)

If T_j has dyadic denominator 2^k_j, a shared final denominator may be
2^(2i+2 sum_j k_j). Before final scaling, there are at most L^2 outer
products of unit vectors. Intermediate numerator/denominator bit lengths
are therefore bounded by O(i+sum_j k_j), apart from the ordinary index
and descriptor bit costs. All integer arithmetic, comparison, receipts,
source validation and retained observer transcripts must still be charged.
Equation (6) counts scalar slots, not constant-size bytes.

For s=0 this is an ordinary q-residue matrix contraction and may be slower
than explicit q-row propagation. The useful parameter reduction is from
R=2^s q or an alias count to q; it is not a claim that q itself is cheap.
No implementation or performance measurement of (3)--(5) is in this unit.

## 4. Acquiring exact R without treating it as a promise for free

A supplied return exponent b^K=1 alone is insufficient to replace the
collision condition by m-n=r mod K. If the true order properly divides K,
that replacement misses aliases. Exact-order certification is necessary.
The older bounded BSGS/consecutive-return route remains valid with its
full discovery/output cost, and must not be charged only to a comparator.

There is a targeted discovery algorithm when one is willing to spend a
declared odd-part budget Q. Let n=ceil(log2 N). The order of a unit is
strictly below N, so its 2-adic exponent is at most n. Compute c=b^(2^n)
by n actual modular squarings. Its exact order is the odd part q of R.
Generate consecutive powers c,c^2,...,c^Q, stopping at the first 1.
If none returns, report that this small-odd-part route is unavailable at
budget Q; do not guess R or report a completed contraction.

If the first return is q, that complete consecutive-power trace certifies
the exact odd part. Compute b^q and square until its first return to 1.
If b^q=1 initially, s=0; otherwise the first return after s squarings
certifies exact order 2^s for b^q. The two facts imply R=2^s q exactly.
This costs O(Q+n+log Q) modular operations in the successful budgeted
route, plus their O(log N)-bit typed arithmetic and verification costs.
The discovery transcript may have O(Q) entries even if live computation
uses only the current power. The proof does not silently remove that
certificate-storage cost.

This is polynomial in log N and Q, not in log Q. Choosing Q polynomial
in log N gives an algorithm for a restricted input class with a certified
small odd part. No bound says that general Shor bases belong to that class.

## 5. Query address discovery, and the same-information comparator

Even after exact R is known, a query z may not be in <b>; a valid r is
another input to (1). A full consecutive table costs O(R), which could
erase the saving in (6). With small q there is a direct charged alternative.
The following is a symbolic exact construction, not a new executed module.

First require that z is a unit. Put gq=b^(2^s), yq=z^(2^s), and search the
q powers of gq for yq; if a solution exists it gives r modulo q. Put
g2=b^q and y2=z^q. The order of g2 is 2^s. For s>0 set
eta=g2^(2^(s-1)), which is not 1 and has order two.
Recover r modulo 2^s from low bits upward. If the already recovered
j low bits are e_j, compute

    (y2 g2^(-e_j))^(2^(s-1-j)).

A genuine target power gives 1 for bit zero and eta for bit one. Reject
if neither occurs; otherwise append that bit and continue. The simple
implementation uses O(s^2) modular squarings plus exponent/inverse setup.
For s=0 this part is empty. Combine the two residues by exact integer CRT
and finally check b^r=z. The final check is essential in a unit group
which is not cyclic: merely passing projections is not admitted as a
membership certificate. If z really equals some b^r, all choices above
are forced and recover it, so a failed step or failed final check certifies
nonmembership. In that case the queried Gamma is zero.

Thus address discovery costs O(q+s^2+log N) modular operations with the
straightforward construction, plus exact integer CRT, bit and transcript
costs. The special mass query z=1 has r=0 with no discrete-log discovery.
Neither a target address nor group equality has been granted for free.

The same obtained information is available to the classical comparator.
For the Shor schedule b=a^E, E a power of two, the odd part q of ord(b)
is also the odd part of ord(a). Once q is discovered, repeated squaring
of a^q finds the remaining 2-part and hence the exact order of a, for
only O(log N+log q) extra modular operations. A good base can then be
processed by the usual half-order gcd test without first simulating the
readout distribution. All such verification and gcd costs are charged.
Failure of the good-base test remains possible and is not renamed success.

Accordingly, the saving in (6) is a way to query the complete actual native
control distribution or other Gamma observables under paid structure. It
does not establish a factoring advantage on the small-odd-part class.

## 6. What the actual reverse-square schedule still needs

Let the analysis-only order of the original base be r_a=2^v q, q odd.
For the discussion of a final v-round suffix assume t>=v, as is guaranteed
by the default t=2 ceil(log2 N). The period formula itself holds for every
0<=i<=t.
At depth i the period of b=a^(2^(t-i)) is

    R_i=2^max(0,v-(t-i)) q.                              (8)

Before the final v rounds, the relevant subgroup therefore already has
odd order q. The prospective next multiplier p satisfies p^2=b. If p
has odd order q, it belongs to <b>; its representative is
(q+1)/2 modulo q, since 2 is invertible modulo q. In that middle regime,
the contraction in (6) has s=0 and still needs up to q matrix states.

Once the next multiplier has order 2 R_i, it lies outside <b>. The parent
work support is contained in <b>, its shifted copy is a disjoint coset,
and the next bit is exactly fair. This is the already established terminal
support argument, not a new consequence of phase cancellation. Given the
same certified order information, a control-only sampler may take those
remaining fair bits directly without computing a growing-period Gamma.

Thus removing the large 2^s factor in (6) is real for arbitrary late-prefix
correlation queries, but does not by itself remove the hard odd-order
middle of general Shor. A claim of an overall speedup must compare against
the pre-existing fair-suffix shortcut using the same period information.
Nor does a control correlation oracle alone supply an arbitrary terminal
joint work sample.

## 7. A rank obstruction to a uniformly small local modulo mask

One cannot simply replace the odd q-state constraint by a polylog(q)
local linear automaton because its binary description is short. Here is
a precise restricted obstruction. It concerns the collision *indicator*,
not the complexity of every possible weighted native contraction.

Take R odd and a bit cut with H high bits and k low bits, where
2^H>=R and 2^k>=R. Consider the mask

    K(A,B,u,v)=1[2^k(B-A)+(v-u)=r mod R].                (9)

Flatten this tensor across the chronological high/low cut. Restrict its
high rows to A=0, B=e for 0<=e<R. For each e choose the low column
u=0, v=l_e, where l_e is the unique representative in [0,R) of
r-2^k e modulo R. These are valid low-bit strings, and since R is odd
the values l_e are distinct. The resulting R-by-R submatrix has entry

    1[2^k(e'-e)=0 mod R]=1[e'=e].                       (10)

It is the identity matrix, so the real and rational matrix ranks of the
complete cut are at least R. Any exact local *linear* representation of
this mask at that cut, including a weighted finite-state automaton, needs
bond dimension at least R: a width W representation factors the cut
matrix through a W-dimensional space and has rank at most W.

In particular, a short formula such as R=2^k-1, or a short multiplicative
period of 2 modulo R, does not by itself imply a uniformly polylog(R)
chronological mask representation. This is a conditional statement about
the modulo mask for such R, not a claim that every such R occurs for a
particular already executed Shor input.

This lower bound does NOT exclude low-rank contractions after particular
native words are inserted, analytic cancellation, nonlocal algorithms,
number-theoretic ways to discover useful information, approximation, or
all classical Shor simulators. The fixed seed e0 and actual word family
may make a specific weighted instance easier. Establishing that requires
an additional theorem; it does not follow from the small carrier D.

## 8. Concrete outcome and next bounded check

The new result is the whole-period contraction (2)--(6), parameterized by
the *odd part* q and explicitly separated from discovery of period and
address. The pure two-power case sums arbitrarily many allowed displacements
in O(i) matrix-transition terms. The rank argument (9)--(10) identifies
why the same local-mask idea does not automatically become polylogarithmic
in a large odd period. The original schedule analysis identifies which
regime this changes and which remains hard.

The next useful implementation, after the separate single-displacement
executor is stable, is a small native whole-period aggregator with supplied
*replayed* exact-order/address receipts. Compare its complete matrix with
the sum of all source C_h(d) for one odd-period fixture and one even-period
fixture having multiple aliases. Include r=0, wraparound, s=0, s=i, s>i,
zero-mass histories and actual noncommuting feedback. Count discovery,
address, full native actions, signed observers, numerator bits and receipt
bytes separately. Compare also with explicit small-q rows plus the existing
fair-suffix shortcut. Do not rerun a favorable instance until a desired
cost ratio appears, and do not call these proposed checks completed here.

Global-Knowledge-Sync: main@06788df0 / GLOBAL_KNOWLEDGE_V1
