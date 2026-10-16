# Matched finite-level log-crystalline specialization for the saved algebraic source

Author: EM-P11-4A56E9, inheriting EM-T6-BFF294 and all CONTROL/T6/P11/paper history, NONBLIND. Status: **new author paper, unreviewed**. The two preceding LC-D papers and their true nonauthor assessments retain their own scopes. Neither assessment reviews this new primary-source application. The fixed-(233,119) Task remains stopped2165/2100, remaining0, zero scientific execution.

## 1. The positive arrow claimed, and its limits

Fix an allowed split prime p=13 or19 modulo24. Let A=Z_p[[t]], A_n=A/p^n and R_n=Z/p^n. Let Y be the explicit projective Weierstrass family of the saved Source809bd geometry, with r=1+t and s=4r^3-3r:

    y^2=x^3+3(4s-5)x+4s^2-28s+22.

Write Y_n=Y x_A A_n, X=Y x_A F_p[[t]], and X_0=X x_(F_p[[t]]) F_p. All log structures below are the semistable t-divisor structure and its pullbacks. Define

    S_n=(Spec A_n, N->A_n, 1->t, I_n=(p), gamma_n),
    T_n=(Spec R_n, N->R_n, 1->0, J_n=(p), gamma_n),

and let Sbar=Spec F_p[[t]], Tbar=Spec F_p with the corresponding same-chart log structures. Thus T_n is a standard log point with nilpotent coefficients, **not** Spec R_n with trivial log structure. Put

    D_n=R Gamma((X/S_n)_log-crys,O),
    D_0n=R Gamma((X_0/T_n)_log-crys,O).

The claim is a canonical isomorphism of derived R_n-module complexes

    sp_n: R_n tensor^L_(A_n) D_n  ~> D_0n,               (1)

compatible with reduction in n. It is the actual finite-level crystalline specialization for this explicit **algebraic** model of the saved family, not the previous coherent normalization calculation. There is also the functorial Frobenius-compatibility square in section6; it requires no scheme Frobenius lift on Y_n.

No passage to a differently completed/formal site, Rlim_n, inversion of p, Q_p[[t]], locally free H^1, generic Gauss-Manin frame, Frobenius isogeny, cup multiplier or normalization graph injection is claimed. In particular (1) does not assert H^1(D_n) tensor R_n=H^1(D_0n): that assertion requires its own Tor/base-change control. Full LC A-C and whole D remain OPEN.

## 2. Exact primary text and selected imports

The primary source is O. Hyodo and K. Kato, *Semi-stable reduction and crystalline cohomology with logarithmic poles*, Asterisque223(1994), Expose V,221-268, official URL

    https://www.numdam.org/item/AST_1994__223__221_0.pdf

I consumed the existing complete shared PDF,1867725B, SHA256220873e91f89094d14f1a82631c6887a40ec362139990928236ca0525b1050cf, and verified its bytes independently. This is not a claim that I performed the earlier network retrieval. Its existing layout text has SHA25607202df784b3bf5a35b41e00d3e545a560450d2e041250c98a834fe52da6551a. I read the site/PD definitions in2.14-2.16, embedding definitions2.18-2.19, and the following two selected propositions; printed239-240 were additionally rendered from the PDF and visually inspected to check the diagram and derived-tensor symbol.

The two matched positive imports, paraphrased rather than reproduced, are:

- Proposition2.20, printed238: for an embedding system as defined there, the crystalline direct-image complex is canonically computed by the associated embedding/PD de Rham complex.
- Proposition2.23, printed239-240: in its cartesian fine-log diagram, with smooth integral X->Sbar, the two exact PD closed immersions, their PD-subideal condition, a radicial Sbar'->Sbar, and a flat crystal, the canonical **derived** sheaf-level base-change map is an isomorphism.

The PDF displays a superscript L on that tensor product; text extraction alone can obscure it. The adjoining lemma2.22 and beginning of2.24 are visible on those pages, but are not additional selected imports. No application of2.24's p-isogeny result or5.1's DVR comparison is made. Flatness needed in the calculation below is checked directly for this explicit lift, rather than adding2.22 as a third premise.

The source-family and primary-custody pins are inherited respectively from reviewed bundles Source809bd4b2c20682dfa29cb2eac0cf251bd4fa7d38 and Source82ac07759766a129bd5c6f442ccf12e8c7b4ca44. The old audit's rejection of direct5.1 is preserved. Its mere location of2.20/2.23 was not an application; the following diagram and hypotheses are this new authored work.

## 3. The actual diagram satisfies the selected hypotheses

Use exactly the following three-level diagram, with horizontal arrows specialization t->0:

    (X_0,M_0) -----> (X,M)
         |               |
         v               v
      (Tbar,N) -----> (Sbar,N)
         |               |
         v               v
       (T_n,N,J_n,gamma_n) ---> (S_n,N,I_n,gamma_n).

