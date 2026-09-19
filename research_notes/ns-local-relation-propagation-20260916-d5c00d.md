# 局部关系传播：把有限 stabilizer 关系拆成 X6 端点片段

Progress-Event-ID: `NS-LOCAL-RELATION-PROPAGATION-20260916-D5C00D-19`  
Researcher-ID: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Research-Activity-ID: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING — exact finite relational construction and executed checks; not primitive force, Foundation or Navier–Stokes theorem.**

## 0. Question

Event18 supplies a finite relation interface: the three-logical-qubit stabilizer/Clifford/Pauli subtheory closes on a finite signed-Pauli relation state and carries an operationally necessary GHZ global relation. But a single global relation table is not yet a native local dynamics.

This event asks a narrower constructive question:

> Can the relation state be split into finite **endpoint fragments** so that every single-party gate changes only one endpoint, every two-party gate changes only the two actually meeting endpoints, relation support grows only through actual encounters, and all X6 spatial moves remain primitive signed-axis steps?

The answer is yes for the declared stabilizer comparator. This is still an external quantum interface; it does not certify CNOT as a primitive P000 force event or derive quantum mechanics from P000.

## 1. Distributed relation representation

Keep three independent relation-row IDs `r=1,2,3`. Party `q` stores for each row:

- one local Pauli letter `P_{r,q} in {I,X,Y,Z}`;
- one local sign factor `sigma_{r,q} in {+1,-1}`.

The global row reconstructed from its endpoint fragments is

\[
S_r=\left(\prod_{q=1}^3\sigma_{r,q}\right)
P_{r,1}\otimes P_{r,2}\otimes P_{r,3}.                 \tag{1.1}
\]

A raw endpoint therefore needs at most

\[
4^3\,2^3=512                                            \tag{1.2}
\]

internal relation symbols before imposing validity constraints or gauge identifications. This is a fixed finite local alphabet for the declared three-row interface. Spatial Cell coordinates remain the unbounded discrete X6 torsor and are not counted as internal relation symbols.

The initial product state `|000>` is represented by the rows

\[
ZII,\quad IZI,\quad IIZ.                                \tag{1.3}
\]

## 2. Local update laws are exactly endpoint-local

For a single-party H or S on party q, conjugate only `P_{r,q}`. If the exact Pauli conjugation produces a minus sign, multiply only `sigma_{r,q}` by -1. All other endpoints are unchanged.

For a CNOT between co-located parties c,t, conjugate only the pair `(P_{r,c},P_{r,t})`. The possible exact conjugation sign is stored at one of those two local endpoints. The third endpoint is unchanged byte-for-byte.

Reconstructing the global signed row after every such operation gives exactly the same row as ordinary global Clifford conjugation. The checker derives the parent H/S/CNOT Pauli maps from exact matrices and compares the distributed reconstruction with the full event18 relation state after every stage.

Thus relation evolution factors through the actual participating endpoints:

\[
\boxed{\text{single gate} \to 1\text{ endpoint},\qquad
       \text{pair gate} \to 2\text{ co-located endpoints}.}      \tag{2.1}
\]

This is an implementation property of the declared relation representation, not a claim that primitive force arity has become two.

## 3. GHZ global relation grows through actual encounters

Use three party identities A,B,C. Let A start at a chosen native Cell `c`, B at `c+s_b e_i`, C at `c+s_c e_j`, where `i!=j` and `s_b,s_c in {+1,-1}`.

Apply the following finite test protocol:

1. H on A at c;
2. move B by one primitive step to c;
3. apply CNOT A->B while co-located;
4. move B back by one primitive step;
5. move C by one primitive step to c;
6. apply CNOT A->C while co-located;
7. move C back.

No off-axis spatial step appears. The first independent relation row evolves as

\[
\boxed{XII\longrightarrow XXI\longrightarrow XXX.}     \tag{3.1}
\]

Its support size is therefore

\[
1\longrightarrow2\longrightarrow3.                    \tag{3.2}
\]

The first extension occurs only when A and B actually meet; the second occurs only when A and C actually meet. The other independent rows become `ZZI` and `ZIZ`, giving the usual GHZ generator set.

This gives a concrete meaning to “relation propagation” in the comparator: it is not a scalar energy pulse moving instantaneously to remote parties. It is the extension of a retained joint relation through a sequence of local interactions and explicit transport events.

## 4. Remote endpoint fragments and remote local marginals stay unchanged

At the A-B CNOT, C's three local relation fragments are exactly unchanged. At the A-C CNOT, B's local fragments are exactly unchanged.

Reconstructing the density matrix gives the corresponding observer statement:

