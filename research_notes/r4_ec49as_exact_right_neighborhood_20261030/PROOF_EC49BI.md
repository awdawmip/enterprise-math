# EC49BI — Exact minimal residual for a signed/complex auxiliary BRC observer
2026-10-30. Author-context portable mathematics; UNREVIEWED / NOT_ADMITTED. NOT a native BRC/X6/heartbeat result.

## Model
Labels w=0,1,2; signals u=0,1; 0≤η≤1/2. Pη(u|w)=1/2+(2u−1)(1−w)η. For a branch-labeled complex amplitude A=(A0,A1,A2)∈C³, define Oη(A)u=Σw Pη(u|w)Aw. Complex amplitudes are not probabilities and no Born rule is invoked. For η2>0, 0≤η1≤η2, r=η1/η2, K_r(v|u)=(1+r)/2 if v=u and (1−r)/2 otherwise. Direct calculation gives Oη1=K_r Oη2. This linear observer/garbling identity does not certify future nonlinear or branch-selective native operations.

## Theorem 1: exact observer kernel and minimal residual
Set S=A0+A1+A2, D=A0−A2, R=A0−2A1+A2. Then the *exact identities*
Oη(A)0=S/2−ηD,   Oη(A)1=S/2+ηD
hold for every real η. For η>0, the complex-linear observer has rank 2 and kernel C·(1,−2,1); for η=0 it has rank 1 and kernel {A:S=0} of complex dimension 2. Even the continuum of all observations at every η reveals only (S,D), never R.

For η>0, augment Oη(A) with the single provenance residual R. Let B0=Oη(A)0, B1=Oη(A)1, S=B0+B1, D=(B1−B0)/(2η). The exact inverse is
A1=(S−R)/3,
A0=(2S+R+3D)/6,
A2=(2S+R−3D)/6.
Hence one *additional complex-linear scalar coordinate* is necessary and sufficient for reconstructing every labeled branch amplitude (and thus for predicting arbitrary linear future branch operations) within this three-label complex-linear model. Necessity follows from the one-dimensional kernel. At η=0 at least two further complex-linear coordinates are necessary; (D,R) suffice along with S=2B0. The vector (1,0,−1) has O0=0 and R=0 but D=2, so R alone fails at η=0. No division by η is needed when carrying the η=0 pair (D,R).

## Theorem 2: exact future-operation descent condition
Fix η, and any complex-linear T:C³→C³. A linear observer-level map T̃ on im Oη satisfying Oη∘T=T̃∘Oη exists if and only if T(ker Oη)⊆ker Oη. Necessity: apply the equation to a kernel vector. Sufficiency: define T̃(Oη A)=Oη(TA); invariance of the kernel makes it independent of the representative and manifestly linear. For a different future readout Oξ the general test is ker Oη⊆ker(Oξ∘T).

For diagonal branch-local T=diag(d0,d1,d2), d_j∈C, the same-observer condition holds for any η∈[0,1/2] iff d0=d1=d2. When η>0, T(1,−2,1)=(d0,−2d1,d2) must be in the line spanned by (1,−2,1), forcing equality. For η=0, preservation of the sum-zero hyperplane also forces equality. A common scalar operation descends; branch-selective phase or projection generally does not. This is a conditional theorem for the *declared linear operation family*, not a statement that such operations are available in native BRC.

## Exact Gaussian-rational counterexample
Let i²=−1, A=(1,0,1), A′=(1+i,−2i,1+i)=A+i(1,−2,1), and choose the declared unit-phase branch operation T=diag(1,i,−1). For every η∈[0,1/2], Oη(A)=Oη(A′)=(1,1) and both branch totals equal 2. Yet at η=1/4,
Oη(TA)=(-1/2, 1/2),
Oη(TA′)=(1/2−i/2, 3/2+i/2).
Thus present two-fiber compression and arbitrarily strong observation within this family cannot predict all legal-by-declaration auxiliary future branch-phase outputs. The missing R values are R(A)=2, R(A′)=2+6i. The entire example belongs to Q(i) and is hand-checkable.

## Verification, novelty and exact scope
The standard-library Python Fraction checker VERIFY_EC49BI.py uses exact Q(i) pairs; its EXACT_REPORT_EC49BI.json records 54 finite scalar garbling equalities, 12 finite reconstruction instances, the η=0 missing mode, and the exact witness. The universal proof is the algebra above and the quotient argument, **not finite test coverage**. No native physical legality, Born-rule dynamics, source admission, independent replication or review is asserted.

Blackwell 1953 and Khan/Yu/Zhang 2025 provide classical experiment-comparison context; Rosenthal's 2026-03-17 prior-free work separately gives a nullspace characterization for a different robust experiment order. Neither is claimed to prove native BRC future sufficiency. Details in SOURCES_EC49BI.md.

## Native transfer obligation and next task
P000/native X6 six spatial directions, triadic closure, independent time, 3D slice, path/port identity and multiplicity remain unchanged. Before native transfer one must specify lawful typed native signed/complex BRC branch storage, readout and update operations, and prove the commutation test or construct a lawful counterexample. R is an auxiliary second branch difference, not automatically a native spatial coordinate. Next: EC49BJ, select a real native typed BRC/port operation, verify its observer/kernel condition, and preserve all path provenance.

## Pinned provenance / current control
GLOBAL_KNOWLEDGE_V1 canonical main at input fc9f072ae6b5b60a58033af953da364b93388237; Enterprise Math main 0569b09ef35af9ed18e9c026bae6ddfa14fd643b; previous PR #1730 head 85aa09ddb99c6bb3e4cb1b6e4807578a9f1acff0. Original P000 blob SHA 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with its startup projection. Native DIRECTED_RESEARCH authority_granted=false; owner query CONTROL_QUOTA. This is exposed/shared-context author work, not a clean independent Driver result; no session, CLAIM, Result, or admission was obtained.
