"""One packaging selector for text and gzip; metadata only, no arithmetic.

Historical validation directories are excluded from source_current_root()
but must be explicitly accounted for by VALIDATION_EVIDENCE_ALLOWLIST.json.
This module performs no work at import time.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
HARD_EXCLUDED = {'closeout', 'transport', 'source_cache', '__pycache__'}
ROOT_EXCLUDED = {'PUBLICATION_MANIFEST.json', 'activity_observation.json', 'startup_guard.py',
                 'DELIVERY_RECEIPT.json'}
HISTORICAL_ALLOWLIST = 'VALIDATION_EVIDENCE_ALLOWLIST.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_relative(value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('Expected canonical relative POSIX path')
    parts = PurePosixPath(value).parts
    if PurePosixPath(value).is_absolute() or '..' in parts or '.' in parts or ':' in value:
        raise ValueError('Unsafe relative path')
    if PurePosixPath(value).as_posix() != value:
        raise ValueError('Noncanonical relative path')
    path = (ROOT/value).resolve()
    path.relative_to(ROOT.resolve())
    return path


def historical(path):
    parts = path.relative_to(ROOT).parts
    # Generated chunks mirror original paths. Their historical provenance is
    # checked by INDEX against the allowlisted original, not as a new original.
    return (parts[0] != 'readable_evidence' and
            any(x == 'prior_validation' or x.startswith('prior_validation_') for x in parts))


def ordinary_file(path):
    relative = path.relative_to(ROOT)
    return (path.is_file() and not any(x in HARD_EXCLUDED for x in relative.parts)
            and path.suffix != '.pyc')


def prior_art_allowlist():
    manifest_path = ROOT/'prior_art/PUBLICATION_MANIFEST.json'
    if not manifest_path.exists():
        return set()
    data = json.loads(manifest_path.read_bytes())
    # This round uses files; permit the previous schema when restoring provenance.
    keys = [key for key in ('files', 'publication_files') if key in data]
    if len(keys) != 1:
        raise ValueError('Exactly one recognized prior_art file list is required')
    names = {'prior_art/PUBLICATION_MANIFEST.json'}
    for record in data[keys[0]]:
        relative = 'prior_art/' + record['path']
        path = canonical_relative(relative)
        if relative in names or not path.is_file() or sha(path) != record['sha256']:
            raise ValueError('Duplicate, missing or changed prior_art allowlisted file: ' + relative)
        names.add(relative)
    return names


def source_current_root():
    """Current source only; generated evidence and historical validation excluded."""
    allowed_prior = prior_art_allowlist()
    result = []
    for path in sorted(ROOT.rglob('*')):
        if not ordinary_file(path) or historical(path):
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative in ROOT_EXCLUDED:
            continue
        if relative.startswith('readable_evidence/'):
            # Publish these two source scripts, never stale generated chunks/index.
            if relative not in ('readable_evidence/build_readable_evidence.py',
                                 'readable_evidence/evidence_selection.py'):
                continue
        if relative.startswith('prior_art/') and relative not in allowed_prior:
            continue
        result.append(path)
    return result


def historical_selection():
    found = {p.relative_to(ROOT).as_posix(): p for p in ROOT.rglob('*')
             if ordinary_file(p) and historical(p)}
    source = ROOT/HISTORICAL_ALLOWLIST
    if not source.exists():
        if found:
            raise ValueError('Historical validation exists but has no explicit allowlist: ' +
                             ', '.join(sorted(found)))
        return [], {'allowlist': None, 'included': [], 'omitted': []}
    body = json.loads(source.read_bytes())
    if body.get('schema') != 'HISTORICAL_VALIDATION_PUBLICATION_V1':
        raise ValueError('Wrong historical validation allowlist schema')
    accounted, included, omitted = set(), [], []
    allowed_prior = prior_art_allowlist()
    for group in ('files', 'omissions'):
        for record in body.get(group, []):
            name = record['path']
            path = canonical_relative(name)
            if name in accounted or name not in found or sha(path) != record['sha256']:
                raise ValueError('Invalid/duplicate/changed historical validation item: ' + name)
            if not isinstance(record.get('reason'), str) or not record['reason'].strip():
                raise ValueError('Each historical include/omission needs a visible reason')
            accounted.add(name)
            if group == 'files':
                if name.startswith('prior_art/') and name not in allowed_prior:
                    raise ValueError('Historical override cannot bypass prior_art frozen allowlist')
                included.append(path)
            else:
                omitted.append(record)
    if accounted != set(found):
        raise ValueError('Historical validation files lack an explicit disposition: ' +
                         ', '.join(sorted(set(found)-accounted)))
    return included, {'allowlist': HISTORICAL_ALLOWLIST, 'sha256': sha(source),
                      'included': body.get('files', []), 'omitted': omitted}


def selected_sources():
    history, disposition = historical_selection()
    files = source_current_root() + history
    unique = {p.relative_to(ROOT).as_posix(): p for p in files}
    if len(unique) != len(files):
        raise ValueError('Duplicate selected source')
    return [unique[k] for k in sorted(unique)], disposition


def validate_readable_index(index, sources):
    """Require exact current gzip coverage, hashes and chunk bytes, no stale extras."""
    import base64
    expected = {p.relative_to(ROOT).as_posix(): p for p in sources if p.suffix == '.gz'}
    seen, chunks = set(), []
    for record in index['artifacts']:
        name = record['restore_path']
        if name in seen or name not in expected:
            raise ValueError('Unexpected/duplicate readable artifact: ' + name)
        seen.add(name)
        raw = expected[name].read_bytes()
        if len(raw) != record['bytes'] or hashlib.sha256(raw).hexdigest() != record['sha256']:
            raise ValueError('Readable artifact differs from selected source: ' + name)
        decoded = []
        for i, part in enumerate(record['chunks']):
            path = canonical_relative(part['path'])
            if not part['path'].startswith('readable_evidence/') or part['index'] != i:
                raise ValueError('Invalid readable chunk path/order')
            data = path.read_bytes()
            block = base64.b64decode(data.strip(), validate=True)
            if sha(path) != part['text_sha256'] or len(block) != part['raw_bytes']:
                raise ValueError('Readable chunk changed')
            chunks.append(path)
            decoded.append(block)
        if b''.join(decoded) != raw:
            raise ValueError('Readable lossless roundtrip failed')
    if seen != set(expected) or len(chunks) != len(set(chunks)):
        raise ValueError('Incomplete/duplicate readable gzip coverage')
    return chunks
