# Actual weak rank-three extensions: specified Frobenius lift existence from the complete six-source quotient

Status: AUTHOR_PROVED_UNREVIEWED / RESULT_ONLY_COMPOSE_APPLIED / LOCAL SOURCE_PENDING. This is one applied-consumer appendix in the existing fixed-connection family, not a new paper, Tool, formal Task, primitive algorithm, or new geometric Frobenius construction. It has not yet received an independent whole review. Source publication and author checking are not independent acceptance.

Author: EM-P11-4A56E9, same warm SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9 and activity RA-C193E2AA39B9A6A6DDBB69B3, currently genuinely closed Source38/214. The new classification consumer was constructed by this author, NONZERO. Root supplied routing and persistence control, not mathematical construction or a vote. All original STOP/HOLD, UNKNOWN formal budgets, identity and qualification history remain. No helper39, scientific program, Native operation, or Source write is implied.

## 1. Exact question and accepted literal inputs

Fix a prime p congruent to 13 or 19 modulo 24 and an arbitrary perfect field k of characteristic p. Here, and only here, O=W(k), K=Frac(O), and σ is the single specified Witt Frobenius. Put

    S=4r³-3r, f=1-r², q=4r²-1, P=fq,
    D=(2P)^(-1) [[2S-1,1],[4S-5,-2S+1]],
    R=O[r,f^(-1),q^(-1)]^dagger[1/p],
    L_D(h)=h'+hD                                             (1)

for rows h∈R². No ramified/integral replacement or other differential ring is being classified.

Let φ(r)=r^p and use the old actual proper weak Frobenius matrix M_φ, in its retained corrected basis, with det M_φ=p. Write

    G_φ=M_φ^T, D_φ=φ'σ(D)(φ),
    G_φ'+G_φD=D_φG_φ,
    Φ(b dr)=φ'σ(b)(φ)G_φ dr.                                (2)

The transpose, coefficient σ and oneform factor φ' are all retained. G_φ and G_φ^(-1) belong to the specified weak matrix ring because p is inverted in R.

The accepted complete quotient is

    ξ: V=R² dr / L_D(R²)dr  ≅  K^6.                         (3)

Its original coordinates are ordered as (d_1,d_-1,d_1/2,d_-1/2,Q1,Q2); denote the coordinate vectors by e_1,...,e_6. On scalar normal forms,

    n=c0+c1r+Σ_a d_a/(r-a),   a=1,-1,1/2,-1/2,
    ξ[n e1 dr]=(d_1,d_-1,d_1/2,d_-1/2,-c0,-c1/8).           (4)

In n e1, e1 means the first row-coordinate vector of R²; in ξ-coordinates e_i means a vector of K^6. Formula (4) fixes the two different uses explicitly. In particular all six coordinates are complete, not merely necessary observations.

The actual induced map on (3) is the σ-semilinear bijection

    F=diag(p²,p²,p²,p²,p²/β,pβ)σ,                            (5)

where β is the named canonical infinity unit in Z_p*. It is not a freely chosen diagonal entry. The accepted general-perfect theorem below applies to this same β, connection, quotient, coefficient field and σ.

For b∈R² define the actual rank-three row connection

    D_b=[[D,0],[b,0]],  N_b=(R³,d/dr+D_b),
    i(h)=(h,0),  q_b(h,a)=a.                                (6)

The problem is to decide exactly which b admit a horizontal isomorphism from φ* N_b to N_b whose restriction on this displayed kernel is the specified G_φ and whose map on the trivial quotient is some scalar λ∈K*. These are fixed restriction/quotient contracts. This is not a classification of all semilinear structures or their structured isomorphisms.

For nonzero [b dr], the accepted rank-three theorem says that the rank-two kernel is intrinsic and that underlying R-linear differential-module isomorphism types of these extensions are their projective source classes in P(V). We consume that theorem to translate our existence test into underlying extension types; it supplies no prior Frobenius lift.

## 2. Exact actual-ring existence criterion, including an actual inverse

Write v=ξ[b dr]. Every matrix with the displayed kernel restriction and quotient map in Section 1 has the form

    A_(t,λ)=[[G_φ,0],[t,λ]],  t∈R², λ∈K*.                 (7)

Indeed the restriction fixes the top two rows, while the quotient fixes its final column. There is no omitted top-right entry consistent with these contracts.