Here the upper square is a fine-log cartesian square. The base specialization map sends the chart generator to the same generator, and is strict; its fine-log base change has the displayed ordinary underlying fiber product. It is not a substitution of the normalization for X_0 and does not remove its node log structure.

Both lower vertical arrows are strict, hence exact, closed immersions defined by(p). The canonical PD structure on(p) in Z_p extends to A by

    gamma_j(p f)=p^j f^j/j!,

and descends to A_n and R_n. The ideal(p^n) is PD-stable: for j>=1, n*j-v_p(j!)>=n. The same formula proves compatibility under reduction and t->0. Thus the defining ideals of Sbar and Tbar are precisely PD-subideals I_n and J_n. The base schemes are killed by p^n, as required by the site's conventions; the PD ideal becomes zero on X and X_0. Finally Tbar->Sbar is a closed immersion of underlying schemes, hence radicial. Neither the DVR condition of5.1 nor perfection of F_p((t)) is a hypothesis of2.23.

For the remaining geometric condition, the saved discriminant is t times a unit, infinity is smooth, and the only central singularity is the ordinary split node with smoothing derivative a p-unit. Away from it the log morphism is ordinary smooth. At the node there is an etale semistable chart U V=t times a unit; after absorbing that unit in one chart coordinate it is the standard chart N->N^2,1->(1,1). Its group cokernel is free of rank1 and its monoid map is integral. Thus X->Sbar and its given lift Y_n->S_n are fine-log smooth and integral of relative log dimension1. This is the semistable structure already certified for the actual curve, not a new assumed global Frobenius lift.

One can check the underlying flatness directly: on the finite Weierstrass chart its monic equation in y makes the coordinate ring free over A[x]; near infinity the Weierstrass equation has a unit derivative in the local projective coordinate and is smooth over A. These opens cover Y, so Y/A and Y_n/A_n are flat. Relative logarithmic differentials are locally free of rank1 in the smooth and standard-node charts. This also checks the module flatness used below without inferring it from cohomology.

Take the structure crystal O on(X/S_n)_log-crys. On every crystalline object its module is the structure module of that object's thickening, free of rank1 over itself; it is therefore a flat crystal in the sense required by2.23. Its crystalline pullback to X_0 is the structure crystal there. All hypotheses selected from2.23 are now specified, not left as an unnamed semistable-comparison import.

## 4. The sheaf-level specialization is canonical and derived

Proposition2.23 applied to section3 gives on the etale topos of X_0

    O_(T_n)|X_0 tensor^L_(O_(S_n)|X_0)
          (Ru_(X/S_n),* O)|X_0
       ~> Ru_(X_0/T_n),* O.                             (2)

Restriction here means inverse-image sheaf, as specified in the primary text. Equation(2) is already a crystalline-category arrow. It is not deduced from the coherent conductor sequence, from branch fixedness, or from a purported O-cohomology-to-crystalline comparison in the wrong direction.

To see its explicit realization, the exact immersion X->Y_n is defined by the base PD ideal(p). It is strict. The constant simplicial embedding into the log-smooth lift Y_n is an embedding system for2.20: the hypercover is the identity and the ambient objects are log smooth. Its relative PD envelope is Y_n itself, since the ideal is already the base ideal with the compatible PD structure. The structure crystal's embedding complex is consequently

    [ O_(Y_n) --d--> Omega^1_(Y_n/S_n,log) ],             (3)

in degrees0,1, viewed on the same etale site as X. Nilpotent closed immersion does not change that etale site. Higher logarithmic wedges vanish because the rank is1. The same statement holds for the actual lifted central curve Y_0n=Y_n x_(S_n) T_n. No normalization of its nonreduced underlying ring is invoked.

The module/base-change map on(3) is the usual one on functions and universal logarithmic differentials. The latter commutes with this log base change by its defining generators and relations. Thus(2), under2.20's canonical models, is precisely the derived reduction of this log de Rham complex to t=0.

## 5. A bounded flat Cech model proves the global arrow

The global assertion(1) is not inferred by moving a tensor product past R Gamma without justification. Choose a finite affine open cover of the explicit separated projective scheme Y over Spec A. Every finite intersection is affine. Its base changes cover Y_n and Y_0n. Let C_A be the total Cech complex of the two-term relative logarithmic de Rham complex on this cover.

Each term is a finite sum of modules of sections of O_Y or Omega^1_(Y/A,log) on an affine intersection. Such a coordinate ring is A-flat because Y/A is flat; the locally free differential module is also A-flat. The finite cover and de Rham length1 give a bounded complex of flat A-modules. This is a termwise-flat Cech model; it is not a claim that its cohomology is flat.

