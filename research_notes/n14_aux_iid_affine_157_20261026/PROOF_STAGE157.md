# Stage157 — external N14 iid exact Bellman optimal interval

**Evidence:** AUTHOR exact-rational finite-model proof, computation assisted. Not an independently reviewed Result, native CLAIM, Lean proof, nor a theorem about P000/X6/Heartbeat.

**Frozen provenance:** GLOBAL_KNOWLEDGE_V1 main@c98c19a23c5dca566b7fe42c933c00b39be93532 (both entry files, Enterprise Math project router, P000 projection matching original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview and relevant mathematical/BRC policy); Enterprise Math initial main@90e8a926574233d61d7e0be2db8ee1358a235b82, consuming Stage156 author proof and current portable research protocol.

## Statement

External ternary iid observations, N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). For any randomized ordered-history stopping/decision policy let eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, and V14(alpha)=min max(tP,tQ) given eP,eQ<=alpha. Count-state (n,a,b) has ratio Q/P=2^(a+b)/3^a.

Previous Stage156 author endpoint:
\[
\alpha_{156}=7319074368089652265/21035720123168587776,\quad V_{156}=5285134543382516317/438244169232678912.
\]

Let k=K157=L157=3342600/10529 and eta157=34752911724120248905/842080912250561737261056. For **EVERY REAL** 0<=delta<=eta157,
\[
\boxed{V_{14}(\alpha_{156}+\delta)=V_{156}-(6685200/10529)\delta.}
\]
The right endpoint and value are
\[
\boxed{\alpha_{157}=763084945158127578305/2192919042319171190784,\quad
V_{157}=3298586218925748578843/274114880289896398848.}
\]
The same supporting line is **strictly nonattainable for all alpha>alpha157**.

## Global exact Bellman bound

At count state s=(n,a,b) compute H(s)=min{ k*2^(a+b)/3^a [decide P], k [decide Q], 1+sum_i P_i H(child_i(s)) [continue] }. Continue is absent for n=14. Exact Fraction recursion over **680 states** produces only two ties: **J=(10,2,0)** decide P versus continue, and **T=(14,0,0)** terminal decide P versus Q. All **1238 nonminimal action gaps are strictly positive**, minimum **232231247/11789784576**, negative count zero. The root value is
\[
H(root)=16797051003483763023587/72098013403919941632.
\]

Any full ordered-history policy obeys H(root)<=tP+k*(eP+eQ)<=max(tP,tQ)+2k*alpha by the exact likelihood-change-of-measure Bellman recursion. Hence V14(alpha)>=H(root)-2k*alpha globally. At previous k156=109612440/326191, the unique midpoint-optimal count policy on [k,k156] is Bellman optimal at both endpoints (allowing endpoint ties); its candidate action gaps are affine in k. It follows that J is the first next closure on **this specified diagonal dual ray**, not a claim of uniqueness among off-diagonal rays.

## Ordered BRC evidence and affine four-observer law

Use exact positive-rational labeled ordered histories, with separate P/Q masses and multiplicities, prior to the iid-specific sufficient count quotient. Let j=P-stop probability at J (otherwise continue) and x=P-decision probability at terminal T (otherwise decide Q). All other actions are strict Bellman minimizers.

Literal ordered integer-weight DFS first-hit counts are **45** histories at J, with P mass **1953125/11943936** and Q mass **1953125/26873856**, and **1** history at T, with P=Q mass **6103515625/78364164096**. The J cone has two occurrences of observation 0 while terminal T is the all-observation-2 path; these cones are disjoint, so the four-observer mixed term vanishes.

Writing M=(eP,eQ,tP,tQ), a conditional iid-suffix Fraction recursion and independently unmerged integer-weight DFS agree at **all four deterministic corners** and yield for all real j,x:
\[
M(j,x)=M_{00}+j\,dJ+x\,dT,
\]
\[
M_{00}=(1220395842171464035/3505953353861431296,\ 
223259694920365/641959232274432,\
5285134543382516317/438244169232678912,\
619867204468061/53496602689536),
\]
\[
dJ=(-3201171875/3962711310336,\
771484375/557256278016,\
-30224609375/165112971264,\
-4150390625/46438023168),
\]
\[
dT=(-6103515625/78364164096,\
6103515625/78364164096,\ 0,\ 0).
\]
The mixed difference M11-M10-M01+M00 is exactly zero. Each ordered J prefix has the same iid suffix laws and Q/P prefix ratio, so history-specific mixing can be averaged without changing exactly these four observers. No signed BRC-amplitude cancellation is inferred.

## Entire real primal interval and sharp endpoint

Solving eP=eQ is exactly
\[
x(j)=660136987826389/327680000000000000-(360279/25600000)j.
\]
Its **whole legal interval** is
\[
0\le j\le j_*=660136987826389/4611571200000000<1.
\]
The terminal coin x decreases from a strictly internal positive value to **x(j*)=0** while the new J-stop coin stays internal. At j=0 the observations reproduce alpha156 and V156 exactly; at j=j* they equal alpha157 and V157. Common error strictly increases affinely by eta157, covering every real alpha in the stated segment.

Endpoint margins tP-tQ are precisely
\[
69060801460053535/146081389744226304>0,\qquad
251826953459549368715/548229760579792797696>0.
\]
They remain positive throughout by affinity. Exact dual equality tP+k(eP+eQ)=H(root) holds at both endpoints and therefore at every real interpolant. The constructed policy meets the global lower bound and proves the theorem with slope 2k=6685200/10529.

For right sharpness, the finite-horizon behavioral policy cube is compact and its observables are continuous. Equality with this same support beyond alpha157 forces both errors to equal alpha (k>0), tP to be the maximal time, and all positive-mass reached actions to minimize Bellman. Strict gaps leave only J and T. Averaging history-specific J coins using common likelihood ratio/suffix distributions produces an effective j in [0,1]; T has one first-hit prefix; cones are disjoint. Thus every support-equality policy has M(j,x). Equality of errors forces the displayed x(j), and x>=0 forces j<=j*. Its common error cannot exceed alpha157. Contradiction. Therefore the supporting line is strict to the right.

## Actual validation, boundaries and next unit

Exact author calculations checked 680 states, 1238 strict gaps, two ties, the first-hit masses, four deterministic corners by two structurally different methods, zero mixed term, precise endpoint compensation, time margins and global dual equalities. The portable VERIFY_STAGE157.py reproduces these using Python Fraction and literal ordered integer DFS (P weight numerators 3,1,20 with denominator 24; Q weights 1,1,10 with denominator 12). certificate157.json preserves exact observables. Storing code is not evidence of remote execution. The proof remains an **external iid finite-model theorem**; it does not establish native six-dimensional Cell dynamics.

Authenticated GitHub actor awdawmip can write; native em_status 0.6.11 reachable, native em_control_tasks returned CONTROL_QUOTA. Active owner, formally authorized researcher CLAIM, frozen Result and independent Driver review remain unverified. This author research note makes no governed ownership claim.

Stage158 open: at Stage157 right endpoint terminal T decides Q surely (x=0), while J's P-stop coin remains mixed. Find an exact **off-diagonal** (K,L) motion preserving J P/continue tie and making T strictly Q (L<K), identify the next Bellman closure and prove a real primal segment or exact obstruction.