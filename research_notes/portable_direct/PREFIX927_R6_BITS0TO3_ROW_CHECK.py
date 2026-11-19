#!/usr/bin/env python3
"""PREFIX-927 exact bits 0..3 zero/one XOR pair census (Python 3 standard library)."""
import hashlib, json, math, sys

N = 1 << 32
QMIN, QMAX, M = 262145, 524287, 131072
ROWS = range(400001, 400128, 2)
BITS = range(4)

def pair_id(a, b):
    return ((a - QMIN) // 2) * M + (b - QMIN) // 2

def special_second_moduli():
    values = set()
    for b in range(QMIN, QMAX + 1, 2):
        r = 2 % b
        for _ in range(1, 32):
            if r in (1, b - 1):
                values.add(b)
                break
            r = (2 * r) % b
    return values

def main():
    special = special_second_moduli()
    def outside_old(a, b):
        if b < 33 * ((N + a - 1) // a) or a < 33 * ((N + b - 1) // b):
            return False
        if (a // math.gcd(a, b)) * b < N:
            return False
        return b not in special

    sets = [set() for _ in BITS]
    params = [0] * 4
    for b in ROWS:
        for k in range(1, (N - 1) // QMIN + 1):
            if math.gcd(k, b) != 1:
                continue
            inv = pow(k, -1, b)
            for i in BITS:
                H = 1 << i
                for sign, r in ((-1, (H * inv) % b), (1, (-H * inv) % b)):
                    if r < QMIN:
                        r += b
                    if r > QMAX or r % 2 != 1:
                        continue
                    a = r
                    A = k * a
                    if A + (H if sign == 1 else 0) >= N:
                        continue
                    assert (A + sign * H) % b == 0
                    x = H if sign == 1 else 0
                    y = A + x
                    assert 0 <= x < N and 0 <= y < N
                    assert (y - x) % a == 0
                    assert (y - (x ^ H)) % b == 0
                    params[i] += 1
                    if outside_old(a, b):
                        sets[i].add(pair_id(a, b))
                    if outside_old(b, a):
                        sets[i].add(pair_id(b, a))

    def digest(ids):
        return hashlib.sha256(b"".join(x.to_bytes(8, "little") for x in sorted(ids))).hexdigest()
    accum = set()
    totals = []
    for ids in sets:
        accum.update(ids)
        totals.append(len(accum))
    result = {
        "schema": "PREFIX927_BIT0_TO_BIT3_ROW_INCREMENT_V1",
        "frozen_scientific_input": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "p": 32, "Q": [QMIN, QMAX, 2],
        "b_rows": [400001, 400127, 64],
        "bits": list(BITS), "special_second_moduli": len(special),
        "parameter_witnesses_by_bit": params,
        "outside_BZS_by_bit": list(map(len, sets)),
        "progressive_outside_BZS_union": totals,
        "increment_beyond_bit0": totals[-1] - totals[0],
        "final_outside_BZS_union": totals[-1],
        "bit0_sha256": digest(sets[0]),
        "final_sha256": digest(accum),
        "BZS_base": 7462508971,
        "combined_count": 7462508971 + totals[-1],
        "complement": M * M - 7462508971 - totals[-1],
    }
    assert params == [386923, 385892, 385639, 387049]
    assert totals == [437560, 654668, 873058, 1091862]
    assert result["bit0_sha256"] == "f8e594257de9a99aa6de4be42d9dde79ba0427a5105c60bfa715d92bd25a60e4"
    assert result["final_sha256"] == "2f03e83c1df067b926ed075e2bf641bdedfc12480590994ede45691d37aa7ad0"
    data = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as f:
            f.write(data)
    print(data)

if __name__ == "__main__":
    main()
