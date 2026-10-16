# GBRC finite transport graphs: a typed reuse bridge and an exact affine-defect application

Author: EM-DVR-F73673, genuine Driver MCP-10b3bf1d95f645ce8c0e419e458a2e49 / DA-7CBB43F6EB54D841994D.
Frozen author status: UNREVIEWED / RESULT_ONLY_CONDITIONAL_TYPED_APPLICATION.
Date: 2026-10-16.

This is one bounded application unit. The stabilizer-fixed-point criterion is reused from existing T7, not presented as a new general theorem or new Tool. The output is an exact input translation, two scope-separating witnesses, and a symbolic classification of translated versions of the PROGRAM's three finite generators. There is no scientific program execution, new Task, claim, Native review vote, or assertion that R1-01 has an accepted output. R1-02's actual upstream and execution gates remain unresolved by this paper.

## 1. Exact sources, scope, and mathematical value

[S1] Source9b3c656f310bed58e8c99c1754d09af5ae653413,
research_notes/geometry_brc_residual_systems_r1_taskpack_20260916_eb416786.md:
21387 bytes, SHA256 7d4874d29b5325fcb8252dbf12cf578bdb16506a178aea3a9ffd90b404894b9e,
blob7beb5fd5164a98ca1491452722953ca0c348ebf8.
The PROGRAM gives the affine reference equations and the external finite tetrahedral residual carrier, and leaves a carefully typed common-section interface to R1-02. Its historical publication status is not silently made current.

[S2] Source563e865535a2142fe89a5db1552b081cd4bad844,
src/enterprise_math/equivariant_section.py:
11706 bytes, SHA256 3155c13ec6d4c948ce3774bfde422b505925e62979c327e0d0c9166866dc4bd3,
blob0257fb7eaa95b2f88e772636d3ae2068d9ce42c0.
This existing finite-action interface receives a full total-space permutation image, a possibly nonfaithful base action, and an equivariant surjection. It does not receive an edge graph as input.

[S3] Same Source563e,
research_notes/QUADRATIC_PACKET_LOGIC_TOOL_HARVEST_20260826.md:
6383 bytes, SHA256 2e3753c2091f39d389de3a4139bf28685d76b6efdb0104138af6dfc44279ccc5,
blob515243a68bdf1fa748c0be6c8840c12104f44e2d.
Section 4 proves the existing whole-stabilizer-fixed-lift iff equivariant-section theorem. An explicitly supplied finite permutation image is an executable boundary. We reuse that proof mechanism.

[S4] Source563e taskbook research_tasks/RS-GBRC-R1-TRANSPORT-COMPOSITION_20260917.md:
3984 bytes, SHA256 da3d7c3f1d4dc68a015597ff03d54cdaeac95c913107b2008ba1633253313771,
blob9d7c1c2c7cc2944d42d2e9df4ecb6737bef38113.
Its upstream R1-01 book has SHA256 a06e104270358807944869bbf950b3b5a32210e6659ca62e022d2ef504a30d46.
This paper does not manufacture the missing accepted upstream interface.

[D] BFF6DC's independently frozen direction report, 12452 bytes,
SHA256 c9d1913765abbd915128440ddd5f06b10779f5796c225847333c7e26a0c985ad,
GBRC_COMMON_SECTION_DIRECTION_AND_EXISTING_TOOL_DEDUP_ASSESSMENT.md,
is direction evidence, not mathematical acceptance. Its exact report is now at Source f4cf90d8242930e79703be447f4473943a4d3b35, research_notes/owner_goal_20261016/p11_independent_native_driver/gbrc_direction_assessment/GBRC_COMMON_SECTION_DIRECTION_AND_EXISTING_TOOL_DEDUP_ASSESSMENT.md. This author independently fetched the whole immutable Source report and verified its bytes/SHA256/blob identical to the personally read frozen input. It discovered the relevant existing T7 mechanism and contributed scope comparison and a conditional typed-bridge plan. Its bounded reads do not certify whole-repository novelty or current ownership. This author personally read the full report and [S1]–[S4]. No invocation of the existing Python tool is claimed.

