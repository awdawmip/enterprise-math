# Finite differential SAME-T centralizer and units of the actual rational rank-four W

NONCANONICAL AUTHOR-PROVED APPLIED-CONSUMER CANDIDATE / UNREVIEWED.
Same-family RESULT_ONLY / classical COMPOSE; not a new paper, Tool or Task.
Sole new finite-operator consumer author: CF1677 / EM-FREE-CF1677.
Root supplies preservation/routing authority and zero mathematical votes.
No new author Source, independent technical whole or ordinary acceptance exists at creation.

## 1. Literal carrier, two actual inputs and the statement

Keep the ORIGINAL characteristic-zero K=Frac(W(k)), the original
allowed prime congruent to 13 or 19 modulo 24, F=K(r), and derivative
partial=d/dr. The derivative's constants on F are exactly K.
Use the actual ROW connection from A's fixed rational rank4 whole:

 S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
 D=(2P)^-1[[2S-1,1],[4S-5,-(2S-1)]], omega=1/(r-1),
 D4=[[D,omega I2],[0,D]],
 W=F^(1x4), L4(h)=h'+hD4,
 L4(u,v)=(u'+uD,v'+vD+omega u).                              (1)

The fixed maps are i(v)=(0,v), pi(u,v)=u, and

 N=i pi=[[0,I2],[0,0]], N(u,v)=(0,u),
 N^2=0, N!=0, N'=0, D4N=ND4.                               (2)

The first exact accepted input is A12072:
Source bf42a27f668c94f94f5ad0add71b20088d279312;
research_notes/owner_goal_20261017/cm24_literal_rank4_self_extension_7cda51/
CM24_LITERAL_RATIONAL_RANK4_SELF_EXTENSION_RESIDUE_COMPOSE_WORKING_AND_CONTEXT.md;
12072 UTF8 bytes;
SHA256 ca7f1e584f82d5949ef581259bcca78332b8b85e3cef9ebea86898092b82050c;
Git blob 09b7cd0ec928607a8ffb1dd600ceede037573e6f.
It supplies this literal F/r/row carrier, not an abstract isomorphic rank4.

The second exact accepted input is BFF11686:
Source 2cff10870a5d1258baea7d3fce25a96edcea98fd;
research_notes/owner_goal_20261017/cm24_rational_rank4_end_aut_compose_bff6dc/
CM24_LITERAL_RATIONAL_RANK4_FULL_HORIZONTAL_END_AUT_COMPOSE_APPENDIX_V1.md;
11686 UTF8 bytes;
SHA256 5c71a7891ca7bd30a4cf0510f317372b5b9931e9352061f5d16598f1b226037b;
Git blob fe30b44fd7622a9141f2b249d98c04273a5c6df0.
Its actual full F-LINEAR horizontal-End contract on precisely (1) is

 A'=D4 A-A D4, A in Mat4(F),
       iff A=a I4+b N, a,b in K.                            (3)

This is a complete End algebra, not only an included nilpotent family.
Both exact old objects were genuinely whole-read and personally
Source-bound by CF earlier, with their true technical/ordinary histories.
The unchanged whole and custody are honestly reused. This round only
the necessary literal type, (2)-(3) and exact exclusion clauses were
reread locally. No new old full GET, compare, old-library hash or
somebody else's API is claimed.

The NEW category is the algebra A_fin of ACTUAL K-linear operators

 T(h)=sum_(j=0)^d h^(j) A_j(r), A_j in Mat4(F), d finite,     (4)

with multiplication given by actual composition. It is not the full
set of arbitrary K-linear maps. Derivatives of rational functions
remain in F. Let C_A(h)=hA denote right multiplication by a matrix.
All displayed polynomial expressions in operators below use composition.

We determine the literal SAME-T centralizer
Z_fin(L4)={T in A_fin:T L4=L4 T}
and its units whose two-sided inverse is finite in A_fin. The result is

 Z_fin(L4) is isomorphic to (K[epsilon]/(epsilon^2))[t],
       epsilon maps to C_N, t maps to L4;                    (5)

 Z_fin(L4)^*={c(Id+C_N h(L4)):c in K^*, h in K[t]}.           (6)

In (6) the finite inverse is c^-1(Id-C_N h(L4)). All h are
ordinary finite polynomials. Positive-order units exist, indeed
one in every positive order. This does NOT change the older
F-linear Aut group or compute A's separate PV group/field.

## 2. Actual finite expansions are faithful and composition is closed

The derivative Leibniz formula expresses the composition of two
operators (4) as another finite sum of the same form. Its coefficients
are matrices in F, because F is a differential field. Thus A_fin
really is an algebra of actual operators on W.

