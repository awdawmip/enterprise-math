# R47 — Sharp all-offset historical-source coverage: H*=225

Status: author-side proof and exact integer-enclosure verification; independent mathematical review pending.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent: R46, Draft PR #2000, commit `99bff704811c7bf39eafb3717c8f1b4dbc6659eb`.
Scope: auxiliary irrational-circle-rotation observer, with original historical interval/owner labels. A native-X6 correspondence is a separate typed task.

## R47.1 — Necessary and sufficient uniform cover criterion

Fix irrational theta in (0,1). The initial m>=2 phases {t theta}, 0<=t<m, determine m labelled **half-open** cyclic historical arcs I_k. Let delta be their minimum positive length. For H>=1, define P_H={{r theta}:0<=r<H}, and g_H as its largest cyclic gap. For integer J let B_(J,H)={{t theta}:J-H<=t<J}.

**Theorem:** Every historical arc I_k is intersected by B_(J,H) for **every integer J** if and only if g_H <= delta.

Proof, sufficient direction, including equality. Every half-open circle arc [a,a+ell) with ell>=g_H contains a point of P_H: otherwise its preceding and succeeding points form a complementary gap strictly longer than ell. This includes ell=g_H because the left endpoint belongs to a half-open arc. The block B_(J,H) is a rotation of P_H by (J-H)theta and retains the same gap lengths. Since every I_k has length >=delta>=g_H, all are met.

Proof, necessary direction. If g_H>delta, take a gap of length g_H and a shortest historical arc I_* of length delta. There is a nonempty open set of rotations that place I_* strictly inside that empty gap, with positive margin. For irrational theta, integer rotations n theta are dense and visit any open circle arc infinitely often; infinitely many source-block starts J therefore have I_* empty. Hence uniform all-J coverage fails. QED.

In particular the exact all-offset minimum is H*=min{H:g_H<=delta}. Since g_H is nonincreasing in H, g_(H-1)>delta certifies minimality once g_H<=delta. Finite samples of J are supporting checks, not the universal proof.

## R47.2 — Exact frozen S23/AV minimum 225, versus R46's strict 389

Frozen enclosure:
```
D  = 1000000000000000000000000
LO = 262204504569236716045286
HI = 262204504569236716045287
theta in [LO/D, HI/D], frozen theta irrational
m = 128
```

The phase orders and phase integer parts of all indices 0..388 are identical at both rational endpoints. Every gap is therefore affine in theta across the full enclosure. We check all 225 x 128 source-gap versus historical-gap inequalities at both endpoints (57,600 exact integer comparisons); they then hold for every enclosed theta.

The shortest historical arc runs from index 103 to index 42 and has
`delta=16-61 theta`. The maximum 224-block gap runs from index 60 to 163 and has `g_224=103 theta-27`. Therefore `g_224-delta=164 theta-43>0`. The maximum 225-block gap runs from index 164 to 103, with `g_225=16-61 theta=delta`. By R47.1 and monotonicity,

**H*=225 is the smallest block length that covers all 128 historical labels at every integer source offset J.**

For 225<=H<=388 the maximal gap equals delta; at H=389 the gap becomes `59-225 theta<delta`, recovering R46's first *strict* certificate. R46's formerly open possibility of a shorter all-offset cover is thereby settled.

All numerators below have denominator D:

| Gap / difference | At LO | At HI |
| --- | ---: | ---: |
| delta = g225 | 5525221276560321237554 | 5525221276560321237493 |
| g224 | 7063970631381752664458 | 7063970631381752664561 |
| g224 - delta | 1538749354821431426904 | 1538749354821431427068 |
| g389 | 3986471921738889810650 | 3986471921738889810425 |

The label map is always based on the initial 128 half-open arcs, using the same bisect_right modular owner rule as R46.

## R47.3 — 298-run integrated risk compiler

The R46 suffix compiler requires only that each current stage's H-source suffix contains every owner label. Replace H=389 with the newly certified 225. Last-source ages, missing-owner counts, R45 Farey boundary transfer and the risk increment identity are unchanged.

The exact frozen calculation again produces 78 Farey stages, 9,697 positive single-step updates and 298 maximal affine runs to n=10^12+128. Final coefficients:

`R_(10^12+128)=-4017401528447+15321634290944 theta`.

Regenerated 15,356-byte TSV has SHA-256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`, byte-identical to the R32 reference and the original R46 calculation.

Source inspections per interval endpoint decrease from 78*389=30,342 to 78*225=17,550, a **42.1594% decrease** (12,792 fewer). This compares like-for-like source scans; certification, integer bit complexity, phase matching, output and independently verified source costs remain separate.

## Independent examples and scientific context

Using theta=sqrt(2)-1 in a strict integer-isqrt denominator-10^30 enclosure, exact auxiliary examples give the minimum uniform H values m=4 -> 7; m=7 -> 17; m=13 -> 41; m=21 -> 41. Every example passes 1,201 checked signed offsets at H and exhibits a counter-offset for H-1.

The broader rotation-gap/continued-fraction framework is classical (three-gap theorem): Tony van Ravenstein, *The Three Gap Theorem (Steinhaus Conjecture)*, J. Australian Math. Soc., online 2009, https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/three-gap-theorem-steinhaus-conjecture/EA75E140919DEA9A55FEFD01EB2F677F ; Diaaeldin Taha, *The Three Gap Theorem, Interval Exchange Transformations, and Zippered Rectangles*, 2017, https://arxiv.org/abs/1708.04380 . The exact all-offset half-open statement is proved above; the frozen H*=225 computation and owner-labelled integration are R47's project-specific research increment.

## Scope and next action

The optimality statement quantifies **every integer block offset J** for the fixed m=128 historical partition. A stage-specific or fixed-J suffix can be smaller (R37 already observed a 164-source cover at one specific J). R48 should compute and certify the actual shortest suffix at each of the 78 stage endpoints, compare total work and develop bit-cost-aware adaptive selection. All mathematical results in this PR are author-side; CLAIM, independent review, Working Truth and P000 remain governed by their own contracts.
