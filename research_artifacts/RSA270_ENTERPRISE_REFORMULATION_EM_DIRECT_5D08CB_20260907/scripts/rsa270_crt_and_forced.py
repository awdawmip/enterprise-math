import math
N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

def g_m(m, r):
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

def admissible_r1(m):
    M6 = 6 * m
    s = set()
    for a in range(5 % 6, M6, 6):
        for b in range(5 % 6, M6, 6):
            if (a * b) % M6 == N % M6:
                S = (a + b) % (2 * m)
                if S % 2 == 0:
                    s.add(((S + 2)//2) % m)
    return s

# S = p+q < 2^449.  Find minimal M such that lcm(2m : m<=M) > 2^449.
print("== CRT bound ==")
l = 1; M = 0
while l <= (1 << 449):
    M += 1
    l = math.lcm(l, 2 * M)
print(f"minimal M with lcm(2m : m<=M) > 2^449 : M={M}, lcm bits={l.bit_length()}")
# odd-m sub-ladder
l = 1; Mo = 0
while l <= (1 << 449):
    Mo += 1
    l = math.lcm(l, 2 * (2 * Mo - 1))   # moduli 2m for odd m
print(f"minimal odd-m depth with lcm(2m : m odd, m<=2Mo-1) > 2^449 : 2Mo-1={2*Mo-1}, lcm bits={l.bit_length()}")

print("\n== RSA-270 forced torsion values (unconditional vs prior) ==")
print("N mod 6 =", N % 6, " N mod 8 =", N % 8)
# unconditional: m=4, m=8
for m in (4, 8):
    r0 = ((N + 3)//2) % m
    ar1 = admissible_r1(m)
    vals = {2 * g_m(m, r0) + 2 * g_m(m, r) for r in ar1}
    print(f"m={m}: r0={r0}, admissible r1={sorted(ar1)}, all profile values P(w_{m}) = {vals}")

# under prior (p,q==2 mod 3, odd): all m with |admissible r1|==1 give a forced profile value
print("\n-- m with |admissible r1| == 1 (forced profile value under construction-family prior) --")
forced = []
for m in range(3, 65):
    ar1 = admissible_r1(m)
    if len(ar1) == 1:
        r1 = list(ar1)[0]
        r0 = ((N + 3)//2) % m
        val = 2 * g_m(m, r0) + 2 * g_m(m, r1)
        forced.append((m, r0, r1, val))
for m, r0, r1, val in forced:
    print(f"m={m:2d}  r0={r0:2d}  r1={r1:2d}  P(w_{m}) = {val:+.10f}")

print("\n-- m=5,7 decode (example of nontrivial 1-bit/multi-bit tests) --")
for m in (5, 7):
    ar1 = sorted(admissible_r1(m))
    r0 = ((N + 3)//2) % m
    print(f"m={m}: admissible r1={ar1}; P(w_{m}) in " +
          "{" + ", ".join(f"{2*g_m(m,r0)+2*g_m(m,r):+.6f}" for r in ar1) + "}")
    # decode to S mod 2m classes
    Smod = sorted({(2*r - 2) % (2*m) for r in ar1})
    print(f"     -> S = p+q mod {2*m} in {Smod}")