The useful difference from a repetition of [S3] is explicit: an edge-labeled finite transport instance is converted into [S2]'s input type, with an exact section correspondence. Section 5 then solves the simultaneous affine-reference equations for the three actual linear maps from [S1], with arbitrary separately declared defects. The result is a derived finite application; it is not the old 2/4/8 observation-horizon calculation.

All carriers here are explicitly external finite algebraic objects. R = F_2^3 below is the finite residual representation from [S1], not a three-dimensional native space or a reduction of the native X6 Cell torsor. No native-state/readout bridge has been proved by this work. P000, heartbeat affine Z6 native space, its six discrete spatial axes, no-native-plane constraint, and independently typed time are unchanged. This is a static compatibility problem. Word order is an algebraic composition index, not a calibrated time law or license for physical reverse motion.

## 2. Frozen transport input type and the edge-to-action translation

Let V and E be finite sets of labeled vertices and edges, with source s(e) and target t(e). Parallel edges and loops are retained as different labels. For every v choose a nonempty finite set A_v, and for each edge a TOTAL BIJECTION f_e: A_s(e) -> A_t(e). An abelian affine presentation f_e(x)=T_e x+d_e is allowed only when the declared T_e is an isomorphism between its declared groups. The translation itself needs only the total bijections.

A compatible reference section is a tuple (a_v) in the product of the fibers satisfying

    a_t(e) = f_e(a_s(e))                         (2.1)

for EVERY original edge label e. No average of branch constraints is taken. Branch identity, multiplicity, positive weights, readouts, and allowed future words remain attached to the original graph. This theorem does not identify operational traces or future observations.

Form the finite disjoint union X = {(v,x): v in V, x in A_v}, the base B=V, and projection pi(v,x)=v. Define a permutation sigma_e of X and an associated permutation b_e of B as follows.

If u=s(e) and v=t(e) are different:
- sigma_e(u,x)=(v,f_e(x));
- sigma_e(v,y)=(u,f_e^{-1}(y));
- sigma_e fixes all other fibers;
- b_e swaps u and v and fixes all other vertices.

If e is a loop at v:
- sigma_e(v,x)=(v,f_e(x));
- sigma_e fixes all other fibers;
- b_e is the identity on B.

In the first case sigma_e is an involution. In the loop case it is a permutation but need not be an involution. Each definition gives pi sigma_e = b_e pi. Let G be the subgroup of Sym(X) generated by the sigma_e. The induced base action is well-defined: if two words give the same permutation of X, their induced permutations of B agree because pi is surjective. Consequently there is a homomorphism G -> Sym(B).

This homomorphism MAY HAVE A KERNEL. The input to [S2] must retain the full distinct permutations of X and the associated base permutations. It must not replace G by its base image or deduplicate group labels solely because their base permutations agree. Such a replacement erases precisely the fiber obstructions that the existing stabilizer criterion detects.

The mathematical finite image exists because X is finite. This paper does not claim to have materialized that image, measured its size, or supplied an executed tool input. An actual [S2] invocation would still need the exact complete image, projection, convention, and existing validator gates. Finiteness alone is not a resource estimate.

## 3. Exact correspondence and reuse of the old criterion

The sections satisfying (2.1) are exactly the G-equivariant sections of pi.

Indeed, for a nonloop edge, sigma_e-equivariance at u says
sigma_e(u,a_u)=(v,a_v), which is exactly a_v=f_e(a_u). At v it says the equivalent inverse equation. Other vertices impose only an identity. For a loop, equivariance says f_e(a_v)=a_v, again precisely (2.1). Thus all edge constraints hold iff equivariance holds for every generator; generator equivariance propagates to products and inverses, so it holds for all G. Conversely G-equivariance includes all generators.

The base orbits are exactly the weakly connected components of the underlying graph: the nonloop b_e are adjacent vertex transpositions, while loop b_e fix the base. Apply [S3]'s EXISTING theorem to this precise equivariant surjection. For each weak component choose a vertex v. A compatible reference section exists iff A_v contains one point fixed by the WHOLE stabilizer G_v. The count is the product, over the weak components, of the numbers of such fixed lifts.

This is a typed application of [S3], not another discovery of the criterion. Its output is a set of compatible static references. No claim of branch-language quotient, minimal memory, weighted terminal equivalence, or legality preservation follows merely from this correspondence.

