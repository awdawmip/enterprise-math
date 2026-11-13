# R5: Exact surjectivity of the four-dimensional seedless-LR behavioral image

Date: 2026-10-30 (Asia/Shanghai). Scope: finite auxiliary two-law fourteen-history stopping tree with exactly two likelihood-ratio collisions. It is not a native Heartbeat/X6 dynamical or physical-measurement claim. Author-side classification: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Pinned sources, lineage and permission

Frozen GLOBAL_KNOWLEDGE_V1 main@78f6e3adeafa9ba289243bc44594ba502f512f6f and Enterprise Math main@ed9e44843ff386caea4371cb3990323cbf219457, read using the connected GitHub tool. Global bootstrap, operating manual and ACTIVE worldview and project AGENTS, P000, joint-observer preservation, Heartbeat/X6 and portable research protocol were consulted. The predecessor at PR #1663 commit dcb6e3ffbcd739f04efe77efe3be1faca5dd1aba gives the exact two-simplex reduction; preceding commit 30f58a195a07311dd7f3fe636b0fe487c916bd70 established full-rank convex-hull equality by 647 rational mixtures. This new theorem independently verifies the hull by exact supporting inequalities and settles the ACTUAL real-image membership question.

Current authenticated GitHub account is awdawmip; this is not a Source Researcher identity. The native DIRECTED_RESEARCH context has authority_granted=false, complete_task_packet=false; the current owner query returned CONTROL_QUOTA. Neither a Source CLAIM nor a Result nor independent Driver review is asserted. This PR artifact is portable author-side preservation only, and neither P000 nor the protected worldview was changed.

## Exact source-labelled model

Fourteen histories in index order A,B,A0,A1,B0,B1,A00,A01,A10,A11,B00,B01,B10,B11 have rows (time,Pmass,Qmass,parent), with both measures normalized by 360:

~~~text
(1,120,240,-1) (1,240,120,-1)
(2,60,180,0) (2,60,60,0) (2,180,60,1) (2,60,60,1)
(3,30,108,2) (3,30,72,2) (3,30,45,3) (3,30,15,3)
(3,90,36,4) (3,90,24,4) (3,20,40,5) (3,40,20,5)
~~~

Each node has a real stop probability in [0,1]; survivors are forced to stop at time 4. FULL permits 14 independent decisions. Seedless likelihood-ratio (LR) permits 12 independent decisions indexed only by (time,Pmass/Qmass), with A1/B1 sharing one and A11/B11 sharing another. P/Q path labels and conditional history mass are retained, never silently identified.

Define unnormalized four-flow observation z=(r,x,y,s): r is the Q stopping mass at A11/B11; x is the total stopped P mass weighted by (4-time) at times <=3; y analogous Q; s is stopped P mass at A10/B10. Deterministic policies produce integral z; real policies give multi-affine z. At eta=delta=1/1000, the actual original four-observer map is

~~~text
TP=4-x/360; TQ=4-y/360
eP=21/100+TP/20+TQ/100+delta*s/360
eQ=41/100+TP/200-TQ/30+eta*r/360
~~~

The mapping between z and (eP,eQ,TP,TQ) is invertible affine for nonzero eta,delta. The conditional terminal error kernels are strictly between zero and one for this previously verified parameter choice. No persistent random seed is permitted in LR.

## Theorem A (face-fiber downset criterion): ALL real behavioral policies

Let f:[0,1]^n to R^d be continuous and multi-affine, and K=conv{f(b):b in {0,1}^n} a full-dimensional bounded polytope. For each nonempty proper face F, let M_F be the Boolean masks b whose f(b) lies in F. Suppose M_F has an anchor a_F in M_F with this downset condition: for every b in M_F, every single-bit flip of b toward a_F remains in M_F. Then f([0,1]^n)=K.

Proof. The Bernstein expansion f(p)=sum_b w_b(p)f(b), w_b(p)=product of Bernoulli factors, has w_b >=0 and sum_b w_b=1. Every face F is exposed, so f(p) is in F precisely when every Boolean corner of strictly positive product weight belongs to M_F. If p belongs to f^{-1}(F), move p along the straight line to anchor a_F. Every positive-weight corner along this movement arises by changing a subset of originally supported corners' bits toward anchor values; repeated applications of the downset condition keep every such corner inside M_F. Thus every proper-face inverse image f^{-1}(F) is star-shaped about a_F, hence nonempty and contractible.

