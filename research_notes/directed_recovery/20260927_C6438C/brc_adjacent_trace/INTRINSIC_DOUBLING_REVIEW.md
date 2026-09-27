# Review: intrinsic doubling versus normal defect

Status: PASS_PURE_SYMBOLIC_REVIEW / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

Reviewed in full: INTRINSIC_DOUBLING_AND_NORMAL_DEFECT.md, SHA-256 bb84d2d716fae955a5a32adeba4f597d2bf0dd6d12721e04d16dc9b169607e47. The review concerns its algebra, geometric domain and interpretation. No native program, numerical reference, character evaluation or parameter search was run. The frozen source and results were not changed.

## Split chart and descent

The assumptions that 2 and Delta=k^2-4 are units are sufficient. The quadratic algebra S=R[lambda]/(lambda^2-k*lambda+1) is finite free of rank two, faithfully flat, and etale: lambda is a unit and (2lambda-k)^2=Delta. Thus lambda-lambda^-1 is a unit in S. This construction works over rings with nilpotents as well as over fields; it does not require the program to find a square root in R.

The proposed coordinate inverses have product (kvw-v^2-w^2)/Delta=1 on the conic. They really produce mutually inverse maps between the split conic and G_m, rather than merely a parameterization of some points. The involution lambda -> lambda^-1 exchanges z and z^-1, so the chart descends to the norm-one torus. The identity z=1 corresponds to (2,k). The smoothness argument is also valid: the two partial derivatives generate the unit ideal on the conic, since their simultaneous vanishing would force v=w=0 and then contradict unit Delta.

Direct substitution yields D0(z)=z^2 and D1(z)=lambda*z^2 with the stated orientation. The latter is translation by the fixed torus point represented by lambda after doubling; it is not a homomorphism fixing the identity. Both operations nevertheless descend, because conjugating lambda and z replaces each resulting parameter by its inverse.

For an explicit split-ring check, on the target coordinate t the square map is described by adjoining z with z^2=t. Its algebra is free of rank two and z is a unit; the derivative 2z is a unit. Hence it is finite etale of degree two. The translated map differs by an isomorphism. This is the standard Kummer argument; the reviewer actually read the relevant proof of Lemma 59.28.1 in [Stacks, Kummer theory](https://stacks.math.columbia.edu/tag/03PK). The descent step is supported by the actually read statements and proofs in [Stacks, properties local in the fpqc topology](https://stacks.math.columbia.edu/tag/02YJ), specifically current Lemmas 35.23.25, 35.23.31 and 35.23.32 for finite, etale and finite locally free of fixed degree. Only those relevant portions were used, not a claimed full literature review or a new professional-query job.

The conclusion is a geometric degree-two cover everywhere on this admitted smooth conic. It is not surjectivity on rational points of a particular finite field and supplies no rational root-selection procedure. The source's phrase about zero or two rational predecessors is read in its finite-field setting; it must not be generalized to arbitrary disconnected residue rings, whose componentwise choices can give more rational preimages.

## Tangential differential and normal direction

With k fixed, dF=(2v-kw)dv+(2w-kv)dw. Therefore the two local expressions for omega agree wherever both are defined. The derivative opens cover the smooth conic, so they glue to a nowhere-zero relative differential. In the split chart,

    dv=(z-z^-1) dz/z,
    2w-kv=(lambda-lambda^-1)(z-z^-1),

and the globally regular expression is omega=(lambda-lambda^-1)^-1 dz/z. This cancellation identifies a differential in the coordinate algebra; it does not ask the native program to divide by a possibly nonunit z-z^-1 at a particular point. Both pullbacks are exactly 2omega because lambda is constant over the base. Thus neither v nor w appears in the intrinsic tangent multiplier.

The two ambient identities F o D0=v^2 F and F o D1=w^2 F are compatible with that result. They induce multipliers v^2 and w^2 on the pullback conormal line (F)/(F^2). The ambient determinants 2v^2 and 2w^2 include that normal behavior as well as the invertible tangent factor 2. At v=0 on the conic, w is a unit; the ambient D0 derivative still acts nontrivially on the conic tangent, as shown in the source. The analogous statement holds for D1 at w=0. No intrinsic singularity or ramification follows from the vanishing ambient determinant at those points.

This also preserves the earlier defect warning. An off-conic history can lose its defect when a normal multiplier is a zero divisor. A terminal zero residual therefore remains insufficient to certify a whole prior orbit. Conversely, such normal loss cannot be cited as information loss of the admitted intrinsic etale orbit itself.

## Research and execution boundary

The theorem correctly separates three languages: reversible one-step torus translation, the two nonlinear degree-two bit maps, and ambient residual propagation. It complements DOUBLING_COVER_CHARACTER.md: the local square class determines rational lifting, whereas the geometric cover alone neither supplies the roots nor resolves unknown odd-order components. Repeated character observations require their own information and cost analysis.

No correction is needed within the stated domain. The elementary chart identities are checked here; the standard finite-etale and descent facts have the precise primary support above. This is a symbolic clarification of the existing HBW interface, not a new native operation, an executed defect observer, a physical-attribution claim, an efficiency result or a general factoring theorem.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1.
