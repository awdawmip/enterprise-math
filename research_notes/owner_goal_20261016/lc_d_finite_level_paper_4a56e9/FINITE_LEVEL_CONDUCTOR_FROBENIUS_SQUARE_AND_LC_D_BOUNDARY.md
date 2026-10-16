# A finite-level conductor square and its precise LC-D boundary

Author: Researcher EM-P11-4A56E9, inheriting EM-T6-BFF294 and all CONTROL, T6, P11 and paper exposure, NONBLIND. Status: **new author paper, unreviewed**. This is a separate Owner-directed CM24 paper unit, not continued fixed(233,119) preparation. That Task remains resource-stopped, budget2165/2100, no scientific execution. No program, enumeration, new checker, Task, Native vote, Tool or Foundation is created here.

## 1. Exact reuse and new question

I independently fetched Source00b7a0506a86d1d405f990afdfaa1be4ccc8daee's14416B direction (SHA6ad620c8699daa7bf50a597cca180eaaad580edfcd06f5a69864bdb5a6c652bf), geometry bundle Source809bd4b2c20682dfa29cb2eac0cf251bd4fa7d38 (SHA c4acbfb51a19897e2265e81607c4f0d9c831f31003207fab3f19b79e86989914), and primary-import bundle Source82ac07759766a129bd5c6f442ccf12e8c7b4ca44 (SHA a76d95e567e9819b002674d6d6bef7fe8a246020a0fd5f0f52ad3a89566b2e26). All18 embedded members were fully byte/SHA/Gitblob verified. Their review is reused at its exact conditional scope, not presented as review of this paper.

EM-DIRECT-18F24A and the earlier source authors retain scientific ownership. EM-CM24LOG-89CC19 proved the saved split-node geometry, normalization identities and conditional LC=>positive-sign argument. EM-FREE-333687's primary audit and its distinct review reject direct Hyodo--Kato5.1 on the two-parameter base and locate only incomplete relative interfaces. EM-PERFECT-9821E2 isolated the present finite-level comparison gap. This paper supplies the elementary finite-level conductor criterion and explicit corrected lift below; it does **not** supply the missing crystalline comparison arrow.

Reuse the exact central fibre and parameter conventions:

    C: y^2=(x-2)(x+1)^2,
    x=v^2+2, y=v(v^2+3),
    branches v=+nu,-nu, nu^2=-3 in Z_p,
    p=13 or19 mod24, theta(t)=t^p, coefficient Frobenius=id on Z_p.

The old facts that the branches are split and fixed modulo p and that eta+omega=dv are not reproved as a new solution of LC-D. The question here is what a **strict finite-level representative** on the normalization must do. In general a crystalline map need not admit such a global representative: it may require embedding complexes and homotopies. The criterion below must not be turned into an extra necessary hypothesis for all possible proofs of LC.

## 2. Base-changed normalization and conductor at every level

Fix the one chosen p-adic root nu, and reduce it compatibly modulo p^n. Put

    R_n=Z/p^n, B_n=R_n[v], q=v^2+3=v^2-nu^2,
    A_n=R_n[X,Y]/(Y^2-X^2(X-3)),
    X=q, Y=vq.                                              (1)

This is the affine nodal chart with X=x+1. At finite n, B_n is nonreduced when n>1: it is the **base change of the normalization over Z_p**, not a claim that the usual reduced-ring normalization of A_n is being taken.

The displayed homomorphism A_n→B_n is injective. Every element of the source has unique form a(X)+Yb(X); its image is an even polynomial in v plus vq times an even polynomial. Their even/odd parts cannot cancel, and substitution X=v^2+3 is injective by its unit leading coefficient. Also

    A_n = R_n + q B_n
        = {g in B_n : g(nu)=g(-nu)}.                        (2)

Indeed qv^(2m)=q(q-3)^m and qv^(2m+1)=vq(q-3)^m belong to the displayed algebra. Conversely the Chinese remainder decomposition B_n/qB_n=R_n×R_n holds because2nu is a unit; the equal-value condition is precisely the diagonal subalgebra. Thus the conductor is exactly qB_n: multiplying either coordinate of R_n×R_n independently shows that an element carrying all of B_n into the diagonal must vanish in both coordinates.

Consequently the following sequence is exact for every n, compatibly with reduction:

    0 → A_n → B_n --delta--> R_n → 0,
    delta(g)=g(nu)-g(-nu).                                  (3)

