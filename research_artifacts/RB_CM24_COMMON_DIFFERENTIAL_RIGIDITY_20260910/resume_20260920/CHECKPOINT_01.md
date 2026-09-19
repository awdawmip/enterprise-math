# Common-kernel and CM-norm checkpoint

Researcher `EM-RB-1EB0B6`; Task `RS-RB-CM24-COMMON-DIFFERENTIAL-RIGIDITY`; publication `TP2-F588CAD6A9583BB015B3`; real CLAIM `5744662393`; ER `ER-F6F23D03479064A62FCD`.

Status: `SOURCE_EXPOSED NON-AUTHOR DERIVATION / NOT DRIVER-ACCEPTED / ARITHMETIC APPLICATION REPORT STILL TO COMPLETE`.

The checked statement and route were proposed by Driver `EM-DVR-5816EB` in `f26db9901f034bbd3a3dae0c03061064ba99caf1:research_artifacts/RB_COMMON_DIFFERENTIAL_TASK_20260910_5816EB/driver_candidate_unreviewed.md` (SHA256 `4178343465d910ea6c40577d2e03b41032194d4d46ae9cd2dab490ae7021b489`). This researcher did not author that proposal. The derivation below supplies its missing arguments as a source-exposed check; it is not clean blind independence. New application formulations will be separated in the final report for other-reviewer acceptance.

## Fixed inputs consumed

The accepted source is `0f4fc206e6c3a950cdd7c7587a455bfc829d8a33`, with formula freeze SHA256 `85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2`, exact-map proof SHA256 `7c8c480af589fcd875488a8031db4e6adb1cc1a144adee2950a2e16b74866f12`, Result `RR-F79FA3D36EF85CC4C6CE`, and accepted review `DR-7D70258F6D39E9B6B00D`. Its later acceptance supplies f0 of degree six and the unsquared equality f0*omega0=phi over L=Q(alpha,beta,i), retaining C0, N/D0 and Y0=w*delta(X0)/(t+k). The historical INCOMPLETE proof header is not being used to revoke that later accepted input. The 80-map computation is not rerun.

## Complete geometric implication, retaining nonprimitive maps

Work over the chosen algebraic closure inside C. Fix a base point P on D and use the Abel map aP:D->J(D). For each f, remove its value f(P), obtaining u:J(D)->E0; likewise u0 for f0. The Abel-map pullback on regular one-forms is an isomorphism, so f*omega0=c phi implies u*omega0=c u0*omega0. Thus their tangent kernels coincide. A homomorphism to an elliptic curve in characteristic zero with zero differential is zero: otherwise its positive-dimensional image is the elliptic curve and its smooth kernel has codimension one. Applying this to restrictions to the connected kernels shows B=(ker u)^0=(ker u0)^0. No equality of their full kernels is asserted.

