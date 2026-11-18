# EC49BN — subgroup/covariant native X6 weighted BRC exact residual
2026-10-30 | AUTHOR_ANALYTIC_PROOF / EXACT_FINITE_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Full author materials (lossless)
- `PROOF_EC49BN.md.gz.b64`: complete 11,946-byte proof, decoded SHA-256 `7e0710bf6dddb11f2b98647aadd8b7730003c6dcd41fb27e8e007e3cca2c2a91`.
- `VERIFY_EC49BN.py.gz.b64`: the exact 5,684-byte executed Python verifier, decoded SHA-256 `869d63cc4306b7e8436ea9b24df515409272f123fdd8e1643f5253243ebc565a`.
- `EXACT_REPORT_EC49BN.json`: exact finite census; native `signed_brc.py` Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.
- Encode convention: base64(gzip(raw UTF-8 bytes, mtime=0)), followed by one newline. To decode: `base64 -d PROOF_EC49BN.md.gz.b64 | gzip -d > PROOF_EC49BN.md` (same for checker).

## New mathematical results
For a fixed (source,n,d,prefix_r,suffix_r) path fiber, six loop counters k_i sum to K=(n-||d||_1)/2, with q_i=w_i^+w_i^- positive rationals. With future concatenation, inverse and **fixed-instrument** allowed axis subgroup H<=S6, exact future weighted indistinguishability is
`C_{H,q}={z in Z^6: sum z_i=0; prod_i q_{sigma(i)}^z_i=1 for all sigma in H}`.
Finite prime-valuation rows give an exact integer kernel.

For proper subgroup H=S({1,2,3}) x S({4,5,6}), q=(4,4,4,9,9,9), the minimal added history is **one integer** K_A=k1+k2+k3; internal per-axis loops can safely merge for this declared observer. At n=4,d=0,r=1 there are 396 words and respectively 144 boundary-only, **156 block-residual**, 204 full-histogram classes. u=(+1,+2,-2,-1),v=(+1,+3,-3,-1) are weighted-equivalent but histogram-distinct; w=(+1,+4,-4,-1) is distinguished.

If instead the **instrument table follows axis labels** under simultaneous path+table relabeling, each weight readout is invariant. The minimal weighted kernel reduces to `{z in W:prod_i q_i^z_i=1}` with NO extra permuted constraints. For q_i=2^i and w_i^+=1,w_i^-=2^i, only L=sum i*k_i is needed, even though all q_i differ. At n=6,d=0,r=1 there are 19,920 closed paths, **924 covariant weighted classes** versus 1,044 full-histogram classes; native aggregate endpoint_weight is 140,179,680. Distinct closed words X=(+1,+2,-2,+4,-4,-1),Y=(+1,+3,-3,+3,-3,-1) both have exact product 128.

## Verification/provenance/limits
The original checker was executed twice locally with byte-identical JSON and imported the byte-pinned native signed_brc.py. Exact arithmetic only. Native `endpoint_weight` is the **sum** across all compatible words, not a per-path observer; these theorems do not prove aggregate selected-multiset sufficiency, signed/phase BRC or heartbeat dynamics. The controlling global snapshot was `b312bb23eabe0b05635bc97dba047b6fbf5ba3a6`, project main `af3176e185d991d3d93fbec05736f0968aed1948`, predecessor EC49BM research commit `123e5884c0bd32b19e6d25d8f33ddecced746822`. P000 and ACTIVE worldview untouched. Gateway authority denied (`research_authority_granted=false`); owner query `CONTROL_QUOTA`; no formal CLAIM, Result or independent review.

## Next EC49BO
Classify mixed-orbit proper H and nontrivial q through Smith-normal-form certificates; separately construct an exact selected-multiset BRC counterexample distinguishing per-witness and aggregate observer sufficiency. No new native task has been registered.
