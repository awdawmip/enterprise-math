"""EC49CH independent literal certificate: signed X6, typed positive BRC.
Uses only the 33 literal source words and four declared suffixes from
CERTIFICATE_EC49CH.json; verifies integer 33x33 nonzero minor modulo prime.
"""
import json
from pathlib import Path

P = Path(__file__).resolve().parent
S = ((-1, -1), (-2, -2), (1, 2, -1, -2), (2, 1, -2, -1))
WP = ((2, 3, 3, 2, 1, 1), (3, 2, 3, 2, 1, 1))


def endpoint(word):
    z = [0] * 6
    for a in word:
        z[abs(a) - 1] += 1 if a > 0 else -1
    return tuple(z)


def brc(word, channel):
    product = 1
    if channel < 2:
        for a in word:
            if a > 0:
                product *= WP[channel][a - 1]
    return product


def atom(word):
    return 2 * int(any(word[k:k+2] == (1, 2) for k in range(len(word)-1))) + int(
        any(word[k:k+2] == (2, 1) for k in range(len(word)-1)))


def column(prefix):
    out = []
    for suffix in S:
        full = tuple(prefix) + suffix
        z = endpoint(full)
        a = atom(full)
        for label in range(4):
            for channel in range(3):
                out.append(brc(full, channel) if z == (0,)*6 and a == label else 0)
    assert len(out) == 48
    return out


def det_mod(square, p):
    m = [[v % p for v in row] for row in square]
    det = 1
    for j in range(len(m)):
        i = next((i for i in range(j, len(m)) if m[i][j] != 0), None)
        if i is None:
            return 0
        if i != j:
            m[i], m[j] = m[j], m[i]
            det = -det
        pivot = m[j][j]
        det = det * pivot % p
        pivot_inv = pow(pivot, -1, p)
        for i in range(j+1, len(m)):
            if m[i][j]:
                factor = m[i][j] * pivot_inv % p
                for k in range(j+1, len(m)):
                    m[i][k] = (m[i][k] - factor * m[j][k]) % p
                m[i][j] = 0
    return det % p


def main():
    cert = json.loads((P/'CERTIFICATE_EC49CH.json').read_text())
    words = [tuple(w) for w in cert['witness_words']]
    rows = cert['pivot_output_coordinate_indices']
    prime = cert['prime_modulus']
    assert len(words) == 33 and all(len(w) == 6 for w in words)
    assert len(rows) == 33 and len(set(rows)) == 33
    c = [column(w) for w in words]
    result = det_mod([[col[r] for col in c] for r in rows], prime)
    assert result == cert['nonzero_minor_residue'] != 0, result
    print('EC49CH_STANDALONE_CERT_PASS', len(words), len(rows), prime, result)


if __name__ == '__main__':
    main()
