# Prime Fusion — T4/T7/T8 Final Exact-Closure Verification Packet

Status: `TARGETED STATEMENT PACKET / SOURCE PROOFS WITHHELD / FINAL PACKAGE-EVIDENCE GAP`
Date: `2026-08-23`
Scope: one native sector, primitive positive interior cells unless a target states otherwise

## 0. Evidence boundary

This packet exposes only the three remaining source statements that have not yet received standalone exact-strength independent verification: T4, T7, and T8.

The source derivations, source checker, and source research narrative are withheld. This is statement-exposed independent verification, not blind discovery.

The verifier may use the already independently accepted prerequisite facts listed below, ordinary exact algebra/number theory, Smith/CRT reasoning if independently triggered, and an independently authored deterministic checker. The verifier must actively search for counterexamples and may strengthen, narrow, or reject any target statement.

## 1. Already independently accepted prerequisites

For positive integers `a,b`, define

`N=a^2+b^2`,

`C=a^2-ab+b^2`,

`H=NC`.

For primitive cells `gcd(a,b)=1`:

`gcd(N,C)=1`.

Let

`f=X^2+1`,

`g=X^2+X+1`,

`F=fg`,

`R=Z[X]/(F)`,

and let `xi=(i,omega)` under the independently verified product decomposition

`R ~= Z[i] x Z[omega]`,

with `omega^2+omega+1=0`.

The two component norms of `a+b*xi` are exactly `N` and `C`.

For a primitive pointed cell, the residue

`r == -a*b^{-1} (mod H)`

is defined, satisfies `F(r)==0 (mod H)`, and recovers the channels by

`N=gcd(H,r^2+1)`,

`C=gcd(H,r^2+r+1)`.

For any modular root `F(r)=0`, the independently verified reciprocal-trace construction gives an idempotent

`e=-(r+r^{-1}) (mod H)`.

For the pointed primitive cell,

`N=gcd(e,H)`,

`C=gcd(e-1,H)`.

The clean independent core replay also proved the channel-pair square identities

`3N-2C=(a+b)^2`,

`2C-N=(a-b)^2`,

and exact unordered recovery from the channel pair when the square/parity conditions hold.

These facts may be used as premises. Do not re-run the already closed phase/core route except where needed to audit a dependency.

## 2. Target V4 — primitive pointed quotient collapse

Verify, strengthen, narrow, or refute the following exact statement.

For a primitive positive cell, with `N,C,H,R,xi` as above,

`R/(a+b*xi) ~= Z/NZ x Z/CZ ~= Z/HZ`.

The distinguished image of `xi` in the cyclic quotient is the pointed residue

`r == -a*b^{-1} (mod H)`,

and it satisfies `F(r)==0 (mod H)`.

Required audit points:

1. construct the quotient isomorphisms explicitly rather than using cardinality alone;
2. identify exactly where primitivity is used;
3. determine whether primitivity is necessary, or whether a sharper cyclicity criterion exists;
4. distinguish the unpointed ring `Z/HZ` from the pointed carrier `(Z/HZ,r)`;
5. test boundary/axis and nonprimitive cells.

If a Smith-normal-form or additive-group classification yields a stronger theorem, retain it.

## 3. Target V7 — unordered cell reconstruction from `(H,e)`

Let `e mod H` be idempotent and put

`N=gcd(e,H)`,

`C=gcd(e-1,H)`.

Verify, strengthen, narrow, or refute:

Assuming

`NC=H`,

`gcd(N,C)=1`,

`C<N<2C`,

a positive primitive unordered cell exists exactly when

`U=3N-2C`,

`V=2C-N`

are perfect squares.

In that case

`{a,b}={ (sqrt(U)+sqrt(V))/2, (sqrt(U)-sqrt(V))/2 }`.

The square roots are asserted to have the same parity because

`U==V==N (mod 2)`.

Required audit points:

