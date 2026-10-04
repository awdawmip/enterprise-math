# X6 Euler readout and residual repair — provisional BRC certificate

Date: 2026-10-04. Status: PROVISIONAL / MODEL_PROOFS_AND_FINITE_CHECKS / NOT_FORMALLY_ADMITTED.
Researcher: EM-DIRECT-D32A39 / TASK_RESEARCH. Activity: RA-FBC811D5334B2DE01A596A92.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01 (not platform-attested).
Service session: MCP-77e03ea2598c479f8f3e12bf49314077; genuine registration: kimi-query-bridge#2719, session-20261004-euler-x6-02, SUCCEEDED at Source commit 3cb278b51eb41f1d284ab9174de1e1ac53910782. No CLAIM, formal run or review is asserted.
Prior authored note: global projects/enterprise-math/20261004_EULER_READOUT_INTEGER_LAYER_NOTE.md, blob eff04f440a91aeba7632df4038b1d0c22f1dc469. Earlier enterprise-math#1527 did not establish a service session; status#2718 returned session=null before the proper registration. Historical bytes are retained.

## Source and scope

Global snapshot: awdawmip/chatgpt-global-knowledge@6d4fb42f31697252b6be228f234ba7bec126d52b. Mathematical Source: awdawmip/enterprise-math@165a57caf1050267ea8579ca82d384616341ac55.
Applied P000, ACTIVE worldview, PORTABLE_RESEARCH_PROTOCOL, HEARTBEAT_BRC_ONLY_ARITHMETIC and research_constraints/heartbeat_brc_only.json. Six native spatial axes, the 120-degree native right-angle convention and separate time are unchanged. No native plane or omitted zero coordinate is introduced.

Exact reused sources: definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md (blob ea4cb6eda83ce56fee37830bc04675ee7ea0ee4d), src/enterprise_math/brc_weighted.py (blob 3f205696709e847909958a153f8fe10d3f6b70f0), euler_rotation_refinement.py (blob 55e12f7ffb68a5b241f5d6323f5fde118de2716a). The earlier C3 complex-structure and four-coefficient phase recurrence are not claimed anew. Standard cyclotomic background: SageMath official polynomial-ring documentation gives Phi_12(t)=t^4-t^2+1. No literature-wide novelty claim.

T and U below are newly declared coordinate-automorphism CANDIDATES, not a derived native force/heartbeat law. They preserve the declared raw adjacency and length, but preservation of actual triadic incidence, fields and Cell/gate types is NOT established. Source's existing six-Cell/six-gate incidence cycle is not identified with twelve signed directions merely from equal cardinality. An action application is not a primitive displacement or a physical time interval. Raw coordinate return does not erase history or return time.

## 1. Full-X6 update induces, rather than assigns, phase

Let x=(a0,a1,a2,a3,a4,a5) in the raw Z^6 chart relative to a chosen Cell. Define

T(x)=(-a5,a0,a1,a2,a3,a4).

It permutes signed primitive generators, is bijective and preserves L_E(x)^2=sum(a_j^2). Direct composition gives T^6=-I, T^12=I and (T^3)^2=-I. The orbit of e0 proves exact order twelve. This is an algebraic relation, not a new native angle definition.

Encode x by f_x(t)=sum(a_j*t^j) in Z[t]/(t^6+1). Multiplication by t is exactly T. Factor

t^6+1=(t^2+1)(t^4-t^2+1).

Take the first-quadrant root alpha of Phi_12, so alpha^6=-1, and set rho12(x)=f_x(alpha). Therefore rho12(Tx)=alpha*rho12(x), derived from the raw rule. The exact coefficient output is

c=(a0-a4,a1-a5,a2+a4,a3+a5),

and T sends c to (-c3,c0,c1+c3,c2).

## 2. Kernel, repair and complete integer image

Irreducibility of Phi_12 makes coefficient equality exact. Setting c=0 gives, and is equivalent to,

ker(rho12)={(s,t,-s,-t,s,t):s,t in Z}.

This is two hidden integer degrees of freedom within X6, not extra space. Every T power preserves this kernel, so the differences are invisible to this observer under T alone.

Let beta^2=-1 and rho4(x)=f_x(beta)=h0+h1*beta, with

h0=a0-a2+a4; h1=a1-a3+a5.

T sends h to (-h1,h0). The distinct evaluation at beta may be embedded with beta=alpha^3; it is not the same evaluation as f(alpha). On the kernel h=(3s,3t).

The image of x -> (c,h) consists EXACTLY of integer tuples satisfying

h0-c0+c2 == 0 (mod 3), h1-c1+c3 == 0 (mod 3).

Necessity follows because these expressions are 3a4,3a5. For sufficiency put s=(h0-c0+c2)/3 and t=(h1-c1+c3)/3; then the unique inverse is

x=(c0+s,c1+t,c2-s,c3-t,s,t).

Thus the image has index nine in Z^4 x Z^2. The divisions recover integers; no Cell is divided. The rank statement concerns this additive encoding, not arbitrary nonlinear coding or a bit-complexity lower bound.

## 3. Coordinate intervention reveals the hidden data

Define U(x)=(a0,a1,a2,a3,-a4,-a5). It preserves raw adjacency and length and U^2=I. It changes raw coordinates rather than editing free phase labels. With the above s,t, its exact output is

c'=(c0+2s,c1+2t,c2-2s,c3-2t), h'=(h0-2s,h1-2t).

Generator identities and induction prove that the joint representation preserves every finite word in {T,U}.

