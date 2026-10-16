#!/usr/bin/env python3
"""CONTROL-only lossless ASCII Source carrier, post-job reporting phase.

No compression assumption, scientific import, recomputation or acceptance.
Source must contain every part in one immutable commit and full readback must
precede a Native small wrapper. This script does not upload or grant authority.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

RAW_CAP = 8 * 1024 * 1024
PART_CAP = 262144
INDEX_CAP = 32768
ENCODED_CAP = RAW_CAP + INDEX_CAP


def sha(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True,
                       allow_nan=False) + '\n').encode('ascii')


def write(path, data):
    with path.open('xb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())


def sync(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def pack(result_path, target, *, report_started_monotonic):
    # Genuine report start is recorded by the actor before any reporting work;
    # the 300s report ledger includes earlier semantic work too, never reset.
    if not 0 <= time.monotonic() - report_started_monotonic < 300:
        raise ValueError('expired or invalid semantic report clock')
    with result_path.open('rb') as f:
        data = f.read(RAW_CAP + 1)
    if len(data) > RAW_CAP:
        raise ValueError('result over original job output cap')
    data.decode('ascii')
    target.mkdir(mode=0o700)  # exclusive, never overwrite/replay
    parts = []
    for n, offset in enumerate(range(0, len(data), PART_CAP)):
        if time.monotonic() - report_started_monotonic >= 300:
            raise TimeoutError('semantic report deadline')
        part = data[offset:offset + PART_CAP]
        name = f'part-{n:02d}.txt'
        write(target / name, part)
        parts.append({'filename': name, 'bytes': len(part), 'sha256': sha(part),
                      'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(part)).encode() + b'\0' + part).hexdigest()})
    index = {'schema': 'PARITY_M7_LOSSLESS_ASCII_SOURCE_CARRIER_V1',
             'original_result_bytes': len(data), 'original_result_sha256': sha(data),
             'encoding': 'ASCII_BYTES_CONCATENATE_ORDERED_PARTS_NO_SEPARATORS',
             'parts': parts, 'parts_count': len(parts), 'part_cap_bytes': PART_CAP,
             'index_cap_bytes': INDEX_CAP, 'carrier_cap_bytes': ENCODED_CAP,
             'mathematical_acceptance': False, 'Native_Task_completion': False,
             'Source_publication': 'NOT_PERFORMED_BY_CODEC',
             'required_custody': 'ATOMIC_IMMUTABLE_ALL_PARTS_AND_INDEX_THEN_FULL_BYTE_READBACK_BEFORE_NATIVE_WRAPPER'}
    raw = json_bytes(index)
    if len(parts) > 32 or len(raw) > INDEX_CAP or len(data) + len(raw) > ENCODED_CAP:
        raise ValueError('carrier exceeds fixed resource plan')
    if time.monotonic() - report_started_monotonic >= 300:
        raise TimeoutError('semantic report deadline before index')
    write(target / 'INDEX.json', raw)
    sync(target)
    sync(target.parent)
    return index


def unpack(directory):
    with (directory / 'INDEX.json').open('rb') as f:
        raw = f.read(INDEX_CAP + 1)
    if len(raw) > INDEX_CAP:
        raise ValueError('oversize index')
    index = json.loads(raw)
    if index['schema'] != 'PARITY_M7_LOSSLESS_ASCII_SOURCE_CARRIER_V1':
        raise ValueError('wrong carrier schema')
    if type(index['original_result_bytes']) is not int or not 0 <= index['original_result_bytes'] <= RAW_CAP:
        raise ValueError('wrong original bound')
    if len(index['parts']) > 32 or index['parts_count'] != len(index['parts']):
        raise ValueError('wrong part count')
    chunks, total = [], 0
    for n, member in enumerate(index['parts']):
        if member['filename'] != f'part-{n:02d}.txt':
            raise ValueError('noncanonical part name/order')
        with (directory / member['filename']).open('rb') as f:
            part = f.read(PART_CAP + 1)
        total += len(part)
        if len(part) > PART_CAP or total > RAW_CAP or len(part) != member['bytes'] or sha(part) != member['sha256']:
            raise ValueError('carrier byte mismatch')
        blob = hashlib.sha1(b'blob ' + str(len(part)).encode() + b'\0' + part).hexdigest()
        if blob != member['git_blob_sha1']:
            raise ValueError('carrier Git blob mismatch')
        part.decode('ascii')
        chunks.append(part)
    data = b''.join(chunks)
    if len(data) != index['original_result_bytes'] or sha(data) != index['original_result_sha256']:
        raise ValueError('reconstructed original differs')
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', type=Path, required=True)
    parser.add_argument('--carrier-dir', type=Path, required=True)
    parser.add_argument('--genuine-report-start-monotonic', type=float, required=True)
    args = parser.parse_args()
    result = pack(args.result, args.carrier_dir,
                  report_started_monotonic=args.genuine_report_start_monotonic)
    print(json.dumps({'parts': result['parts_count'], 'bytes': result['original_result_bytes'],
                      'sha256': result['original_result_sha256'], 'Native_Task_completion': False}))
