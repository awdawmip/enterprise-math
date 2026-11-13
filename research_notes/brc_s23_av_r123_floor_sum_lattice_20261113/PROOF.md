# R123 — Wide-band exact S23 joint signature oracle by rational 2D floor sums

**Scope:** author-side S23 auxiliary arithmetic-progression model. Date: 2026-11-13. Frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Follows R122 source `33e1b5d0fa726de672ae717519fb079d2b113209`. Full extended proof: [PROOF.md.gz.b64](PROOF.md.gz.b64); executable Python: [check_r123.py.gz.b64](check_r123.py.gz.b64); deterministic full results: [verification_r123.json.gz.b64](verification_r123.json.gz.b64).

## R123.1: Exact counting in a bounded rational 2D integer polygon

Consider finitely many rational affine inequalities `A*n+B*k <= D` or `A*n+B*k < D`, with `n,k` integers, explicit finite bounds on `k` and finite lower/upper bounds on `n`. An exact count and one lattice witness can be computed in polynomial bit complexity with no factor proportional to the number of integer k-bands.

**Proof.** Each inequality with `A=0` restricts k by an exact floor/ceil bound; each inequality with `A<0` gives an affine lower bound `n >= L(k)` (possibly strict), while `A>0` gives an affine upper bound `n <= U(k)` (possibly strict). Take the maximum lower envelope and minimum upper envelope. Partition the integer k-range by the floors and ceilings of *all* pairwise rational intersections of the bound lines. There are at most `O(s^2)` marked integers and integer runs for `s` constraints. On each unmarked run the active bounding lines and their order are constant; singleton marks retain all ties and strict endpoints.

For `L(k)<=U(k)`, the number of integer n at a fixed k equals
`floor(U(k)) - ceil(L(k)) + 1` with the exact modifications `n < U => ceil(U)-1` and `n > L => floor(L)+1`. Equality with any strict bound is empty; coincident weak bounds contribute only when their common value is integral. The run sum is a linear combination of rational affine floor sums `sum_{i=0}^{r-1} floor((a*i+b)/m)`, `m>0`, evaluated exactly by the signed Euclidean floor-sum recurrence in logarithmically many integer divisions. Its bit complexity is polynomial in input coefficient lengths. Thus all integer k in an arbitrarily long run are counted without visiting them. On a positive run, monotonicity of the prefix count supports binary search to locate an admissible k; take its minimal admissible n and check the original inequalities. This proves counting and constructive feasibility.

## R123.2: S23 arbitrary signed time separation

R122 provides, for each fixed mechanical lift word and one chosen directed-arc segment for each requested bit, a rational system in real theta and integer n,k:
`A_i*theta + B_i*n + C_i*k <= D_i` or `< D_i`, with `theta in (l,h)`, `k=floor(d*theta)` and `n=floor(x+(N-j)*theta)`.

Eliminate theta exactly. Each inequality with `A_i<0` gives a lower theta-bound; each with `A_i>0` an upper theta-bound; each with `A_i=0` is retained. The existence of a real theta is equivalent to every lower bound being no greater than every upper bound, with the comparison **strict when either contributing bound is strict**. Every resulting condition is rational affine in n,k. The original phase identities give finite integer bounds
`floor(min(dl,dh)) <= k <= ceil(max(dl,dh))-1` and
`floor(min(x+(N-j)l,x+(N-j)h)) <= n <= ceil(max(x+(N-j)l,x+(N-j)h))-1`.
Therefore the projected system satisfies R123.1. A lattice witness yields a rational theta by a midpoint between active bounds (or a common value when both are weak). Conversely every actual theta produces its legitimate lift and integer floor pair, so it appears in an enumerated system.

For a fixed number m of requested times, exact joint-qualification feasibility has polynomial binary-input bit complexity even for wide J and enormous signed N,d; no scan proportional to `|d|(h-l)` is necessary. For variable m, using the pre-existing finite Sturmian-word count `|P_m|=Theta(m^3)`, at most `O(2^m*m^3)` projected 2D systems suffice for a single bit pattern, each polynomially decidable. Full-signature enumeration may require another factor `2^m`.

## Validation and scope

The program implements the generic rational 2D solver and end-to-end S23 `m=2, a=j=0,c=1` where `M_t(theta)=[frac(x+t theta)<theta]`, `0<theta<1`. Its independent exact phase-cut enumerator checks the integer-crossing events `x+t theta in Z` and `x+(t-1)theta in Z`. It also tests strict facet coincidences, signed rational polygons and enormous time separations. The complete proof and program are gzip/base64 encoded as exact UTF-8 bytes; decode with `base64 -d FILE.gz.b64 | gzip -d > FILE`. Source SHA-256: full PROOF.md `28169797a9d9db0cdd6b9cb0fde4c80ae933e1da0aa4b9742e4db8d2931e3d47`; Python `deab84f06113f4b6fdcd05c619064051cb129f7a0e7440bbd2f4744ed646bdc3`; verification JSON `e021396c427369d98dbe36edce1d0e963bd1c1330a1606ed1387dc63de84dd08`.

The general directed-arc segment generator for arbitrary a,j,c and m>2 remains for R124, along with whole-cost benchmarks against R122's fiber-clipped oracle. This is a mathematical result for the declared auxiliary model; independent review and formal task admission are separate actions.
