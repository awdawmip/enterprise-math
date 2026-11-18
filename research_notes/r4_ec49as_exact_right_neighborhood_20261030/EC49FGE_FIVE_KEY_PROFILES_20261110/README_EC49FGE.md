# EC49FGE — exact five-full-key profile classification for the original 24 BRC signatures

Date: 2026-11-10. Mode: author-side TASK_RESEARCH. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Predecessor EC49FGD at ae24f0cfeebc2d3d4692a6e5676ce98f2ecdea90. No native Result or independent Driver admission is asserted.

## Mathematical model

H2, H3, H5, H9 require observations {16,32}; H4, H6, H7, H8 require {1,2,4,8}, for exactly 24 demands. Choose a legal original-nine-state-DFA operation word of each required length over a,c,d,e,f,g, with endpoint (+2,0,0,0,0,0). Ordered native signed-six-axis microsteps:

    a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1)
    e=(3,1,1,-3), f=(1,-1), g=(2,-2).

The raw complete cache key is K=(number of +1, +2, +3 microsteps). Zero components are permitted, e.g. H2 fe has (3,0,1). The endpoint condition is equivalent to count(e)=count(a)+1. The cost is the number of distinct nonempty ordered signed-native microstep prefixes across all 24 chosen words.

## Result A: exact five-key profile classification

The minimum number of distinct raw complete keys for all 24 demands, ignoring native-prefix cost, is exactly FIVE. Every five-key realization uses exactly one set among these 16:

    Base = {(3,0,1), (2,1,1), (3,1,1)}
    A = {(3,3,1), (4,2,1), (5,1,1), (5,1,2)}
    B = {(5,5,1), (6,4,1), (7,3,1), (7,3,2)}
    All 16 sets = Base union {a,b}, a in A, b in B.

Finite exhaustive proof: enumerate all six-letter continuations of original nine-state observer at each H2..H9, prune the absorbing dead state, and require both the demanded terminal signature and count(e)=count(a)+1. This yields exactly 178,850 admissible demanded words and 94 distinct raw full keys. Assign to each key the exact 24-bit set of demands it can serve. H2 signatures 16 and 32 respectively force (3,0,1) and (2,1,1). No pair of additional keys covers the other 22 demands; exactly 16 triples of additional keys cover them, precisely the Cartesian family above. The witness of Result B attains five keys. The standard-library script VERIFY_EC49FGE.py reproduces every enumeration and checks the Cartesian family.

## Result B: one five-key profile has exact minimum 112 native edges

Fix K* = {(3,0,1), (2,1,1), (3,1,1), (4,2,1), (6,4,1)}. For all 24 original demands, allowing every legal word with key in K*, full finite integer optimization gives minimum C_native = 112. The model uses 10,901 nonempty operation-prefix variables, 1,904 sibling-overlap discounts, 14,728 linear constraints, and 33,786 nonzeros. Actual SciPy/HiGHS result: status=0; primal=112; dual bound=112; MIP gap=0. The independently reconstructed literal signed-native witness also has exactly 112 edges:

    H2:  16=fe        32=ge
    H3:  16=feg       32=gef
    H4:   1=gefd       2=fegd       4=fegc       8=gefc
    H5:  16=feggf     32=geffg
    H6:   1=gefddd     2=fegddd     4=fegccc     8=gefccc
    H7:   1=gefddgf    2=fegddgf    4=fegccfg    8=gefccfg
    H8:   1=geffgfgd   2=feggffgd   4=feggffgc   8=geffgfgc
    H9:  16=feggffgfg 32=geffgfggf

The standard-library audit verifies all required observer signatures, endpoint and raw keys, 24 lengths, and rational nine-history rank nine for each H2..H9. It directly recomputes the union of literal signed microstep prefixes, not an operation-length proxy.

### Why the integer program measures literal native-prefix cost

There is a binary activation x_v for every nonroot operation-prefix Trie node, with x_child <= x_parent. Every signature demand has at least one selected terminal node. The initial objective charges length(last operation)*x_v for each active node. At any parent, the children c,f share exactly one initial native microstep +1, while d,g share exactly one initial native +2; all other sibling first microsteps differ. Introduce y_cf,y_dg <= each corresponding child activation, and subtract y from the objective. Minimization selects discounts when both siblings are used. By the previously established EC49FBS operation/native-prefix counting identity, the integer objective equals the true literal native prefix count. VERIFY_EC49FGE_MILP.py constructs the entire finite word pool and solves this model; its zero-gap MIP result is solver-assisted finite evidence. A separate exact rational dual certificate remains a possible strengthening of the 112 lower-bound audit.

## Consequence and next discriminating unit

The mother target is at most FIVE raw complete keys AND at most 93 native prefix edges. This result reduces its key combinatorics to only 16 exact five-key profiles. The specified K* profile is excluded from the 93-edge target by its 112-edge finite optimum. The remaining FIFTEEN profiles are the next exact optimization units. The earlier EC49FGD 93-edge solution uses eight raw keys and remains a valid relaxed witness; it is not a mother-target solution.

Reproduce using Python standard library: python VERIFY_EC49FGE.py. Reproduce the full scoped MIP: OPENBLAS_NUM_THREADS=1 python VERIFY_EC49FGE_MILP.py (SciPy/NumPy). Proof standards: finite-domain key support theorem independently enumerated; fixed-profile minimum is computational MIP with attained witness and zero solver gap; native Source Result and independent Driver review are outstanding. P000, ACTIVE worldview and frozen scientific inputs are unchanged.
