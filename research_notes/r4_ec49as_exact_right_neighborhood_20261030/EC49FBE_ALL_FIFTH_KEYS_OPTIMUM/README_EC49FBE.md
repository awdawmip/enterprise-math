# EC49FBE — Exact fifth-key classification and 127-edge theorem

Date: 2026-11-05 (Asia/Shanghai). Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Status: AUTHOR_FINITE_THEOREM / EXACT_INTEGER_OR_MASK_DP_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Statement
Within the frozen seven-operation native signed-six-axis BRC model, fix the early horizon word sets:
 H2: de, ec, fe; H3: feg, gef; H4: fegg, gefg; H5: feggg, gefgg.
These occupy 39 ordered signed primitive-prefix edges and four complete six-axis positive-step cache keys (3,0,1), (3,1,1), (3,2,1), (3,3,1), all with trailing zeros.
Let H6–H9 independently choose arbitrary legal ordered-word subsets, subject to a global budget of at most five complete keys, signed endpoint (+2,0,0,0,0,0), and each horizon's nine-history observation rank equal to nine. Then the exact least total number of distinct ordered signed primitive prefix edges is 127. The fifth key (6,4,1,0,0,0) is the unique key achieving that minimum.

## Exhaustive seven-key classification
For length h, put e=#e, a=#a, r=#c+#d, f=#f, g=#g. The native endpoint condition is e=a+1. A complete positive-step cache key (x,y,z,0,0,0) has x=r+2e+f, y=r+g, z=e, so a=z-1, e=z, r=x+y-h-1, f=h+1-y-2z, g=h+1-x must be nonnegative integers. Operation b cannot occur because it contributes negative axis E2 without a compensating positive primitive step.
The four early keys satisfy x+y<=6, whereas H6–H9 each need x+y>=h+1>=7. Thus every later window must use the SAME single fifth key. The exact count-state observer DFA over (#a,#e,#(c+d),#f,#g,nine-state-observer) gives single-window rank-nine key counts H6=28, H7=43, H8=62, H9=86. Their four-way intersection has precisely seven fifth-key candidates.

| Fifth key (last three coordinates 0) | Exact total primitive edges |
| --- | ---: |
| (5,5,1) | 140 |
| (6,4,1) | **127** |
| (6,5,1) | 166 |
| (7,3,1) | 135 |
| (7,3,2) | 154 |
| (7,4,1) | 162 |
| (7,5,1) | 182 |

## Complete finite proof algorithm
For each key, explicitly generate every ordered word compatible with the operation-count constraints, including every c/d orientation. Check exact native signed terminal displacement and six-axis positive-step cache key; run the frozen nine-state observation transition to determine six-bit signature s. EC49FAR's rank-nine condition on the OR of selected signature bits m is (m&18)&&(m&20)&&(m&33)&&(m&40). Encode for each word a four-bit clause-hit mask, shifted by four for each of H6,H7,H8,H9. Full 16-bit mask 65535 is equivalent to all four rank requirements.
Build a trie in the ordered signed native primitive steps (NOT scalar displacement or an unsigned macro-operation trie), marking the 39 early edges free. At each node v, D_v[M] is the minimum newly paid edges for the OR of the terminal masks M selected below the node. Start D={0:0}; selecting terminals at the node adds their full available OR-mask at zero; combine children by D_new[a|b]=min(D_new[a|b],D_old[a]+D_child[b]); pay one on each nonfree incoming edge iff its subtree selection is nonempty. Induction on trie depth proves this computes the exact minimum over ALL selected terminal-word subsets, including cross-window prefix sharing.
The actually executed VERIFY_EC49FBE.py implements the complete unpruned integer DP for all seven candidates. EXACT_REPORT_EC49FBE.json retains actual candidate counts, signature histograms, native trie sizes, OR-convolution pair counts and exact minima. The (6,4,1) key result was separately crosschecked by a second pure-Python unpruned DP and an independent C++ dominance-reduced DP in EC49FBD.

## Achieving 127 edges
H2: de ec fe
H3: feg gef
H4: fegg gefg
H5: feggg gefgg
H6: ecgcfc fegccc fegddd gefddd
H7: ecgcffg fegccfg fegddgf gefddgf
H8: fegggffc fegggffd gefggffc gefggffd
H9: fegggffgf gefggffgf
Literal signed native prefix recount and complete rank/key checks give cumulative edges 22,31,35,39,85,97,121,127. The explicit construction attains the seven-key lower bound.

## Provenance and continuation
Previous EC49FBC Git source 954c3cac68a8d21a905e5aa8b89a5a56e9cc807f, EC49FBD checked intermediate 770dbbb5171689837bc3fcf2461c59b274fd95fc. Current normative snapshots were read from global main 42c72244d7a26470aed0e2a96efc9ee3e09635e6 and EM main 0ce66db2fed5b5e2135258ef904786ae84cd85e5. Frozen science pin retained. P000/ACTIVE worldview unchanged.
Native CLAIM, Result, and independent Driver admission require their separate authority; this is durable author-side exact finite research evidence.
Next EC49FBF: change early H2/H3 or H4/H5 and jointly optimize key schedules, comparing full costs to the existing independent 94-edge upper witness; seek a 93-edge construction or a stronger broad-family lower bound.
