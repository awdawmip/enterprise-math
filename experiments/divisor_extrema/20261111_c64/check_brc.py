"""Replay labelled paths in the inherited positive-mass histogram carrier."""
from fractions import Fraction
from pathlib import Path
import argparse
import json
import sys
import tempfile
from zipfile import ZipFile


def state_after_word(native, word, k, initial, counts):
    one = native.weight_histogram([1])
    zero = native.weight_histogram([])
    rows = [one if initial == i else zero for i in range(3)]
    rates = [Fraction(1, 4), Fraction(1), Fraction(4)]
    stock = [k, k, k + 1, 1]
    for symbol in word:
        next_rows = [zero, zero, zero]
        for i, hist in enumerate(rows):
            if hist.is_zero:
                continue
            scaled = [stock[0], stock[1], stock[2] * rates[i], stock[3]]
            probability = Fraction(scaled[symbol], sum(scaled))
            if symbol == 1:
                successors = [(0, Fraction(7, 8)), (i, Fraction(1, 8))]
            elif symbol == 0:
                successors = [(min(2, i+1), Fraction(1))]
            else:
                successors = [(i, Fraction(1))]
            for target, prob in successors:
                branch = native.histogram_serial(hist, native.weight_histogram([probability * prob]))
                next_rows[target] = native.histogram_recoalesce(next_rows[target], branch)
                counts['serial'] += 1
                counts['recoalesce'] += 1
        stock[symbol] -= 1
        rows = next_rows
    assert stock == [0, 0, 2, 1]
    masses = [h.total_mass for h in rows]
    return tuple(x/sum(masses) for x in masses)


def replay(c62_archive):
    counts = {'schedules': 0, 'conditional_rows': 0, 'serial': 0, 'recoalesce': 0}
    with tempfile.TemporaryDirectory() as tmp, ZipFile(c62_archive) as archive:
        root = Path(tmp) / 'prime_quantum_schedule_extrema_c62'
        for file in archive.namelist():
            if file.startswith(root.name + '/') and file.endswith('.py'):
                dest = (Path(tmp) / file).resolve()
                if not dest.is_relative_to(root):
                    raise ValueError('Invalid archive path')
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(archive.read(file))
        sys.path.insert(0, str(root))
        import schedule_extrema as c62
        native = c62.old.prior.inherited.old.old.inherited.native
        for k in range(2, 6):
            for gaps in c62.compositions(k-1, k+1):
                actual = tuple(state_after_word(native, c62.word(gaps), k, i, counts) for i in (0, 1))
                assert actual == c62.rows(gaps)
                counts['schedules'] += 1
                counts['conditional_rows'] += 2
    return counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('c62_archive', type=Path)
    print(json.dumps(replay(parser.parse_args().c62_archive), indent=2))