The pullback connection matrix is D_(b,φ)=[[D_φ,0],[b_φ,0]], where b_φ=φ'σ(b)(φ). Direct multiplication in the original R gives

    A'+AD_b=[[G_φ'+G_φD,0],[t'+tD+λb,0]],
    D_(b,φ)A=[[D_φG_φ,0],[b_φG_φ,0]].

Here λ'=0. Using (2), the horizontal equation is therefore exactly

    L_D(t)dr=Φ(b dr)-λb dr.                                 (8)

If (8) has a weak row solution, (3) gives F(v)=λv. Conversely, suppose F(v)=λv. Then the actual row-oneform on the right side of (8) has ξ-coordinate zero. The accepted assertion (3) is an isomorphism of the complete quotient by L_D(R²)dr; its kernel on the original row-oneform space is exactly that image. Consequently some t in the SAME R² solves (8). This is the actual weak-ring existence step. It does not replace the complete quotient by a formal/local quotient or a list of necessary residues.

For any such t,

    det A_(t,λ)=λp ∈R*,
    A_(t,λ)^(-1)
       =[[G_φ^(-1),0],[-λ^(-1)tG_φ^(-1),λ^(-1)]].          (9)

Both displayed matrices have entries in R. Thus the solution is a genuine invertible horizontal pullback matrix with the required restriction and quotient, rather than just proportional quotient data.

We have proved, for every actual b,

    ∃λ∈K*, t∈R² satisfying the specified lift
      iff ∃λ∈K*: F(v)=λv.                                  (10)

For v≠0 the latter is exactly F-stability of the K-line Kv; λ is then unique for this fixed nonzero representative v. No uniqueness of t is asserted. No coefficient construction, canonical weak primitive, algorithm, convergence-loss bound, finite truncation, precision or cost estimate is provided by this existential use of completeness.

## 3. The complete general-perfect line theorem being consumed

Let d be the exact order of the ACTUAL β modulo p in F_p*. Define

    C_β(k): for every integer j≥0,
            k contains the finite field F_(p^(d p^j)).       (11)

Finite fields here are the unique finite subfields of the fixed k; k need not be algebraic over F_p. We do not evaluate d or replace β by a parameter.

The accepted general-perfect theorem proves that a unit u∈W(k)* with σ(u)=βu exists if and only if C_β(k). It also classifies all stable K-subspaces, and in particular all stable K-lines of the actual map (5):

- If C_β(k) fails, the line set is P³(Q_p) in the finite-four coordinates, disjoint union {Ke_5,Ke_6}.
- If C_β(k) holds, choose such a unit u and put
  w_i=e_i for i≤4, w_5=u e_5, w_6=u^(-1)e_6. Then F is diag(p²I_5,p)σ in this QUOTIENT basis. With T_2=span_(Q_p)(w_1,...,w_5), its line set is P(T_2)=P⁴(Q_p), disjoint union {Kw_6=Ke_6}.

The projective spaces in these statements mean K-lines generated by nonzero Q_p-vectors in the indicated Q_p-space, not all K-lines of its K-span. Distinct Q_p-projective points give distinct K-lines. Forward stability is equality because F is a σ-semilinear bijection over the perfect coefficient field.

This complete classification, including its unit criterion and arbitrary-perfect quantifier, is an accepted input, not a new proof supplied by this appendix. In particular this consumer does not silently substitute the older finite-residue or algebraically closed-residue cases for it.

If u and u' are two allowed units, σ(u'/u)=u'/u. The σ-fixed fraction field is Q_p: Witt coordinates fixed by Frobenius belong to F_p, and inverting p then gives Q_p. Their unit quotient consequently lies in Z_p*. Replacing u by u' rescales w_5 by a Q_p-unit and w_6 by its inverse, so T_2 and the listed line set are unchanged. The displayed basis and individual vector representatives may change. This is not a new geometric gauge or frame.

## 4. Full existence classification and actual representatives

Combining (10) with Section 3 gives the complete list of nonzero projective source classes whose N_b admits the specified lift with SOME quotient scalar in K*.

Case I, C_β(k) fails:

    P³(Q_p) in span_K(e_1,...,e_4),
    together with Ke_5 and Ke_6.                            (12)

Case II, C_β(k) holds:

    P(T_2)=P⁴(Q_p), T_2=span_Qp(e_1,...,e_4,u e_5),
    together with Ke_6.                                    (13)

Both are exact classifications for each fixed arbitrary perfect k under (11), not claims after enlarging its constants. By the accepted rank-three theorem in Section 1, these classify the nonzero underlying R-isomorphism types in this family for which the specified existence property holds. They do not classify choices of the lift on a fixed module up to semilinear conjugacy.

