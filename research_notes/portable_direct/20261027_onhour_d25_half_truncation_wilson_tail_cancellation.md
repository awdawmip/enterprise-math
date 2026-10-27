# D25 / SECOND-DIGIT-LIFT — proved half-length companion bridge and Wilson cancellation certificate

Date: 2026-10-27. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (TASK_RESEARCH; not CONTROL_PLANE_MAINTENANCE).
Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen SCIENTIFIC Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Classification: AUTHOR-SIDE EXACT DERIVED REDUCTION / PROVED USING A PUBLISHED SUPERCONGRUENCE / EIGHT EXACT PORTABLE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Native fixed H0/B0 divided-power benchmark NOT_EXECUTED / PENDING_OWNER. No source-native checkpoint, Result, independent review or accepted native Frobenius data.

## Consumed exact inputs (do not reprove)

For prime p=6m+1 with p mod 24 in {13,19}, set

  w_n=(6n+1) binom(2n,n)^2 binom(3n,n)/216^n,
  s_n=(8n+1) binom(4n,2n) binom(2n,n)^2/2304^n,
  W_p=sum(n=0..p-1) w_n,
  S_p(N)=sum(n=0..N) s_n.

All denominators are p-units. Source-preserving author proof at research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md establishes the original frozen observer identity:

  Delta_p - R_p = (W_p-p)/p^2 mod p,

given accepted UR/JT0, retaining the ORIGINAL signed Clausen cutoff R_p. The original LIFT is OPEN; it is not an auxiliary theorem's acceptance criterion.

A published theorem of V. J. W. Guo and W. Zudilin, "A q-microscope for supercongruences," Advances in Mathematics 346 (2019), 329–358, arXiv:1803.01830, gives BOTH

  S_p(p-1) = p*(-3/p) mod p^3,
  S_p((p-1)/2) = p*(-3/p) mod p^3

for every prime p>3. On the target classes (-3/p)=1, and (p-1)/2=3m. Their two independent truncation assertions (NOT just the full one) are the new imported input. Prior author companion-tail proof research_notes/portable_direct/20261027_onhour_d25_companion_tail_wilson_defect_p373.md gave a NONZERO higher segment (4m,q], q=floor((3p-1)/4), and found E_373=281. This unit consumes that result rather than recomputing its proof.

## New exact reduction: no unmatched companion tail in the smallest bridge

For every target prime, the following equivalent statements hold:

  original LIFT
   <=> W_p = p (mod p^3)
   <=> W_p - S_p(3m) = 0 (mod p^3)
   <=> [sum(n=0..3m)(w_n-s_n)] + [sum(n=3m+1..4m)w_n] = 0 (mod p^3).         (HB)

Proof: The source-aligned identity identifies the original LIFT with W_p=p mod p^3, after the accepted first digit. Guo–Zudilin supplies S_p(3m)=p mod p^3. Finally the exact original coefficient valuations show v_p(w_n)>=3 for n>=4m+1, hence W_p=sum(n=0..4m)w_n mod p^3. Split this at n=3m. No term of the original w-model from (3m,4m] is dropped.

Compared with the already-proved full companion-tail reduction,

  W_p-S_p(p-1)
    = sum(n=0..4m)(w_n-s_n)-p^2 E_p (mod p^3),

the new (HB) removes ALL s_n at n>3m by a *proved aggregate cancellation*, rather than by the false termwise claim that they vanish. The only companion terms left in (HB) have n<=3m, while W terms extend only to 4m. The all-prime vanishing of (HB) is still OPEN; this is an exact shorter equivalent target, not a proof of LIFT.

## New finite-field Wilson identity resolving the apparent nonzero higher segment

Put a=3m+1=(p+1)/2 and q=floor((3p-1)/4), and let

  D_p(n) = 2(8n+1)(4n-2p)! / [(n!)^4 2304^n] in F_p,  a<=n<=q.

For all p>3 and a<=n<=q,

  s_n/p^2 = D_p(n) (mod p).                                                (W)

Indeed 2p<=4n<3p, so (4n)! has precisely the two p-factors p,2p; n! and 2304 are p-units. Wilson gives (4n)!/p^2 = 2 (p-1)!^2 (4n-2p)! = 2(4n-2p)! (mod p). For n>q, v_p(s_n)>=3. Guo–Zudilin's difference of the full and half sums then implies the NEW finite-field all-prime identity

  sum(n=(p+1)/2..floor((3p-1)/4)) D_p(n) = 0 (mod p).                    (WC)

For target p=6m+1 this explicitly decomposes into two opposite signed sub-band residuals:

  L_p = sum(n=3m+1..4m) D_p(n),
  E_p = sum(n=4m+1..q) D_p(n),
  L_p + E_p = 0 (mod p).                                                  (LC)

E_p is exactly the prior author's high-band Wilson correction, now consumed. LC is a sourced exact counterweight that the previous E_p-only comparison did not express. It relies on Guo–Zudilin's already proved two-truncation theorem and therefore is not being claimed as a new independent supercongruence or publication priority. The weighted exceptional s-index differs by p residue class: p=13 mod24 has n_star=(5p-1)/8 inside the lower (3m,4m] band, raising that *single* term's valuation from 2 to 3; p=19 mod24 has n_star=(3p-1)/8 below that band. The proof still handles both classes without discarding this signed branch.

