# The public Jacobi clock: a common resonance and a nonsaturating signed branch

Status: PURE_SYMBOLIC_RESULT / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

This note examines an explicit factor-blind clock, rather than leaving exponent selection as an unspecified oracle. It uses the regular companion/HBW torus and its primitive signed observer. The mathematics is classical cyclic-group/Jacobi analysis; no global novelty or factoring advantage is asserted.

## 1. A clock obtained from public data

Assume N=pq for distinct odd primes, with regular discriminant Delta=k^2-4 modulo N. Put

    sigma_p=(Delta|p), sigma_q=(Delta|q),
    j=Jacobi(Delta,N)=sigma_p*sigma_q,
    L_p=p-sigma_p, L_q=q-sigma_q,
    E=N-j, d=gcd(L_p,L_q).

The program would know N, k and the actually computed j, and can construct the positive even E by a paid typed operation. The factors, local types, L values and d appear only in the analysis. This requires neither a Blum-prime promise nor knowledge of the prime factors. Computing Jacobi and selecting the clock remain paid operations; this note has not executed either integration.

Each local eigenvalue belongs to the cyclic group of order L_r. Reduction of N-j modulo the two group orders gives

    N-j = sigma_p*(q-sigma_q) modulo L_p,
    N-j = sigma_q*(p-sigma_p) modulo L_q.

Because the signs are units,

    gcd(E,L_p)=gcd(E,L_q)=d.

Thus this public clock selects exactly the same kernel size in the two local tori. A compact exponent of size comparable to N has not independently covered the two unknown group orders: it has exposed their common divisor. The identity is algebraic and does not compute d for free.

## 2. A signed branch that cannot saturate

For a cyclic group of even order L, the equation lambda^E=-1 is soluble precisely when L/gcd(E,L) is even. Here that condition is L_r/d even. The two quotients L_p/d and L_q/d are coprime, so they cannot both be even.

Consequently at most one prime component can have the negative return. The primitive negative main-clock divisor

    D_minus=gcd(N, all entries of M(k)^E+I)

is always either 1 or one proper prime factor. It cannot equal N for any regular k in this squarefree two-prime domain. The marked adjacent observer computes the same ideal through V_E+2 and V_(E+1)+k.

More precisely, if v_2(L_p)=v_2(L_q), neither quotient is even and the negative branch always gives 1. If the valuations differ, only the component with the larger valuation can return negatively. The positive branch can return at both components and has no analogous no-saturation guarantee.

This expands the domain of a no-saturation component beyond the dyadic Blum selector. It does not imply a large hit probability. It also makes no assertion about E+2, a translated scalar union, nonsquarefree moduli or more than two prime factors.

## 3. Exact conditional fibers

Fix a nonempty local type orientation (sigma_p,sigma_q), and choose k uniformly among regular parameters with that orientation. The two local trace distributions are independent and uniform on their respective groups modulo inverse pairing, with the eigenvalues +1 and -1 removed. There are (L_r-2)/2 such local trace parameters.

Since E is even, the positive return has d-2 nonexceptional eigenvalues. The negative return has d eigenvalues if L_r/d is even and none otherwise; neither exceptional root can be negative at this even clock. Therefore write

    a_r=(d-2)/(L_r-2),
    b_r=d/(L_r-2) if L_r/d is even, and 0 otherwise,
    c_r=1-a_r-b_r.

These are exact probabilities of the local labels positive return, negative return, and neither. An empty type orientation, such as the split type at prime 3, is excluded from this conditional law and has zero weight in an unconditional mixture; it is not assigned a zero denominator.

Because b_p*b_q=0, the probability of a proper factor from the negative observer alone is b_p+b_q. If both signed primitive observers are evaluated, a proper factor is obtained exactly when the local labels differ. Thus

    P_both_signs=1-a_p*a_q-b_p*b_q-c_p*c_q
                =1-a_p*a_q-c_p*c_q.

This formula includes the cases where one component returns positively and the other negatively. It does not treat the two signs as independent trials. Each selected observer and any exact factor division must actually be paid by the eventual program.

For uniform regular k conditioned only on j, mix these orientation-specific probabilities with weights proportional to

    C_p(sigma_p)*C_q(sigma_q),
    C_r(+1)=(r-3)/2, C_r(-1)=(r-1)/2,

over the orientations whose sign product is j. There is no reason to give the orientations equal weights. A deterministic k or an adaptive proposal process has a different law.

## 4. Why the large clock is not a generic solution

If d=2, the positive branch is empty in both regular local type families. If the two group orders have the same 2-adic valuation, the negative branch is empty as well. If their valuations differ, its exact hit probability is only

    2/(L_r-2)

at the component with larger valuation. Such a small fiber can remain expensive to hit despite a guaranteed proper result whenever it is hit. Large shared odd factors in d would enlarge the fibers, but selecting or forcing those without knowing the factors is still the unsolved task.

Within a fixed orientation, changing k changes the eigenvalue but not L_p, L_q or d. The public E=N-j clock therefore does not evade the common-resonance restriction simply by trying new parameters of the same type. This is not a lower bound against all BRC/HBW algorithms: other operation languages, observables, curve families and adaptive strategies are outside this one-clock theorem.

The concrete result is a fully public clock with an exact non-saturation branch and a fully specified conditional hit law. It replaces a vague selection proposal with a testable, costable contract and shows precisely which odd-order problem it leaves unresolved.

## 5. Continuation and native integration

The existing typed_jacobi_trace can supply the character label after a linked native discriminant construction. The adjacent-trace binary power program can then evaluate the public E using its ordered pair, without any factor or order input. A successor must freeze its proposal law, actual E construction, chosen signs, rejection/degeneracy outcomes, complete costs and saved evidence before any scientific execution.

No source, input or result from the four-case adjacent-trace run is changed by this note. That run used its fixed predeclared clocks and did not call Jacobi or this public-clock selector. This symbolic theorem is available for any authorized continuation to review or combine with the separate torus square-character tool.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1.
