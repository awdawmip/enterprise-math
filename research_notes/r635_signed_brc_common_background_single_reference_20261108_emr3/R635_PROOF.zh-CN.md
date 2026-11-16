# R635 — 共享加性背景下的精确 BRC 方向纤维与单参照定理

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED.

## Frozen substrate and declaration

Scientific pin R462: 18783e01e3646c72b7aab3b16d3f565e83e6446f; signed binomial K generator blob 7fa7a762f758b30c6090468ac43487daa34abad8; theta=0. Immediate predecessor R634: 1fab59f1bb9b0d89d79baa51989aaf30cd33f35b.

Fix the six native X6 spatial axis labels, without changing native spatial dimension. For j=1,...,6 let P_j=K_(2j-1) and M_j=K_(2j). The frozen input has
P_j=t^(2j-2) U_j, M_j=t^(2j-1) V_j,
U_j(0)=(2,-8,6,106,83,9)_j and V_j(0)=(-1,-11,53,119,36,1)_j, all units modulo 5.

Unknown orientation pi in S6 assigns j=pi^(-1)(x) to spatial axis x. Each axis carries gains A_x^+,A_x^- in Z[t] with nu_5(A_x^+)=a>=1 (known common a) and nu_5(A_x^-)>=a-1; A_x^+ leading coefficient mod 5 is nonzero. Define nu_5 as the first nonzero mod-5 polynomial coefficient; for the positive gain we additionally require the integer t-valuation to equal a. Both readouts share ONE UNKNOWN POLYNOMIAL H in Z[t] across ALL six axes and both probes:

Y_x^+(t)=A_x^+(t) P_j(t)+H(t),
Y_x^-(t)=A_x^-(t) M_j(t)+H(t).

Observer: the twelve mod-5 jets through degree d>=0, optionally augmented by ONE matched background reference R=H mod 5 through the same degree. This is a stronger cross-axis background coupling than R634; its admissibility for actual Source X6 joint-field operators is NOT presumed. A matched reference on any one axis reveals H for all six only because of this exact common-mode hypothesis.

Define m=clamp(floor((d-a)/2)+1,0,6), h=6-m, with clamp(v,0,6)=min(6,max(0,v)). A fiber counts distinct pi compatible with one observed transcript, permitting nuisance parameters to vary with pi.

## Theorem A — no direct reference: exact worst-case fiber

For every a>=1 and d>=0, the maximum possible orientation-fiber size is

F_0(d,a) = max{2, h!}.

Proof of upper bound. For distinct x,y the common H cancels in the positive-probe difference:

Y_x^+-Y_y^+ = A_x^+ P_i - A_y^+ P_j.

The two nonbackground terms have STRICTLY DISTINCT mod-5 orders v_i=a+2i-2 and v_j=a+2j-2. Thus, including truncated jets,
delta_d(x,y) := nu_5( jet_d(Y_x^+-Y_y^+) )
= min(v_i,v_j) when min(v_i,v_j)<=d, and infinity otherwise.

Define D_x=max_{y!=x} delta_d(x,y) in the ordered extended set of degrees plus infinity. If h>=2, D_x=v_j for each j<=m and D_x=infinity for j>m: for each visible j there exists a later axis, and among the at least two hidden labels each hidden axis has a hidden partner with zero difference jet. Consequently j<=m is individually determined, and the h remaining labels may be permuted in at most h! ways.

If h=1 or h=0 (m>=5), D_x=v_j for j=1,...,4, while the two axes with j=5 and j=6 both have D_x=v_5 when d>=v_5; hence at most two orientations. When m=4, h=2 and the h! bound already equals two. This proves F_0<=max(2,h!).

Sharpness for h>=2. Let W=product_(j=1)^6 U_j V_j and C_j=t^(a+2j-2)W. Choose H=0 and, on the axis bearing label j,
A^+=t^a (W/U_j), A^-=t^(a-1)(W/V_j), both honest integer polynomials since W contains each divisor. Then Y^+=Y^-=C_j. All leading positive coefficients are 5-units because every U_j(0),V_j(0) is a 5-unit. For all hidden labels j>m the two d-jets C_j vanish. Permuting those h labels therefore preserves the complete transcript, giving h! orientations.

