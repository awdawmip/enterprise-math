# PREFIX-585-R2 — Polynomial 96-port UV/VU intertwining behind all-length BRC symmetry

Date: 2026-11-08 Asia/Shanghai. AUTHOR-SIDE PROVED WITH EXACT ORIGINAL NATIVE STRUCTURAL CHECK / UNREVIEWED / NOT_ADMITTED.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d; preserve P000 and all original 48 phases, 96 branch ports, 576 native labeled actions, six source-axis labels and original gate.

## The selected mathematical question

PREFIX-584 proved a novel unbounded-length closed-path trace identity by pairing native cyclic phase walks using a 48-phase anti-involution and summing their original two-branch gate weights with symmetric 2x2 matrices. Can the same symmetry be certified *directly as a finite 96-by-96 polynomial matrix identity*, without calculating any power or characteristic polynomial, and in a form useful for opening/endpoint correction?

YES. The result below gives two explicit polynomial 96x96 intertwiners U,V, valid even at singular gate parameter z=1 or zero axis weights. It constructs the entire spectral identity by a Sylvester AB/BA factorization.

## Exact original block decomposition

For every original phase i=(a,p,c), denote its axis label a(i)=|c|. For a phase j let t_j=1{j=T}, where T=(0,1,-3) is the original fixed native gate target.

Index the 96 states as (i,u), phase i∈{0,...,47}, branch bit u∈{0,1}. Let S_{ij} be the **original** 48-phase directed successor adjacency, S_{ij}=1 precisely when j is one of the three original successor phases of i, else 0. Keep the original six independent axis weights x=(x1,...,x6) and gate weight z.

Define the 96x96 polynomial matrices in 2x2 phase blocks:

    B(x)_{ij}= S_{ij} x_{a(i)} I_2,

    D(z) = blockdiag(M_{t_0}(z), ..., M_{t_47}(z)),

    M_t(z) = [[1, 1],
              [1, z^t]].

The complete original 96x96 marked native labeled weighted transition is

    A(x,z) = B(x) D(z).

Indeed its (i,u)->(j,v) entry is
    S_{ij} x_{a(i)} z^{t_j*1{u=v=1}},
which is precisely the original native BRC action weight; all 576 labeled edges are retained, including three distinguished gate edges. The probability version is A/6, with identical reasoning after scaling B by 1/6.

## Exact phase reversal

Let α=(1 3)(2 4), fixing axes5,6, and let Θ(a,p,c)=(a',-α(c),-α(p)) be the involution from PREFIX-584, with a' the unique STAR containing the transformed absolute labels.

On the 48 native phases Θ is a bijection, fixes T, reverses each of the 144 original phase edges, and maps the source-axis reward on an edge by α:

    i->j  implies  Θ(j)->Θ(i),
    a(Θ(j))=α(a(i)).

These are finite original-input structural identities already checked by the exact standard-library 48-phase certificate.

Lift Θ to the original 96 ports by the bit-preserving permutation
    H:(i,u) ↦ (Θ(i),u).
Write H for its 96x96 permutation matrix. Since t_{Θ(j)}=t_j and each M_t is symmetric, the following complete polynomial matrix identities hold by inspection of each 2x2 block:

    D(z)^T = D(z),
    H D(z) H^(-1) = D(z),
    B(αx) = H B(x)^T H^(-1).

These equations hold over Z[x1,...,x6,z] and require no inverse of B,D or any weight. Only H^(-1), a genuine permutation matrix, occurs.

## THEOREM 585.1 — Explicit polynomial UV/VU factorization

Define two 96x96 matrices:

    U(x)=H B(x)^T,
    V(z)=D(z) H^(-1).

Then for every set of commuting formal axis variables and gate variable,

    A(αx,z) = U(x) V(z),
    A(x,z)^T = V(z) U(x).

**Proof:** Since H commutes with D and B(αx)=H B^T H^-1,

    U V=H B^T D H^-1
       =H B^T H^-1 D
       =B(αx)D=A(αx,z),

and

    V U=D H^-1 H B^T =D B^T=(BD)^T=A(x,z)^T.

Each equality is a direct finite polynomial block identity. QED.

**Corollary 585.2: elementary polynomial characteristic identity.** For two square matrices U,V of the same size over any commutative ring, Sylvester's determinant identity gives

    det(λI-UV)=det(λI-VU).

Apply Theorem585.1 and transpose invariance of determinant:

    det(λI-A(αx,z))
      = det(λI-U V)
      = det(λI-V U)
      = det(λI-A(x,z)^T)
      = det(λI-A(x,z)).

This is an exact characteristic polynomial identity over Z[λ,x1,...,x6,z] for ALL parameters, including z=1 and x_i=0. It directly proves PREFIX-584's all-length trace and all-order spectral results (via equality of trace powers and the same characteristic polynomial), and it uses only two finite original BRC factor maps.

**Corollary 585.3: explicit polynomial intertwiners and boundary transport.**

    A(αx,z) U(x)=U(x) A(x,z)^T,
    V(z) A(αx,z)=A(x,z)^T V(z).

For every integer d≥0, the same equations hold with the corresponding d-th powers in place of A. Thus, for any column vector v,

    A(αx,z)^d U(x) v = U(x) (A(x,z)^T)^d v.

This gives an explicit algebraic boundary-vector conversion for open weighted paths in the range of U; the image and kernel of U delimit which endpoint data are transported without information loss. At x=z=1, B and D are singular, so we use these actual polynomial intertwining equalities rather than asserting an unproved invertible conjugacy.

## Verification and exact scope

An independent standard-library 96-port sparse integer checker reconstructs all original four STARs, all 48 phases/144 directed phase edges, the marked target and all 576 original labeled port actions. It verifies Θ is an involution fixing T; it checks every reversed edge and axis reward; then it builds A,B,D,H and tests

    A=B D; B(αx)=H B(x)^T H^(-1);
    A(αx)=U V; A(x)^T=V U

in **all 96x96 entries** at three integer weight specializations:
    x=(2,3,5,7,11,13), z=17;
    x=(1,1,1,1,1,1), z=1;
    x=(0,1,2,0,4,7), z=0.

All assertions passed (including singular parameter cases). The universal algebraic proof comes from the symbolic 2x2 block identities shown above, not from these three samples. Script: PREFIX585_R2_96port_ABBA_certificate.py; original full results: PREFIX585_R2_96port_ABBA_results.json.

BRC method reuse: COMPOSE_APPLIED (original native 96-port branch/gate weighted adjacency from PREFIX565 + exact Θ anti-involution from PREFIX584 + Sylvester AB/BA identity). This is an extension of the original BRC operator's observer-level spectral interface, not a replacement of native sources or global project foundations.

### Next

Use the explicit kernels/images of U(x), V(z) to characterize boundary vectors for which α acts as a finite-length open-path symmetry or as an exact endpoint repair, especially at singular z=1. A rank calculation over Q(x,z) and specialized open-path Markov boundary observables will distinguish intrinsic endpoint loss from repairable source/target mismatch.

The two previous group conclusions continue unchanged: marked native axis automorphism group C2, full characteristic-polynomial axis stabilizer C2×C2. PR and all math remain author-side until independent Source review; native Researcher-ID/CLAIM/Result unavailable during this run.
