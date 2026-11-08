# D25/LIFT — exact identification of the frozen 216 second-digit target with the supersingular specialization of published equation (6.8)

Date: 2026-11-09 (Asia/Hong_Kong). TASK_RESEARCH author-side; logical research conversation `chatgpt-research-onhour-enterprise-math-20260923` (distinct from maintenance). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. **SOURCE-ALIGNED EXACT IDENTITY / EXECUTED TWO-PATH FINITE TEST / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

## 1. A new, source-verified research correspondence

Babei, Roy, Swisher, Tobin, Tu, *Supercongruences arising from Ramanujan-Sato Series*, arXiv:2408.08844v3 (2025-03-12), Section 1.1 (definition (1.1)), Theorem 2.1, Section 6, equation (6.8), and Proposition 6.3:
- manuscript: https://arxiv.org/pdf/2408.08844v3
- preprint metadata: https://arxiv.org/abs/2408.08844

Their exact definition for `b=(1/2,1/3,2/3)` is
```
[F_{6,b}]_{p-1}(1/2) =
sum_{n=0}^{p-1} (6n+1) (1/2)_n (1/3)_n (2/3)_n
                                * (1/2)^n / (n!)^3.
```
For each integer n>=0, the elementary Pochhammer identities give
```
(1/2)_n = (2n)!/(4^n n!)
(1/3)_n(2/3)_n = (3n)!/(27^n n!)
(1/2)_n(1/3)_n(2/3)_n/(2^n(n!)^3)
  = (2n)!(3n)!/(216^n(n!)^5)
  = binom(2n,n)^2 binom(3n,n)/216^n.
```
Hence the published full truncation is **termwise, exactly** the frozen original `W_p`, without rescaling, a changed cutoff or a p-adic quotient:
```
[F_{6,(1/2,1/3,2/3)}]_{p-1}(1/2) = W_p.
```
Previously source-aligned, exact original Clausen bridge (consume without reproof): `Delta_p-R_p = (W_p-p)/p^2 mod p`; see `research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md` and source-fixed signed cutoff `Q/p^2=R_p mod p`.

## 2. Critical supersingular sign conversion: no undocumented sign choice

The manuscript's Theorem 2.1 defines `sgn=+1` in the ordinary case and `sgn=-1` in the supersingular case. Its equation (6.8), explicitly reported as numerically checked for applicable primes `5<=p<150`, is
```
[F_{6,b}]_{p-1}(1/2) = sgn * ((1-1/2)/p) * p (mod p^3).
```
For *both* frozen target residue classes `p=13 or 19 (mod 24)`, one has `p=5 or 3 (mod 8)`, hence `((1/2)/p)=(2/p)=-1`. The source-aligned CM discriminant `-24` elliptic `E3((2-sqrt2)/4)` is supersingular for these inert primes (the project already consumed this known CM0/UR property), so `sgn=-1`. Therefore the displayed conjectural right-hand side **specializes to `+p`**, not `-p`:
```
published (6.8) on p=13,19 mod 24
  <=> W_p = p (mod p^3)
  <=> frozen original D25 LIFT: Delta_p-R_p=0 (mod p).
```
The first equivalence uses exact termwise equality and the verified signs; the second consumes the already proved signed-cutoff source bridge. This is a **proved identity/equivalence of problem formulations**, not a proof that either target congruence is true for all primes. This aligns the external literature's precise open supersingular case with our current mother target.

## 3. Exact two-implementation finite check of the literature-port equality

On 2026-11-09, ran Python 3 standard-library independent integer modular methods:
1. original `binom(2n,n)^2 binom(3n,n)/216^n`, direct exact binomial coefficients and modular inverse;
2. published rising-factorial term with recurrence
   `c_0=1`, `c_{n+1}/c_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3)`,
   only for `n+1 < p` so all inverted denominators are p-units.
