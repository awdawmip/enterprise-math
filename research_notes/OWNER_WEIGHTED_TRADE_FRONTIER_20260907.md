# Weighted X6 zero-three-marginal arrays: eight positive cells force equal weights

Auxiliary work package: `/root/exact_solver`; local owner-directed mathematics,
not a registered task/claim, official review, or Foundation promotion.
Status: `PROVED_DERIVATION / MINIMUM_POSITIVE_SUPPORT_CLASSIFICATION`.
Current global read lease: `main@4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`.

**Result.** Let a finite rational array `h` on a raw six-coordinate product
have all 20 three-axis marginals zero and exactly eight positive spatial
cells. Then it has exactly eight negative cells, and every nonzero value is
`+lambda` or `-lambda` for one positive rational `lambda`. In particular,
eight positive cells with nine or more negative cells are impossible.
After bijectively labeling the two levels of each varying axis, its support
is a four-bit cube with the positive and negative parity classes as its two
sides. Additional physical axes are constant, duplicates, or complements
of those four bit-coordinate types.

This closes the proposed route of deleting an unusually light positive cell
from an eight-positive zero-marginal array. It does **not** determine the
optimal stability constant for all differences with at most seven positives.

## 1. Exact scope, source reuse, and the volume distinction

The object is a signed algebraic difference of finite nonnegative spatial
mass distributions, in one common anchor and labeled raw six-axis chart.
Support counts distinct collected spatial cells. No negative physical BRC
branch, branch-identity reconstruction, new native dimension, or coordinate
rotation is introduced. Coordinate-level bit labels below are reversible
combinatorial names, not native geometric operations. In the native X6
torsor these are legal integer-coordinate cells; zero extension outside an
originally declared legal subset, when needed, is only a proof device.

Actual reuse is of the support lower bound in
`OWNER_FREE_CANDIDATE_20260907.md` §3 and the positive-mass observer law:
if a raw marginal fiber has zero positive mass, it has no negative-side
mass either. The latter is the positive BRC fiber-sum law applied to the
two nonnegative sides separately. We extend that existing slicing method;
we do not create a solver or assert a new top-level tool family.

The previously proved minimum-**total**-support equal-amplitude lemma in
`OWNER_STABILITY_CONSTANT_FRONTIER_20260907.md` §3 is consistent with the
result, but is not used to assume the negative count. The new work below
first forces that count to be eight. Its final amplitude step can then use
that lemma; an independent cube-edge argument is also supplied.

