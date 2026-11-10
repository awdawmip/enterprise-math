# R41 — Certified hybrid source-owner selection and full S23 risk reconstruction

Date: 2026-11-10. Status: author-side mathematical derivation with exact regression, independent project review pending.

Scientific freeze: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. 
Prior source: R32 (PR #1929), R33 (#1935), R35 (#1946), R36 (#1951), R37 (#1955), R38 (#1965), R39 (#1969), R40 (#1974). 
Object: auxiliary irrational circle rotation, preserving historical interval labels; typed BRC provenance/observer rule reused, without claiming native X6/triadic dynamics.

## R41.1 — Source-preserving suffix/coboundary hybrid theorem

Fix irrational `0<theta<1`, integer `m>=2`, `m` distinct historical cutpoints `{z theta}`, `0<=z<m`, with their cyclic half-open owner arcs `I_0,...,I_(m-1)`. Let `J` be any integer and `N>=1`; for arc `k` set

`tau_k=max({t: J-N<=t<J, {t theta} in I_k})`, using `None` if empty.

Scan backwards `t=J-1,J-2,...` for at most `B` sources, preserving the exact owner label. For every owner seen in the scan, its *first* hit is already its exact `tau_k`, because every omitted source is older. If all `m` owners have been seen, or the entire window is exhausted, this vector is complete. Otherwise, for precisely the missing owners, invoke R40's exact, monotone suffix-count selector `C_k(L,J)` and obtain each missing `tau_k` by exponential bracketing and bisection. Joining the two disjoint owner sets gives the exact labelled vector `(tau_0,...,tau_(m-1))`.

**Proof:** For any seen owner `k`, let `t` be its first hit in the reverse scan. Each later source `u` with `t<u<J` was scanned and did not have label `k`, so `t` is its largest source in the *whole* window. For missing owners no scanned source has that label. R40 gives the exact count `C_k(L,J)`, monotone in `L`; the greatest source is characterized by `C_k(t,J)>0` and `C_k(t+1,J)=0`, or absence by `C_k(J-N,J)=0`. The two procedures compute different coordinates of the same labelled vector. QED.

All phase and floor tests use the declared rational enclosure `theta_lo <= theta <= theta_hi`. The certified source-owner test must prove the relevant historical endpoint comparisons are fixed across the enclosure. If an enclosure cannot certify a comparison, refine it before claiming a result. Neither the scan budget nor the selection heuristic changes the mathematical output.

## R41.2 — Optional near-rational q-channel partition

In the R38 setting `theta=p/q+eta` with `eta>0`, `gcd(p,q)=1`, `sigma=q eta>0`, and a historical arc whose width is at least `sigma` over the enclosure, R38's exact q-lane predecessor formula can supply that missing owner's `tau_k`. The remaining narrow arcs use R40. Since owner labels partition the arcs, suffix-found, q-lane, and R40 coordinates combine exactly by R41.1. This is an implementation option, not an assumption about R40 itself.

## R41.3 — Risk-compiler substitution corollary

Within a fixed Farey stage of the auxiliary S23/AV observer, R35–R36 use the owner-indexed last surviving source `tau_k` to calculate `F(n)=m-h+rank_T(n-i)` for `T=sorted({tau_k:tau_k is not None})`. Therefore replacing the previous last-source selector by any certified R41 exact selector preserves `F`, every stage risk increment `[F(b)-F(a)] min(u,v)`, and all resulting affine risk intervals. This follows by substitution into the previously established formulas, not by a new universal theorem about arbitrary observers.

## Exact S23/AV results

For `m=128`, `J=1000000000128`, `N=10^9` and `theta in [262204504569236716045286,262204504569236716045287]/10^24`, all 128 arcs appear within the most recent 164 sources. Last-source ages form exactly `{1,...,106} union {143,...,164}`. The suffix option uses 164 certified source-label probes and zero R40 batch floor evaluations; independent Euclidean-Floor-Sum reference returns all 128 identical owners.

The full R41 integration run actually executes both the hybrid (suffix first) and forced R40-endpoint choices in the initial three Farey stages of the existing R33/R36/R32 risk compiler. Each yields four initial risk blocks, 78 full Farey stages, 28 exact quotient-jump decisions, 148 tail positive blocks, 298 maximal affine risk intervals, and the exact final risk

`R_(10^12+128) = -4017401528447 + 15321634290944 theta`.

The six-column affine interval TSV is byte-identical to R32's independent reference; SHA256 is `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`.

## Operation counts and adaptive experiment

On the pinned local Python environment, R40-only versus a 4m-source suffix-first route (each independently compared against the R40 Euclidean-Floor-Sum oracle) gives:

| Input | R40-only endpoint floor evaluations | R41 scanned sources | R41 fallback owners | R41 endpoint floor evaluations |
| --- | ---: | ---: | ---: | ---: |
| S23, m=128 | 35,562 | 164 | 0 | 0 |
| Mixed near-third, m=257 | 138,242 | 869 | 0 | 0 |
| Very-near-third, m=21 | 2,442 | 84 | 18 | 2,402 |

The last case demonstrates that suffix scanning need not improve cost. R41's optional decision `m*(q theta_hi-p) < 1/8` skips the suffix probe and uses R40 directly for these very-near-rational enclosures. The threshold is an empirically chosen performance rule; all branches preserve exactness independently. A q-channel path was also tested and returned the same labels, but Python rational arithmetic often favored R40 for the small-q case.

The cost model must account for `O(m log m)` initial phase sorting, up to `B` certified `O(log m)` label searches with integer/rational bit-cost, any `q*|W|` channel candidates, up to `O(mQ)` exact scalar floors for `Q` distinct R40 thresholds, large-integer bit widths, input enclosure precision, any input conversion and serialization of the `m` source labels and final `K` intervals. The comparison table counts particular operations, not a universal complexity improvement.

## Verification boundaries and provenance

The project version of `VERIFY_R41_STANDALONE.py` includes the verified R40 arithmetic and independently exercises R41 on S23, near-third m=21 and mixed m=257. The companion `VERIFY_R41_INTEGRATION.py` runs with the exact predecessor code in the R41 local bundle and re-generates all 298 risk segments twice. The extended local `VERIFY_R41.py` adds the optional q-lane path, mixed cases, exact ownership and deterministic source certificates. See `EVIDENCE.md` and `NEXT_TASK.md`.

This is a direct author-side algorithmic integration in the specified auxiliary observer. Independent project mathematical review and task/owner admission are pending. Frozen science, P000 and the active worldview retain their original scope.
