# CM24 prescribed-source gap: directed paper crosscheck

Status: DIRECTED / NONBLIND AUXILIARY PAPER REVIEW; local mathematical crosscheck only. This is not a decisive independent Driver review, Native Task/Claim/Run, Result acceptance, Working Truth, or parent completion. Root retains the Driver, original owner and all six contributor provenance IDs. Reviewer marker EM-CM24-6CC51A is locally assigned; no platform or Native role attestation is claimed. No prime sample, symbolic checker, old proof/check replay, branch, or competing owner was created.

The inherited two exact Source inputs are recorded in ../SOURCE_INPUT_PINS.json at immutable EM commit 1b5ba622d8cef73128d86ae61414f95924c4fe20. AGENTS/P000, heartbeat X6, joint-observer preservation, residual fidelity and BRC semantic alignment were read. The following is finite classical auxiliary algebra/readout reasoning; it makes no native spatial or physical propagation claim. Native X6 and separately typed time retain their existing meanings.

## 1. The central observer does not determine the endpoint on the stated ambient space

Work over F_p, with p=6m+1 prime in classes 13 or 19 modulo 24, m>=2 and N=3m. Let

    q(x)=x(x-3)^2/4,
    T(B)=Pi_(0..N)[x^(-N)(x-3)B(q(x))/24],
    V={B in F_p[z]: deg B<=N-1}.

For any delta B of degree d<m, the ordinary polynomial (x-3)delta B(q(x)) has degree at most 1+3d<=3m-2=N-2. Multiplication by x^(-N) leaves every exponent strictly negative (the largest is at most -2). Therefore T(delta B)=0. This proof uses only the declared finite support and unit constants 4 and 24; it does not delete the omitted coefficients from a different observer.

The explicit witness delta B=1 belongs to V, has T(delta B)=0 and delta B(1)=1. Thus B and B+1 have identical central coefficients but different endpoints. Consequently no universal linear functional L on the central coefficients can satisfy L(T(B))=B(1) for every B in V. More strongly, no arbitrary function of T(B) alone can do so on V. Every J/seed/terminal readout which is genuinely computed solely from T(B) factors through the same observer and cannot repair this witness. A readout that also uses forcing or omitted Laurent coefficients is additional information, not a counterexample to this scoped assertion.

This establishes only inclusion F_p[z]_(<m) subset ker T and non-descent of endpoint evaluation. It does not prove that this inclusion is the full kernel, identify a minimal repair dimension, rule out any other carrier, or prove that an already fixed scalar target is nonzero. The small low-degree block is invisible to this current central observer while remaining relevant to endpoint evaluation; it must therefore be retained or explicitly reconstructed in that future-observer scope.

Crucial fixed-source limitation: D_A^*(1)=-5/9. Hence B and B+1 do not satisfy the same prescribed forcing G_N(2z)/9. The ambient-space obstruction is not nonuniqueness within the fixed-source problem and does not forbid a formula that uses the independently prescribed source. At this fixed source, descending coefficient rows with unit D_j and B_N=0 determine the polynomial uniquely. No additional identifiability claim is justified merely by the ambient kernel witness.

## 2. Fixed-source low-block transport is exact

Use the already declared adjoint

    D_A^*=z(1-z)d^2+(3/2-5z/2)d-5/9,
    D_A^*B=G_N(2z)/9,
    A_j=(j+1)(j+3/2),
    D_j=(j+2/3)(j+5/6),
    e_j=(2/3)_j(5/6)_j/[(3/2)_j j!],
    E_k(1)=sum_(i=0)^k e_i.

Its coefficient row is A_j B_(j+1)-D_j B_j=2^j/9. For 0<=j<m, the ratio identity A_j e_(j+1)=D_j e_j allows division of this row:

    B_j/e_j=B_(j+1)/e_(j+1)-2^j/(9 D_j e_j).

Finite telescoping from j through m-1 proves exactly

    B_j=e_j[B_m/e_m-(1/9)sum_(k=j)^(m-1) 2^k/(D_k e_k)],
    0<=j<m.

The sign is negative and the forcing factor is 1/9. There is no e_N, no inversion of an internal h coefficient, and no target-derived seed. Summing over j=0,...,m-1 and exchanging only these finite triangular sums yields

    sum_(j=0)^(m-1) B_j
      =E_(m-1)(1) B_m/e_m
       -(1/9)sum_(k=0)^(m-1) 2^k E_k(1)/(D_k e_k).

These are exact identities for the prescribed-source solution. They do not assert B_m/e_m, the displayed weighted source sum, or the high block has an independently evaluated closed form.

## 3. Denominator window and the full endpoint ledger

All arithmetic divisions above occur in F_p. The base constants 2,3,6,9,24 are units because p>=13. The largest numerator in the relevant A_j factors is 2m+1<p, and the low D_j factors have numerators 3j+2<=3m-1<p and 6j+5<=6m-1=p-2. Thus all A_j,D_j used for j<m are units.

