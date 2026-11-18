# R271 — Smith-exponent-optimal precision for coupled rational BRC Port stars

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED.
Independent portable research, no formal CLAIM. Follows R270A at 5383c9477cf8b1d7d8026a8c5856b1b65cbd6928.
Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Typed predecessor: WBRC-T30/T31/T32, definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md (frozen and current blob e7823e69fe8112663af2feeb3fc3207b73b2fabe).
The result concerns exactly the stable finite positive-rational *labeled visible Port star*; it keeps P000, native X6, source/branch provenance and the joint-relation constraint as separate ambient information, with no asserted map from R269's auxiliary sources to native BRC states.

## Theorem: optimal input digits governed by largest Smith exponent

Let p be any prime, R=Z_(p), and A in M_d(R) nonsingular. For a stable nonnegative rational BRC effective-port matrix and an allowed rational nonnegative port context, A=I-W_eff-C, with rows and columns retaining the original Port labels; the visible star is S=A^(-1). Let

  s(A)=min{n>=0 : p^n A^(-1) is entrywise p-integral}.

Equivalently, if A has Smith exponents 0<=a_1<=...<=a_d over R, then s=a_d.

**Theorem R271-A.** For every integer m>=1 and B in M_d(R) with B=A (mod p^(s+m)), B is nonsingular, has the same Smith exponents as A, and

  p^s B^(-1) = p^s A^(-1) (mod p^m)

entrywise. Therefore s+m input digits suffice for all labeled entries of the intrinsically normalized star to m-digit precision, conditional on the certified exponent s. The result is uniform across all matrices and contexts meeting these hypotheses.

**Proof.** Write B=A+E and F=A^(-1)E. Since E lies in p^(s+m)M_d(R) and p^s A^(-1) is integral, F lies in p^m M_d(R). Thus B=A(I+F), and I+F belongs to GL_d(R), being the identity modulo p. This invertible right factor preserves Smith exponents. Moreover p^s B^(-1)=(I+F)^(-1)p^s A^(-1); the first factor is the identity modulo p^m. QED.

**Cofactor certificate.** Let t=v_p(det A) and c=min_ij v_p(adj(A)_ij), treating zero cofactors as valuation infinity. Smith normal form yields t=sum a_i, c=sum_(i<d) a_i, s=t-c. Thus the earlier determinant bound t+1 can be tightened by c digits to t-c+1 for one intrinsically normalized output digit, or to t-c+m for m digits. This is a sharper conditional input-precision result than R270A.

**Important observer distinction.** R270A's *determinant-normalized* observer is p^t A^(-1). If c>0, p^t A^(-1)=p^c(p^s A^(-1)) is the zero matrix modulo p; no nonzero determinant-normalized first-digit star survives. If c=0, t=s and the earlier t+1 bound applies unchanged. The intrinsically normalized p^s A^(-1) may still be nonzero and preserve visible Port distinctions when c>0.

## Exact sharpness with genuinely interacting positive-rational Port modules

For every s>=1 and m>=1, choose p=13, P=13^s, L=1+13^(m-1), M=4PL+1, and

  q0=P/M, q1=PL/M, K=[[2,-1],[-1,2]],
  A_i=q_i K, W_i=I-A_i=[[1-2q_i,q_i],[q_i,1-2q_i]].

Both W_i have strictly positive coupling q_i. Since 0<q_i<1/4, W_i is entrywise nonnegative and its row sums equal 1-q_i<1. Therefore each is a strictly stable two-labeled-Port rational BRC module, with no hidden-state connections and with the empty permitted future context.

K has determinant 3, a 13-unit, so the Smith exponents of both A_i equal (s,s). Hence t=2s, c=s and s(A_i)=s. Their input difference is exactly

  A_1-A_0 = 13^(s+m-1) K/M,

so the two labeled inputs agree modulo 13^(s+m-1). Their exact stars are

  S_i = 1/(3q_i) [[2,1],[1,2]],

whose intrinsically normalized off-diagonal difference is

  (13^s S_0-13^s S_1)_12
  = (M/3)(1-1/L)
  = M*13^(m-1)/(3L).

Both M and L are 13-units, so the difference has valuation **exactly m-1**. The two normalized stars differ modulo 13^m. This proves no general bound s+m-1 suffices, even for fully coupled positive-rational labeled two-Port stars. The precision s+m in Theorem A is sharp for all s,m in this family.

Example s=m=1: P=13,L=2,M=105; initial A matrices agree mod 13 while the residues of 13*S_0 and 13*S_1 at entry (1,2) are 9 and 11. The older determinant-normalized stars 13^2*S_i are both zero modulo 13. The sharper normalization retains a distinguishable relational residue.

## Evidence and limits

The accompanying pure-standard-library Python Fraction checker independently verifies positive rational stability, exact inverse identities, two invariant-factor depths, input valuation and output valuation for all 48 pairs 1<=s<=8 and 1<=m<=6. Result PASS 48; the full generated JSON has SHA-256 6d9538341e683ac9be9dc811010676f6fdf0ca7a7eea9a9e9682679882877ddc. This finite check supports the symbolic universal proofs; it is not the proof of all parameter values.

The theorem's context is finite stable positive-rational recurrent BRC with visible labeled Port star observations at a declared p-adic output precision. It neither proves lossless source/Port/branch-history compression nor permits unknown future contexts of arbitrarily large resonance depth from a single fixed modular snapshot. WBRC-T32's exact W_eff remains the signature for unrestricted permitted contexts. Classical Smith form and adjugate identities are standard antecedents; the contribution here is the precision theorem's typed Port interpretation and a sharp coupled-rational family. Formal independent review and project admission are pending.

## Next mathematical question

For a *fixed sparse set of permitted Port-edge perturbations* E_(kl), derive entry-specific minimal input precision from the actual resolvent terms (S E_(kl) S)_ij, and test tightness on nonnegative stable BRC models. Separately construct or refute an actual provenance-preserving map from the R269 auxiliary source observation carrier to genuine WBRC-T32 Port signatures, proving future observer fiber constancy when such a map is proposed.

Artifacts: R271_SMITH_SHARP_MULTIPORT_ADIC_PRECISION_20261118.md; R271_smith_precision_certificate.py; R271_verification_digest.json. Local full R271_verification.json is reproducible by running the accompanying script.