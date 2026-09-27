# Short-segment and setup reuse for the highest-bit observer

Status: SYMBOLIC / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

This is a prospective optimization of the arbitrary-modulus observer, source
33a46d5f3dacf61e83cedd75cb3424f2375485b3b58984429d5c9fc76b8c96d0,
whose formula is TOP_BIT_GENERAL_MODULUS.md,
880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89.
It changes no frozen execution or old certificate. All inputs remain supplied.

## A single displacement needs no moment table

Let k=g-1, V=2^ell, M=2^(g-ell), L=VM, H=L/2. Write the reached
displacement d=Vz+t with 0<=t<V. The exact stretch identity gives

    A(d)=(-1)^z [(V-t)B(z)-t B(z+1)],

where B(z)=M-3z for z<=M/2 and B(z)=z-M for z>=M/2,
with B(M)=0. At the shared endpoint the two formulas agree.
Within the low displacement piece d<H, z<M/2, so B(z+1)=B(z)-3,
including z+1=M/2. Within the high piece d>=H, z>=M/2 and
B(z+1)=B(z)+1, including the empty endpoint z+1=M. Therefore

    A(d)=(-1)^z [(V-2t)B(z)-alpha*t],
    alpha=-3 in the low piece and alpha=1 in the high piece.       (1)

A certified segment containing exactly one displacement can evaluate (1)
directly. Its d/V quotient and remainder and the parity remainder of z/2
must be actual typed divisions; B(z), V-2t, the products, subtraction and
sign multiplication must also be paid typed work. Selecting the piece from
the already observed segment metadata and choosing +/-1 from the observed
parity remainder are wiring. No host scientific arithmetic or point oracle
is introduced. Empty segments retain their explicit typed zero.

The direct route is bounded to n=1. It does not iterate over an arbitrary
segment and does not change the at-most-eight table bound for longer segments.
It gives the same signed count and original 4^-g normalization. At r=0 the
heads are 0 and R; half-modulus heads still have multiplicity two.

## Lazy piece coefficients

The ten moment coefficients depend only on V, M and the selected piece.
They are unnecessary for empty and singleton segments. Build a piece's
coefficient record only when a segment with n>=2 is first reached. Save the
actual operation range and result once, and use a source-bound reference for
later segments needing that piece. A coefficient cache hit performs no new
coefficient arithmetic and must not be charged as a second construction.
It is also not a free first construction: the initial paid work remains in
the common observer evidence.

## Scale and coefficient reuse across queries

For requests with identical public (g,ell), the scales V,M,L,P=2V,H=L/2
are identical. A per-observer setup record may retain their initial typed
construction and the lazy piece records. A new (g,ell) creates a distinct
record and pays all construction; neither R nor r is part of these data.
Use an append-only list of setup records and a private lookup mapping the
strict public integer pair to its list index. Every successful request binds
its setup index; export includes the full setup list and chronological raw
arithmetic. Fresh verification starts with an empty cache, repeats the exact
request sequence, and compares the full resulting certificate, excluding
only the existing native primitive cache-call delta.

Attach a provisional setup to the shared list before any typed scale work,
and attach a provisional piece record before its coefficient work. Mark each
complete only after construction. A failed in-flight numerical request keeps
the provisional records and raw operations, blocks later calls and export,
and requires a fresh observer. Invalid public inputs reject before creating
an in-flight request or changing the setup cache, so valid later calls remain
possible. This distinction must remain visible in the checker.

Certificates use a new schema and bind the new source and proof. Cache hits
are inspectable references to prior completed construction, never fabricated
operation ranges or copied charges. The cache does not prove its own values:
source-bound fresh chronological replay verifies construction and reuse.

## Scope and next check

No numerical run, speed measurement or saving is asserted by this note.
The expected removal of unnecessary work is structural; real arithmetic
costs and negative replay costs must be measured on a declared grid. Reuse of
the previous full raw comparator is sufficient for unchanged input tuples.
Add separate bounded new input coverage only if a new branch needs it.
The new implementation should retain complete failed/rejected evidence,
setup/proof pins and the same scientific arithmetic restrictions.

This remains a fixed selected-highest-bit scalar family, polynomial in the
explicit scale length g+log(R+1) under the existing moment contract. Setup
reuse changes neither the general complexity class nor the unresolved
non-top mixed sums, unknown-order discovery, matrix correlation or full Shor
sampling problems. No new literature-priority claim is made.

Global-Knowledge-Sync: main@6e443c7 / GLOBAL_KNOWLEDGE_V1
