# D25/LIFT — exact finite exclusion certificate for WZ second-digit cancellation, $10^7<p\le10^8$

2026-10-24 · TASK_RESEARCH author-side **portable mathematical computation**. Status: **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is not an authenticated Researcher run, canonical checkpoint, frozen Result, independent review, native CM/divided-power computation, or proof for unbounded primes.

## Source boundary and precise question

Mother task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. The prior [exact WZ cancellation-fibre theorem](https://github.com/awdawmip/enterprise-math/blob/d1ba02f53b411242a534646df00e625cc52fe723/research_notes/portable_direct/20261024_hourly_d25_cubic_filter_harmonic_lift_full_wz_cancellation_fibre.md) supplies the **already proved** equivalence, for primes $p=6m+1\ge13$,

$$
 F_p=(S_{m+1}-S_m)/p\equiv2/3\pmod{p^2}
 \quad\Longleftrightarrow\quad p^2\mid M_p,
$$
$$
 D=3942400,\quad M_p=D(27^{p-1}-16^{p-1})-699519p\,16^{p-1}.
$$

Neither the WZ formula nor its equivalence is re-proved/re-credited here. The historical author certificate searched primes up to $10^7$ and found (1423,5827); the present **new** complete search is strictly $10^7<p\le10^8$, never re-running that earlier range.

**New finite result (exact computational certificate):** among all **2,548,323** primes $10{,}000{,}000<p\le100{,}000{,}000$ with $p\equiv1\pmod6$, **none satisfies** $p^2\mid M_p$. This excludes second-digit cancellation in precisely this bounded new interval. It does not prove that the inherited two lower primes are the only exceptions for all primes, nor close the original CM/LIFT target. The original target prime classes $p\bmod24\in\{13,19\}$ are a subset of the checked class; no new exception occurs there either.

## Two exact integer observers and verification

Observer I computes
$$
 R_p=[D(27^{p-1}-16^{p-1})-699519p\,16^{p-1}]\bmod p^2
$$
using modular exponentiation, without constructing enormous powers. Observer II computes the actual Fermat quotients modulo $p$,
$$
 a_p=(2^{p-1}-1)/p,\qquad b_p=(3^{p-1}-1)/p,
$$
and the independent reduced test
$$
 T_p=[3D b_p-4D a_p-699519]\bmod p.
$$
Because $27=3^3$, $16=2^4$ and $2^{p-1}\equiv3^{p-1}\equiv1\pmod p$, the binomial identity modulo $p^2$ gives $R_p\equiv pT_p\pmod{p^2}$. Thus both exact observers have zero simultaneously, and all candidates were independently evaluated through both modular bases. The equality is a mathematical identity; agreement of programs alone is not its proof.

A deterministic Eratosthenes sieve covers every integer through $10^8$: every composite has a prime divisor not exceeding $\sqrt{10^8}=10^4$. It found $\pi(10^8)=5{,}761{,}455$, and exactly 2,548,323 of the qualifying primes in the newly searched interval. Both congruence tests returned zero hits. For reproducible integrity of the **enumerated candidate population** only, SHA-256 of the little-endian unsigned 32-bit concatenation of all inspected prime values in ascending order is:

`5a11d7a6c84c50f1e1b39c95f7260e3a823b1536c15dc860b469f6a8d0cb1dda`.

This digest is a population check, not an independent scientific review, native Source receipt, or an authenticity claim about earlier scans.

## Complete standard-library reproducer

~~~python
from hashlib import sha256
from math import isqrt
from struct import pack

LOW, HIGH = 10_000_000, 100_000_000
D = 3942400
is_prime = bytearray(b'\x01') * (HIGH + 1)
is_prime[:2] = b'\x00\x00'
for d in range(2, isqrt(HIGH) + 1):
    if is_prime[d]:
        is_prime[d*d:HIGH+1:d] = b'\x00' * ((HIGH-d*d)//d + 1)

count = 0
hits_i, hits_ii = [], []
population_sha = sha256()
start = LOW + 1 + (1-(LOW+1)) % 6
for p in range(start, HIGH + 1, 6):
    if not is_prime[p]:
        continue
    count += 1
    population_sha.update(pack('<I', p))
    pp = p*p

    r27 = pow(27, p-1, pp)
    r16 = pow(16, p-1, pp)
    R = (D * (r27-r16) - 699519*p*r16) % pp
    if R == 0:
        hits_i.append(p)

    q2 = (pow(2, p-1, pp)-1)//p
    q3 = (pow(3, p-1, pp)-1)//p
    T = (3*D*q3 - 4*D*q2 - 699519) % p
    if T == 0:
        hits_ii.append(p)

    # A per-prime exact cross-check, not only an exception-list comparison:
    assert R == (p*T) % pp

assert is_prime.count(1) == 5761455
assert count == 2548323
assert hits_i == hits_ii == []
assert population_sha.hexdigest() == (
    '5a11d7a6c84c50f1e1b39c95f7260e3a823b1536c15dc860b469f6a8d0cb1dda'
)
print("PASS; 2548323 p=1(mod6) primes in (10^7,10^8]; no cancellations")
~~~

The original run used the same sieve, and first tested Observer I in nonoverlapping intervals $10^7<p\le2\cdot10^7$ (302,932 candidates) and $2\cdot10^7<p\le10^8$ (2,245,391 candidates). A second complete pass computed Observer II on all 2,548,323 candidates and matched the empty hit set; source code above includes an additional algebraic per-prime congruence assertion. No floating point, probabilistic primality acceptance, random seed, alternate WZ terminal, or change to the p-local conditions is involved.

## Provenance, BRC/observer scope, and next action

BRC **COMPOSE_APPLIED only to this declared scalar observation**: the inspected population, branch label $p$, input powers, two alternative exact modular observers, range, and prime-class filter remain visible; the compression to an empty hit list is certified only by the exhaustive finite scan and deterministic verifier. It is **not** a collapse of the four labeled WZ tails, a native Heartbeat/X6 claim, nor the Source-required CM/divided-power primitive representative. The external number-theoretic identity uses the actual original WZ observer and the inherited theorem's scope; P000 remains unchanged.

The canonical continuation remains unavailable to this author-side execution (read-only gateway returns `CONTROL_QUOTA`; Sites status `static_machine_readonly`, `write_relay_enabled=false`, `research_authority_granted=false`). Original four-file UR V2 bytes (historical 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) were **not** recovered or republished; an old upload pointer is not persistent evidence. No claim/open/checkpoint/handoff was asserted.

**Next exact action:** recover the original UR bundle from a genuinely authorized source and verify full bytes and the target SHA-256; reconcile exact current D25 continuation and the original pending session/write receipts when authorized. For the scientific parent, establish the Source-valid **same-prime, same-primitive-class** CM/divided-power representative and direction/normalization map before a true comparison against the frozen WZ observer. Do not repeat earlier $p\le10^7$ prime searches or this interval merely to make another checkpoint. The research remains OPEN.


## Reproducer transcription repair and source-separated cross-implementation check (2026-10-24)

This author-side maintenance corrects two **Python transcription syntax errors** in the published reproducibility block: `hits_i.append$p$` and `hits_ii.append$p$` were invalid Python; the intended calls are now `hits_i.append(p)` and `hits_ii.append(p)`. The scientific finite-range statement, prime class, arithmetic predicate, immutable input pins, and source/admission status are unchanged. The fixed Python program was syntax-checked locally; **its complete long Python replay was not completed in this repair pass**. Do not treat the earlier invalid text as executable evidence.

For a fast complete-range cross-implementation check, the following author-side **GNU C++17** program independently computes the exact quotient observer `T_p` on all admissible primes without floats, using 128-bit modular intermediate products. This run returned exactly `all-primes=5761455 range-primes=2548323 hits=0`; the generated little-endian prime population stream had SHA-256 `5a11d7a6c84c50f1e1b39c95f7260e3a823b1536c15dc860b469f6a8d0cb1dda`. The calculation is a second implementation, **not** an independent author/Driver review, new discovered prime range, native BRC experiment or mathematical admission. The congruence equivalence of observers remains the algebraic identity already proved above.

~~~cpp
#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t; using u128=__uint128_t;
static inline u64 mm(u64 a,u64 b,u64 mod){return (u128)a*b%mod;}
static inline u64 power(u64 a,u64 n,u64 mod){
    u64 r=1;
    while(n){if(n&1)r=mm(r,a,mod);n>>=1;if(n)a=mm(a,a,mod);}
    return r;
}
int main(){
    const int LO=10000000, HI=100000000; const u64 D=3942400;
    vector<uint8_t> prime(HI+1,1); prime[0]=prime[1]=0;
    for(int k=2;k*k<=HI;k++)if(prime[k])
        for(int n=k*k;n<=HI;n+=k)prime[n]=0;
    uint64_t count=0, hits=0; vector<uint32_t> vec;
    vec.reserve(2600000);
    for(int p=10000003;p<=HI;p+=6){if(!prime[p])continue;
        count++;vec.push_back((uint32_t)p);u64 pp=(u64)p*p;
        u64 a=(power(2,p-1,pp)-1)/p;
        u64 b=(power(3,p-1,pp)-1)/p;
        u64 T=((3*D*b)%p+(u64)p-(4*D*a)%p+
               (u64)p-699519%p)%p;
        if(T==0){hits++;cerr<<"HIT "<<p<<"\n";}
    }
    uint64_t nprime=0;for(auto x:prime)nprime+=x;
    cerr<<"all-primes="<<nprime<<" range-primes="<<count
        <<" hits="<<hits<<"\n";
    ofstream out("d25_wz_prime_candidates_le32.bin",ios::binary);
    for(auto p:vec)for(int j=0;j<4;j++)out.put(char(p>>(8*j)));
    out.close();
    return (count==2548323&&hits==0&&nprime==5761455)?0:1;
}
~~~

Reproduce on a GNU C++17 toolchain with `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify && sha256sum d25_wz_prime_candidates_le32.bin`; store the code block as `verify.cpp`. The expected digest is the population digest above. Distinguish this complete fast-source scan from the corrected Python program's uncompleted full replay.
