# H0P author-side matrix support: one diagonal support on the accepted [-3] carrier

Status: FROZEN_AUTHOR_SIDE_SUPPORT / PAPER_DERIVATION / NOT_AN_INDEPENDENT_REVIEW.

Author: EM-FREEPRIM3-A15D7C92. New direct activity:
RA-4ED8EF52CD84B113CECB33A2, TASK_RESEARCH, locally assigned stable session key
codex-local-root-primitive-round3-h0p-matrix-support-20261015.

This supports only EM-HODGE-7936BF's already opened execution
ER-BF4F98F4E5E071C9DCF6 / MCP-e3eda4529333438d8ae1ae7e6983e5e5 / claim
MCP-f80cca4c647192413eb7fda2 for
RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT. It does not borrow that
Researcher-ID, session or claim; create another H0P Task/claim; or supply a Native
review vote. The author's own direct-activity registration was created at EM
commit 50fefb87a0dec6be4bcfd688bf31a33651a6d11a and fully fetched there: blob
2d8913472fdc93d1ed73f29111c23d7e7977d7a1, SHA-256
ff65b9b5b270f771eed159922d039f2f76a3f805d42a285066013519edad0405.
Startup guard returned activity_allowed=true, persistence_allowed=true, and no
Task/claim/review/Working Truth/mathematical-acceptance authority.

## 1. Exact inputs, exposure and scope

Use only the accepted H0N carrier data for the construction:

    K=Q(i), U=K^6, Lambda=Z[i]^6,
    h=diag(1,1,1,-1,-1,-3).

Write D=diag(1,1,3). Fix the Hermitian convention linear in the first variable:

    h((x,y),(x',y'))=x^T conjugate(x')-y^T D conjugate(y').

The alternating form is E(v,v')=(1/2)Tr_{K/Q}(i h(v,v')). The special complex
structure is J_0(x,y)=(i x,-i y). These are the H0N carrier data, not a new
classification of the discriminant or a repetition of H0N's no-go theorem.

Exact source pins actually read:

* H0P taskbook at dfb6d99ae20038018de48fb25b631ab0c1ccafa8:
  research_tasks/HODGE_H0P_NONSPLIT_WEIL_BILATERAL_DEFORMATION_OBJECT_20260919.md,
  blob ee3ba08a77297bc0a29f41fbba2dca6acc8174ed.
* H0N return at the same commit:
  research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md,
  blob b504f4e3aa5401988cb3f51d699115489db3ee1c; use its carrier and its
  "Exact exceptional projector" section, at their stated strength.
* Accepted H0N Driver Markdown at 51b980512a901f6aaa377c2805be24b1a0c6ebe1:
  driver_reviews/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_DRIVER_REVIEW_20260902.md,
  actual returned blob 4074938be40dd54aa56997f3fafb6112482365ad. The initially
  relayed 8785195d0d17d94546cc2d422e2c5510d0627161 belongs to the separate
  review-record JSON, not this Markdown; the assigning author confirmed this
  metadata correction. The accepted strength remains NEGATIVE_BOUNDARY with an
  exact exceptional separator, not a general seed theorem.

The exact H0P publication TP2-05FAE6E393BAE7759DEC and the assigning author's
actual own-open receipt were checked. The taskbook's September-19 frontier is
explicitly UNREVIEWED and is not a mathematical premise here. I did not open
the September-19 bilateral graph note, the assigning author's later proof, a
32-graph search, a new candidate scan, or a higher-order/very-general argument.

This is NOT CLEAN. The same real author previously contributed the X6 modular
quadratic observer note and its mechanical index, retained at reviewed Source
7cff7b7ec220347b4f5d43b573d607cea2d1d403 and index Source
a43a87dfc24f438173f4e170b241919f18f6a0c5. All earlier primitive/router/tool and
Phase-B current-source exposure remains exposure. TASK_RESEARCH registration is
a real mode change, not a reset of identity, knowledge, contribution or author
independence. I have no earlier H0P construction contribution to hide; this note
itself is parallel author-side mathematical construction support.

Heartbeat's full native X6 remains the project spatial base, with no native
plane. The abelian variety below is an explicitly typed external algebraic
geometry object, not the spatial X6 Cell chart. A harmless state bridge is the
product (c; the declared external torus/Hodge data) over any native Cell c:
the present readout uses only the external data and leaves c, and all six native
spatial coordinates, intact. No spatial dimension, primitive direction,
physical force/rotation, final Cell address or physical time law is inferred
from this complex sixfold. The first-order parameter epsilon, epsilon^2=0,
is a formal external deformation parameter, not a time or spatial axis.

## 2. Independently specified special A_0, K action, polarization and Z

Let E_0=C/(Z+iZ), and define holomorphic coordinates

    z=x,       w=conjugate(y).

Then J_0 is multiplication by i in both z and w, and conjugation preserves the
Gaussian lattice. Hence

    A_0=(U_R,J_0)/Lambda = E_0^3_z x E_0^3_w.

For a+bi in Z[i], the holomorphic K action is

    iota(a+bi)(z,w)=((a+bi)z,(a-bi)w).

