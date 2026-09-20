"""Replay M12 machine reports through the existing exact field and data readers.

Replay checks deterministic contents, not authorship or independent mathematical
acceptance. Display startup is an explicit projection; it never rewrites the
machine source or supplies a missing precision budget.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from . import multiplicative as m

# Reader resource limits, not restrictions on the underlying arithmetic domain.
MAX_REPORT_BYTES = 16 * 1024 * 1024
MAX_HISTOGRAM_CELLS = 262144
REPORT_KEYS = frozenset((
    'schema', 'lab_version', 'config', 'statistics', 'all_pairs', 'cell_engine',
    'cell_scale_source', 'cell_membership_exact', 'browser_startup',
    'html_observer_boundary', 'display_role', 'cell_precision',
))


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False)


def _exact_json(value: Any, depth: int = 0) -> None:
    if depth > 64:
        raise ValueError('machine report exceeds the reader nesting budget')
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise ValueError('machine report keys must be strings')
        for child in value.values():
            _exact_json(child, depth + 1)
    elif type(value) is list:
        for child in value:
            _exact_json(child, depth + 1)
    elif value is not None and type(value) not in (str, int, bool):
        raise ValueError('machine report permits no float or non-JSON values')


def _keys(value: Any, keys: set[str] | frozenset[str], name: str) -> None:
    if type(value) is not dict or set(value) != keys:
        raise ValueError(name + ': missing or unknown fields')


def parse_machine_report(text: str) -> dict:
    """Decode without floating conversion, duplicate keys or nonfinite tokens."""
    if type(text) is not str or len(text.encode('utf-8')) > MAX_REPORT_BYTES:
        raise ValueError('machine report exceeds the reader byte budget')

    def reject(token):
        raise ValueError('inexact JSON token in machine report: ' + token)

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('duplicate machine report key: ' + key)
            result[key] = value
        return result

    try:
        record = json.loads(text, parse_float=reject, parse_constant=reject,
                            object_pairs_hook=pairs)
        _exact_json(record)
        _keys(record, REPORT_KEYS, 'machine report')
    except RecursionError as exc:
        raise ValueError('machine report exceeds the reader nesting budget') from exc
    return record


def load_machine_report(path: str | Path) -> dict:
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_REPORT_BYTES + 1)
    if len(raw) > MAX_REPORT_BYTES:
        raise ValueError('machine report exceeds the reader byte budget')
    return parse_machine_report(raw.decode('utf-8-sig'))


def _observation_options(statistics: Any) -> tuple[int, int, int | None]:
    if type(statistics) is not dict:
        raise ValueError('machine statistics must be an object')
    rings, sectors = statistics.get('rings'), statistics.get('sectors')
    if any(type(x) is not int or x <= 0 for x in (rings, sectors)):
        raise ValueError('histogram dimensions must be positive exact integers')
    if rings * sectors > MAX_HISTOGRAM_CELLS:
        raise ValueError('histogram exceeds reader allocation budget, not arithmetic domain')
    scales = []
    for key in ('angular_cv_squared_exact', 'area_sector_cv_squared_exact'):
        ratio = statistics.get(key)
        if type(ratio) is not dict:
            raise ValueError('missing exact histogram record: ' + key)
        if ratio.get('readout') is None:
            scales.append(None)
            continue
        readout = ratio['readout']
        scale = readout.get('scale') if type(readout) is dict else None
        if (type(scale) is not str or not scale.isascii() or not scale.isdigit()
                or len(scale) > 256 or scale.startswith('0')):
            raise ValueError('invalid exact readout scale in report')
        scales.append(int(scale))
    if scales[0] != scales[1]:
        raise ValueError('histogram readout scales disagree')
    return rings, sectors, scales[0]


def replay_machine_report(report: dict) -> dict:
    """Rebuild exactly at the saved budget; reject every mismatching output.

    The returned field is a detached mutable result, not an authentication token.
    A report with consistently changed sources is a different valid source, not
    something this deterministic replay can identify as a forged author record.
    """
    _exact_json(report)
    _keys(report, REPORT_KEYS, 'machine report')
    record = copy.deepcopy(report)
    constants = {
        'schema': m.MACHINE_REPORT_SCHEMA, 'lab_version': m.LAB_VERSION,
        'cell_engine': 'CERTIFIED_INTEGER_RESIDUAL', 'browser_startup': None,
        'html_observer_boundary': 'NOT_GENERATED_MACHINE_ONLY',
        'display_role': m.NO_DISPLAY,
    }
    for key, expected in constants.items():
        if _canonical(record[key]) != _canonical(expected):
            raise ValueError('machine report contract mismatch at ' + key)
    cfg = m.checked_machine_config(record['config'])
    source = record['cell_scale_source']
    _keys(source, {'text', 'syntax', 'numerator', 'denominator', 'unreduced'}, 'scale source')
    pair, parsed_source = m.parse_cell_scale_text(source['text'])
    if _canonical(source) != _canonical(parsed_source):
        raise ValueError('scale spelling and exact source disagree')
    budget = record['cell_precision']
    _keys(budget, {'initial_bits', 'max_bits'}, 'cell precision')
    initial, maximum = m._cell_precision(budget['initial_bits'], budget['max_bits'])
    rings, sectors, scale = _observation_options(record['statistics'])
    field = m.build_field(cfg, cell_scale=pair, cell_bits=initial,
                          cell_max_bits=maximum, include_display=False)
    field['cell_scale_source'] = copy.deepcopy(parsed_source)
    expected = {
        **constants, 'config': cfg,
        'statistics': m.statistics(field, rings, sectors, readout_scale=scale),
        'all_pairs': m.all_pair_audit(field),
        'cell_scale_source': parsed_source,
        'cell_membership_exact': m.cell_membership_summary(field),
        'cell_precision': budget,
    }
    # JSON-level comparison distinguishes false/0 and true/1 as well as strings.
    for key in REPORT_KEYS:
        if _canonical(record[key]) != _canonical(expected[key]):
            raise ValueError('machine report replay mismatch at ' + key)
    return field


def _visual_data(field: dict, report: dict) -> dict:
    data = m.hex_data(field)  # Reject unresolved/out-of-carrier cells; never guess.
    data['metadata']['machine_report_import'] = {
        'schema': m.MACHINE_REPORT_SCHEMA,
        'canonical_report_sha256': hashlib.sha256(_canonical(report).encode('utf-8')).hexdigest(),
        'validation': 'DETERMINISTIC_REPLAY_NOT_AUTHENTICITY',
        'source_statistics': copy.deepcopy(report['statistics']),
    }
    from .core import validate
    return validate(data)


def machine_report_to_data(report: dict) -> dict:
    """Adapt to the existing visual-data V2 carrier without approximate pixels."""
    return _visual_data(replay_machine_report(report), report)


def _startup(field: dict, report: dict, *, display_scale: int | float) -> dict:
    if _observation_options(report['statistics']) != (8, 32, 1000000):
        raise ValueError('browser startup uses fixed 8/32/1000000 readouts; custom report observations require a separate display adapter')
    cfg = field['config']
    display = m.config(cfg['count'], cfg['scheme'], display_scale, cfg['overrides'])
    budget = field['cell_precision']
    return m.browser_startup(display, cell_scale_text=field['cell_scale_source']['text'],
                             cell_bits=budget['initial_bits'], cell_max_bits=budget['max_bits'])


def machine_report_startup(report: dict, *, display_scale: int | float) -> dict:
    """Explicitly create a browser seed, not a browser execution receipt.

    The exact source and precision do not change; browser range is checked by
    the existing startup function. No missing display scale is inferred.
    """
    return _startup(replay_machine_report(report), report, display_scale=display_scale)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('input', type=Path, help='M12 machine report JSON')
    parser.add_argument('--verified-report', type=Path, help='preserve the checked report')
    parser.add_argument('--hex-data', type=Path, help='existing visual-data V2 JSON or CSV')
    parser.add_argument('--startup', type=Path, help='explicit existing browser startup JSON')
    parser.add_argument('--display-scale', help='required only for --startup; display-only')
    args = parser.parse_args()
    try:
        if (args.startup is None) != (args.display_scale is None):
            raise ValueError('--startup and --display-scale must be supplied together')
        paths = [p for p in (args.input, args.verified_report, args.hex_data, args.startup) if p is not None]
        m._distinct_output_paths(*paths)
        for i, left in enumerate(paths):
            for right in paths[:i]:
                if left.exists() and right.exists() and left.samefile(right):
                    raise ValueError('input/output paths refer to the same file')
        record = load_machine_report(args.input)
        field = replay_machine_report(record)
        data = _visual_data(field, record) if args.hex_data is not None else None
        startup = (_startup(field, record, display_scale=float(args.display_scale))
                   if args.startup is not None else None)
        # All semantic conversions precede writes. I/O rollback is not claimed.
        if args.verified_report is not None:
            args.verified_report.parent.mkdir(parents=True, exist_ok=True)
            args.verified_report.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        if data is not None:
            from .core import write_data
            write_data(data, args.hex_data)
        if startup is not None:
            args.startup.parent.mkdir(parents=True, exist_ok=True)
            args.startup.write_text(json.dumps(startup, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(json.dumps({'status': 'REPLAY_MATCHED',
                          'cell_status': field['cell_membership_exact']['status'],
                          'population': field['config']['count'],
                          'scope': 'deterministic replay; not source authentication or browser execution'}))
        return 0
    except (ValueError, TypeError, OSError, UnicodeError) as exc:
        parser.exit(2, f'error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
