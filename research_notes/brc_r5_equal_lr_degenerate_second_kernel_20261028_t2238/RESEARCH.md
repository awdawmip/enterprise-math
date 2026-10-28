# R5 — Equal-LR nested collisions: exact second-kernel separation

2026-10-28 Asia/Shanghai. Author-side TASK_RESEARCH mathematical derivation; authenticated GitHub account awdawmip. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Frozen scientific and normative input

GLOBAL_KNOWLEDGE_V1 main@cbdd616c4ed89b8bbef3a81631dc7e4a50a74d07; Enterprise Math main@7c27001816f6b439ee320f14d4aa653ffcd1aea8. Read global bootstrap/manual, mathematical/code/BRC/activity policies, ACTIVE worldview and TASK_RESEARCH router; project AGENTS.md, P000 V5, HEARTBEAT X6+time, residual fidelity, joint-relation preservation, portable research protocol and current autonomous operations. Immediate predecessor: research_notes/brc_r5_nested_two_collision_no_go_20261028_t2147/{RESEARCH.md,NEXT_TASK.md}. It excluded a single nonterminal downstream LR s* unequal to its parent LR r. This result resolves the complementary case s*=r with homogeneous first kernels.

Scope: finite N2 two-law sequential statistical observation with source-preserving BRC positive masses, not native X6 dynamics, native three-dimensional slice, or physical calibration.

## Model and theorem

At time 1 two hidden source histories A,B have LR r=P(h)/Q(h)>0 and positive Q arrival masses a,b. All other initial histories are terminal. Both sources have the SAME Q next-signature law q=(q_i) on positive s_i, with sum(q_i)=1 and sum(s_i q_i)=r. Exactly one child LR is nonterminal, s*=r with q*=q(s*)>0; other time-2 children stop. At repeated LR r at time 2, the respective source-specific terminal next-signature laws z_A,z_B on positive t_j both have mean r and positive probabilities. P child laws are s_i q_i/r and t_j z_Hj/r. A full-history policy can distinguish A,B; an unseeded LR policy shares stop/continue/declaration probabilities at each (time,LR). All local behavioral probabilities lie in [0,1].

Observable O=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P), and T_μ the expected stopping time.

THEOREM: Within this equal-first-kernel model, (i) z_A=z_B, (ii) actual all-real image sets O_full=O_LR, and (iii) equality of minimal support values for all signed lambda in R^4 are equivalent. If z_A differs from z_B, a separating lambda can always be chosen of the form (1,c,0,beta) with c,beta>0. For rational data, c,beta can be rational.

Let f(u)=min(u,c), let h=f(r)-sum_i q_i f(s_i)>=0, and j_H=f(r)-sum_k z_Hk f(t_k)>=0 for H=A,B. Select c so j_A>j_B (swap A/B if necessary). Set jbar=(a*j_A+b*j_B)/(a+b) and define

~~~text
beta = jbar                     when jbar <= h
beta = (h+q* jbar)/(1+q*)       when jbar > h
~~~

With lambda=(1,c,0,beta), the exact all-real support gap is

~~~text
inf_{O_LR} lambda·O - inf_{O_full} lambda·O
    = q* a b/(a+b) (j_A-j_B) > 0.
~~~

### Complete algebraic proof

1. Stop-loss hinge separation: suppose z_A != z_B. Their difference d_k has sum d_k=0 and sum t_k d_k=0. The continuous piecewise-linear function H(c)=sum_k d_k min(t_k,c) has derivative sum_{t_k>c} d_k between consecutive signatures. If H vanished at every positive c, every tail sum would vanish and d would be zero. Thus some c among the positive terminal LR signatures distinguishes the kernels. Rational signatures supply rational c. Since f is concave and the conditional mean equals r, Jensen yields h,j_A,j_B>=0.

2. Terminal optimal declaration: for a Q-arrival mass m at likelihood ratio u, declaring Q costs m*u and declaring P costs m*c, so optimized cost is m*f(u). Every one-step delay adds beta*m because lambda_3=0 and lambda_4=beta.

3. At time-2 repeated LR r, the optimized source-H value is f(r)+min(0,beta-j_H). At time 1 the optimized continuation improvement over immediate stopping is

~~~text
F_beta(j_H)=min(0, beta-h+q* min(0,beta-j_H)).
~~~

