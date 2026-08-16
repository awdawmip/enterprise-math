# R059D Stage Q — Cross-Scale Torsor Synchronization

Researcher-ID: `EM-R059D-9C6B2A`
Taskbook source: `c13713d68635b51c78e9fd3e589a63230b441de5`
Frozen parent: `a621f80d0294f5a5139eb4a2ed26e552e6368b18`

## Disposition

`BRC_RELATIVE_CONSTRAINT_SYNCHRONIZATION_ESTABLISHED`

Also established:
`GLOBAL_Z2_TORSOR_AMBIGUITY_ESTABLISHED`;
`ONE_ANCHOR_GLOBAL_COMPONENT_INITIALIZATION_ESTABLISHED`;
`ODD_PARITY_CYCLE_INCONSISTENCY_DETECTED`;
`CROSS_SCALE_POST_CREDIT_FIXED_POINT_ESTABLISHED` on finite acyclic pairwise-XOR factor trees;
`CROSS_SCALE_LOCAL_PROPAGATION_INSUFFICIENT` for unary-only propagation on cyclic parity systems without a cycle summary;
`CENTERED_GAP_TAU_ODD_CARRIER_ESTABLISHED`;
`CENTERED_GAP_CONTEXT_DOES_NOT_BY_ITSELF_SELECT_BRANCH`.

Continue:
`GAUGE_EQUIVALENCE_NOT_ESTABLISHED`;
`ABSOLUTE_INITIAL_SELECTOR_STILL_NONIDENTIFIED`.

## Relative Z2 theorem

For edges `b_u xor b_v=c_uv`, choose a root r and let p_v be root-to-v edge parity. Cycle consistency is exactly path independence of p_v. Every solution in one consistent component is

`b_v=a xor p_v`, `a in {0,1}`.

Hence an unanchored connected component has exactly two globally complementary solutions. One exact anchor fixes a and all nodes. Odd cycle parity gives `0=1` and an empty solution set. With u unanchored consistent components, the full solution count is `2^u`.

The pre-frozen registry solution counts are:

`2,2,0,8,1,2,1,2,1,0`.

Straight continuation is only the relative edge `b_(k+1) xor b_k=0`; before an independent anchor, a straight chain remains the all-0/all-1 torsor pair.

## Cross-scale synchronization

After two-endpoint completion carriers are normalized to Boolean collapse coordinates, exact relations such as normalized equality/complement reduce to XOR edges.

Two-level:
`B xor f0=0`, `f0 xor f1=1`,
solutions `{(0,0,1),(1,1,0)}`; `B=1` fixes `(1,1,0)`.

Three-level:
`B xor M=1`, `M xor f0=0`, `f0 xor f1=1`,
solutions `{(0,1,1,0),(1,0,0,1)}`; `B=0` fixes `(0,1,1,0)`.

For finite acyclic pairwise-XOR trees, exact subtree messages plus edge relations and back-substitution recover exactly the full joint solution set. Leaf elimination is exact because each XOR edge is a bijection over F2.

This is not true for information-poor unary-only propagation on arbitrary cycles. The frozen odd cycle
`x xor y=0`, `y xor z=0`, `z xor x=1`
has no joint solution, while unary domains `{0,1}` remain locally supported. The lost datum is cycle parity/correlation.

## Centered gap carrier

`eta(q;L,U)=2q-L-U`.

For `J(q)=L+U-q`:

`eta(J(q))=-eta(q)`.

If `f=a q+b L+c U+d` is jointly translation-invariant and endpoint-reflection odd, exact coefficient comparison gives
`b=c=-a/2`, `d=0`; thus `f=kappa eta`.
So eta is unique up to scale in this affine-linear class.

Controls:
vector half-state `L=-1,U=0,q=-1/2`: `eta=0`;
scalar square gap `L=4,U=9,q=5`: `eta=-3`; reflected q=8 gives `eta=+3`.

Nonzero eta is a tau-nonfixed context carrier, but bare algebra admits two equivariant identifications with the branch torsor. Therefore `sign(eta)` is not a selector.

## Exact anchors and global complement

Positive anchors must independently reduce the full Boolean feasible set to a singleton. Frozen classifications include:
independent root/coarse singleton -> `ABSOLUTE_SINGLETON_ANCHOR`;
XOR constraint -> `RELATIVE_EDGE_ONLY`;
flip-invariant both-branch certificate -> `SYMMETRIC_NO_INFORMATION`;
conflicting anchors -> `INCONSISTENT`;
branch-conditioned residue sign -> rejected as circular.

Global bit complement preserves pairwise XOR, cycle parity and the relative solution structure. It does not generally preserve individual bits, realized completion endpoints, Hamming weight, signed residues, or an absolute anchor held fixed. Therefore relative torsor ambiguity is established, but physical/observable gauge equivalence is not.

## Scalar 5

For square completion, q=5 has legal endpoints `{4,9}` and `eta=-3`. The eta orbit `{-3,+3}` is tau-nonfixed, but has two equivariant identifications with lower/upper branch labels. Bare algebra selects neither. Freeze:
`SCALAR_5_ABSOLUTE_SELECTOR_STILL_NONIDENTIFIED`.

## Covariance / large background / firewalls

Global complement, coordinate permutation, global inversion, jointly transformed completion layers, and positive integer scale pass exact covariance checks. `eta` scales as `eta'=s eta`. Backgrounds near `10^36` are tested by O(1) exact identities only.

No nearest rounding, endpoint argmax, arbitrary reward, ML, random tie break, hidden coordinate ordering, Euclidean selector premise, path-language reinterpretation, sign-eta selector, circular residue anchor, physical probability, or physical gauge claim is used.

## Checker

`3199 / 3199 PASS`; 0 failures.

Digest:
`7aeb27d308d4237b667ee6c6cdd358b555702bd9bc0639056b68e31d5aa8a802`.

Parent immutability:
`PASS_BY_GITHUB_COMPARE_PRE_MANIFEST`.