All listed lines have actual weak sources. For v=(v_1,...,v_6), take the original normal form

    b_v=( -v_5-8v_6 r+Σ_(i=1)^4 v_i/(r-a_i), 0),
    (a_1,...,a_4)=(1,-1,1/2,-1/2).                         (14)

Then ξ[b_vdr]=v by (4), including both minus signs and the factor 8. Formula (14) belongs to the same R; it is not a formal source outside the carrier.

In Case I one may normalize the listed generators and quotient scalars as follows:

    v=(q_1,...,q_4,0,0), q∈Q_p^4\{0}:  λ=p²;
    v=e_5: λ=p²/β;
    v=e_6: λ=pβ.

In Case II one may use

    v=Σ_(i=1)^4 q_i e_i+q_5 u e_5,
       q∈Q_p^5\{0}: λ=p²;
    v=e_6: λ=pβ.

Equivalently the last line can be normalized by w_6 with λ=p. All these λ are in K*, and Section 2 supplies an actual R-valued t and invertible matrix for EACH listed b_v. This conclusion uses full actual-image membership, not an additional assumption that b_v itself is a row eigenform.

For a different nonzero representative v=a w with a∈K* and F(w)=λ_w w,

    F(v)=(σ(a)/a)λ_w v.                                   (15)

This is the unique scalar for that representative. Thus the existence property depends only on its projective class. Combining (15) with (8) again gives an actual t for every actual b representing that class, including b that differs from (14) by an L_D-image. This does not give a preferred primitive.

Any projective class outside (12) or (13) cannot have this specified restriction/quotient lift: such a lift would give a forbidden stable line by (8). In particular the old b=(1+r,0) has finite-four coordinates zero, Q1=-1 and Q2=-1/8. Both infinity components are nonzero, so both cases exclude it. This is consistent with the accepted mixed-source obstruction and does not count that old negative result as a new vote.

## 5. Zero class and the exact stopping boundary

The zero class is not a point of projective space. If ξ[b dr]=0, completeness gives an actual h∈R² with b=L_D(h). For every λ∈K*, take

    t=σ(h)(φ)G_φ-λh.                                      (16)

The chain rule and G_φ'+G_φD=D_φG_φ give

    L_D(σ(h)(φ)G_φ)=φ'σ(L_Dh)(φ)G_φ.

Hence (16) solves (8), and (9) is again an actual inverse. Thus the split class allows every quotient λ under this specified restriction contract. No uniqueness of h or t is needed.

The new finite obligation is now closed at author-proof level: the original actual weak quotient and its full stable-line classification give exact lift existence on every class, including actual representatives, a real weak solution by membership, and a real matrix inverse. The resulting positive theorem is existential. This is deliberately not the missing request for an explicit coefficient-level positive primitive.

There is no claim about an integral R0 lattice, ramification, altered D, another φ or a Frobenius power, arbitrary quotient differential modules, all semilinear structures, full automorphism groups, canonical t, geometric extension of the quotient-basis change, period normalization, LC/h_div, or Native/formal authority. No follow-up parameter variant or primitive algorithm is authorized by saving this standard COMPOSE consumer.

## 6. Exact immutable input ledger and personal reading/reuse

These exact old inputs have already been genuinely whole-read and personally Source-bound by this same author in their original authorized phases. No new managed old-file request or old per-body rehash was made for this consumer. In this phase I recovered the following exact locators from my accepted Source38 record/readbacks and reconsulted only the necessary old typed and row contracts. That local reconsultation is not represented as a new whole review, new Source observation, or new independent vote.

1. Actual six-boundary Frobenius F:
   Source 0464ecd04acab1e33dd3a480001ba6b2a3d1677d.
   Path research_notes/owner_goal_20261016/cm24_convergence_new_anchor/actual_boundary_frobenius/CM24_ACTUAL_SIX_BOUNDARY_WEAK_FROBENIUS_JOINT_AUTHOR.md.
   21977 UTF-8 bytes; SHA256 8e5dbe7d89528632b402e5d103925f6f3452ea11b654b7939ac3c68c779f2133; GitOID 9ed8a851e463cc905f8443cebbb1742da96084f8.
   This is the actual original R/D/φ/M_φ, complete same-R quotient and actual action contract. Its joint old construction belongs to 883/F736/BFF with the prior source-normal-form credits retained, not to this new consumer.

