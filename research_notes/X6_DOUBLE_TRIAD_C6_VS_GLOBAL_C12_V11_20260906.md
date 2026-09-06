# X6 rotation V11: complementary triads give C6+C6, while global Ori6 rotation gives one C12

Status: `FREE_RESEARCH / EXACT TRIADIC-ROTATION SYNTHESIS / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_SIGNED_TRIADIC_DECOMPOSITION_BRC_V2_20260906.md`;
- `X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- `X6_GLOBAL_SIGNED_DIRECTION_C12_AND_C24_LIFT_V10_20260906.md`.
Checker: `experiments/x6_double_triad_v11_20260906/check_double_triad_vs_global.py`.

## 1. Six equal axis quanta have ten complementary-triad decompositions

For the uniform unsigned macro population

`D=(1,1,1,1,1,1)`,

P000 requires nonprimitive stability to decompose into two three-axis atomic units. The unordered underlying decompositions are precisely the partitions

`{S,S^c}`

of the six native axes into two complementary three-axis sets.

There are

`(1/2) C(6,3)=10`

such decompositions.

V2 already identified these as ten genuine BRC decomposition branches. V11 asks what frame dynamics each branch naturally supports.

## 2. Complementary triadic generators commute

Let `S` and `T=S^c` be complementary triads. Their signed generators act on disjoint coordinate sets, hence

`Q_S Q_T = Q_T Q_S`.

Choose one chirality on each triad:

`epsilon_S,epsilon_T in {+1,-1}`

and define

`H_{S,T}^{epsilon_S,epsilon_T}`

`=Q_S^{epsilon_S} Q_T^{epsilon_T}`.

There are four chirality choices for every unordered complementary decomposition.

Because the two factors commute and each satisfies

`Q_S^3=-I_S`,

`Q_T^3=-I_T`,

we obtain

`H^3=(-I_S)(-I_T)=-I_6`,

`H^6=I`.

So the composite is an exact full-six-axis half-turn root of order six.

## 3. Exactly 40 canonical complementary-triad frames

The positive-axis permutation of `H` is a product of two disjoint 3-cycles, one on `S` and one on `T`. Every unordered partition admits two orientations per block, giving exactly four oriented double-3-cycles.

Thus

`10 partitions * 4 chirality pairs = 40`

distinct canonical signed frames.

Conversely every positive permutation of cycle type `(3)(3)` determines its two complementary 3-cycles and their orientations, so these 40 are exactly one canonical signed representative over each of the 40 positive double-3-cycle permutations.

All are even positive-axis permutations and hence have

`Ori_6=0`.

This is the natural static frame class attached to the simplest six-force triadic decomposition branches.

## 4. Signed primitive-direction orbit topology is C6 + C6

On one complementary triad, `Q_S^{+/-1}` acts transitively on its six signed primitive directions

`{+/-E_i:i in S}`

as one C6 orbit. The complementary generator does the same on `T` and does not mix the two sets.

Therefore every canonical `H` acts on the full 12-element primitive signed direction shell as

`C6 disjoint_union C6`.

This is a full-six-axis frame transformation but **not** one globally mixed C12 phase orbit.

It retains the triadic decomposition as a dynamical separation into two signed-direction components.

## 5. Full signed double-C6 class has 640 frames

More generally take any signed permutation whose positive-axis permutation has cycle type `(3)(3)` and whose sign holonomy on **each** 3-cycle is `-1`.

Each positive double-3-cycle has:

- four sign assignments with negative holonomy on the first 3-cycle;
- four on the second.

So each of the 40 positive permutations has 16 signed lifts of this type, giving

`40*16=640`.

Every such frame satisfies

`g^3=-I`,

`g^6=I`,

and its primitive signed direction orbit decomposition is exactly `6+6`.

The 40 complementary-triad products are convenient canonical representatives; the remaining sign choices are their signed-frame gauge/conjugacy relatives.

## 6. The 640 form one R_triad conjugacy orbit

The positive double-3-cycle class is one `A6` conjugacy orbit: its S6 conjugacy class does not split because its centralizer contains an odd permutation exchanging the two 3-cycles.

For fixed positive cycle structure, sign-kernel conjugation acts transitively on sign assignments with fixed negative holonomy on each component cycle.

Therefore all 640 signed double-C6 frames form one conjugacy orbit under

`R_triad=(C2)^6 semidirect A6`.

The stabilizer order is

`23040/640=36`.

Thus, up to current triadic frame changes, there is one signed double-C6 frame type associated with a complementary-triad decomposition.

## 7. OUTER Cell lift: two disjoint C12 cycles

For either signed C6 direction orbit

`a_0,...,a_5`,

every consecutive macro edge has the two familiar shortest Cell realizations. Choosing OUTER defines

`m_r=a_r+a_{r+1}`

and the 12-state native Cell cycle

`a_0,m_0,a_1,m_1,...,a_5,m_5`.

Because the two complementary triads use disjoint native axis supports, their two OUTER Cell cycles are disjoint.

So the full-shell OUTER topology of a complementary-triad frame is

`C12 + C12`

on 24 distinct native Cells.

This is a concrete path-level image of the underlying `C6+C6` signed-direction decomposition.

## 8. Contrast with the global odd C12 class

V10 classified global primitive-direction-transitive frames. Their signed direction topology is

`C12`

and they necessarily have `Ori_6=1`.

Their all-OUTER Cell lift is one connected

`C24`

cycle on 24 distinct native Cells.

Thus the two exact upper structures are:

### Triadically decomposed full-six-axis frame

- static charge: `Ori_6=0`;
- signed direction topology: `C6 + C6`;
- OUTER Cell topology: `C12 + C12`;
- canonical source: one of ten `3+3` force/decomposition branches plus two chirality choices.

### Globally mixed signed-direction frame

- static charge: `Ori_6=1`;
- signed direction topology: one `C12`;
- OUTER Cell topology: one `C24`;
- canonical source: signed 6-cycle with negative holonomy.

This is an exact combinatorial/topological distinction inside the current frame/path theory.

It does **not** prove that physical stability prefers the first or that physical global rotation prefers the second. Those are law-selection questions.

## 9. BRC interpretation of the six-force branch

At `D=(1,...,1)`, Boolean macro stability records only that a triadic decomposition exists.

The unordered BRC layer has ten complementary decompositions. Adding a chirality choice on each atomic triad gives 40 canonical frame branches.

A future observer that asks only “stable or not” may discard this multiplicity. A future operation that evolves each triad by its local Q generator cannot: different decompositions pair different axes into the two C6 subsystems.

Hence the tenfold triadic decomposition provenance becomes direct rotation-dynamical provenance.

This supplies a concrete future-operation witness for why the decomposition BRC cannot generally be collapsed to Boolean stability.

## 10. Relation to global C12 path multiplicity

A single double-C6 direction orbit has six macro edges and therefore

`2^6=64`

concatenated shortest branch histories over one frame period. The two complementary direction components together have a 12-bit branch word and hence `2^12=4096` joint shortest full-shell histories if both are tracked.

The global odd C12 frame also has twelve macro edges and 4096 shortest histories, but their connectivity differs:

- double-triad OUTER section: two C12 Cell components;
- global-C12 OUTER section: one C24 Cell component.

Thus equal raw branch cardinality does not imply equal relational topology.

## 11. A conditional bridge across Ori6

V8/V9 show that adding any one admissible `Ori_6=1` frame event connects the static odd coset to the current even group.

V11 shows what such a change can do to full-shell phase connectivity: it can connect a triadically separated `C6+C6` regime to a globally mixed `C12` regime.

This is a structural possibility, not a physical transition theorem. A concrete event law must still specify state/context, path section/weights and time/internal coupling.

## 12. Verification

The exact checker verifies:

- ten complementary 3+3 decompositions;
- four chirality choices per decomposition and exactly 40 distinct canonical frames;
- commuting complementary Q generators;
- `H^3=-I`, `H^6=1` and `Ori_6=0`;
- exact `C6+C6` primitive-direction topology;
- all 640 signed double-C6 frames and their one `R_triad` conjugacy orbit with stabilizer 36;
- two disjoint 12-Cell OUTER cycles for a representative;
- one connected 24-Cell OUTER cycle for the V10 global odd representative.

No Foundation promotion or physical-law claim is made.
