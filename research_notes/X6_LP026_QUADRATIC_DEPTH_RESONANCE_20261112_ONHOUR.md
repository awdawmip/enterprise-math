# X6 LP026 — exact quadratic/depth resonance for signed native Cell fibers

**Date:** 2026-11-12. **Evidence:** AUTHOR_PROVED / EXACT_INTEGER_CHECK_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY. Mother `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; original historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, native scientific pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Existing HRI `REQUEST_REVISION` remains.

## Verified current consumer boundary

Historical `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md` at the frozen pre-rebase generation, Git blob `11f47f9d2d70439fdada6d59242790fdcf46929e`, lines 224–244, retains the diagonal-invariant quadratic `Delta(a,b,c)=a²+b²+c²-ab-bc-ca` as a derived quotient observer and explicitly excludes it as native length. The current retyped file, blob `175d2c0f00db8e94a263442dbdc77928c0dc9567`, lines 126–148, calls it `Q_car` and makes that same carrier/native metric distinction. Current `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`, blob `875e3b274e5be03c5872f782872065a0b96d14eb`, lines 14–42 and 94–112, retains signed raw Cell distance and reconstruction `d=r+h(1,1,1)`.

This is an exact LP026 quadratic consumer line: **PRESERVE_OBSERVER for `Q_car`; PRESERVE_NATIVE for raw signed squared norm**. The following theorem identifies a smaller sufficient repair for *one declared norm query* and its exact ambiguity set. It does not convert the carrier quadratic into a native metric.

## Theorem LP026-Q1 — norm reconstruction and depth-resonance classification

For any `n>=2` and signed vector `d in Z^n`, put

`h=min_i d_i`, `r=d-h*1`, `S=sum_i r_i`, `G(d)=sum_i d_i²`,

`D(r)=sum_{i<j}(r_i-r_j)² = n*sum_i r_i²-S²`.

`D(r)` is invariant under diagonal shifts and is determined entirely by the relative/min-zero observer `r`. The exact identity is

**`n*G(d) = D(r) + (S+n*h)²`.**

Consequently, given `(r,G)`, compute `t=nG-D(r)`. If `t` is not a nonnegative perfect square, there is no signed lift. Otherwise set `q=sqrt(t)` (integer), and inspect just `s in {q,-q}` satisfying `s≡S (mod n)`. Every admissible signed lift is exactly

**`d=r+((s-S)/n)*1`.**

In particular the mapping `h -> G(r+h*1)` on an entire fixed relative-observer fiber is **injective exactly when `2S` is not divisible by `n`**. If `2S≡0 (mod n)`, it has paired levels `h'=-2S/n-h` with identical `(r,G)`; the pair collapses to one only at the central level `S+n*h=0`. There are no further collisions.

**Proof.** Expand `G(r+h1)=sum r_i²+2hS+nh²`; by the displayed expression for `D`, multiplying by `n` yields `D+(S+nh)²`. Equal norms at levels `h,h'` give `(S+nh)²=(S+nh')²`, hence either `h=h'` or `h+h'=-2S/n`. The latter has an integer solution pair exactly when `n | 2S`. All candidate lifts satisfy `min(r)=0`, so reconstructing `d` from integer `h` is valid. This proves injectivity, the complete pair involution and the reconstruction algorithm. QED.

The declared research domains provide sharp arithmetic cases:

- Selected native **three-axis** X6 slice (`n=3`): ambiguous fibers precisely when `S≡0 (mod 3)`. For `r=(0,1,4)`, `S=5`, `G=17`, the only signed lift is `d=(0,1,4)`.
- Full signed **six-axis** native displacement (`n=6`): ambiguous fibers precisely when `S≡0 or 3 (mod 6)`; otherwise `(r,G)` recovers the original signed vector uniquely.

**Nontrivial X6/BRC counterexample at the ambiguous class `S≡3 mod 6`:**

`A=(0,0,0,0,0,3)` and `B=(-1,-1,-1,-1,-1,2)`.

Both have the same `rho(A)=rho(B)=(0,0,0,0,0,3)` and the same native squared norm `G(A)=G(B)=9`. Yet the unchanged source native signed BRC kernel yields `shortest_event_count(A)=3`, `B_min(A)=1`, versus `shortest_event_count(B)=7`, `B_min(B)=7!/2!=2520`. Therefore even `(rho, native squared norm)` does **not** universally recover signed-native path length or positive BRC multiplicity. A sufficient scalar norm-only repair is the signed sum `sum_i d_i` up to sign (its square), while full endpoint/path consumers need the actual signed lift or equivalent retained information.

The three-axis historical `Q_car` is `D/2`; thus for a selected triple, **`3*G(d)=2*Q_car(r)+(sum_i d_i)²`**. This is a precise carrier-native quadratic decomposition for LP026 without retyping the carrier as a native metric.

## Reproducibility and exact continuation

`research_checks/X6_LP026_QUADRATIC_DEPTH_RECOVERY_20261112_ONHOUR.py` was executed using exact Python integers. It enumerated all **1,331** signed triples in `[-5,5]^3` (979 unique / 352 double recovery cases), and all **15,625** signed six-tuples in `[-2,2]^6` (12,167 unique / 3,458 double cases), checking the exact inverse, resonance classification, norm identity and relative-shift invariant on every input. It additionally imported the *unmodified* native `signed_brc.py` after verifying Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176` and confirmed BRC masses `1` and `2520`. Local result: **PASS**. The all-integer theorem has the separate proof above; finite execution checks the recovery algorithm and actual native BRC implementation.

**Do not repeat:** previous LP011 chamber/median-bit theorems and typed X6 transfer, LP019 signed-thickness positive-BRC crosswalk, prior R063 signed shell counts, old historical72/local111/kernel and closed-disk proofs. LP026-Q1 is a narrower, new exact norm-recovery/fiber-resonance theorem; it is not a new global X6 transformation law or new Foundation rule.

**Next:** attach the explicitly verified `Q_car`/native metric source lines and this precise resonance witness to the frozen 28-row LP026 consumer matrix; continue actual old quadratic/parity/affine caller audit. Source `REQUEST_REVISION` and independent admission remain pending. Previous own Research lane `chatgpt-research-onhour-enterprise-math-20260923`, Session `MCP-de3e5bafb24f43f4a5e6285e7601676a`, original continuation request #6827 and typed-frontier support issue `awdawmip/enterprise-math#2141` are preserved. No winning X6 CLAIM/open is verified; research evidence persists independently of native checkpoint authorization.