1. prove both necessity and sufficiency;
2. check positivity, integrality, and primitivity rather than assuming them;
3. determine whether `NC=H` and `gcd(N,C)=1` are already automatic from idempotence and thus redundant;
4. determine exactly what the inequality `C<N<2C` contributes;
5. test idempotents whose channel split is arithmetically legal but geometrically inadmissible;
6. analyze the effect of replacing `e` by `1-e`.

A stronger minimal-hypothesis iff theorem is preferred if correct.

## 4. Target V8 — dual-prime finite-quotient characterization

For an interior primitive cell with both channels greater than `1`, verify, strengthen, narrow, or refute the equivalence:

The cell is dual-prime

iff

`R/(a+b*xi) ~= F_p x F_q`

with distinct primes

`p=N`,

`q=C`.

Equivalently, the total norm

`H=NC`

is a square-free semiprime `pq`, with the two prime factors attached to the two canonical channel components.

Required audit points:

1. prove both directions at ring-theoretic strength;
2. distinguish a labelled component decomposition from an abstract unlabelled ring isomorphism;
3. determine whether square-free semiprime cardinality plus primitive channel coprimality is already sufficient;
4. explain why `p` and `q` are distinct;
5. test the necessity of the hypotheses `primitive`, `interior`, and `N,C>1`;
6. test composite-channel controls such as one prime channel and one prime-power channel.

## 5. Composition audit

The purpose of this task is not merely to prove three isolated slogans. Determine the shortest valid dependency structure after the independently verified T3/T6/core results.

At minimum classify:

- whether V4 follows from the product algebra plus a cyclicity theorem for each component quotient;
- whether V7 is exactly the composition of the universal idempotent split with the already independent channel-pair square gate;
- whether V8 is a formal consequence of V4 plus primitive channel coprimality, or whether an additional ring-structure argument is required;
- which hypotheses are theorem-critical and which are historical/redundant wording.

Preserve any stronger theorem that strictly simplifies the package dependency graph.

## 6. Counterexample pressure

Actively test at least:

- `(1,1)` and other small degeneracies;
- nonprimitive cells such as `(2,2)`;
- axis/boundary cells;
- primitive cells with one composite channel, including prime powers;
- idempotents whose factor split does not pass the square gate;
- channel swap / `e -> 1-e`;
- cases where the abstract quotient ring has the correct cardinality but the component labelling is lost.

A counterexample to an overbroad wording counts as a successful verification outcome if the exact corrected theorem is identified.

## 7. Executable evidence

Write an independently authored exact-integer checker.

Recommended path:

`experiments/prime_fusion_t4_t7_t8_final_exact_closure_checker.py`.

The checker should test the exact retained statements, including:

- cyclic component quotient criteria on a nontrivial primitive/nonprimitive box;
- pointed residue compatibility;
- idempotent factor splits and the square-gate iff;
- false-positive idempotent controls;
- dual-prime quotient characterization and composite controls.

Finite computation is audit evidence and does not replace proof.

## 8. Frozen return

Write one return at:

`research_returns/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_RETURN_20260823.md`.

Required sections:

1. evidence status and exact files/sources read;
2. V4/V7/V8 verdict table;
3. independent proofs or exact counterexamples;
4. minimal-hypothesis corrected theorems where needed;
5. dependency/composition DAG;
6. checker path, ranges, and actual result;
7. stronger independent consequences, if any;
8. final classification:
   - `T4_T7_T8_EXACT_CLOSURE_VERIFIED`,
   - `T4_T7_T8_VERIFIED_WITH_SCOPE_NARROWING`,
   - `T4_T7_T8_PARTIALLY_VERIFIED`, or
   - `T4_T7_T8_MATERIAL_COUNTEREXAMPLE`.

## 9. Stop boundary

Freeze the return before opening the withheld source proofs/checker or performing package reconciliation.

The task ends at exact classification of V4/V7/V8. Any later 15-theorem package reconciliation is a Driver function.