Surjectivity follows from delta(v/(2nu))=1. The modules A_n, B_n and the quotient R_n are flat over R_n: for A_n use its free basis over R_n[X] given by1,Y. No finite-level normality or unproved crystalline base-change premise is used here.

## 3. A strict descent criterion

Let f in B_n satisfy f=v^p modulo p, and let psi_f:B_n→B_n be the R_n-algebra homomorphism g(v)↦g(f(v)). The following are equivalent:

1. psi_f(A_n) is contained in A_n.
2. f(nu)=nu and f(-nu)=-nu in R_n.
3. delta psi_f=delta as maps B_n→R_n.

For the nontrivial implication1=>2, write r=f(nu), s=f(-nu). Reduction modulo p gives r=nu, s=-nu there, since the residue field is F_p. In particular r-s,2r and r+nu are units. Applying1 to X=v^2+3 gives

    0 = r^2-s^2 = (r-s)(r+s),

so s=-r. Applying it to Y=v(v^2+3) then gives

    0 = 2r(r^2+3).

Hence r^2=nu^2, and the unit r+nu implies r=nu; thus s=-nu. Condition2 implies3 by direct evaluation of every polynomial g, and3 implies1 by (2).

This proves an actual finite-level constraint, stronger than knowing only which branches are fixed in characteristic p. It preserves the two branch evaluations jointly and fixes the induced map on their difference quotient, with coefficient Frobenius=id.

## 4. The naive lift can already fail modulo p^2

For f(v)=v^p, put a=(-3)^((p-1)/2). Then f(nu)=nu a and f(-nu)=-nu a. The criterion says

    v↦v^p descends to A_n iff a=1 modulo p^n.               (4)

This holds modulo p for our split branches. It need not hold modulo p^2. At the allowed prime p=13,

    a=(-3)^6=729,  a-1=728=13*56,

and56 is a13-unit. Thus the naive lift does not descend to A_2. An explicit failure occurs on the actual nodal coordinate Y=vq:

    delta(psi_f(Y)) = 2nu^p(nu^(2p)+3)
                   = 6nu a(1-a^2),

whose13-adic valuation is exactly1, so it is nonzero modulo13^2. This is a paper integer identity and a fixed finite-level counterexample, not a prime scan or executed test. It refutes this particular strict representative, not intrinsic crystalline Frobenius or LC.

The failure is not corrected by adding an element of the conductor qB_n to f: such an addition changes neither endpoint. A successful correction must alter the offending endpoint values.

## 5. An explicit compatible correction exists on the underlying nodal scheme

Define

    D(v)=(v+nu)^p-(v-nu)^p,
    N(v)=nu*((v+nu)^p+(v-nu)^p),
    f_n(v)=N(v)/D(v) in B_n.                               (5)

This denominator is a genuine unit of B_n. Its constant term2nu^p is a unit; all nonconstant coefficients are divisible by p, and its degree is at most p-1. Write D=d_0+pE. Its inverse in B_n is the finite expression

    D^-1=d_0^-1 sum_(j=0)^(n-1) (-pE/d_0)^j.               (6)

Therefore (5) is polynomial at each finite level, with degree at most n(p-1)+1. The construction commutes with reduction n+1→n. Modulo p it equals nu^(1-p)v^p=v^p. Direct substitution gives f_n(nu)=nu and f_n(-nu)=-nu, so it descends to A_n and makes the following square commute **strictly at every level**:

    B_n --delta--> R_n
     | psi_f_n       | id
     v               v
    B_n --delta--> R_n.                                   (7)

It also has a projective construction: conjugate the power map w↦w^p by w=(v-nu)/(v+nu). Equivalently its homogeneous pair is [N(v,u):D(v,u)], where v±nu is replaced by v±nu*u in (5). This is a composition of two PGL_2 automorphisms and the degree-p power map; it is a morphism on P^1_R_n. It fixes both branch sections. The induced map on the affine nodal chart and on the complement of the node agree through the normalization, so they glue to a morphism of the proper nodal cubic. No flatness of that descended singular-curve endomorphism is asserted.

Here the gluing assertion can be checked within these charts. On the finite affine chart,

    f_n^2-nu^2 = 4nu^2 q^p/D^2.                            (8a)

