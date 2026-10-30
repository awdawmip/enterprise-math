# D25/LIFT GH-157: full CM(-24) split-prime integer trace (author side)

2026-10-30 (+08). AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Research lane chatgpt-research-hourly-enterprise-math-20260923; D25/LIFT/JT2 OPEN. Scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 and P000 ACTIVE_LOCKED unchanged. GH-157 is an author working identifier, not an admitted native Task.

## Theorem

For every prime p≡11(mod24), p>=11, fix rho²=2 in F_(p²), B+=(1+2rho/3)/8, B-=B+^p and E_B: y²=x(x²+x+B). There exist integers x>0,y>0 (unique up to signs) such that p=2x²+3y², x even, y odd. Then

a_(p²)(E_B+)=a_(p²)(E_B-)=6y²−4x²=2p−8x²,
#E_B±(F_(p²))=(p−1)²+8x².

This is an exact integer-valued infinite-family statement. Together with GH-155/156 (inert class p≡19(mod24): trace 2p and #=(p−1)²), it resolves all unweighted elliptic-curve integer traces for the entire p≡3(mod8) family at this specific CM mark, without solving the separate marked first derivative or GH-3.

## Proof

The GH-155 direct j computation gives j(B+)=2417472−1707264rho, a root of the Hilbert class polynomial H_{−24}=X²−4834944X+14670139392. Thus the characteristic-zero curve has CM by the maximal order O_K=Z[sqrt(−6)], K=Q(sqrt(−6)). It has good reduction here because B(1−4B)=1/144 and Norm(B)=1/576.

For p≡11(mod24), (−6/p)=+1; Deuring CM reduction gives an ordinary curve with geometric endomorphism ring O_K (maximal CM order). The primitive reduced positive definite binary forms of discriminant −24 are exactly (1,0,6), (2,0,3). Enumerate a≤sqrt(24/3)<3, |b|≤a≤c, b²−4ac=−24. Every split prime p is represented by one of these forms. The first gives x²+6y², impossible modulo 8 for p≡3(mod8); hence p=2x²+3y², with x even and y odd.

Let γ=2x+y sqrt(−6), so Norm(γ)=2p; then π=γ²/2=(2x²−3y²)+2xy sqrt(−6) lies in O_K with Norm(π)=p². As x,y!=0, π is not ±p. For split p, the only ideal factors of norm p² are P², P Pbar=(p), and Pbar². Thus (π) equals P² or Pbar². Ordinary q=p² Frobenius belongs to O_K, has norm p², and is not ±p; hence its ideal equals P² or Pbar². The unit group O_K× is {±1}; therefore Frobenius is ±π or ±conjugate(π), giving a_q=±(4x²−6y²).

The remaining sign is forced by an EXACT rational 2-division calculation. Choose eta²=6 and rho²=2 in F_(p²); for this split class eta^p=−eta, rho^p=−rho. Then v=rho/eta∈F_p with v²=1/3, and choose s²=3 in F_p. The two nonzero 2-torsion abscissas are α=(-1+(rho−1)/eta)/2 and β=(-1−(rho−1)/eta)/2. Their field norms satisfy

Norm(α)=(7−12v)/24=2*((2−3v)/(4s))²,
Norm(β)=(7+12v)/24=2*((2+3v)/(4s))².

The square factors are nonzero; since (2/p)=−1, α and β are nonsquares in F_(p²). Since χ_(p²)(−1)=+1, −α and −β are nonsquares too. The usual 2-division criterion for y²=(x−e1)(x−e2)(x−e3) then forbids any rational half of all three nonzero rational order-two points. The 2-Sylow subgroup is exactly (Z/2)², so #E(F_q)≡4(mod8). As p≡3(mod8), q+1≡2(mod8), requiring a_q≡6(mod8). Since x is even and y odd, 4x²−6y²≡2(mod8), so its sign must be MINUS. This proves a_q=6y²−4x², and the group order formula follows from p=2x²+3y². The Frobenius-conjugate B− has the same F_q point count.

Classical inputs stated: Hilbert class polynomial identification, CM splitting/ordinary endomorphism theorem, binary quadratic form/ideal correspondence, rational 2-division criterion, and Frobenius norm. No numerical 3347 point count enters the general proof.

## New 3347 arithmetic certificate

3347=2*(40)²+3*(7)². Consequently a_(3347²)=6*49−4*1600=−6106 and #E(F_(3347²))=(3346)²+8*1600=11,208,516. This independently matches the earlier GH-143 full 11,202,409-element integer point count, using a CM representation and torsion sign instead of another full enumeration. No claim of author independence is made.

Author-executed Python stdlib verification found the representation for all 71 primes p≡11(mod24), p<4000; their traces agreed modulo p with independently computed direct Hasse coefficients. Four small split p=11,59,83,107 also agree with this turn's independent exact F_(p²) integer counts: −10,−10,134,86. The new numeric proof-bounded checker returned PASS_CM24_SPLIT_TRACE_FORMULA_CONCORDANCE; full author-executed local checker SHA256 19398e3e74b95f763908bf77394f9b521705785d834c9b32971c0a6858dd4d59. The code uploaded here is a concise independently readable reproduction and is not asserted byte-identical to the locally executed full checker.

The mathematical boundary is important: this determines unweighted integer Frobenius traces, not H'_p(B+), S_1(B+), the reflected R_p(9), original GH-3, or native D25 p373/divided-power/frobenius-normalization. In the split family the oriented GH-153 condition still requires the independent CM-jet identity H'_p(B+)=6rho H_p(B+); an equivalent Hasse recurrence is not its independent proof.

BRC COMPOSE_APPLIED: retains inert/split branch, ideal class, (x,y), twist sign fixed by 2-torsion, integer trace, root characters and observer orientation. Mod-p unmarked trace alone does not determine the full integer point-count source.

Sources: https://numberdb.org/Hilbert_class_polynomials ; https://math.mit.edu/~drew/vantage/ElkiesSlides21.pdf ; https://crypto.stanford.edu/pbc/notes/numbertheory/form.html .
