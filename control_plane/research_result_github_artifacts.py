"""Read the actual committed bytes selected for a Result, independently of main.

Only the existing public enterprise-math repository is supported. A commit/path
identifies input content, never a current-branch membership or output permission.
The process-local cache is bounded; historical checkout trees are not retained.
"""
from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from functools import lru_cache
import hashlib
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import quote
from urllib.request import build_opener, HTTPRedirectHandler, ProxyHandler, Request

REPOSITORY = "awdawmip/enterprise-math"
MAX_ARTIFACT_BYTES = 32 * 1024 * 1024
_FREEZE_SOURCES = ContextVar("result_github_sources", default=None)


class GithubArtifactError(ValueError):
    pass


def relative_path(value):
    if (not isinstance(value, str) or not value or "\\" in value or ":" in value
            or PurePosixPath(value).is_absolute() or ".." in PurePosixPath(value).parts
            or PurePosixPath(value).as_posix() != value or value == "."):
        raise GithubArtifactError("invalid GitHub artifact relative path")
    return value


def normalize_sources(sources):
    if not isinstance(sources, list) or not sources:
        raise GithubArtifactError("artifact_sources must be a nonempty list")
    values = []
    seen = set()
    for raw in sources:
        if not isinstance(raw, dict) or raw.get("repository") != REPOSITORY:
            raise GithubArtifactError("artifact repository is outside this project")
        path = relative_path(raw.get("path"))
        commit, blob = raw.get("source_commit"), raw.get("git_blob_sha1")
        if (not isinstance(commit, str) or re.fullmatch(r"[0-9a-f]{40}", commit) is None
                or not isinstance(blob, str) or re.fullmatch(r"(?:sha1:)?[0-9a-f]{40}", blob) is None
                or path in seen):
            raise GithubArtifactError("invalid or duplicate committed artifact reference")
        seen.add(path)
        value = {key: raw[key] for key in ("repository", "source_commit", "path", "git_blob_sha1")}
        if "sha256" in raw:
            digest = raw["sha256"]
            if not isinstance(digest, str) or re.fullmatch(r"(?:sha256:)?[0-9a-f]{64}", digest) is None:
                raise GithubArtifactError("invalid artifact SHA-256")
            value["sha256"] = digest
        values.append(value)
    return values


@contextmanager
def freeze_sources(sources):
    token = _FREEZE_SOURCES.set(None if sources is None else normalize_sources(sources))
    try:
        yield
    finally:
        _FREEZE_SOURCES.reset(token)


def current_freeze_sources():
    return _FREEZE_SOURCES.get()


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise GithubArtifactError("GitHub artifact redirect was not followed")


@lru_cache(maxsize=8)
def _committed_bytes(commit, path, root):
    # A normal developer checkout can satisfy the same read from its Git store.
    if (Path(root) / ".git").exists():
        try:
            result = subprocess.run(["git", "-C", root, "show", commit + ":" + path],
                                    capture_output=True, timeout=30, check=False)
        except (OSError, subprocess.SubprocessError):
            result = None
        if result is not None and result.returncode == 0:
            if len(result.stdout) > MAX_ARTIFACT_BYTES:
                raise GithubArtifactError("GitHub artifact exceeds reader byte capacity")
            return result.stdout
    # Archive-based native workers have no Git store or API credentials. Read
    # the selected immutable public URL, never the current working-tree path.
    url = "https://raw.githubusercontent.com/" + REPOSITORY + "/" + commit + "/" + quote(path, safe="/")
    try:
        opener = build_opener(ProxyHandler({}), _NoRedirect())
        with opener.open(Request(url, headers={"User-Agent": "Enterprise-Math-Result-Reader"}), timeout=20) as response:
            data = response.read(MAX_ARTIFACT_BYTES + 1)
    except (OSError, ValueError) as exc:
        raise GithubArtifactError("committed GitHub artifact bytes unavailable") from exc
    if len(data) > MAX_ARTIFACT_BYTES:
        raise GithubArtifactError("GitHub artifact exceeds reader byte capacity")
    return data


def read_reference(source, root):
    pin = normalize_sources([source])[0]
    data = _committed_bytes(pin["source_commit"], pin["path"], str(Path(root).resolve()))
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    digest = hashlib.sha256(data).hexdigest()
    if blob != pin["git_blob_sha1"].removeprefix("sha1:"):
        raise GithubArtifactError("selected GitHub artifact blob does not match actual bytes")
    if pin.get("sha256", "sha256:" + digest).removeprefix("sha256:") != digest:
        raise GithubArtifactError("selected GitHub artifact SHA-256 does not match actual bytes")
    return data


def artifact_pin(source, root):
    pin = normalize_sources([source])[0]
    data = read_reference(pin, root)
    return {**pin, "git_blob_sha1": pin["git_blob_sha1"].removeprefix("sha1:"),
            "sha256": hashlib.sha256(data).hexdigest()}


def reference_manifest(sources, paths, root):
    pins = normalize_sources(sources)
    if {pin["path"] for pin in pins} != set(paths):
        raise GithubArtifactError("artifact references must identify the selected Result inputs")
    manifest = []
    for pin in pins:
        actual = artifact_pin(pin, root)
        manifest.append({"repository": pin["repository"], "source_commit": pin["source_commit"],
                         "path": pin["path"], "git_blob_sha1": "sha1:" + actual["git_blob_sha1"],
                         "sha256": "sha256:" + actual["sha256"]})
    return pins, manifest


def audit_references(item, root):
    pins, actual = reference_manifest(item["artifact_sources"],
                                     [row["path"] for row in item["output_manifest"]], root)
    expected = {row["path"]: row for row in item["output_manifest"]}
    for row in actual:
        old = expected[row["path"]]
        if (row["git_blob_sha1"].removeprefix("sha1:") != str(old.get("git_blob_sha1", "")).removeprefix("sha1:")
                or row["sha256"] != old.get("sha256")):
            raise GithubArtifactError("Result artifact digest differs from its selected GitHub content")
    returned = expected.get(item.get("return_path"))
    if (returned is None or str(returned.get("git_blob_sha1", "")).removeprefix("sha1:")
            != str(item.get("return_blob_sha1", "")).removeprefix("sha1:")
            or returned.get("sha256") != item.get("return_sha256")):
        raise GithubArtifactError("Result return digest differs from its selected GitHub content")
