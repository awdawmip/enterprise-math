# PREFIX-620-R2 — Uncalibrated X6-BRC terminal tomography: sharp 3/4/5 time-aware versus 6 fixed phase sensors

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT PROOF + EXECUTED ORIGINAL NATIVE-BRC CHECKER; independent Driver review pending.
Frozen scientific source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessors: PREFIX-617 full48 positive eight-state intertwiner (00cdf3bcbea94aaa623e8b3e969f2354a5bfd21e), PREFIX-618 calibrated four terminal sensors (a546f6402d43d772975cf8adec4eee01f06d8c9e), PREFIX-619 original STAR source checker (9467c5233981f096a56954f76c7893c7234826e1). Normative context is read separately, and frozen science is not repinned.

## Mathematical problem and scope
Fix the original X6-STAR native 48-phase positive BRC branch-sum operator Q(g), with six-axis weights (1,1,1,1,0,0), and four-point controlled *difference* input d=e4+e11+e14+e32. At known terminal time t, observe x_t=lambda Q(q_t)...Q(q_1)Q(b)Q(a)d with *unknown* a,b,q_s>=0 and lambda>0. Determine the smallest number of original phase-coordinate readings that reconstruct all 48 terminal positive sums, (i) if indices may depend on t, (ii) if the same fixed sensor indices must work for all t. This does not identify native 96-port tagged/path histories with their 48 positive sums.

## Exact native BRC factorization used
PREFIX-617 proves for the original STAR source Q(g)H = H diag(C,B(g)), where C=2P is a four-cycle and B(g) shifts w0->w1->w2->w3 with wrap w3->4(g+3)w0, and H=[H_C H_B] has precisely the following nonzero rows:

| column | original phase row(s) | coefficients |
|---|---|---|
| C0 | 2,3,15 | 1 |
| C1 | 5,28,29 | 1 |
| C2 | 27,38,39 | 1 |
| C3 | 16,17,41 | 1 |
| W0 | 3,14,15 | 1 |
| W1 | 17,40,41 | 2 |
| W2 | 26,27,39 | 4 |
| W3 | 4;5,29 | 4;8 |

After two unknown initial gates, c_init=lambda(0,0,4,4) and w_init=lambda(b+3,a+3,1,1/2). Consequently x_t=H_C c_t+H_B w_t with c_t[j]=2^t*c_init[(j-t) mod4]. Exactly two adjacent coordinates of c_t, indexed (t+2) and (t+3) mod4, equal 4*2^t*lambda, while the other two vanish. The four native terminal samples at rows (14,40,26,4) always give w_t=(x[14],x[40]/2,x[26]/4,x[4]/4). Pure C readings are x[2]=c[0], x[28]=c[1], x[38]=c[2], x[16]=c[3]. Also x[3]-x[14]=c[0] and x[27]-x[26]=c[2].

## Theorem 620.1: the exact time-aware sensor minimum
For all nonnegative gates and positive lambda, with t known but a,b,lambda unknown, the least number of original phase readings for uniform complete terminal x_t recovery is 3 when t=0, 4 when t=1, and 5 when t>=2.

**Construction.** For t=0, read (14,40,26); w2=lambda, w3=lambda/2, so recover lambda, w and c. For t=1, read (14,40,26,4); w3=lambda gives lambda and therefore the complete eight-state lift. For t>=2 read (14,40,26,4,p_j), where j=(t+2) mod4 and (p_0,p_1,p_2,p_3)=(2,28,38,16). The fifth reading equals 4*2^t*lambda, so lambda=x[p_j]/(4*2^t). Four dedicated rows recover w and known c_t then recovers all 48 outputs.

**Lower bound even with nonlinear decoding.** The full48 output map from (lambda,w0,w1,w2,w3) has five independent columns: the four W-isolating rows give a diagonal minor, and a pure-C row separates lambda. The attainable parameter image has interior of dimension d(t)=3,4,5: at t=0 independently vary lambda,a,b; at t=1, w=(2lambda(q1+3),lambda(b+3),lambda(a+3),lambda), so vary lambda,a,b,q1; at t=2, w=(4lambda(q2+3),2lambda(q1+3),lambda(b+3),lambda(a+3)), so vary lambda,a,b,q1,q2; at t=3 vary lambda,b,q1,q2,q3 holding a positive fixed; at t>=4 vary lambda and the last four gates (one per residue class), holding earlier values fixed. All these parameterizations have full-rank Jacobians on a positive open box. Any k<d(t) native phase selections yield a linear rank-deficient map of this open parameter family to R^k: a small displacement along its nonzero kernel leaves *all samples* equal while changing full48. Thus no decoder can recover the lost output. The constructions attain the bounds.

## Theorem 620.2: six time-independent phase sensors, and six are necessary
The single fixed set S6=(14,3,40,26,27,4) works for **every** known t>=0. The four entries (14,40,26,4) recover w. Differences u0=x[3]-x[14]=c0 and u2=x[27]-x[26]=c2 recover either c0 or c2. For every t the active C pair is adjacent, hence exactly one of c0,c2 equals 4*2^t*lambda, and the other is zero. The active index is known from t. Therefore lambda, c_t and x_t are reconstructed exactly.

No fixed set of five phase-coordinate sensors works for all t. Indeed, for t>=4 the attainable (lambda,w) space has dimension five and full48 output is injective in it; any five successful rows must give rank five for each of four terminal time residues. Since the W0,W1,W2,W3 native support groups are disjoint, a five-row selection must cover all four groups. The remaining fifth row is either (a) a pure C row, whose one C-class coefficient vanishes for two residues; (b) a second row of one W group, whose extra information after eliminating that W variable is at most its single associated C class, likewise zero for two residues; or (c) a zero row. Hence rank five fails at some residue. This is an open-set indistinguishability proof, regardless of nonlinear decoder. Six is optimal for **time-independent phase-coordinate sets**, while five time-aware coordinates suffice for t>=2.

## Exact BRC computation and exhaustive finite rank witness
The standalone Python 3 checker rebuilds original 48 signed STAR phases and its 96 structural nonzero positive-branch-sum transitions. It checks the gate-affine 48x8 original-source intertwiner at g=0 and g=1 (768 coordinate equalities), which establishes the symbolic identity for all g by affinity; compares native Q evolution to H-lift and both recovery algorithms on 44 exact Fraction test cases at terminal lengths 0,1,2,3,4,5,6,7,8,12,20 and four nonnegative initial configurations, including zero and rational gates (4,224 exact reconstructed output-coordinate comparisons). It enumerates all C(16,5)=4,368 candidate five-row subsets of the 16 possible active phase indices and the four time residues. No five-row selection has full rank in all four residues; the highest possible coverage is two residues. S6 has rank five in all four residues. Exact input/case inventory and raw results accompany the checker. Universal statements rest on the explicit intertwiner and rank argument, not finite-test extrapolation.

## Preserved source/observer boundary and next experiments
This is an exact result about the four-point paired *difference signal* in the original positive BRC 48-phase quotient with known terminal time. Neither unknown absolute input state, the original gate word, nor the genuine 96-port/576-tagged-action path history is reconstructed. P000/ACTIVE native-world and provenance constraints are unchanged. Next: (1) build a typed *original* 96-port history and seek a two-history separation under one permitted future tagged operator, or prove a narrowly scoped fiber-preservation result; (2) classify five fixed sensors on selected time residues/gate subclasses; (3) compare time-dependent five-sensor and six-fixed-sensor readout cost, including exact rational bit lengths and source setup. Independent Driver review, formal Native Result and Foundation acceptance remain pending.
