# Constructive four-square phase words on the unchanged 61-mode carrier

Status: AUTHOR_SYMBOLIC_CONSTRUCTION / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. Root proposed this direction; the present document is a shared
author cross-check and derivation. No new four-square search, normal vector,
phase word, target refinement, Shor state or ideal numerical reference was
executed for this unit. The currently frozen fair compiler is unchanged.

Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.
Control Source `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen executable primitive source `0852cad130c1d877174d235687cf60c19f318c58`.

## 1. Result and what makes it stronger than blind word enumeration

For each inherited exact phase index m>=3 and rational tolerance delta>0,
there is a direct finite integer construction of a native word W on D=61
coordinates with

    det W = +1,   ||W-U_m||_op <= ||W-U_m||_F < delta.

It needs only the unchanged exact H4/sign/swap primitives, the existing
algebraic polynomial observer, four-square completion, and the already shipped
`stage80.fixed_phase.synthesize_unit` algorithm. Four new retained coordinates
suffice for the completion; dimension need not grow with accuracy.

Choose an integer B>=2, put S=2^B, and require

    S > 128/delta^2.                                      (1)

Use observer depth h=B+4. The indexed native word has length at most
`10B+124`, with at most `2B` H4 letters. Even after translating every indexed
letter into the precise 62-letter alphabet, its length remains O(B), with an
explicit conservative bound below. A completely elementary four-square search
takes O(delta^-4) candidate tuples times polynomial bit arithmetic. This is a
polynomial in inverse tolerance, not a polynomial in its binary input length.

The construction thus supplies a concrete candidate and a known sufficient
observer horizon; it need not search 62^word_length candidates. Its intended
certificate still replays every full column and inverse through the existing
actual executor. The separate fair compiler remains a valid fallback and is
not silently replaced by an unexecuted constructor.

## 2. The half-angle and orientation are exactly the inherited ones

Let q_2=1, and let q_j be the positive root of

    q_(j-1) q_j^2 + 2q_j - q_(j-1) = 0.

As in the existing target contract, define

    c(q)=(1-q^2)/(1+q^2),   s(q)=2q/(1+q^2),
    U_j = [[c(q_j),s(q_j)],[-s(q_j),c(q_j)]] direct-sum I59.

These expressions are symbolic target definitions and certificate observers;
they are never inserted as a dynamic propagator. The target recursion gives
`U_(m+1)^2=U_m`. Write

    c*=c(q_(m+1)),  s*=s(q_(m+1)),
    z*=(c*,s*,0,...,0),  D0=diag(1,-1,...,-1).

Both leading coordinates are nonnegative and `||z*||=1`. Direct symbolic
multiplication gives

    D0(2z*z*^T-I)
      = [[c*^2-s*^2, 2c*s*],[-2c*s*,c*^2-s*^2]] direct-sum I59
      = U_m.                                             (2)

Thus the required root index is m+1, and the order of the two factors is D0
on the left. Reversing them would produce the opposite phase. The completion
scheme does not choose a sign from measured history, an unknown order or a
hidden factor. The exact m2 quarter turn remains available directly.

## 3. Lower endpoints produce a nonnegative integer remainder

Obtain the closed dyadic enclosure `[l,u]` of q_(m+1) at depth h=B+4 from the
existing actual polynomial-probe recursion. Its proved width satisfies

    0 <= u-l < 4*2^-h = 1/(4S).                           (3)

On [0,1], c decreases and s increases; both are 2-Lipschitz. These bounds can
be checked algebraically without a trigonometric or square-root evaluator:

    c(x)-c(y)=2(y-x)(x+y)/((1+x^2)(1+y^2)),
    s(y)-s(x)=2(y-x)(1-xy)/((1+x^2)(1+y^2)),  x<=y.

The first quotient factor `(x+y)/((1+x^2)(1+y^2))` is at most one, since
`1+x^2+y^2-x-y >= 1/2`; the second is also at most one.

Set

    C_low=c(u), S_low=s(l),
    a0=floor(S*C_low),  a1=floor(S*S_low),
    K=S^2-a0^2-a1^2.                                     (4)

Since `0<=a0/S<=c*` and `0<=a1/S<=s*`, K is a nonnegative integer. Neither
coordinate is rounded to the nearest grid point: the lower choices are what
guarantee a completable norm deficit.

Write `d0=c*-a0/S` and `d1=s*-a1/S`. Equations (3)-(4) give

    0<=dj<1/S+2(u-l)<3/(2S).                              (5)

Consequently

    K/S^2 = 2(c*d0+s*d1)-(d0^2+d1^2)
           < 3(c*+s*)/S <= 3*sqrt(2)/S < 5/S,
    0 <= K < 5S.                                         (6)

These bounds also cover l=0; a zero lower endpoint must be retained literally.
The proof never replaces it with an invented positive root.

## 4. Four-square completion and a finite, factor-free search

Lagrange's four-square theorem supplies natural numbers a2,a3,a4,a5 with

    a2^2+a3^2+a4^2+a5^2=K.

For a primary implementation source, the official Mathlib development states
`Nat.sum_four_squares` and includes its complete Lean proof, using a prime
case, descent and Euler's composition identity. The inspected source is pinned
at commit `5e0c4e5239cb0a2d86d68a884bf52cfd963fce22`:
[official source](https://github.com/leanprover-community/mathlib4/blob/5e0c4e5239cb0a2d86d68a884bf52cfd963fce22/Mathlib/NumberTheory/SumFourSquares.lean),
[official theorem documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Nat.sum_four_squares).
This is a cited mathematical dependency, not a claim that Lean was run locally
or that this project has obtained formal admission.

No factorization of K, N, or an unknown Shor order is required in the proposed
executor. A deliberately simple total search is:

1. Find the largest integer R with R^2<=K by a bounded integer binary search.
2. Enumerate all four tuples in `{0,...,R}^4` in a fixed order.
3. Return the first tuple whose four squared values sum exactly to K.

The theorem proves this finite search contains a witness. Its witness is
independently checkable by four multiplications and additions; those are not
outsourced to the theorem source. For K=0, return four zeros immediately.
The tuple count is `(R+1)^4=O((K+1)^2)=O(S^2)`. The enumeration can be interrupted
with a tuple cursor and `PARTIAL`; a resource interruption must not be reported
as a completed phase or as evidence that the theorem failed.

A faster meet-in-the-middle or descent algorithm is optional, not a premise.
The existing binary-square completion is not a substitute for this fixed-D
claim: its number of coordinates can grow with B. Conversely the already
proved fair-word compiler is a separate fixed-D fallback if this constructor
is not implemented; it does not make an unexecuted four-square search a run.

Define the complete 61-coordinate unit vector

    z=(a0,a1,a2,a3,a4,a5,0,...,0)/S.

Every coordinate, including the four residual coordinates, remains in the
state space. They are not postselected, projected out, reset or renormalized.
The exact norm equality is `sum(ai^2)=S^2`.

## 5. The shipped dyadic-unit synthesizer terminates on this input

The actual frozen source `stage80/fixed_phase.py`, function `synthesize_unit`,
already accepts an integer vector v satisfying `sum(v_i^2)=4^B` and synthesizes
a word G with `G(v/2^B)=e0`. Here is its complete descent invariant.

At a denominator level k>=1, the invariant is `sum(v_i^2)=4^k`. Reducing modulo
four shows the number of odd coordinates is a multiple of four. Divide the odd
indices into quartets. Within each quartet, negate the coordinates congruent
to 3 modulo 4; every remaining odd coordinate is then 1 modulo 4. In the actual
Walsh H4 column catalog, the integer row patterns contain either four plus
signs or two plus and two minus signs. Every resulting row sum is divisible
by four. Applying the actual H4/2 therefore makes each of those four output
coordinates even. The previously even coordinates outside the quartet remain
even. The actual operation preserves the squared norm.

After processing all odd quartets, all coordinates are even. Dividing every
integer numerator by two while reducing k by one is an exact representation
change of the same rational state; it discards no norm or mode. The invariant
becomes `sum(v_i^2)=4^(k-1)`. After B levels, an integer vector of norm one has
one nonzero entry, equal to +1 or -1. At most one native sign and one swap send
it to e0. The shipped function finally executes its word and inverse to check
the complete original vector exactly.

Here the nonzero support is initially contained in coordinates 0 through 5.
The algorithm only operates on odd indices already in that support, so it
never introduces a nonzero coordinate outside these six. Its odd count at a
level is therefore only 0 or 4. At most four signs and one H4 are used per
level, plus two final routing letters:

    length(G)<=5B+2,      H4_count(G)<=B.                  (7)

This argument checks the actual algorithm rather than invoking a generic
universal-gate theorem. It also handles negative intermediate coordinates:
their residues are aligned modulo four with the exact native sign primitive.

## 6. Compose the full native phase and certify all residual directions

Let the temporal word for G be g. The exact sequence used by `FixedRotor` is

    g ; D0 ; reverse(g) ; D0,

where each D0 is the 60 native sign changes at indices 1 through 60. As a matrix
this temporal sequence is

    W = D0 G^T D0 G = D0(2zz^T-I).                       (8)

Its determinant is +1, regardless of the determinant of G. In dimension 61,
D0 itself has 60 negative eigenvalues, but no parity special case is needed:
the product contains D0 twice. All columns outside the six-coordinate support
are fixed by the final phase, because the two negative signs cancel there.
The four completion modes inside the support are retained exactly.

From (7), the literal indexed-native phase has

    length(W)<=10B+124,       H4_count(W)<=2B.             (9)

For the specific 62-letter alphabet, indexed letters require only fixed
routing words. An H4 on any ordered quartet among six coordinates is a
permutation conjugate of H4 on 0,1,2,3; a permutation of six positions needs at
most 15 adjacent swaps, so its routed H4 costs at most 31 letters. A sign on
index at most 5 costs at most 11 letters; the final swap costs at most 9.
Thus the routed G length is at most `75B+20`. Each full D0 costs at most
`sum(j=1..60)(2j+1)=3720` letters by separate routing of every sign. Hence

    length_62(W)<=150B+7480.                              (10)

This deliberately loose constant shows that a fixed alphabet really suffices;
changing B does not enlarge the alphabet or change any primitive coefficient.

For implementation, `synthesize_unit` can supply g directly, followed by the
literal sequence above and the existing full-word certificate. `FixedRotor`
also performs complete column checks of this same word, but its rank-one
quotient must not be confused with a newly inserted ideal target propagator.
The already frozen compiler verifier should still run every actual basis
column and inverse for a newly constructed candidate.

## 7. Explicit whole-carrier error and a sufficient existing-observer depth

The unit-vector dot product gives an exact identity independent of which
four-square witness is chosen:

    ||z-z*||^2 = 2-2(z dot z*) = 2(c*d0+s*d1) < 5/S.       (11)

For unit z,z*, expand the projector difference as

    zz^T-z*z*^T = z(z-z*)^T + (z-z*)z*^T.

Each rank-one term has Frobenius norm at most `||z-z*||`. Multiplication by
D0 preserves either relevant norm. Equations (2),(8),(11) therefore imply

    ||W-U_m||_op <= ||W-U_m||_F <= 4||z-z*||,
    ||W-U_m||_F^2 < 80/S.                                (12)

There is a tighter rank-two identity, but it is unnecessary. The bound in
(12) is already full-carrier, including arbitrary residual-bearing input.

The current trace-based certificate can accept the constructed word at a
known finite horizon, instead of relying on unspecified future refinement.
Use the q_m enclosure at the same depth h=B+4. Its width w is less than 1/(4S).
For the actual orthogonal W, the certificate coefficients satisfy `|A|<=2`
and `|B|<=2`. Each monotone c/s endpoint differs from its exact value by at
most 2w. Therefore the trace upper bound's additional looseness is at most

    E_upper - ||W-U_m||_F^2
      <= 2(|A|*2w+|B|*2w) <= 16w < 4/S.

Combining this with (12) gives

    E_upper < 84/S < delta^2                             (13)

under the convenient parameter choice (1). Thus the existing strict
positive-path margin observer is sufficient without a new acceptance rule.
Its target is still q_m; q_(m+1) is used only to construct the candidate normal.
No equality at the requested tolerance can stall this explicit construction.

## 8. Which arithmetic must become actual before this is executable evidence

This document is symbolic; reading the four-square theorem or the old helper
does not count as running them on new inputs. A future implementation needs
the following concrete source-preserving maps.

- New h-depth root endpoints must be actual `polynomial_probe` executions with
  retained endpoint receipts, as in the current compiler. This is a new
  exact-target observer horizon, never an alteration of old target32/vector64.
- The two floors can be found by integer binary search with positive-path
  polynomial comparisons. For example a0 is certified by comparing
  `a0*(1+u^2)` and `(a0+1)*(1+u^2)` to `S*(1-u^2)` on signed rails; a1 uses
  `2*S*l` against the positive denominator `1+l^2`. No ordinary numerical
  square root or trig evaluator is needed.
- K, tuple square sums, equality, counters and floor searches can use the
  existing actual full-adder integer transducers or the explicit signed
  positive-path arithmetic observer. Python arithmetic alone must not be
  labeled an actual BRC search. The four-square theorem is only an existence
  justification; the returned tuple must pass an actual norm certificate.
- The proposed integer normal, denominator level trace, generated native word,
  all 61 complete columns, inverses and existing strict phase certificate must
  be retained together. The old `brc_square_budget` can verify the final norm;
  the current complete-word certificate observes the resulting actual word.
- Source and target bindings, budgets and tuple/phase cursors must survive
  interruption. Resource exhaustion yields `PARTIAL` and a precise cursor.

These are compositions of existing arithmetic and native-word families;
they do not require a new variable-weight runtime gate or a hidden-order
oracle. They remain future execution obligations, not automatically granted
receipts from a source lookup.

## 9. Cost and the limited polynomial statement

Take the least B>=2 satisfying (1). Then S is O(1+delta^-2), B is
O(1+log(1/delta)), and the elementary four-tuple search uses
O(1+delta^-4) tests on O(B)-bit integers. Schoolbook typed multiplication,
comparison and addition contribute polynomial factors in B. Root isolation
through m+1 uses O(mh) actual fixed-degree polynomial probes; the input bit
sizes are O(h), and h=B+4. The native word and full-column replay costs are
polynomial in B for fixed D=61. These bounds remove the unquantified search
frontier of the density-only compiler for this one-parameter target family.

If t=O(n), L=O(n^2), and a one-run error budget epsilon=Theta(1/n) is split as
delta=epsilon/(2L)=Theta(n^-3), then the crude four-square candidate tests per
phase are O(n^12), and at most O(n) phases give O(n^13) such tests, with further
polynomial logarithmic-bit factors. This is a theoretical polynomial bound
for this phase compiler, not an efficient implementation claim.

The overall classical Shor simulation still has the work-state and retained
amplitude costs, and the current Wilson prime-leaf baseline still costs O(N)
modular products. Nothing here proves polynomial-time classical factoring,
reduces all those costs, derives a physical Born law, or executes an autonomous
geometric layout. The immediate frontier is a separately registered bounded
constructor plus its actual integer and full-column certificates.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
