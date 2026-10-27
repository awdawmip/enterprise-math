# Stage207: exact all-real optimum interval (external ternary IID N=14)

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. This proves a theorem about the declared finite IID model, not native P000/X6 Cell evolution, physical time, or BRC-Shor.

## Problem and exact theorem

P=(3,1,20)/24 and Q=(2,2,20)/24 on ordered ternary observations. A policy may use any ordered-history-dependent decision and any real internal randomization, but must stop at time tau<=14 and declare P or Q. Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf over eP,eQ<=alpha of max(tP,tQ).

The previously proved (author-level) Stage206 endpoint is
alpha206=413520058350802705/1168651117953810432,
V206=2181785245548332573/219122084616339456.
For every **real** delta with
0<=delta<=1421036161625/1711891286065152,
including irrational delta,

> **V14(alpha206+delta) = V206 - (2524248916944/11368289293)*delta.**

The exact new endpoint is
alpha207=1243470457111416115/3505953353861431296 and
V207=2141397262877228573/219122084616339456.

## Lower bound for the entire ordered-history policy class

For a particular ordered history h of length n, let a,b count the first two symbol types. Because each branch probability is strictly positive,
rho(h)=Q(h)/P(h)=2^(a+b)/3^a.
For K=1262124458472/11368289293 define the exact finite recursion
B(n,a,b)=min { K*rho(h), K, 1+sum_j P_j B(next_j) },
omitting continuation for n=14. The respective costs correspond to declaring P, declaring Q, and continuing. At every *individual ordered history*, the conditional Lagrangian tP+K(eP+eQ) has precisely these one-step costs after dividing by P(h). By backward induction and the convexity of randomized choices, even a rule depending on the full word has cost no smaller than this Bellman value. Therefore
tP+K(eP+eQ)>=B(0,0,0)=H207,
H207=6891276038721445301535256357/77845101512617870328070144,
and hence V14(alpha)>=H207-2*K*alpha whenever each error is <=alpha.

Exact Fraction enumeration exhausts sum(n=0..14) binomial(n+2,2)=680 count states; there are 1238 strict positive alternative-action gaps, minimum 169734458831/14733302923728, and *only* two ties:
Y=(4,0,1), announce Q / continue; Z=(14,0,0), announce P / announce Q. The count quotient is used for the IID suffix minimizer, but the universal inequality is proved per ordered history, so count restriction is not imposed on competing policies.

## Exact primal witness and zero interaction

At Y, declare Q with probability u in [0,1], otherwise continue. At Z, declare P with probability z in [0,1], otherwise Q. All other states use the unique Bellman minimizer. Let O(u,z)=(eP,eQ,tP,tQ).

No ordered history may visit both ties: Y has symbol-1 count b=1, whereas Z has b=0, and a count never decreases; Z is terminal and cannot precede Y. The mixed u*z coefficient is thus identically (0,0,0,0), not merely numerically small.

Exact conditional Fraction suffix DP and independent unmerged ordered-history integer-weight DFS agree on four deterministic corner vectors (298360 DFS nodes total). Subtracting the stored corner vectors gives

O(u,z)=O0+u*DY+z*DZ,

O0=(647615499226350899/1752976676930715648, 36190470936649/106993205379072, 2181785245548332573/219122084616339456, 83581016151245/8916100448256),

DY=(585383004625/95105071448064, -7514474375/1671768834048, -6573564887875/35664401793024, -41252400875/139314069504),

DZ=(-6103515625/78364164096, 6103515625/78364164096, 0, 0).

Solving eP=eQ uniquely yields the exact affine coin
z(u)=164012470200881049/819200000000000000+(218780590119/3200000000000)*u.

The inequalities 0<z(0)<z(1)=220020301271345049/819200000000000000<1 hold exactly, so this is a legal policy for every real u in [0,1]. Its common error is
alpha(u)=alpha206+(1421036161625/1711891286065152)*u,
a strictly increasing affine bijection to the asserted interval. The P-time minus Q-time is affine and strictly positive at each endpoint: respectively
127698192615335453/219122084616339456 and
152194626194087453/219122084616339456.
Hence max(tP,tQ)=tP throughout. The policy uses only Bellman minimizers and has both errors exactly alpha(u), therefore
tP(u)+2*K*alpha(u)=H207.
It attains the universal lower bound at *every real* alpha(u). At u=0 both alpha and value match the exact Stage206 endpoint; at u=1 they equal the stated Stage207 endpoint. This completes the full-real proof without rational-grid interpolation.

## Strict-right support and Stage208 dual candidate

An exact first-switch scan at K207 yields
K208=19224/175 < K207,
H208=168140201472112396231/1917318240392970240,
with the first new tie (11,3,1) P/continue and terminal Z P/Q, 680 Bellman states, 1238 strict gaps, minimum 3757/340200. It verifies exactly
H208=H207+2*alpha207*(K208-K207).
Consequently, for every alpha>alpha207,
V14(alpha)>=H208-2*K208*alpha
=H207-2*K207*alpha
+(4655573727936/1989450626275)*(alpha-alpha207)
>H207-2*K207*alpha.
This is strict-right separation of the *fixed Stage207 supporting line*, not a Stage208 primal optimality claim.

## Reproducibility, BRC observer boundary, and scope

The complete rational witness certificate, all four corner vectors, the exact Bellman reference program, next dual scanner and observed author run logs accompany this proof. The original executed source and independent arithmetic audit are preserved in the current-turn portable evidence archive. The program uses only integer/Fraction operations. Ordered branch identity and multiplicity, and distinct positive P/Q path masses, are retained by the full DFS. Count compression is justified only for this finite IID future law, four specified observers, and stated stopping operations (BRC provenance/observer discipline). No X6 embedding/readout with future-operation preservation has been established; there is no native P000 result.

Frozen current read pins: GLOBAL_KNOWLEDGE_V1 main ecd9a62fddac9d34492c57cf902c9c119f4e58c1; Enterprise Math main 34b47b6cc01bfebcfaa61aaaefd1e41f5ee3d92a; P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; Stage206 immutable parent 922f12df5041fcec793b0dc7c604857323f1e324. Native owner query returned CONTROL_QUOTA and provided no current owner. This is author-side evidence; no native CLAIM, Source Result or independent Driver acceptance.

**Next precise question:** Stage208 at K208 and ties (11,3,1) P/continue, (14,0,0) P/Q: compute ordered four corners, mixed term, feasible all-real equal-error witness, expected-time dominance, next optimal segment/obstruction, with exact verification. See NEXT_TASK_PACKET_208.md.
