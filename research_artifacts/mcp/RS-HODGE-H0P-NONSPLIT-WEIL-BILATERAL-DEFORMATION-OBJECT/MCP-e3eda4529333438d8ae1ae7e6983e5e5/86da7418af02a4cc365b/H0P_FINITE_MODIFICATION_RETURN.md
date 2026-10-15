# H0P: finite-length graph modifications retain a rank-six complete obstruction

Status: FROZEN_AUTHOR_RETURN / NEGATIVE_BOUNDARY_FOR_DECLARED_FAMILY /
AWAITING_INDEPENDENT_NATIVE_AND_SCIENTIFIC_REVIEW.

Lead author: EM-HODGE-7936BF, prior contribution ID EM-CM24LOG-89CC19.
Mathematical support contributor: EM-FREEPRIM3-A15D7C92
(TASK_RESEARCH activity RA-4ED8EF52CD84B113CECB33A2).
Task: RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT.
Publication: TP2-05FAE6E393BAE7759DEC.
ER: ER-BF4F98F4E5E071C9DCF6.
Own winning claim: MCP-f80cca4c647192413eb7fda2.
Own service session: MCP-e3eda4529333438d8ae1ae7e6983e5e5.
Authorized run: h0p7936bf-open-20261015-01.

## Result and exact scope

Let A0 be the explicitly specified special member of the accepted non-split
[-3] Weil component, and let j:Z=E^3 -> A0=E^3 x E^3 be the diagonal.
For every zero-dimensional closed subscheme D of Z, including arbitrary
nonreduced D and the empty scheme, consider the actual perfect sheaf
F_D=j_*I_{D/Z}. This is an actual finite-length elementary modification of
the graph sheaf, not a signed virtual graph class.

For every member of this declared family:

1. Pi_W(ch_3(F_D)) is the same nonzero exceptional class as Pi_W[Z].
2. The complete object Atiyah--Kodaira--Spencer obstruction on the full
   nine-dimensional polarized K-linear tangent space has rank six and kernel
   B={[[a,c,0],[c,b,0],[0,0,0]]}.
3. In particular no F_D has zero complete obstruction in all nine directions.
   Adding finite torsion on this fixed support cannot repair its deformation.

The exact full restricted map is supplied below in an explicit basis of its
image, with Yoneda representatives specified by At(F_D) and fixed tangent
classes. An ambient basis for the entire Ext^2(F_D,F_D), whose size depends on D,
is neither asserted nor needed for this negative family-level classification.
No unrestricted mixed-derived no-go or positive all-direction object is claimed.

## 1. Same carrier, polarization and actual seed

The accepted H0N data are K=Q(i), Lambda=Z[i]^6, and
h=diag(1,1,1,-1,-1,-3), linear in its first argument.
Write D0=diag(1,1,3) for the polarization weight matrix; D0 is distinct from
the finite subscheme D. On underlying K coordinates (x,y), use
J0(x,y)=(i x,-i y). Holomorphic coordinates are (z,w)=(x,conjugate(y)).
Then A0=E^3_z x E^3_w for E=C/(Z+iZ), with K action

    iota(a+bi)(z,w)=((a+bi)z,(a-bi)w).

The Riemann form (1/2)Tr(i h) becomes

    omega=(i/2)(sum dz_a wedge dbar(z_a)
                      +sum d_a dw_a wedge dbar(w_a)),  d=(1,1,3).

It is integral and positive, with weights diag(I3,D0), on the same accepted
h/lattice carrier. In particular the third weight is 3, not 1.

The algebraic diagonal j(t)=(t,t) is not K-stable. Its cycle is

    [Z]=product_a (i/2)(dw_a-dz_a) wedge (dbar(w_a)-dbar(z_a)).

In H^1(A0,C), the sigma eigenspace has ordered basis
(dz1,dz2,dz3,dbar(w1),dbar(w2),dbar(w3)).
Write its top exterior form Omega_sigma, and let Omega_barsigma be its
complex conjugate in that displayed conjugate order. Extracting the two pure
embedding-count terms gives

    Pi_W[Z]=(i/2)^3 (Omega_sigma-Omega_barsigma) != 0.       (1.1)

Here Pi_W is exactly H0N's accepted rational polynomial in iota(1+2i)^*;
its spectral action is reused, not reclassified. The two determinant lines
are independent. Although (1.1) uses a complex basis, the class is rational
because both [Z] and Pi_W are rational.

