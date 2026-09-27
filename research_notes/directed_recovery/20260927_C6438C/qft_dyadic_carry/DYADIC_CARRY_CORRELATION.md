# Dyadic displacement coefficients: two-carry contraction and modular alias cost

Status: AUTHOR_SYMBOLIC_CANDIDATE / SHARED_CONTEXT / NOT_ADMITTED.
This bounded unit reads and extends the already implemented relative-Gram
observer. It is not a new execution, ideal-QFT calculation, priority claim or
polynomial classical-Shor theorem. The parent supplied the current canonical
policy lease `06788df022dbd11720132b4ed0882ce8e41b3b8a`; professional archival
append `35da005f357501045d4462d9eda78fe6f7346c11` changes no research policy.
No EM/GK write or professional query is performed by this unit.

## 1. Consumed frontier and new question

The files actually read are:

- `sep26-shor-general/optimization/collision_analysis/COLLISION_GRAM_ANALYSIS.md`;
- `sep26-shor-general/optimization/collision_analysis/GRAM_PROTOTYPE_NOTE.md`;
- that directory's `gram_sampler.py`, SHA256
  `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`;
- `sep27-qft-coherence/CONTINUE.md`.

The old prototype already computes full raw correlations Gamma, memoized by
depth and observed residue. Its six bounded tests were exact but used more
matrix slots than the explicit selected state. This draft does not rediscover
its recurrence or equate the existing exact D=6 carrier codec with orbit
compression. It factors the dyadic query dependence into a history-dependent
signed coefficient and a history-independent modular alias condition.

Fix a real measured prefix h of length i. Every phase word is the actual
complete admitted word; write its chronological round-j feedback as T_j and
the selected sign as sigma_j. Put O_j=sigma_j T_j. Different O_j may fail to
commute. All D coordinates, including residuals, remain. D=6 is allowed only
with the existing full61 boundary-embedding certificate; otherwise D=61.

The empty-prefix case is the existing basis correlation. Below i>=1,
L=2^i, and b is the actually certified residue a^(2^(t-i)) mod N. The base
a must be a unit. This is inherited from the admitted modular program, not
inferred from this observer. No factor or order is an input.

For n in [0,L), let n_j be its bit of weight 2^(i-1-j), so j=0 is the first
processed, most significant preparation choice. Define

    U_h(n) = O_(i-1)^n_(i-1) ... O_1^n_1 O_0^n_0 e0.

This is a column vector with the original temporal order. Direct expansion
of the inherited actual two-arm branch identity gives

    v_h(w) = 2^-i sum_(0<=n<L, b^n=w mod N) U_h(n).       (1)

This identity includes colliding paths with their signs. It is not a claim
that the paths are incoherent or that a label has a unique preparation.

## 2. Exact displacement decomposition of the existing Gamma observer

For any integer d with |d|<L define the complete matrix

    C_h(d) = 4^-i sum_(0<=n<L, 0<=n+d<L)
                         U_h(n) U_h(n+d)^T.               (2)

For other d set C_h(d)=0. It includes raw denominator squares, with no
division by the history probability. Changing the summation index gives

    C_h(-d)=C_h(d)^T.                                    (3)

For an actually queried unit residue z, define the finite alias set

    A_i(z)={d in [-(L-1),L-1] : b^d=z mod N}.             (4)

Substitute (1) into the old Gamma_h(z)=sum_w v_h(w)v_h(zw)^T.
Every ordered pair (n,m) has exactly one d=m-n, and its label condition is
b^m=z b^n, equivalent to b^d=z because b is a unit. Therefore

    Gamma_h(z) = sum_(d in A_i(z)) C_h(d).                (5)

The sampling observer stays exactly the old one:

    M_h=trace Gamma_h(1),
    G_h=trace(T_i Gamma_h(p_i)),
    P(next bit 0 | h)=(M_h+G_h)/(2M_h),                  (6)

where p_i=a^(2^(t-1-i)) mod N is the next actual multiplier and M_h>0.
Zero-mass histories remain a separate condition. For i=t only the mass or
other requested correlations exist; there is no next-bit query.

