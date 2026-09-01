# R005-B — Cubic Lower Cofactor Finite Closure through Current Prime-Gap Data

Status: `PROVED R005 REDUCTION + EXACT PREFIX CERTIFICATE + EXTERNAL COMPUTATION TRANSFER / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: R005-A T-A16; R005-B Supplements 02, 08, 12, 14

## 1. Result

The cubic lower cofactor-gap band can be closed on a large finite range without
scanning basin witnesses q.

Two ingredients suffice:

1. an exact R005-B necessity theorem:

   \[
   \boxed{
   \text{lower-band e=1 failure at a consecutive gap }a<b
   \Longrightarrow
   (b-a)^3>27a;
   }
   \]

2. a complete consecutive-prime-gap prefix certificate.

A reproducible standard-library sieve through

\[
190{,}000{,}000
\]

contains exactly

\[
10{,}555{,}473
\]

primes and finds exactly one consecutive gap with

\[
(b-a)^3>27a:
\]

\[
\boxed{1327<1361,\qquad b-a=34.}
\]

The exact reciprocal carry compiler proves that this exceptional gap never
captures an integer q in the cubic lower band.

Using the current 2026 Prime Gap List data:

- exhaustive prime-gap analysis is reported through \(10^{20}\);
- the last confirmed maximal gap beginning below \(10^{20}\) has size 1724,
  starting at 68068810283234182907;
- the next larger maximal gap, 1854, starts at 101412319996363309069, already
  above \(10^{20}\).

Therefore, as an inference from those two external tables, every consecutive
prime gap with start below \(10^{20}\) has size at most 1724.

Since

\[
\boxed{
\left\lceil\frac{1724^3}{27}\right\rceil
=189{,}778{,}942,
}
\]

the exact 190-million prefix and the external 1724 cap overlap.  Consequently:

\[
\boxed{
\text{there is no cubic lower-band e=1 failure whose cofactor-gap start is}<10^{20}.
}
\]

Converting the cofactor range back to the cubic basin coordinate gives

\[
\boxed{
2\le k\le5{,}848{,}035
}
\]

as a current-data finite closure range for the **entire lower band**
`q F_3(k) <= k^3`.

Every lower-band candidate prime q in that range has an e=1 exclusive cofactor
certificate and is therefore forced.

This is not full cubic forcing: horizon/upper candidates remain a separate
mechanism and explicit upper failures already exist inside this k range.

---

## 2. B45 — any cubic lower-band failure forces a cube-root-supercritical prime gap

Let

\[
A=k^3,
\qquad
U=(k+1)^3-1,
\qquad
F=F_3(k)=\lfloor\sqrt U\rfloor.
\]

Take a candidate prime witness q in the lower cofactor band

\[
\boxed{qF\le A.}
\]

Put

\[
x=A/q.
\]

Let a be the largest prime at or below x and b the next prime after a.  Thus
`a<b` are consecutive and `a<=x<b`.

Suppose the e=1 exclusive cofactor route fails.  Then

\[
\boxed{qb>U.}
\]

We prove

\[
\boxed{(b-a)^3>27a.}
\]

### Preliminary lower bound on the factor horizon

For every k>=1,

\[
F>\sqrt A=k^{3/2}.
\]

Indeed the integer

\[
t=\lfloor\sqrt A\rfloor+1
\]

satisfies

\[
t^2<(\sqrt A+1)^2
=A+2k^{3/2}+1
<U,
\]

because

\[
3k^2+3k>2k^{3/2}+1.
\]

Hence `t<=F` and `F>sqrt(A)`.

### Case I — a>=F

Since `a<=A/q` and `qb>U`,

\[
\frac ba>\frac UA.
\]

Therefore, with `g=b-a`,

\[
\frac ga
>
\frac{U-A}{A}
=
\frac{3(k+1)}{k^2}.
\]

Thus

\[
g>
\frac{3a(k+1)}{k^2}.
\]

But `a>=F>k^(3/2)`, so `a^(2/3)>k`, and hence

\[
\frac{a(k+1)}{k^2}
>
a^{1/3}.
\]

Therefore

\[
\boxed{g>3a^{1/3}}.
\]

### Case II — a<F

The lower-band bound gives

\[
q\le A/F.
\]

Since `qb>U`,

\[
b>\frac{UF}{A}.
\]

Hence

\[
g=b-a>b-F>
F\frac{U-A}{A}
=
\frac{3F(k+1)}{k^2}.
\]

Again `F>k^(3/2)`, so

\[
\frac{F(k+1)}{k^2}>F^{1/3}>a^{1/3}.
\]

Thus

\[
\boxed{g>3a^{1/3}}.
\]

Both cases give

\[
\boxed{g^3>27a.}
\]

This theorem is stronger than the strict PRE-only real-window criterion from
Supplement 08: it also covers a lower-band candidate whose cofactor gap is
already being crossed by the moving factor horizon.

---

## 3. B46 — bounded absolute gap kills the lower mechanism above one finite a

If an external computation supplies the uniform bound

\[
g\le G,
\]

then B45 shows that a lower failure is impossible whenever

\[
G^3\le27a.
\]

Therefore the exact cutoff is

\[
\boxed{
a\ge A_G:=\left\lceil\frac{G^3}{27}\right\rceil.}
\]

Two useful values are

\[
\boxed{A_{1328}=86{,}742{,}206}
\]

and

\[
\boxed{A_{1724}=189{,}778{,}942.}
\]

Thus a finite gap table plus one exact prime prefix is enough to close an
otherwise enormous cofactor range.

---

## 4. B47 — exact 190-million prefix certificate

The companion experiment

`experiments/r005b_cubic_lower_gap_prefix.py`

uses a standard-library bytearray Eratosthenes sieve and tests the exact integer
predicate

\[
(b-a)^3>27a
\]

for every consecutive prime gap in the prefix.

Frozen full command:

```text
python experiments/r005b_cubic_lower_gap_prefix.py --limit 190000000 --assert-current-certificate
```

The certificate is:

```text
prime_count = 10,555,473
cube_root_supercritical_gaps = [(1327,1361,34)]
```

No floating-point cube root is used.

An independent NumPy Eratosthenes implementation was also run during discovery
and produced exactly the same count and unique crossing.  The repository
certificate deliberately does not require NumPy.

### The exceptional 1327→1361 gap still does not produce a lower q

The only supercritical prefix gap has the following relevant cubic states.

At k=119:

\[
F_3(119)=1314<1327,
\]

but its lower-band reciprocal integer interval is empty:

\[
[1270,1269].
\]

At k=120 and 121 the factor horizon lies inside the gap, but after intersecting
with the lower band `qF<=A` the intervals remain empty:

\[
[1302,1299],
\qquad
[1335,1315].
\]

At k=122,

\[
F_3(122)=1364\ge1361,
\]

so the gap has retired from the exclusive-cofactor role.

Thus the unique real-supercritical prefix gap creates **no lower-band integer q
at all**.

---

## 5. B48 — current 2026 external gap-table transfer

The Prime Gap List project's current exhaustive-analysis page reports that all
prime gaps have been exhaustively analyzed through

\[
\boxed{10^{20}}
\]

as of 8 May 2026.

Its current maximal-gap table lists the confirmed record

\[
\boxed{1724}
\]

starting at

\[
68068810283234182907<10^{20},
\]

while the next larger record

\[
1854
\]

starts at

\[
101412319996363309069>10^{20}.
\]

Because the interval through `10^20` is exhaustive, these tables together imply
that every consecutive gap beginning below `10^20` has length at most 1724.

This is an **external computation premise/inference**, not an Enterprise Math
proof of the prime-gap database.

Now

\[
A_{1724}=189{,}778{,}942<190{,}000{,}000.
\]

For `a>=A_1724`, the bound `g<=1724` contradicts B45.  For `a<A_1724`, the exact
prefix certificate applies and the only possible gap 1327→1361 was already
eliminated at the integer layer.

Therefore

\[
\boxed{
\text{no lower-band e=1 failure occurs for any cofactor gap starting below }10^{20}.
}
\]

---

## 6. B49 — conversion to the cubic basin coordinate

For any candidate prime q,

\[
q\ge2,
\]

so its cofactor point satisfies

\[
x=\frac{k^3}{q}\le\frac{k^3}{2}.
\]

To stay conservatively inside the external exhaustive range even after one
maximal allowed gap, require

\[
\boxed{
\frac{k^3}{2}+1724<10^{20}.
}
\]

The largest integer satisfying this strict inequality is

\[
\boxed{k=5{,}848{,}035.}
\]

Indeed

\[
\frac{5{,}848{,}035^3}{2}+1724<10^{20},
\]

whereas the next k crosses the selected boundary.

Consequently:

\[
\boxed{
\forall\,2\le k\le5{,}848{,}035,
\quad
qF_3(k)\le k^3
\Longrightarrow
q\text{ has an e=1 exclusive cofactor certificate}.
}
\]

So the complete lower candidate band is forced throughout this finite range.

Again, this does **not** say the full candidate set is forced.  The upper
horizon band has its own failures; e.g. the already-recorded cubic examples at
k=23,64,120,138,1005 live there.

---

## 7. Conservative replay of the older R005-A external premise

R005-A already recorded a deliberately conservative external premise based on
the Oliveira e Silva computation:

\[
g\le1328
\]

through a selected double-checked region below

\[
4\cdot10^{17}.
\]

Keeping that older source layer unchanged gives

\[
A_{1328}=86{,}742{,}206.
\]

An exact prefix sieve through 87,000,000 again finds only 1327→1361 above the
cube-root line, and that gap has no lower integer q.

The conservative cofactor-endpoint condition

\[
\frac{k^3}{2}+1328<4\cdot10^{17}
\]

gives

\[
\boxed{k\le928{,}317.}
\]

Thus there are two honest finite frontiers:

1. `k<=928,317` using the already-consumed R005-A premise;
2. `k<=5,848,035` using the current 2026 Prime Gap List exhaustive extension.

The second extends rather than silently rewrites the first.

---

## 8. Architectural consequence

For a large explicit finite range the cubic candidate language now separates as

\[
\boxed{
\text{lower cofactor band: completely e=1 forced}
}
\]

versus

\[
\boxed{
\text{horizon/upper band: the only remaining source of full-forcing failure}.
}
\]

This is a stronger finite statement than the asymptotic lower-gap phase diagram:
it removes the entire lower mechanism, not merely a small sufficient core.

It also demonstrates a useful research pattern:

\[
\text{structural cube-root necessary condition}
\to
\text{small exact prefix search}
\to
\text{external uniform gap cap}
\to
\text{huge finite witness closure}.
\]

The computational burden is paid only below `ceil(G^3/27)` rather than across
the full external prime-gap range.

---

## 9. Status / prior-art boundary

Eratosthenes sieving, record prime-gap computation and exhaustive prime tables
are prior mathematics/computation.

External 2026 inputs in B48 come from the Prime Gap List project's current
exhaustive-analysis and maximal-gap tables.  The older 1328/`4e17` premise is
consumed exactly as already recorded by R005-A.

R005-B owns only the factor-horizon / reciprocal-witness reduction, exact cutoff
conversion, prefix certificate artifact and project-side finite closure.

No claim is made that the external databases themselves are independently
reproved here.  No theorem here settles cubic full forcing beyond the stated
finite lower-band range or removes the separate upper mechanism.
