# BRC N=4 / S23 — sharp three-atom obstruction for a fixed nine-decoder bank

Date: 2026-11-01. Research mode: independent author-side portable mathematics; **UNREVIEWED / NOT_ADMITTED**. This is an exact theorem in the six-source statistical S23 model, not a claim about P000 native X6/Cell/time dynamics or a freely redesigned ten-decoder bank.

## Frozen input

Use six positive-weight statistical sources AU0, AU1, AV, BU0, BU1, BV, six preparation inputs, four stopping times, and 11 behavioral controls ordered
`(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)`.
For source x, its lawful distribution is
`(a_g,(1-a_g)b_h,(1-a_g)(1-b_h)c_x,(1-a_g)(1-b_h)(1-c_x))`, with the U second-stage information set shared by AU and BU.

The preparation mixing matrix M=M20/20 is

```text
M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
```

Freeze the deterministic common four-state encoder E grouping (AU0,AU1)->AU; AV->AV; (BU0,BU1)->BU; BV->BV. Freeze the original first nine decoder kernels, in row order AU AV BU BV; each two-digit string ij is a half-half mixture of stop times i,j:

```text
1: 34 24 34 24     2: 34 23 34 34     3: 34 34 34 23
4: 24 24 12 12     5: 12 12 24 34     6: 12 13 23 24
7: 23 34 12 13     8: 24 34 12 14     9: 13 12 13 13
```

The arbitrary tenth kernel D is a row-stochastic 4x4 matrix fixed before the later behavioral policy. Its label may be selected after the policy is revealed but before observing the stopping time. Define p(z)=M F(z), q_D=M E D, L_D(z)=max_i TV(p_i(z),q_{D,i}), and G_D(z)=min(L_1(z),...,L_9(z),L_D(z)).

## Exact result

Three explicitly lawful S23 behavioral policies are

```text
W = (1,0,0,0,1 ; 0,0,0,0,0,0)
H = (1/3,1,0,0,0 ; 1,0,1,0,0,0)
U = (0,0,1,0,1/3 ; 0,0,0,0,0,1/2)
```

The **sharp three-policy minimax identity** is

\[
\boxed{\inf_{D\in(\Delta_4)^4}\max_{z\in\{W,H,U\}}G_D(z)=2/3.}
\]

Consequently, for the **fixed encoder and first nine decoders**,

\[
\boxed{\forall D\in(\Delta_4)^4,\quad
\sup_{z\in[0,1]^{11}}G_D(z)\ge2/3.}
\]

This increases the earlier fixed-nine global obstruction from 11/18 to 2/3. It neither proves a full 11D upper bound for this fixed-nine bank nor changes the unrestricted optimized k=4,6 ten-label problem.

## Analytic proof

The fourth preparation is the equal mixture BU0/BU1. E maps both to the single BU encoding state, so its predicted row for the tenth decoder is always one policy-independent probability vector
`q=D_BU=(q1,q2,q3,q4)`.

The prepared fourth-input targets and original nine-label minima are:

| policy | p_4(z) | min of frozen L1,...,L9 |
|---|---|---|
| W | e4=(0,0,0,1) | 1 |
| H | e1=(1,0,0,0) | 2/3 |
| U | e2=(0,1,0,0) | 2/3 |

Every entry is a rational consequence of the specified matrix, causal controls and original nine rows, checked on all six preparations in VERIFY.py. For any real probability vector q, TV(e_j,q)=1-q_j. Since q1+q2+q4<=1, one of q1,q2,q4 is <=1/3; therefore at least one of W,H,U has L_D(z)>=2/3. At this same z all nine frozen labels have risk >=2/3, so G_D(z)>=2/3. This holds for **every real stochastic** tenth D; hence the full-11D lower bound. The argument preserves the latent source identities until the explicit shared-BU encoder quotient, whose future behavior contrast is the obstruction.

## Sharpness restricted to W,H,U

The following tenth kernel, rows AU,AV,BU,BV, is stochastic:

```text
AU=(1/3,1/3,1/3,0)
AV=(1/3,1/3,0,1/3)
BU=(1/3,1/3,0,1/3)
BV=(2/3,1/3,0,0)
```

Exact evaluation of all six prepared inputs gives
`L_D(W)=L_D(H)=L_D(U)=2/3`. This attains the lower bound **on the displayed three-policy set**, proving the minimax identity.

## Verification, sources and next question

The accompanying Python standard-library Fraction checker reconstructs all six source laws and preparation rows, all nine decoded kernels, 27 fixed-label policy risks, the three target atoms and the explicit matching kernel. The saved output is the actual execution evidence. The universal statement about real D is analytic; the program checks the finite rational witness and upper construction.

BRC interface: the positive-rational latent-source mixture and provenance-preserving grouped encoding from the previous fixed-nine proof are REUSE_APPLIED. Statistical ports are not native spatial axes.

Parent research: PR #1765, immutable prior author-side proof commit `5272933b590d957eba7046d4f99afffe88b2453a`, directory `research_notes/brc_n4_s23_four_witness_two_faces_sharp_11_18_20261101_research1/`. This task's inspected EM control snapshot was `main@a673d9c9852957727a17317b223423451f48f6a1`. GLOBAL_KNOWLEDGE_V1 pinned read was `main@aa0cb116abe430e33dc4db4b8a72210160b5dd97` (P000 projection blob matches canonical P000).

Next: globally beating 2/3 on this k=4 grouping now requires changing at least one of the first nine decoders. Study jointly redesigned ten-label banks with rigorous continuous 11D coverage or an unrestricted lower bound; separately examine k=6 source-resolving encoders. P000 X6/time fidelity, S2 information-set transfer and independent scientific review remain distinct pending obligations.
