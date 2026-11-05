# PREFIX-513 — Exact W-prefix for the native negative-b displacement fiber

Date: 2026-11-05 Asia/Shanghai. Classification: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific pin (unchanged): `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: PREFIX-512, `2026-11-05_prefix512_positive_b_single_displacement_W_prefix.md`.
Role: author-side independent research attached to the open X6 native path-fiber direction; formal Task CLAIM not made. Mother target remains full signed native C6 triad dynamics and observer-safe path composition.

## Theorem (all m, exact integer arithmetic)

Fix `m >= 0`, `n = 2m+1`, and the original ordered signed ten-direction step alphabet `a,A,b,B,c,C,d,D,e,E` with net displacement `y=(0,-1,0,0,0)` inside the restricted native X6 path family. Its cancellation occupations `p_a,p_b,p_c,p_d,p_e` are nonnegative and sum to `m`; the b-axis has one additional native negative `B` step. Keep the BRC observer

```text
V = p_b + 2*p_d + p_e,
W = p_c + p_e.
```

Use the inherited five-color terminal KMP mapping `(a,A,b,B,c,C,d,D,e,E) -> (0,4,1,2,3,3,4,4,4,4)`, gate `g=aab` or `g=aba`, terminal KMP prefix length `q=0,1,2,3`, and first b/B-versus-c/C source `t=B,C`. Every path has at least one b/B step, hence t=N is absent.

For nonnegative occupancy thresholds `alpha,beta,gamma` (`p_a>=alpha,p_b>=beta,p_c>=gamma`), let `P(alpha,beta,gamma;j)` count distinct observation pairs `(W,V)` with `W<j`. Its full integer support is precisely

```text
gamma <= W <= m-alpha-beta,
beta <= V <= 2*m - W - 2*alpha - beta - gamma.
```

An invalid row is empty. Put
```text
J = max(0,min(j,m-alpha-beta+1)-gamma).
P(alpha,beta,gamma;j)
  = J*(2*m-2*alpha-2*beta-gamma+1)
    - J*(2*gamma+J-1)/2.
```
The second numerator is always even.

The following eight mutually disjoint controller labels have exactly those occupancy-support predicates, for all integers `m>=0` (each table entry is the triple `alpha,beta,gamma`):

| Gate | (q=0,B) | (q=1,B) | (q=2,B) | (q=3,B) | (q=0,C) | (q=1,C) | (q=2,C) | (q=3,C) |
|---|---|---|---|---|---|---|---|---|
| aab | (0,0,0) | (1,0,0) | (2,0,0) | (2,1,0) | (0,0,1) | (1,0,1) | (2,0,1) | (2,1,1) |
| aba | (0,0,0) | (1,0,0) | (1,1,0) | (2,1,0) | (0,0,1) | (1,0,1) | (1,1,1) | (2,1,1) |

The **complete source- and KMP-resolved W-prefix** is the sum of these eight P terms; thus its query cost is O(1) exact integer operations with no W index. The p_b threshold is different from the surplus negative B: q=2/3 needing a *positive* terminal b requires a paired positive b and so beta>=1. Compared with PREFIX-512 for positive b, the extra negative B can be positioned before a positive terminal b; no exceptional R source-order correction is necessary.

Let `Phi(h)=(h+1)*(3h+2)/2` for h>=0, and 0 otherwise. The full distinct joint observer counts for **either gate** agree:

```text
S_negative_b(m) = Phi(m)+2*Phi(m-1)+2*Phi(m-2)
                  +2*Phi(m-3)+Phi(m-4).
