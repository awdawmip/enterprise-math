# R005-A — Residual Arity Filtration and the Square-Basin Rank-3 Frontier

Status: `PROVED GENERIC STRUCTURE + EXACT BOUNDED P2 EVIDENCE / PRIOR-ART PRIME-GAP INPUT / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`  
Track: `R005-A — Enterprise Prime Algorithm Lab`

---

## 1. Why this checkpoint changes the p=2 frontier

The previous residual cubic-core theorem T-A20 showed that forcing every candidate witness up to

`floor(U^(1/3))`

eliminates every residual composite.

That theorem is only the first useful member of a more general filtration.

The correct object is not merely:

`residual exists / residual does not exist`.

It is:

`how many prime factors can a residual state still have after a declared forced core is known?`

This checkpoint introduces that filtration and then specializes its first nontrivial new layer to square basins.

---

## 2. Setup

Let the truth domain be an integer interval

`A < n <= U`.

Let

`F = floor(sqrt(U))`.

Candidate divisor witnesses are the primes

`q <= F`,

and witness q rejects n exactly when `q | n`.

A witness is **forced** when some composite state in the domain has q as its unique candidate divisor witness.

A composite is **residual** when it is not rejected by any forced witness.

Write

`Omega(n)`

for the total number of prime factors of n counted with multiplicity.

For an integer `m>=3`, define the m-th-root forced-core cutoff

`C_m(U) = floor(U^(1/m))`.

---

## 3. T-A21 — residual arity filtration

Assume every candidate prime witness

`q <= C_m(U)`

is forced.

Then every residual composite n satisfies

`Omega(n) <= m-1`.

### Proof

Suppose a residual n had

`Omega(n) >= m`.

Let q be its smallest prime factor.

Then

`q^m <= n <= U`,

so

`q <= floor(U^(1/m)) = C_m(U)`.

Because `m>=3`, q is certainly at most `sqrt(U)`, hence q is a candidate witness.

By hypothesis q is forced.

But q divides n, contradicting that n is residual.

Therefore no residual can have m or more prime factors.

### Interpretation

Increasing the forced core through successive root cutoffs gives a descending filtration:

`C_3 forced  -> residual arity <=2 -> no residual at all`  
`C_4 forced  -> residual arity <=3`  
`C_5 forced  -> residual arity <=4`  
`...`

T-A20 is therefore the `m=3` endpoint of a larger residual-arity theory.

---

## 4. Why every residual already has arity at least three

Independently of T-A21, every residual composite has at least two distinct candidate prime divisors.

Reason:

- if it had only one distinct candidate divisor q, the composite itself would be an exclusive collision for q;
- hence q would be forced, contradicting residuality.

A residual cannot have `Omega(n)=2`.

- `n=q^2` has singleton candidate support and forces q;
- `n=q r` with one factor above F again has singleton candidate support;
- if q and r are both candidate divisors and both non-forced, then `q^2<=A` and `r^2<=A`, hence `q r<=A`, contradicting `n>A`.

Thus:

`residual -> Omega(n)>=3`.

Combining this with T-A21 at `m=4` gives exact arity.

---

## 5. T-A22 — quartic-core three-factor normal form

Assume every candidate prime

`q <= C_4(U)=floor(U^(1/4))`

is forced.

Then every residual composite, if one exists, has exactly

`Omega(n)=3`.

Moreover every prime factor of n is at most F.

Therefore every residual has exactly one of the two forms:

1. `a^2 b`, with distinct primes `a,b<=F`;
2. `a b c`, with three distinct primes `a,b,c<=F`.

All displayed prime factors are non-forced candidate witnesses.

The form `a^3` is impossible because it has singleton candidate support.

### No-large-factor proof

Suppose an arity-3 residual had a prime factor `r>F`.

There can be only one such factor because

`U < (F+1)^2`.

The remaining two prime factors p,q satisfy

`p q = n/r < U/(F+1) < sqrt(U)`.

Hence

`min(p,q)^2 <= p q < sqrt(U)`,

so

`min(p,q) < U^(1/4)`.

That prime lies in the quartic forced core and divides the residual n, contradiction.

