#!/usr/bin/env python3
"""R762FG: exact 6-coordinate integer arithmetic in Z[zeta_9]. No dependencies."""
import json
from pathlib import Path

LAM = (2, 1, 1, 2, 0, 0)  # P(1,zeta,zeta^2)
BETA = (-7, -2, 2, 0, 5, 7)  # LAM^3 / 3, reduced modulo Phi_9
ONE = (1, 0, 0, 0, 0, 0)

def mul(a, b, modulus=None):
    c = [0] * 11
    for i in range(6):
        for j in range(6):
            c[i + j] += a[i] * b[j]
    for d in range(10, 5, -1):
        t = c[d]
        c[d] = 0
        c[d - 3] -= t
        c[d - 6] -= t
    return tuple(v % modulus if modulus else v for v in c[:6])

def power(a, exponent, modulus):
    result = ONE
    while exponent:
        if exponent & 1:
            result = mul(result, a, modulus)
        a = mul(a, a, modulus)
        exponent >>= 1
    return result

def v3(values):
    vals = []
    for x in values:
        if x:
            count = 0
            while x % 3 == 0:
                x //= 3
                count += 1
            vals.append(count)
    return min(vals) if vals else None

def main():
    assert mul(mul(LAM, LAM), LAM) == tuple(3 * v for v in BETA)
    assert power(BETA, 3, 3) == (2, 0, 0, 0, 0, 0)
    assert power(BETA, 2, 3) != ONE
    b6 = power(BETA, 6, 9)
    assert b6 == (1, 3, 6, 0, 6, 3)
    checks = []
    for k in range(8):
        modulus = 3 ** (k + 2)
        y = power(BETA, 6 * 3**k, modulus)
        delta = tuple((y[i] - ONE[i]) % modulus for i in range(6))
        assert v3(delta) == k + 1
        checks.append({"k": k, "exponent": 6*3**k,
                       "modulus_power": k+2, "exact_valuation": k+1})
    payload = {
      "schema": "R762FG_CHARACTER_PERIOD_EVIDENCE_V1",
      "scope": "six-positive-labelled-branch BRC on (Z/9Z)^3",
      "character_X_Y_Z": ["1", "zeta_9", "zeta_9^2"],
      "relation": "zeta^6+zeta^3+1=0",
      "lambda_coeffs_low_to_high": list(LAM),
      "beta_coeffs_low_to_high": list(BETA),
      "lambda_cube_equals_three_beta": True,
      "beta_cube_mod3": [2,0,0,0,0,0],
      "beta_square_not_one_mod3": True,
      "beta_six_minus_one_mod9": [0,3,6,0,6,3],
      "beta_order_mod3": 6, "valuation_beta_six_minus_one": 1,
      "power_checks": checks,
      "result": "h>=3: any eventual full-vector normalized period L is divisible by 18*3^(h-3)",
      "review": "NOT_REVIEWED", "local_execution": "PASS"
    }
    filename = Path(__file__).with_name("R762FG_CHARACTER_PERIOD_EVIDENCE.json")
    filename.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print("PASS: lambda^3=3beta; exact order 6; v3(beta^6-1)=1; eight power tests")
    print(filename)

if __name__ == "__main__":
    main()