Equation (5) separates tasks. C_h(d) depends on the actual measured history
and its noncommuting words; once that word list is fixed, its contraction
uses neither N, a nor a hidden period. The choice of a compiled word list
may itself depend on the externally requested circuit/error parameters.
A_i(z) depends
on the modular schedule, not the history or internal phase word. The same
certified alias geometry can be reused for different histories or repeated
shots with the same base and schedule. It must still be discovered and
verified; returning only some solutions is not sufficient for (5).

## 3. New lemma: one displacement coefficient uses two carry matrices

Let 0<=d<L and write its ordinary i-bit digits as d_p, with p=0 least
significant. In m=n+d let c_p be the carry *into* digit p. Since n,m are both
i-bit integers without wraparound, the boundary conditions are

    c_0=0, c_i=0,
    n_p+d_p+c_p = m_p+2c_(p+1),                         (7)

and all carries are 0 or 1. Normal addition propagates low-to-high. We do
not reverse the native operator order to follow that propagation. Instead
process the finite constraints (7) high-to-low, keeping the still-undecided
incoming carry as a two-state boundary index.

Initialize two D-by-D signed matrices

    X_0=e0 e0^T, X_1=0,

where the initial state index is c_i. For j=0,...,i-1 set p=i-1-j. For each
old boundary c_out=c_(p+1), each new boundary c_in=c_p and bits x,y in {0,1}
satisfying

    x+d_p+c_in = y+2c_out,

add, to a fresh matrix Y_(c_in),

    O_j^x X_(c_out) (O_j^y)^T.                          (8)

After this layer replace X by Y. Return X_0/4^i after the last layer; discard
X_1 because it represents an invalid carry c_0=1. Negative d uses (3), not
negative-digit arithmetic or a reversal of words.

**Lemma.** This two-state algorithm returns exactly C_h(d).

**Proof.** After j layers, X_c is the sum over all chosen high-order bit
pairs and carry paths satisfying the already processed constraints and
c_i=0, whose remaining boundary carry is c. Each summand is the ordered
partial vector on the left times the ordered partial vector on the right
transposed. Applying (8) appends O_j on the left of each partial vector,
which is precisely chronological state evolution. It neither reverses nor
commutes earlier factors. After i layers, requiring c_0=0 makes the accepted
bit pairs exactly the unique additions m=n+d in [0,L). There is one carry
path for each accepted pair, so the sum has neither omission nor multiplicity.
The common 4^-i restores the original two raw amplitudes. This proves (2).

For either value of d_p there are exactly four allowed tuples
(c_out,c_in,x,y), before zero-state pruning. Thus at most four full left/right
native matrix actions and their sums occur per digit, while the live state
is two D-by-D matrices. At d=0, the accepted paths have x=y throughout and
the result is the ordinary unaliased path-density sum; in particular

    trace C_h(0)=2^-i.                                 (9)

Equation (9) is not the whole history mass if nonzero aliases return to 1.
The omitted terms could include negative trace contributions.

A two-round ordering check makes the convention explicit. If chronological
operators are A then B, the four path vectors are e0, B e0, A e0, BA e0
in increasing integer n order. For X=e0e0^T this gives

    16 C_h(1)=X B^T+B X A^T+A X A^T B^T.

The carry contraction has exactly these three accepted terms. Moving A and
B past one another or evolving the physical word low-bit-first is not an
allowed simplification.

## 4. Actual-executor contract and resource accounting

No numerical execution is claimed here. A future implementation can reuse
the frozen Gram prototype's actual columnwise `_left`, transpose-mediated
right action, signed `PositivePathObserver` sums and dyadic denominator
representation. Signs sigma_j enter both chosen arms in (8), once for each
arm whose bit is one. A carry index is a summation label, not a physical
coordinate or an excuse to drop residuals.

With word length ell_j and the fixed native alphabet, a left or right action
uses D actual vector actions on its matrix. Computing one C_h(d) therefore
uses O(D sum_j ell_j + i D^2) primitive/vector arithmetic slots, up to the
known cost of each native gate and exact signed observer. This is polynomial
in the input word descriptions and i, not in the number L of paths. Keep
two boundary matrices plus fresh accumulators; no work-amplitude map or
ancestral Gram cache is required. Streaming one d at a time into Gamma also
avoids storing every coefficient.

