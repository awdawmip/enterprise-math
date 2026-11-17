# R5 K3 — Two-level source-mask fibers and full proportional-clock four-observer classification

Date: 2026-11-04 (Asia/Shanghai). Scope: source-sensitive K3 common-terminal-label stopped experiment, author-side exact theorem, unreviewed and not natively admitted.

## Scientific source and assumptions

The immediate predecessor is Enterprise Math immutable commit 0f849a3451760e49f33eb94fb2f31c540489580d, research_notes/brc_r5_k3_all_signed_clock_hull_20261104_t0339/RESEARCH.md. Earlier exact source-uniform answer classification is commit c7caa7554474a18e3e5a71398e0293317624c10c, research_notes/brc_r5_k3_common_label_uniform_clock_rigidity_20261103_t1835/RESEARCH.md. Frozen scientific pins are account global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e; current behavioral policy was read separately. P000 and ACTIVE Heartbeat X6/remainder worldview are unchanged. This is an auxiliary two-law finite stop/continue experiment with four BRC-positive provenance sources, not an asserted native X6 physical embedding.

Fix S=(C,I,BJ,IJ), c=(1/8,1/6,1/16,3/32). FULL upstream variables 0<=x,y<=1, 0<=i<=1-x; seedless LR restricts i=(1-x)y. Carrier weights w=(1/8,(1-x)/6,y/16,3i/32); d=y/16+3i/32. For sourcewise z_s,t_s,u_s in [0,1], put M_s=w_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s. LR has one common triple z,t,u. Four actual real-policy observables:

eP=107/128-21x/128+d/4-(1/2)sum S_s+sum p_s S_s/8;
eQ=13/64+3x/64-d/2+(1/8)sum S_s+sum q_s S_s/32;
TP=3+sum M_s+(3/2)sum S_s+sum r_s U_s;
TQ=3+(1/2)sum M_s+(3/8)sum S_s+sum v_s U_s/4.

Assume 0<k<1, v_s=k r_s, 0<r_s<1 for all four sources, and arbitrary 0<p_s,q_s<1. Thus there are 13 free real parameters (one k, four r and eight answers).

## Lemma A — two remaining time-exposed masks have an error-fiber obstruction

For a strict two-level clock r_s = R on a high group D, and r_s=L outside D, with 0<L<R<1, assume D is either {C,I} or {C,BJ}. Then the FULL four-observer convex hull differs from the seedless LR four-observer convex hull, for every allowed p and q.

Proof. Define mu(r)=(9+2kr)/(8(3+r)), strictly decreasing in r since mu'(r)=(6k-9)/(8(3+r)^2)<0. For any t in (mu(R),mu(L)), the time-only direction n0=(0,0,t,-1) satisfies 0<t<3/8. The stage scores at source s are 0, t-1/2, 2t-3/4 and g_s=(2+2r_s/3)t-3/4-kr_s/6. The two intermediate scores are strictly negative, while g_s>0 exactly for s in D, negative outside D. The coefficient of r_s in g_s is 2t/3-k/6>0 by t>mu(R)>k/4.

A FULL clock maximizer W takes (x,y,i)=(0,1,1), preserving all positive carrier capacities, chooses stage 3 at each high source and stage 0 at each low source. The positive source scores sum to sum_{s in D}c_s g_s. A seedless LR clock maximizer must use common stage 3 and the accessible upstream mask D. The four LR stage-3 corner masks are {C,I} at (x,y)=(0,0), ALL at (0,1), {C} at (1,0), {C,BJ} at (1,1). Strict high/low score signs make D the unique best corner mask. The LR clock support is the same as FULL, and its exposed four-observer face is a singleton H (stage differences on zero-capacity sources are observationally null). Uniqueness also holds for real LR behavioral strategies by multi-affinity and strict corner maximality.

If D={C,I}, H has x=0,y=i=0, hence d_H=0. W has x=0,y=i=1, d_W=5/32. Both have equal positive M,S,U for C,I, with zero M,S,U elsewhere. Direct substitution yields W-H=(5/128,-5/64,0,0).

If D={C,BJ}, H has x=y=1,i=0, hence d_H=1/16. W has x=0,y=i=1,d_W=5/32. Both have equal positive M,S,U for C,BJ, with all other M,S,U zero. Thus W-H=(3/16,-3/32,0,0).

The source-specific p_s,q_s terms cancel exactly in either case because S_s agrees for every source. Thus W differs from singleton H while lying on the LR clock-support hyperplane n0. Consequently W is outside the LR four-observer convex hull. Finite deterministic LR vertices imply a sufficiently small positive epsilon makes n=(epsilon,0,t,-1) an explicit strict signed support separator. This proves the claim for all real parameters in the stated region.

