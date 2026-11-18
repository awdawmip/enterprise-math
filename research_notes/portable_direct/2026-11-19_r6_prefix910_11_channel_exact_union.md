# PREFIX-910 — Eleven new opposite-parity multiplier channels: exhaustive 19-bit collision coverage

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6. Domain: auxiliary provenance-retaining two-port named-XOR/BRC observer. Prior verified frontier: PREFIX-909 at immutable Source commit c4d75721b97198453f084f97afc5dd42504a96bd, exact certified union 7,780,668,986 ordered pairs. Frozen scientific input identifier carried forward unchanged: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Current rules were loaded separately from scientific pins.

**Result**: Eleven additional coprime opposite-parity endpoint-multiplier families yield **3,571,456 additional distinct ordered modulus pairs**, exactly de-duplicated against C909. The explicit certificate union rises to **7,784,240,442**, leaving **9,395,628,742** pairs outside this *particular certificate union*. This remains an author proof with two independent finite exact recounts, not independent formal review or Foundation admission.

## Exact observer, theorem, and proof

Let N=2^32 and Q={262145,262147,...,524287}, |Q|=131072. Distinct named legal trajectories are Z_x=(x,x) and F_x^i=(x,x XOR 2^i) for 0<=x<N and 0<=i<32. For odd a,b in Q define Phi_(a,b)(u,v)=(u mod a,v mod b). The following constructive lemma is the general witness from PREFIX-909, reused without increasing its mathematical claim:

Let k,ell be positive integers with opposite parity, and let 1<=i<32 and s in {-1,1} satisfy k*a-ell*b=2^i+s. Put x=1-(k mod 2) for s=1, and x=(k mod 2) for s=-1. Put y=x+k*a. If x, y, x+2^i, y-s all lie in [0,N), then F_x^i=(x,x+2^i) and F_y^0=(y,y-s) are distinct legal XOR tracks with identical two-port observations.

Indeed x in {0,1} has bit i unset, so x XOR 2^i=x+2^i. Since a is odd, y mod 2=(x+k) mod 2, which equals 1 when s=1 and 0 when s=-1. Thus y XOR 1=y-s. Their start difference is y-x=k*a, their endpoint difference is (y-s)-(x+2^i)=k*a-(2^i+s)=ell*b. Both modular observations therefore agree, with source indices i and 0 retained. QED.

For the eleven families below, k<=8, a<=524287 and i<=22. Hence y<=1+8*524287=4,194,297 and x+2^i<=4,194,305; all four endpoints are within the 32-bit state range.

## Finite exhaustive census

Every (k,ell) here is coprime and of opposite parity, with 1<=ell<k<=8. Enumerate *every* odd a in Q, every i=1..22 and both s signs, solve b=(k*a-(2^i+s))/ell, and accept only exact integral odd b in Q. Validate every named XOR witness. Per-family sets eliminate repeated parameter witnesses; the predecessor C909 membership is the union of C908 and the two orientations of the exact PREFIX-909 (3,2),(4,1),(4,3) classes.

| (k,ell) | Parameter witnesses | Distinct oriented pairs | Oriented pairs outside C909 |
|---|---:|---:|---:|
| (5,2) | 78,643 | 78,643 | 34,493 |
| (5,4) | 812,650 | 792,989 | 408,202 |
| (6,1) | 43,690 | 43,690 | 27,887 |
| (6,5) | 716,531 | 699,055 | 364,840 |
| (7,2) | 56,174 | 56,174 | 27,775 |
| (7,4) | 271,508 | 266,826 | 116,177 |
| (7,6) | 636,632 | 621,029 | 325,427 |
| (8,1) | 32,768 | 32,768 | 9,371 |
| (8,3) | 54,613 | 54,613 | 26,551 |
| (8,5) | 327,680 | 321,127 | 149,296 |
| (8,7) | 575,775 | 561,732 | 295,775 |

Let A be the union of all new **positively oriented** pairs after removing C909, and A^T its transpose. Exact set construction yields |A|=1,785,732 and |A intersect A^T|=8, so the collision symmetry under time reversal/port exchange gives

```
|C910 \ C909| = |A union A^T|
               = 2*1,785,732 - 8 = 3,571,456
|C910| = 7,780,668,986 + 3,571,456 = 7,784,240,442
|Q^2 \ C910| = 131072^2 - 7,784,240,442 = 9,395,628,742.
```

An explicit newly certified pair outside C909 is a=296245, b=478469; k=5, ell=2, i=19, s=-1. Its named tracks are F_1^19=(1,524289) and F_1481226^0=(1481226,1481227). The start difference 1,481,225=5*a; the endpoint difference 956,938=2*b. The XOR transitions, state bounds, and congruences check directly. The two source labels are distinct.

## Reproducibility and evidence

- `PREFIX910_R6_OPPOSITE_PARITY_11_CHANNEL_CENSUS.py`: self-contained Python 3 stdlib integer census; reconstructs exact C908 predecessor classes and the 1,900,472 old positively oriented R909 pairs, and scans the eleven complete new families, with XOR and range assertions.
- `PREFIX910_R6_OPPOSITE_PARITY_INDEPENDENT.js`: separately written JavaScript exact safe-integer census; tests R909 algebraically rather than constructing its stored set. It also validates every named XOR transition.
- `PREFIX910_R6_OPPOSITE_PARITY_11_CHANNEL_RESULTS.json`: actual per-family outputs, overlap, verified example and domain.
- Executed Python and Node.js 22 independent algorithms on 2026-11-19. Their all-family counts, |A|, |A intersect A^T|, and the new union agree exactly. Largest JS integer intermediates are below 2^53; no floating-point approximation enters any computed count.

This certifies the specifically enumerated finite classes. Uncovered pairs are a research frontier, not an established injection family.

## Ontological scope, continuation, and source provenance

The tracks are a **typed auxiliary observation model**. P000's six native axes, native triadic closure, three-dimensional slice and independent time dimension remain untouched. No native X6 event correspondence is asserted. The prior Source pin and named source provenance are preserved.

Predecessor scientific files: `research_notes/portable_direct/2026-11-18_r6_prefix909_j0_mixed_multipliers_exact_union.md`, `PREFIX909_R6_INDEPENDENT_CHECK.py`, and `PREFIX909_R6_MIXED_MULTIPLIER_CHECK.js` at `enterprise-math@53cc9a7836bf7f34e9dafbd621c1712026b5a2f6` (files' bytes read). Source task control read `r6-20261119-0050-x6-current-continuation-read` was still QUEUED during the local scan; this independent work has no new shared CLAIM.

Next high-value test: target additional coprime opposite-parity (k,ell) with k>=9 under explicit endpoint bounds, and compare direct two-bit carry collision certificates over the complement rather than repeating already-covered channels. The mother question remains `B_fix,odd(32) in {19,20}`, unresolved.
