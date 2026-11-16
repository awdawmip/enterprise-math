# R5 — Exact joint-flow optimum for four-observer LR cube (2026-11-07)

Scientific status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific pins (unchanged): global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Immediate scientific predecessor: fbe407fab76d396f12efd5c79f2283d6a59a7257, research_notes/brc_r5_variable_flow_cube_20261107_t0144/RESEARCH.md. Current normative main is read independently.

## Theorem: exact maximum over one common v

Use the frozen strictly positive four-stage P/Q–BRC probability model, δ=1/4. The original four observables are W=(eP,eQ,TP,TQ), where eQ=Q(declare P), eP=P(declare Q). Let

\[
W_*=\left(\frac{161801}{180000},\frac{6499}{18000},\frac{267}{80},\frac{137}{40}\right).
\]

Consider the **full seedless-LR subfamily with g=u0=1 and u1=v∈[0,1]**. Time-3 continuation probabilities are independently chosen at the three pooled LR keys and all six distinct stopped LR declaration probabilities are independently chosen. For each v write O_LR(v) for its four-observer image. The same v must be held fixed for the entire cube; other probabilities may depend on W.

**Exact optimization theorem (all real strategies and targets):**

\[
\boxed{\max_{0\le v\le1}\ \max\{h\ge0:W_*+[-h,h]^4\subseteq O_{\rm LR}(v)\}=\frac{3543}{3009580}}
\]

attained at

\[
\boxed{v_*=\frac{17741}{21497}}.
\]

Against the preceding proved half-radius 47/40000, the exact gain ratio is 7086000/7072513 (>1). This resolves the optimization over a **single common v** in the stated g=u0=1 subfamily. The unrestricted four-observer FULL_HIST versus seedless-LR image comparison remains the R5 mother problem; allowing v to vary separately by target W is also a different class.

## Frozen probability input and observer equations

The two time-2 LR keys are (3/4,5/4), each with Q mass 1/2. Time-3 keys are (1/2,1,3/2), time-4 keys (1/10,1,19/10). Frozen conditional Q kernels:

    q3[0] = (13/20, 1/5, 3/20)
    q3[1] = (1/40, 9/20, 21/40)
    q4[i,0] = (509/900,382/900,9/900)
    q4[0,1] = (47/180,43/90,47/180)
    q4[1,1] = (67/162,14/81,67/162)
    q4[i,2] = (9/900,382/900,509/900)

Their rows are strictly positive, normalized, and have the entering LR as conditional first moment. The exact verifier checks all those equalities. At time 3 let

\[
V_j=\tfrac12(q3[0,j]+v\,q3[1,j]),\quad 0\le X_j\le V_j.
\]

The pooled LR-shared continuation probability is X_j/V_j; individual history (i,j) continues Q mass (u_i/2)q3[i,j] X_j/V_j. There are six distinct stopped LR keys r∈{1/10,1/2,1,5/4,3/2,19/10}. Let M_r be pooled stopped Q mass and let 0≤E_r≤M_r be Q stopped mass declaring P. Then, with D=eP+eQ−1,

\[
 e_Q=\sum_r E_r,\qquad D=\sum_r(1-r)E_r,
\]

\[
 T_Q=2+\frac{1+v}{2}+X_0+X_1+X_2,\quad
 T_P=2+\frac{3+5v}{8}+\frac{X_0}{2}+X_1+\frac{3X_2}{2}.
\]

Write a=1/10, b=1/2. From the frozen kernel,

\[
 M_a=c_0X_0+c_1(v)X_1+c_2X_2,\quad M_b=V_0-X_0,
\]
\[
 c_0=\frac{509}{900},\quad c_2=\frac1{100},\quad
 c_1(v)V_1=\frac{47}{1800}+\frac{67v}{720}.
\]

## Upper bound: two sharp support inequalities

Any feasible centered cube contains its center W*. Because the total time-3 continuation Q mass is at most (1+v)/2, its center must obey T_Q≤3+v. Thus v≥17/40.

For every such v,

\[
c_1(v)-\frac{c_0+c_2}{2}=\frac{1019v-96}{900(9v+4)}>0.
\]

Define p=TP−[2+(3+5v)/8], q=TQ−[2+(1+v)/2]. Solving the two time equations yields

\[
X_0=\frac{3q}{2}-p-\frac{X_1}{2},\qquad
X_2=p-\frac q2-\frac{X_1}{2}.
\]

Since X1≤V1, the previous coefficient positivity makes M_a and M_b jointly no larger than their values at X1=V1:

\[
M_a\le M_a^*=c_0(\tfrac32q-p-\tfrac12V_1)
+c_1V_1+c_2(p-\tfrac12q-\tfrac12V_1),
\]
\[
M_b\le M_b^*=V_0-\tfrac32q+p+\tfrac12V_1.
\]

At the cube center these expressions become

\[
 M_{a,0}^*=\frac{8737-1661v}{36000},\qquad
 M_{b,0}^*=\frac{5v-1}{20}.
\]

