# X6 LP019 — even relative address + native squared norm + shortest length loses natural BRC: sharp G=18

**Date:** 2026-11-15 15:15 Asia/Hong_Kong. **Mother:** RS-X6-LEGACY-PLANE-RECONCILIATION; frozen signed P000 V5 mathematical source awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03; historical comparison @fd2bcff10ca6e147348b6c1236027fc0d2877df3. **Researcher:** EM-X6-FB6990; Source session MCP-082892eb480e45dea6d4b9fcc0491034. **Classification:** AUTHOR-PROVED FINITE EXHAUSTIVE / EXACT CHECK PASS / UNREVIEWED / NOT_ADMITTED. No theorem or foundation promotion.

## Mother dependency and new question

The preceding [first loss theorem at G=9](https://github.com/awdawmip/enterprise-math/blob/597d8e4a3994b20a8da784a5ac52588a9eb5bb7d/research_notes/X6_LP019_MINZERO_PLUS_NATIVE_G_SHARP_BRC_NONFACTOR_G9_20261115_1500.md) proves that even a correct squared native norm G does not repair an old min-zero observer's BRC loss. Its first witnesses have distinct shortest path lengths 3 and 5. This unit tests the strictly stronger observer retaining the exact **native shortest word length L**, with the same named signed three-axis Cell embedding and all other three native coordinates explicitly fixed to zero.

Define for signed native triples z:

\[
r(z)=z-\min_i(z_i)(1,1,1),\quad
G(z)=\sum z_i^2,\quad
L(z)=\sum|z_i|,\quad
B(z)=\frac{L(z)!}{\prod_i |z_i|!}.
\]

The intended consumer is exact positive natural N-BRC path counting, not a derived signed/amplitude or Boolean support observer.

## New sharp exact result

The strengthened readout \(T(z)=(r(z),G(z),L(z))\) still **does not determine** the exact natural shortest-path BRC mass.

The first failure occurs at native squared norm **G=18**. An exact pair is:

\[
z=(-3,-3,0),\qquad z'=(1,1,4).
\]

Both are valid chosen-Cell signed primitive-axis displacements within the named slice. Their relative observers agree:

\[
r(z)=r(z')=(0,0,3).
\]

Their intrinsic squared lengths and shortest path lengths agree:

\[
G(z)=9+9=18,\qquad G(z')=1+1+16=18,\qquad L(z)=L(z')=6.
\]

But exact path multiplicities differ:

\[
B(z)=\frac{6!}{3!\,3!}=20,\qquad B(z')=\frac{6!}{1!\,1!\,4!}=30.
\]

Hence preserving the min-zero address, true native squared norm **and true shortest path length simultaneously** is still insufficient for N-BRC. Recovering native depth, the absolute step-count vector or another formally sufficient operation-specific path carrier is necessary for this consumer.

### Sharpness and complete finite certificate

Every signed integer triple with G<=17 has all three components in [-4,4]; every triple with G<=18 has all components in [-4,4] as well because \(4^2=16\) and \(5^2=25>18\). Therefore exhaustive evaluation of the 11^3=1,331 triples in [-5,5]^3, selecting those with \(G\le18\), is a **complete** proof for the finite sharpness interval.

The [executed pure-stdlib checker](https://github.com/awdawmip/enterprise-math/blob/574226948ca44f8de2dedde04c70389925b589a9/research_checks/X6_LP019_RELATIVE_NORM_LENGTH_SHARP_BRC_G18_20261115_1515.py) groups every selected signed triple by the exact integer triple (r,G,L), compares exact factorial multinomial values, and asserts:

- 315 distinct (r,G,L) observation fibers occur in the tested population;
- all fibers with \(G\le17\) have constant B;
- exactly six ordered relative-address fibers first have differing B at \(G=18,L=6\);
- each of these six contains N-BRC counts {20,30}, and the displayed pair is explicitly among them.

The six first-failure fibers are the coordinate permutations of relative addresses (0,0,3) and (0,3,3), each retaining G=18,L=6. This is a complete finite classification at the first boundary, not a sampled search.

Actual execution: exit code 0, all assertions pass:

~~~text
PASS_X6_LP019_SHARP_RELATIVE_NORM_LENGTH_BRC_LOSS_G18
exact_fibers=315 differing_fibers=6
earliest_G=18; common_L=6; differing_BRC_values=20,30
~~~

The actual Python process also reported an unrelated spreadsheet warmup diagnostic on startup and subsequently completed the exact check with exit 0.

**Immutable checker:** GitHub commit 574226948ca44f8de2dedde04c70389925b589a9, source Git blob bd3e11ddfd0adce8b707f3ff4b6677c890de313a, exact bytes SHA256 3b54a027e86f057b1846fb24edf056c7286d6ec881e9e692a9f0945a7506612c.

## Scoped consequence and handoff

The old min-zero relative coordinate is useful and exact for its original observer domain; extra G and L are valuable partial recovery coordinates, but the fiber above distinguishes two *different natural path populations* of cardinalities 20 and 30. An exact native path-sensitive consumer must retain a sufficient absolute step-count/provenance representation. No actual particular old LP019 signed-cancellation code defect or LP011 native argmax bad caller is inferred from this construction.

**Parent preserved:** the prior 31 Source-confirmed semantic units; author-side saved GitHub #32 and #33, and freshly recorded #34 sharp G9 unit (own Activity #53). This is a second newly completed, separate research unit with exact checker. Do not redo #34 or earlier proofs. Native semantic publication under the same winning Research SID/CLAIM/RUN requires its original queued #32–#34 Source request's terminal receipt before any further mutation. No alternate claim or dispatch.

**Remaining mother requirements:** precise historical LP011/LP019 bad-caller provenance, complete 28-LP actual consumer closure, original R063 Stage0 unchanged 17-gate 512-case benchmark via unassigned [runner intake #2416](https://github.com/awdawmip/enterprise-math/issues/2416), and independent Driver REQUEST_REVISION. Next scientific action is the highest-information actual uninspected caller source trace and genuine runner ownership/evidence request.
