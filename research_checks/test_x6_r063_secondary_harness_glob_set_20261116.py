"""Verify exact 5-part loader manifest, including extra part*.inc.

Run next to X6_R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_20261116.py.
Synthetic source fixture only; not the original 512-case benchmark.
"""
from __future__ import annotations
import hashlib
import importlib.util
from pathlib import Path
import tempfile

module_path = Path(__file__).with_name('X6_R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_20261116.py')
spec = importlib.util.spec_from_file_location('r063_second', module_path)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot import pinned secondary harness')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)

def digest(body):
    return hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()

def require(test, message):
    if not test:
        raise AssertionError(message)

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    folder = root/'scripts/r063_stage0_checker_parts'
    folder.mkdir(parents=True)
    loader = root/'scripts/r063_stage0_validate_path_valued_sqrt_2500.py'
    loader.write_text('exec(compile(_SOURCE, "part00.inc", "exec"), globals(), globals())\n', encoding='utf-8')
    files = [loader]
    for i in range(5):
        f = folder/f'part{i:02}.inc'
        f.write_text(f'x{i}={i}\n', encoding='utf-8')
        files.append(f)
    original = h.ORIGINAL
    try:
        h.ORIGINAL = {str(f.relative_to(root)):digest(f.read_bytes()) for f in files}
        require(len(h.verify_pins(root)) == 6, 'exact five parts should pass')
        extra = folder/'part05.inc'
        extra.write_text('unintended = True\n', encoding='utf-8')
        try:
            h.verify_pins(root)
        except AssertionError as error:
            require('glob source set' in str(error), 'wrong failure predicate')
        else:
            raise AssertionError('six original blobs plus unpinned part05.inc accepted')
        extra.rename(folder/'part999.inc')
        try:
            h.verify_pins(root)
        except AssertionError:
            pass
        else:
            raise AssertionError('unlisted part999.inc accepted')
        (folder/'part999.inc').unlink()
        require(len(h.verify_pins(root)) == 6, 'clean source set no longer accepted')
    finally:
        h.ORIGINAL = original
print('PASS_X6_R063_EXACT_LOADER_GLOB_FIVE_PARTS (SYNTHETIC)')
