#!/usr/bin/env python3
"""Original B2304 p=373 second-digit weighted cutoff guard; not native H0/B0."""
from math import comb
p = 373
M = p * p
w = pow(9, -1, M)
b = (7*p - 3)//8

def coefficients(parameters, fixed_denominator, length):
    vals = [1]
    for n in range(length - 1):
        numerator = 1
        for a, step in parameters:
            numerator *= a + step*n
        vals.append(vals[-1]*numerator*pow(fixed_denominator*(n+1)**len(parameters), -1, M) % M)
    return vals

beta = coefficients([(1,8),(3,8)], 64, b + 1)
gamma = coefficients([(1,4),(2,4),(3,4)], 64, p)
K = sum(c*pow(w,i,M) for i,c in enumerate(beta))%M
theta_K = sum(i*c*pow(w,i,M) for i,c in enumerate(beta))%M
weighted_K2 = (K*K + 16*K*theta_K)%M
high = 0
for i,bi in enumerate(beta):
    for j,bj in enumerate(beta):
        n = i + j
        if n >= p:
            high = (high + (1+8*n)*bi*bj*pow(w,n,M))%M
weighted_C = sum((1+8*n)*g*pow(w,n,M) for n,g in enumerate(gamma))%M
B_original = sum((8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,M) for n in range(p))%M
assert (K,theta_K%p,weighted_K2,high,weighted_C,B_original)==(0,5,0,M-p,p,p)
assert (weighted_K2-high)%M==weighted_C
print('PASS_D25_B2304_P373_SECOND_DIGIT_SOURCE_PORT')
print('p=',p,'modulus=',M,'K(1/9)=',K,'theta_K modp=',theta_K%p,'weighted_K2=',weighted_K2,
      'weighted_high_tail=',high,'weighted_projected=',weighted_C,'original_binomial_B=',B_original)