2. General-perfect G primary:
   Source 693cfc169ebe6c81b779d1efb587aec406c07dfc.
   Path research_notes/owner_goal_20261016/cm24_perfect_residue_six_class_field_criterion_feasibility_88303d/CM24_ACTUAL_SIX_SOURCE_CONSTANT_FIELD_CRITERION_AND_PERFECT_RESIDUE_CLASSIFICATION_AUTHOR.md.
   17267 bytes; SHA256 2661e665d64a6d950095398dd42e0348271f86dd7e78264d1dd4b3f0f7224d01; GitOID 081b1b6ac5326e533b602ca827454282c47e0b9e.
   Same Source typed interface path research_notes/owner_goal_20261016/cm24_perfect_residue_six_class_field_criterion_feasibility_88303d/TYPED_PERFECT_RESIDUE_ACTUAL_SIX_SOURCE_FIELD_CRITERION_AND_OPEN_SCOPE.json.
   4984 bytes; SHA256 5ced049e1003d7324b66c3f83a6bb8fed2acba700eed0855ff659cff2a152882; GitOID 0ac71383b7b7234318c7ed3b7d05bc3f4c223744.
   The complete arbitrary-perfect theorem, tower criterion and stable spaces/lines are 883's old contribution. I genuinely reviewed its complete unified scope earlier; I do not replace that proof by a finite-field claim or borrow CF's coverage.

3. My original complete G peer evidence:
   Source 1ad373d2be330e790a4a8f7ebe9c6cc019781724.
   Path research_notes/owner_goal_20261016/reviews/cm24_perfect_residue_six_class_nonauthor_4a56e9/CM24_PERFECT_RESIDUE_SIX_CLASS_UNIFIED_FAMILY_INDEPENDENT_WHOLE_REVIEW.md.
   16391 bytes; SHA256 b542d6e4b02e9d9cf6042681ee6d575e308497f01782e236b505c1a8177157ff; GitOID cb9bd33b212c9d0130fca8159f87436b5701268a.
   Its exact context at the same Source is research_notes/owner_goal_20261016/reviews/cm24_perfect_residue_six_class_nonauthor_4a56e9/REVIEW_CONTEXT_ACTUAL_SOURCE_INPUTS_INDEPENDENCE_AND_PERFECT_RESIDUE_FAMILY_SCOPE.json.
   26811 bytes; SHA256 4dc7e8d735bffe58c06fb468004cb3d0378a41deb6340ff68e030d6f632ddf80; GitOID de8062f60dae0d52615352f6b511d497269d584b.
   This proves my old reading/qualification history; it is not my independent review of the present self-authored theorem.

4. Actual rank-three underlying classification:
   Source 324e8b6045e8bfe1d27d543c2a98af306588f907.
   Path research_notes/owner_goal_20261017/cm24_rank3_actual_source_extensions_4a56e9/RANK_THREE_ACTUAL_SOURCE_EXTENSIONS_CANONICAL_KERNEL_AND_PROJECTIVE_CLASSIFICATION_AUTHOR_COMPOSE_V1.md.
   16181 bytes; SHA256 e81c33fc27a3927f9aaea5416a7622dc5c2fe44285ed8d26bfdd355b84780219; GitOID aac29321b28bb6e54d5e29ae47070cdcee409873.
   I authored and genuinely whole/Source-bound this earlier theorem. Its accepted underlying classification is reused, not advertised as having contained Φ. Its nested scalar-End premise is my old E:
   Source 21047d56910b24aac7c99db4ea47a7c53d6c702b;
   path research_notes/owner_goal_20261016/cm24_weak_endomorphism_scalar_4a56e9/CM24_SPECIFIED_WEAK_HORIZONTAL_ENDOMORPHISMS_SCALAR_AUTHOR_COROLLARY.md;
   13645 bytes; SHA256 3210a4ba5a82e79313f3a83d29fd5f56675b41fc2955fc0c3a37ef3e01b0e5f8; GitOID ab7e10cf798d466f212556bd7e5a8d0526931c5b.
   E is a credited nested premise, not a newly imported all-ring theorem.

