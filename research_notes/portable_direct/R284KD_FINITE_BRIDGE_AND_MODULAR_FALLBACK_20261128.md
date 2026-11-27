# R284KD — Complete finite real-root bridge and interval/modular integer exclusion to d=3000

2026-11-28. Author written proof plus executed bounded interval and exact modular computation; NOT_REVIEWED. Ordinary auxiliary arithmetic of the R284 observer, not native spatial attribution. Own metadata recovery r1-20261128-0755-own-recovery succeeded, original registration r1-20261124-0256-r284gd-session-v1, EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4, no own RUN. LEASED inventory r1-20261128-0755-owner-inventory-v1 SUCCEEDED, as of 2026-11-27T23:56:23.438212Z no LEASED rows. No shared task mutation. Global main immutable entry snapshot e1bcecdb55f8da73998ef466a409e471d36854a1; P000 V4/V5, ACTIVE worldview, joint/residual and portable contracts consulted. Current normative control and frozen science are separate.

Frozen scientific sources:
- KC 52028797f285dc23fcdad50a3f52f9d3d2fa5bea:research_notes/portable_direct/R284KC_CENTERED_SCALE_AND_REAL_UNIQUENESS_ONSET_20261128.md (author proof, d>=600).
- KA 2ec462057a7401092c3627c153787deef3f1024f:research_notes/portable_direct/R284KA_EFFECTIVE_JOINT_SCALING_AND_FINITE_JET_REMAINDER_20261128.md (exact division-free normalized carrier).
- JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md (all integer budgets for 3<=d<=80; read theorem and carrier; prior exact computation not repeated).

## Theorems

A. For each integer 81<=d<=599, the original cross residual C(q,d) has exactly one simple real zero on the entire legal real budget interval q>=d^2/4, with C positive below and negative above. Together with frozen KC this proves the same assertion for every integer d>=81.

B. For each integer 81<=d<=3000, and every integer q>=max(64,ceil(d^2/4)), C(q,d)!=0. Together with frozen JR this covers every integer 3<=d<=3000 with no upper budget bound. Thus qK(q,d)!=32/3 on that scope by JR's necessary cross-residual equality. The finite calculation uses KC for d>=600, not an independent global real-root proof on that tail. The d<=80 real-root statements retain JR's exact interval starting at ceil(d^2/4) (or 64). No claim of excluding all d>3000 is made.

## 1. Exact joint carrier and recurrence

Use KA: h=1/d, s=d^2/q, x=k/d, y=1-x. For lambda in {1,2}, R_(lambda q+d)(0)=1 and the recurrence multiplies by
(1+(d-i)s/(lambda*d^2))/(1+(d+i+3)s/(lambda*d^2)).
Let f_k=R_(q+d)(k) R_(2q+d)(d-k). Store both complete prefix arrays. Define t=s h^2/(1+sh), r=s/(1+sh), T_k=s(y^2+hy/2)/(1+(s/2)(hx+h^2)),
G=[(3/2)r-(x^2+2xh)r^2]/[2(2+t)].
Let vv=(x+h)(y+h)f_k and jj=(x+h)(1-T_k)f_k. Then v=h sum vv, j=h sum jj, g=h sum G(2vv-h jj), b=v-hj, a=(v+b)/4+h^2g.
The full endpoint is
e=R_(q+d)(d)(2+3h)/(2(2+2sh+sh^2))*(2+sh+2sh^2)/(8+4sh+2sh^2).
With P1=24s(3+h)+3s^2 h(3+h)^2, P=48+hP1, T1=32s(1+h), TT=96+hT1, the exact residual is
F=C/(q^3 d^5)=-24aj-96hag+P1ab-T1a^2+hPeb-TT[2ash(v+b)+s^2 h^3(v+b)^2].
At s=0 use the same rational continuation, including endpoint. These identities preserve the signed joint difference and full endpoint; no asymptotic approximation is used in the finite bridge.

## 2. Rigorous interval and derivative propagation

The executed implementation uses IEEE binary64 interval endpoints with explicit outward padding, not an unbounded floating-point approximation. Under round-to-nearest, for an elementary finite operation with rounded result z, the exact result differs from z by at most 2^-52|z|+2^-1073 (a conservative bound including subnormals). The code pads each computed endpoint by p=RN(2^-50|z|+2^-1000), and rounds z-p or z+p. The padding exceeds the original rounding error plus rounding of the pad and the final addition/subtraction: for finite nonoverflowing magnitudes, each of the latter errors is bounded by 2^-53 times its magnitude plus a subnormal ulp. Thus the padded interval encloses the exact endpoint. All computed endpoints here are finite (assertions remain enabled); there is no overflow in this bounded calculation. The explicit absolute term covers small and zero endpoints. Compilation disables fast-math and floating-point contraction. Integer constants used in the executed range are exactly representable, and noninteger rationals are formed with interval operations. Interval division asserts positive denominator lower endpoints and multiplies by enclosed reciprocal endpoints.

For derivative enclosures use pairs (v,t) with interval v enclosing value and interval t enclosing derivative at every s in the input box. For products t=(v1*t2+t1*v2), for quotients t=(t1-(v1/v2)*t2)/v2; all arithmetic is interval arithmetic. Start with the variable pair ([a,b],[1,1]) and constants with derivative zero. Induction through the full recurrence and joint carrier encloses F and F' on each complete box. In particular no numerical differentiation or smooth interpolation is assumed.

