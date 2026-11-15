# R175 — Exact provenance-monoid lift of the signed six-axis four-moment port algebra

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: R174 at commit c545f0791abde0af7680abbf56d88b2d4b583d13, research_notes/portable_direct/R174_SIGNED_PORT_FOUR_MOMENT_CONTEXT_ALGEBRA_20261115.md.
Source code comparison: enterprise-math main@753008935fc9915f83da64a9d2cd6bb1fc7b0d83.

## Declared branch and provenance population

The path alphabet is the twelve signed X6 primitive directions (±E_i, i=1,...,6), with chart-relative displacement D(P) in Z^6 and prefix integral J(P)=sum_{t=1}^{|P|} sum_{r<=t} v_r. Fix any finite monoid (M,*,1) of provenance labels. This is a **chosen label algebra** for the proposed signed branch family, not a presumption about every native provenance implementation.

A branch is (input port i, output port j, signed rational weight w, monoid label m, ordered X6 path P). Alternative branches add formally. Compatible serial branches concatenate their ordered paths, multiply rational coefficients, and multiply labels in their given order. The allowed observer sees, at each ordered port pair and at each label m, the exact signed vector C_m=sum w J(P). Future contexts are all compatible left/right finite serial path families; single unit-labeled paths (including the empty path) are admissible probes. Internal branch inspection, arbitrary source filtering beyond the declared label observer, and physical dynamics are not admitted observations here.

The installed native modules src/enterprise_math/brc_weighted.py and src/enterprise_math/brc_recurrent_ports.py respectively implement positive CWM and nonnegative recurrent port closure. This R175 signed-rational extension is a mathematical design beyond those existing positive carriers.

## R175A — Algebraic theorem, for every finite monoid

Define A_m=sum w, L_m=sum w|P|, B_m=sum wD(P), C_m=sum wJ(P), separately at each port pair (i,j) and label m. Matrices A and L have entries in Q[M], and B and C have entries in Q[M]^6, with the *ordered* convolution product of the monoid algebra (which need not commute). For all composable families F,G,

    A(FG) = A(F) A(G)
    L(FG) = L(F) A(G) + A(F) L(G)
    B(FG) = B(F) A(G) + A(F) B(G)
    C(FG) = C(F) A(G) + A(F) C(G) + B(F) L(G).

For example, the last equation at output (i,k,m) is the sum over all intermediate ports j and ordered label decompositions u*v=m of C_ij,u(F)A_jk,v(G)+A_ij,u(F)C_jk,v(G)+B_ij,u(F)L_jk,v(G).

**Proof.** Each raw composable path pair satisfies |PQ|=|P|+|Q|, D(PQ)=D(P)+D(Q), J(PQ)=J(P)+J(Q)+|Q|D(P) (R171/R174). Multiply by both signed branch weights and sum over intermediate ports and ordered label products. Regroup terms by the label of the composite. This gives all equations. Their associativity follows from raw serial concatenation (and monoid associativity). QED.

## R175B — Exact observer minimality

**Theorem.** Two compatible finite signed branch families have identical C_m at every port and label after *every compatible two-sided serial context* if and only if their arrays (A_m,L_m,B_m,C_m) agree at every port and label.

Sufficiency follows by R175A and iteration.

For necessity fix a port pair and label m, and work with E=F-G. Port selectors isolate the chosen pair. If all labeled C-observations vanish, the identity context first gives C_m(E)=0. Let e be any signed native primitive step, and give each probe path monoid identity label 1. The left probe X=e(-e) has D(X)=0 and J(X)=e, so C_m(XE)=C_m(E)+e A_m(E), hence A_m(E)=0. The probe X=e gives C_m(eE)=C_m(E)+e(A_m(E)+L_m(E)), hence L_m(E)=0. The right probe Y=e yields C_m(Ee)=C_m(E)+e A_m(E)+B_m(E), hence B_m(E)=0. This recovers every coordinate for each m and port pair. QED.

For independent indispensability at any chosen label m, give every term of these R174 signed formal ensembles label m:

    A-only: epsilon
    L-only: e(-e)+(-e)e-2 epsilon
    B-only: ee-2e(-e)+(-e)e
    C-only: e(-e)-(-e)e.

Their respective nonzero A,L,B,C values are 1,4,2e,2e, and every other coordinate is zero. Unit-labeled identity contexts expose the one targeted coordinate. Vary e across the six native axes to cover every vector component. Therefore the four kinds of moments at every observable label are each necessary in this finite-linear four-moment summary.

## R175C — Exact coarser provenance quotient

Let φ:M→N be a surjective monoid homomorphism to a finite monoid N. Suppose only the N-class labels φ(m) are selectable in observations, and future serial contexts reveal only their φ-projected output labels. Then the exact necessary-and-sufficient summary is the four-moment pushforward for every n in N:

    A'_n=sum_{φ(m)=n} A_m, and analogously L'_n,B'_n,C'_n.

**Proof.** The pushforward Q[M]→Q[N] preserves addition and multiplication because φ(uv)=φ(u)φ(v). Apply it to all four equations in R175A; this proves sufficiency for arbitrary future serial contexts. Identity-labeled short probes and separate N-class C observers repeat the R175B necessity proof directly in Q[N]. Thus unequal pushed moments can be distinguished, and equal pushed moments remain equivalent under every declared operation. QED.

The theorem gives an exact scope-typed rule: retain label classes according to the future selectable quotient, including their signed moments; collapsing them further requires another observer certificate.

## R175D — Explicit positive-weight witness to label loss

In one port, let e=+E_1, f=-E_1, red ≠ blue, with two families of **positive unit-weight** branches:

    F = {(red,ef), (blue,fe)}
    G = {(red,fe), (blue,ef)}.

After forgetting the labels, both families have (A,L,B,C)=(2,4,0,0), since J(ef)=e and J(fe)=-e. However C_red(F)=+e and C_red(G)=-e. Thus the unlabeled R174 four moments lose a genuinely future-observable distinction even when all branch weights are positive. Merging red and blue by an allowed quotient is safe precisely when future selectors cannot distinguish that merged class, by R175C.

## Exact verification / status

Executable: research_notes/portable_direct/R175_label_monoid_check.py.
Machine result: research_notes/portable_direct/R175_verification.json.
The author-executed Python Fraction checker uses the six native components and M=Z/2×Z/3. It checks 36 exact signed four-branch families, 1296 raw-vs-labeled-moment products, 1296 corresponding quotient products, 81 two-sided quotient contexts, the positive red/blue counterexample and all four independent coordinate probes; every assertion passed. Universal claims R175A-C are established by the proofs above; the finite run is a separate reproducibility check.

This is author proof and exact local checking, NOT_REVIEWED by an independent mathematical reviewer. No native signed BRC execution, formal task CLAIM/Result, Working Truth or Foundation promotion occurred.

## Durable handoff / next discriminating question

Compare an actual source branch provenance API and its serial label operation (full-word concatenation, provenance tuples, last-writer labels, etc.) against the chosen monoid model. Determine which future selectors are allowed and whether a finite quotient N is sufficient; for weaker-than-all-class selectors, compute the actual minimal linear observational quotient. Signed recurrent closure also needs separate convergence/cancellation typing rather than assuming the positive Schur-port kernel already implements it.