For e_j with j<=m, all numerator Pochhammer factors have numerators 3i+2 and 6i+5 for 0<=i<j<=m; both are positive and below p. Its denominator factors are 2i+3<=2m+1<p and i+1<=m<p. Therefore e_0,...,e_m are units. This proof is sufficient for every displayed quotient. It does not extrapolate the ratio recurrence to e_N: A_(N-1)=N(N+1/2)=0 in F_p, so that extrapolation would be invalid.

If descending uniqueness on the full degree<=N-1 space is used, D_j is also a unit for 0<=j<N: 3j+2 ranges below 2p and cannot equal p (residue modulo 3 differs); 6j+5 ranges below 3p and cannot equal p or 2p (residues modulo 6 differ). The top row may use A_(N-1)=0 because B_N=0; no division by that coefficient occurs.

The exact endpoint remains

    B(1)=sum_(j=m)^(N-1) B_j
          +E_(m-1)(1) B_m/e_m
          -(1/9)sum_(k=0)^(m-1)2^k E_k(1)/(D_k e_k).

The first term is the complete retained high block. The second and third terms reconstruct the invisible low block from a boundary coefficient and the fixed source. Dropping the high block, declaring the weighted source sum zero, or identifying B_m with an available central seed without a separate formula would be an overclaim. The already constructed half-prefix source, its class-dependent terminal correction and its specific first-row mismatch are inherited; this crosscheck does not reprove or alter them.

Disposition: the ambient endpoint obstruction and both low-block transport identities are mathematically sound with the scope above. The useful interface is source-assisted reconstruction, not a global impossibility or closure of the original scalar target. All mathematical parents remain OPEN.

## 4. Newly requested polynomial-pullback discriminator

This addition is pure paper verification; no executed p=13 check was read or reproduced. Let H(z) be any polynomial of degree<=N-1 and let y be the central coefficient vector of -x^(-N)q'(x)H(q(x)). The sign does not affect the annihilator. For 1<=s<=m-1 set L=p-s-1. Each monomial source has

    q' q^j (x-3)^(2s)
      =3/4^(j+1) * x^j (x-3)^(2j+2s+1)(x-1),
    0<=j<=N-1.

Set a=2j+2s+1 and k=L-1-j. Then k+1=L-j is an actual integer in [1,p-1] (in fact at least 2m+2 and at most p-2), and

    a+2k+3=2p,
    (k+1) binom(a,k+1)=(a-k) binom(a,k).

Division by k+1 is therefore legal in F_p, giving binom(a,k+1)=-3 binom(a,k). This remains valid when a>=p; the recurrence is an integer binomial identity reduced modulo p, not an illicit factorial quotient across p. If k>a, both relevant coefficients are zero. The case k=a is impossible here because a+2k+3=2p would give 3(a+1)=2p. Otherwise k<=a-1 and ordinary expansion gives

    [x^L] x^j(x-3)^a(x-1)
      =(-3)^(a-k-1)[-3 binom(a,k)-binom(a,k+1)]=0.

Linearity establishes [x^L]q'H(q)(x-3)^(2s)=0. Since 2N=p-1, extracting the coefficient at N-s after the x^(-N) shift yields the precise central constraint

    sum_(k=0)^(2s) binom(2s,k)(-3)^(2s-k) y_(N-s-k)=0,
    1<=s<=m-1.

Its entire support lies in the interior: 3<=N-3s<=N-s<=N-1. No Laurent exterior or endpoint row is silently discarded in this extraction. The largest index in row s is N-s with nonzero coefficient 9^s. These distinct largest indices form a triangular pivot argument, so the m-1 row functionals are linearly independent. This does not assert that they exhaust all constraints on the pullback family.

For s=1 the constraint is exactly

    y_(N-3)-6y_(N-2)+9y_(N-1)=0.

For the inherited half source, write explicitly b^h_r=beta^h_r-beta^h_(r-1)=(2/r+8/(2r-1))2^(-r). Using only N=(p-1)/2 as a field element and the actual independently proved 2^(-N)=-1 gives

    b^h_N=8, b^h_(N-1)=20/3, b^h_(N-2)=128/15,
    beta^h_(N-3)-6beta^h_(N-2)+9beta^h_(N-1)
      =4 beta^h_N-4b^h_N+5b^h_(N-1)-b^h_(N-2)
      =4 beta^h_N-36/5.

All indices are >=1 and denominators 3,5,15 are units at the allowed primes. Consequently a source from this polynomial pullback family that agrees with -beta^h at every central interior row necessarily satisfies beta^h_N=9/5. The same statement with +beta^h has the identical zero condition. The symbol must be beta^h: these displayed increments are not increments of the full beta^1+beta^h+beta^q (whose increment at N is 26/3).

This is a fresh necessary membership discriminator for the stated degree<=N-1 Gauss polynomial pullback family. It is not a proven exclusion until 4 beta^h_N-36/5 is independently evaluated and shown nonzero, and it is not a no-go theorem for the fixed mother target, other sources, other carriers or allowed repairs. No value of beta^h_N is asserted here. No old Green identity, earlier first-row mismatch or prior checker was re-proved or executed.

