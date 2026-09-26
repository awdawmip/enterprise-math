# Effective fixed-word compilation after density

Status: AUTHOR_SYMBOLIC_CONSTRUCTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED.

Researcher: EM-DIRECT-C6438C. Activity: RA-CAAAC604CB513AEA8BBC1DFC.
Control Source: `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen executable primitive source: `0852cad130c1d877174d235687cf60c19f318c58`.
Scientific continuation Source supplied by root:
`58e689cbebb73b0ceaedfc33e5daebad34d0ca48`.

This unit gives a total, finite-on-each-input mathematical compiler and a typed
certificate design. It performs no new trajectory, numerical ideal reference,
word search, root refinement, or propagator implementation. The separate
bounded implementation, if executed by another unit, must supply its own
receipts and does not retroactively make this proof an execution report.

## 1. The theorem and the algorithm being changed

Use the actual D=61 H4/sign/swap alphabet of `stage80.fixed_phase`, retaining
every internal coordinate. `FIXED_ALPHABET_DENSITY.md` proves, at shared-author
level, that determinant-positive finite words are dense in SO(61). The present
theorem composes that result with a computable strict error certificate.

For every finite phase index m>=2 and positive rational delta, there is a
terminating search that returns a finite actual word W with

    det W = +1,
    ||W - U_m||_op <= ||W - U_m||_F < delta,              (1)

where U_m is the inherited algebraic ideal phase on coordinates 0,1, direct-sum
the identity on the other 59 coordinates. Every letter coefficient remains
exactly the same as in the frozen source. The search returns all-column and
inverse replay obligations, a complete word, and a rational strict error
witness. An implementation with an imposed finite search cap can return
PARTIAL, not a false impossibility or successful approximation.

Consequently, for every finite allowed even Shor width t and positive rational
epsilon, finitely many such compiled words give a full-circuit operator error
and terminal readout TV smaller than epsilon. This is a **new compiled-word
algorithm**, not the old K33 algorithm and not an improvement claim about its
unchanged phase bank. It depends on the density theorem at its actual current
author-proof status; neither document grants independent admission.

The original `target_bits=32`, `vector_bits=64`, 61-mode bank and its certificates
remain immutable. In the new profile, `target_definition` is the exact borrowed
algebraic phase branch, `observer_depth` is a proof-isolation parameter, and
`word_length` is a resource parameter. Increasing either latter parameter is
not changing a primitive angle, coefficient, physical weight or the old grids.
The same fixed native letters are merely composed into longer words.

## 2. Policy and concrete reuse resolution

The following current records were read at the control Source:

- `docs/PORTABLE_RESEARCH_PROTOCOL.md`, blob
  `ca5de2d680d2439ff4b67c2c55fbd4159813cd5c`;
- `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`, blob
  `787e74952765b61904f2bd67038291f5f081af83`, and its frozen matching machine
  contract in `stage46/constraints/heartbeat_brc_only.json`;
- `tool_invocation_policy.json`, blob `7c11ccc90f2dcfed61444cfe97fe89d5d117aa26`;
- toolbox registry blob `3889506451091ebcfbf7a58cda6517c4af8c3597` and method
  inventory blob `9289039bc689c638fbef10f9f4489e3793e999f0`.

They require ACTUAL_TYPED_BRC_ONLY for scientific arithmetic, distinguish
lookup from execution, and allow proved, provenance-preserving extensions.
They do not authorize a floating or ordinary exact-arithmetic propagator merely
because it is called a compiler. Portable research explicitly allows symbolic
identities and certificate design without reporting unexecuted work as run.

The resolutions here are:

- **T0_BRC / REUSE_APPLIED:** the exact native fixed-column and sign-companion
  semantics of `stage80.fixed_phase.primitives` and `apply_word` supply every
  candidate word and its composition law. The full columns and word provenance
  are retained. Actual execution is required for a later runtime claim.
- **COMPOSE_APPLIED:** `stage79.phase_compiler.polynomial_probe` supplies the
  actual positive three-step comparison observer; `root_bracket` and the
  existing `adversarial/zero_endpoint_extension.py` supply rational endpoint
  isolation, including zero. Their exact input/output laws are used below.
- **EXTEND_EXISTING_TOOL:** the missing interface is a strict, complete-carrier
  word-error certificate plus a fair unbounded selection procedure. This is a
  domain compiler/observer extension of the existing family, not a new generic
  BRC family. The old zero-endpoint execution was at depth 32; it is not evidence
  that arbitrary new observer depths have already been executed.
- **COMPOSE_APPLIED:** `sparse.native_adder` and the typed add/compare/multiply
  transducers in `completion/typed_integer_prechecks.py` provide a conservative
  actual-integer route for new rational certificate arithmetic, if needed.
  Signed quantities keep separate sign/magnitude or positive/negative rails;
  cross multiplication uses positive denominators and records carries/signs.
- The inventory's path-valued square-root operator is **NOT_APPLICABLE** to
  numerical algebraic-root isolation: its path-fiber semantics must not be
  confused with a scalar square-root oracle. No catalog lookup is counted as a
  new executed mathematical tool.

The frozen source's `unsafe_extensions` includes adaptive target fitting.
Here the target is fixed by m before searching, and never changed to fit a
state, residual, measured output, unknown order, factor or empirical success
rate. Only a native word is selected against that immutable specification.
This distinction and the new observer horizon must appear in the new profile;
one must not silently broaden the old profile while retaining its identifier.

## 3. Exact algebraic targets without a trigonometric evaluator

Define q_2=1. For m>=3 let q_m be the unique root in (0,1) of

    q_(m-1) q_m^2 + 2 q_m - q_(m-1) = 0.                (2)

For p in [0,1], the polynomial p x^2+2x-p is strictly increasing for x>=0,
is nonpositive at zero, and is positive at one except for the harmless p=0
case, whose unique nonnegative root is zero. This specifies an exact real
algebraic tower, including the branch choice, without evaluating pi, sine,
cosine, an exponential, or a numerical square root.

Put

    c(q)=(1-q^2)/(1+q^2),     s(q)=2q/(1+q^2),
    U(q)=[c(q)  s(q); -s(q)  c(q)] direct-sum I_59.

Then c^2+s^2=1, det U(q)=1, and (2) gives U(q_m)^2=U(q_(m-1)).
The m=2 matrix is the already exact quarter turn. The positive root choice
selects the inherited repeated-halving branch; it is not an arbitrary solution
of a high-degree root-of-unity equation. Induction gives primitive order 2^m
on the principal plane. The reference/ideal interpretation remains borrowed
exactly as in Stage79; this construction does not derive physical Born law.

The rational expression for U(q) is used **only inside a target certificate**.
No dynamic state is ever multiplied by an independently inserted U(q), and no
target-dependent weighted junction or coordinate chart is introduced. In
particular this is not a Cayley time-step fallback or a renamed rotor.

## 4. Finite typed rational isolation and its convergence

The frozen `polynomial_probe(p,x)` actually returns the signed difference of
two positive BRC endpoint observations:

    [p*x*x+2*x] - [p].

Thus bisection on a declared dyadic grid can bracket the unique nonnegative
root h(p) with rational endpoints separated by at most eta=2^(-b). At p=0,
use the existing exact zero-endpoint extension, not a fabricated tiny positive
root. Every comparison must retain p,x, the two endpoint values, source/kernel
pin and chosen interval side. Merely performing the polynomial in ordinary
Python arithmetic is not this actual comparison receipt.

The function h is increasing and 1/2-Lipschitz on [0,1]. An algebraic proof
avoids differentiating a trigonometric expression. For p2>=p1 and xj=h(pj),
monotonicity first gives x2>=x1, and subtraction of (2) gives

    [2+p1(x1+x2)](x2-x1)=(p2-p1)(1-x2^2)<=p2-p1.

If q_(m-1) is enclosed in [l,u], bracket h(l) from below and h(u) from above
using that same observer. Writing w_m for the resulting width gives

    w_2=0,    w_m <= w_(m-1)/2 + 2 eta < 4 eta.          (3)

For every finite m these enclosures therefore converge to its unique q_m as
b tends to infinity. All individual stages are finite. The repeated same-grid
zero enclosure at deep m does not defeat convergence: increase the *observer
depth in the new profile*, and (3) still holds. It does not change any frozen
runtime gate or normalize any dynamic state.

An alternative half-angle description is the algebraic chain

    c_(m+1)=sqrt((1+c_m)/2),
    s_(m+1)=sqrt((1-c_m)/2),

with nonnegative root branches and exact norm/sign relations. The frozen
`stage80.fixed_phase.square_probe` already compares weight*x*x against rhs via
actual positive paths, so a typed rational root-interval extension is possible
in principle. It is a target observer, never a projection or normalization of
state coordinates. But it needs its own sound interval propagation, stopping
and receipt contract; an ordinary sqrt call would violate the route. The
preferred design is (2)-(3), which directly reuses the existing polynomial
observer and avoids adding this unnecessary square-root interface.

## 5. Complete-carrier strict error is certifiable by rational inequalities

Execute a candidate native word on every basis column e_j, j=0,...,60, using
the actual `apply_word`. Fix orientation explicitly: W_ij is destination i
from source j. Preserve all dyadic numerators, denominators and word indices;
replay the reverse word on all columns. Exact orthogonality follows from the
certified letters, with the full-column replay binding the implemented word.

The simple certificate encloses every entry of U(q_m) and sums all squared
entry differences with rational interval arithmetic. The resulting rational
upper bound E_upper dominates ||W-U_m||_F^2. Accept only if

    E_upper < delta^2.                                  (4)

No numerical singular value or eigenvalue is needed. The strict threshold is
essential to effective certification. It is a sufficient full-operator test;
it is not claimed to accept every word with operator error below delta.

There is also a smaller equivalent observer once full orthogonality is bound.
Set

    A=W_00+W_11,   B=W_01-W_10,   C=sum_(j=2)^60 W_jj.

Then the **full** Frobenius error is exactly

    E(q)=2D-2[C+A*c(q)+B*s(q)].                          (5)

For 0<=l<=q<=u<=1, c is decreasing and s is increasing, so

    c(u)<=c(q)<=c(l),    s(l)<=s(q)<=s(u).

Use the signs of the exact rationals A and B to bound their products and get
a rational lower bound J_lower for C+A*c+B*s. Then

    E_upper=2D-2 J_lower

is sound and converges to E(q_m) as the isolation width tends to zero.
This trace identity does **not** discard off-diagonal or residual errors:
sum_ij W_ij^2=D and sum_ij U_ij^2=D incorporate every column. Without the
complete orthogonal-word contract, checking just the displayed corner/trace
would be unsound. The complete word and columns remain in the certificate;
the scalar is only a derived proximity observation.

Rational comparisons can be implemented by signed integer rails and positive
denominator cross products composed from the actual full-adder arithmetic.
The finite expression graph, all intermediate operands and strict final
comparison must be replayable. No operation updates a Shor state. Existing
permitted internal Fraction operations do not grant permission to label any
new rational evaluator as BRC without this correspondence.

### Optional total decision of the Frobenius threshold, including equality

The baseline below needs only the sound, eventually accepting strict test
(4). Nevertheless full equality is algebraically decidable here without an
unbounded undecided equality case. Let T=2D-2C-delta^2. Since 1+q^2>0,

    sign(E(q)-delta^2)
      = sign((T+2A)q^2 - 4Bq + (T-2A)).                 (6)

For m=2, q=1 is rational. For m=3, q has minimal polynomial x^2+2x-1;
reduce the quadratic in (6) to a linear polynomial. A zero remainder is exact
equality; a nonzero remainder cannot vanish at this irrational q, so refining
its interval eventually decides its sign.

For m>=4, q_m has algebraic degree 2^(m-2)>=4. One proof uses the primitive
2^m-th root zeta=c+i*s. Its real subfield has degree 2^(m-2). Since i is a power
of zeta, q=s/(1+c) lies in that real subfield; conversely c=(1-q^2)/(1+q^2)
generates it. Thus Q(q) is precisely that real subfield. This is an algebraic
degree proof, not a numerical root-of-unity calculation. A nonzero quadratic
in (6) cannot vanish. If all its rational coefficients are zero, equality is
decided immediately; otherwise convergent intervals eventually decide its
sign. All equality decisions reduce to exact rational coefficient comparisons.

This optional sign procedure and the simpler upper-certificate search have
the same sound acceptance direction. They need not be implemented together.
An exact operator-norm decision is unnecessary because Frobenius density and
the norm inequality already establish (1).

## 6. A fair enumeration with a proof of termination

A finite alphabet suffices: H4 on coordinates 0,1,2,3, one sign change at 0,
and all 60 adjacent swaps. It has 62 letters. Every letter is an involution;
H4 has determinant +1, while a sign change or swap has determinant -1. These
facts come from the actual primitive columns. All other indexed H4/sign/swap
operations are words in this alphabet by permutation conjugation.

Enumerate finite words in this alphabet and retain determinant-positive ones.
The determinant is tracked exactly by letter parity; no approximate determinant
test is used. To avoid an uncertified candidate blocking the search forever,
use the following explicit dovetail schedule:

    for n=0,1,2,...:
        b=n+3
        form the target enclosure at observer depth b
        for every determinant-positive word of length at most n:
            bind/reuse its exact full-column native execution
            compute the finite rational upper error at this b
            if E_upper < delta^2: return word and full certificate

Each stage contains finitely many words and finitely many actual comparisons.
Caching can remove repeated execution while retaining the source/word binding.
Deterministic heuristic or native seed candidates may be tried first, but they
do not replace this complete tail of the search or its fair stage progression.

By density, choose a finite positive-determinant word W_* with

    ||W_*-U_m||_F < delta/2.

Indeed operator-norm density suffices because ||X||_F<=sqrt(D)||X||_op; that
inequality is used only in the existence proof. Once n is at least the length
of W_*, that same word is revisited at every later stage. Its E_upper converges
to a number smaller than delta^2/4. Hence (4) eventually holds at a finite
stage and the algorithm terminates. A word exactly at the threshold cannot
stall the dovetail; it simply is not accepted by its current certificate.

Alternatively, the total comparison in (6) permits ordinary length-first
enumeration, with each candidate classified before moving on. The dovetail
version is simpler and does not need to implement the algebraic-degree branch.

Every finite word has an exact inverse: reverse its letters. Its approximation
obeys ||W^(-1)-U^(-1)||=||W-U|| for either operator or Frobenius norm. A target
in SO(61) is approximated by determinant-positive words only. Reflections are
not silently substituted for rotations; determinant-negative orthogonal words
are at operator distance exactly two from any positive-determinant orthogonal
matrix in their relative determinant-negative component.

## 7. Controlled direct sums and a finite Shor error allocation

For a retained control projector P, controlled execution is

    C(W)=(I-P) tensor I + P tensor W.

The existing native controlled catalog implements each letter with unchanged
bypass coordinates and preserved control labels. Composing controlled letters
gives C(W), because the orthogonal control blocks never mix. In particular

    ||C(W)-C(U)||_op = ||W-U||_op

when P is nonzero; a zero P gives zero error. Tensoring any untouched work or
reference system with identity also leaves the operator norm unchanged.
Even if a controlled lift has many repeated active blocks, it does not multiply
the operator error by their number. One must not use the base-word Frobenius
norm as an equality for the enlarged Frobenius norm; the lift uses the operator
bound already certified by (1).

For t>=3, the nonexact phase occurrence count is

    L=(t-1)(t-2)/2.

Leave m=2 as the exact native quarter turn, and for each needed m=3,...,t compile
with delta=epsilon/(2L). Reusing that word at all t-m+1 occurrences is valid:
all residual-bearing inputs are covered by the full-operator bound. Exact
modular permutations, H4/spectator operations, controls and readout conventions
remain unchanged. Unitary telescoping gives

    ||U_compiled-U_ideal||_op
       <= sum_(m=3)^t (t-m+1)||W_m-U_m||_op
       < L*delta = epsilon/2 < epsilon.                 (7)

If L=0, all required phase operations are already exact. The same argument
works with any declared positive per-occurrence budgets whose sum is below
epsilon. For normalized inputs, including arbitrary reference entanglement,
(7) bounds the terminal measurement TV by epsilon. Any common fixed classical
postprocessing can only reduce TV. This is an absolute complete-output bound,
not relative error on a rare conditional history.

For the semiclassical streaming view, retain the measured history and use the
already proved deferred-measurement/direct-sum equivalence; do not sum ad hoc
renormalized conditional-state errors. A finite adaptive retry transcript needs
its own sum of conditional round budgets. An unbounded retry policy needs a
summable allocation or another proof; a one-run epsilon bound is not silently
a bound on every indefinitely long transcript.

## 8. A portable executable interface and honest cost accounting

A suitable new interface takes `(m, delta_num, delta_den, dimension=61,
source_pins, optional_finite_budget, optional_cursor)`. It should return either
`CERTIFIED` with a complete word and strict certificate, or `PARTIAL` with an
honest resume cursor. Suggested certificate fields are:

- primitive source/kernel and alphabet definition; word execution order;
- dimension, determinant parity, complete signed dyadic columns and inverse;
- exact algebraic target definition and branch, m, rational requested delta;
- observer depth, all root brackets/probe receipts and interval convergence rule;
- full-column error observer inputs, rational E_upper, and strict delta^2 test;
- control/direct-sum scope, preserved residual coordinates and allowed operations;
- actual native calls, word/H4 counts, integer bit lengths and resource cap;
- execution/admission status distinct from mathematical termination.

The cursor must bind target, tolerance, source and alphabet hashes and record
the outer stage, word index and observer depth. A budget interruption preserves
completed certificates and resumes the first unprocessed pair; it does not
alter a tolerance, drop columns, invent a native receipt or infer no solution.
None of this requires a particular chat client to reason about or replay the
certificate semantics. Execution support and mathematical continuation remain
separate, as required by the portable-research protocol.

For a word of length ell with h H4 letters, denominators divide 2^h and exact
normalized column numerators need O(h) bits. A literal full-column replay has
O(D*ell) fixed local gate applications, plus exact integer cost; inverses add a
comparable amount. The number of words up to length ell is O(62^ell). At fixed
depth b, each inherited root bisection has O(b) probes, and a finite target
tower through m has O(m*b) probes, with exact operand bit costs additionally
counted. These are resource expressions in the search frontier, not a useful
bound on the frontier reached for a prescribed tolerance.

Density plus the strict semidecision provides a **total computable** algorithm
for each finite rational input. It does not here provide a useful closed-form
word-length bound in m and log(1/delta), a polynomial-time compiler, a practical
search budget, or a proof that a particular bounded attempt must succeed.
Nothing here removes the roughly N work-label cost or all other costs of a
classical Shor simulation. A finite logical word also does not establish an
autonomous six-axis physical layout, a new random source or native Born law.

## 9. What is closed and what remains an execution obligation

The symbolic gap from fixed-alphabet density to effective arbitrary finite
tolerance compilation is closed by the algebraic target, convergent typed
observer specification, full-column strict certificate, and fair enumeration.
The K33 finite-family TV obstruction does not apply to this growing family of
words: no width-independent positive minimum branch contraction was proved
over all finite words of unbounded length.

The current unit has not executed this new compiler. A concrete small returned
word still needs actual full-column/inverse replay and actual target-observer
receipts under the new profile. The existing fixed primitive and arithmetic
sources make those bounded obligations concrete; no new ordinary propagator
is needed. A future successful bounded run validates only its stated words,
targets, strict budgets and future-operation scope, while the universal claim
continues to rest on the separate author-level termination proof above.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