Therefore a quartic-core residual is F-smooth.

### Hypergraph consequence

Under quartic-core forcing, the residual support hypergraph has rank at most 3:

- `a^2 b` gives a 2-vertex edge `{a,b}`;
- `a b c` gives a 3-vertex edge `{a,b,c}`.

So the residual repair problem becomes an exact rank-3 hitting-set problem.

---

## 6. General p-power arity / prime-gap exponent

Now specialize to the p-power basin

`A=k^p`,  
`U=(k+1)^p-1`.

To force the m-th-root core, the hardest core witness has scale

`q ~ k^(p/m)`.

For the ordinary `q*r` exclusive-collision route,

`x=A/q ~ k^(p(m-1)/m)`,

while the available cofactor interval has length

`(U-A)/q ~ k^(p(m-1)/m - 1)`.

Expressed as a power of x, the required short-prime exponent is

`lambda_m(p) = 1 - m/(p(m-1))`.

This yields a whole arity phase diagram:

- `m=3`:
  `lambda_3(p)=1-3/(2p)` — enough to eliminate residuals;
- `m=4`:
  `lambda_4(p)=1-4/(3p)` — enough to force residual arity at most 3;
- larger m:
  progressively weaker arity bounds.

---

## 7. Consequence of the peer-reviewed 0.525 short-interval theorem

Baker–Harman–Pintz give the established exponent

`theta=0.525=21/40`

for primes in sufficiently short intervals.

For `p=3,m=4`:

`lambda_4(3)=1-4/9=5/9≈0.5556 > 0.525`.

Therefore:

> for all sufficiently large cubic basins, every residual composite, if one exists, must have exactly three prime factors and all of them must lie below the candidate horizon.

So the unresolved p=3 frontier is asymptotically narrower than “arbitrary residual composite”:

`possible residual`  
`-> F-smooth a^2 b or a b c`  
`-> rank<=3 residual support hypergraph`.

This does not prove that a cubic residual exists, nor that the least basis ever fails.

It only classifies the form of a hypothetical sufficiently large residual.

### Why p=2 remains exceptional

For p=2,

`lambda_m(2) = (m-2)/(2(m-1)) < 1/2`

for every finite m, and it tends to 1/2 from below.

Thus an exponent 0.525 theorem cannot force **any fixed finite residual-arity bound** in square basins through this filtration.

This is a stronger explanation of why p=2 remains structurally exceptional.

If one someday had a uniform prime-gap exponent strictly below 1/2, then sufficiently large m would begin to give finite residual-arity bounds for p=2. No such input is assumed here.

---

## 8. Exact square-basin atlas through k=10000

For the square basin

`k^2 < n < (k+1)^2`

the exact factor horizon is simply

`F=k`.

A dedicated integer SPF scanner exhaustively evaluated every basin through

`k<=10000`,

hence every integer state through

`n<=100,020,000`.

It performs two exact passes per basin:

1. identify forced witnesses from singleton candidate support;
2. enumerate residual composites and factor them exactly.

The old `k<=2000` atlas is embedded as a hard regression check.

### Regression

The previously known 35 bad basins through k=2000 are reproduced exactly.

The previously known residual count through k=2000 is reproduced exactly:

`36`.

### Extended result through k=10000

- basins containing residual composites: `45`;
- total residual composites: `46`;
- first bad basin: `k=25`;
- maximum residual composites in one basin: `2`;
- residuals with a prime factor above the horizon k: `0`;
- residuals with `Omega>=4`: `0`;
- arity distribution:
  - `Omega=3`: `46`;
- support-rank distribution:
  - rank 2: `41`;
  - rank 3: `5`.

Thus every exact residual found through `10^8` is already of the T-A22 three-factor normal form.

This is bounded evidence, not an all-k theorem.

---

## 9. Exact rank-3 examples

Five rank-3 residuals occur through k=10000:

- `k=888`:
  `790079 = 73 * 79 * 137`;
- `k=1078`:
  `1163243 = 37 * 149 * 211`;
- `k=1162`:
  `1351447 = 43 * 53 * 593`;