In particular the tangent matrix of iota(i) is diag(i I_3,-i I_3). It is not
scalar multiplication by i on all six holomorphic factors.

For a complex coordinate t, (i/2)dt wedge dbar(t) has integral one on E_0.
The Riemann form associated to the displayed E is represented by

    omega=(i/2)(sum_{a=1}^3 dz_a wedge dbar(z_a)
                  +sum_{a=1}^3 d_a dw_a wedge dbar(w_a)),
    (d_1,d_2,d_3)=(1,1,3).

Thus its positive Hermitian weight matrix in (z,w) is
A=diag(I_3,D); it is integral and positive. Indeed the real Riemann expression
E(v,J_0 v) equals ||x||^2+sum d_a |y_a|^2. This specifies the polarization on
the very same H0N h/lattice carrier, including the third negative weight 3.
No principal-polarization normalization replacing D by I_3 is made.

Define the algebraic embedding

    j:E_0^3 -> A_0,        j(t)=(t,t),       Z=j(E_0^3).

Its tangent vectors are tau_b=partial_{z_b}+partial_{w_b}. The induced
polarization on Z has weights (2,2,4). Z is not K-stable: iota(i)(t,t)=(it,-it)
is generally not diagonal. This is an ordinary algebraic diagonal support on
the special fiber, not a K-linear subvariety asserted on a very-general fiber.

## 3. Derivation of the complete nine-dimensional polarized K-linear tangent

Use the constant Kodaira-Spencer/Beltrami convention

    kappa_C=sum C_{ab} partial_{s_a} tensor dbar(s_b),
    s=(z_1,z_2,z_3,w_1,w_2,w_3).

These constant tensors represent H^1(A_0,T_{A_0}); the row is the holomorphic
tangent output and the column is the antiholomorphic covector input. This
fixes all transpose conventions below.

Preserving iota(i) requires C_{ab} to intertwine the conjugate source
eigenvalue with the target tangent eigenvalue. The two eigenvalues are i and
-i, so exactly the off-diagonal blocks survive:

    C = [ 0  B ]
        [ L  0 ],                B,L in M_3(C).

The linearized requirement that the fixed polarization remain of type (1,1)
is kappa_C contracted with omega having zero (0,2) part. Directly its
coefficients give

    A C = (A C)^T.

Since A C has blocks [0,B; D L,0], this condition is

    D L=B^T,             L=D^{-1} B^T.                 (3.1)

It is NOT L=B^T D^{-1}. Positivity is an open condition at the positive
Riemann point, so adds no further first-order linear equation. The resulting
constant first-order tensors are all polarized K-linear infinitesimal
deformations; the signature labels remain (3,3) on this local component.
Consequently the tangent space is exactly

    T_Weil = { C(B)=[0,B;D^{-1}B^T,0] : B in M_3(C) },

a complex vector space of dimension nine.

An ordered basis is indexed row-major by

    (11,12,13,21,22,23,31,32,33),

with B=E_{ij} and the explicit tensors

    kappa_{ij}=partial_{z_i} tensor dbar(w_j)
                  +(1/d_j) partial_{w_j} tensor dbar(z_i).     (3.2)

All nine independent B entries appear. Equations (3.1)-(3.2) give their full
6-by-6 matrices without suppressing any direction.

## 4. Normal-support obstruction, full matrix, rank and kernel

Identify the trivial normal bundle N_{Z/A_0} with O_Z^3 by the quotient

    q(v_z,v_w)=v_w-v_z.

Use n_a=q(partial_{w_a}) for its ordered constant basis and dbar(t_b) for
H^1(O_Z). The target basis is n_a tensor dbar(t_b), in the same row-major
order as above. Restriction along j sends both dbar(z_b) and dbar(w_b) to
dbar(t_b). Therefore the normal-support obstruction convention
ob_Z(kappa)=q(kappa restricted to Z) gives exactly

    ob_Z(B)=D^{-1}B^T-B,
    (ob_Z(B))_{ab}=(1/d_a) B_{ba}-B_{ab}.            (4.1)

This is the standard restriction/normal-quotient map to H^1(Z,N_{Z/A_0}).
Its vanishing is the first-order normal-support condition. Changing the overall
Kodaira-Spencer sign convention changes the entire map's sign, not its rank or
kernel. We do not identify this map with the full Atiyah/Yoneda obstruction of
an arbitrary mixed torsion/derived object.

In the specified source and target bases, its exact 9-by-9 matrix is

    M =
    [ 0  0   0   0  0  0   0  0  0   ]
    [ 0 -1   0   1  0  0   0  0  0   ]
    [ 0  0  -1   0  0  0   1  0  0   ]
    [ 0  1   0  -1  0  0   0  0  0   ]
    [ 0  0   0   0  0  0   0  0  0   ]
    [ 0  0   0   0  0 -1   0  1  0   ]
    [ 0  0  1/3  0  0  0  -1  0  0   ]
    [ 0  0   0   0  0 1/3  0 -1  0   ]
    [ 0  0   0   0  0  0   0  0 -2/3 ].