We first prove that the expansion (4) is unique as an actual action.
Suppose T(h)=0 for every h in F^(1x4). On the constant standard
rows e_l, this gives e_l A_0=0, so A_0=0. Inductively assume
A_0,...,A_(j-1) vanish. Apply T to r^j e_l. Derivatives of order
greater than j vanish, the lower coefficients are zero, and the
j-th derivative is j! e_l. Hence j! e_l A_j=0 for every l.
Characteristic zero gives A_j=0. This finite induction covers all
coefficients and proves faithfulness, without choosing evaluations,
solutions or a new coefficient ring.

The order of a nonzero T is therefore its largest nonzero derivative
coefficient. L4 is monic of order one, and induction by Leibniz
shows L4^d has highest derivative coefficient I4. No finite power
of L4 is zero as an actual operator.

A matrix coefficient need not be invertible or have nonzero
determinant to be a genuine leading coefficient. That point matters
for the nilpotent coefficients here. We will NOT infer that orders
of arbitrary nonzero matrix differential operators always add.

## 3. Every finite commuting operator is a polynomial with horizontal coefficients

Let a nonzero T have order d and highest coefficient A_d.
Compute (L4 composed with T)-(T composed with L4) using (4).
The h^(d+1) terms cancel. The h^d terms involving A_(d-1)
cancel as well, leaving exactly

 A_d'+A_d D4-D4 A_d.                                        (7)

For d=0 the same formula holds with no lower coefficient present.
Thus commutation implies (3), so A_d=a_d I4+b_d N for a_d,b_d in K.

For any horizontal A, direct differentiation gives
L4(C_A h)=C_A(L4 h). In particular C_N commutes with L4.
The actual operator C_(A_d) composed with L4^d commutes with L4
and has highest derivative coefficient A_d. Subtracting it from T
strictly lowers the order, or gives zero. No inverse of A_d was
used: this subtraction is valid when A_d is nonzero nilpotent.

Continue by finite order induction. Every commuting operator is

 sum_(j=0)^d C_(a_j I4+b_j N) L4^j
      =f(L4)+C_N g(L4), f,g in K[t].                         (8)

Conversely each displayed operator commutes with L4, by (2)-(3),
and belongs to A_fin. This proves equality of the full centralizer,
not merely a constructed commutative subalgebra.

The map from the polynomial algebra in (5) to (8) is injective.
A nonzero polynomial has a highest coefficient a_d+b_d epsilon
not zero in K[epsilon]/(epsilon^2). The corresponding matrix
a_d I4+b_d N is nonzero: the diagonal blocks determine a_d and
the upper-right block determines b_d. Thus the actual image
has nonzero leading derivative coefficient and cannot vanish,
by section 2. Surjectivity is (8). This proves the full algebra
isomorphism (5), including uniqueness of f and g.

The source of the new phenomenon is now explicit: the actual
horizontal coefficient algebra has a nilpotent, unlike the old
rank2 scalar-End SAME-T case. The proof did not transplant that
older scalar conclusion or assume a generic rank4 Schur lemma.

## 4. Entire finite unit group and finite inverses

The word unit means an actual two-sided inverse S in A_fin.
It is not enough that T be a bijection among some K-linear maps
whose inverse might be infinite or outside the finite category.

If T commutes with L4 and TS=ST=Id, then T L4 S=L4.
Multiplying on the left by S gives L4 S=S L4. Thus ANY actual
finite inverse automatically belongs to the same centralizer.
There is no hidden assumption that the inverse was already a
polynomial in L4.

Use the isomorphism (5). If f(t)+epsilon g(t) is a unit,
its image f(t) modulo epsilon is a unit of K[t]. Degrees in
that SCALAR polynomial domain force f(t)=c in K^*.
Conversely, for any finite g in K[t],

 (c+epsilon g)(c^-1-c^-2 epsilon g)=1

in both orders. The same identity holds for the actual
operators because C_N^2=0 and C_N commutes with L4.
Writing g=c h gives exactly (6) and its stated two-sided inverse.

There are no other finite centralizing units. In normalized
coordinates the group is K^* times the additive group K[t]:

 (c,h) maps to c(Id+C_N h(L4)),
 (c,h)(c',h')=(cc',h+h').                                    (9)

This is a statement about the specified commuting finite
differential operators. It is not a classification of all
units of the generally noncommutative A_fin.

For h of degree d>=1 with leading coefficient h_d!=0,
the operator in (6) has leading derivative coefficient
c h_d N!=0, so its order is exactly d. Its inverse has the
same positive order. Products can nevertheless have order zero:
the top matrix coefficients are nilpotent, and the explicit
two-sided formula gives their cancellation. A scalar-style
order-addition argument excluding these units would be false.

## 5. One literal positive-order witness and the category boundary

