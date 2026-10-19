# RSA-270 continuation: explicit constant-width ternary twisted-trace decoder

Status: `RESEARCH NOTE / EXACT DECODER / N-ONLY EVALUATION OPEN`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-06T20:31:34+08:00`  
Parent: `research_notes/RSA270_3ADIC_TORSION_PACKET_LADDER_20260906.md`  
Verifier: `experiments/rsa270_explicit_ternary_trace_decoder.py`

No RSA-270 factor is obtained.

## 1. Correction to the parent note

The parent note established information-theoretically that at most two suitably chosen twisted traces can separate at most three candidate lifts, but left an explicit probe selector open.

That gap is now closed for the normalized extreme packet: there is a deterministic selector using at most **four integer traces per level**, with no search over the `3^e` possible probe positions.

## 2. Sparse normalization of the extreme packet

Let `m=3^e`, `n=3^(e-1)` and `zeta=zeta_m`. The two extreme hidden terms are

`E_e = 2[W_((p+m q+2)/2)(zeta) + W_((m p+q+2)/2)(zeta)]`.

For odd m,

`W_(t+1)(zeta)=zeta (zeta^t-zeta^(-t))/(zeta^2-1)`.

Define

`tau_e(r)=(r+m)/2 (mod m)`

for odd r modulo `2m`. Then

`Z_e := ((zeta^2-1)/(2zeta)) E_e
      = zeta^tau_e(p)-zeta^-tau_e(p)
       +zeta^tau_e(q)-zeta^-tau_e(q)`.

Under H2 (`p,q≡2 mod3`), every positive `tau_e` exponent is `1 mod3`, while every negative exponent is `2 mod3`.

## 3. The ternary lift digits are literal cyclotomic triples

Suppose the previous factor residue r is known modulo `2n`. Its three lifts modulo `2m` are

`r`, `r+2n`, `r+4n`.

If

`t0=tau_(e-1)(r) (mod n)`,

then the corresponding positive exponents at level e are exactly

`t0`, `t0+n`, `t0+2n (mod m)`.

Thus the unknown 3-adic lift digit is exactly the position inside one cyclotomic triple.

## 4. Two fixed traces encode one lift digit

Define

`L_r(Z)=Tr_{Q(zeta_m)/Q}(zeta_m^(-r) Z)`.

For `m=3n`, the Ramanujan trace is

`Tr(zeta_m^k)=2n` if `k≡0 mod m`,
`=-n` if `k≡n or 2n mod m`,
`=0` otherwise.

Probe one previous fiber at

`r=t0` and `r=t0+n`.

Because the negative exponents live in the opposite mod-3 sector, they contribute zero to these probes. An isolated positive exponent therefore has the exact code

- lift digit 0 -> `(2n,-n)`;
- lift digit 1 -> `(-n,2n)`;
- lift digit 2 -> `(-n,-n)`.

The three codes are distinct. Hence **two predetermined integer traces recover one ternary lift digit**.

## 5. Coincident previous factor fibers are still decoded by the same two probes

If the two previous factor residues have the same `t0 mod n`, the probe sees the sum of two digit codes. The six unordered digit multisets have codes (in units of n):

- `{0,0}` -> `(4,-2)`;
- `{0,1}` -> `(1,1)`;
- `{0,2}` -> `(1,-2)`;
- `{1,1}` -> `(-2,4)`;
- `{1,2}` -> `(-2,1)`;
- `{2,2}` -> `(-2,-2)`.

All six are distinct.

Therefore two probes recover the unordered pair of lift digits even in the coincident-fiber case.

## 6. Explicit constant-width branch decoder

At level e:

1. from the previous unordered factor residues modulo `2n`, compute their one or two distinct `t0` fibers modulo n;
2. for each distinct fiber query the two traces at `t0` and `t0+n`;
3. decode the corresponding digit or unordered digit pair using the tables above;
4. obtain the unique factor residue pair modulo `2m`.

Hence the width is:

- 2 integer traces if the previous factors occupy the same fiber;
- 4 integer traces if they occupy distinct fibers.

No probe-position search is required. The verifier exhaustively checks all H2 local lift groups through `e=5`, in addition to the symbolic code tables.

## 7. Extraction from the full multiplied profile

The decoder is stated for the extreme normalized packet `Z_e`, but the full coefficient contains:

- an N-only divisor packet;
- intermediate hidden terms with multipliers `3^j, 1<=j<=e-1`;
- the two extreme hidden terms.

Given the previous factor residues modulo `2*3^(e-1)`, every intermediate term is already determined modulo `3^e`: changing p or q by a previous-level lift modulus contributes a multiple of `3^e` once multiplied by at least one factor 3.

Therefore the N-only packet and intermediate packet can be subtracted from any exact level-e profile observable, leaving `E_e`, after which the known scalar normalization gives `Z_e`.

## 8. BRC residue-imbalance form

Multiplication by `(zeta^2-1)/(2zeta)` is a signed one-step difference:

`((zeta^2-1)/(2zeta)) R(zeta) = (zeta R(zeta)-zeta^-1 R(zeta))/2`.

Consequently each decoder trace is an integer linear combination of Ramanujan three-bin residue counts. If `c_j` are the exponent masses of the residual profile modulo m, then

`L_r( ((zeta^2-1)/(2zeta))R )
 = 1/2 * sum_j c_j [c_m(j+1-r)-c_m(j-1-r)]`,

where `c_m` is the Ramanujan sum for modulus `3^e`.

So the needed compact observable is not a huge cyclotomic object: it is a **signed BRC three-bin residue-flow count** whose output has only `O(e)` bits.

## 9. Refined factorization frontier

Combining this note with the branch-oracle reduction:

- the mathematical decoder is now explicit and constant-width;
- the output per level is at most four ordinary integers of `O(log(3^e))` bits;
- the remaining obstacle is solely **N-only evaluation** of those four residue-imbalance counts from the product/generating-function side without recovering the factor packet first.

For RSA-270, if that evaluation were available through `e=282`, the factorization would follow.

This is the sharpest current formulation of the route:

`BRC multiplied profile -> subtract known/lower packets -> 2-4 ternary residue-flow traces -> one 3-adic factor lift -> repeat`.