Quasicoherent sheaves on these affines have no higher etale cohomology (equivalently their affine faithfully-flat descent complexes are exact), so this Cech model computes the required hypercohomology of(3). Sections on an affine intersection commute with the displayed base changes, and the log differential presentation does too. Hence2.20 identifies

    D_n   with C_A tensor_A A_n,
    D_0n  with C_A tensor_A R_n.                          (4)

Both identities compute crystalline cohomology through the given lift, not through a chosen Frobenius on that lift. The right complexes are bounded and termwise flat over their respective bases. Derived associativity now gives

    R_n tensor^L_(A_n) D_n
      ~ R_n tensor_(A_n) (C_A tensor_A A_n)
      = C_A tensor_A R_n
      ~ D_0n.

This is(1). The resulting map is the global specialization of(2), since each identification uses the same restrictions, log differential maps and canonical embedding comparison. Replacing the cover gives its usual common refinement and the same map. The construction also commutes with A_(n+1)->A_n and R_(n+1)->R_n, using the same flat C_A and compatible PD structures. No inverse-limit theorem is used to assert that compatibility.

## 6. Frobenius naturality, without an underlying lift on Y_n

The base PD endomorphism theta_n sends t->t^p and fixes R_n. On the log chart it multiplies the generator by p. Its central restriction phi_0n on T_n fixes the coefficient ring but also multiplies its log generator by p; it is **not** the identity as a log-base map. The specialization i_n:T_n->S_n satisfies

    i_n composed phi_0n = theta_n composed i_n

as log-PD-base morphisms. The characteristic-p schemes X and X_0 have their canonical absolute log Frobenius, which commutes with their specialization and these base maps modulo p.

Functorial crystalline pullback of the structure crystal along these morphisms supplies the usual semilinear maps Phi_n and Phi_0n on D_n and D_0n. This only uses the crystalline category's functorial pullback, not an endomorphism of the chosen characteristic-zero lift. After the canonical base-change identifications, naturality of(2) gives the commuting diagram

    R_n tensor^L_(A_n) theta_n^*D_n --1 tensor Phi_n-->
                         R_n tensor^L_(A_n) D_n
                  |                         |
                  | canonical              | sp_n
                  v                         v
             phi_0n^*D_0n ------Phi_0n-----> D_0n.       (5)

Here theta_n^* and phi_0n^* denote derived scalar pullback together with the indicated crystalline base maps. Underlying coefficient pullback on T_n is the identity, but the log map is retained. Equation(5) follows because both compositions are the contravariant crystalline pullback of the same commuting square; the base-change morphism is canonical. It can also be checked in common embedding/PD-envelope comparisons before taking hypercohomology, using the universal pullback maps, without a global scheme Frobenius on Y_n.

No calculation of Phi_n's matrix, p-isogeny, H^1 regularity or cup multiplier is included. Those stronger claims would require further input, including a correctly matched Frobenius theorem;2.24 is not imported here. In particular the earlier p13 obstruction to one specific scheme/log-node representative is consistent with(5): a crystalline morphism need not have that representative on the actual lift.

## 7. Precisely what has advanced

The new positive output is a fully matched crystalline sheaf specialization(2) and its global finite-level derived isomorphism(1) for the explicit saved algebraic model, with the functorial Frobenius square(5). This replaces an unnamed base-change hope by a specified diagram, PD structure, crystal and bounded flat calculation. It supplies one part of the previously missing LC-D route.

It does not identify any graph generator in D_0n, construct a crystalline normalization injection, or show that a graph image is the actual source residue-kernel line. The coherent graph calculation and its identity action still cannot be substituted for those arrows. The jump normalization of(omega+eta)/12, actual sign mu, c and extension data remain unresolved.

The formal LC problem may impose a particular completed site or Rlim_n realization. Only the explicit algebraic Spec(A_n) objects were defined and used here. Identifying them with any such separately specified completed realization, proving cohomological flatness, identifying the generic source connection/frame and establishing a Frobenius isogeny are separate obligations. No unqualified discharge of LC A-C, whole D, dagger/gluing, original functional or parent Goal is asserted.

No scientific program, symbolic consumer, enumeration, new checker, Task, Native vote, Tool, Foundation or Working Truth is created. PDF/text reading, rendering and hashing are primary-custody work. No raw third-party primary text or PDF is included in a publication capsule. This remains the CM24 mother axis; the separately allocated Parity m7 work is not duplicated. External arithmetic/log coordinates do not alter native Heartbeat X6 axes or physical-time semantics.

Researcher-ID: EM-P11-4A56E9 / TASK_RESEARCH
Global-Knowledge-Sync: main@051d8cb / GLOBAL_KNOWLEDGE_V1