Take h(t)=t and c=1. The actual finite pair is

 U=Id+C_N L4, U^-1=Id-C_N L4.                               (10)

They are order one, commute with the literal L4 and multiply
to identity in both orders. Their full original-row action is

 U(u,v)=(u, v+u'+uD),
 U^-1(u,v)=(u, v-u'-uD).

The omega term lies in the second component of L4 and disappears
under C_N, so these displayed formulas agree with (1)-(2).
No change of connection or frame is made.

This witness is genuinely not F-linear. For a row h with hN!=0,
the connection Leibniz identity gives

 U(rh)-rU(h)=hN!=0.                                         (11)

Thus it is not an extra member of the older F-linear horizontal
Aut group, and its existence does not contradict that complete
old result. The order-zero part of (6), h constant, recovers
exactly the old F-linear dual-number units; nonconstant h
gives the new finite-differential behavior.

In particular this is neither a PV-field automorphism nor a
representation of a differential-Galois group, a cochain
homotopy class, arbitrary K-linear bijection, infinite formal
inverse or pseudodifferential operator. The carrier is exactly
the rational W and the actual finite category (4).

## 6. Actual coverage, method credit and authorship history

The narrow known-file coverage check was real. BFF11686 section1
states its maps are F-linear horizontal endomorphisms; its end
explicitly excludes degreewise finite differential operators.
I actually reread those clauses and the exact two old type/End
passages. I did not infer absence from a file name or silently
change its category. No exact previously frozen complete SAME-T
finite-operator statement for this W was identified there.

A, BFF and 4A were asked only occupation/held-coverage metadata.
All reported no occupation or personally held full same-scope
locator; their personal coverage remained UNKNOWN. BFF explicitly
confirmed the F-linear scope of his fixed11686. None supplied
a new formula, proof step or repair. This finite check is not
a full-library absence or priority claim. Broad old coverage
and novelty remain UNKNOWN; exact earlier literal coverage
would require REUSE and proper attribution.

Old rank2 SAME-T14300, authored by 4A and genuinely whole/Source
received by me earlier, supplies the established monic
leading-coefficient/order-induction METHOD background. This
appendix gives the complete actual rank4 proof afresh, so it
does not use the old weak-R conclusion as a rank4 theorem.
The new issue is the actual nilpotent coefficient algebra
and its finite units, with (4)'s faithfulness and inverse
category fully paid. No generic Tool is extracted.

A retains credit for the original literal rank4 matrix,
injection/projection, non-split class and N. BFF retains the
complete rational horizontal-End/Aut proof, with its actual
old no-stable-line input and credit. CF's new responsibility
is the finite-differential centralizer/units consumer,
faithfulness/order argument, complete inverse classification
and actual non-F-linear witness. Root supplied no mathematics.

The warm scope freeze was 2026-10-17 10:48:46 UTC. Private
candidate reasoning was already NONZERO, including monic
order induction and possible nilpotent-coefficient finite
units. This is ordinary warm, nonblind paper work, not
zero-construction or blind Phase A. The actual complete
formal proof was then checked against the literal old carrier
and full End contract. No future reviewer received this new
construction before its first persistence/freeze.

The kill is respected: if the exact same finite-operator
classification had already been stated, this would be REUSE.
The known11686 instead expressly excluded it. With its actual
positive End contract, the present proof is a complete
CLASSICAL COMPOSE applied consumer, not a reason to generate
nearby ranks, parameters or independent papers. The unit
does not supply an old LC/functional/rank4 Task caller,
weak-R/cohomology/strictPhi result or Native physical law.

## 7. Actual actor state and pending publication observations

This is the first persistence of this complete new applied
argument, not recovery or modification of an earlier Source.
The actual subsequent full self-reading and byte freeze,
independent technical whole, author Source and ordinary
acceptance require their own observations. The creation
AUTHOR-PROVED words are not an independent verdict.

CF remains original EM-FREE-CF1677, same bare LOCAL/composite
and Source25 lineage, canonical25/108 and no PUBLISH debt.
This work is after that fixed activity cut and is not a
helper26 append. Five formal authority flags remain false;
Goal OPEN and all live STOP/HOLD/UNKNOWN and original
error/CAS histories persist. No identity/RA allocation,
formal Task, new budget or scientific authority is created.

Only hand proof, selected textual reads of two already
known exact old files, and administrative prose/byte IO
were used. No scientific code, coefficient generation,
enumeration, solver, recurrence table, new external
search/API, Native action, helper or Source mutation
was used for this construction. Own actually read
main@67a02007 policy and unchanged CodeV2/ENV/POSIX are
reused; later journal-only/unrelated-project advances
do not change those applicable rules.

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1