Build h:K to [0,1]^n continuously by induction on proper face dimension. At each vertex choose its anchor. On higher-dimensional proper F, h is already defined on the boundary with values in f^{-1}(F), since lower faces are contained in F. Cone the boundary map to a_F inside its star-shaped preimage. Finally cone the entire boundary map into the ambient convex n-cube to define h on K. Then g=f composed h maps every face into itself. The straight-line homotopy from g to id_K preserves every face, including the boundary, so g restricted to boundary has topological degree one. If an interior point were omitted by g, radial projection from that point to the boundary would extend a degree-one boundary map over the ball, impossible (or by no-retraction). Hence g hits the interior; compactness hits its boundary too. As g(K) is included in f([0,1]^n), and the Bernstein expansion bounds that image inside K, equality follows. QED.

The finite certificate must check the downset property for ALL proper faces. Testing a grid of real behavior probabilities would NOT prove this theorem.

## Theorem B (four-dimensional actual set identity)

For this fixed double-collision tree, let f_LR:[0,1]^12 to R^4 and f_FULL:[0,1]^14 to R^4 be the actual z observers. Then

~~~text
f_LR([0,1]^12) = f_FULL([0,1]^14)
                = conv(f_LR({0,1}^12))
                = conv(f_FULL({0,1}^14)) = K,
affine_dimension(K) = 4.
~~~

In particular the *actual real* images of (eP,eQ,TP,TQ) coincide: no FULL-only observation exists in this model, even without a persistent LR random seed.

Exact finite proof: FACETS.txt contains 57 integer SUPPORTING halfspaces a.r+b.x+c.y+d.s <= bound. Forty-five are actual facets, twelve are valid auxiliary supports. VERIFY.cpp uses only signed integral arithmetic (__int128 for Cramer's rule). It enumerates all 4096 Boolean LR strategies and 16384 FULL strategies: exactly 272 versus 647 distinct integer z vectors. Five LR vectors (origin plus (0,20,40,20),(0,30,45,30),(0,30,72,0),(15,750,375,0)) give determinant -135000, proving dimension four.

Every LR and FULL Boolean point satisfies all 57 halfspaces. Exact NONNEGATIVE rational combinations of these rows bound their intersection H by 0<=r<=35; 0<=x,y<=1080; 0<=s<=50. The checker exhausts all C(57,4)=395010 hyperplane quadruples: 332443 nonsingular, 4371 feasible intersections, yielding 69 distinct integral vertices, ALL of them genuine LR Boolean observer vectors. Because H is bounded and full-dimensional, H is the convex hull of its vertices. Thus H equals conv(LR) and contains every FULL Boolean vector; since LR is included in FULL, the two convex hulls equal H=K. This argument independently certifies ALL signed support directions; no finite selection of cost directions is assumed complete.

For each of the 57 supporting rows, collect its optimizer Boolean LR policy masks, including masks with duplicate z. Close these sets under nonempty intersection; obtain exactly 438 distinct nonempty proper-face optimizer sets. A face of a polytope given by these supports is the intersection of all its active supports, so this is ALL proper faces. For a set M, each missing one-bit neighbor of a mask b forces the anchor bit to equal b's bit. The checker sees no conflicting forced bits and finds an actual anchor mask meeting all requirements for EVERY one of the 438 sets. Hence each face satisfies Theorem A's Boolean downset property. Consequently the actual seedless LR image is all K. As LR strategies are included in FULL and every FULL real observation is inside conv(FULL deterministic)=K by multi-affinity, the FULL actual image is K also. QED.

The integer supports were discovered by exploratory convex-hull computation but the final proof depends only on the 57 published integer rows and VERIFY.cpp's exhaustive exact checks; every claimed exact predicate is recomputed from first principles. No floating-point optimization is a dependency of the final proof. The actual executed console output is EXACT_OUTPUT.txt, ending PASS_EXACT_R5_RANK4_REAL_IMAGE_SURJECTIVITY.

## Scope-typed observer-factorization corollary

Because actual four-flow images agree as sets, for EVERY function G defined on K (including arbitrary nonlinear postprocessing or changed error readout coefficients) whose observation factors SOLELY through z=(r,x,y,s), the attainable G-image is equal in FULL and seedless LR. This is an observer-specific exact elimination certificate, NOT a claim that the original source-labelled histories or future operations are equivalent. In particular adding a genuinely independent path/source observer or changing the topology lies outside the corollary. Protect P000 and all BRC source, sign and path data until the exact future-observer factorization is proved.

## Reproduction, limits, next question

Run g++ -std=c++17 -O2 -Wall -Wextra VERIFY.cpp -o verify && ./verify FACETS.txt. The stdout actually obtained is preserved in EXACT_OUTPUT.txt. Finite enumeration proves the checkable finite hypotheses; topology+multi-affinity proves the quantifier over ALL real behavior. No formal Lean checker, independent reviewer, native Source Result, or external physical-model correspondence is claimed. NEXT_TASK.md fixes the next non-factorizing five-coordinate screen. Do not reopen this fixed model's semialgebraic nonmembership search; the mother problem of finding a DIFFERENT model with hull-equal but actual-image-unequal observers remains open.
