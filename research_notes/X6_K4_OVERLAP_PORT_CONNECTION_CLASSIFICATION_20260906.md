# X6/FCC K4 overlap transport: exact two-choice S4 connection, remote-port provenance bit, and concrete Euler holonomy

Status: `FREE_RESEARCH / EXACT FINITE CONNECTION CLASSIFICATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Depends on:
- `research_notes/VIETE_X6_K4_ROOT_HOLONOMY_C24_ATLAS_20260906.md`
- `research_notes/EULER_FCC_CHIRALITY_FACE_HOLONOMY_CLASSIFICATION_20260904.md`
- `src/enterprise_math/euler_fcc_chirality.py`
Checker: `experiments/x6_k4_overlap_connection_20260906/check_x6_k4_overlap_connection.py`
Checker source commit: `952993c99340ef7cce7542b5573ab2182a3e9328`
Current source frontier consumed: `main@57440ab85f4b95b6085d8f00fe630c7a8f941ad1`

## 1. Exact question

The four physical FCC STARs are the four K4 vertex stars `S_i`.  The previous Viète atlas theorem selected the natural K4 transposition

\[
T^-_{ij}=(ij)
\]

as an explicit connection from `S_i` to `S_j`, producing the all-negative chirality class.

The remaining connection-selection question is:

> after requiring an `S4<S6` axis permutation to map `S_i` to `S_j` **through their shared line** `E_ij`, how many transports are actually available, and what native/carrier provenance distinguishes them?

## 2. Theorem: exactly two shared-line-fixing S4 transports exist on every overlap

Fix distinct K4 vertices `i,j`, and let `k,ell` be the complementary two vertices.

Require `g in S4` to satisfy

\[
g(S_i)=S_j
\]

and

\[
g(E_{ij})=E_{ij}.
\]

There are exactly two solutions:

\[
\boxed{T^-_{ij}=(ij)}
\]

and

\[
\boxed{T^+_{ij}=(ij)(k\ell)}.
\]

No third `S4` axis permutation maps the source STAR to the target STAR while preserving the common overlap line setwise.

Their support sizes on the four STAR labels are respectively

\[
2
\quad\text{and}\quad
4.
\]

Their permutation parities are respectively odd and even.

## 3. The missing bit is remote-port provenance

Each nonshared line in `S_i` has a unique remote STAR port.  For example `E_ik` is the line shared by `S_i` and remote STAR `S_k`.

The two transports act differently:

### Minimal-support transport

\[
T^-_{ij}(E_{ik})=E_{jk},
\qquad
T^-_{ij}(E_{i\ell})=E_{j\ell}.
\]

It preserves the two remote port labels `k,ell` individually.

### Complement-swapping transport

\[
T^+_{ij}(E_{ik})=E_{j\ell},
\qquad
T^+_{ij}(E_{i\ell})=E_{jk}.
\]

It swaps the two remote ports.

Therefore the overlap ambiguity has a concrete typed meaning:

\[
\boxed{
\text{OVERLAP CONNECTION BIT}
=
\text{REMOTE-PORT TRANSPORT CHOICE}.
}
\]

This is not an abstract sign inserted after the fact.

## 4. Chirality bit equals the parity of the actual overlap permutation

Orient STARs by one tetrahedral boundary orientation as in the previous atlas theorem.

Then

\[
T^-_{ij}(o_i)=-o_j,
\]

while

\[
T^+_{ij}(o_i)=+o_j.
\]

Thus if the Euler edge bit is encoded by

\[
e_{ij}=1\iff\text{local chirality reverses},
\]

then

\[
\boxed{
e_{ij}=1\iff T_{ij}=T^-_{ij},
}
\]

and

\[
\boxed{
e_{ij}=0\iff T_{ij}=T^+_{ij}.
}
\]

Equivalently, the Euler edge bit is the parity/orientation character of the selected actual `S4` overlap permutation.

## 5. Every one of the 64 Euler edge cochains has an actual S4 axis-permutation realization

There are six K4 overlaps and two admissible transports on each overlap.

Therefore there are exactly

\[
2^6=64
\]

connection assignments of this type.

Choose `T^-` on an edge when its desired Euler bit is `1`, and `T^+` when the desired bit is `0`.

This gives a concrete `S4<S6` realization of every one of the 64 edge cochains classified by the existing Euler finite tool.

Hence the finite chirality connection space is not merely formally realizable as signed-graph data:

\[
\boxed{
\text{ALL 64 K4 EDGE COCHAINS ARE REALIZED BY EXPLICIT SHARED-LINE-FIXING S4 AXIS-PERMUTATION CONNECTIONS}.
}
\]

## 6. Face holonomy is exactly the parity of the actual loop permutation

For a triangular atlas loop

\[
i\to j\to k\to i,
\]

let the selected overlap maps be the chosen `T^+` or `T^-` maps.

The actual loop automorphism is

\[
H=T_{ki}T_{jk}T_{ij}.
\]

It fixes the starting STAR `S_i` setwise.

Exhaustively over all 64 global connection choices and all four triangular faces:

\[
\boxed{
\operatorname{parity}(H)
=e_{ij}+e_{jk}+e_{ki}\pmod2.
}
\]

The right side is exactly the Euler face holonomy bit.

Therefore:

### Face bit zero

The loop permutation is orientation preserving on the starting STAR.  It is either

- the identity, or
- a visible 3-cycle.

### Face bit one

The loop permutation is orientation reversing on the starting STAR and is an actual visible transposition.

Thus

\[
\boxed{
\text{EULER FACE HOLONOMY}
=
\text{ORIENTATION-PARITY CHARACTER OF THE ACTUAL S4 LOOP TRANSPORT}.
}
\]

This is the concrete connection-level meaning of the existing `F2` holonomy.

## 7. Two fully symmetric endpoint connections remain

Two especially symmetric connection laws are immediate.

### A. Remote-port-preserving / minimal-support connection

Choose

\[
T_{ij}=T^-_{ij}=(ij)
\]

on every edge.

Then all six edge bits are `1`, every triangular face bit is `1`, and

\[
H_{ijk}=(jk).
\]

This is the all-negative/antibalanced `1111` class used by the Viète K4 root-bundle theorem.

### B. Remote-port-swapping connection

Choose

\[
T_{ij}=T^+_{ij}=(ij)(k\ell)
\]

on every edge.

Then all six edge bits are `0`, every triangular face bit is `0`, and every triangular loop transport is the identity.

This is a fully flat `0000` connection.

Therefore carrier symmetry and shared-line preservation alone still do not choose between flat and all-odd connection classes.

## 8. Exact selector reduction

The previous natural connection can now be characterized without simply naming the transposition:

\[
\boxed{
\text{REMOTE-PORT-PRESERVING SHARED-LINE OVERLAP TRANSPORT}
\Longrightarrow
T_{ij}=(ij)
\Longrightarrow
\text{ALL-NEGATIVE }1111\text{ CONNECTION}.
}
\]

Equivalently, among the two admissible overlap maps it is the unique map with minimum support on the four STAR labels.

However this is still a **declared transport principle**.  Current P000 does not yet state that actual native rotation must preserve remote STAR ports or minimize support.

So the remaining rotation-law selector is now extremely small:

> Does the actual native rotation/transport semantics preserve remote atlas-port provenance, swap it, or retain it as path-dependent state?

The connection ambiguity is no longer an unspecified global mystery; it is one explicit local port-transport bit per overlap.

## 9. BRC operation-safety interpretation

The numerical recurrent Schur port-collapse theorem is not directly applicable because the present atlas connection is deterministic rather than a positive-rational recurrent module.

But its typed boundary is relevant: **port labels are semantic and no unlabeled port identification is implicit**.

For the present deterministic observer/future-operation gate, the two overlap maps agree on:

- source STAR;
- target STAR;
- shared line.

They differ on the future identity of the two remote ports.

Hence a quotient which remembers only `(source STAR,target STAR,shared line)` is unsafe for any future operation which subsequently asks which remote STAR/line is reached.

The smallest residual on that horizon is the one remote-port swap bit.

BRC resolution:

`REUSE_BOUNDARY = PORT LABELS ARE SEMANTIC / NO UNLABELED PORT COLLAPSE`.

`RECURRENT_SCHUR_NUMERICAL_TOOL = NOT_APPLICABLE`.

`ACTIVE_REDUCTION = DETERMINISTIC OBSERVER/FUTURE-OPERATION FACTORIZATION`.

## 10. Consequence for the Viète root bundle

The Viète principal root-sign connection uses the same chirality edge bit.

Therefore:

- under the remote-port-preserving minimal connection, the four-STAR root-sign bundle is the nontrivial cube/antibalanced cover;
- under the remote-port-swapping flat connection, a global signed root trivialization exists on the four STAR base;
- under mixed connection choices, the exact Euler face-holonomy class controls whether local root signs can be globally trivialized.

Thus the root bundle topology is not separate from the actual atlas-port transport law.

The next physical question is not “where does the sign come from?” but:

\[
\boxed{
\text{WHICH OF THE TWO SHARED-LINE-FIXING OVERLAP TRANSPORTS DOES THE ACTUAL NATIVE ROTATION LAW USE, AND IS THAT CHOICE PATH-DEPENDENT?}
}
\]

No Foundation promotion is made here.
