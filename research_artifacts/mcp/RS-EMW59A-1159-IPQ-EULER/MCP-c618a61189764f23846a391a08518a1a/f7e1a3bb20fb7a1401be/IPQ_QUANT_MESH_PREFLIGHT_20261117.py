# IPQ finite mesh preflight; mpmath>=1.3, no trig/pi imported as native premise.
import mpmath as mp
mp.mp.dps = 70

def series(x, cosine=False):
    v = mp.mpf(1) if cosine else x
    total = v
    for j in range(1, 80):
        if cosine:
            v = -v*x*x / ((2*j-1)*(2*j))
        else:
            v = -v*x*x / ((2*j)*(2*j+1))
        total += v
    return total

S = lambda x: series(x)
C = lambda x: series(x, cosine=True)
tau = mp.findroot(S, (mp.mpf(3), mp.mpf(4)))
max_residual = mp.mpf(0)
max_gap_to_bound = mp.mpf(0)
count=0
for M in [2,3,4,5,8,16,32]:
    for k in range(1,M):
        u = 2-2*C(k*tau/M)
        a, b = mp.mpf(1), 2-u
        for n in range(2,M):
            a,b=b,(2-u)*b-a
        rho = 2*M*S(k*tau/(2*M))
        gap = k*tau-rho
        bound = k**3*tau**3/(24*M**2)
        invgap = 1/rho**2-1/(k*tau)**2
        assert gap >= -mp.mpf('1e-60') and gap <= bound + mp.mpf('1e-60')
        assert 2*k <= rho + mp.mpf('1e-60') <= k*tau + mp.mpf('1e-60')
        assert invgap >= -mp.mpf('1e-60') and invgap <= tau**2/(48*M*M) + mp.mpf('1e-60')
        if M+1>k:
            rho_finer=2*(M+1)*S(k*tau/(2*(M+1)))
            assert rho_finer > rho
        count += 1
        max_residual=max(max_residual,abs(b))
        max_gap_to_bound=max(max_gap_to_bound,gap/bound)
assert count==63
print('tau=',mp.nstr(tau,35),'pairs=',count,
      'max_recurrence_residual=',mp.nstr(max_residual,8),
      'max_gap/bound=',mp.nstr(max_gap_to_bound,12))
