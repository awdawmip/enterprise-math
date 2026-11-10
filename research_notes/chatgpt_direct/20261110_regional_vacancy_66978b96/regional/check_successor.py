"""Finite interval verification of the sparse available-index representation."""
from pathlib import Path
import json
from region import FreeIndexTree, RegionEvidence


def run():
    checks = 0
    for size in (1, 2, 4, 8):
        for blocked in range(1 << size):
            tree = FreeIndexTree(size)
            for index in range(size):
                if (blocked >> index) & 1:
                    tree.set_free(index, False)
            for lower in range(size):
                for upper in range(lower, size):
                    expected = next((i for i in range(lower, upper+1)
                                     if not ((blocked >> i) & 1)), None)
                    assert tree.first(lower, upper) == expected
                    checks += 1
            for index in reversed(range(size)):
                tree.set_free(index, True)
            assert tree.root is None
            checks += 1
    region = RegionEvidence(2, 3)
    region.acquire(1, 0)
    region.bind(0, 8)
    assert not region.contains(0)
    region.copy(1, 0)
    region.drop(0)
    assert not region.contains(0)
    region.drop(1)
    assert region.contains(0)
    region.bind(0, 0)
    assert region.contains(0)
    return dict(status='PASS', sizes=[1, 2, 4, 8],
                interval_and_restore_checks=checks,
                nonempty_zero_residue_and_last_alias='PASS',
                scope='Exact finite control representation; no physical BRC execution')


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('successor_checks.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
