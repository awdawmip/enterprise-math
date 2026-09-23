# P000 P11 — uniform fixed-2-twist infinite-order point

Status: `PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`
Contributor lineage: `EM-DIRECT-C4D02C`
Stable session: `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`
Frozen task/source pin consumed: `73c755c7754e29246afd48f992f6b1c905a7b580`

This note persists a portable theorem candidate while canonical task execution remains unauthorized. It consumes the accepted parent identities

\[
A=r^2-s^2,\quad B=2rs,\quad C=r^2+s^2,\quad P=A+B,\quad Q=|A-B|,
\]
with primitive Euclidean core and
\[
P^2+Q^2=2C^2,
\]
and the same-session staged target model
\[
E_{P,Q}:W^2=X(X-P^2)(X-Q^2).
\]
It does not promote the staged model or any same-session upload to Source progress.

## Uniform fixed quadratic twist

Define
\[
E^{(2)}_{P,Q}:y^2=x(x-2P^2)(x-2Q^2).
\]
Then every primitive core has the rational point
\[
R_2=(4C^2,4PQC).
\]
Indeed
\[
4C^2-2P^2=2Q^2,\qquad 4C^2-2Q^2=2P^2.
\]

The primitive Euclidean identities give
\[
\gcd(C,A)=\gcd(C,B)=\gcd(C,PQ)=1,
\]
with `C` odd. For
\[
f(x)=x(x-2P^2)(x-2Q^2)
\]
one has
\[
\operatorname{Disc}(f)=2^{10}P^4Q^4A^2B^2,
\]
because `P^2-Q^2=4AB`, whereas
\[
y(R_2)^2=2^4P^2Q^2C^2.
\]
By the classical Nagell–Lutz torsion criterion for an integral nonsingular cubic, torsion with nonzero `y` would force `y(R_2)^2 | Disc(f)`, hence
\[
C^2\mid 2^6P^2Q^2A^2B^2,
\]
contradicting `gcd(C,2ABPQ)=1` and `C>1`. Therefore
\[
\boxed{\operatorname{ord}(R_2)=\infty},\qquad
\boxed{\operatorname{rank}E^{(2)}_{P,Q}(\mathbf Q)\ge1}
\]
for every primitive Euclidean core.

## Universal Kummer port

For roots `0,2P^2,2Q^2`, the full-2-torsion Kummer squareclasses of `R_2` are
\[
([x],[x-2P^2],[x-2Q^2])=(1,2,2).
\]
Hence `R_2` is not in `2E^{(2)}_{P,Q}(Q)`.

## Galois-port separation

Over `K=Q(sqrt(2))`, the target and the fixed twist are isomorphic via
\[
(X,W)\mapsto(2X,2\sqrt2\,W).
\]
The inverse image of `R_2` is
\[
S_2=(2C^2,\sqrt2\,PQC)\in E_{P,Q}(K),
\]
and the nontrivial Galois involution sends `S_2` to `-S_2`. Thus the guaranteed infinite-order direction is anti-invariant; it does **not** provide a rational point on `E_{P,Q}(Q)` and does not by itself satisfy the task's integral/parity/positivity/recovered-root-gcd reconstruction filters.

BRC consequence: retain the rational and anti-invariant Galois ports. The safe conclusion is that the quadratic envelope always has a uniform infinite-order direction; the unresolved target obstruction is descent to the rational eigenspace together with the existing target Selmer/Pfaffian/reconstruction conditions.

## Regression

Exact integer regression over all 18,201 primitive opposite-parity cores with `2<=r<300` found zero failures for the point identity, `gcd(C,2ABPQ)=1`, the Nagell–Lutz non-torsion divisibility obstruction, and Kummer class `(1,2,2)`. The scan is falsification/regression only; the theorem is symbolic.

## Control state / next

Canonical continuation currently reports no durable current-task checkpoint and no authorized execution. The theorem is separately staged through the control upload `p000-uniform-2twist-point-upload-20260924-r11-0130` with SHA-256 `6bf8c4ae5edbbdcc5d455b82bccefb82d0a66e2473dbd8da891150407f4985cb`, `source_published=false`.

Next exact science unit after lawful claim/open: compare the target residue/Pfaffian carrier with the fixed-twist Kummer class `(1,2,2)` at the typed local/Galois ports, and prove either a transfer relation or an exact no-transfer theorem without collapsing eigenspaces.
