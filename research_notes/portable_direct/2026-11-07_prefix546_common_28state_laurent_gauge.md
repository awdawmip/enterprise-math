# PREFIX-546 — A single 28-state Laurent-gauge operator for all three rooted BRC signs

Date: 2026-11-07. Independent-author research note, Enterprise Math / RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen scientific source: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessor: PREFIX-545 at dd9f068d02cddf62783e553de974ab4d682df9e8.
Current behavioral context read from GLOBAL_KNOWLEDGE_V1 main@b487e9d4c6707885efddff80e4c75f8fc352b26c and Enterprise Math main@91ec9d893bba99e33bb129ce079b1f5f29e971ff.

## Frozen model and precise question

The four STAR triples are A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6). The model has 48 directed phases, 144 legal directed phase edges and 96 (phase, preceding-branch-bit) boundary ports. Each port has six labeled transitions. The gate target is T=(A,+L1,-L3), with gate increment g(b,j,c)=1 iff b=c=INNER and j=T. Let sigma(i) be the first-axis phase sign in {-1,0,+1}. For fixed original rooted sign r, the BRC cocycle used in PREFIX-539 and PREFIX-544 is

    tau_r(i,j) = (|sigma(i)|+|sigma(j)|-|sigma(j)-r|+|sigma(i)-r|)/2.

Write M_r for the 96-port weighted matrix over Z[q,z], with each allowed labeled transition weighted q^tau_r z^g. The question is whether the three r-dependent 28-state scalar quotients from PREFIX-545 can share one exact operator, instead of just three equal-sized but separately constructed operators.

## Theorem 1 — Exact 96-port Laurent-gauge equivalence (all path lengths)

For r in {-1,+1}, define h_r(i)=-[sigma(i)=r] and h_0(i)=0; D_r is diagonal on the 96 ports with entries q^h_r(i). Over Z[q,q^(-1),z],

    M_r = D_r M_0 D_r^(-1)    (r=-1,0,+1).

Proof. For every sign s in {-1,0,+1} and r in {-1,+1}, |s-r|-|s| = 1-2[s=r]. Substitution into the displayed tau formula gives tau_r(i,j)-tau_0(i,j)=h_r(i)-h_r(j). The gate exponent g is independent of r. Thus the identity holds on every labeled edge, and hence after addition over edges with the same endpoints. It is an identity of the full matrices and extends to powers of every nonnegative integer length. In particular every cyclic labeled port walk has identical total BRC and gate monomial weight for all three rooted signs.

## Theorem 2 — The same 28 classes, and a common weighted quotient (all lengths)

For a fixed root sign r, ports u and v are scalar-continuation equivalent when e_u^T M_r^d 1 = e_v^T M_r^d 1 for all d>=0. The complete finite symbolic certificate proves that all three root signs induce **exactly the same 28 equivalence classes** of the 96 ports. The class size multiset is {1:2, 2:9, 4:15, 8:2}. Each class is homogeneous in sigma; the classes split into 2 of sign -1, 21 of sign 0 and 5 of sign +1.

Finite proof obligation and discharge. For each r, compute exact Z[q,z] fingerprints at depths 0..5 (with arbitrary-size integer coefficients). The resulting 28-class partitions agree port by port. On all 96 ports, group every one of the six outgoing edges by target class and q,z monomial, and verify exact equality of the resulting weighted row within each class. Thus each partition is a weighted bisimulation with a well-defined 28x28 quotient Q_r and the scalar continuation polynomials agree inside classes at every depth by induction. Distinct classes already differ by depth <=5, so these are exactly the scalar equivalence classes. The finite enumeration is exhaustive over the stated frozen 96-port transition table.

Let s(C) be the sign of a quotient class C, and define diagonal B_r(C,C)=q^{-[s(C)=r]} for r=+-1, B_0=I. Since the sign is constant on classes, each quotient edge from C to E gets q^{h_r(C)-h_r(E)} times the r=0 weight. The executable independently checks this transformation on all 28 quotient rows for r=+-1, establishing

    Q_r = B_r Q_0 B_r^(-1).

Consequently Q_0 is a single universal 28-state Laurent-gauge operator for these three rooted observers, with a fixed graph and class map. Q_r have identical characteristic polynomials and traces of powers over Q(q,z). This is matrix similarity, rather than a claim that an unweighted class permutation is required.

## Corollary — Exact three-terminal-vector recovery

Let t_0(C)=1. For r=+-1 set t_r(C)=q^[s(C)=r]. For every original boundary port v and every depth d>=0:

    F_v^(0)(d) = (Q_0^d t_0)[class(v)],
    F_v^(r)(d) = q^(-[s(class(v))=r]) (Q_0^d t_r)[class(v)]    (r=+-1).

Proof: F^(r)(d)=M_r^d 1, then apply the 96-port and 28-class gauge identities and B_r^(-1) 1=t_r. Although Laurent factors appear in the intermediate identity, the recovered polynomial has nonnegative q,z exponents. All 48 rooted starts with either initial branch bit are recovered from the same weighted Q_0 operator and three initial terminal vectors. This shares structural preprocessing; a full implementation performance comparison remains a next research unit.

## Exact execution certificate

Companion file PREFIX546_gauge_common_quotient_certificate.js is self-contained, JavaScript V8/Node-compatible, using BigInt exact polynomial coefficients. It was actually executed with maxDepth=16 and returned ALL_CHECKS_PASS. Exhaustive checks: 192 port membership comparisons for common partitions; class-sign homogeneity; 1152 labeled 96-port gauge edge comparisons; 56 quotient gauge row comparisons; 4896 full polynomial comparisons over all 96 ports and three signs for depths 0..16, independently propagating 96-port matrices versus a common 28-state operator with terminal vectors. The theorems for all depths use algebraic identities and exhaustive finite row congruence, not numerical extrapolation. No Lean check or independent review was performed.

## Next discriminating question — PREFIX-547

Implement one universal Q_0 batch executor for all 48 fixed roots and both initial branch bits, accounting for shared class-map construction, three terminal vectors, propagation, output recovery, coefficient memory, and initialization. Benchmark it against the established 49-coordinate sparse transfer on identical exact BRC--gate observables. Explore multiaxis BRC joint observers with the required native path and Cell provenance retained.

Research status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE_CERTIFICATE / BIGINT_CROSSCHECK / UNREVIEWED / NOT_ADMITTED. The native Enterprise Math MCP status/session/task calls returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; no new formal Researcher-ID, Owner confirmation, CLAIM, Result or Review.