The full-history improvement is a F_beta(j_A)+b F_beta(j_B). The unseeded LR improvement is (a+b)F_beta(jbar): its shared first action preserves the arriving A:B ratio, since the first kernel q is common; its shared second-stage action sees mean jbar. All other initial terminal states add the same baseline constant. This derivation is valid for every real local randomization, since the linear objective is affine in each stage's decision, and endpoint actions optimize each conditional Bellman step.

4. If jbar<=h, take beta=jbar. Then F_beta(j)=jbar-h-q*(j-jbar)_+. In particular F_beta(jbar)=jbar-h while weighted full improvement has the extra negative term -q*a(j_A-jbar). Since a(j_A-jbar)=ab(j_A-j_B)/(a+b), this gives the claimed exact gap.

5. If jbar>h, take beta=(h+q*jbar)/(1+q*). Then h<beta<jbar. For j<=beta, F_beta(j)=0. For j>beta, the inner branch yields min(0,(1+q*)beta-h-q*j)=-q*(j-jbar)_+. Thus for all j, F_beta(j)=-q*(j-jbar)_+. Weighted full improvement again differs from the pooled LR optimum by q*a(j_A-jbar), the same strict positive gap.

6. If z_A=z_B, the first kernel q is common as well. For any full-history real behavior policy, average all local actions within each (time,LR) fiber using its actual Q arrival masses. Identical kernels transport each averaged continue mass to exactly the original Q mass at every next LR. Because each history's P mass is its LR times Q mass, P flow is preserved too. Inductively all time/declaration outcome totals match under P and Q, hence O_full is contained in O_LR. The reverse inclusion is automatic. This proves equality of actual images. Equality of actual images implies support equality, while heterogeneous z yields the preceding strict support gap. QED.

## Strictly positive rational witness

Time-1 Q arrivals (A,B,O)=(1/4,1/4,1/2) with LRs (3/2,3/2,1/2); corresponding P arrivals (3/8,3/8,1/4). The terminal O state stops at time 1. The common first kernel has child signatures s=(1/2,3/2,5/2) with q=(1/4,1/2,1/4). At s*=r=3/2, the terminal child signatures are t=(1,3/2,2) and the two source kernels are

~~~text
z_A=(1/4,1/2,1/4);
z_B=(1/8,3/4,1/8).
~~~

All Q and induced P transition probabilities are strictly positive and normalized. Take c=3/2, so h=1/4, j_A=1/8, j_B=1/16, jbar=3/32. Choose lambda=(1,3/2,0,3/32). Then

~~~text
V_full = 259/256; V_LR = 65/64 = 260/256; gap = 1/256.
~~~

An actual full-history minimizer continues A and B at time 1, continues A but stops B at the repeated time-2 LR, then optimally declares at terminals, choosing P for ties. The observed vector is O*=(11/32,11/32,31/16,13/8). Since ||lambda||_1=83/32, EVERY real unseeded LR policy has

~~~text
||O-O*||_infinity >= (1/256)/(83/32) = 1/664.
~~~

Hence this strict rational example has different actual images AND different convex hulls: it excludes this candidate from the mother target, which specifically seeks convex-hull equality and actual-image inequality.

## Verification, BRC typing, and frontier

VERIFY.py uses exact Python fractions.Fraction. It checks all P/Q normalizations, 16 full-history deterministic action profiles and 4 LR profiles for the displayed example, as well as 324 additional positive rational models, covering both beta regimes. EXACT_OUTPUT.txt contains its executed output. The theorem for all real policies is proved algebraically; finite enumeration is regression validation of specified instances. No Lean formalization or independent review is claimed.

BRC retains positive Q/P branch masses, source labels, and a source-specific downstream stop-loss gain j_H. Erasing provenance at repeated LR loses a computable signed observer amount q*ab|j_A-j_B|/(a+b). Applying the result to native X6 requires a separate explicit state embedding, readout, and future-operation preservation theorem.

During the run, Enterprise Math native service v0.6.11 returned research_authority_granted=false and 5/5 active control jobs; its current task inventory read failed with CONTROL_QUOTA. Formal owner, CLAIM, Result, and Driver review therefore remain unverified. This GitHub research note is author-side evidence and not formal Source admission.

Next unresolved task: analyze the degenerate repeated-LR chain with *heterogeneous first kernels* q_A != q_B, or two different downstream nonterminal LR signatures. Derive exact joint Bellman support criteria, find signed separation or prove global support equality before studying actual-image nonattainment. See NEXT_TASK.md.
