# PREFIX-588-R2 — A single exact simplicial cone is invariant for the entire original nonnegative X6-BRC gate family

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR-SIDE PROVED / EXACT ORIGINAL 96x96 INTEGER CERTIFICATE EXECUTED / UNREVIEWED / NOT ADMITTED.
Frozen original scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged.
Predecessor: PREFIX-585 AB/BA source at 5ec3c4c3787fb1e98cc9d8f288cf0d2f28f2efd7; PREFIX-586 exact 96-port inverse, PREFIX-587 integer local combinatorial inverse and 24 simplicial endpoint blocks.
The entire original 48-phase, 96-port, 576-labelled-action source remains the model; no change to BRC provenance or P000.

## Mathematical question and result

PREFIX-587 found a common-parameter-independent candidate positive endpoint cone C with 96 extreme rays. Is the cone preserved by the actual original 96-port BRC transition A(x,z), and is preservation stable under arbitrarily many successive transitions with DIFFERENT nonnegative axis and gate weights?

Answer: YES. An exact *fixed* 96-by-96 integer coordinate matrix W makes the whole nonnegative original weighted family simultaneously nonnegative.

## Original typed construction

Let G_c be the original four-phase set with signed current axis c, for each c in ±1,...,±6. Keep both original branch bits u=0,1. These form 24 disjoint groups of four genuine original 96 ports. In each four-port group put W_block=J_4-I_4 (zero diagonal and all remaining off-diagonal entries one). Let W be their direct sum in original-port order. Then

    W^-1 = direct_sum_{24 groups} (J_4/3-I_4).

The image C=W R_+^96 is exactly the PREFIX-587 native endpoint cone. It is a single parameter-free simplicial cone with 96 extreme rays, independent of all x and z.

The original transition A(x,z) is the exactly marked native 96-port operator, with six original source-axis positive weights x_a and three original gate-labelled actions carrying extra z, as in PREFIX-585. No phase, source axis or branch bit is collapsed.

## THEOREM 588.1 — Universal common positive similarity

For every six-tuple x∈R_{>=0}^6 and gate z∈R_{>=0}, the complete original BRC transition satisfies

    W^-1 A(x,z) W >= 0

ENTRYWISE. Equivalently,

    A(x,z) C ⊆ C

for one and the same fixed 96-ray simplicial cone C.

Proof, route 1 (algebraic). For all x_a>0, the exact original PREFIX-585/586 similarity and its transpose give

    U(x)^-T A(x,z) U(x)^T = A(alpha*x,z)^T >= 0

where alpha=(1 3)(2 4), U=H B(x)^T, and the last inequality is the original nonnegative gate-marked transition for z>=0. On each four-port group G_c with a fixed branch bit u, all four original source-axis weights in the columns of U(x)^T are the same x_|c|. Its columns have three ones and one zero in precisely the W_block pattern, with original source/target index permutation. Hence

    U(x)^T=W Q(x),

where Q(x) is an explicit positive monomial (permutation times diagonal) 96-by-96 matrix. Therefore

    W^-1 A(x,z) W =
        Q(x) A(alpha*x,z)^T Q(x)^-1 >= 0.

This is an exact cone equivalence, not a native gate-labelled action automorphism. W is constant and invertible. As x_a approach zero from positive values and A(x,z) varies polynomially, entrywise nonnegativity extends to all x_a>=0 by continuity without using U(x)^-1 at singular inputs. QED.

Proof, route 2 (finite exhaustive coefficient certificate). Write the original native labelled operator as the exact degree-1/gate-bilinear polynomial

    A(x,z) = SUM_{a=1}^6 x_a A_a + x_1*z*G,

where the A_a are its six ORIGINAL axis-labelled matrices at z=0, and G contains precisely the three marked gate transitions. Define seven fixed original-port matrices

    C_a=W^-1 A_a W,  a=1,...,6,
    C_gate=W^-1 G W.

The complete exact arithmetic verifier computes EVERY entry of all seven 96x96 matrices (7*9216=64512 rational coefficients), proving each is in {0,1}. Their numbers of ones are

    C_1: 93;  C_2,...,C_6: 96 each;  C_gate: 3.

Their supports are disjoint, totaling 93+5*96+3=576. The unweighted sum has exactly six entries one in every row AND in every column. Thus

    W^-1 A(x,z) W =
      x_1*C_1 + ... + x_6*C_6 + x_1*z*C_gate

is manifestly entrywise nonnegative for every nonnegative x,z. This exhaustive integer check of a fully declared finite 96-state polynomial identity independently verifies the exact positive-algebraic construction. QED.

## THEOREM 588.2 — Arbitrary nonstationary products

For any integer n>=0, any sequence x^(1),...,x^(n)∈R_+^6 and z_1,...,z_n>=0, the original BRC product

    A(x^(n),z_n) ... A(x^(1),z_1)

preserves the SAME cone C. Indeed, W^-1 times the product times W is the product of the nonnegative conjugate matrices, with no parameter matching or re-choosing a cone.

This is an unbounded-horizon exact algebraic result for the stated 96-port weighted BRC operator family. The product index is a sequence length of declared operations, not an assumed physical heartbeat duration. The output is an observation-preserving positive linear representation, not a new native 96-port gate-marked graph automorphism.

The common representation also keeps all 576 labelled-action monomials, but their transformed 0/1 supports are an alternative positive observer; it does not identify a physical original-port bijection or an endpoint-unrepaired equality.

## Exact computation

The standard-library certificate constructs original four STARs and the same 48 phases and 96 (phase,bit) ports; W by 24 native group blocks; W^-1 rationally with 1/3. For each original axis unit weight at z=0 and the separate original x1*z gate term, it computes 96x96 rational conjugates. Exact Fractions establish each coefficient is an integer 0 or 1 and all seven supports are disjoint, with 576 total entries and six in/out per port at x=z=1. Additional complete 96x96 regression matrices for six parameter sets, including x=0 and z=0,1,2,7,17,999 and nonuniform x, verify the polynomial expression. Result: ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED.

BRC reuse status: COMPOSE_APPLIED / EXTEND_EXISTING_TOOL. This finding gives a new uniform positive *observer* coordinate for retaining the full original 96-port dynamic path operator. Its cone and all-label coefficient identities are exact within the specified frozen native weighted system. Review and any promotion remain subject to the original project's independent source contracts.

## Smallest next mathematical question

Determine whether there exists an exact, local provenance-preserving interpretation of the seven transformed 0/1 coefficient matrices as actions on a dual **typed BRC port carrier**, retaining the exact original gate and six source-axis observers via W and W^-1. Compare its operation/observer semantics and conversion cost to the original native port action graph. Separately investigate whether the common positive cone yields a new fast evaluation or ranking scheme after accounting for W/W^-1 and reconstruction costs.
