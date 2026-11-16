#!/usr/bin/env python3
"""Unit 68: exact signed-X6 observer/G/T collision with unequal natural BRC.

Independent, portable integer checker of the frozen signed_brc.py interface.
This does not execute or replace the frozen module / R063 benchmark.
"""
from functools import lru_cache
from math import comb, factorial
from hashlib import sha256
import json


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def canonical(x: tuple[int, int, int]) -> tuple[int, int, int]:
    a = min(x)
    return tuple(i - a for i in x)


def mass(x: tuple[int, ...]) -> int:
    T = sum(abs(i) for i in x)
    n = factorial(T)
    d = 1
    for i in x:
        d *= factorial(abs(i))
    require(n % d == 0, "multinomial integrality")
    return n // d


def count_by_binom(x: tuple[int, ...]) -> int:
    remaining = sum(abs(i) for i in x)
    answer = 1
    for i in x:
        answer *= comb(remaining, abs(i))
        remaining -= abs(i)
    require(remaining == 0, "combinatorial recurrence")
    return answer


def count_by_recursion(x: tuple[int, int, int]) -> int:
    lengths = tuple(abs(i) for i in x)

    @lru_cache(None)
    def ways(a: int, b: int, c: int) -> int:
        if not (a or b or c):
            return 1
        return ((ways(a - 1, b, c) if a else 0)
                + (ways(a, b - 1, c) if b else 0)
                + (ways(a, b, c - 1) if c else 0))
    return ways(*lengths)


def one(m: int) -> dict:
    x = (0, -3*m, -3*m)
    y = (4*m, m, m)
    X = x + (0, 0, 0)
    Y = y + (0, 0, 0)
    require(canonical(x) == canonical(y) == (3*m, 0, 0), "observer collision")
    require(sum(z*z for z in X) == sum(z*z for z in Y) == 18*m*m, "same quadratic mass")
    require(sum(abs(z) for z in X) == sum(abs(z) for z in Y) == 6*m, "same event count")
    nx, ny = mass(X), mass(Y)
    require((nx, ny) == (count_by_binom(X), count_by_binom(Y)), "independent binomial count")
    require(ny > nx, "strict multiplicity separation")
    num, den = 1, 1
    for j in range(1, m + 1):
        require((m+j)*(2*m+j)-j*(3*m+j) == 2*m*m, "strict factor witness")
        num *= (m+j)*(2*m+j)
        den *= j*(3*m+j)
    require(ny*den == nx*num, "exact product ratio")
    if m <= 5:
        require(count_by_recursion(x) == nx, "word recurrence x")
        require(count_by_recursion(y) == ny, "word recurrence y")
    return {"m":m,"r":canonical(x),"G":18*m*m,"T":6*m,
            "x":X,"y":Y,"N_x":str(nx),"N_y":str(ny),
            "ratio_numerator":str(num),"ratio_denominator":str(den)}


def main() -> None:
    data = [one(m) for m in range(1, 129)]
    sample = [data[i-1] for i in (1, 2, 3, 5, 16, 32, 64, 128)]
    payload = {
        "schema":"EM_X6_SIGNED_BRC_OBSERVER_G_T_COLLISION_UNIT68_V1",
        "source_pin":"59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "native_producer_path":"experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py",
        "native_producer_blob_sha1":"300a96e3dc24bf6fff73743037a0347a8bc83176",
        "scientific_scope":"selected signed Z3 embedded in frozen Z6; same can3,G,T but unequal natural shortest path counts",
        "status":"AUTHOR_EXACT_CHECK_PASS_UNREVIEWED_NOT_ADMITTED",
        "m_range":[1,128],"tested":len(data),"failure_count":0,
        "recursion_both_endpoints_checked_m_range":[1,5],
        "samples":sample,
        "formula":"N_x=(6m)!/((3m)!)^2; N_y=(6m)!/((4m)!(m!)^2); N_y/N_x=product_j ((m+j)(2m+j))/(j(3m+j))>1"
    }
    digest=sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    payload["payload_sha256_without_digest"]=digest
    with open('/mnt/data/X6_LP019_EQUAL_OBSERVER_G_T_DIFFERENT_BRC_UNIT68_RESULTS_20261117.json','w') as f:
        json.dump(payload,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print(json.dumps({"status":"PASS","tested":len(data),"samples":sample[:2],"payload_sha256":digest},ensure_ascii=False))


if __name__=='__main__':
    main()
