"""Replay Phase32 machine observations at their original exact source and budget.

A replay match is content consistency, not source authentication or independent
mathematical acceptance. No pitch, precision, pixels or phase modulus is inferred.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from . import phase32_lab as p
from .multiplicative import parse_cell_scale_text, _cell_precision, _distinct_output_paths

MAX_REPORT_BYTES = 16 * 1024 * 1024
MAX_DECIMAL_DIGITS = 256  # Reader resource limit, not an arithmetic-domain claim.
REPORT_KEYS = frozenset((
    'schema', 'version', 'config', 'phase_modulus', 'cell_engine',
    'cell_pitch_source', 'cell_precision', 'cell_membership_exact', 'metrics',
    'multiplication', 'display_role', 'browser_startup', 'observation_scope',
))


def _exact_json(value: Any, depth: int = 0) -> None:
    if depth > 64:
        raise ValueError('Phase32 report exceeds reader nesting budget')
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise ValueError('Phase32 report keys must be strings')
        for child in value.values():
            _exact_json(child, depth + 1)
    elif type(value) is list:
        for child in value:
            _exact_json(child, depth + 1)
    elif value is not None and type(value) not in (str, int, bool):
        raise ValueError('Phase32 report permits no float or non-JSON values')


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False)


def _keys(value: Any, keys, name: str) -> None:
    if type(value) is not dict or set(value) != set(keys):
        raise ValueError(name + ': missing or unknown fields')


def _decimal(value: Any, name: str) -> int:
    if (type(value) is not str or not value or len(value) > MAX_DECIMAL_DIGITS
            or not value.isascii() or not value.isdecimal() or value[0] == '0'):
        raise ValueError(name + ': expected bounded canonical positive integer text')
    return int(value)


def parse_machine_report(text: str) -> dict:
    """Strict bounded JSON decoding; parsing alone does not verify the report."""
    if type(text) is not str or len(text.encode('utf-8')) > MAX_REPORT_BYTES:
        raise ValueError('Phase32 report exceeds reader byte budget')

    def reject(token):
        raise ValueError('inexact JSON token in Phase32 report: ' + token[:40])

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('duplicate Phase32 report key: ' + key)
            result[key] = value
        return result

    try:
        record = json.loads(text, parse_float=reject, parse_constant=reject,
                            object_pairs_hook=pairs)
        _exact_json(record)
        _keys(record, REPORT_KEYS, 'Phase32 report')
    except RecursionError as exc:
        raise ValueError('Phase32 report exceeds reader nesting budget') from exc
    return record


def load_machine_report(path: str | Path) -> dict:
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_REPORT_BYTES + 1)
    if len(raw) > MAX_REPORT_BYTES:
        raise ValueError('Phase32 report exceeds reader byte budget')
    return parse_machine_report(raw.decode('utf-8-sig'))


def _pitch_source(source: Any) -> tuple[int, int]:
    if type(source) is not dict:
        raise ValueError('Phase32 pitch source must be an object')
    ratio_keys = {'numerator', 'denominator', 'unreduced'}
    if set(source) == ratio_keys:
        # M18's direct Python machine_report also emits explicit integer-ratio
        # sources. Preserve that form; do not invent a lexical spelling for it.
        if source['unreduced'] is not True:
            raise ValueError('Phase32 pitch must retain its unreduced source')
        return p._cell_pitch((_decimal(source['numerator'], 'pitch numerator'),
                              _decimal(source['denominator'], 'pitch denominator')))
    _keys(source, ratio_keys | {'text', 'syntax'}, 'Phase32 lexical pitch source')
    pair, parsed = parse_cell_scale_text(source['text'])
    if _canonical(parsed) != _canonical(source):
        raise ValueError('Phase32 pitch spelling and integer source disagree')
    return pair


def _readout_scale(metrics: Any) -> int | None:
    if type(metrics) is not dict:
        raise ValueError('Phase32 metrics must be an object')
    scales = []
    for name in ('angular_cv_squared_exact', 'equal_area_cv_squared_exact'):
        ratio = metrics.get(name)
        if type(ratio) is not dict or 'readout' not in ratio:
            raise ValueError('missing Phase32 readout record: ' + name)
        readout = ratio['readout']
        if readout is None:
            scales.append(None)
        elif type(readout) is dict:
            scales.append(_decimal(readout.get('scale'), 'readout scale'))
        else:
            raise ValueError('Phase32 readout must be a record or null')
    if scales[0] != scales[1]:
        raise ValueError('Phase32 histogram readout scales disagree')
    return scales[0]


def replay_machine_report(report: dict) -> dict:
    """Return a detached model after checking every original report field.

    Uses the saved budget, not refinement. Changing source and all its results
    consistently can create another valid report; replay does not certify origin.
    """
    _exact_json(report)
    _keys(report, REPORT_KEYS, 'Phase32 report')
    if len(_canonical(report).encode('utf-8')) > MAX_REPORT_BYTES:
        raise ValueError('Phase32 report exceeds reader byte budget')
    record = copy.deepcopy(report)
    constants = {
        'schema': p.MACHINE_REPORT_SCHEMA, 'version': p.VERSION,
        'phase_modulus': str(p.DEN), 'cell_engine': 'CERTIFIED_INTEGER_RESIDUAL',
        'display_role': p.NO_DISPLAY, 'browser_startup': None,
        'observation_scope': 'FINITE_A2_OBSERVER_NOT_NATIVE_X6; NO_SOURCE_AUTHENTICATION',
    }
    for key, expected in constants.items():
        if _canonical(record[key]) != _canonical(expected):
            raise ValueError('Phase32 report contract mismatch at ' + key)
    cfg = p.checked_machine_config(record['config'])
    pair = _pitch_source(record['cell_pitch_source'])
    precision = record['cell_precision']
    _keys(precision, ('initial_bits', 'max_bits'), 'Phase32 precision')
    initial, maximum = _cell_precision(precision['initial_bits'], precision['max_bits'])
    scale = _readout_scale(record['metrics'])
    try:
        model = p.build(cfg, cell_pitch=pair, cell_bits=initial,
                        cell_max_bits=maximum, include_display=False)
        model['cell_pitch_source'] = copy.deepcopy(record['cell_pitch_source'])
        expected = p.machine_report(model, readout_scale=scale)
    except RuntimeError as exc:
        if 'Enterprise Math BRC' in str(exc):
            raise ValueError('Phase32 replay requires Enterprise Math BRC; no approximate fallback') from exc
        raise
    for key in sorted(REPORT_KEYS):
        # Typed JSON comparison: bool is not an integer, despite True == 1.
        if _canonical(record[key]) != _canonical(expected[key]):
            raise ValueError('Phase32 report replay mismatch at ' + key)
    return model


def _visual_data(model: dict, report: dict) -> dict:
    """Internal adapter for an already replayed pair; never infer missing cells."""
    data = copy.deepcopy(p.hex_data(model))
    data['metadata']['machine_config'] = copy.deepcopy(report['config'])
    data['metadata']['source_machine_report'] = copy.deepcopy(report)
    data['metadata']['machine_report_import'] = {
        'schema': p.MACHINE_REPORT_SCHEMA,
        'canonical_report_sha256': hashlib.sha256(_canonical(report).encode('utf-8')).hexdigest(),
        'validation': 'DETERMINISTIC_REPLAY_NOT_AUTHENTICITY',
        'observer': 'CERTIFIED_A2_CELL_CENTERS_NOT_ORIGINAL_POLAR_PIXELS',
    }
    from .core import validate
    return validate(data)


def machine_report_to_data(report: dict) -> dict:
    """Replay then adapt to the existing V2 carrier, retaining every identity."""
    _exact_json(report)
    record = copy.deepcopy(report)
    return _visual_data(replay_machine_report(record), record)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('input', type=Path, help='Phase32 machine report JSON')
    parser.add_argument('--verified-report', type=Path, help='save the checked observation unchanged')
    parser.add_argument('--hex-data', type=Path, help='V2 JSON or CSV; requires complete cells')
    args = parser.parse_args()
    try:
        paths = [x for x in (args.input, args.verified_report, args.hex_data) if x is not None]
        _distinct_output_paths(*paths)
        for i, left in enumerate(paths):
            for right in paths[:i]:
                if left.exists() and right.exists() and left.samefile(right):
                    raise ValueError('Phase32 report input/output paths must not alias')
        record = load_machine_report(args.input)
        model = replay_machine_report(record)
        data = _visual_data(model, record) if args.hex_data is not None else None
        text = json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
        # Validate all requested semantic conversions first; no I/O rollback claim.
        if args.verified_report is not None:
            args.verified_report.parent.mkdir(parents=True, exist_ok=True)
            args.verified_report.write_text(text, encoding='utf-8')
        if data is not None:
            from .core import write_data
            write_data(data, args.hex_data)
        print(json.dumps(dict(status='REPLAY_MATCHED', population=model['config']['count'],
                              cell_status=model['cell_membership_exact']['status'],
                              validation='DETERMINISTIC_REPLAY_NOT_AUTHENTICITY')))
        return 0
    except (ValueError, TypeError, OSError, UnicodeError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