Take Q=J/B. One may construct it using a Poincare complement B' and the finite quotient B'/(B intersect B'). Both u and u0 factor through q:J->Q as isogenies v,v0:Q->E0. If g=q aP then deg(v)deg(g)=deg(v0)deg(g)=6, so the finite isogeny degree m divides six but is not set to one. This retains all nonprimitive possibilities and does not compute any saturation or period index.

Use the canonical principal polarizations to define daggers. Under Jacobian autoduality u-dagger is the Picard pullback f*, so the divisor identity f_*f*=[deg f] gives u u-dagger=[6] and u0 u0-dagger=[6]. Because the polarizations are principal, these are integral homomorphisms; no rational inverse of a nonprincipal polarization occurs. Duals reverse composition and v-dual,v0-dual are surjective isogenies. Consequently u-dagger and u0-dagger have the same image A0, an elliptic subvariety of J. This step does not require q-dual to be an isomorphism or u0 to be primitive.

Put P0=u0-dagger u0. On A0, P0=[6], since P0 u0-dagger=u0-dagger[6] and u0-dagger surjects onto A0. For A=u u0-dagger in End(E0), therefore

    A A-dagger = u (u0-dagger u0) u-dagger = u [6] u-dagger = [36].

The definition of elliptic duality gives degree(A)=36. All finite-kernel factors remain in this argument; there is no omitted primitive index.

The CM identification is separate. The accepted j is 2417472+1707264 beta. The Hilbert class polynomial of discriminant -24 is

    H_-24(X)=X^2-4834944 X+14670139392.

The exact integer substitution into this polynomial vanishes using beta^2=2. The polynomial was read in Joan-C. Lario's original CM table and independently computed locally by python-flint0.8.0 / FLINT3.3.1. The Hilbert-class-polynomial characterization identifies its complex roots precisely with End(E) equal to the order of discriminant -24; it is not an inference from a task label or j alone. This order is the maximal order Z[sqrt(-6)]. Geometric endomorphisms are thus integral a+b sqrt(-6), and elliptic duality is conjugation, so degree(A)=a^2+6b^2=36.

The existing BRC integer/root facade supplies complete bounds and exact remainder traces: |b|<=2, and for |b|=0,1,2 the possible a^2 values are 36,30,12. Only 36 is a square. Hence A=+/-[6]. Also u0(P0-[6])=0. The image of the connected J under P0-[6] lies in B, so u(P0-[6])=0 and A u0=[6]u. Consequently [6](u-epsilon u0)=0. A connected image cannot be a nontrivial finite subgroup; therefore u=epsilon u0, epsilon=+/-1. Returning to the unbased maps gives

    f=epsilon f0+T,  c=epsilon,

with a constant translation T. The scalar was derived, not fixed at the start.

## Primary facts and checked hypotheses

- Milne, [Jacobian Varieties](https://www.jmilne.org/math/xnotes/JVs.pdf), Proposition2.2, Proposition6.1, Corollary6.3, Theorem6.6 and Lemma6.9: Abel differentials, Albanese property and canonical autoduality. D is smooth projective, geometrically connected, with positive genus; E0 is nonsingular; base points are explicitly removed. The transpose/pullback identification is used with canonical polarizations and the positive push-pull degree convention.
- Milne, [Abelian Varieties](https://www.jmilne.org/math/xnotes/AVs.pdf), section8, Theorem11.1 and Proposition12.1: characteristic-zero kernels, duals of isogenies, and Poincare complements. The quotient used above kills only the connected common kernel; its residual isogenies are retained.
- Sutherland, [18.783 Lecture20](https://math.mit.edu/classes/18.783/2023/LectureNotes20.pdf), section20.3 and Theorem20.12: roots of H_D have the exact imaginary quadratic order indexed by D, and the polynomial is integral. This is used geometrically, not to identify twists over L.
- Lario, [original CM table](https://web.mat.upc.edu/joan.carles.lario/ellipticm.htm), h_2 row D=-24; local independent polynomial output is `cm_class_polynomial.json` and `cm-replay.stdout.json`.

## Actual checks and remaining work

`check_cm_norm_and_transports.py` imports the unchanged pinned RB integer-ring primitives and existing BRC facade. It executes no historical checker main. Its frozen certificate `exact_certificate.json` has SHA256 `cb82f4e1eb4c0b3c8d42184f4acf11ac9db8ebbbed070931745a1293e91c3585`: ten polynomial identities, six tamper checks, and three norm/scalar boundary tests pass. A rational norm-36 element with denominator7 and a Gaussian norm-36 element explicitly show why integrality and the correct CM order may not be omitted. These finite checks do not replace the geometric proof above.

Remaining before the complete return: finish the self-contained base-point/dagger conventions, write the exact target-twist differential multiplier and Galois descent conditions, separate centered translations from arbitrary translations, and apply the resulting constraint to the full retained parameter index with degeneracy/field boundaries. Proper-subfield descent and any actual lattice/period index must not be silently claimed. No accepted classification of the 1980 systems or parent closure is asserted by this checkpoint.
