# D25: exact prime-horizon signed Cauchy pair support modulo p^3 (2026-10-28)

Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Shared D25 author context; not an independent reviewer, native Source checkpoint, or H0/B0 benchmark.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT;
publication TP2-B6F4FC938FF94941C1B7;
unchanged scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Scope and new theorem

Let p>=5 be prime, u_j=binom(2j,j)/8^j, c_k=(3k)!(2k)!/[216^k(k!)^5] in Z_(p), and
S_p=sum_{j+k<p}(3(j+k)-1)u_j c_k.
Ordered (j,k), signed weights and triangular cutoff are part of the observation. The allowed projection is coefficientwise zero suppression for this exact signed sum modulo p^3; it does not extend to arbitrary future operations or native X6 dynamics.

Set K=ceil(2p/3). Define E_p as follows:
* p=6r+1: E_p={(4r+1-k,k): 3r+1<=k<=4r}, exactly r source pairs.
* p=6r-1: E_p is empty.

Then the EXACT set of nonzero signed summands modulo p^3 is

T_p={(j,k):0<=k<K, 0<=j<p-k} \ E_p.

Thus S_p equals the sum over T_p modulo p^3. Its count is:
* p=6r+1: |T_p|=(4r+1)^2-r=16r^2+7r+1.
* p=6r-1: |T_p|=16r^2-2r.

For target primes p=13,19 (mod 24), p=6r+1. The earlier joint u/c VALUATION mask gives no further compression than k<K at horizon N=p; the ORIGINAL SIGNED WEIGHT adds exactly r=(p-1)/6 safe deletions. In particular p=19 retains 166 out of 190, and p=373 retains 61939 out of 69751 ordered sources.

## Exact all-prime proof

By Legendre's factorial valuation formula, for j,k<p:
v_p(u_j)=floor(2j/p),
v_p(c_k)=floor(3k/p)+floor(2k/p).

If k>=K, the second valuation is >=3. For k<K, if k>=ceil(p/2), v_p(c_k)=2 while j<p-k forces v_p(u_j)=0; if ceil(p/3)<=k<ceil(p/2), their valuations sum to <=2; for smaller k, v_p(c_k)=0. Thus every k<K pair has coefficient-product valuation <=2. This proves the joint coefficient-only mask degeneracy at N=p.

Write m=j+k in [0,p-1]. The integer signed weight 3m-1 has absolute value <p^2 and is divisible by p for EXACTLY ONE m: m=4r+1 when p=6r+1 (weight=2p), or m=2r when p=6r-1 (weight=p). Its valuation is precisely one at those m. In the p=6r+1 case, the diagonal m=4r+1 reaches coefficient-product valuation two exactly for k=3r+1,...,4r, at which j=4r+1-k lies in [1,r] and u_j is a unit. These are precisely E_p. Every other point on that diagonal has product valuation at most one. In the p=6r-1 case, m=2r forces j,k<=2r, giving v_p(u_j)=0 and v_p(c_k)<=1, so there are no additional zero terms. Consequently the signed summand has valuation >=3 exactly outside T_p, and <=2 exactly inside T_p. Counting the original k<K triangle gives Kp-K(K-1)/2, then subtract |E_p|. QED.

This is exact *termwise* support, not a statement that final signed totals cannot have additional cancellation. It reuses the existing u_j/c_k carry valuation laws and adds the signed-weight diagonal classification, with BRC provenance tags retained. The optional mask is only certified for this p-integral signed observer modulo p^3; no claim of p^4 safety, H0/B0 transfer, Source research admission, or independence.

## Executed evidence and next action

The full local author checker on 2026-10-28 used an independent Legendre factorial-valuation oracle on 595285 ordered source pairs across primes
5,7,11,13,17,19,23,31,37,43,73,211,373,997.
It also reconstructed signed S_p in Z/p^3Z using the inherited exact coefficient recurrences; every full/sparse sum and count agreed. The companion repository reproducer checks the same theorem. A short run summary is in the sibling JSON. The full local author run certificate SHA-256 is 3a91c6d4c137a137868876c9b01ec3f6f4b12f46b8bb79a3dbfccf7ac1b606e7 (only an artifact content fingerprint, not independent proof).

For native successor: first establish the actual original H0/B0 same-class p-integral coefficient and signed observer port map. Only if that map preserves u/c and 3(j+k)-1 may the above support rule be transported. Original p=373 H0/B0 with Frobenius and Delta_p-R_p remains pending in Issue #1559. UR V2 original four-file bundle remains to be found and checked at exactly 94687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; reuse completed UR mathematics rather than reproving it.

Native continuation/CLAIM/OPEN not verified in this conversation. For current-input-only seeds predecessor completed_units must remain []; this author evidence belongs to staging/do_not_repeat until a lawful Source publication.