## Exact p=373 certificate and finite independent cross-check

For p=373, m=62, p^2=139129, p^3=51895117, half cutoff=186, original cutoff=248, q=279:

  sum(n=187..248) s_n  =  92*139129 = 12799868 (mod 51895117),
  sum(n=249..279) s_n  = 281*139129 = 39095249 (mod 51895117),
  total half-to-full companion tail = 51895117 = 0 (mod 373^3).

Thus the previously nonzero 31-term Wilson gap is *exactly cancelled* by the 62 preceding companion terms. It is invalid to truncate the full companion model at 248 termwise, but legitimate to replace the entire full model by its proved half-length truncation.

The still-OPEN shortened original bridge has exactly computed terms

  prefix P = sum(n=0..186)(w_n-s_n) = 14886803 (mod 51895117),
  middle M = sum(n=187..248)w_n   = 37008314 (mod 51895117),
  P+M=51895117=0 (mod 373^3).

This is a finite confirmation at p=373, NOT an all-target proof of HB. The known original scalar R_373=Delta_373=196 mod373 is retained; the calculation does not assert Delta_373=0.

Portable standard-library exact checker executed on p=13,19,37,43,61,67,211,373, independently computing all binomial terms modulo p^3 and the finite-field factorial formula (W) per term:

~~~python
from math import comb, factorial

def audit(p):
    assert p>=13 and p%24 in (13,19)
    m, mod=(p-1)//6,p**3
    h,c,q=3*m,4*m,(3*p-1)//4
    def w(n):
        return (6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)%mod
    def s(n):
        return (8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pow(2304,-n,mod)%mod
    P=sum(w(n)-s(n) for n in range(h+1))%mod
    M=sum(w(n) for n in range(h+1,c+1))%mod
    low=sum(s(n) for n in range(h+1,c+1))%mod
    high=sum(s(n) for n in range(c+1,q+1))%mod
    assert (low+high)%mod==0
    assert all(w(n)==0 for n in range(c+1,p))
    assert all(s(n)==0 for n in range(q+1,p))
    for n in range(h+1,q+1):
        digit=2*(8*n+1)*factorial(4*n-2*p)*pow(factorial(n),-4,p)*pow(2304,-n,p)%p
        assert s(n)==p*p*digit
    assert (P+M)%mod==0  # finite check only: OPEN LIFT!
    return p,P,M,low//(p*p),high//(p*p)

for p in (13,19,37,43,61,67,211,373):
    print(audit(p))
~~~

Observed tuples (p, P, M, L_p, E_p):

  (13, 507, 1690, 7, 6)
  (19, 3610, 3249, 3, 16)
  (37, 23273, 27380, 20, 17)
  (43, 14792, 64715, 15, 28)
  (61, 163724, 63257, 48, 13)
  (67, 40401, 260362, 18, 49)
  (211, 400689, 8993242, 128, 83)
  (373, 14886803, 37008314, 92, 281)


## BRC / evidence / next action

BRC carrier: original weighted W branch, companion S branch, split at 3m and 4m, prime-digit observer mod p^3, explicit signed lower/high Wilson corrections with valuation 2, and original Delta/R provenance. Safe quotient: the full companion tail can be removed only *as an aggregate at mod p^3*, using the proved Guo–Zudilin two-cutoff theorem. It is not safe to zero its components or regard the separate nonzero E_p as a mathematical error. This is a classical finite-field computation/observer, NOT a native Enterprise 3D slice or fixed H0/B0 module.

Scientific mother remains OPEN: no native original-class [X]U mod139129, rank, semilinear Frobenius basis normalization, signed odd Green/Hesse nor original kappa; support ticket #1559 remains PENDING_OWNER / NATIVE_NOT_EXECUTED. In the event a canonical lawful researcher route authorizes portable successor proof, the smallest new uniform proof obligation after (HB) is the shared lower prefix + native original last m coefficients modulo p^3, without reintroducing already cancelled companion higher bands. Native benchmark should not be replaced with repetitions of this lemma.

Research execution authority: last own Research recovery via bridge #6575 source_authority_verified=false, no verified own winning claim/open. Original dispatch #6576 failed TimeoutExpired. Old staging SD-d7c23e7984c2ddaac60a separate, not admitted. No replay, no maintenance lane identity, no made-up session ID/claim/run or Source-native checkpoint. This author artifact does not assert registered Research Activity or approved scientific output; REGISTER_PENDING/SYNC_DEBT.

Do not repeat: frozen D24 UR/CM0/JT0; previous E3 second-kind and CM eigenbasis notes; 815-prime W scan; E_p Wilson high tail derivation; all published Guo–Zudilin proof. Next original task action: authorized Source/native owner take existing #1559, locate/execute actual fixed H0/B0 representative and publish raw same-original-class data for independent verification; use (HB) only if canonical route independently authorizes portable proof. If Source role authority returns, read exact Research continuation then reconcile requests and resume/claim by current schema; preserve immutable science pin.
