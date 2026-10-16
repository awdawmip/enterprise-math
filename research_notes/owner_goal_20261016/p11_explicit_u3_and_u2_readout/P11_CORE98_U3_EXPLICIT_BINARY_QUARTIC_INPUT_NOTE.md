# A fixed explicit binary-quartic input for U3 at core (9,8)

FROZEN UNREVIEWED SAME-FAMILY INPUT NOTE. Author EM-DVR-F73673, actual Driver SID MCP-10b3bf1d95f645ce8c0e419e458a2e49 / DA-7CBB43F6EB54D841994D. No program, parameter search, local enumeration or consumer has run. This is an exact change of a known two-cover model, not the missing four-Selmer lift, a new point, actual mixed value or another independent discovery. Prior PASS reports do not review the new explicit algebra; a genuine different nonauthor must assess it. All classical curves retain external types under Heartbeat X6. The fixed233 STOP/NO_INVOKE and every old Task remain unchanged.

## 1. Retained input and the explicit new model

Keep P=161,Q=127,S=P^2+Q^2=42050,D=P^2-Q^2=9792 and

    E: y^2=x(x-P^2)(x-Q^2).

The sixth full Selmer proof, Source4090e063926e770103afc4628ea40c8a8949cedb, supplies the actual full two-Selmer class U3=(1,3,3). Its retained two-cover is

    C: s1^2-3s2^2=P^2*t^2,
       s1^2-3s3^2=Q^2*t^2,

with homogeneous coordinates [s1:s2:s3:t]. The complete map to the projective Weierstrass model of E is

    [X:Y:Z_E]=[s1^2*t : 3s1*s2*s3 : t^3].

This exact ordered-root covering convention is also retained in the mixed-bit paper Sourcea29ad230bfd4a94e305b9cdb4d3b046d7dcb88e6. It is the proof input, not a new claim of local computation.

Define the weighted-projective binary-quartic curve Q3, with weights (1,1,2) on [Z:W:R], by

    R^2 = 3Z^4+2S*Z^2*W^2+(D^2/3)*W^4
        = 3Z^4+84100Z^2W^2+31961088W^4
        = (Z^2+27648W^2)(3Z^2+1156W^2).

All coefficients are exact rational integers for this fixed input. No general parameter claim is hidden in the fractions: the symbolic proof below is valid for rational nonzero P,Q with P^2!=Q^2, while these displayed integer coefficients are the fixed P=161,Q=127 specialization.

## 2. The explicit map has no base point and satisfies both quadrics

Define G:Q3->C by

    [s1:s2:s3:t]=[3R : 3Z^2-DW^2 : -3Z^2-DW^2 : 6ZW].

Every entry has weighted degree two. If both middle entries were zero, their sum gives -2DW^2=0 and their difference gives6Z^2=0. Since D is nonzero, this would force Z=W=0, and then the quartic forces R=0, which is not a projective point. Hence these formulas have no common zero, including at Z=0 or W=0.

Using the quartic identity gives

    (3R)^2-3(3Z^2-DW^2)^2
        =18(S+D)Z^2W^2=36P^2Z^2W^2=P^2(6ZW)^2,
    (3R)^2-3(-3Z^2-DW^2)^2
        =18(S-D)Z^2W^2=36Q^2Z^2W^2=Q^2(6ZW)^2.

Thus G is an everywhere-defined morphism into the precise retained C. On the open ZW!=0, putting W=1 gives the inverse affine coordinates

    s1/t = R/(2Z),
    s2/t = (Z-D/(3Z))/2,
    s3/t = (-Z-D/(3Z))/2.

Conversely on C away from s2-s3=0 and t=0 the weighted inverse is

    [Z:W:R]=[s2-s3 : t : 2s1(s2-s3)].

Indeed subtracting the two quadrics gives

    (s2-s3)(s2+s3)=-(D/3)*t^2,

which verifies the inverse formulas and the quartic equation. These inverse expressions are birational charts, not an assertion that the displayed inverse formula has no base point at every geometric point. The global direction G has already been checked at all points.

The binary quartic is separable: its two quadratic factors have nonzero constant coefficients, each has distinct roots in characteristic zero, and they share no root since 3*27648=82944!=1156. Thus its smooth weighted-projective model is a smooth genus-one curve. The retained C is likewise smooth genus one. A birational morphism between these smooth projective curves is an isomorphism. Consequently the charts extend uniquely across the missing finite sets; no points over Qp with sqrt3, or real boundary points, are discarded merely because an affine expression uses Z in its denominator.

## 3. A complete covering map to the exact target E

Composing G with the retained map C->E, and cancelling a global nonzero constant9, gives

    [X:Y:Z_E]=
      [6R^2*ZW : R(D^2W^4-9Z^4) : 24Z^3W^3].

All entries have weighted degree six. On ZW!=0 this is

    x=R^2/(4Z^2W^2),
    y=R(D^2W^4-9Z^4)/(24Z^3W^3).

At Z=0 the quartic forces R nonzero, so the middle homogeneous coordinate is nonzero and the map reaches O. At W=0 the same holds, with middle coordinate -9RZ^4. On ZW!=0 the last coordinate is nonzero. Thus the covering map has no common-zero exception. At R=0 the coordinates reach (0,0) on E; this is a legitimate geometric two-torsion fiber, not a division by a discarded zero factor.

Its covering level is two and its map degree is four, inherited by the proved isomorphism G from the known full two-cover. Weighted polynomial degree six is not a map-degree computation. The compatibility with the exact C->E map fixes its H1(Q,E[2]) class as U3, not just an unnamed isomorphic genus-one torsor. Therefore Q3 is an everywhere locally soluble two-cover at the exact same strength as inherited U3 membership. This mathematical transfer is not a file containing newly computed local points on Q3.

## 4. Value and limits for the existing-method route

The explicit coefficient tuple and complete target map provide a concrete input model for a future, correctly bound existing four-descent or isogeny-chain interface. They do not supply a genus-one four-cover above it, a four-Kummer cocycle, the required T0-pushout on that higher cover, local four-cover witnesses or the mixed bit. Although abstract existence of a four-Selmer lift is known, Q3 itself remains a two-cover. Relabelling it as that lift would lose a factor of two in the covering maps.

A current runtime/API and its model conventions must be read before choosing a concrete intrinsic call. No parameter names, binary signature, code, test, runtime cost or export capability is invented here. An intermediate conic parameter's squareclass label is not silently identified with U3 merely because it is written3: the exact maps above, rather than an unverified normalization, preserve the input class.

The two global maps and separability proof are paper algebra. An actual future consumer still needs immutable input/code/codec and its genuine preaudit/resource/authorization gates. This note changes no budget and makes no scientific invocation. In particular neither the absence of rational points in a selected affine chart nor a local residue observation proves rank zero. Core(9,8)'s rational rank, actual higher lift and mixed bit remain UNKNOWN. All original paper/Source histories and the OPEN parent are preserved.

Driver-ID: EM-DVR-F73673 / CONTROL_PLANE