Every legal declaration using all six keys satisfies the two universal inequalities

\[
D\le\tfrac12e_Q+\tfrac25 M_a,\qquad
D\le\tfrac9{10}M_a+\tfrac12M_b.
\]

The first follows because 1−r≤1/2 for every r≠1/10; the second because for all r other than 1/10 and 1/2, 1−r≤0. Both inequalities respect arbitrary real random declarations.

If the cube of half-side h is contained in O_LR(v), its corner t+=(1,1,1,−1) is attained. There D=D*+2h, eQ=eQ*+h, and

\[
M_a^*(t^+)=M_{a,0}^*-\frac{1259}{900}h.
\]

The first capacity inequality simplifies to the necessary bound

\[
\boxed{h\le U_1(v)=\frac{1589-1661v}{185360}}.
\]

The second corner t−=(1,1,−1,−1) gives

\[
M_a^*(t^-)=M_{a,0}^*-\frac{259}{900}h,\qquad
M_b^*(t^-)=M_{b,0}^*+\frac h2.
\]

The second capacity inequality yields

\[
\boxed{h\le U_2(v)=\frac{3(1113v-887)}{80360}}.
\]

U1 decreases strictly and U2 increases strictly with v. Their unique intersection is v*=17741/21497, with U1(v*)=U2(v*)=3543/3009580. Consequently h≤min(U1(v),U2(v))≤3543/3009580 for every feasible common v. This is an **analytic, all-real upper-bound certificate** over the full defined subfamily, including all six stopped declaration keys.

## Explicit construction attaining the bound

Choose the single common v=v*, h=h*. For every real t=(t0,t1,t2,t3)∈[−1,1]^4, set W=W*+h t. Define the affine inverse:

\[
X_2=\frac{81993}{1719760}+h t_2-\frac h2t_3,
\]

\[
E_a=\frac{78158903}{386946000}
+\frac{1181}{902874}(t_0+t_1)
-\frac{1181}{1805748}t_2
+\frac{1181}{1203832}t_3.
\]

Obtain the other masses by the exact equations

    p=TP-(2+(3+5*v)/8)
    q=TQ-(2+(1+v)/2)
    X0=X2+2*(q-p)
    X1=2*p-q-2*X2=V1
    D=eP+eQ-1
    Eb=2*D-(9/5)*Ea
    E1=eQ-Ea-Eb

Set E[1/10]=Ea, E[1/2]=Eb, E[1]=E1, and E=0 at the three other stopped LR keys. For each stopped key with M_r>0, the LR-shared declaration probability is E_r/M_r. At each time-3 pooled LR key use continuation probability X_j/V_j. By direct substitution these recover all four target observables exactly.

It remains to certify legal probabilities. The twelve slack functions are affine in t:

    X0, X1, X2, V0−X0, V1−X1, V2−X2,
    Ea, Eb, E1, M[1/10]−Ea, M[1/2]−Eb, M[1]−E1.

Their exact minima across all sixteen t∈{−1,1}^4 vertices, in order, are

    2119387/12038320
    245657/859880
    552693/12038320
    923197/6019160
    0
    364449/1504790
    535597571/2708622000
    923197/6019160
    0
    0
    0
    46341301/270862200

All are nonnegative. An affine function attains its minimum on the cube at a vertex; therefore all real t, including irrational coordinates and boundaries, produce legal seedless-LR policies. The lower bound matches the upper bound.

## Verification, provenance and continuation

The adjacent VERIFY.py is precisely the Python standard-library Fraction file actually executed for this result. EXACT_OUTPUT.txt is its observed stdout, ending in PASS_EXACT_R5_COMMON_V_COMPLETE_SIX_LABEL_GLOBAL_CUBE_OPTIMUM. Checks cover frozen conditional LR moments; mass normalization; algebraic upper-bound coefficient identities; sixteen vertex slack minima; 625 additional rational targets; and exact reconstruction of all four observers. The all-real result is supplied by the stated algebraic inequalities and affine convexity argument, not inferred from the grid.

The scientific input pins are unchanged. P000 and the ACTIVE Heartbeat World serve as the project's starting frame; this restricted probability model is an explicit typed observer, not a replacement of the native six-dimensional substrate. This result proves observer-specific feasibility only and retains the four-observer/FULL_HIST mother question.

Next scientific route: allow v to vary by W, then consider variable g and u0 while maintaining the same frozen model. For an interior FULL_HIST rational W, test the complete seven-variable K(W) and the residual F=(A+B)J−X1(αA+βB) for a zero or a strict sign over the real LR feasible set. Alternatively independently audit the two sharp support bounds.

Control observation (2026-11-07): GitHub authenticated login awdawmip with repository push permission; native Enterprise Math status, task list and session-start calls returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Active owner, formal CLAIM and independent mathematical admission remain unconfirmed. These files are durable author-side research, suitable for continued review.
