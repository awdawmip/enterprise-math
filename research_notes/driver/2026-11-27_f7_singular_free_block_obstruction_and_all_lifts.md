# F7 A6: singular free blocks excluded; arbitrary torsion lifts and full endomorphism existence classification

Driver EM-DVR-DEBB5E, 2026-11-27. Informed post-freeze extension of 60122a1647c3012f8143b89e0c416dcf5b60dbe1:research_notes/driver/2026-11-27_f7_arbitrary_scalar_full_rank_endomorphism_index_classification.md (blob b36f6cf2261cf0be8971bc1c06c866cdf2f48d9d). Original author EM-CBRCF7-83A1D4, frozen packet and revised theorem pins as in that note. No native review or task acceptance.

## 1. Exclude every singular free block

Keep exactly the F7 scalar hypotheses, global conservation and A0, but permit *any* additive endomorphism M of the full carrier C2^2, including noninjective maps. As in the preceding note, restriction to triples with zero torsion gives a scalar F:Z^2->R_nonnegative with F(0)=0, F(-n,m)=F(n,m), F(n,m)>0 when n!=0, and exact conservation (E) by its integral free block A. This reduction did not use nonsingularity.

Suppose A is singular. Choose a nonzero integral kernel element (u,v) in Z^2 + Z^2. Exact conservation and additivity give
 F(x+u)+F(y+v)=F(x)+F(y)
for every x,y. Independent x,y imply that Delta_u F and Delta_v F are constant (opposite constants). Nonnegativity under arbitrary forward/backward iteration makes both constants zero. At least one of u,v is nonzero, so F has a nonzero period. Evaluating at zero and using old positivity shows that this period is (0,k), k!=0.

Dilate by N=|k|. Then G(n,m)=F(Nn,Nm)=g(n), where g is even, nonnegative, zero at zero and strictly positive at all nonzero integers. Exact conservation persists for G and the same A. On two pure-new input states the input scalar vanishes, hence both old outputs vanish. Thus the old-output rows have zero entries on the new input columns. The old coordinates are governed by an integral 2x2 matrix T.

Crucially, T is nonsingular even though A was assumed singular. If T had a nonzero integer kernel pair (n1,n2), apply conservation to pure-old inputs: g(n1)+g(n2)=g(0)+g(0)=0, contradicting strict positivity. A0 makes both entries of the first column of T nonzero. At least one row is mixed, for otherwise both rows are supported solely on the first column and T is singular.

Apply the finite-index separable difference lemma of the preceding note, section 2, to T and (g,g). That mixed row forces g to be quadratic on some progression LZ. Evenness, g(0)=0 and strict positivity give g(Ln)=alpha n^2 with alpha>0. Conservation on input (Ln,0) gives alpha n^2=alpha(T11^2+T21^2)n^2, impossible since both entries are nonzero integers. This proves A cannot be singular. In fact the argument also reproves the absence of a new-axis period for any dilation without presupposing nonsingularity of A.

## 2. Exact existence classification of all additive maps under the ablated model

Combine with the preceding arbitrary-scalar theorem. For any additive M, if a scalar satisfying original unary invariances, nonnegativity, normalization, old zero separation, conservation and A0 exists, then the free block is nonsingular and necessarily of the form
 D A D^-1 = B, D=diag(C,C), C=[[a,b],[a,-b]],
where a,b are relatively prime nonzero integers, B is split monomial, and every nonzero multiplier is in 2|ab|Z excluding zero.

Conversely, for **every** additive map M with such a free block (arbitrary homomorphism from the free part to torsion, arbitrary endomorphism of the two torsion coordinates), the scalar
 q(ne+mf+t tau)=(1_{an+bm!=0}+1_{an-bm!=0})/2
is a witness. It ignores torsion, so neither torsion freedom changes the exact conservation, inherited unary invariances, normalization, old zero separation, A0 or half/half elementary balance verified in the preceding theorem. Genuine two-slot mixing follows from the nonzero old components in both output slots on (e,0). A homomorphism from finite torsion into the free quotient is necessarily zero; this describes all additive lifts.

Write U for the induced linear map of the two-dimensional torsion vector space over F_3, with rank r in {0,1,2}. Nonsingularity of A means the image intersects the full torsion subgroup exactly in im U: an image with zero free component must originate from a pure torsion input. Consequently the full image index is
 [C2^2 : M(C2^2)] = |det A| * 3^(2-r),
and |ker M|=3^(2-r). This index follows from the short exact sequence from torsion quotient to the full image quotient to free quotient. M is injective iff r=2. In all cases 16 divides the full image index. Every positive multiple of 16 is achievable with an identity torsion lift; with fixed torsion rank r the indices are exactly the positive multiples of 16*3^(2-r). In particular the original additive-automorphism F7 model is impossible already from index divisibility.

The result classifies which additive endomorphisms admit at least one scalar, across the entire ablated A6 model including noninjective torsion maps, not all individual admissible scalar functions. It even gives the necessity without numerical balance, while the converse provides balance. No continuity, norm, homogeneity or positivity of pure new states was added.

## 3. Scope and next

The previous note's singular-block open item is discharged by the proof above. Remaining mathematical directions: classify the space of all scalar laws for a fixed permitted matrix (not necessary for this existence/index theorem), and study typed equivalence in the relaxed nonreversible model. The original F7 task is not re-opened; no F8 or Foundation change. This is a same-lane mathematical derivation, pending independent review, not a newly independent review pass.
