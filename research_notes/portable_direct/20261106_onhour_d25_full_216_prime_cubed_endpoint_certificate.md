# D25 — Full 216 weighted-sum Gosper residual and cubic endpoint cancellation

Date: 2026-11-06. Task publication TP2-B6F4FC938FF94941C1B7, frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3. This author-side scientific increment consumes the exact source-resolved 216 weighted-prefix transfer at d45b65a2b2455475ae97760ce51130a5451c1d30. Status: AUTHOR-PROVED / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED; not an official Source CLAIM, Result, independent review, or original native H0/B0 experimental run.

## Exact finite identity

For n>=0 define a_n=(2n)!(3n)!/[216^n(n!)^5]=C(2n,n)^2 C(3n,n)/216^n and W_N=sum_(n=0)^(N-1) (6n+1)a_n. Then a_(n+1)/a_n=A(n)/B(n), with A(n)=(2n+1)(3n+1)(3n+2), B(n)=36(n+1)^3.

Set R(n)=4-12n and h(n)=(66n^2+113n+49)/[9(n+1)^3]. For every integer n>=0, the following is an exact rational identity:

    (6n+1)a_n = R(n+1)a_(n+1)-R(n)a_n+h(n)a_n.                  (1)

Proof: expand A(n)R(n+1)-B(n)R(n)=B(n)(6n+1)-4(66n^2+113n+49), and divide by B(n).

For every N>=1, summing (1) and retaining its final rational term gives

    W_N=-4+sum_(n=0)^(N-2) h(n)a_n+E_N,
    E_N=R(N)a_N+h(N-1)a_(N-1)
       =-36 N^3(6N-11)a_N/[(2N-1)(3N-2)(3N-1)].               (2)

The last expression follows by substituting the original coefficient ratio at n=N-1. This is an EXACT cancellation between two endpoint contributions: neither term is separately discarded.

For any prime p>3, v_p(a_p)=v_p((2p)!)+v_p((3p)!)-5v_p(p!)=2+3-5=0; 216 is a p-unit. All denominator factors 2p-1,3p-2,3p-1 are also p-units. Hence v_p(E_p)>=3. Thus the original unmodified 216 series satisfies

    W_p == -4 + sum_(n=0)^(p-2) [(66n^2+113n+49)/(9(n+1)^3)] a_n   (mod p^3).  (3)

All denominators in the reduced sum are p-units. For the frozen p==13,19 mod24 mother objective, W_p==p modp^3 is equivalent to the precise remaining requirement

    sum_(n=0)^(p-2) h(n)a_n == 4+p  (mod p^3).                 (4)

Equation (4) is NOT proved here; the conversion (3) is unconditional for all primes >3. The previously established signed Clausen boundary J_p is not set to zero: J_19=6 and J_373=98 modulo p.

## Scope-specific single-channel Gosper obstruction

There is NO rational r(n) in Q(n) satisfying A(n)r(n+1)-B(n)r(n)=B(n)(6n+1).

Proof: suppose r has a pole and choose a nonempty integral-shift orbit of poles, with rightmost pole alpha and leftmost beta. At alpha the term r(n+1) has no pole to cancel, hence B(alpha)=0 and alpha=-1. At n=beta-1, r(n) has no pole, hence A(beta-1)=0 and beta in {1/2,1/3,2/3}. These fractional pole positions are never in alpha's integral shift orbit, contradiction. Therefore r is a polynomial. For a polynomial of degree d, the leading degree of A(n)r(n+1)-B(n)r(n) is d+3 with leading coefficient -18 times that of r. The target is degree 4, so d=1. Matching degrees 4 and 3 forces r(n)=4-12n, but leaves nonzero remainder 4(66n^2+113n+49). Contradiction.

Because degree strictly rises by 3 on nonzero polynomials, the image of this polynomial difference operator has unique remainder representatives span_Q{1,n,n^2}; this full-216 operator is not identified with the distinct prior middle-shell operator. The obstruction is solely to a single rational-term Gosper primitive; it does not preclude coupled WZ, CM, p-adic or native approaches.

## Actual exact computation and evidence interpretation

The companion Python standard-library checker performs exact Fraction verification for n=0..128 and all N=1..24, then independently compares the original original-coefficient weighted W_p against the p-unit reduction (3) modulo p^3 for all 166 primes 5<=p<=997. All tests passed. Representative [p,W_p modp^3,new RHS modp^3,E_p modp^4] values:

    [5,120,120,500]; [11,1320,1320,0]; [13,13,13,4394];
    [19,19,19,54872]; [373,373,373,18786032354].

The exact algebra proves (1)-(3) for their stated scope; the finite computation is corroboration, not proof of the mother p^3 target. Original native fixed p=373 H0/B0 divided-power [X]U modulo 139129, semilinear Frobenius/eta/rank, odd Hesse/Green, kappa and independent replication remain NOT_EXECUTED/PENDING_OWNER under issue #1559. Original Source continuation request onhour11-20261106-1400-exact-research-lane-continuation must be reconciled by its own request ID; no claim/run/result is asserted.

## Next research action

Combine the original full-216 p-unit residual (3) with the source-resolved signed J weighted-prefix transfer at d45b65a2b2455475ae97760ce51130a5451c1d30. Construct a multichannel finite integration-by-parts or parameter deformation proving the residual identity (4) uniformly in the frozen two prime classes, with valuations and nonzero J19/J373 retained. Native #1559 remains separately actionable only through authorized same-original-class computation and independent replication.