If T_j has common dyadic denominator 2^k_j, all unnormalized coefficient
entries may use denominator 2^(2i+2 sum_j k_j). The number of summands is at
most L and all U vectors have norm one, giving polynomial numerator-bit
bounds in i and sum k_j. These bit lengths, native receipts and observer
transcripts must be counted; O(D^2) matrix slots is not O(1) byte memory.

This replaces the generic three-way recursive expansion by a contraction of
its *signed coefficients*. It changes the quantities computed, not just the
constant D. It does not remove the modular information in (4).

## 5. Complete modular-alias discovery, with no supplied order

Let J_i(z)=|A_i(z)|. All entries must be generated or replaced by an exact
proved aggregate. Neither random spot checks nor finding one return proves
completeness. For nonnegative d, solve b^d=z for 0<=d<L. Negative d are
obtained by solving b^d=z^-1 for 1<=d<L and using (3); d=0 is included once.
Every inverse must be certified on the unit domain by the existing typed
arithmetic. A nonunit input returns to the parent gcd/failed-admission path,
not to this group argument.

One explicit discovery option is bounded-interval baby-step/giant-step. Fix
1<=B<=L. Store all pairs (b^u,u), 0<=u<B, including repeated labels if any.
For each 0<=v<=floor((L-1)/B), query z*b^(-vB), retrieve every matching u,
and retain d=vB+u<L. Each valid d has exactly one (v,u) representation. Repeat
for z^-1 with the stated zero exclusion. Storing only one exponent for a
repeated baby residue would lose aliases and invalidate (5).

This takes O(B+L/B+J_i(z)) exact group operations, O(B) stored label/exponent
pairs, plus all equality/hash/sort work and output work. Choosing
B=ceil(sqrt L) is just a time-space option; arbitrary B permits an explicit
tradeoff. All labels use O(log N) bits and displacement exponents O(i) bits.
Construct b^B and its inverse through actual typed multiplication/squaring;
do not treat exponentiation, giant steps or equality as free. Hashing may
route labels as declared host wiring, while the label values and membership
witnesses must come from the authorized exact arithmetic route. Source/native
admission and table-cache/trace bytes are additional costs.

The complete query cost using this option is consequently

    modular_cost(B+L/B+J) + J * carry_coefficient_cost(i),      (10)

and J can be large. If the analysis-only order R=ord_N(b) is small, J is of
order L/R, even though the subgroup itself is small. The implementation must
not call (10) O(sqrt L) while suppressing that output term. It may instead
use a short-period fallback: consecutive baby powers that first return to 1
at R<=B discover and certify R with their complete preceding list. Then the
existing explicit dynamics on at most R labels is a legitimate alternative.
This discovers order by finite work; it never receives it as an input.

If no return occurs through exponent B, then R>B. In that case each of the
two bounded intervals has at most 1+L/B solutions, so J=O(L/B). With the
short-period fallback, B near sqrt L gives a conservative generic bound of
poly(i,D,word bits,log N)*sqrt L for this query/history computation. This is
not a new asymptotic improvement over the already constructed checkpoint
point-row meet-in-the-middle backend. The difference is the separation of
reusable history-independent modular data from two-state signed contractions.
It may reduce repeated ancestor reconstruction across histories; actual
total arithmetic, matrix storage and certificate cost must decide that.

At default t=2 ceil(log2 N), sqrt(2^t) is of order N. Thus this generic bound
still does not provide polynomial bit complexity or a factoring advantage.
Nor does a fast conditional Gram query automatically provide the terminal
work label requested by a joint-latent interface. Equation (6) supports the
existing control-only Gram sampling route; other outputs need their own cost.