The primary source [Ghorbani, Kamali, Khosrovshahi and Krotov,
*On the volumes and affine types of trades*, §2.1 and Lemma 4](https://arxiv.org/html/1810.02296)
defines integer coefficients as block
multiplicities and volume as a leg's cardinality including repetitions.
Its minimum-volume classification assumes volume `2^t`. Clearing the
denominators of a rational array with eight positive **locations** need not
give volume eight. That theorem alone therefore does not prove the present
claim. We make no external-priority or exhaustive-literature claim.
The proof here has three bounded parts: support slicing; eight-row binary
column structure; transfer of actual raw marginal constraints to negatives.

The distinction is substantive: at order one, on six binary coordinates,
`5 delta_0 + delta_(1,1,1,1,1,1) - sum_i delta_(e_i)` has zero one-axis
marginals, two positive locations, and unequal positive weights. No
all-orders equality assertion is inferred from the order-three result.

## 2. Lower marginals, binary axes, and balanced positive counts

Write `P={x:h(x)>0}` and `N={x:h(x)<0}`. All marginals on zero, one, or two
axes also vanish: extend their axis sets to three axes and sum the remaining
raw labels. Finiteness justifies every such sum.

Fix one physical axis `j`. Each nonzero slice `h_(j=b)` has all marginals
through order two zero. The existing support lower bound gives at least
four positive cells in that slice. Since `|P|=8`, the entire support uses at
most two values of axis `j`. A varying axis uses exactly two, with exactly
four positive cells at each value. A constant axis needs no bit label.

Fix two physical axes. Each nonzero fixed-two-axis slice has all marginals
through order one zero, so it contains **at least two positive cells**.
This assertion concerns support locations, regardless of their rational
weights or the number of negative cells in the slice.

For two varying axes, label their levels `0,1`. The table of positive-cell
**counts** has both row sums and both column sums equal to four, hence is

`[[a,4-a],[4-a,a]]`.

Every nonzero entry is at least two. Thus `a` is `0`, `2`, or `4`. For `0`
or `4`, one column of bit values on `P` is the complement or duplicate of
the other. In the remaining case their four pair patterns each occur twice.
No equality of the underlying masses has been used here.

Constants, duplicates, and complements on `P` hold on `N` as well. Indeed,
one- and two-axis marginal equality between the positive and negative
mass distributions forbids a negative cell in any pattern absent from `P`.
The same argument forbids an extra coordinate level appearing only in `N`.
Retain one representative from each varying column class modulo complement.
The full coordinate point, on both sides, is determined by these retained
bits. They still distinguish the eight positive spatial cells, and every
pair of distinct retained columns has all four patterns twice.

## 3. Three independent bit labels and affine characters

For any three retained columns, let `n_abc` be their eight positive-pattern
counts. Their three pair-count tables are all constant two. Solving these
elementary sum equations gives

`n_abc = 1 + alpha (-1)^(a+b+c)`.

The entries are nonnegative integers, so `alpha` is `-1`, `0`, or `1`.
The triple therefore either sees all eight patterns once, or sees precisely
one parity class, with its four patterns occurring twice.

There must be a triple of the first kind. Otherwise choose two distinct
retained columns. Every other retained column, by the parity alternative,
is their XOR or its complement. Together with the already discarded
duplicate/complement columns and constants, all physical coordinates would
then depend on only two bits. There could be at most four different positive
spatial points, contradicting eight. The case of fewer than three retained
columns gives the same contradiction directly.

Choose an all-once triple of actual distinct physical axes, and label `P`
bijectively by `u=(u1,u2,u3) in F2^3`. Consider any additional retained bit
column `z`. It equals one on four of these eight labels. Its pair counts with
each chosen basis column are all two, so that set of four labels contains
two zeros and two ones in each of the three coordinates. The XOR of its
four distinct vectors is consequently zero.

Four distinct vectors `a,b,c,d` in `F2^3` with `a+b+c+d=0` form an affine
plane: `d=a+(b+a)+(c+a)`, with the two displayed differences independent.
Such a plane is the solution set of one nonzero affine linear equation.
Thus every additional column is an affine parity function of the three
basis bits. Independently exchanging that axis's two bit labels removes
its affine constant. Duplicate/complement classes have already been removed,
so additional representative columns can only be

`u1+u2`, `u1+u3`, `u2+u3`, or `u1+u2+u3`, with addition modulo two.

This is a conclusion about eight actual rows and actual axis columns. It
does not assume a linear observation graph or import a binary coding model
as a native premise.

## 4. Actual three-axis zero patterns force the negative support

Take any negative cell and denote its three basis-axis bits by `v1,v2,v3`.
All other physical bits satisfy the constants and duplicate/complement
constraints already justified by one- and two-axis marginals.

If a representative pair-sum column, for example `z12=u1+u2`, is present,
look at the raw table for the **three distinct actual axes** representing
`u1,u2,z12`. Its positive support contains only patterns with
`z12=u1+u2`. Positivity and marginal equality therefore force the negative
cell to satisfy `z12=v1+v2` as well. The same holds for every present pair-sum.

If the triple-sum column `q=u1+u2+u3` is present together with some pair-sum
column, say `z12`, look at the raw table for the distinct actual axes
`z12,u3,q`. Its positive patterns satisfy `q=z12+u3`, so the negative cell
must satisfy that relation too. Combined with the preceding constraint,
this forces `q=v1+v2+v3`.

Hence, if at least one pair-sum representative is present, every coordinate
of the negative cell is forced to equal the coordinate of the unique
positive cell labeled `(v1,v2,v3)`. This contradicts disjointness of `P,N`.
If no additional representative exists, the same contradiction holds
because the three basis bits already determine the full physical point.

There is just one remaining possibility: the representatives are exactly
`u1,u2,u3,q`, with `q=u1+u2+u3` on `P`, and there is no pair-sum representative.
Thus `P` is the even parity class of a four-bit cube. Both `P` and `N` lie
in that cube after restoring physical constants, duplicates, complements,
and coordinate-level dictionaries. The map back to physical points is
injective because each of the four types has an actual representative axis.
Only the eight odd points remain available for `N`.

The support lower bound already gives `|N|>=8`, so `|N|=8`. This proves the
previously unresolved exclusion of eight positives with nine or more
negative cells, without assuming a bound on negative support in advance.

## 5. Equal amplitudes and the deleted-cell consequence

The total support is now 16, so the independently proved minimum-total-
support lemma applies. Alternatively, choose any three of the four actual
representative axes. Each resulting three-bit fiber contains exactly one
even and one odd cube point. All extra physical axes are fixed functions of
the four representative bits, so there are no other support points in that
fiber. Its zero marginal gives equal absolute weights on that cube edge.
Doing this for the four omitted representatives covers all edges of the
connected four-cube. Every nonzero weight therefore has one common absolute
value `lambda>0`.

If `W=sum_(P) h=8 lambda` and a positive point of weight `w` is deleted, then
`w=lambda=W/8`, and

`(||h||_1-w)/(20w) = (16 lambda-lambda)/(20 lambda) = 3/4`.

In particular `w/W=1/8 > 2/21`. No eight-positive zero-three-marginal array
can pass the proposed `w<2W/21` threshold or improve the established lower
bound one by deleting a light point. This closes that entire eight-positive
trade route, not merely the previously tested eight-negative subclass.

The optimal stacked stability constant for general `p(f)<=7` remains open
within the already proved interval `[1,111/20]`. This classification does not
claim that every candidate for that separate optimization arises by deleting
one point from a zero-marginal trade.

## 6. Bounded independent checks and remaining authority boundary

`owner_weighted_trade_20260907_check.py` checks the finite combinatorial
lemmas and actual raw BRC witnesses, without a linear optimizer:

- all balanced third columns compatible with two independent columns;
- all coordinate-balanced four-subsets of `F2^3` and their affine equations;
- all 15 possible additional-character sets on at most six representative
  axes, using direct raw projection joins to check the negative-support gate;
- four-bit parity embeddings with ordinary, repeated/complemented, and signed
  physical coordinate levels, including the deleted-point `3/4` ratio;
- the unequal order-one counterexample as a guard against an all-orders claim.

The result is saved in `owner_weighted_trade_20260907_check.json`. These are
small exact regressions of the stated lemmas and witnesses, not a search over
weighted supports and not a substitute for the proof in §§2–5. The existing
465-support exploration is not repeated. No remote mutation, publication,
identity allocation, or Foundation change was made by this auxiliary unit.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
