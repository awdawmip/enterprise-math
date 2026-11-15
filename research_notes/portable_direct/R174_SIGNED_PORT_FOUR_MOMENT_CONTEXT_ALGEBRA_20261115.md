# R174 — Exact signed-port BRC candidate: minimal four-moment context algebra

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Dependency: R171–R173 signed-X6 prefix-integral observer, same research branch.
Foundation comparison: ENTERPRISE_MATH_WEIGHTED_BRC_GLOBAL_SUBSTRATE_V1 (finite positive-rational branch carriers, signed-amplitude boundary), P000 signed-X6 primitive directions and joint preservation, and HEARTBEAT_BRC_ONLY_ARITHMETIC. This is an explicitly **proposed signed-rational branch/port extension**, not an existing admitted positive-weight BRC implementation, nor a native physics/heartbeat/Shor computation. Its algebra is a mathematical design with exact proof.

## 1. Typed population, operations and observable

Fix a finite set of input/output ports I and native chart-relative primitive directions A={±E_i:1<=i<=6}. An elementary **signed branch** is the tuple (input_port i, output_port j, ordered path P∈A*, signed exact rational coefficient w∈Q). A finite branch family F is a finite *formal Q-linear combination* of these tuples. Retain this raw family whenever another future observer requires identity, coefficients, path labels, multiplicity or provenance beyond the declared moment readout.

- Parallel composition is formal addition (coefficients may be signed, including cancellation only after equality in the full chosen basis).
- Serial composition concatenates matching output/input ports, ordered native paths and multiplies rational coefficients. It is bilinear and associative.
- The permitted current observer reads for every ordered port pair (i,j) the **signed total prefix-displacement integral**
  
      C_ij(F) = sum_{branch i->j} w(P) J(P) in Q^6,
      J(P) = sum_{t=1}^{|P|} (sum_{r<=t} v_r).

- Future contexts are *all compatible left/right serial path families*, with the same C readout at the declared ports. Contexts may contain a distinguished single path with coefficient one. Branch inspection, path filtering, coefficientwise histogram/provenance and internal state access are **not** among these future observations.

Define the four source-signed port matrices with entries (scalars A,L and vectors B,C):

    A_ij(F)=sum w(P),
    L_ij(F)=sum w(P)|P|,
    B_ij(F)=sum w(P)D(P) in Q^6,
    C_ij(F)=sum w(P)J(P) in Q^6.               (1)

Each sum retains the selected port pair. A and L are scalar Q matrices, B and C are Q^6-valued matrices. No norm, positive mass, absolute values or floating point appear.

## 2. R174A: exact serial algebra and observer-safe quotient

For compatible F:I->J and G:J->K, with matrix multiplication over intermediate ports and coordinatewise extension to vectors, one has

    A(FG) = A(F) A(G);
    L(FG) = L(F) A(G) + A(F) L(G);
    B(FG) = B(F) A(G) + A(F) B(G);
    C(FG) = C(F) A(G) + A(F) C(G) + B(F) L(G). (2)

These equations hold *entrywise*, with (B(F)L(G))_ik=sum_j B(F)_ij L(G)_jk and genuine port indexing. They preserve the C readout under arbitrary serial composition of the four-moment summaries, and are linear under parallel addition. Thus F↦(A,L,B,C) is a typed algebraic quotient for exactly this C/context scope.

**Proof.** For each pair of elementary branches P,Q, R171 gives D(PQ)=D(P)+D(Q), J(PQ)=J(P)+J(Q)+|Q|D(P), and |PQ|=|P|+|Q|. Multiply by signed rational branch coefficients w(P)w(Q), sum over matching ports, and group separated terms. The cross term is precisely B(F)L(G). All identities follow; associativity of the induced four-moment algebra is inherited from the associative raw-path serial composition, or by direct expansion of (2). QED.

A quick algebraic interpretation: these four coordinates are the first length/displacement and mixed path-prefix jet of the formal branch language. This term is a local description, not a claim of implementing a previously admitted BRC jet tool.

## 3. R174B: four coordinates are jointly necessary and sufficient