The (12,21) block has rank one. Each (13,31) and (23,32) block is
[[-1,1],[1/3,-1]], of determinant 2/3 and rank two. The 33 block has rank one,
while 11 and 22 are zero. Hence, on paper,

    rank_C M=1+2+2+1=6,       dim_C ker M=3.

Solving exactly gives

    ker ob_Z={ B=[a c 0; c b 0; 0 0 0] : a,b,c in C },

with ordered kernel basis E_11,E_22,E_12+E_21. In source vector coordinates
the 9-by-3 kernel-inclusion matrix has columns

    (1,0,0,0,0,0,0,0,0)^T,
    (0,0,0,0,1,0,0,0,0)^T,
    (0,1,0,1,0,0,0,0,0)^T.

The factor 3 is essential: replacing D by I_3 would produce a different map
B^T-B and would falsely give a six-dimensional kernel for this carrier.
There is no claim that Z survives all nine directions; its support obstruction
has a nonzero six-dimensional image. This single support calculation does not
decide whether another object can cancel a complete H0P obstruction.

## 5. Nonzero exceptional projection of this same special-fiber Z

The accepted H0N embedding-count separation applies to the K action on H^6
of this special fiber as well. Explicitly, in H^1(A_0,C), take

    V_sigma=span(dz_1,dz_2,dz_3,dbar(w_1),dbar(w_2),dbar(w_3)),
    V_barsigma=span(dbar(z_1),dbar(z_2),dbar(z_3),dw_1,dw_2,dw_3).

Here iota(i)^* has eigenvalues +i and -i respectively. Define the ordered
determinant forms

    Omega_sigma=dz_1 wedge dz_2 wedge dz_3
                    wedge dbar(w_1) wedge dbar(w_2) wedge dbar(w_3),
    Omega_barsigma=conjugate(Omega_sigma)
                 =dbar(z_1) wedge dbar(z_2) wedge dbar(z_3)
                    wedge dw_1 wedge dw_2 wedge dw_3.

They span the two distinct pure embedding-count blocks B_6 and B_0 and have
Hodge type (3,3). The elliptic quotient F_i(z,w)=w_i-z_i defines Z as the
transverse common zero fiber of the three F_i. With the normalized elliptic
point classes this gives its exact Poincare dual

    [Z]=product_{i=1}^3 (i/2)(dw_i-dz_i) wedge (dbar(w_i)-dbar(z_i)). (5.1)

The pure sigma term picks -dz_i and +dbar(w_i) in each pair. The three minus
signs and the three interleaving swaps cancel. Its coefficient at Omega_sigma
is (i/2)^3. For the conjugate ordered basis above, the pure barsigma coefficient
is -(i/2)^3. Thus the pure-block part is

    (i/2)^3 (Omega_sigma-Omega_barsigma),              (5.2)

which is nonzero since the two determinant lines are independent.

For an explicitly accepted separator, retain H0N's exact polynomial

    P(T)=-(T-125)(9881T-609029)(T^2+70T+15625)(T^2+150T+15625)
             /57000000000000000,
    Pi_W=P(iota(1+2i)^* on H^6).

On embedding-count block B_p the eigenvalue is
(1+2i)^p(1-2i)^(6-p). H0N's accepted substitution certificate says that P is
one on p=0,6 and zero on p=1,...,5. This spectral action depends on the K
action, not the very-general Neron-Severi rank. Applying it to (5.1) proves

    Pi_W[Z]=(i/2)^3(Omega_sigma-Omega_barsigma) != 0.

This is a rational cohomology class because both [Z] and the accepted projector
are rational; expression (5.2) merely writes it in a complex determinant basis.
It supplies a special-fiber algebraic input, not transport to a very-general
[-3] fiber, not all-direction deformation, and not a Hodge-conjecture claim.

## 6. Reuse, verification level and handoff boundary

Tool coverage was queried only after the assigned information structure was
understood and before proposing any tool. The actual lookup is retained in
COVERAGE.json. Its broad lexical REUSE_CANDIDATE_FOUND matches BRC and other
finite certificates, but none provides the typed polarized-Weil tangent/normal
map computed here. Those unrelated richer interfaces are NOT_APPLICABLE;
there is no claimed new global tool family or executable capability gap.
H0N's accepted K-eigenblock projector is REUSE_APPLIED at precisely the
separator strength; no semihomogeneous classification is recomputed or extended.

All nine directions, all 81 matrix entries, the rank decomposition, kernel
basis and the nonzero projector component above are complete paper derivations
for this one explicitly defined Z. No prior scientific experiment, candidate
scan, 32-graph computation, higher-order calculation or Native backend science
run was executed. No software enumeration or independent mathematical review
is claimed for this support. The companion MATRICES.json is a literal
structured transcription, not an additional mathematical assertion.

The requested bounded support unit is complete. Freeze these bytes and send
their paths and hashes to the authorized assigning author. Wait for their
actual artifact Source publication and immutable full readback, then append a
checkpoint to this support's own new TASK_RESEARCH activity. Do not emit a
Native scientific verdict, claim parent-task success, or start another support
family automatically. The assigning author's H0P execution and the project
parent remain OPEN.

Researcher-ID: EM-FREEPRIM3-A15D7C92 / TASK_RESEARCH