5. Same-contract mixed-source obstruction and old block-equation credit, not an additional completeness premise:
   CF author Source fba532bc04f53ccd9282da15f9ff8e7a0e23e28b;
   path research_notes/owner_goal_20261017/cm24_rank3_mixed_source_frobenius_obstruction_cf1677/ACTUAL_WEAK_RANK3_MIXED_SOURCE_NO_SPECIFIED_FROBENIUS_LIFT_APPLIED_CONSUMER_APPENDIX_V1.md;
   12293 bytes; SHA256 f1d805450bdb6abe5f158887b46cbeb6d5571842609bf7a6108cea486b4b4ba0; GitOID 51d8d36af73f11cb5a6bd2c694237844624a638d.
   My genuinely complete peer/Source evidence is 396ef7c6b1509ad690b9d33dbe07e9f4c7d4cfe3,
   path research_notes/owner_goal_20261017/reviews/cm24_rank3_mixed_source_frobenius_nonauthor_4a56e9/ACTUAL_WEAK_RANK3_NO_SPECIFIED_FROBENIUS_LIFT_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md;
   15170 bytes; SHA256 8a2e4b982c96ac2a09ae025f60f5d0182c19f663a2f9b44d780e2066b98c4d4f; GitOID c544fc07acedcb4145a16075a3a7a9e77eac44a3.
   That old note did not claim this full positive classification or explicit positive primitive. My present use of exact image membership does not retroactively expand it.

The repository for every Source/path above is awdawmip/enterprise-math; each immutable URL is https://github.com/awdawmip/enterprise-math/blob/ followed by the full Source and exact path. The original old creation-PENDING/UNREVIEWED wording is historical and is not edited by this appendix. Personal prior whole/Source acceptance is the stated later history, not a conclusion inferred from a filename or a lone author's label.

## 7. Construction, qualification and persistence context

After my genuine new CM partial whole report was frozen, but before its Source/ordinary closure, I checked a possible CM0 continuation by occupation metadata only. A already had an independently frozen same-literal CM0 candidate, so I stopped that branch without reading its proof or contributing repair. A narrow search in my own already consumed old LC review did not recover a direct independent-κ constructor; that bounded HOLD is not a global absence theorem, and no stopped LC/h_div/P11 research was restarted.

I then chose this different typed rank-three existence question. Its private candidate and occupation check also began before the CM partial publication was completed. I retained its hand-proof stopping point while executing the authorized short Source transaction; the complete author chat was sent after my own publication postcheck, before A's ordinary receipt arrived. This artifact was saved after that ordinary receipt. Private candidate reasoning and the actual construction of the present classification are NONZERO and belong to me. I first checked occupation only with CF: CF reported no current occupancy and no personally frozen full-class locator, while expressly limiting the old 12293 result to its mixed-source obstruction. CF sent no new proof or repair. The older A rank-three reply had likewise been occupancy only. Neither becomes a new coauthor or independent reviewer through such metadata.

The first two complete author self-reads (5167 and 5321 displayed tokens) caught chronology wording that had put these checks after the CM partial Source/ordinary process and then placed the complete chat after the ordinary receipt. This final text records their actual order. These were author-only context corrections before the first freeze, with no mathematical change and no external repair; the earlier drafts are not claimed to be the final frozen bytes.

I reconsulted the exact actual action and the full general-perfect line theorem from my existing actual receipts, derived the block equation again in the original row type, and paid both directions with SAME-R image membership and an actual inverse. The explicit representatives retain all four finite source positions and the -c0,-c1/8 normalization. The zero class, unique quotient scalar for a fixed nonzero representative, arbitrary-perfect case split and independence of u are included rather than forecast.

This is a standard composition of accepted results with a newly stated actual consumer. It makes no novelty claim. It is worth preserving because the old mixed example left its positive/exhaustive counterpart unasserted, and the present theorem supplies that exact existence interface without asserting an algorithm. It is one appendix, not a family of parameter variants or a new research-count object.

At this creation cut the new author chat and this working appendix have no independent peer verdict and no new author Source. Root's receipt and instruction to preserve it are control facts only. A later reviewer must genuinely consume the complete frozen new proof/context and whatever necessary old theorem scope that reviewer actually lacks, with truthful NONBLIND history. That review cannot be replaced by my old G peer vote or my own rank-three/E authorship. No author ordinary acceptance or future Source compare is prefilled here.

This whole file is to be personally complete-read and once-frozen after creation. Original Source38 publication transaction1 UNKNOWN and its separately authorized successful transaction2 remain preserved in their own administrative record; they are unrelated to mathematical acceptance of this new appendix. No checkpoint39, identity/budget reset, formal Task, Native experiment, scientific program, or parent finalization has occurred. Goal OPEN.

