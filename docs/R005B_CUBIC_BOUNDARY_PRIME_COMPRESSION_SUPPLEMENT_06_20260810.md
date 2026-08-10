# R005-B — Cubic Boundary-Prime Compression

Status: `PROVED WIP / DRAFT OWNER SUPPLEMENT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 02–05

## 1. Result

The cubic pure-cap failure **existence** question does not require the complete
prime slice.

For `k>=3`, write

\[
A=k^3,\qquad
U=(k+1)^3-1,
\]

\[
S=\lfloor\sqrt A\rfloor,\qquad
F=\lfloor\sqrt U\rfloor.
\]

Let

\[
\boxed{Q=\max\{q\le S:q\text{ prime}\}},
\]

and

\[
\boxed{R=\min\{r>F:r\text{ prime}\}}.
\]

Then the cubic pure-cap non-forced set is nonempty if and only if

\[
\boxed{QF>A\quad\text{and}\quad QR>U.}
\]

When it is nonempty, `Q` itself is the **largest non-forced pure-cap witness**.

Thus the yes/no query

> does the cubic upper pure cap contain any non-forced candidate?

compresses from a whole prime slice to exactly two boundary primes.

This is a task-relative state reduction. Recovering the *entire set* of
non-forced witnesses still requires the prime-slice data from Supplement 04.

---

## 2. B25 — canonical maximal obstruction theorem

Supplement 04 proved that the cubic non-forced pure-cap witnesses are exactly

\[
\left\{q\text{ prime}:\max\left(\left\lfloor\frac AF\right\rfloor,
\left\lfloor\frac UR\right\rfloor\right)<q\le S\right\}.
\]

The interval is an upper interval ending at `S`. Therefore, if it contains any
prime at all, it contains the largest prime `Q<=S`. Conversely, if `Q` does not
lie in the interval, no smaller prime can lie in it.

Since `Q` is an integer,

\[
Q>\left\lfloor\frac AF\right\rfloor\iff QF>A,
\]

and

\[
Q>\left\lfloor\frac UR\right\rfloor\iff QR>U.
\]

Hence

\[
\boxed{\operatorname{NonForcedCap}_{3,k}\ne\varnothing
\iff QF>A\ \land\ QR>U.}
\]

When this holds, `Q` is the maximum element of that non-forced set. ∎

This replaces an interval-occupancy existence test by one canonical witness.

---

## 3. Nearest-gap coordinates

Define the left prime lag and right prime gap by

\[
\boxed{\ell=S-Q,\qquad g=R-F.}
\]

Also define the deterministic structural margins

\[
\boxed{\Delta=FS-A,\qquad E=RS-U.}
\]

Then

\[
QF-A=(S-\ell)F-A=\Delta-\ell F,
\]

and

\[
QR-U=(S-\ell)R-U=E-\ell R.
\]

Therefore B25 is equivalent to

\[
\boxed{\ell F<\Delta,\qquad \ell R<E.}
\]

Equivalently,

\[
\boxed{\ell<\min\left(\frac\Delta F,\frac ER\right).}
\]

No probability or independence is being asserted. The result only says that
the cubic upper-cap existence question is determined by two nearest-prime
distances plus deterministic basin geometry.

---

## 4. Relation to the opening/saturation law

Supplement 05 described the right gap `g=R-F` by three phases.

The second margin can be written

\[
E=RS-U.
\]

Thus:

- `E<=0`: the raw q-window is closed;
- `E>0`: a raw q-window has opened;
- once the moving wall crosses the fixed horizon wall, the allowed left-lag
  threshold stops increasing.

B25 adds the missing left-side condition:

\[
\boxed{\text{open right window}+\text{sufficiently small left prime lag}
\iff\text{actual cubic pure-cap failure}.}
\]

The right gap creates capacity; the predecessor prime below `S` decides whether
that capacity is occupied.

---

## 5. Selected exact examples

The canonical boundary pairs are:

| k | S-side Q | horizon F | R | result |
|---:|---:|---:|---:|---|
| 23 | 109 | 117 | 127 | Q is non-forced |
| 64 | 509 | 524 | 541 | Q is non-forced |
| 120 | 1307 | 1330 | 1361 | Q is non-forced |
| 138 | 1621 | 1638 | 1657 | Q is non-forced |
| 1005 | 31859 | 31907 | 31957 | Q is non-forced |

For `k=120` the full non-forced slice contains both `1303` and `1307`, but the
existence question needs only the maximal one, `Q=1307`.

This is the exact distinction between:

- **existence precision** — two boundary primes suffice;
- **identity/count precision** — retain the full prime slice.

---

## 6. A2/A4 interpretation

If the declared future query is only

\[
\text{“does an upper pure-cap obstruction exist?”},
\]

all internal prime identities below the maximal boundary prime are
future-irrelevant. The state can be compressed to `(Q,R)` or equivalently the
gap pair `(ell,g)` together with the deterministic basin coordinates.

If the future may ask “which candidates are non-forced?” or “how many are
there?”, that compression is no longer sufficient and the whole prime slice is
reactivated.

Generic future-quotient ownership remains A2/P023; this supplement only
supplies the R005-B arithmetic specialization.

---

## 7. Executable checkpoint

`src/enterprise_math/prime_cubic_boundary.py` implements:

- previous prime at or below a boundary;
- the cubic boundary-prime pair `(Q,R)`;
- the canonical maximal non-forced pure-cap witness;
- exact left/right gap and product-margin coordinates.

`tests/test_prime_cubic_boundary.py` compares the two-boundary-prime compiler
against the existing exact cubic prime-slice compiler for every `3<=k<2000`,
and locks the margin identities.

No floating-point arithmetic is used.

---

## 8. Boundary

This theorem concerns only the **cubic upper pure horizon cap**. It does not
classify the lower cofactor-gap band, the complete cubic forced core, or whether
cubic full-forcing failures are finite or infinite.
