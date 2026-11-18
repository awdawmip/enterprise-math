# R749SUQ — An exact O(sqrt(M)) segmented closest-divisor optimizer for the labeled two-Port feedback problem

Date: 2026-11-18 (Asia/Shanghai). Status: `AUTHOR_EXACT_NOT_REVIEWED`. Scope: auxiliary finite-positive-rational WBRC-T30–T32 two-Port feedback-bin observer with **named** Ports. The native X6 event interface is unchanged.

## Frozen inputs, provenance, and the selected mathematical question

- Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30–T32).
- R749SUO, immutable `161123938bc7836d62d130a755b3d6601a743182`, establishes for every `M >= 116` that all noncanonical labeled maximizers of `max(u,v)ad`, under `ad-uv=1` and `1<=a,u,v,d<=M`, have `Q=u+v-a-d=+1`; it gives a bijective nearest-factor optimization and labeled tie reconstruction.
- R749SUP at the same immutable commit proves for `M >= 9999` that all optimal configurations have oriented `u=max(u,v)>=p`, for explicitly constructed `p` with `0<=M-p<=2ceil(sqrt(floor(sqrt(M+1))))+1`. Its previous exact algorithm performs `O(M^(3/4))` integer operations by independently trial-dividing each `n=u+1` in the short interval.
- Current P000 and ACTIVE worldview supply six native spatial axes, three-dimensional slices, source and residual fidelity, triadic equilibrium and causal/resource permissions. This matrix is a typed auxiliary feedback observer; the present work makes no native-event equivalence assertion.

**Question:** Can the short boundary layer be processed collectively rather than independently trial-dividing each integer, while still returning every labeled optimal configuration?

## Theorem — segmented divisor marking

For every integer `M >= 9999`, put `t=floor(sqrt(M+1))`, `k=M+1-t^2`, `j=1` if `k<=t`, otherwise `j=2`, and

```
z = min{integer z>=0: z(z+j)>=j*t-k},
r=t-z, s=t+z+j,
p=rs-1,
L=p+1, U=M+1, w=U-L+1=M-p+1,
D=floor(sqrt(U)).
```

Allocate a length-`w` integer array `c`, initially zero. For each `d=2,3,...,D`, in **increasing** order, mark precisely the multiples

```
n = first, first+d, ..., <=U,
first = max(d*d, d*ceil(L/d)),
```

setting `c[n-L]=d`. Then for every integer `n in [L,U]`, `c[n-L]` is exactly the greatest divisor `x_n` of `n` satisfying `2<=x_n<=sqrt(n)`, or zero if `n` is prime. For each nonzero entry write `y_n=n/x_n` and evaluate

```
v_n=n-x_n-y_n,
T_n=(n-1)*(n-x_n-1)*(n-y_n-1).
```

Ignore `v_n<1`. The maximum of `T_n` is the exact maximum **over noncanonical named configurations** in the frozen problem. Every maximizing `n` produces all its labeled configurations by

```
(a,u,v,d)=(n-x_n-1, n-1, n-x_n-y_n, n-y_n-1)
```

and the diagonal-label swap `x_n<->y_n` (if distinct) and directed-Port swap `u<->v`. The exact multiplicity is 2 when `x_n=y_n`, otherwise 4, summed over tied `n`.

The complete computation takes

```
O(sqrt(M) + w log M) = O(sqrt(M)) integer arithmetic operations,
O(w) = O(M^(1/4)) auxiliary integer words.
```

The output enumeration adds its actual number of labeled optima. Arithmetic-count complexity is stated in integer operations; each input integer has `O(log M)` bits and scores have `O(log M)` bits, so arbitrary-precision bit cost depends on multiplication and division costs.

### Proof

**Correctness of the segmented sieve.** Fix `n in [L,U]` and a positive divisor `d>=2` with `d<=sqrt(n)`. Then `d<=D`, `d*d<=n`, and `n` is a multiple of `d` no smaller than `L`. Hence the `d`-loop marks `n`. Conversely, every marked `n` satisfies `d*d<=n`, `d|n` and `L<=n<=U`. Because `d` increases, the last value stored at `n` is precisely the greatest such divisor. No mark is stored if there is none.

**Optimality and reconstruction.** R749SUO proves `Q=1` for all noncanonical maximizers at these scales and, after orientation, `xy=n=u+1` with `x=u-a`, `y=u-d` positive. For fixed `n`, maximizing `(n-1)(n-x-1)(n-y-1)` is equivalent to minimizing `x+y`, attained by the factor pair closest to `sqrt(n)`. R749SUP proves `u>=p`, so all maximizing `n` lie in `[L,U]`. The segmented sieve finds exactly the required closest pair for every candidate `n`. The two independent label swaps yield precisely the stated 2/4 configurations; the Port pair is unequal because `u-v=x+y-1>0`. Therefore the algorithm returns the maximum and all ties.

**Time and space.** Computing `t` by integer square root and the smallest `z` by a scan uses `O(M^(1/4))` simple integer operations. For each `d` the first-multiple computation is constant-time in the integer-operation model; at most `1+w/d` marks are made. Thus the total number of operations is bounded by `O(D+w sum_(d=2)^D (1/d)) = O(sqrt(M)+w log M)`. The R749SUP boundary theorem gives `w<=2ceil(sqrt(t))+2=O(M^(1/4))`; hence `w log M=O(sqrt(M))`. The only bulk array is `c` of length `w`; keeping all tied factor pairs also fits in `O(w)` words. QED.

## Exact computational evidence

The companion standard-library Python file `R749SUQ_SEGMENTED_DIVISOR_CERT.py` runs two independent comparisons. First it constructs a full-prefix closest-divisor oracle, then checks every integer `M=9999,...,25000` (15,002 scales), including exact score and all labeled-tie counts. Second it directly tests *every* possible factor `d<=sqrt(n)` for each candidate `n` at `M=9999,10000,25000,100000,1000000,100000000` (6 scales); both methods agree. All arithmetic is Python arbitrary-precision integer-exact, without floating point or probabilistic factoring. Output: `R749SUQ_SEGMENTED_DIVISOR_RESULTS.json`, `status=PASS`.

| M | candidate interval width | maximum score | labeled maximizers |
|---:|---:|---:|---:|
| 9,999 | 11 | 979804019799 | 2 |
| 25,000 | 12 | 15420641299674 | 4 |
| 100,000 | 12 | 993550256897434 | 4 |
| 1,000,000 | 58 | 997998004001997999 | 2 |
| 100,000,000 | 102 | 999799980004000199979999 | 2 |

The general theorem uses the cited exact R749SUO/SUP structural arguments plus the proved sieve invariant. These finite tests validate the implementation and its reconstruction, not an independently admitted Foundation theorem.

## Relation to existing methods and next question

The independent per-product trial division of R749SUP takes `O(M^(3/4))` operations; the present work shares divisor marks across all candidate products and takes `O(M^(1/2))`, with a compact `O(M^(1/4))` working array. It is a classical segmented divisor-sieve optimization applied to the proven Enterprise Math feedback boundary layer, not a claim to invent sieve theory or to improve every general integer-factorization problem.

Next scientific problems: (1) establish any *sharper* extremal bound on the offset `M-u` than the present `O(M^(1/4))` window, using number-theoretic information about near-square products; (2) determine whether the interval closest-divisor stage admits sub-square-root exact arithmetic time for all M, with honest preprocessing/output costs; (3) separately construct a provenance-faithful licensed native X6 three-force Cell/Link/Port event and its time/resource-preserving observer map.
