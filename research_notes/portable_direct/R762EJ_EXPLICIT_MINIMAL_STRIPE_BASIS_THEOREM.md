# R762EJ — Explicit minimal stripe basis for the integral BRC null-lattice quotient

Date: 2026-11-18. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Author: EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Review: NOT_REVIEWED.

Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000) and immutable taskbook @e3f42efac29a2da2d95be391f3231a664e2fade0. Antecedents: R762ED (PR #2705), R762EF (PR #2707), R762EI (PR #2714), all author-proved / NOT_REVIEWED. This is a terminal, positive six-branch BRC observer theorem, not a signed-native Cell/Link/Port admission.

## Definitions

For any a>=1 put q=3^a, G=(Z/qZ)^3, R=Z[G], P=1+X+Z+XY+YZ+XYZ, K=ker_Z(m_P), and I=K_A R+K_B R+K_C R+K_D R with the integer annihilators of R762EF. R762EI gives the **inherited hypothesis** K/I=(Z/3)^(4q-8), in particular 3K subset I.

For each coefficient location g=(x,y,z), let ell_J be modulo q and m_J modulo 3, with

| J | ell_J(g) | m_J(g) |
|---|---|---|
| A | x | y+z |
| B | y | x-z |
| C | z | x+y |
| D | x-y+z | y+z |

For each t in Z/q define the integer coefficient function

    B_(J,t)(g) = 1_(ell_J(g)=t) * (1_(m_J(g)=0) - 1_(m_J(g)=1)).

## All-q theorem: explicit minimal basis

(1) Every B_(J,t) is integrally annihilated by P, so belongs to K.

(2) Remove precisely the eight index pairs

    E = {(A,0),(A,1),(A,2),(B,0),(B,1),(C,0),(C,1),(D,0)}.

The remaining **4q-8 explicit residue classes** [B_(J,t)], (J,t) not in E, form an F_3 basis of K/I, for **every** q=3^a, a>=1.

Consequently each k in K has a unique coordinate vector lambda_(J,t) in F_3^(4q-8) such that k - sum lambda_(J,t) B_(J,t) belongs to I. A quotient normal form is obtained by exact finite-field linear algebra, without a fresh Smith normal form for each k.

## Proof

**Integral annihilation.** R762EI realizes integer translates of the R762EF annihilators as A_(J,t,b)=3 H_(J,t,b)-L_(J,t), where H_(J,t,b)=1_(ell_J=t,m_J=b) and L_(J,t)=1_(ell_J=t). Both A_(J,t,0) and A_(J,t,1) belong to I and are annihilated by P; A_(J,t,0)-A_(J,t,1)=3 B_(J,t). The integral group ring is Z-torsion-free, hence P B_(J,t)=0.

**Injection into a small finite-field carrier.** Define V_0=I mod3 in F_3^G. Since each A_(J,t,b) mod3 equals -L_(J,t), V_0=span {L_(J,t)} and R762EI proves dim V_0=4q-4. Reduction induces an injective map rho:K/I -> F_3^G/V_0. Indeed, if k mod3 is in V_0, choose i in I with k-i=3r. Since k and i are killed by P, torsion-freeness forces r in K. The inherited 3K subset I then gives k=i+3r in I.

**Generation.** At m=0,1,2 the contrast (1_(m=0)-1_(m=1)) is (1,-1,0), equal to 1+m modulo3. Hence rho(B_(J,t)) agrees modulo V_0 with L_(J,t) m_J. Let W_q=span_F3 {L_(J,t), L_(J,t)m_J}. The universal rank lemma from R762EI establishes dim W_q=8q-12, so the B-classes span a (8q-12)-(4q-4)=4q-8 dimensional subspace. This equals dim K/I; injectivity makes all 4q B-classes generators.

**Exactly eight relations.** A relation sum_(J,t) g_J(t)[B_(J,t)]=0 is equivalent via rho to existence of f_J:Z/q->F_3 satisfying the identity

    sum_J [f_J(ell_J) + m_J g_J(ell_J)] = 0 in F_3^G.

The relation-descent lemma in R762EI proves each such g_J is 3-periodic, with zero carry coefficient, and all relations descend from q=3. At q=3 the complete space of possible g quadruples has dimension 8; the following eight rows are an explicit reduced-row-echelon basis. Each three-digit string gives g_J(0),g_J(1),g_J(2), repeated periodically for q>3.

| Row | g_A | g_B | g_C | g_D |
|---:|:---:|:---:|:---:|:---:|
| 1 | 100 | 001 | 002 | 011 |
| 2 | 010 | 001 | 002 | 020 |
| 3 | 001 | 001 | 002 | 002 |
| 4 | 000 | 102 | 000 | 021 |
| 5 | 000 | 012 | 000 | 012 |
| 6 | 000 | 000 | 102 | 021 |
| 7 | 000 | 000 | 012 | 012 |
| 8 | 000 | 000 | 000 | 111 |

The companion code includes explicit f_J witnesses and checks all eight equations at every point for q=3,9,27. Algebraically, because the f/g equations only involve residues modulo3, the q=3 equations lift verbatim to every q=3^a. The restriction of the eight rows to columns E is the identity matrix, so those eight classes can be uniquely eliminated. Since the full relation space has dimension 8, the 4q-8 remaining classes are independent and form a basis. QED.

## Exact quotient-coordinate algorithm

Given integer k in K, solve modulo3:

    k mod3 = sum_(J,t not in E) lambda_(J,t) (B_(J,t) mod3)
                 + sum_(J,t) mu_(J,t) L_(J,t).

The lambda vector is unique, whereas mu can be nonunique because the L families have four dependencies. The injection argument above certifies that the corresponding integer remainder lies in I. This is a finite deterministic method; no unproved complexity improvement is claimed.

## Verification and limits

R762EJ_VERIFY.py checks q=3,9,27 exhaustively with exact integer P-annihilation for all 4q stripe generators, and exact F3 ranks rank(L)=4q-4, rank(L,B_keep)=rank(L,B_all)=8q-12; it verifies eight explicit f/g witnesses pointwise and independence of the eight omitted-index columns. JSON evidence is in R762EJ_EVIDENCE.json. Finite checks support but do not establish the all-q conclusion, which is proved relative to inherited R762EI/R762ED/R762EF.

Next questions: independent proof review of inherited zero-locus and quotient lemmas; a structured fast solver for the sparse quotient normal form; exact coefficients of membership in I; native TRIADIC_CLOSURE_E signed-event licensing and V17/V29/V39 transports. P000, six-dimensional native space, three-dimensional research slice and frozen source pins are unchanged.

Status: AUTHOR_PROVED_CONDITIONAL_ON_R762EI; exact author verification PASS for q=3,9,27; independent review NOT_REVIEWED; no Result/Foundation/native event acceptance.