- the reduced state of C is unchanged by the local A-B gate;
- the reduced state of B is unchanged by the local A-C gate.

The global relation can nevertheless change. This is the familiar separation between joint state and remote marginal in the declared quantum comparator. It is not faster-than-light signalling.

## 5. Local sign splitting has a certified gauge quotient

The factorization of one global row sign into three local signs is not unique. Multiplying two endpoint signs of the same row by -1 leaves the global product unchanged.

For each row there are four even-parity sign redistributions. Across three independent rows there are

\[
4^3=64.                                                 \tag{5.1}
\]

gauge lifts of the same global relation table.

The checker exhausts all 64. Each is propagated through the entire local H/CNOT/transport protocol and reconstructs the **identical global density state at every stage**.

Hence for the future operations declared in this event, the individual local sign split is a safe gauge redundancy; the global row sign is the operational relation coordinate. This is a positive, scope-typed BRC quotient certificate rather than an informal erasure.

This certificate does not authorize deleting party-local Pauli letters or the row identity: doing so would destroy the global relation reconstruction.

## 6. Six-axis spatial covariance of the transport layer

The relation protocol was executed for every ordered pair of distinct native axes `(i,j)` and every choice of signs `(s_b,s_c)`:

\[
6\cdot5\cdot2\cdot2=120.                               \tag{6.1}
\]

transport variants.

In each case:

- every nonzero move has exactly one signed X6 component;
- each CNOT is attempted only when its two register identities occupy the same Cell;
- B and C return to their original Cells;
- the entire relation-row trajectory is the same as the reference protocol.

Thus the finite relation mechanism does not depend on choosing a privileged spatial axis. The quantum party labels and the native spatial axes remain separately typed.

## 7. Final BRC/Mermin witness survives the local factorization

At the end the reconstructed stabilizer group contains

\[
+XXX,+ZZI,+ZIZ,-XYY,-YXY,-YYX.                         \tag{7.1}
\]

The exact Mermin value remains 4; deterministic local-hidden assignments remain bounded by 2.

The incoherent `000/111` mixture has the same one-party marginals and pair-Z relations but Mermin value 0. Therefore the local-fragment implementation has not accidentally replaced the global relation by its marginals.

## 8. What has and has not been achieved

This event closes one interface question:

\[
\boxed{\text{a finite global relation table can be factorized into finite endpoint fragments and propagated by local encounters}.} \tag{8.1}
\]

It also closes a small locality/gauge question: no update of a remote endpoint fragment is required for the declared Clifford preparation, and a 64-element sign-gauge family is provably operationally redundant for the stated future operations.

It does **not** provide the missing physical law. The gate sequence is a declared test protocol. CNOT is a quantum comparison operation, not certified as `TRIADIC_CLOSURE_E`; pair interaction here must not be reinterpreted as primitive two-force balance. A physical native implementation still needs a lawful triadic (or explicitly composite) mechanism, resource/read dependencies, and a derivation of why these relation-update rules should hold.

The global GHZ relation should therefore be treated as a **target interface/falsifier**: any proposed native reduction that keeps only local marginals/pair-Z information already fails this finite future-observer test.

## 9. Exact checks

The event19 checker imports the event18 checker by exact SHA256 pin

`6ff48da0bbd6a041f580696f464353216696bd21a27d0ac411b0e2dafe4202a4`

and executes its Pauli conjugation/reconstruction helpers unchanged.

Executed:

- complete local relation protocol and global-reference equality at every stage;
- first-row support `1,2,3` at H_A, CNOT_AB, CNOT_AC;
- byte-for-byte remote endpoint-fragment invariance at pair gates;
- exact remote one-party marginal invariance;
- all 64 sign-gauge lifts through the full trajectory;
- all 120 ordered signed two-axis transport variants;
- final Mermin 4 versus incoherent-mixture 0;
- all 64 deterministic local-hidden Mermin assignments.

A fresh repo-like directory containing event18 and event19 checkers produced byte-identical event19 results.

Checker SHA256:
`e3ea2ebb040b00969a5896164978b92c4726bd53bc7f1c4e6784d08c573c98a7`

Result SHA256:
`97f610eff8ea9c493bd990f78a86df186018aad69725eedeb597b11a8914d222`

## 10. Next unresolved physical unit

The next problem is no longer “can a finite relation be propagated locally?” for this comparator. It is:

> Can a **legal P000-native triadic event system**, without target-fitted repair or hidden continuous precision, generate the required endpoint relation transformation from its own state and resources?

A trivial unchanged third spectator is not enough to certify primitive triadic force balance. The next construction must state all three participants' nontrivial roles, intermediate state, conservation ledger, path provenance and event-selection rule before using its output as evidence.