## Theorem B — complete 13-real-parameter proportional-clock four-observer classification

For the above common-label K3 model with 0<k<1 and v_s=k r_s:

conv O4(FULL) = conv O4(seedless LR)
if and only if
r_C=r_I=r_BJ=r_IJ,
p_C=p_I=p_BJ=p_IJ,
q_C=q_I=q_BJ=q_IJ.

In the equality case the actual real-behavior observer images also coincide.

Proof. A previous exact all-signed two-clock support theorem (immediate predecessor cited above) gives complete time-hull equality exactly for (i) all equal r, (ii) two-level high group {C}, {C,I} or {C,BJ}, (iii) three-level r_C>r_I>r_BJ=r_IJ or r_C>r_BJ>r_I=r_IJ. When a clock kernel is outside this list, a clock-only separating normal is already a four-observer separating normal. For nonuniform clock kernels inside the list: {C} and both three-level types have unique highest C, for which the predecessor's exact C-face theorem constructs a four-observer obstruction independent of all p,q; the remaining two high groups are covered by Lemma A. Therefore equality of four-observer convex hulls forces all four r_s to be equal.

When r_s=r and v_s=kr are both source-constant, the earlier source-uniform-clock rigidity theorem (cited above) gives equality of four-observer convex hulls if and only if all p_s are equal and all q_s equal, for every 0<r,v<1 (hence also v=kr). For sufficiency its explicit real-policy aggregation preserves x,d,M=sum M_s,S=sum S_s,U=sum U_s through y'=32d/(5-3x), i'=(1-x)y', z'=M/Tbar, t'=3S/(2M) where M>0 else 0, u'=U/S where S>0 else 0, Tbar=1/8+(1-x)/6+d. When r,p,q are common, all four observers depend only on these retained aggregates. Therefore the actual FULL and LR real observer images coincide. QED.

The conclusion classifies this K3 proportional-clock family. The broader R5 mother objective of equal convex hulls but unequal actual real observer images remains open for other finite experiments.

## Exact rational verification

The companion standalone Python 3 standard-library Fraction verifier enumerates six FULL upstream vertices times 4^4 source stage patterns = 1536 FULL deterministic observations and four LR upstream corners times four shared stages = 16 LR deterministic observations for each of the two high-group examples. Take k=1/2, high R=4/5, low L=1/5, and independent p=(1/4,1/2,3/4,1/3), q=(3/4,1/2,1/4,2/3). In both examples n0=(0,0,1/3,-1), n=(1/4096,0,1/3,-1). Exact outputs:

High {C,I}: H=(431/576,355/1536,673/180,4663/1440); W=(907/1152,235/1536,673/180,4663/1440). LR clock support=-1721/864, mixed full support=-28194143/14155776, mixed LR support=-14097139/7077888. Exact full-minus-LR support gap=5/524288; witness L-infinity distance lower bound=15/2097536.

High {C,BJ}: H=(485/768,727/3072,139/40,1009/320); W=(629/768,439/3072,139/40,1009/320). LR clock support=-383/192, mixed full support=-2091481/1048576, mixed LR support=-2091529/1048576. Exact full-minus-LR support gap=3/65536; witness L-infinity distance lower bound=9/262192.

All exact assertions in the executed verifier passed. The exhaustive deterministic support tests establish these rational examples; the continuum parameter theorem follows by the proofs above and the explicitly cited earlier all-real signed-support and uniform-clock results. No independent reviewer/Result/admission is implied by finite tests or Git publication.

## Next scientific unit

Explore source-dependent, genuinely nonproportional r_s,v_s where neither clock support mismatch nor the currently known time-exposed error-fiber obstruction applies. For a rational candidate compare ALL 1536 FULL and 16 LR deterministic four-observer vectors by exact rational convex combinations with at most five LR vertices per FULL vector; otherwise retain a rational Farkas separator. Only after proving all-signed full four-hull equality test actual real observer-image nonmembership by an exact semialgebraic method. Maintain every BRC provenance source, P000, ACTIVE worldview, and frozen scientific pins.

## Authority and persistence context

This note is an author-side portable proof, not canonical mathematical admission. GitHub connector identity awdawmip has repository push/admin rights; live Enterprise Math Site observation on 2026-11-04 reports static_machine_readonly, research_authority_granted=false; control owner lookup returned CONTROL_QUOTA. Native Researcher-ID, active owner, CLAIM, Result and independent Driver review were not established by this session. No credential material, protected worldview edits, or shared task state mutations are included.