The graph is the common zero fibre of q_a(z,w)=w_a-z_a. The three associated
point divisors have squares zero, so their Koszul formula gives
ch(O_Z)=[Z]. The exact sequence
0 -> F_D -> O_Z -> O_D -> 0 and a composition series for O_D then give

    ch(F_D)=[Z]-length(D)[point],       ch_3(F_D)=[Z].       (1.2)

The separate Chern lemma supplies the global point-divisor Koszul verification.
Thus this family passes the nonzero-seed test on A0; it fails at deformation,
not at an assumed loss of its Weil component.

## 2. All nine tangent directions and normal-support map

Use tangent-output rows and antiholomorphic-input columns for a constant
Kodaira-Spencer tensor. Preserving the K action forces off-diagonal blocks.
Preserving the polarization requires diag(I3,D0)C to be symmetric. Thus all
nine directions, with no omitted equation or scalar normalization, are

    C(B)=[[0,B],[D0^{-1}B^T,0]],       B arbitrary in M3(C).

For B=E_ij the class is explicitly

    kappa_ij=partial_z_i tensor dbar(w_j)
                      +(1/d_j) partial_w_j tensor dbar(z_i).

Identify N_{Z/A0}=O_Z^3 by q(v_z,v_w)=v_w-v_z. Restriction to the diagonal
identifies both antiholomorphic covectors with dbar(t). The normal obstruction is

    delta_Z(B)=D0^{-1}B^T-B.                              (2.1)

In row-major source and target orders (11,12,13,21,22,23,31,32,33), its full matrix is

    [0  0   0   0  0  0    0  0   0  ]
    [0 -1   0   1  0  0    0  0   0  ]
    [0  0  -1   0  0  0    1  0   0  ]
    [0  1   0  -1  0  0    0  0   0  ]
    [0  0   0   0  0  0    0  0   0  ]
    [0  0   0   0  0 -1    0  1   0  ]
    [0  0  1/3  0  0  0   -1  0   0  ]
    [0  0   0   0  0 1/3   0 -1   0  ]
    [0  0   0   0  0  0    0  0  -2/3].

The (12,21) block has rank one, the (13,31) and (23,32) blocks each have
determinant 2/3, and the 33 coefficient is -2/3. Therefore rank(delta_Z)=6,
with kernel span(E11,E22,E12+E21). These are exact rational calculations, not a
parameter-count argument or an empirical rank.

The independently derived author-side MATRIX_SUPPORT.md gives the full
same-carrier verification, coefficient signs, spectral extraction and matrix
derivation. MATRICES.json records all nine 6-by-6 tangent matrices and all
81 entries above. The author-side support is not an independent review vote.

## 3. Bridge to the complete object obstruction

For a smooth closed projective Z in a smooth projective X with dim Z>=3 and
finite D in Z, the companion FINITE_SUPPORT_DEFORMATION_LEMMA.md proves

    j_*I_{D/Z} admits a perfect lifting over X_R
                         iff delta_Z(kappa)=0.           (3.1)

The proof is essential; simply identifying a normal map with an Ext obstruction
would not suffice. Its necessary direction first shows any derived lifting of
this sheaf is an R-flat sheaf: tensor the exact dual-number sequence
0 -> C -> R -> C -> 0 and use the special fibre concentrated in degree zero.
Away from D the sheaf is cyclic O_Z; a lifted generator and its annihilator
therefore recover a flat embedded deformation of Z minus Supp(D).
The normal obstruction consequently restricts to zero there.
The normal bundle has depth three at the finite punctures. Local-cohomology
vanishing in degrees1,2 makes H^1(Z,N) -> H^1(Z minus Supp(D),N) an isomorphism,
so its original class is zero.

For sufficiency, a zero normal Cech class glues a first-order embedded Z_R.
A smooth affine chart containing D has a noncanonically trivial first-order
deformation, allowing the constant finite scheme D_R. Its ideal is flat and
perfect; pushforward along the regular immersion Z_R -> X_R gives the desired
perfect lifting. Nonreduced finite D is covered by this argument without any
enumeration.