**Theorem (all finite signed-rational families and all compatible two-sided path contexts).** Two families F,G with identical source/target port types have the same vector C readout under every compatible left and right serial path context if and only if their four port-moment matrices (A,L,B,C) are exactly equal.

**Sufficiency** follows immediately by iterating (2) and taking the C coordinate; parallel addition is also preserved.

**Necessity** is constructive. Compare one selected (i,j) port entry at a time using basis-port selectors; all other entries can be excluded by choosing compatible left/right port contexts. Set E=F-G, so the question is whether C(X E Y)=0 for all path contexts. We need only the four following probes, using any one native primitive direction e=+E_1:

1. X=Y=empty compatible identity paths: C(E)=0.
2. X=(+e,-e), Y=empty: J(X)=e, D(X)=0; by (2), C(XE)=C(E)+e A(E), so A(E)=0.
3. X=(+e), Y=empty: J(X)=e, D(X)=e; C(XE)=C(E)+e(A(E)+L(E)), so L(E)=0.
4. X=empty, Y=(+e): J(Y)=e, |Y|=1; C(EY)=C(E)+e A(E)+B(E), so B(E)=0.

The scalar-matrix equations are recovered channel by channel (the last one is vector-valued). This proves every coordinate is reconstructible from the declared future C contexts, hence any observer-safe quotient must distinguish unequal four-moment signatures. QED.

**Only context scope is being claimed:** if a future update can filter raw paths by hidden branch label or see branch coefficients individually, the four-moment quotient may cease to be sufficient and the raw provenance must be retained.

## 4. R174C: each coordinate independently indispensable

One-port explicit integer-coefficient witnesses, viewing F as a signed linear combination of primitive paths. Let ε be the empty path, e=+E_1, f=-E_1, and juxtaposition denote path concatenation. Define:

- A-only witness: H_A = ε. It has (A,L,B,C)=(1,0,0,0).
- L-only witness: H_L = ef + fe - 2 ε. It has (A,L,B,C)=(0,4,0,0).
- B-only witness: H_B = ee - 2 ef + fe. It has (A,L,B,C)=(0,0,2e,0).
- C-only witness: H_C = ef - fe. It has (A,L,B,C)=(0,0,0,2e).

All follow from the exact primitives:

    ε: (1,0,0,0);
    ee: (1,2,2e,3e);
    ef: (1,2,0,e);
    fe: (1,2,0,-e).

For any proposed deletion of one coordinate, its witness has **every other coordinate equal to zero**, yet the appropriate short context probe from Section 3 yields a nonzero C. These are four independent exact obstructions, not an argument merely based on parameter count.

The witnesses demonstrate that a signed *formal branch ensemble* is essential for the independence proof: R171–R173's single-path quotient alone does not assert these signed-linear dependencies.

## 5. Exact source-backed check

Executable: research_notes/portable_direct/R174_signed_port_moment_check.py.
Data: research_notes/portable_direct/R174_signed_port_moment_verification.json.

The checker uses exact Python Fraction arithmetic, constructs formal finite signed weighted path families with 2 ports, compares direct raw pairwise path concatenation with equations (2) for all 4 moments, and verifies the four independent witness signatures and their separating context responses. It does not call a native BRC kernel, claim an amplitude simulation, or compute physical residuals. Full universal results are proven algebraically; finite tests validate the proposed new typed extension.

Independent mathematical review and formal checker: NOT_REVIEWED / NOT_RUN. No theorem promotion, Result, CLAIM or Foundation admission is inferred from this author proof.

## 6. Value and next experiment

R174 converts the previous path-level residual into an explicit **port-labeled signed branch algebra**, with a fully characterized minimal observer-safe compression lease under chosen serial/parallel operations. It clarifies the transition from R170's one-bit word-identity repair to a branch-sensitive BRC-style observer: four exact signed moment matrices are necessary even before hidden labels or higher moments are exposed.

The next concrete task is to map this candidate against an *actual* signed/native BRC interface (if present), including the repository's real branch representation, port semantics, allowed update and cancellation relations. If that interface needs branch-specific filtering, give a minimal counterexample where equal (A,L,B,C) splits under a legitimate new operation, then add only the required provenance coordinate. Do not treat positive Weighted-BRC mass as signed amplitude.
