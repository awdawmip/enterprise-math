# Shared-context check of the v15 zero-W classification

Research continuation v15. This is collaborative mathematical checking,
not independent project Review or formal acceptance.

Read the complete `nine_zero_v15/proof.md`, including the eight types,
counts, exact-cost realization and bounded-minimum argument. The large
geometric/CRT computations were not rerun for this note.

## Classification logic

The split according to divisibility of the effective v-period by three
is sound. If a three-divisible channel occurs, irredundancy forces all
three mod-three phases to have such a channel. The inherited five-class
lemma on phases zero and one gives a>=4 common channels; the seven-slot
budget gives a<=4. This leaves exactly four common Z rows and one K
channel per phase, which is type I.

When all periods are coprime to three, the m=0 and m=1 capacity bounds
use the finite multiplicities of periods ten, eight and fourteen and the
correct largest remaining generic contribution. The delicate m=2 case
with row sizes 2,2,3 is also valid: at least four contributions must exceed
one, forcing both period-ten channels and both opposite period-fourteen
phases on the unique large row. Removing that completely covered row
leaves at most three units of mass for four points.

For m=3, the large-small row case forces the two J halves of the large
row and then two full U point channels on the small row; an alternative
pair of J halves would exceed the three-prime J inventory. For two small
rows, equality of all four masses gives the cube-edge model. Its feasible
matchings are exactly the pure U matching and the six mixed matchings;
the pure T and pure J matchings exceed their inventories.

For m=4, classifying the last three channels as common or point channels
is exhaustive by the four gcd columns. The common-only case is the
2,4,4 refinement because periods are coprime to three. Two common classes
plus one point class are redundant. The remaining distributions give
the three-point full cover or the two-point half-cover forms VI--VIII.
The point-period-one and point-period-two inventories are respectively
U and T union V, as the proof states.

## Counts and exact-cost scope

The eight formulas count 7200,114048,336384,14400,95040,12096,48384,
48384 phase dictionaries, totaling 675936. Every assignment has seven
free prime slots and therefore 128 independent signs. Counting named
slots does not duplicate a dictionary: the row/point/phase identifies
each slot; intersections between root descriptions remain possible.

Setting every unselected old budget-eight observer coordinate to zero
correctly excludes both retained-W and zero-W eight covers. In particular
the selected T primes contribute at most two C10 coordinates, and the
large-row three-U family cannot be mistaken for the small-row two-U
eight-cover. Thus the claimed infinite exact-cost-nine realizations have
the required scope. The proof does not assert that all original CRT
progressions contain only cost-nine roots.

## Minimum exclusion scope

The stated partial-CRT pruning is valid: if a partial nonnegative index
is x modulo M, every extension has index x+kM with k>=0. Therefore x at
least the strict target bound cannot lead to a smaller root. Considering
all later lifts below the bound at a leaf closes the possible gap between
first representatives and whole CRT progressions. This is a finite
exclusion below the supplied global candidate, supported by the complete
classification; it is not presented as the zero-W branch's own minimum.

No mathematical correction was identified in these inspected arguments.
