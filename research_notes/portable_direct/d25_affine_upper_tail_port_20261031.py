#!/usr/bin/env python3
"""D25 exact source-port proof regression, not a universal bridge verifier.

Unweighted coefficient valuations and p^4 upper-tail port of the two *distinct*
weighted, fully truncated 216/2304 models. All arithmetic is exact modulo p^4.
The universal result is supplied by the accompanying elementary proof; these
finite checks do NOT prove the p^4 affine bridge for arbitrary primes.
"""
from math import comb, isqrt


def primes_up_to(limit):
    sieve = bytearray(b'\1') * (limit + 1)
    sieve[:2] = b'\0\0'
    for q in range(2, isqrt(limit) + 1):
        if sieve[q]:
            sieve[q*q::q] = b'\0' * ((limit-q*q)//q + 1)
    return [p for p in range(5, limit + 1) if sieve[p]]


def v_mod(x, p, max_exponent=4):
    if x == 0:
        return max_exponent
    n = 0
    while x % p == 0:
        n += 1
        x //= p
    return n


def band(k, p):
    # Integer-only thresholds; each indicator is a strict crossing.
    return sum((4*k >= p, 3*k >= p, 2*k >= p,
                3*k >= 2*p, 4*k >= 3*p))


def original_ports(p, check_valuations=True):
    modulus = p**4
    inverse_36 = pow(36, -1, modulus)
    inverse_288 = pow(288, -1, modulus)
    inverses = [0] + [pow(k, -1, modulus) for k in range(1, p)]
    a = b = 1
    ports_a = [0] * 6
    ports_b = [0] * 6
    last_term_a = last_term_b = None
    for k in range(p):
        if k:
            j = k - 1
            inv3 = inverses[k] ** 3 % modulus
            a = (a * (2*j+1) * (3*j+1) * (3*j+2)
                 * inverse_36 * inv3) % modulus
            b = (b * (4*j+1) * (2*j+1) * (4*j+3)
                 * inverse_288 * inv3) % modulus
        if check_valuations:
            assert v_mod(a,p) == 2*k//p + 3*k//p, (p,k,'A valuation')
            assert v_mod(b,p) == 4*k//p, (p,k,'B valuation')
        r = band(k, p)
        ports_a[r] = (ports_a[r] + (6*k+1)*a) % modulus
        ports_b[r] = (ports_b[r] + (8*k+1)*b) % modulus
        if k == p-1:
            last_term_a = a
            last_term_b = b
    assert last_term_a % modulus == (p**3 * (p-1)) % modulus
    assert last_term_b % modulus == (p**3 * (p-1)) % modulus
    return ports_a, ports_b


def reflected_upper_tail(p):
    """Residue (A_last-2B_last)/p^3 mod p, using only reflected units."""
    P = Q = 1
    last = 0
    m = p//4
    for j in range(m):
        last = (last + (5+6*j)*P - 2*(7+8*j)*Q) % p
        if j + 1 < m:
            dA = (2*j+3)*(3*j+4)*(3*j+5)
            dB = (2*j+3)*(4*j+5)*(4*j+7)
            assert dA % p and dB % p, (p,j,'reflection denominator')
            P = P * 36*(j+1)**3*pow(dA,-1,p) % p
            Q = Q * 288*(j+1)**3*pow(dB,-1,p) % p
    return last


def direct_last_band(p):
    """Independent integer-binomial cross-check of the last band only."""
    m = p**4
    ia = pow(216,-1,m)
    ib = pow(2304,-1,m)
    aa = bb = 0
    for k in range((3*p+3)//4, p):
        aa += (6*k+1)*comb(2*k,k)*&*ÛÛXÊËÊJÝÊXKËJB
ÏH

ÊÌJJÛÛX
ËÊJÛÛXËÊJÝÊXËJB]\

XKLI[JKËÜ
ÂYXZ[
NÈH[Y\×Ý\ÝÊL
B[
	ÐÒPÒÑQÔSQTÉË[ÊK	ÍO\LL	ÊBÜ[ÎKHÜYÚ[[ÜÜÊ
BYJVÍWKLÍWJI\
\ÜÙ\Y	\
ÈOH\ÜÙ\YËÜ
ÈOHYXÝYÝ\\ÝZ[

KY[
KËLKLËNKÍËËÍÌÊN\ÜÙ\YËÜ
ÈOH\XÝÛ\ÝØ[

K[
	ÔÔÕÒUTÔÉË	ÝKHH[	ËÊ
K
JK
KJK
K
ËK
ËÊWK	ÑÛ\ÝÜÉËYËÜ
Ë	ÑÚIËÊKLI\
ÜK[\
KWJBK[ÜYÚ[[ÜÜÊLÊB\ÜÙ\[

KLILLÊOHÜK[\
KJB[
	ÐSÔÈÓTÈULLÎTÔÉÊB[
	ÕSUTÐSTTURSÔUSNSUHQÔTÔÒSÓTÔÎÈÓÑSÕIÊB[
	ÑSÕTSÔTQSHQÑNÔSÈUUHÍÌÈÐÕÑVPÕUQ	ÊBY×Û[YW×ÈOH	××ÛXZ[×ÉÎXZ[
B