Both compute identical `W_p mod p^3`, with no floating point. Values (p, modulus p^3, both readouts):
```
(13, 2197, 13), (19, 6859, 19),
(37, 50653, 37), (43, 79507, 43),
(157, 3869893, 157), (163, 4330747, 163),
(373, 51895117, 373).
```
p=157,163 are *beyond the cited paper's stated p<150 test range*, while the broader Enterprise Math project already had other finite scans; these are **cross-implementation provenance checks**, not novel global observations. All seven exact checks PASS, and the rigorous termwise identity has no finite restriction.

Reproducer: `research_notes/portable_direct/d25_source68_crosswalk_exact_check_20261109.py`; output `research_notes/portable_direct/d25_source68_crosswalk_exact_results_20261109.json`.

## 4. Source strength / research consequence

The manuscript's Theorem 2.1 proves the general weighted supercongruence **mod p^2**. Theorem 6.1 proves certain **ordinary-prime** cases for `b=(1/2,1/6,5/6)`, **not** our d=3 supersingular mod-p^3 objective. Its equation (6.8) is a *numerically examined instance of Zudilin's proposed mod-p^3 strengthening*, and Proposition 6.3 is conditional on that strengthening. Treat it as an exact **published conjectural target with checked signs**, not a 2025 published proof of D25.

This finding tightens a useful next proof direction: the precise missing step is the supersingular d=3, lambda=1/2 `p^2 -> p^3` lift in Theorem 2.1, preserving `sgn=-1` and the frozen signed Clausen `Q/R` interface. Any proof of that particular published strengthening for the frozen classes would close original LIFT. Re-proving the already accepted p^2 theorem, using ordinary-prime Theorem 6.1, or deriving an untyped Hesse scalar would not fill the second digit.

BRC/coordinate usage: **COMPOSE_APPLIED**; retain `(p mod24, hypergeometric lambda and alpha, original term coefficient, cutoff n<p, CM supersingular sgn, Legendre symbol, frozen Delta and signed R)` as distinct source-labelled ports. The equality of published/frozen coefficients is a lossless termwise transform; neither taking absolute values nor erasing the signs or p^2 boundary is valid. Classical auxiliary complex/elliptic coordinates are not native X6 geometry.

## 5. Durable continuation and exact authority boundary

Mother objective remains `Delta_p-R_p=0 mod p` for all `p=13,19 mod24`. Accepted D24 UR/JT0, Source authors/owners and existing author-side exact tools are consumed without re-credit. The actual same-original-class p=373 H0/B0 divided-power benchmark `[X]U mod139129`, its native module rank, semilinear Frobenius, two-digit eta, signed odd Green/Hesse kappa, original Delta-R and independent reproducer remain **NOT_RUN / PENDING_OWNER** under issue #1559; no native experimental progress or Source admission is inferred from this literature check.

Native historical Researcher registration: `EM-ENTERPRISE-4DEB43`, session `MCP-ecbfd1c046864bb3bff1a2e04c87d207`, activity `RA-9553E027FD14223807511263` (own onhour lane). Previous exact continuation request `onhour11-20261108-2202-current-task-continuation`: `SUCCEEDED` read receipt; original successful registration request `onhour11-20261108-2202-own-researcher-session-start`: `SUCCEEDED`. Fresh own recovery in this run: `SESSION_CAPABILITY_REQUIRED`; no private capability, winning claim/run, legitimate Source-native checkpoint or Result. No maintenance lane session or claim reused.

**Next precise action:** an authorized native Source executor, when assigned to #1559, executes the unmodified original p373 H0/B0 fixed divided-power object and records raw `[X]U`, rank, actual operator/normalization, signed kappa and Delta-R under the frozen pin, followed by independent replication; meanwhile a permitted portable research route may test the exact supersingular d=3, lambda=1/2 **third-digit** strengthening directly, rather than adding unrelated auxiliaries. Source rule/HEAD changes do not move scientific input pins. No automatic task dispatch, result freeze, reviewer acceptance, scheduler mutation or claimed original benchmark completion.
