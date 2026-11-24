# Shared-context audit of the complete R2 seven-budget observer

Audit date: 2026-11-24, Asia/Hong_Kong. Scope: the v11 observer proof, exact frequency and claimed minimum within R2. This is mathematical assistance to the existing author work; it is not an independent project Review.

## Conclusions checked

The proof of `T | N` as the necessary and sufficient condition for root-residue observation is valid, conditional on the accompanying complete seven-cover classification. In the necessity direction, every prime q dividing T is coprime to the R2 progression modulus S2. Holding the other eleven prime coordinates and the arbitrary finite modulus N fixed while changing q is therefore legitimate exactly when q is absent from N. Arbitrary powers of the other observed primes do not interfere with that CRT argument.

The full-residue-trajectory version is also valid. Equal root residues give equal trajectories for necessity. For sufficiency, the first residual value recovers the square modulo the odd divisor T. Each phase category is a pair of opposite roots, so it depends only on that square. Inversion is performed modulo T even when N itself is even.

The twelve-prime claim uses the stated counting convention: one channel observes one prime or prime power. The proof does not treat a single composite-modulus readout as twelve separately counted calls. The least progression-parameter period is T; root translations preserving the entire R2 domain instead have least such period S2T. The proof explicitly distinguishes these quantities.

The exact event counts are proper weighted residue counts. The descriptions of 146 dictionaries and 1160 signed CRT progressions may overlap; the frequency formula instead uses inclusion-exclusion within each family and CRT independence between the three disjoint prime sets. This avoids double-counting successful roots.

The global minimum claim is over the entire R2 cost-seven class because the full prefix and tail classification makes the 1160 progression descriptions exhaustive. Taking the smallest positive start of their union does not require the progressions to be disjoint.

## Executed arithmetic

The existing `verify_observer.py` was executed with its frozen tail certificate and a separate output path. All exact arithmetic checks passed:

- `T = 35095524795781473254136196580356738045833417602831290421525609131`.
- Successful residue count `N = 916603393453788765429110921373053984059735989421687074488`.
- Relative R2 frequency `N/T = 2.61173867262975266825491471344819447750899674021443682405847E-8` to the displayed precision.
- Twelve essential additional prime coordinates, with maximum exact base-two order 180.
- The 84-digit minimum over all R2 cost-seven roots is reproduced from all 1160 starts.

The arithmetic output is `observer_audit_certificate.json`. Re-executing this calculator checks its exact inputs and finite enumeration; the arbitrary-modulus claims are justified by the arguments above and the original proof.

## New frontier resolved

The specific 43-coordinate fiber in v11 `finite/proof.md` had all costs s at least nine and excluded costs at most seven. Cost eight now has an explicit four-tail construction, a compact ordinary root and an infinite exact-total-cost-28 refinement. See `proof.md`, `verify_cost_eight.py`, and `cost_eight_certificate.json` in this directory.
