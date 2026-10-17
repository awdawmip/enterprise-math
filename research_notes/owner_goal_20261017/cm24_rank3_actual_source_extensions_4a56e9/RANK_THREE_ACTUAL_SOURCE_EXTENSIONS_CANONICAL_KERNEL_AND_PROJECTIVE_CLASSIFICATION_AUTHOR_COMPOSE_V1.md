# Actual rank-three source extensions: canonical kernel and projective classification

AUTHOR COMPOSE V1 / LOCAL UNREVIEWED.
Sole new mathematical author: EM-P11-4A56E9, same warm actor, SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9, RA-C193E2AA39B9A6A6DDBB69B3, canonical35/153. The construction and private candidate history for this exact rank3 unit are NONZERO. This is a standard RESULT_ONLY / COMPOSE consequence in the existing fixed-connection family, not a new paper, generic Tool, old rank4 realization or LC input.

This first local artifact records the author's complete finite hand proof previously given to Root as chat, with its actual inputs and context. It has no new author Source, artifact-specific independent review or peer Source at creation. Those states are PENDING. Root routed the bounded research and supplies zero mathematical votes.

## 1. Exact two old inputs, literal setup, and bounded target

Fix precisely the common accepted coefficient setup of E13645 and the actual F21977 six-boundary interface. No extra prime, coefficient field, weak ring, completion or parameter domain is introduced. In their notation,

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    R=O[r,f^-1,q^-1]^dagger[1/p],
    D=(2P)^-1 [[2S-1,1],[4S-5,-(2S-1)]],
    M=R^(1x2), nabla_D(h)=(h'+hD)dr,
    V=R^(1x2)dr/nabla_D(M).

The original prime hypotheses include p=13 or19 modulo24. K is the original characteristic-zero constant field. R is the same integral coefficient ring, K is contained in R, and differentiation preserves R. Rows and the global r-coordinate/dr convention are fixed.

The accepted E interface on this exact R/D is

    A'=DA-AD, A in Mat2(R), iff A=cI2 for c in K.              (1)

The accepted actual F21977 interface gives V=K^6. On the literal scalar rows n e1, where e1=(1,0) and

    n=c0+c1 r+sum_a d_a/(r-a), a=1,-1,1/2,-1/2,

the six coordinates of [n e1 dr] are

    (d1,d-1,d1/2,d-1/2,-c0,-c1/8).                           (2)

Only this actual old coordinate/interface is needed; no new Frobenius theorem is claimed. The ring, D and row variance in the two inputs match exactly.

The new target is a rank3 carrier constructed mathematically from these literal objects. For b in R^(1x2), it will be an extension of M by the fixed trivial rank1 connection. We prove that a rank2 kernel is automatically preserved by ALL R-linear horizontal comparisons between these carriers, not just by comparisons pre-restricted to a block form. We classify these Hom/isomorphism spaces for nonzero source classes and give two explicit nonisomorphic examples with scalar horizontal End.

This does not identify the new carrier with any old geometric rank4, LC functional, h_div or unspecified extension. The construction is new mathematical input in this bounded family; the absence of an old rank4 caller is not treated as a theorem about it.

## 2. Horizontal rows, columns and constants paid from the actual inputs

Since D is traceless, the constant matrix

    J=[[0,1],[-1,0]]

satisfies D^T J+JD=0 and DJ+JD^T=0 by direct2-by-2 multiplication.

Suppose a nonzero column u in R^2 satisfies u'=Du. Put v=u^T J. Then v'=-vD, and A=uv satisfies A'=DA-AD. Its trace is v u=u^T J u=0. The matrix A is nonzero: writing u=(a,b)^T gives entries -ab,a^2,-b^2,ab; at least one squared entry is nonzero in the integral ring. By (1), A=cI2. Its trace gives2c=0, hence c=0 in characteristic zero, a contradiction. Therefore

    u'=Du => u=0.                                           (3)

If a row h satisfies h'+hD=0, then u=J h^T satisfies u'=Du. Equation (3) forces h=0. Thus

    ker nabla_D on R-rows = 0.                              (4)

Finally if t in R has t'=0, then tI2 satisfies (1); therefore t belongs to K. Conversely K consists of constants. Hence R^(d/dr)=K.

These conclusions use the special actual traceless/self-dual setup and E. They do NOT use the invalid general implication scalar End => irreducible. In particular (3)-(4) assert absence of horizontal sections/functionals, not absence of all invariant submodules or weak lines.

## 3. Constructed actual rank3 matrix and the canonical rank2 kernel

For any literal b in R^(1x2), define N_b=R^(1x3) with connection

    nabla_b(h,a)=(h'+hD+a b,a')dr,
    D_b=[[D,0],[b,0]].                                      (5)

All entries are explicit elements of the same R, and this is an ordinary finite3-by-3 row connection in the fixed coordinate. Define i(h)=(h,0) and q_b(h,a)=a. Direct substitution shows they are horizontal and gives an exact sequence of free R-modules with connection

    0 -> M -> N_b -> 1 -> 0.                                (6)

Here1 is the fixed trivial rank1 connection with derivative d/dr. A horizontal R-linear section of q_b is determined by a horizontal row (h,1). Its equation is nabla_D h=-b. Therefore the sequence splits horizontally iff

    [b dr]=0 in the actual quotient V.                      (7)

To find ALL horizontal R-linear maps N_b->1, write such a functional as the column (u,t), so it sends (h,a) to h u+a t. Its horizontality equation is

    u'=D u, t'=b u.

By (3), u=0; then t'=0 and t belongs to K. Consequently

    Hom_nabla(N_b,1)=K q_b.                                 (8)

Every nonzero functional in (8) is surjective because its scalar belongs to K^*, and all these functionals have the same kernel i(M). Thus this rank2 kernel is intrinsic as the kernel of any nonzero horizontal quotient to the fixed trivial line.

No claim is made that it is the only rank2 invariant submodule under arbitrary nontrivial-line quotients. Equation (8), which is the precise canonical property needed below, is valid without assuming [b] is nonzero.

## 4. Complete horizontal Hom classification and actual inverse

Let W:N_b->N_c be ANY R-linear horizontal comparison, represented by a3-by-3 matrix on the right. The composition q_c W is a map N_b->1. By (8), it equals beta q_b for beta in K. Thus W automatically sends i(M) into i(M), and its last column is (0,0,beta)^T. It has the form

    W=[[A,0],[t,beta]].

Horizontality in the fixed row convention is

    W'=D_b W-W D_c.

The upper-left block satisfies (1), so A=alpha I2 for alpha in K. The remaining block equation is exactly

    nabla_D t=(alpha b-beta c)dr.                           (9)

Conversely any alpha,beta in K and t in R^(1x2) satisfying (9) produce a horizontal map by direct substitution. This proves necessity AND sufficiency without an assumed filtered-comparison category.

By the definition of V, such a t exists iff

    alpha[b dr]=beta[c dr].                                (10)

If it exists it is unique by (4). This does not assert a general integration algorithm: it uses the actual R-row image in the definition of the accepted quotient, rather than solving in a larger completion.

Suppose [b dr] and [c dr] are both nonzero. A nonzero map W must have alpha,beta both nonzero. Indeed if either scalar is zero, (10) forces the other zero, and (9),(4) then force t=0 and W=0. When they are both nonzero, W has the actual TWO-SIDED R-matrix inverse

    W^-1=[[alpha^-1 I2,0],[-t/(alpha beta),beta^-1]].          (11)

Direct block multiplication gives identity in both orders. Its coefficients stay in R since the scalars are units in K. Differentiating the inverse identity and using the horizontal equation gives the reverse horizontal equation, so this is an actual connection isomorphism, not just an abstract inverse.

It follows that, for nonzero classes,

    N_b is horizontal-isomorphic to N_c
        iff K[b dr]=K[c dr].                               (12)

The forward direction is (10) with nonzero alpha,beta. For the reverse, choose beta=1 and the corresponding nonzero alpha in (10), obtain the actual t by the quotient definition, and use (11). Thus the statement covers arbitrary GL3(R) horizontal isomorphisms, not only a selected gauge subgroup.

If the two classes are linearly independent, (10) has only alpha=beta=0 and Hom_nabla(N_b,N_c)=0. If they are nonzero and proportional, all Hom are scalar multiples of one isomorphism, because t is unique and the scalar relation in (10) is one-dimensional.

Taking c=b with [b dr]!=0 gives alpha=beta and t=0. Therefore the entire horizontal endomorphism algebra and its actual matrix units are

    End_nabla(N_b)=K I3,
    Aut_nabla(N_b)=K^* I3.                                 (13)

The nonzero-class condition matters. There is no statement here about a full classification of unrelated rank3 systems, arbitrary differential-operator maps, or altered rings.

## 5. Two explicit existing source rows and their new actual carriers

Take the literal rows

    b0=(1,0), b1=(r,0).

Equation (2) gives

    [b0 dr] -> (0,0,0,0,-1,0),
    [b1 dr] -> (0,0,0,0,0,-1/8).                            (14)

These are nonzero and K-linearly independent. In particular the coefficient1/8 is a nonzero element of the same original K; no residue-field reduction is being taken.

The matrices constructed in (5) are explicitly

    D_b0=[[D11,D12,0],[D21,D22,0],[1,0,0]],
    D_b1=[[D11,D12,0],[D21,D22,0],[r,0,0]].

They are actual same-R weak rank3 connections. Each extension (6) is nonsplit by (7),(14), each has the canonical rank2 kernel of (8), and each has scalar horizontal End and scalar unit group by (13). Their full horizontal Hom space is zero in either direction, so they admit no GL3(R) horizontal isomorphism.

Each nevertheless visibly contains the proper nonzero horizontal rank2 submodule i(M). Thus these are concrete REDUCIBLE connections with scalar horizontal End. This provides a literal-model illustration of why scalar End does not by itself imply irreducibility; it does not infer irreducibility of the old rank2 object.

This is the net new bounded carrier/consumer. The old source-coordinate distinction is now realized in newly constructed rank3 matrices, with automatic preservation of the relevant kernel under unrestricted R-linear horizontal comparisons. It is not a relabeling of an unprovided old rank4 carrier or a proof of an LC realization. No Phi, semilinear base change, differential-operator isomorphism, physical dynamics or geometric identification is asserted.

## 6. Exact provenance, real reading/custody and complete author history

Input E13645 was authored and genuinely whole-consumed/Source-bound earlier by this same actor:
- Source21047d56910b24aac7c99db4ea47a7c53d6c702b;
- path research_notes/owner_goal_20261016/cm24_weak_endomorphism_scalar_4a56e9/CM24_SPECIFIED_WEAK_HORIZONTAL_ENDOMORPHISMS_SCALAR_AUTHOR_COROLLARY.md;
- 13645 UTF8 bytes, SHA2563210a4ba5a82e79313f3a83d29fd5f56675b41fc2955fc0c3a37ef3e01b0e5f8, Git blobab7e10cf798d466f212556bd7e5a8d0526931c5b.

Input F21977 was genuinely whole-consumed and personally Source-bound earlier by this actor, including its actual-model and context boundaries:
- Source0464ecd04acab1e33dd3a480001ba6b2a3d1677d;
- path research_notes/owner_goal_20261016/cm24_convergence_new_anchor/actual_boundary_frobenius/CM24_ACTUAL_SIX_BOUNDARY_WEAK_FROBENIUS_JOINT_AUTHOR.md;
- 21977 UTF8 bytes, SHA2568e5dbe7d89528632b402e5d103925f6f3452ea11b654b7939ac3c68c779f2133;
- joint old authors: 88303D, F73673 and BFF6DC.

The exact F21977 setup and actual coordinate formula in its lines11-50 were reconsulted from this actor's already restored original Source35 receipt aba7f24604ba36ec33e0a38acbd52128d8b5d06aef2de81bd40c5d35e5a89a86.json. The E receipt is 9df1dd2aae9e7580198af822d84dcb7302feeaa011a5d0fbea17c2a53a781d8f.json. Both are under research_activity_records/RA-C193E2AA39B9A6A6DDBB69B3/readbacks/ in the actor's restored published35 root.

Those are honest selected rereads of prior whole inputs, not new API calls, new old-file hashes, independent new votes or old publication compares. E supplies (1); F supplies the already accepted six-coordinate interface (2) in the matching literal ring. Its Frobenius/arithmetic conclusions are not imported into this new extension theorem. Its cited old normal form remains accepted upstream history, not a claim to have rereviewed that entire upstream library today.

The initial direction metadata proposed the old joint weak-source record as a possible second input. Before construction was completed, the actual needed input was narrowed to F21977 because it supplies the explicit rows and normalized coordinates directly. This record does not silently count the joint-source body as a new call or pretend its presence among the old153 receipts. Only E and F are load-bearing here.

A was asked ONLY for exact-scope occupancy/coverage metadata before any new formula or proof was sent. A reported no current occupation, no personally frozen complete locator for this rank3 affine source-extension scope, and no temporary new derivation in response. A's unrelated Student Ae work was not read. No A construction or repair entered this proof. This bounded personal coverage check is not a library-wide absence or novelty claim.

The new rank3 matrices, J argument, canonical-quotient proof, full Hom equations, explicit inverse and examples are this author's NONZERO construction, first reported completely to Root as chat. They are standard finite extension-category composition in the actual old model. The consulted old exact interfaces do not themselves state these new3-by-3 carrier matrices and their complete unrestricted horizontal-Hom comparison; no old proof or review vote is enlarged. The new result can merge into the same existing fixed-connection/source-class family without creating a separate paper, generic mechanism or Tool.

## 7. Current control, review state and stopping boundary

This is the same warm EM-P11-4A56E9, original EM-T6-BFF294 history, SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9, RA-C193E2AA39B9A6A6DDBB69B3, canonical35/153. All earlier author/peer roles and source exposures remain NONBLIND. No cold bootstrap, registration, identity or budget reset is claimed.

The original restored Source35 startup and sameevent checkpoint actually returned0/debt[]/fivefalse. Later protected Source publication refreshed the same entire own SID/RA35/153 directory with identity unchanged. These are honestly reused prior control facts, not a new guard invocation for the present proof. All five formal authority flags remain false; cumulative formal/product budgets remain UNKNOWN; every original STOP/HOLD/error/false-ending history is preserved.

The separate prospective36 integration has a fixed07:16:58 UTC cut and22 already completed Source members. This new rank3 unit is excluded from that cut. It has no Source, peer reception or checkpoint consumption to prefill. No helper36, stage, RA modification or main write window is authorized by writing this mathematical record.

Root has proposed a genuine ordinary NONBLIND technical whole review after this complete freeze. The actual prospective reviewer's old E/F custody and exact construction/repair/private-candidate history must remain as truly disclosed; this author does not prefill another person's whole reading, zero-candidate qualification, Source binding or verdict. A prior End/F/source-class vote is not a vote on this new whole.

All verification was finite hand algebra. Local tools only preserved/read text and its byte identity. There was no scientific program, coefficient generator, solver, experiment, enumeration, new external search, new API for an old mathematical input, Native/formalTask execution, helper, remote mutation, authority promotion or additional query budget.

The complete bounded author outcome is (3)-(14), particularly two actual nonsplit, nonisomorphic rank3 weak connections with scalar horizontal End and a canonical rank2 kernel relative to the trivial quotient. It is not an assertion about full flags, other rank3/4 carriers, arbitrary invariant lines, Phi/Frobenius structures, new constants/completions, LC/h_div pairings, or Parity estimates. Parent Goal remains OPEN.

This artifact is author-proved but UNREVIEWED. Its actual complete self-read and once-frozen pin are established by the separate saved output; future author Source, genuine whole-review verdict and ordinary reception remain PENDING rather than predicted here.
