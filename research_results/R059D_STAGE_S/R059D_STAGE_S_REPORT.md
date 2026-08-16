# R059D Stage S — 3D Six-Axis / S3 Donor-Symmetry / Complementary Collapse

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source: `bdf5ecb6807c9c9a9aa499c03c7d9a68883ca265`  
Frozen parent: `83d318944534b2e5e38479d959eb4c1746fc7e8b`  
Owner branch: `research/r059d-stage-s-brc-3d-six-axis-s3-donor-collapse`

## Disposition

Stage S establishes:

- `BRC_3D_THREE_DONOR_COMPLEMENTARY_COLLAPSE_ESTABLISHED`
- `D12_REDERIVED_AS_ALL_ORDERED_PAIR_TRANSFERS`
- `TRANSITIVE_S3_HOMOGENEOUS_BRANCH_SET`
- `STATELESS_S3_EQUIVARIANT_UNIQUE_DONOR_SELECTOR_IMPOSSIBLE_AT_FULLY_SYMMETRIC_STATE`
- `S3_INVARIANT_POST_CREDIT_CANNOT_INITIALIZE_UNIQUE_DONOR_AT_FULLY_SYMMETRIC_STATE`
- `STRAIGHTNESS_THREE_STATE_DONOR_MEMORY_CONTINUATION_LAW_ESTABLISHED_WITH_INITIAL_DONOR_UNIDENTIFIED`
- `THREE_DONOR_INITIALIZATION_EQUALS_EXACT_CONTEXTUAL_SINGLETON_WHEN_AVAILABLE`

The bare fully S3-symmetric substrate still has no absolute initial donor selector.

## 3D carrier and D12

`Lambda3={(d1,d2,d3,d4) in Z^4: d1+d2+d3+d4=0}` has rank 3 with basis `e1-e4,e2-e4,e3-e4`.

The ordered transfer family `{e_i-e_j:i!=j}` has 12 distinct vectors in Lambda3. Pairing each with its inverse gives 6 unoriented axes. It equals the frozen notation set `+/-u,+/-v,+/-w,+/-p,+/-q,+/-r`, with `u+v+w=0`, `u=p-q`, `v=q-r`, `w=r-p`. Axis names/signs are notation only.

## Symmetric precollapse and three donors

For `Delta X1=+1`, transverse S3 symmetry gives `Delta X2*=Delta X3*=Delta X4*=a`. Conservation gives `1+3a=0`, so `a=-1/3`.

This is an unresolved algebra/precision carrier state, not a packet weight or Euclidean projection.

On completion layer `Z`, `PREV(-1/3)=-1`, `NEXT(-1/3)=0`. Write `Delta Xj=-1+b_j`. Conservation becomes `b2+b3+b4=2`.

The exact solutions are `(0,1,1),(1,0,1),(1,1,0)`: exactly one donor supplies `-1`. For recipient X1 these are `e1-e2`, `e1-e3`, `e1-e4`. Permuting recipients yields exactly all 12 `e_i-e_j`; no nearest/minimal-distance rule is used.

## S3 symmetry

For fixed recipient, donor set `B1={X2,X3,X4}` is transitive under S3. A donor stabilizer is S2 of order 2, so the full S3 action is not free and `B1 ~= S3/S2`, not an S3 torsor.

The canonical A3 subgroup does act freely and transitively, but no canonical choice of which nonidentity 3-cycle is the positive Z3 generator is established; odd S3 permutations exchange the two choices. This regular subaction supplies no distinguished donor.

At a fully S3-fixed state, deterministic equivariance would require the selected donor to be fixed by all S3. No donor is. Hence the stateless unique selector no-go.

An S3-invariant feasible donor subset can only be empty or all three donors, so symmetry-invariant exact post-credit also cannot initialize a unique donor.

## Straightness and context

For fixed recipient X1, `t2=e1-e2,t3=e1-e3,t4=e1-e4` are Z-linearly independent (a 3x3 minor has determinant `-1`). Therefore the displacement-span rank equals the number of distinct donor identities used.

Rank-one straight continuation is therefore exactly `donor_(k+1)=donor_k`. It does not choose the initial donor.

A continuation context must distinguish all three donors, so minimum context cardinality is 3. One bit is insufficient. Two bits can encode three donors but introduce a noncanonical coding. The direct previous `(recipient,donor)` relation is a minimal three-state covariant context.

For exact initialization define `A(s,h) subseteq B_i`: sizes 0/1/2/3 mean inconsistent / unique forced / partial ambiguity / full multibranch. A preexisting independent donor relation or upstream exact certificate may initialize only when the full feasible set is singleton. Branch-conditioned readouts and hidden ordering are rejected.

## 2D reduction and d-dimensional algebraic gate

At d=2: `a=-1/2`, `b2+b3=1`, two donor branches, free transitive S2 ~= Z2 action, and one-bit straight-continuation memory. Thus the 3D mechanism reduces exactly to the frozen 2D case.

For every integer `d>=2`, `d+1` relation carriers give symmetric transverse `a=-1/d`; integer completion yields `sum b_j=d-1`, hence exactly one donor among d transverse carriers. There are `(d+1)d` directed transfers and `d(d+1)/2` unoriented axes. The donor symmetry is S_d with stabilizer S_(d-1). This is an algebraic generalization only; physical dimensionality is not established.

## Covariance

Carrier permutations map `e_i-e_j` to `e_pi(i)-e_pi(j)`. Global inversion swaps directed orientation. Additive backgrounds near `10^36` leave the displacement theorem unchanged. If event and completion layer scale together by positive integer s, the precollapse state is `-s/3`, neighbors are `-s,0`, and the same three-donor Boolean constraint survives.

## Checker

Deterministic checker: `456/456 PASS`  
Checks digest: `aa0e29cd5dd727402d5c6c5d7633ecca2e5e2f20f0bf42d2ac794e69a96c40fe`

Primary proofs use exact algebra, group actions/stabilizers, completion-neighbor reduction, and rank certificates. Tiny enumeration is only regression/oracle.

## Firewalls

Not established: physical probability from donor multiplicity; Euclidean tetrahedral angle as native premise; physical axis preference; random S3 choice as physical probability; universal absolute donor selector; physical dimensionality from the d-generalization.

`STOP_FOR_DRIVER_REVIEW`
