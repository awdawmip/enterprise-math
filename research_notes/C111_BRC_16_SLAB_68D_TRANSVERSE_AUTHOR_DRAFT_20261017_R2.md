# C111 | 68D finite BRC transverse-zero radius via exact 16-slab Bernstein refinement

**Status:** independent author-draft provenance; classical finite positive-weight BRC auxiliary, not native P000-X6 mathematics. No native Task CLAIM or Driver review/admission.

## Frozen provenance
- Global knowledge GLOBAL_KNOWLEDGE_V1 `main@e4b94e481b7d2032ead71e7210985103209da6c5`, bootstrap and operating manual, P000 projection validated against original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, ACTIVE worldview.
- Enterprise Math source read `main@748654b6f143b53e5af9fe2a8fbe3de3f0a68c8d`; current Portable Research Protocol.
- Input C110 portable SHA256 `b5141665b36c3beb9ab1d4f2fa8134ed2b326841f1f94c88a0a464aa5488258d`; nested C109–C105 exact four-moment coefficient and independent graph/Walsh validation.

## New theorem, exact scope
For the eleven connected C105 stages with core `c2=c24=1`, write `F=AD-BC=4(ad-bc)`, `Q=4(ad+bc)=(A²+D²-B²-C²)/2`. 68 weak couplings independently vary as `r_f=eps+(1-eps)r0_f+z_f`, where `delta=7/10000000`, `eps=71/100000000`, and `|z_f|<=delta`. Every coupling stays strictly between zero and one.

Partition the `t` interval into sixteen rational subintervals in *each* of eleven stages; use exact Bernstein lower `L_{s,j}` for `-∂_uF0` and upper `U_{s,j}` for `Q0` on the *same* rectangle `I_j×[2/5,99/100]`. Retain C109/C110's pointwise correlated-state ratio bounds `rho, beta`: `|Fz-F0|<=U*(2rho+rho²)`, `-∂_u Fz>=L-2U[300rho(2+rho)+beta(1+rho)²]`.

All **176 rectangles** and **22,096 exact rational Bernstein evaluations** pass, with strict global results
- `min(L - U*derivative_factor)>120` (approximate display 123.6707276);
- `max(U*F_error_factor)<13/4` (approx. 3.2249409);
- `max(U*F_error_factor/L)<1/750` (approx. 0.0012592003).

Using original `F0(t,2/5)>100` and `F0(t,99/100)<-29`, conclude `Fz(t,2/5)>96`, `Fz(t,99/100)<-25`, `∂_uFz<-120`. There is exactly one simple interior root `u_*(t,z)`; `|u_*-u0|<1/750`. Exact moment junctions imply the five-family connected zero-star persists for common `z`. The radius is **2.8 times C110**; the displacement bound improves from C110's 1/600.

## Reproducibility and limitations
This run created `EM_C111_BRC_16_SLAB_68D_TRANSVERSE_PORTABLE.zip`, SHA256 `7a1fdc177d440ecd2bc6ead68783e761098858966f9d379156e9fd284a889c4d`. It contains full theorem, C111 proof code and rational certificate, immutable C110 parent zip, manifest, and a verifier. Clean extraction recomputed the C110 parent and C111 176-rectangle certificates byte-for-byte and verified their hashes. Local portable file is not automatically present in Source GitHub; evidence program upload is still pending.

The status is **AUTHOR_EXACT_RATIONAL_VERIFIED**, not official mathematical acceptance. Neither global connectivity of the full 68D zero locus nor preservation into native X6/3D slices is proved. Control-owner query returned `CONTROL_QUOTA`, so there is no verified active owner or CLAIM.

**Next discriminating problem:** adaptive rational 2D Bernstein subdivision of the critical pair (8,9) stage I, tracking the closest possible derivative-zero obstruction and testing whether the uniform unique-root tube can exceed `delta=10^-6` without new hypotheses.
