"""Exact finite checks for R284FB carry-over omission states; standard Python only."""
from itertools import combinations
import json


def words(u, q):
    if u == q == 0:
        return ["00", "01", "11", "10"], (0, 0, 0)
    a, b = u + q + 1, 3 * u + q
    return ["0" * a + "0" * b + "0" * a,
            "0" * a + "1" * b + "1" * a,
            "1" * a + "0" * b + "1" * a,
            "1" * a + "1" * b + "0" * a], (a, b, a)


def hamming(x, y):
    return sum(c != d for c, d in zip(x, y))


def successors(states, old, new, q):
    diff = [i for i in range(len(old)) if old[i] != new[i]]
    out = set()
    for state in states:
        for k in range(min(q, len(diff)) + 1):
            for missed in combinations(diff, k):
                missed = set(missed)
                out.add(''.join(state[i] if i not in diff or i in missed else new[i]
                                for i in range(len(old))))
    return out


def error_patterns(u, q):
    c, (a, b, _) = words(u, q)
    if u == q == 0:
        return {c[0]}, {c[0]}
    actual = successors(successors({c[2]}, c[2], c[3], q), c[3], c[0], q)
    # At c0: last A/B misses plus preceding C misses; omission budgets independent.
    last = list(range(a + b))
    before = list(range(a + b, 2*a + b))
    expected = set()
    for n in range(q+1):
        for left in combinations(last, n):
            for k in range(q+1):
                for right in combinations(before, k):
                    fault = set(left+right)
                    expected.add(''.join('1' if i in fault else '0' for i in range(len(c[0]))))
    return actual, expected


def main():
    rows = []
    for u in range(3):
        for q in range(3):
            code, _ = words(u, q)
            actual, expected = error_patterns(u, q)
            assert actual == expected, (u, q, len(actual), len(expected))
            maxerr = max(hamming(y, code[0]) for y in actual)
            assert maxerr == 2*q
            wrong_reachable = any(any(hamming(y, code[j]) <= 2*u+q
                                      for j in (1, 2, 3)) for y in actual)
            expected_wrong = q >= 2 or (u == 0 and q >= 1)
            assert wrong_reachable == expected_wrong, (u, q, wrong_reachable)
            rows.append({"u":u,"q":q,"n":len(code[0]),"endpoint_states":len(actual),
                         "max_stable_errors":maxerr,"false_generation_reachable":wrong_reachable})
    # Explicit 2-edge witness (u=0,q=1): c2=11011 -> c3 physical 11110 -> c0 physical 00110.
    c,_ = words(0,1)
    assert c == ["00000","00111","11011","11100"]
    assert "11110" in successors({c[2]}, c[2], c[3], 1)
    assert "00110" in successors({"11110"}, c[3], c[0], 1)
    assert [hamming("00110",w) for w in c] == [2,1,4,3]
    print(json.dumps({"status":"PASS","case_count":len(rows),"rows":rows,
                      "witness":{"codewords":c,"physical_after_2_to_3":"11110",
                                 "physical_after_3_to_0":"00110",
                                 "stable_truth":0,"decoder_output":1,"radius":1}},
                     ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