Thus the complement of the two branch sections maps into that same complement: q and D are units there. On the projective normalization the only topological preimages of either branch section are that branch itself, since the reduction of the conjugated power map is Frobenius. The smooth complement of the node is isomorphic to the corresponding normalization complement. The affine map supplied by the descent criterion and this projective map therefore agree on their overlap. This argument only asserts affine preservation at each finite level, where D is a unit; it does not assert D is a unit of Z_p[v].

Replacing nu by -nu gives the same rational expression f_n; it reverses the chosen delta but leaves (7) unchanged. The correction Delta_n=f_n-v^p lies in pB_n and satisfies

    Delta_n(nu)=nu(1-a), Delta_n(-nu)=-nu(1-a).              (8)

Thus the correction need not lie in the conductor; at p=13,n=2 it cannot. Equations (5)-(8) exhibit the finite-level information omitted by a bare characteristic-p branch-permutation argument.

## 6. Exactly which cohomological graph statement follows

For the proper base-changed nodal cubic C_n and the base-changed normalization morphism pi:P^1_R_n→C_n, (3) gives the sheaf sequence

    0→O_C_n→pi_*O_P1→i_*R_n→0.                            (9)

Since H^0(P^1_R_n,O)=R_n, the global difference of constants is zero, and H^1(P^1_R_n,O)=0, its connecting map is an isomorphism

    j_n^coh:R_n ≅ H^1(C_n,O_C_n).                          (10)

The standard two-affine cover of P^1 proves the stated coherent cohomology over any R_n; no characteristic-zero de Rham argument is hidden here. The morphisms in (5) make (9) functorial, and (7) proves that their action under (10) is the identity, compatibly for all n. This is a **coherent normalization graph calculation for the constructed underlying-scheme lift**. It is not an identification with H^1_log-crystalline, the actual relative specialized H^1, or the saved source residue-kernel line.

## 7. The remaining LC-D morphism is still explicit

Keep S_n=(Z/p^n)[[t]], its t-divisor log structure, theta(t)=t^p, and the actual proper semistable source family. Let K_n denote a correctly constructed relative log-crystalline complex. The desired conclusion needs a Frobenius-compatible derived specialization/base-change map from K_n along t=0 to the central log-crystalline object, a normalization graph map into that object, and a lift/identification of that graph line with the actual specialized relative module. None of (1)-(10) constructs these arrows.

In particular:

- The base-ring identity i_n theta=i_n and the underlying nodal-scheme lift in (5) do not verify an embedding system, its PD ideals, exactness/flat-crystal hypotheses, proper-cohomology base change or formal inverse limits. The located Hyodo--Kato2.20/2.23/2.24 interfaces retain those obligations.
- A scheme-level lift preserving the conductor is not automatically a morphism of the saved log-PD embedding data. Its compatibility with the chosen smoothing chart and theta, or the required chain homotopies when no global strict lift is available, must be supplied. This paper claims no such log-crystalline identification for (5).
- j_n^coh has codomain coherent H^1(O), not the desired log-crystalline group. There is no automatic arrow in the required direction merely from (10). A crystalline normalization sequence and its Frobenius compatibility must actually be proved in the same convention.
- The saved relation eta+omega=dv has a primitive with an infinity pole. Its proper de Rham/Cech principal parts and branch jump must be transported through that actual comparison, not treated as global regular functions in (9). The saved e_hat,1=(omega+eta)/12 has oriented jump±nu/6;2,3,nu are units. This fixes a required normalization once the comparison exists, not its existence.

Thus the concrete output is the proven finite-level conductor square (7), its naive-lift obstruction (4), and the exact outstanding **crystalline/relative comparison morphism**. LC A-C remain uninstantiated; whole LC-D remains OPEN. No unconditional actual mu=+1, actual c, extension xi/eta, full-carrier dagger/gluing, original functional or parent closure follows. The old conditional implication LC=>mu=+1 is reused and not counted as a new result.

No broad literature lookup was made. The exact old reuse audit already rules out the circuit/BRC lexical tools at this input/output type; this is RESULT_ONLY elementary paper work, not a new shared tool family. All schemes and arithmetic precision parameters are separately typed external models over the unchanged native HeartbeatX6 project basis; neither v,t nor n is a native spatial axis or a physical time law.

Researcher-ID: EM-P11-4A56E9 / TASK_RESEARCH
Global-Knowledge-Sync: main@051d8cb / GLOBAL_KNOWLEDGE_V1