The exact external obstruction input is Huybrechts--Thomas,
arXiv:0805.3527v2, Corollary3.4: under its square-zero and smooth-ambient
embedding hypotheses, a perfect lift exists exactly when the full
Atiyah/Kodaira-Spencer product in Ext^2 vanishes. Those hypotheses apply here:
the object is perfect on smooth A0, the first-order polarized deformation is
projective, and its projective embedding over R embeds in a smooth complex
ambient P^m x A^1. Stacks tags0AVZ,0G71,0A6T provide the exact local-cohomology
interfaces. The primary-input ledger states each import and its hypotheses.

Thus, with Omega_D the complete object obstruction, not its Chern trace,

    ker(Omega_D|T_Weil)=ker(delta_Z|T_Weil).               (3.2)

No semiregularity injectivity is assumed.

## 4. Exact restricted Ext/Yoneda map and family no-go

Put eta_ij=(id_{F_D} tensor kappa_ij) composed with At(F_D)
for ij in the ordered list (12,13,23,31,32,33).
These are concrete Yoneda degree-two classes for the explicitly defined object
F_D and explicitly specified kappa_ij. Equation (3.2) and the six independent
columns of (2.1) prove these six classes are linearly independent; this is not
an assumption about Ext dimension.

Linearity and the other three exact kernel relations yield the complete map

    Omega_D(B)=(B12-B21) eta12+B13 eta13+B23 eta23
                                +B31 eta31+B32 eta32+B33 eta33.   (4.1)

Its 6-by-9 matrix in that image basis has rows

    [0 1 0 -1 0 0 0 0 0]
    [0 0 1  0 0 0 0 0 0]
    [0 0 0  0 0 1 0 0 0]
    [0 0 0  0 0 0 1 0 0]
    [0 0 0  0 0 0 0 1 0]
    [0 0 0  0 0 0 0 0 1].

This specifies the full restricted object obstruction, its rank and every
vanishing direction for every finite D. For example kappa33 has the nonzero
support class -(2/3)n3 tensor dbar(t3), so eta33 != 0 for every member.
It follows that no member deforms over all nine Weil directions, despite (1.1).
The entire finite-length modification family is killed for the positive route.

## 5. What is new, what is retained, and what stays open

The new bounded conclusion is the exact complete-obstruction classification of
all finite-length modifications of one explicit non-split graph seed:
nonzero exceptional ch3 is retained, while rank-six obstruction and its
three-dimensional kernel are invariant under every such modification.
The general proof uses standard deformation and local-cohomology techniques;
no claim of novelty priority or new global software/tool family is made.

H0N's very-general semihomogeneous/divisor no-go is retained at its actual
strength. The present special fibre has extra divisor classes, so its graph
does not contradict that theorem. H0O's fixed Fourier--Mukai conservation
boundary is not reopened. No 32-graph checkpoint is consumed as theorem evidence.

The minimal unresolved H0P gap remains an actual mixed torsion/perfect derived
object, outside this finite-length graph-modification class, whose nonzero
exceptional ch3 survives with zero complete obstruction in all nine directions.
This return supplies no such object, no unrestricted family no-go, no higher
order deformation, and no transport to a very-general fibre. H0Q/H0R gates and
the mother objective remain open; no successor Task is registered here.

Kill/no-repeat: do not rescan D, enlarge its finite length, replace it by
nonreduced finite schemes, or add acyclic resolutions hoping to change this
obstruction; all are covered. A future candidate must change the relevant
generic support/object geometry or leave the precisely declared class, and
must pass a fresh same-carrier, exceptional-seed and complete-obstruction test.

## 6. Provenance and control boundary

The lead author read H0N/H0O inputs, the unreviewed September19 note and the
restored H0P/Q/R routing; old CM24 and QR/CRT contributions remain exposed.
The helper retained its X6/primitive contributions, registered a real new
TASK_RESEARCH activity, and independently derived only the model, nine-direction
matrix and exceptional graph projection before reading the lead proof.
Both are authors. Neither gives a third-party scientific or Native review vote.

Exact native session_start -> task -> prepare_exact -> winning claim -> open
receipts are retained in the startup control directory. This paper began only
after own open SUCCEEDED. No other conversation's session/claim was borrowed.
The ordinary algebraic varieties, tangent parameters and cohomology above are
explicitly external mathematical carriers; they neither identify a native
Cell torsor with a plane nor modify the full native Heartbeat X6 base.

The present artifact is an author-frozen negative family boundary, to be
published/checkpointed/frozen through the actual run and independently reviewed.
It is not mathematical acceptance, Driver authority or project-goal closure.

Researcher-ID: EM-HODGE-7936BF / RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT
