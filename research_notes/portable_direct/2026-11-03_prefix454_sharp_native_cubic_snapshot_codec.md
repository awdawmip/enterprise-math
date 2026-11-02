# PREFIX-454 — Sharp cubic rank and a 52-coordinate terminal-sector BRC port

**Date:** 2026-11-03 Asia/Shanghai. **Status:** AUTHOR_PROVED / EXACT_NATIVE_CHECKED / UNREVIEWED / NOT_ADMITTED. **Scientific input pin:** awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. **Current rule reads:** awdawmip/enterprise-math@87f0e39b6a564efe50ccf3a65d28d1c6790c2e8c; awdawmip/chatgpt-global-knowledge@f8e90e0f9122f1bd28874303b78985dbb0b205f8. Predecessor PREFIX-453@ffb0f5be9d1f196b01c1faff57e810b679413d9b.

## Problem and theorem

Fix the P000 signed native six-axis X6 primitive steps ±e_i, path duration N=q+1 and history residue r=(number of negative e_1 moves) mod q, with any integer q≥3. Raw terminal x∈Z^6 is chart-relative to a chosen Cell. For each r, allow any nonnegative rational histogram mass on reachable (r,x). Store the degree≤d joint monomials x^alpha independently in each history state. Under rational-affine, positive-rational, history-conditional BRC alternatives and arbitrary finite compositions, retaining all degree≤3 moments is sufficient for exact degree≤3 sector readouts via polynomial pullback.

**Theorem A (all q≥3).** The degree≤2 observation rank at N=q+1 is exactly 28q. The degree≤3 observation rank is exactly **84q−32**: sectors r=0,...,q−2 each have cubic rank84, and r=q−1 has cubic rank52. Thus precisely **56q−32** additional independent rational *linear* moment coordinates above the 28q quadratic moments suffice and are necessary for preserving every degree≤3 snapshot observer. At q=3,N=4, the complete cubic rank is **220**, versus 252 nominal cubic coordinates and 84 quadratic coordinates.

## Proof

Let D={+e_1}∪{±e_i:2≤i≤6}. For r≤q−2, take r negative e_1 moves, then q−r−2 positive e_1 moves, then any three moves in D. This embeds a translation of the full three-step D terminal support into the correct sector. In any s-dimensional signed t-step support, all polynomials of total degree≤t are unisolvent: choose the C(s+t,s) points formed by replacing at most t baseline −e_1 steps with +e_1,+e_2,...,+e_s. They form an invertible affine image (linear determinant 2) of the complete integer t-simplex grid; multivariate falling-factorial interpolation proves unisolvence. Now a cubic P(z,y), z first coordinate and y the remaining five coordinates, vanishing on three D steps restricts at z=0 to the full signed three-step y set, forcing P=zQ, deg Q≤2. At z=1 the signed two-step layer forces Q=(z−1)R, deg R≤1. At z=2 the signed one-step layer forces R=(z−2)C. The z=3,y=0 layer forces C=0. Hence the cubic rank of every earlier sector is full 84.

In the last sector r=q−1, the count of negative e_1 steps is exactly q−1, since 2q−1>q+1 for q≥3. Two D steps remain. Set z=x_1+q−1 and y=(x_2,...,x_6). Terminal layers are: z=0 with 51 signed two-step five-axis terminals {0,±2e_i,±e_i±e_j}; z=1 with ten terminals ±e_i; z=2 with one terminal y=0. Degree≤3 polynomials on the first layer have rank exactly **41**: among 56 cubic-in-five-axis monomials, ten square-free triple products y_i y_j y_k vanish, and five independent relations y_i³=4y_i−3∑_{j≠i}y_i y_j² hold. The remaining 41 monomials are independent by sign evaluation at 0, ±2e_i and ±e_i±e_j. Restriction to the remaining layers contributes at most 10+1. Conversely the following 52 polynomials are independent: the 41 surviving y-monomials; ten polynomials z y_i and z y_i²; and z(z−1). First restrict a hypothetical relation to z=0, then z=1, then z=2; each block of coefficients vanishes. Thus the last cubic rank is exactly 52.

For degree≤2, the same layer-peeling argument at the last sector forces P=zQ after z=0 (five-axis two-step support is quadratic-unisolvent), then Q=(z−1)C after z=1, then C=0 at z=2. Hence all 28 quadratic coordinates are independent there; the earlier sectors inherit full quadratic rank. Summing gives 28q and 84(q−1)+52. A linear encoder with fewer than 84q−32 coordinates has a kernel vector separated by a cubic observer. Add a large positive rational baseline to that vector and zero, yielding two valid nonnegative rational histograms that collide under the encoder but differ in cubic observation. The explicit 84(q−1)+52 moment basis attains the bound. QED.

## Explicit minimal cubic snapshot codec and decoder

Keep all 84 ordinary cubic monomials for r<q−1. In r=q−1 store the 41 five-axis y^beta (degree≤3) excluding pure cubes and square-free triple products, plus z y_i, z y_i² (1≤i≤5), and z(z−1). These 52 moments admit a rational decoder for any requested polynomial P(z,y) of degree≤3: reduce P(0,y) using y_i³=4y_i−3∑_{j≠i}y_i y_j² and the vanishing square-free triples to B(y) in the 41-basis. Put R_i^±=P(1,±e_i)−B(±e_i), α_i=(R_i^+−R_i^-)/2, β_i=(R_i^++R_i^-)/2, γ=(P(2,0)−B(0))/2. At every valid last-sector terminal,

P(z,y) = B(y) + z∑_i(α_i y_i+β_i y_i²) + γ z(z−1).

Therefore all 84 ordinary cubic moments can be recovered by exact rational linear operations. For an arbitrary future in the declared L3 language, decode once into the standard full cubic jet and propagate that jet by polynomial pullback. The reduced 52-port is tied to the known N=q+1 snapshot support; later supports may require the full standard cubic jet.

## Exact checks and resource evidence

The standalone Node.js certificate accompanying this note checks the full reachable signed-path supports at q=3,N=4 and q=4,N=5; computes modular ranks over the prime 1,000,003; and validates the decoder identity with doubled integer coefficients at every one of the 62 last-sector terminals for each of the 84 original cubic monomials. The actual run output is in PREFIX454_COMPACT_EXACT_CERTIFICATE.log.

A separate executed Python/Fraction package performed the same exact decoder test also for q=6,N=7, with cubic ranks (84,84,84,84,84,52). It imported the frozen native classes without changing their mathematical code: brc_transport.py Git blob be1debe367263931bd5e93fd750be3ed54624fe1; brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8; brc_histogram.py blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1. The original ControlPacket 84-path parallel and moment_action interfaces passed. Direct exact propagation through six history-conditional rational affine edges, including a shear, agreed with reconstructed cubic polynomial pullback on all output cubic moments (2082 propagated joint bins). PREFIX-453's two nine-path sources have identical quadratic ports but cubic x_2³ observations 0 and 24; the new 52-coordinate port distinguishes them.

Measured compact, uncompressed UTF-8 JSON byte counts at q=3,N=4 (all moments padded, rational pairs encoded as [numerator,denominator], tags codec/q/N):

| Source | Bins | HIST | Degree 2 | Full cubic | Reduced cubic |
| --- | ---: | ---: | ---: | ---: | ---: |
| Single | 1 | 60 | 559 | 1569 | 1380 |
| 84 chosen | 84 | 2078 | 605 | 1728 | 1502 |
| Full 20736 words | 1059 | 25739 | 631 | 1700 | 1491 |

The reduced cubic port saved 209 bytes (12.29%) relative to the standard full cubic port for the dense sample. Python reference three-repeat median conversion-and-serialization times, with tracemalloc enabled, were ~0.018 s (HIST), 0.100 s (M2), 0.297 s (M3), and 0.262 s (reduced M3). Observed peak traced allocations were 293552, 10844, 35882, and 56632 bytes, respectively. These are implementation-specific timings, not a universal runtime improvement claim: conversion from raw histograms and streaming operation costs differ. Histograms remain the smaller encoding for a one-bin source; degree2 moments remain suitable for a quadratic-only future consumer.

## Authority and next question

GitHub authenticated this run as awdawmip with repository push permission. Native Site gateway returned research_authority_granted=false and the current em_control_tasks query returned CONTROL_QUOTA. Current active Owner, native CLAIM, independent Review and Admission remain unconfirmed; this research note is an author-side scientific output. No P000 or ACTIVE worldview file is modified.

**PREFIX-455:** generalize the near-threshold rank deficiency at N=q+d−2 for higher degrees and quantify the cost of a typed native L3 jet with this exact snapshot decoder, including streaming update costs and rational bit growth. Scientific pin remains the frozen task input.

