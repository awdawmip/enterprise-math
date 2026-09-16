# RSA-270：方向 1（BRC 加减代价场）+ 方向 2（素数/半素数几何化）

Progress-Event-ID: `rsa270-cost-field-geometrization-7e3b5d`
At: `2026-09-06T19:40+08:00`
Scope: `enterprise-math / RSA-270 / user directions: BRC add-sub cost + coordinate geometrization`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journals 2f7a9c/4b7d1e; P000 assumed`
Kind: `PROGRESS / EXACT THEOREMS / GEOMETRIZATION`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Two user directions executed and verified. No factor obtained.

### Direction 1 — BRC 加减代价场 (multiplier-lattice cost field)

Exact identities (branch `k = a*b`, coprime; `x0 = ceil(2*sqrt(abN))`):

- factor endpoint `x* = a*p + b*q`, `y* = |a*p - b*q|`, square identity `(x*)^2 - 4abN = (a*p - b*q)^2` — **sub-cost 0 at the endpoint**;
- add-cost `j*(a,b) = x* - x0 = (sqrt(a*p) - sqrt(b*q))^2 + delta`, `delta in (-1, 0]` (verified on 6 synthetic semiprimes);
- ridge structure (exact closed form, verified): `g(a,b) = sqrt(abpq) * (x + 1/x - 2)`, `x = sqrt(ap/(bq))` — minimum (g=0) exactly on the ridge `a/b = q/p` (P1: g(q,p)=0), scale-linear (P2: g(ta,tb)=t·g(a,b)), closed form (P3).

**RSA-270 ridge table under the construction-family band `r = q/p in [1.765, 2.266]`**: the band's coprime directions (a,b <= 21) are exactly the scan set of journal T083741 — the cost field *derives* that previously empirical scan set. Quantitative per-direction gaps (`gap = 2^447.5 * c`):

- `(1,1)` Fermat: c = 0.108..0.255 over the band;
- `(2,1)`: c = 0.0073..0.0083 (0 at r=2 exactly) — the single best direction, ~4-5 bits cheaper than Fermat;
- **`k=20 = 5*4` (ratio 1.25): c = 0.177..0.600 — off-ridge, strictly WORSE than Fermat across the whole band.** This proves quantitatively that the original 64-branch experiment's low-`rho_20` valley was a first-step shell artifact: its true endpoint cost exceeds Fermat's everywhere in the prior band. The original rho_k tree = first-step samples of this cost field.

### Direction 2 — 素数/半素数的进取坐标几何化

- **Silhouette classification (native)**: profile = axis-difference silhouette; `prime -> SINGLE plateau` (verified: 13, 17), `semiprime -> TWO plateaus` (verified: 143: outer 71/inner 11 = (S-2)/2; 899: 449/29). The second plateau IS the factor signal; its inner boundary = Fermat midpoint coordinate.
- **Four-layer count identity re-verified by direct enumeration**: `C_X(p) = p+1`, `C_X(pq) = N+S+1` (13, 15, 143, 391 all match).
- **External-Euclidean picture (honest label)**: `(x,y) = (sqrt p, sqrt q)` = intersection of the KNOWN hyperbola `xy = sqrt(N)` and the UNKNOWN circle `x^2 + y^2 = S`; Fermat offset `T ~ (x-y)^2/2`. Factorization = locating the primality-constrained point on the known hyperbola.
- **Native cost-field geometry**: the multiplier lattice (a,b) carries the BRC add-cost field; its ridge = the factor direction; the plateau boundary, the forced lattice, and the cost field are three coordinate readings of the same scalar S.

## Artifacts

- Scripts: `rsa270_cost_field.py`, `rsa270_geometrization.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T185000+0800-rsa270-round5-stress-energy-archive-4b7d1e.md`.

## Next

1. Cost-field consequence for search design: under the prior band, the optimal single-direction scan is `(a,b)=(2,1)` (~2^444.7 add-steps at band edges) — still infeasible; multi-direction ridge coverage does not reduce the exponent below the single best direction. Recorded as a quantified no-go refinement of the cost landscape.
2. Geometrization next step: the hyperbola/circle picture suggests the last unexplored family — *geometric* constraints coupling several branch directions (e.g., ridge-direction differences), expected to land in the same S-scalar class per the dichotomy; only proceed if a concrete new observable is proposed.