For each d=81..599, adaptively split the three closed intervals [0,3/4], [3/4,5/4], [5/4,4] at exact dyadic midpoints until respectively upper(F)<0, lower(F')>0, lower(F)>0. At depth <=30 all endpoints are exactly representable; an unproved box aborts, never counts as covered. The executed complete cover has 12174 strict sign leaves and 2076 strict derivative leaves (26943 visited boxes; maximum depth 6). All 519 parameters pass. Positive derivative on the middle interval and the strict exterior signs give exactly one simple zero, and the sign pattern on the whole compact scale interval. Since q=d^2/s reverses orientation and all legal real budgets correspond to 0<s<=4 for d>=81, this proves A. There are no unchecked gaps between sample points.

## 3. Integer exclusion and the exceptional ambiguous sign

For each d=81..3000, use the full uniqueness and sign theorem (section 2 for d<600, KC otherwise). Start with q_a=floor(4d^2/5), q_b=ceil(4d^2/3), both legal for this scope. The program verifies F(d^2/q_a)>0 and F(d^2/q_b)<0 via intervals at exact rational scales. Bisection retains the signs, and 2919 of the 2920 parameters reach two consecutive integers with strict opposite signs. Uniqueness proves that no legal integer q is a zero, including q outside the initial bracket.

The first extended test using only interval signs halted at d=2464,q=6467382. This was an enclosure ambiguity, not an exact equality. The final implementation handles it by proving strict positive and negative signs at q-1 and q+1 respectively, leaving q itself as the only possible integer root. Evaluate the original JR/KA unnormalized rational C modulo p=1000000007 with all denominators nonzero modulo p (asserted on every division). The residue is 138102596, nonzero. Indeed a rational zero with invertible denominator has zero residue, so C!=0 regardless of its sign. The prime was independently checked locally by trial division through isqrt(p), and an independent Python integer computation using pow(den,-1,p) reproduced the residue. The two neighboring signs and the exact modular nonzero witness suffice without raising floating precision. There was exactly one such fallback in the final run. This proves B.

The smallest lower bound of the absolute normalized residual at the two final *outer bracket endpoints* in this run was 7.1975685177541539e-11 at d=2565. This is not a lower bound over all integer q or a root-distance estimate; at the modular fallback the center is certified by a different observable.

## 4. Reproduction and evidence

C++ source: 8ecce9c5315a575188d34495aa867a58ef268ef6:research_notes/portable_direct/R284KD_bridge.cpp, Git blob 8c5215c9412bdb07a1259026bfe8aa7848f31d58, SHA256 aeead7feaa3b4dd2cda2edd796df0b44e61a5ee9daa30838d52ba72b8b84aa20.
Full stdout: 6614fb2436253380b6b5b0de3a9eb379f69565f4:research_notes/portable_direct/R284KD_bridge_output.txt, Git blob 51903c1e07c9f515735a618b095894f9cedd2f65, SHA256 894c8795c2943c8304fc44022bf0771a6d8b8a0438e1a88b883b50ac880385c6. Both remote blobs matched the actual local files. An initial stdout transcription had incorrect intermediate counters; corrected by CAS and exact local Git blob comparison, use only the corrected pin.

Executed x86_64 Debian g++ 14.2.0:
    g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off R284KD_bridge.cpp -o R284KD_bridge
    ./R284KD_bridge 81 3000
Run exited successfully, local wall time 27.10 seconds, no NDEBUG. Last lines:
    MOD PASS d=2464 q=6467382 residue=138102596
    PASS d=81..3000 count=2920 modular=1 boxes=26943 sign_leaves=12174 derivative_leaves=2076 maxdepth=6 min_endpoint_residual_lower=7.1975685177541539e-11 at d=2565

Independent modular crosscheck (executed):
    p=1000000007
    from math import isqrt
    assert all(p%i for i in range(2,isqrt(p)+1))
    d,q=2464,6467382
    u,m=q+d,2*q+d
    def R(n):
        a=[1]
        for i in range(d): a.append(a[-1]*(n-i)*pow(n+i+3,-1,p)%p)
        return a
    U,M=R(u),R(m);V=Q=A=0
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*M[l]%p
        b=(k+1)*l*U[k]*M[l-1]%p if l else 0
        V=(V+a)%p;Q=(Q+b)%p
        A=(A+(u-k)*(u+k+2)*(a+b)*pow(2*u*(2*u+1),-1,p))%p
    E=U[d]*(u-d)*(2*d+3)*(m+2)*pow(2*(2*u+1)*(4*m+2),-1,p)%p
    C=(3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*(q*A+Q+V)**2)%p
    assert C==138102596

## 5. Remaining problem and next action

The finite real-root bridge is now complete. For d>3000 the problem is to exclude the unique real root from the integer lattice. The interval/modular hybrid is an exact certification pattern: use the joint carrier for continuous coverage and integer candidate location, but preserve the original rational carrier for exact modular nonzero tests at ambiguous points. It avoids high-degree polynomial expansion (O(d) arithmetic operations per residual evaluation with stored prefix products; O(log d) evaluations for bisection, plus modular inversion costs on fallback). This is a finite algorithm, not an asymptotic complexity bound independent of required precision. Next pursue tighter effective root localization and modular nonzero witnesses for all remaining d, rather than merely increasing the finite upper bound. JY/JZ subpower sparsity and KC analytic tail remain at their prior evidence scope; global integer exclusion is open. No independent review/formal verification claimed.