Witness: xA=(1,0,0,0,2,0), xB=(-1,0,2,0,0,0). In separate experiments, use the SAME source ID, one branch of positive weight one, and empty history. Both have CWM=(1,1,1), L_E^2=5 and c=(-1,0,2,0). Their h are (3,0),(-3,0). Both squared phase-readout moduli are 3.

After the SAME U, cA'=(3,0,-2,0), hA'=(-1,0), while cB'=(-1,0,2,0), hB'=(-3,0). Squared readout moduli are now 7 and 3. Every positive CWM remains (1,1,1), and every raw squared length remains 5. This is an exact observer contrast, NOT measured intensity, extra mass, energy creation or quantum entanglement.

## 4. Combined invariant and two-observation reconstruction

Define A(c)=c0^2+c1^2+c2^2+c3^2+c0*c2+c1*c3 and B(c)=c0*c1+c1*c2+c2*c3. Algebraic conjugation yields |rho12|^2=A+B*sqrt(3). The implementation keeps the integer pair (A,B) and never evaluates sqrt(3).

Expansion of the integer definitions proves

3*L_E(x)^2=2*A(c)+h0^2+h1^2.

For xA, 2*3+9=2*7+1=15. A is not generally the whole squared phase modulus because B may be nonzero; neither term is physical energy.

For observer rho12 and future alphabet {T}, c is sufficient. For {T,U}, it is not. Safe elimination depends on the specified observer/actions, not solely on the current value.

Given exact coefficient outputs c=rho12(x), u=rho12(Ux), recover s=(u0-c0)/2, t=(u1-c1)/2, then use the unique inverse above. Compatibility requires even differences and u2=c2-2s,u3=c3-2t. Thus these two exact algebraic observations recover all raw coordinates. This does NOT assert recovery from two finite-precision numerical sensor readings or a nondisturbing physical measurement. Four integer coefficients are not a constant-bit complex measurement. No physical resource or speedup bound is proved.

## 5. Actual BRC composition and execution

Retained branch=(source_id, raw X6, positive CWM path state, complete operation word). The finite model declares no additional fields; it does not assert that actual native states have no such fields.

Alternatives are disjoint labelled unions with actual Source cwm_recoalesce=(+,+,max). Serial positive edge v applies the raw T/U map, appends its symbol, and calls actual Source cwm_propagate with cwm_edge(v). Source IDs survive. Algebraic readout is computed AFTER raw transport, never substituted for positive mass.

Observer sum_b w_b*rho12(x_b) is additive on alternatives. A common T edge gives v*alpha times that sum by section 1. General/source-sensitive operations retain per-branch (c,h), not just totals. The proved per-branch inverse and generator identities preserve arbitrary declared finite words. Serial associativity follows from raw-map composition, history concatenation and CWM multiplication. This supplies the scoped extension's composition/readout proof.

REUSE_EXECUTED: the full 9,635-byte brc_weighted.py matches source blob 3f205696709e847909958a153f8fe10d3f6b70f0. Its unchanged dependency-closed CWM AST core is loaded; unused LN/DivisionExpr imports are not executed or stubbed. EXTEND_EXISTING_TOOL: provisional X6 labels and observers. This is not an accepted new family, a whole-repository capability audit, or a full package test.

Actual local finite result: 38,815 assertions passed over all 729 points in {-1,0,1}^6, all 15 words of length <=3 per point, twelve consecutive T actions per point, 24 signed-generator/action checks, 49 kernel inputs with s,t in [-3,3], and all 729 mod3 tuples (81 compatible). Positive serial/alternative and weighted-observer laws were also checked. Source calls: cwm_edge=36677, cwm_propagate=35800, cwm_recoalesce=6. These are assertion/call counts, not independent experiments or an infinite-domain proof; the algebra above establishes the model's universal statements.

No pi, classical trigonometry, matrix exponential, Taylor/Pade/Cayley or high-precision reference runs were used. After a whitespace-only publication formatting change in the extension, the exact publication files were locally revalidated; all 38,815 assertions passed again. This was integrity validation, not a new scientific result or an independent replication.

## Evidence and recovery

The sibling directory 20261004_D32A39_X6_EULER_BRC contains brc_x6_extension.py, check_certificate.py, source/brc_weighted.py, evidence/certificate.json and evidence/execution.log. Run python check_certificate.py inside that directory with Python 3.10+; standard library only. Their recorded Git blob IDs are respectively 1b0e3747af2ea82a7f0f3b2e34f358dcefe70356, fdaf0f102501609505b741696c3da779d99a2407, 3f205696709e847909958a153f8fe10d3f6b70f0, 4c824424b3dc9491e7cbb4e6f966fcf150dcd954 and 463cb99f94dad285de6d1ca8013c3eb0bcb5c1ac.

Publication integrity repair: the preceding 57b116544d77df082893ee9caee1514a1b929794 note had an incomplete evidence capsule; its blob did not match the locally intended artifact. Do not consume that capsule. This replacement publishes ordinary UTF-8 code and evidence together, preserves the mathematical frontier, and does not erase history or claim the defective publication was verified.

Completed: full-X6 T, induced phase recurrence, integer kernel, mod3 gluing/inverse, U witness, invariant, all-word representation, two-readout reconstruction, BRC extension and finite certificate. Not completed: a source-specified native force/heartbeat realization, full triad/field preservation, Cell/gate identification, physical energy/quantum predictions, speedup or independent admission.

Next scientific unit: one exact existing native triadic/Cell-gate action with a type/incidence-preserving intertwiner or an explicit defect. Equal cycle size is insufficient. Do not repeat the C3 result, four-coefficient recurrence, kernel/gluing proof or finite cube checks as new progress. Activity checkpoint linkage/guard remains separate from source storage and is not claimed here.
