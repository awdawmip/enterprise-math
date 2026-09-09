# Retrospective v1 runner provenance

This note is written after v1. It is not the script file used by v1, an independently rerun execution, or a replacement for its immutable receipt.

The actual v1 command ran at 2026-09-09T00:43:07.130375+00:00 through inline tool orchestration (session tool output chunk `dedf6a`). Its exact child argv, source pins, timestamps and stdout/stderr hashes remain in `runs/identity_v1/receipt.json`, SHA256 `d67a19adaf231cca83394206e865d2b5a869034ffef78530e5cc1ab6b8ba7a36`. The inline parent used `subprocess.run(argv, cwd=root, capture_output=True, timeout=600)`. This is the retained invocation fragment, not a claim that a full original runner file existed or that its bytes were separately archived.

The 600-second parent timeout is distinct from the child cooperative deadline and its 4096 MiB Windows Job memory ceiling. No measured memory peak was recorded. The peer review records which facts were supplied by the author and which it inspected; it did not rerun the identity mathematics.

The original `.py.frozen` copy is an exact source archive. The peer's direct archive-help probe failed because that file's relative ROOT calculation assumed its canonical original path. Its raw `archive-help.stdout` and `archive-help.stderr` are preserved verbatim next to this review package. Replaying v1 requires restoring the archive to the canonical `check_exact_map.py` path in an isolated checkout (or using immutable source commit `341f36bb53c25d97c3ae533a71c92ad273a7b904`) and choosing the v1 certificate explicitly with `--output`. Do not compare a v1 source against the new primary certificate.

The newly stored `runs/placement_v3_final/replay.py` really was executed for v3 and accepts explicit root/output paths. It does not retroactively become v1's runner. No v1 source, receipt, certificate or probe output was changed in preparing this note.