Sharpness for m>=5, including full infinite polynomials. Use the same W and C_j, with first orientation identity and H=0. Let H'=C_5+C_6 and interchange labels 5 and 6, leaving labels 1..4 unchanged. For every original axis j<=4,
C_j-H'=t^(a+2j-2) W [1-t^(v_5-v_j)-t^(v_6-v_j)].
For original axis j=5 now assigned label 6,
C_5-H'=-t^(a+10)W.
For original axis j=6 now assigned label 5,
C_6-H'=-t^(a+8)W.
In each case, for the newly assigned label k the corrected output has the form t^(a+2k-2) W Q_j with Q_j(0)=+1 or -1. Define
A_new^+=t^a (W/U_k)Q_j, A_new^-=t^(a-1)(W/V_k)Q_j.
Both are legal integer polynomials with positive first gain 5-unit, and yield exactly the original C_j for BOTH probes after adding common H'. Thus two different S6 orientations generate the same complete twelve-polynomial transcript. Combined with the upper bound, F_0=max(2,h!) follows for all d. QED.

## Theorem B — ONE matched common-background reference

When R=H is provided to the same d-jet precision, subtracting it from every Y_x^+ produces the pure response A_x^+P_j with distinct known valuation v_j when v_j<=d, otherwise zero jet. Therefore the complete calibrated transcript fixes m labels and leaves exactly the h unseen labels freely permutable at worst. The witness C_j above realizes that ambiguity. Consequently

F_1(d,a)=h!.

Full 720-state orientation reconstruction holds iff h<=1, equivalently d>=a+8. At d=a+8, m=5, h=1, so F_1=1 while F_0=2. The one background reference is NECESSARY and SUFFICIENT within the declared choice of (zero vs at least one) matched common-mode references; one reference suffices irrespective of which spatial axis reports it. For d<=a+7, h>=2 and F_1>=2, proving the depth bound sharp.

## Representation, scope and future operations

This is an EXACT STATIC OBSERVER-FIBER classification only. The "2" for no reference persists under unlimited coefficient precision because a second common H' and changed gain polynomials realize an exact polynomial collision; it is NOT a statement that physical X6 admits such gains. The common H remains a retained joint field, not an erased spatial dimension or physical time. This result determines orientation information under the stated readout; it does NOT certify quotient safety for arbitrary future branch append, native rotations beyond S6, triad dynamics, sources, path/grade updates, or heartbeat time. Retain those coordinates until an actual operation-specific descent proof.

BRC reuse: signed twelve-branch K polynomials and typed positive/negative probes; S6 orientation skeleton and explicit observable differences. R633 supplies independent-gain full-zero obstruction and R634 supplies the five independent-reference comparator. New result: with a shared single cross-axis background, worst-case uncertainty drops from 720 to 2 with no reference at d=a+8, then to 1 with one reference. This model switch is a hypothesis to test against Source field couplings, not a silent promotion.

## Computation and next question

R635_VERIFY.py regenerates all signed K from the pinned integer binomial generator, constructs W, both complete collision representations, and checks 60,672 exact integer/mod-5 assertions: 3 gains (a=1,2,4), 14 cutoffs each, all 720 permutations and two fingerprint observers, plus polynomial identities. Output: R635_EVIDENCE.json; marker R635_SHARED_BACKGROUND_SINGLE_REFERENCE_PASS. The theorem is analytic; finite enumeration checks only the declared frozen six-axis family.

Next unresolved task: locate an authentic Source X6 joint-field operation whose six backgrounds are one common H (or a certified cross-axis lower-rank law), and prove that the reference R can be acquired without modifying gains or source provenance. If exact common mode fails, identify the minimal retained cross-axis residual coordinate and test a rank-two background as an alternate construction. Owner/CLAIM and Driver review require independent live control authority.