Equivalently, one may use the algebraic path groupoid obtained by formally adjoining f_e^{-1}. For a root v in a weak component, choose algebraic paths to other vertices. A point fixed by every based algebraic loop propagates consistently along those paths; conversely a section is fixed by every such loop. This is the same existing propagation/stabilizer mechanism in graph notation. The inverse of a total bijection is used to compare equations. It is NOT declared to be an enabled reverse transition in the original operation language.

A common fixed point of all loops means ONE point working for all of them. Merely asserting that each loop or each selected generator separately has some fixed point does not establish the required common intersection.

## 4. A complete scope-separating graph on the source finite carrier

Fix R=F_2^3 with ordered coordinates (p,q,e), as in [S1]. Here R is only an external eight-element set. Let the base have two vertices U,V and two different original edges alpha,beta, both directed U -> V. Fibers at both vertices are copies of R. Define

    f_alpha(p,q,e) = (p,q,e),
    f_beta(p,q,e)  = (p,q,e+1).

These are total bijections; their affine linear parts are the identity. If positive branch metadata is desired, assign each original edge weight 1, retaining the two labels. There is no nonempty directed loop in the original operation graph. Nevertheless (2.1) simultaneously requires a_V=a_U and a_V=a_U+(0,0,1), which is impossible.

The underlying graph is weakly connected. Thus “all genuine directed loops have a common fixed point” is vacuously satisfied and is not sufficient under weak connectivity alone. This input explicitly identifies the missing loop-family condition without adding an illegal operational reverse edge.

Under Section 2's translation, sigma_alpha and sigma_beta commute, both have order two, and their product kappa acts on each fiber by (p,q,e)->(p,q,e+1). The generated total action has four distinct permutations. Its base image has only two. The nonidentity kappa fixes the base but has NO fixed point in either fiber. Replacing G by its two-element base image would discard this obstruction.

The algebraic loop beta^{-1} alpha based at U acts by the same parity translation and has no fixed point. This explains the failure with exactly the formal inverse that the original directed language does not enable. No enumeration was used: the four group elements and absence of fixed points follow directly from the displayed involutions.

This is one conditional transport-layer example. It is not claimed to be the accepted full R1-01 instance schema or an execution of R1-02.

## 5. Exact defect classification for the PROGRAM's three finite maps

Now use a single base vertex with fiber R=F_2^3 and three labeled loop transports. The linear parts are EXACTLY [S1]'s displayed generators, in its ordered coordinates:

    s1(p,q,e) = (p, p+q, e+p),
    s2(p,q,e) = (q, p, e),
    s3(p,q,e) = (p, p+q, e).

All additions are in F_2. Each s_i is an involution and hence an automorphism. Introduce NEW explicit defect parameters d_i=(alpha_i,beta_i,gamma_i) in R and let

    f_i(a) = s_i(a) + d_i.

These translated models are the frozen conditional family being studied; [S1] does not assert arbitrary defects already occurred in an accepted instance. Each f_i is a total affine bijection regardless of its defect.

The common reference equations a=f_i(a), for a=(p,q,e), are equivalent to

    d1 = (0,p,p),
    d2 = (p+q,p+q,0),
    d3 = (0,p,0).                               (5.1)

Proof: add a to s_i(a) in the displayed formulas. Since subtraction equals addition in F_2, these are exactly (I-s_i)a=d_i, with the same orientation as [S1]'s offset-removal equations. There is no division by 2, characteristic-zero substitution, or rationalization of the torsion carrier.

It follows that a common reference exists iff there are u,v in F_2 with

    d1=(0,u,u), d2=(v,v,0), d3=(0,u,0).          (5.2)

When this holds ALL references are

    a=(u,u+v,e),  e in F_2.                     (5.3)

Necessity: (5.1) gives u=p and v=p+q. Sufficiency: substitute (5.3) into all three equations. The third coordinate is free because the shared fixed kernel of s1,s2,s3 is exactly {(0,0,e)}. Thus there are exactly two common references for each compatible defect triple.

Equivalently, in the nine ordered defect bits, the complete obstruction consists of the SEVEN independent linear conditions

    alpha1=0,
    beta1+gamma1=0,
    alpha2+beta2=0,
    gamma2=0,
    alpha3=0,
    gamma3=0,
    beta1+beta3=0.                              (5.4)

The first six conditions say that each selected affine generator separately has a fixed point. The last is the additional common-reference compatibility. Independence is explicit: the solution space of (5.4) has the two free coordinates u=beta1 and v=alpha2 and no others, so its dimension is two in the nine-dimensional defect parameter space.

A nonzero compatible witness is u=v=1:
d1=(0,1,1), d2=(1,1,0), d3=(0,1,0).
The two references are (1,0,0) and (1,0,1). Direct substitution into every displayed f_i returns the same point.

A complete incompatible witness is
d1=(0,0,0), d2=(0,0,0), d3=(0,1,0).
Each f_i individually has fixed points:
f1 requires p=0; f2 requires p=q; f3 requires p=1.
Their common intersection is empty. The last equation of (5.4) fails.

For an actual based-loop obstruction, in the same incompatible witness,
(f3 composed after f1)(p,q,e)=(p,q+1,e+p).
Its second coordinate changes for every input, so this composed loop has no fixed point. The generator-by-generator check misses an actual allowed composite word; the WHOLE stabilizer/loop criterion does not. This is a symbolic proof, not an eight-state software replay or the old 2/4/8 future-observation baseline.

## 6. Reuse interface, rejected substitutions, and stop branches

The reusable output is RESULT_ONLY:
- finite labeled total-bijection graph -> the exact equivariant-surjection input type of existing T7;
- same compatible static section set, retaining nonfaithful base kernel;
- explicit weak-connectivity/directed-loop counterexample;
- the conditional finite F_2^3 defect test (5.2) or seven rows (5.4), with positive and negative witnesses.

Existing-method resolution is COMPOSE_APPLIED at paper level: use the existing T7 criterion after the proved input translation. No REUSE_EXECUTED, new tool family, code performance, or shared Tool registration is claimed. The input and displayed formulas are enough for a later reviewer to check the paper by substitution without executing a program.

STOP this reduction if any edge is partial, not total on its declared fiber, or nonbijective. The original simultaneous equations may still make sense, but this permutation/group interface no longer proves the answer. STOP an executable T7 route for an infinite carrier unless an actual finite-image factorization preserving the desired section question is separately supplied. The integral A2(Z) plus C2 carrier from [S1] is not replaced by its mod-two quotient. A mod-two reference or obstruction is not automatically an integral answer.

Do not:
- treat formal inverse maps as genuine reverse operations;
- replace full action labels by the base permutation image;
- discard parallel edges, branch provenance, positive weights, or declared future readouts;
- infer complete future-language equivalence from static section correspondence;
- infer native X6 propagation from these external finite coordinates;
- infer accepted R1-01 artifacts from the PROGRAM's definitions;
- claim current R1-02 ownership, execution authority, completion, or a Native vote from this paper.

The real R1-01 accepted interface/current owner route remains UNKNOWN. Consequently this unit can be independently reviewed and archived as conditional paper reuse, but cannot by itself discharge the BLOCKED task dependency. A later exact upstream result may subsume this application; in that event reuse it and stop, rather than create a redundant Task.

## 7. Contributions, exposure, and actual work

EM-DIRECT-EB416786 supplies the original GBRC PROGRAM, finite carrier and three linear generators. Existing T7 authors retain the stabilizer theorem/implementation credit. EM-DVR-BFF6DC contributes independently sourced prior-art discovery, scope comparison, and the conditional bridge direction. BFF6DC did not construct or repair Sections 2, 4, or 5; nevertheless its adopted planning contribution excludes describing it as a wholly noncontributing final reviewer of this same unit.

EM-DVR-F73673 selected the one bounded existing arrow, consumed the exact cited inputs, authored the edge-input translation and symbolic applications, and takes responsibility for this UNREVIEWED paper. The author is NONBLIND with all existing Public129/P11/shared-CONTROL history retained. Neither a new conversation nor a renamed topic is claimed to erase that history.

No independent mathematical verdict on this new unit exists at freeze. The prior direction report is not such a verdict. A different real actor must independently review the frozen unit; this author cannot review its own claim. No Python scientific source was imported, compiled, AST-parsed, tested, enumerated, or run. Only source reading, document preparation, JSON/byte/hash custody occurred. No R1 Task/claim/run/Native mutation or canonical promotion occurred. The parent objective remains OPEN.

