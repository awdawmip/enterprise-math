"""Compatibility shim for repository-root review-evidence storage semantics."""
from __future__ import annotations

import research_review_evidence_store as _impl

for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

ROOT = _impl.ROOT