```

This numerical equality between the gates is **not** equality of controller-resolved (V,W) fibers: the q=2 rows use different beta shifts.

## Proof

**Occupancy interval.** Fix W. Write `p_a=alpha+h_a, p_b=beta+u, p_c=W-e, p_d=v, p_e=e` where `0<=e<=W-gamma`, `u,v,h_a>=0`, and `u+v+h_a=H=m-alpha-beta-W`. For fixed e the value `u+2v` attains every integer in `[0,2H]`: for `z<=H`, take `u=z,v=0`; for `H<z<=2H`, take `v=z-H,u=2H-z`. Translating by `e=0,...,W-gamma` gives precisely the interval `[beta,beta+2H+W-gamma]` stated in the theorem. This directly constructs a signed path with the required occupations by using the supplied surplus negative B and arbitrary ordering of the paired positive/negative steps.

**Prefix.** Each W row contains `2m-2alpha-2beta-gamma-W+1` distinct V values. Its allowed W range starts at gamma and ends at m-alpha-beta. Summing that arithmetic progression for `gamma<=W<j` gives P. As `J=0` for empty ranges, the expression also covers negative j, m smaller than the threshold sum, and all boundary cases.

**Exact KMP and first source.** Under the inherited five-color map, only native positive a yields KMP character a, and only native positive b yields KMP character b. Thus the terminal statuses are realized by the suffixes: q=1 -> `a` (alpha>=1), aab q=2 -> `aa` (alpha>=2), aba q=2 -> `ab` (alpha>=1,beta>=1), and either q=3 -> the complete gate (alpha>=2,beta>=1). Place any extra ordered primitives before the desired suffix. An available negative native B, colored 2, can be placed just before the suffix to prevent an accidental longer a-prefix; its existence is guaranteed by y_b=-1. For source B put one negative B before c/C; for source C, require p_c>=1 and put a c/C before all b/B steps, then the surplus negative B before the suffix. The specified first-source order is preserved. To obtain q=0, finish with a non-a native step; the surplus B itself can be final for source C, while for source B one uses a remaining non-a step (a negative A when p_a>0, another b/B when p_b>0, c/C when p_c>0, or d/e when present). When m=0, the single negative B already ends at q=0 and first source B. These constructions establish all table rows. Conversely each q and source requires the indicated native positive letters and/or c/C occurrence, giving the listed threshold necessities.

**Totals.** The complete P count with `j>m` depends only on `h=m-alpha-beta-gamma`; it equals `Phi(h)`. For either gate, the eight thresholds have sums 0,1,1,2,2,3,3,4. Adding their Phi counts proves the S formula. The gate-dependent q=2 fibers nevertheless have different V lower bounds.

## Executed exact verification

The companion `prefix513_compact_certificate.py` uses a native step-by-step 10-direction signed path DP with displacement/remaining-steps pruning. KMP and first-source are updated from each signed primitive, independently of P. It compares exact (V,W,q,t) sets for each row, then verifies every W-prefix and a separate wide-range integer formula check.

Actual CPython execution: `ALL_CHECKS_PASS`. For each gate the exhaustive native fibers at n=1,3,5,7,9 have respectively 1,7,24,58,114 distinct joint states. Across both gates: 30 native W rows; 408 joint-state memberships; 70 prefix equalities; 4,270 additional m=0..60 analytic checks. The actual JSON is in `PREFIX513_EXACT_EXECUTION.json`. Arbitrary-m theorem strength comes from the constructive proof, not the finite checks. Integer-operation complexity omits growing integer bit lengths.

## Research bridge and next discriminating question

BRC is the exact occupation-and-provenance observer here; KMP/source tags retain ordering information lost by (V,W) alone. This is a signed native-X6 path *restricted fiber*, not a new spatial dimension or a physical rotation law. Next PREFIX-514: compute the sign-reflected c-axis cases `y=(0,0,+1,0,0)` and `y=(0,0,-1,0,0)`, checking for new first-source/terminal obstructions and deriving the four-sign classification for `|y_b|+|y_c|=1`. The mother X6 triad C6 generator/path composition problem remains in the formal Task.

Sources: project frozen scientific pin above; PREFIX-508 mod-6 support compiler, PREFIX-509 direct ranks, PREFIX-511 zero-displacement W-prefix, PREFIX-512 positive-b fiber; current research continuation and portable method protocols (2026-11-05).
