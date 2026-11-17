"""Out-of-module source-call profiler for immutable X6 signed BRC checks.

Usage: python [-O|-OO] X6_UNIT109_NATIVE_CALL_TRACE_20261118.py PATH_TO_UNIT108_CHECKER
Set X6_TRACE_PATH to a writable output .json file. A profile event counts real Python call frames.
"""
import sys, collections, runpy, json, os, atexit
counts = collections.Counter()
def tracer(frame, event, arg):
    if event == 'call' and frame.f_code.co_filename.endswith('/x6_signed_native_spatial_v16_20260905/signed_brc.py'):
        counts[frame.f_code.co_name] += 1
sys.setprofile(tracer)
def write():
    with open(os.environ['X6_TRACE_PATH'], 'w', encoding='utf-8') as f:
        json.dump(dict(counts), f, sort_keys=True)
atexit.register(write)
sys.argv = [sys.argv[1]]
runpy.run_path(sys.argv[0], run_name='__main__')
