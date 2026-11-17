# R262 — exact minimal zero-only labelled observers

Date: 2026-11-18, Asia/Shanghai. Status: **AUTHOR_PROVED / EXACT_FINITE_VERIFICATION / NOT_REVIEWED**.
Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Direct parent: R260 and R261 on `awdawmip/enterprise-math`; the subject remains the **auxiliary 63-mask positive rational scalar model**.

## Typed observer question

Fix one of the R256/R257/R258 parameter and prime cases. For original
mask `m`, let `q_(m,k)` be the exact integer-normalized sequence for
`k>=3`, reduced modulo `p`. A *zero-only labelled observer* associated
with subset `S` decides the predicate
`Z_S(k) := (all q_(m,k)=0 mod p for m in S)`.
We require `Z_S(k)` to agree with the all-63-mask predicate
`Z_all(k)` **for every k>=3**. The empty subset is interpreted as
vacuously all-zero. Minimize |S| among original mask labels.

This is a weaker observer than constant-linear reconstruction of all
labelled values. It preserves the labels actually read; it does not
reconstruct the omitted values.

## Theorem — exact minima for all four pinned cases

| Fixed input | modulus | minimum source labels | explicit minimal set | jointly-zero k in one joint period |
|---|---:|---:|---|---|
| R256, s=67/169 | 13 | **4** | [9,10,13,26] | 1093,2185 (period 2184) |
| R257, s=770/1973 | 23 | **1** | [42] | none |
| R258, s=866/2197 | 23 | **1** | [42] | none |
| R258, s=866/2197 | 13 | **1** | [9] | none |

Proof of the three singleton cases. Their exact monic characteristic
polynomials reduce respectively to
`x^4+6x^3 = x^3(x-17)` over F_23,
`x^4+20x^3 = x^3(x-3)` over F_23,
and `x^3+6x^2=x^2(x-7)` over F_13.
The exact initial windows match the corresponding geometric progressions.
Therefore, for all `k>=3`:

- R257-p23: `q_(42,k)=17*17^(k-3) mod 23`;
- R258-p23: `q_(42,k)=10*3^(k-3) mod 23`;
- R258-p13: `q_(9,k)=5*7^(k-3) mod 13`.

Each is nonzero at every event. The all-mask zero predicate is therefore
always false, while the singleton zero predicate is also always false.
The empty observer is always true, establishing minimality 1.
In the R258-p13 case the same mask 9 also remains nonzero modulo
`13^a` for **every integer a>=1**, because its reduction modulo
13 is nonzero. Consequently, the minimum zero-only witness remains
one source at every 13-adic precision, even though the R261 minimal
constant-linear reconstruction basis grows from one to fifteen labels
over the first ten powers.

Proof of the four-source R256-p13 case. The 63 labelled sequences
all obey a common monic product annihilator of degree 249. An exact
integer-mod-13 computation checks for every mask that its first
249 outputs match the outputs shifted by `P=2184`; induction
gives an infinite sequence with period P. Across one complete period
exactly 24 masks are not identically zero. The union of their
nonzero-event sets has 2182 elements; its two missing event indices
are `k=1093` and `k=2185`. The four masks [9,10,13,26]
have exactly this same union, so their joint-zero predicate matches
all 63 at every event.

Exhaustive enumeration rejects all `C(24,3)=2024` three-mask
subsets: each fails to cover the full union. Any subset of at most
three active labels can be extended to a three-label subset, so none
works; the 39 identically-zero masks cannot improve a cover.
Therefore four is optimal. The enumeration is finite and exhaustive
within the proved full period, completing the all-event claim.

## Reproduction and evidence

Run `python R262_zero_only_observer.py` from the R260/R261 source
directory. It imports the exact R260 pinned reconstruction,
checks all four cases using modular integer arithmetic, verifies
the geometric initial conditions and characteristic factors, checks
all 249 period-shifted taps in R256 and exhausts 2024 active triples.
It emits `R262_verification.json`. There are no approximate
calculations or floating tolerances. The computational check has been
executed locally and returned PASS.

The result identifies a sharp **observer-type distinction**: over
R256 F_13, complete constant-linear reconstruction previously needed
8 named masks, whereas the exact all-zero Boolean observation needs
4; for the R258 F_13 input complete reconstruction requires 1 mask,
then more at higher 13-adic precision (R261), but zero-only observation
continues to require 1.

## Next

Classify minimal zero-only witnesses for 13-adic powers at the
R256 periodic-dip parameter, including higher-depth zero events.
Determine structural or algorithmic bounds for Boolean witness
selection without enumerating long periods. A native BRC port,
signed-source or X6 result requires an explicit typed mapping and
independent proof in that domain.
