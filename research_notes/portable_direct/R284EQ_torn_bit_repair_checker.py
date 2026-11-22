"""R284EQ small-domain exhaustive checker. Python 3, standard library only.

Models: binary repetition source label; s arbitrary existing bit errors; one
unconfirmed write to a chosen bit. Torn bit settles to either binary value.
"""
import json
from itertools import combinations
from hashlib import sha256
from pathlib import Path


def hamming(u, v):
    return (u ^ v).bit_count()


def ball(t, b, s):
    center = ((1 << t) - 1) if b else 0
    return {u for u in range(1 << t) if hamming(u, center) <= s}


def tear(u, j, v):
    return (u & ~(1 << j)) | (v << j)


def distinguishable(t, s, kind):
    if kind == 'directed':
        return not (ball(t, 0, s) & ball(t, 1, s))
    if kind == 'unknown-address':
        outcomes = []
        for b in (0, 1):
            states = set()
            for u in ball(t, b, s):
                for j in range(t):
                    states.add(tear(u, j, 0))
                    states.add(tear(u, j, 1))
            outcomes.append(states)
        return not (outcomes[0] & outcomes[1])
    if kind == 'known-address':
        # Persistently known attempted address j; two different labels must be
        # distinguishable even if j is completely arbitrary after the attempt.
        for j in range(t):
            a = {(u & ~(1 << j)) for u in ball(t, 0, s)}
            b = {(u & ~(1 << j)) for u in ball(t, 1, s)}
            if a & b:
                return False
        return True
    raise ValueError(kind)


def check():
    cases = 0
    monotonic_checks = 0
    interleaved_checks = 0
    witness = {}
    for t in range(1, 10):
        for s in range(0, 4):
            if s > t:
                continue
            for model, threshold in [('directed', 2*s+1),
                                     ('known-address', 2*s+2),
                                     ('unknown-address', 2*s+3)]:
                actual = distinguishable(t, s, model)
                predicted = t >= threshold
                assert actual == predicted, (t, s, model, actual, predicted)
                cases += 1
                if s in (0, 1, 2, 3) and model not in witness:
                    witness[model] = {}
                if s in (0, 1, 2, 3) and t == threshold:
                    witness[model][str(s)] = t

            # Directed repair selects only positions actually disagreeing with
            # the correctly decoded true bit. Torn result can only keep or
            # correct that mismatch; it never creates a fresh error.
            for b in (0, 1):
                center = ((1 << t) - 1) if b else 0
                for u in ball(t, b, s):
                    wrong = [j for j in range(t) if ((u >> j) & 1) != b]
                    for j in wrong:
                        for v in (0, 1):
                            new = tear(u, j, v)
                            assert hamming(new, center) <= hamming(u, center)
                            monotonic_checks += 1
                        # Exactly one external flip may occur after selecting
                        # an initially wrong j and before the torn write.
                        # The complete read-select-write interval may gain at
                        # most that one externally charged error.
                        for k in range(t):
                            mid = u ^ (1 << k)
                            for v in (0, 1):
                                new = tear(mid, j, v)
                                assert hamming(new, center) <= hamming(u, center) + 1
                                interleaved_checks += 1

    # Concrete sharp witnesses at s=1.
    assert distinguishable(3, 1, 'directed')
    assert not distinguishable(3, 1, 'known-address')
    assert distinguishable(4, 1, 'known-address')
    assert not distinguishable(4, 1, 'unknown-address')
    assert distinguishable(5, 1, 'unknown-address')
    certificate = {
        'research_id': 'R284EQ',
        'model': 'binary repetition; stable torn bit can settle to 0 or 1; one torn operation',
        'tested_t': [1, 9],
        'tested_s': [0, 3],
        'classification_cases': cases,
        'directed_repair_monotonic_checks': monotonic_checks,
        'interleaved_external_flip_checks': interleaved_checks,
        'formulas': {
            'directed_only_wrong_positions': 't >= 2*s+1',
            'unknown_torn_address': 't >= 2*s+3',
            'known_torn_address_erasable': 't >= 2*s+2'
        },
        'sharp_minimum_t_by_s': witness,
        'proof_scope': 'all integers s>=0 via Hamming balls; finite checker supplements proof',
        'independent_review': 'NOT_REVIEWED'
    }
    return certificate


if __name__ == '__main__':
    cert = check()
    output = Path(__file__).with_name('R284EQ_torn_bit_repair_certificate.json')
    output.write_text(json.dumps(cert, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(cert, indent=2, ensure_ascii=False))
    print('checker_sha256', sha256(Path(__file__).read_bytes()).hexdigest())
    print('certificate_sha256', sha256(output.read_bytes()).hexdigest())