The classical comparator must receive the same discovered information.
In particular, a nonzero return in A_i(1) supplies a verified exponent
multiple for b, while the first return in the complete consecutive baby
list supplies its exact order R. Since b=a^E with E=2^(t-i), a return d
also supplies a verified return exponent E d for a. That may be used
directly by an ordinary order/factor postprocessor, with its verification,
possible further reduction and gcd costs included; a supplied multiple
alone does not guarantee a factor. It would be misleading to charge BSGS
only once to this observer and then compare against a classical baseline
that is denied its discovered return information. The intended advantage
being tested is reuse when querying the complete actual native control
distribution over many histories. It is not a demonstrated factoring
advantage.

## 6. Why an inexpensive residue quotient cannot replace the signed sum

Here is a reachable, finite source-level counterexample to replacing all
same-character relative shifts by one Gram value. Use the already considered
N=65, a=3, t=4 and public norm representation 65=1^2+8^2. Symbolically,
the first actual multiplier is b=3^8 mod65=61, with b^2=16 and b^3=1.
The first feedback is empty, so after the first sign sigma the actual raw
state is

    v(1)=e0/2, v(61)=sigma e0/2,

with all other rows zero. The complete native 61-carrier is retained; its
residual entries happen to be zero at this first prefix, not deleted.
Consequently

    Gamma_1(1)=e0e0^T/2,
    Gamma_1(61)=sigma e0e0^T/4.                         (11)

Any quartic character sends b=a^8 to color zero, as it sends 1. Thus even
this actual reachable prefix distinguishes two relative shifts with the
same four-color value, including their trace observer. The two histories
sigma=+1 and -1 additionally share identical row norms but opposite shifted
correlation. Equation (11) is a symbolic deduction from the frozen actual
branch identity, not a new propagated experiment. It does not discredit
the valid terminal-support use of that character.

There is also a finite-horizon limitation for a *deterministic point-value*
quotient of the relative shifts. Suppose such a quotient is required to
represent queries at a common depth i and preserve each remaining recursive
action in the prescribed sequence b, b^2, ..., b^(2^(i-1)), choosing a
positive, negative or zero shift at each descent. It must also preserve the
terminal base test Gamma_0(z)=e0e0^T times 1[z=1]. All i descents are
available in this contract. On the distinct residues among 1,b,...,b^(L-1),
any two b^d != b^e are distinguishable: the binary digits of 0<=d<L
choose a negative or zero shift at each prescribed descent, multiplying
both queries by b^-d. The first then returns to 1 and the second does not.
Hence that quotient needs at least min(R,L) classes at this starting depth.
This does not assert the same bound at an intermediate depth with fewer
available shifts, or only for the restricted query set actually encountered
while evaluating one initial Gamma_i(1).
This is a restriction on that exact pointwise automaton contract, not a
lower bound on weighted sums, query algorithms or all classical simulators.
The carry contraction deliberately sums signed paths instead of claiming
these residue queries are equal, and therefore is not contradicted by it.

For comparison, the old unpruned `gamma(i,1)` recursion requests, at depth k,
all residues b^d with |d|<=2^(i-k)-1. Signed powers of two fill this entire
integer interval. Its number of distinct keys at that level is therefore
min(R,2^(i-k+1)-1), independently of phase/history coefficients, because the
current code calls all three children before any coefficient cancellation.
Transpose pairing can save at most a factor of two in this count. The new
two-carry coefficient contraction exploits more structure than such pairing.

## 7. Exact next bounded implementation step

Implement `displacement_coefficient(program, history, d)` separately, using
the existing admitted actual native phase words and signed observer. First
compare every |d|<2^i at selected prefixes of the frozen N21/t4 and N65/t4
fixtures against explicit same-word sums (2), including negative d,
overflow-boundary rejection and at least one genuinely noncommuting ordered
feedback history. Keep all residual entries, not only trace agreement.

Then implement the complete typed alias iterator (4), including repeated
baby residues and the short-period fallback. Compare (5)-(6) with the frozen
Gram query and selected-row implementation. Measure modular setup/columns,
integer bit growth, carry matrix slots, actual native word applications and
signed-observer work. Separately report one-history and repeated-history
cost, so reuse of modular geometry is not confused with free preprocessing.
No favorable scaling claim follows before these checks; no extra ideal
reference or precision upgrade is needed for this representation test.

Global-Knowledge-Sync: main@06788df0 / GLOBAL_KNOWLEDGE_V1
