"""
RSA-270 torsion-ladder known-block and construction-family prior constraint tables.
EM-DIRECT-5D08CB / DIRECT-RSA270.

Profile: P(u) = 2 W_{(N+3)/2}(u) + 2 W_{(S+2)/2}(u), S = p+q, W_s(u) = sum_{j=0}^{s-2} u^(2-s+2j).

Torsion value at primitive m-th root of unity (m>=3):
  P(w_m) = 2 g_m(r0) + 2 g_m(r1),   g_m(r) = sin(2*pi*(r-1)/m)/sin(2*pi/m) = U_{r-2}(cos(2*pi/m))
  r0 = ((N+3)/2) mod m   (computable from N alone -> "known block" K_m = 2 g_m(r0))
  r1 = ((S+2)/2) mod m   (factor-bearing block)

This script computes for RSA-270:
  A. basic sanity: digit count, bit length, small-prime trial division
  B. r0(m) and K_m for m = 3..64 (exact sine-ratio form + decimal)
  C. construction-family-prior admissible r1(m) sets: p,q odd, p==q==2 mod 3,
     ab == N mod 6m  => admissible S mod 2m => admissible r1(m) classes
  D. the m=1 (u=1) and m=2 (u=-1) specializations (full-S / sign-determined-S statements)
  E. QR-mapping for m=3,4 and the CRT reconstruction bound (m<=200 gives full S)
"""
import math

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

def g_m(m, r):
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

print("== A. sanity ==")
print("digits:", len(str(N)), " bits:", N.bit_length())
print("N mod 6 =", N % 6, " N mod 8 =", N % 8, " N mod 16 =", N % 16, " N mod 24 =", N % 24)
# trial division
small = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
for pp in small:
    if N % pp == 0:
        print("SMALL FACTOR FOUND:", pp)
print("trial division over listed small primes: no factor" )

print("\n== B. known block K_m = 2 g_m(r0), r0 = ((N+3)/2) mod m ==")
r0list = {}
for m in range(3, 65):
    r0 = ((N + 3)//2) % m
    r0list[m] = r0
    K = 2 * g_m(m, r0)
    print(f"m={m:2d}  r0={r0:2d}  K_m = 2*sin(2*pi*{r0-1}/{m})/sin(2*pi/{m}) = {K:+.10f}")

print("\n== C. prior-constrained admissible r1(m) = ((S+2)/2) mod m ==")
print("prior: p,q odd primes, p==q==2 mod 3 (construction family); scan mod 6m")
for m in range(3, 33):
    M6 = 6 * m
    admissible_r1 = set()
    # residues a with a odd and a == 2 mod 3  <=>  a == 5 mod 6
    for a in range(5 % 6, M6, 6):
        if a >= M6: break
        if a == 0: continue
        for b in range(5 % 6, M6, 6):
            if (a * b) % M6 == N % M6:
                S = (a + b) % (2 * m)
                if S % 2 == 0:
                    admissible_r1.add(((S + 2)//2) % m)
    K = 2 * g_m(m, ((N + 3)//2) % m)
    vals = sorted({2 * g_m(m, r) for r in admissible_r1})
    valstr = ", ".join(f"{v:+.6f}" for v in vals)
    print(f"m={m:2d}  admissible r1 = {sorted(admissible_r1)}  (count={len(admissible_r1)})  -> profile defect values {valstr}")

print("\n== D. m=1,2 specializations ==")
# u=1: P(1) = (N+1) + S  (sigma(N)); u=-1: P(-1) = (N+1)(-1)^((N+3)/2) + S*(-1)^((S+2)/2)
sgnN = (-1) ** ((N + 3)//2)
print(f"P(1) = sigma(N) = (N+1) + S        [S = p+q unknown]")
print(f"P(-1) = (N+1)*({sgnN:+d}) + S*(-1)^((S+2)/2)")
# sign of S term determined by N mod 4:
# (S+2)/2 = S/2+1; (-1)^(S/2+1): N=1 mod 4 => S=2 mod 4 => S/2 odd => (-1)^(S/2+1)=+1
#                    N=3 mod 4 => S=0 mod 4 => S/2 even => (-1)^(S/2+1)=-1
if N % 4 == 1:
    print(f"N==1 mod 4 -> (-1)^((S+2)/2)=+1 -> P(-1) = (N+1)*({sgnN:+d}) + S   (full S, sign-free)")
else:
    print(f"N=={N%4} mod 4 -> (-1)^((S+2)/2)=-1 -> P(-1) = (N+1)*({sgnN:+d}) - S   (full S)")

print("\n== E. QR mapping and CRT bound ==")
# m=3: r1 = (S+2)/2 mod 3; S mod 6 = 2 (r1=2, g=+1) or 4 (r1=0, g=-1)
print("m=3: r1=2 <=> S==2 mod 6 <=> p==q==1 mod 3 ; r1=0 <=> S==4 mod 6 <=> p==q==2 mod 3")
print("     (deciding = Euler-criterion QR decision for -3 mod N; N==1 mod 6, Jacobi(+3|N)=+1)")
print("     under construction-family prior (p,q==2 mod 3): r1(3)=0 forced -> P(w_3) = K_3 - 2")
print("m=4: r1=2 <=> S==2 mod 8 <=> p==q==+-1 mod 8 ; r1=0 <=> S==6 mod 8 <=> p==q==+-3 mod 8")
print("     (deciding = QR decision for 2 mod N; N==1 mod 8)")
# CRT bound: lcm(2m for m<=200) > 2^449
lm = 1
for m in range(1, 201):
    lm = math.lcm(lm, 2*m)
print(f"lcm(2m : m=1..200) = {lm} bits={lm.bit_length()}  (S < 2^449 -> ladder up to m=200 pins S exactly)")
print(f"K_3 (known block m=3): 2*g_3(r0(3)) = {2*g_m(3, r0list[3]):+.10f}; prior-predicted P(w_3) = K_3 - 2 = {2*g_m(3, r0list[3]) - 2:+.10f}")
print(f"K_4 (known block m=4): 2*g_4(r0(4)) = {2*g_m(4, r0list[4]):+.10f}")
