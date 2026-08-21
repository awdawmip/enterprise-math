# R005-B — Deterministic Post-Database Cubic Cursor Certificate

Status: `EXACT FINITE CURSOR CERTIFICATE + EXTERNAL MR12 THRESHOLD / NOT CANONICAL`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 17, 20, 23

## 1. Main result

Supplement 20 gives the complete cubic full-forcing classification through

\[
K=10^{10},
\]

with exactly five exceptional basins

\[
23,64,120,138,1005.
\]

Supplement 23 shows that immediately beyond K the part of the lower q>k band
not covered by the current \(10^{20}\) exhaustive prime-gap database is a tiny
integer cursor rather than the whole candidate set.

A deterministic cursor certificate now verifies every actual prime-q overflow
state on

\[
\boxed{10^{10}<k\le10^{10}+2000.}
\]

Every such q has an explicit prime cofactor inside its cubic basin.  Therefore
the complete five-exception classification extends to

\[
\boxed{2\le k\le10{,}000{,}002{,}000.}
\]

No new non-forced candidate occurs on the 2000 post-database basins.

This is a small extension in k compared with the earlier billion-scale jumps,
but it proves a new point: the \(10^{20}\) database edge is not an arithmetic
failure boundary.  A sparse local certificate can cross it without extending
the global gap database.

## 2. External primality input

Sorenson and Webster determined

\[
\boxed{
\psi_{12}
=318{,}665{,}857{,}834{,}031{,}151{,}167{,}461,
}
\]

the smallest composite strong pseudoprime to the first twelve prime bases

\[
2,3,5,7,11,13,17,19,23,29,31,37.
\]

Consequently, below \(\psi_{12}\), an integer passing all twelve strong
Miller--Rabin tests is prime.

The cursor verifier uses this fact as a deterministic theorem.  It refuses to
test an integer at or above \(\psi_{12}\); there is no BPSW or probabilistic
fallback.

Every q and r in the frozen certificate lies far below \(\psi_{12}\); the
largest certified cofactor prime is only about \(10^{20}\).

## 3. B77 — exact cursor at the current database edge

Let

\[
K=10^{10},\qquad X=K^2=10^{20},\qquad k=K+d.
\]

Supplement 23 gives

\[
W_X(K+d)
=2d+
\left\lfloor
\frac{3d^2}{K}+rac{d^3}{K^2}
\right\rfloor.
\]

For every frozen offset

\[
1\le d\le2000<57{,}734,
\]

this reduces exactly to

\[
\boxed{W_X=2d.}
\]

Thus the database-overflow integer coordinates are exactly

\[
\boxed{k<q\le k+2d.}
\]

The union of all such q-cursors for the 2000-basin block lies inside the tiny
absolute interval

\[
10{,}000{,}000{,}002
\le q\le
10{,}000{,}006{,}000.
\]

Deterministic MR12 enumeration finds exactly

\[
\boxed{236}
\]

distinct prime q values in that union.

Because the same q can remain active for several neighboring k, the block
contains

\[
\boxed{161{,}846}
\]

prime-q cursor states in total.

## 4. B78 — local cofactor certificate per cursor state

For each prime cursor coordinate q at basin k, define

\[
x=\left\lfloor\frac{k^3}{q}\right\rfloor,
\qquad
Y=\left\lfloor\frac{(k+1)^3-1}{q}\right\rfloor.
\]

The verifier searches deterministically for one MR12-certified prime

\[
\boxed{x<r\le Y.}
\]

Since the cursor is restricted to the lower cofactor band, x already lies at or
above the factor horizon.  Hence every such r satisfies r>F and

\[
k^3<qr\le(k+1)^3-1.
\]

Thus qr is an e=1 exclusive collision and q is forced.

No assertion about the *least* prime r is needed for the theorem; only existence
inside the exact cofactor interval matters.

## 5. Frozen exact block statistics

The independently executed certificate for

\[
10^{10}<k\le10^{10}+2000
\]

produced:

\[
\boxed{
\begin{array}{l|r}
\text{prime-q cursor states}&161{,}846\\
\text{distinct prime q values}&236\\
\text{largest }r-x&523\\
\text{smallest }Y-r&29{,}999{,}993{,}957\\
\text{largest certified r}&100{,}000{,}039{,}890{,}003{,}978{,}139
\end{array}}
\]

Every returned q and r was rechecked against the deterministic twelve-base
strong Miller--Rabin criterion below \(\psi_{12}\).

The most important number is not the small observed offset 523.  It is the
positive minimum slack: even the tightest certified state has almost
\(3\cdot10^{10}\) integers left before the cofactor upper endpoint.

This indicates that the first post-database cursor is extremely far from a
local arithmetic failure, while making no probabilistic extrapolation beyond
the frozen block.

## 6. B79 — extended complete classification theorem

Take

\[
2\le k\le10{,}000{,}002{,}000.
\]

### k<=10^10

Supplement 20 supplies the complete classification: every candidate is forced
except the five already-listed small basins and candidate sets.

### 10^10<k<=10^10+2000

- q<=k remains covered by the existing vertical Oppermann/effective-interval
  certificate stack;
- q>k with cofactor point below \(10^{20}\) remains covered by Supplement 15's
  exhaustive horizontal data;
- upper-horizon candidates remain closed by the 1724 cap and large horizon
  drift;
- the only newly uncovered lower q coordinates are the Supplement-23 cursor,
  and B78 certifies every actual prime q there individually.

Therefore no new exception appears.

Hence the five exception sets from Supplement 17 remain the **complete**
non-forced candidate list through \(10^{10}+2000\).

## 7. Executable certificate

The owner-local implementation has two layers.

`src/enterprise_math/prime_cubic_horizontal_cursor.py` provides:

- deterministic MR12 primality below \(\psi_{12}\);
- exact prime-q cursor enumeration;
- bounded search for a prime cofactor inside one state interval;
- exact block verification with certificate statistics.

`experiments/r005b_cubic_post_database_cursor.py` freezes the 2000-basin block.
The reference command is

```text
PYTHONPATH=src python experiments/r005b_cubic_post_database_cursor.py \
  --offset 2000 --assert-frozen
```

The companion unit test locks smaller reference states and the first 20-basin
summary without making the full 161,846-state certificate part of ordinary test
discovery.

## 8. Research consequence

The post-database frontier is now a **cursor computation problem**.

Extending the global Prime Gap List is only one way to move it.  Another is to
advance the sparse q cursor and certify the corresponding cofactor intervals
locally.

For the initial 57,734-basin regime, the number of integer q positions at one
new k is only 2d, and the union of q values grows linearly in d.  This creates a
practical Pareto choice:

\[
\boxed{
\text{global exhaustive gap computation}
\quad\text{vs}\quad
\text{sparse state-specific primality certificates}.
}
\]

The latter has now crossed the first finite database boundary exactly.

## 9. Boundary

The 2000-basin extension is a finite certificate, not evidence that all later
cursor states succeed.

The Sorenson--Webster MR12 theorem is external prior mathematics.  R005-B does
not claim novelty for Miller--Rabin or the pseudoprime threshold; it consumes
the threshold solely to make the local finite certificate deterministic.

No claim is made beyond k=10,000,002,000 by this supplement.
