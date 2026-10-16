# EM R5 — Fibonacci–BRC sparse t^7 exact period and repair (UNREVIEWED)

Status: LOCAL_SYMBOLIC_PROOF / UNREVIEWED_DRAFT / NO_NATIVE_CLAIM / NOT_ADMITTED. This is an auxiliary one-step-increment integer-polynomial model, **not** a P000 native six-dimensional Cell dynamics theorem nor a five-port BRC preservation theorem.

Fixed read snapshot: GLOBAL_KNOWLEDGE_V1 main@63106b8fb3f6fd2a0d17f5a4a628050db09fe39d; Enterprise Math main@9d04494d2cc45ae23d3106f6593bd3e3931e0cf0.

Define U_1=1, U_2=1+3t, U_(L+2)=(1+3t)U_(L+1)+t^3 U_L; K_L=U_L U_(L+1), c_d(L)=[t^d]K_L. For L>=3, exact identity:

c_7(L) = 2187*C(2L-1,7) + 81*(2L-3)*C(2L-3,4) + 3*(2L-5)*(2L^2-9L+11).
c_7(1)=c_7(2)=0.

Let y_N(L)=c_7(L) mod 3^N, with future defined by all L->L+k, k>=0.

**Theorem.** For N>=2, the exact minimum positive eventual period of y_N on L>=3 is 3^(N-1), and its unary minimum future-state count for L>=1 is 3^(N-1)+2. For N=1, y_1 is identically zero, with one state. The paired current observation (c_3(L) mod 3^a, c_7(L) mod 3^N), with a>=0, is future-sufficient for y_N if and only if a>=N-1.

**Proof of coefficient formula.** With A=1+3t,b=t^3, U_L=sum_j C(L-1-j,j) A^(L-1-2j)b^j. For L>=3, modulo t^8, K_L=A^(2L-1)+(2L-3)A^(2L-3)b+(2L^2-9L+11)A^(2L-5)b^2. Extract t^7.

**Exact period.** Set g(L)=c_7(L)/3 for L>=3. An exact polynomial identity is g(L)=(2L-5)*(648L^6-7452L^5+34794L^4-85005L^3+116267L^2-86328L+27986)/70. Since 3 does not divide 70, g is in Z_(3)[L]. Mod 3, g(L)=L^3+2L^2+L+2 and g'(L)=L+1; values for L≡0,1,2 are 2,0,2 respectively. For any T, g(L+T)-g(L) is divisible by T in Z_(3)[L]. If 3|T and L≡0 mod3, Taylor's polynomial identity gives v_3(c_7(L+T)-c_7(L))=1+v_3(T), as the derivative is a unit; nonmultiples of 3 cannot be a period even mod 9 by the values 2,0,2. Hence the exact period is 3^(N-1). The L=1 and L=2 initial future strings are distinct from each other and from the tail by the mod-9 prefixes (0,0), (0,6,0) versus the unique tail zero phase (0,6,6); exactly two transients remain.

**Minimal auxiliary precision.** For L>=2, c_3(L)=2L-3+27*C(2L-1,3), with c_3(1)=0. This polynomial satisfies v_3(c_3(L)-c_3(M))=v_3(L-M) for L,M>=2. Thus c_3 mod3^(N-1) identifies all 3^(N-1) tail phases; the two initial rows are distinguished because c_7 at tail residues L≡0,2 mod3 is 6 mod9 while at L=1,2 it is zero. Conversely N=2,a=0 is falsified by L=3,5 (both c_7≡6 mod9; successors ≡0,6). For N>=3 and any a<=N-2 take L=5, M=5+3^(N-2); c_3 agrees mod3^a and c_7 agrees mod3^N since g'(5)≡0 mod3, but c_7(L+1) and c_7(M+1) differ with precise valuation N-1, since g'(6) is a unit.

**Finite independent validation.** An integer-only verifier recomputes U_L coefficients through t^7 for 4,000 consecutive L and checks both c_3 and c_7 against the independent closed forms (8,000 coefficient comparisons). For each N=2..8 it exhausts all tail phase positions (up to period 2187), period bounds and distinct paired current observation keys; checks explicit counterexample for insufficient a. Result: PASS. This is finite crosscheck, not the source of the all-N proof.

**Next unit.** Classify exact maximum current c_7-fiber multiplicity and minimum hidden repair alphabet on Z/3^(N-1)Z with the two initial transient rows included; retain derivative-zero phase L≡2 mod3 and provenance. Formal Researcher registration, live owner, CLAIM, native Result, independent Driver admission remain unverified, so this draft branch is not canonical Source acceptance.