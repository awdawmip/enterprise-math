# R272 — Sharp edge-specific 13-adic BRC Port precision

2026-11-18. AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED. Independent portable research after R271@9189a92071f71d602b931686f6fac2be79a40bff; frozen scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Uses the actual WBRC-T30/T31 typed visible Port context, not a hypothetical native X6 or R269 source-to-Port map.

## Exact labeled-edge resolvent theorem

For any prime p, a stable finite positive-rational d-Port model has A=I-W_eff-C and visible star S=A^(-1). Adding one nonnegative rational permitted visible edge from labeled Port u to v with weight delta yields A'=A-delta E_uv. Assume the new Port context is also stable. Then exactly

 S'_(ij)-S_(ij) = delta*S_(iu)*S_(vj)/(1-delta*S_(vu)).

Proof: multiply (A-delta e_u e_v^T) by the rank-one inverse candidate S + [delta/(1-delta S_(vu))] S e_u e_v^T S, obtaining I. Stability ensures the rational denominator is nonzero.

Let v_p(0)=+infinity. For an output normalized by p^e, any declared input precision N satisfying

 N+v_p(S_(vu)) >= 1,
 N+e+v_p(S_(iu))+v_p(S_(vj)) >= m

guarantees that every permitted delta with v_p(delta)>=N preserves p^e S_(ij) modulo p^m. The first inequality makes the response denominator a p-unit, and the second bounds the exact update valuation. If both numerator entries are nonzero and v_p(delta)=N, the lower valuation bound is attained exactly. If a numerator entry is zero, this observed output is precisely unchanged. These are **edge-specific** certificates over the declared observer and allowed future edge, and need not retain the global full-matrix s+m digits from R271.

## Strictly coupled positive-rational sharp witness

For every s>=1, set P=13^s, q=P/(100P+1), epsilon=P/(1000P+1) and h=1/2. Use two visible labeled ports with

 A=[[q,-epsilon],[-epsilon,h]],
 W=I-A=[[1-q,epsilon],[epsilon,1-h]].

The coupling epsilon>0 is genuine. Since 0<epsilon<q<1/100, epsilon<h, every entry of W is nonnegative and every row sum is <1, proving strict BRC Port stability. The determinant qh-epsilon^2 has exact 13-adic valuation s, since qh has valuation s and epsilon^2 has valuation 2s. The rational star is S=(1/det A)[[h,epsilon],[epsilon,q]] and

 v_13(S_11)=-s, v_13(S_12)=0, v_13(S_22)=0, S_22=2 (mod 13).

Thus the full matrix inverse has pole depth s while the labeled second-Port output is already 13-integral. For any m>=1, add ONLY a permitted port-2 self-loop of weight delta=13^(m-1)/(100*13^(m-1)+1). It is positive and <1/100, so the updated positive-rational Port matrix remains stable. The original and modified inputs agree modulo 13^(m-1), and v_13(delta)=m-1. The denominator 1-delta S_22 is a 13-unit: for m>=2, delta is a multiple of 13; for m=1, delta=1/101=4 mod 13, S_22=2 mod 13, hence 1-delta S_22=6 mod13.

The exact resolvent gives

 v_13(S'_22-S_22) = m-1.

Therefore **m digits** of this one labeled self-loop are sufficient to preserve the unscaled Port-2 star modulo 13^m, and m-1 digits are insufficient, for every s>=1. This saves s input digits relative to indiscriminately applying the global full-star s+m bound to the restricted Port-2 observer and one-edge operation. No source/provenance or other Port observer has been erased or claimed to descend.

## Validation and lineage

A standalone stdlib Fraction checker evaluates all 48 exact pairs 1<=s<=8, 1<=m<=6: true Port stability, the determinant and individual star valuations, the exact resolvent identities, denominator unit and difference valuation. PASS 48. Full generated JSON SHA-256: 0e3d4911109252ff49dd5378efa12d1f051c362f7e140494b65f9252a942aa60. Universal s,m correctness comes from the formulas, not finite extrapolation. Classical rank-one inverse updating is prior art; the contribution is the typed Port precision specialization and stable exact sharp example. Independent review and Foundation adoption remain pending.

Next: derive and test the multi-edge Woodbury response for a fixed permitted labeled-edge set, including resonance of its small coupling matrix; characterize the minimal precision for a selected entry. Separately test the existence of a provenance-preserving source-generated R269-to-Port map by exact future-operation fiber constancy.

Files: R272_SPARSE_EDGE_PORT_PRECISION_20261118.md, R272_sparse_port_precision_checker.py, R272_verification_digest.json.