- `k=1781`:
  `3175339 = 101 * 149 * 211`;
- `k=4412`:
  `19469647 = 193 * 281 * 359`.

The other 41 residuals have support rank 2 and form `a^2 b`.

Two examples show that the squared prime need not be the smaller support prime:

- `2375507 = 107 * 149^2`;
- `2819527 = 127 * 149^2`.

So even inside the rank-2 class, the correct normal form is `a^2 b` up to relabelling, not “the smaller prime is always squared”.

---

## 10. New bad square basins beyond the old k<=2000 atlas

New residual basins found before k=10000 include:

- `k=2073`: `4299913 = 97^2 * 457`;
- `k=2164`: `4684411 = 149^2 * 211`;
- `k=2850`: `8126977 = 137^2 * 433`;
- `k=4412`: `19469647 = 193 * 281 * 359`;
- `k=5833`: `34032191 = 281^2 * 431`;
- `k=5834`: `34038679 = 181^2 * 1039`;
- `k=6339`: `40191149 = 281^2 * 509`;
- `k=7289`: `53140753 = 281^2 * 673`;
- `k=8584`: `73697461 = 199^2 * 1861`;
- `k=9369`: `87788213 = 397^2 * 557`.

The complete exact list is preserved in the JSON snapshot.

---

## 11. Quartic-core diagnostic in the same atlas

The scanner also checks whether every prime

`q <= floor(U^(1/4))`

is forced.

Through k=10000 there is exactly one failure of this sufficient condition:

`k=121, q=11`.

Yet the k=121 basin contains no residual composite.

So:

> quartic-core forcing is sufficient for the three-factor theorem, but it is not necessary.

The failure is arithmetically understandable:

- `11^4 = 121^2` lies exactly on the lower basin boundary, not inside it;
- the relevant large-prime cofactor windows do not supply a singleton-support certificate.

Nevertheless the remaining forced witnesses still cover the whole basin.

This is a useful negative boundary against identifying “core sufficient condition” with “exact necessary condition”.

---

## 12. Residual-semigroup interpretation

Let `N_k` be the non-forced candidate prime set in a square basin.

A residual composite is exactly a basin composite whose candidate prime divisors all lie in `N_k`.

The exact atlas suggests that, at least through k=10000, the first nonempty part of this residual semigroup always hits the basin at total factor arity 3.

The observed residual shell therefore consists only of:

`a^2 b`  
or  
`a b c`

over non-forced candidate primes.

This motivates a more efficient next search:

do not enumerate all composites.

Instead:

1. compute the non-forced witness set;
2. enumerate only triple products from it that can enter the square shell;
3. separately search for the first possible four-factor residual beyond the quartic-core protection.

That is the natural p=2 continuation.

---

## 13. Foundation feedback candidate

`FF-R005A-10 — Residual arity filtration`

Candidate reusable theorem family:

`forced C_m(U) -> residual Omega <= m-1`.

Special quartic consequence:

`forced C_4(U) -> residuals are exactly F-smooth rank<=3 states`.

Relation:

`A2 minimal observation language + A4 support arity/hypergraph + A0 root scale`.

Status:

`PROVED GENERIC STRUCTURE / PRIOR-ART SHORT-PRIME INPUT / NOVELTY UNVERIFIED`.

No claim is made that the generic smallest-prime-factor argument is new mathematics.

The Enterprise Math contribution under investigation is the use of root-scaled forced cores to stratify residual observation complexity and to connect collapse exponent to residual hypergraph rank.

---

## 14. Next frontier

The p=2 route should now stop asking only:

`does a least basis exist?`

and instead ask:

1. can an `Omega>=4` residual exist at all?
2. can a residual contain one prime factor above the screening horizon?
3. is there a stronger square-basin-specific argument forcing eventual rank<=3 without a generic prime-gap exponent below 1/2?
4. what exact non-forced-prime conditions characterize the two residual families `a^2 b` and `a b c`?
5. can residual search be converted from integer enumeration into a sparse triple-product / reciprocal-gap search?

The first counterexample to rank 3, if it exists, is now the most informative p=2 computational target.
