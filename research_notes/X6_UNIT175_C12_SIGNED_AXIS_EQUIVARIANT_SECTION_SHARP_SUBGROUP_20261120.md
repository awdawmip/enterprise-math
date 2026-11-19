# X6 Unit175 — signed-axis/unoriented-axis equivariant section: complete subgroup classification

Date: 2026-11-20. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`.
Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / SOURCE_PINNED / UNREVIEWED / NOT_ADMITTED**.

## 1. Fixed typed model and scope

Reuses the *candidate* signed integer coordinate action of Unit162, not a P000-admitted physical rotation. P000 V5 native signed spatial Cell axes and observer-preservation remain fixed at `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical source comparison pin: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

Let `E={+e_0,-e_0,...,+e_5,-e_5}` be the 12 signed primitive axis **labels**, `B={0,...,5}` the six unoriented labels, and `pi(±e_i)=i`. Use the signed permutation
[
A(e_i)=e_{i+1}quad(0leq i<5),qquad A(e_5)=-e_0,qquad A(-v)=-A(v).
]
Then `A^6=-I`, `A^12=I`, and the induced action on `B` is the six-cycle `i -> i+1 (mod 6)`. Projection `pi` is equivariant for the abstract twelve-element group `G=<A>`, but the induced action on `B` has kernel `{1,A^6}`.

A **section** is a sign choice `s:B->E` with `pi(s(i))=i`. For a subgroup `H` of `G`, it is H-equivariant if `s(h i)=h s(i)` for every h and i. All claims below are scoped to these finite label actions; there is no assertion that A is a native physical rotation or changes the present P000 rotation authority `S6`.

## 2. New exact theorem: sharp symmetry restriction for sign recovery

For every subgroup `H_d=<A^d>` with `d | 12`, the exact number of equivariant sections is:
[
oxed{
N(H_d)=egin{cases}
64,&d=12quad(H_d={1}),\
4,&d=4quad(H_dcong C_3),\
0,&din{1,2,3,6}.
end{cases}}
]
Equivalently, a section exists **iff** `H_d` has odd order, i.e. the subgroup does not contain the sign-changing kernel element `A^6`.

**Proof.** If `A^6in H`, then `A^6 i=i` for every base label, whereas `A^6 s(i)=-s(i)
e s(i)` on E. Equivariance is impossible. Every even-order subgroup of cyclic G contains the unique element of order 2, `A^6`. Conversely the only odd-order subgroups are the trivial group and `<A^4>` of order 3. In the trivial group all six independent fibers have two choices, so `2^6=64`. The order-three action on B has two free orbits of three axes (even and odd index); choose either signed lift at one representative of each orbit and propagate by `A^4` uniquely and consistently, yielding `2^2=4`. This also proves completeness and necessity. QED.

In particular, the full C12 signless projection admits **zero** C12-equivariant sections, despite 64 ordinary set-theoretic sign selectors; preserving the C3 subgroup allows exactly four. This is a more precise recovery boundary than the order drop established in Unit166: **an additional explicit sign choice, subgroup restriction or other non-erasing provenance is mandatory for equivariant signed-axis reconstruction**.

## 3. Actual frozen production-consumer chain and semantic audit

The following verified files have **identical historical-pin and current-main Git blobs**:

- Frozen producer `src/enterprise_math/finite_symmetry.py`, blob `ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2`, lines 42–74 (valid finite action), 103–111 (stabilizer), 126–136 (fixed-choice obstruction).
- **Real production importer** `src/enterprise_math/equivariant_section.py`, blob `0257fb7eaa95b2f88e772636d3ae2068d9ce42c0`, lines 30, 112–134 (action and projection validation), 138–169 (stabilizer-fixed fibers), 172–201 (obstruction/section-count).
- **Actual test consumer** `tests/test_equivariant_section.py`, blob `bdc3c76070182698b39f7dea38f2312b9f9c07b6`, lines 3–7, 13–39, 40–90, 91–111. These tests exercise generic equivariant-section logic, **not** this new X6 subgroup specialization.

The current generic implementation handles the nonfaithful quotient/base action correctly; no source repair is required for this producer→production importer. This Unit instantiates its pre-existing valid stabilizer-fixed-lift rule with the new exact signed-axis data; the generic theorem itself is reused, not claimed as original. Neither frozen source chain establishes an LP011 wrong-native argmax nor an LP019 illegal positive N-BRC subtraction; both historical alleged bad callers remain `UNRESOLVED_PROVENANCE` until an exact offending `commit:path:line` is observed.

## 4. Independent exact verification

New independent checker: `experiments/x6_unit175_signed_axis_section_20261120/check_equivariant_section.py`. Result certificate: `experiments/x6_unit175_signed_axis_section_20261120/exact_results.json`. Verified all 12 total and 6 base permutation actions, projection covariance, group composition, kernel sign reversal, all 64 sign selectors and all 6 subgroups, **10,752 actually executed pointwise equivariance comparisons**, and exact stabilizer-orbit products. Observed counts by generator exponent d are `{1:0,2:0,3:0,4:4,6:0,12:64}`, zero violations. Three real local CPython executions (normal, `-O`, `-OO`) generated identical JSON SHA-256 `b95130b8ff1640f11fd20a2d9a6b0a4bd7e6c6f2cfd563e9797c568e78d2d687`; certificate canonical payload SHA-256 `4d66b4a5c755bf08726f9aed057a230f1b0c5b49b415172a6f841fe855a7af97`. Safety checks use **always-on** exceptions, not `assert` erased under Python optimization.

The original R063 six-file 17/17 and 512/512 native benchmark was not rerun. No production implementation or frozen scientific source was modified.

## 5. Remaining mother-task obligations

Continue the true frozen 28-LP producer→active consumer ledger and exact LP011/LP019 alleged offending `commit:path:line`; older Unit149–152 Native linkage and independent Driver review remain pending. Native semantic progress is separate from portable GitHub author proof. Preserve the original researcher, own CLAIM/RUN, and explicit unreviewed/not-admitted status; no maintenance lane reuse.
