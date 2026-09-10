"""Static-site generation and local preview for Nollm Visual Toolkit.

The web layer is an observer/export surface only. It does not alter record identity,
coordinates, relations, or mathematical semantics.
"""
from __future__ import annotations

import contextlib
import html as html_lib
import ipaddress
import json
import re
import threading
import urllib.parse
import webbrowser
from dataclasses import dataclass
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterable, Sequence

from .core import VERSION, demo_hex, demo_x6, fingerprint, html, validate
from .multiplicative import DEFAULT_SEED, config_fingerprint, multiplicative_config, multiplicative_html

SITE_SCHEMA = "NOLLM_VISUAL_SITE_V1"
_SLUG_RE = re.compile(r"[^A-Za-z0-9._-]+")


def _slug(label: str, fallback: str = "view") -> str:
    value = _SLUG_RE.sub("-", label.strip()).strip("-._")
    return (value or fallback)[:80]


def _dedupe_slug(candidate: str, used: set[str]) -> str:
    stem = candidate
    i = 2
    while candidate.casefold() in used:
        candidate = f"{stem}-{i}"
        i += 1
    used.add(candidate.casefold())
    return candidate


def _landing_page(title: str, pages: Sequence[dict[str, object]]) -> str:
    safe_title = html_lib.escape(title, quote=True)
    cards = []
    links = []
    for i, page in enumerate(pages):
        label = html_lib.escape(str(page["label"]), quote=True)
        href = html_lib.escape(str(page["href"]), quote=True)
        kind = html_lib.escape(str(page["kind"]), quote=True)
        sha = html_lib.escape(str(page["sha256"]), quote=True)
        active = " active" if i == 0 else ""
        cards.append(
            f'<button class="card{active}" data-href="{href}" type="button">'
            f'<strong>{label}</strong><span>{kind} · {page["records"]:,} records</span>'
            f'<code>{sha[:16]}…</code></button>'
        )
        links.append(f'<li><a href="{href}">{label}</a></li>')
    first = html_lib.escape(str(pages[0]["href"]), quote=True) if pages else ""
    cards_html = "\n".join(cards)
    links_html = "\n".join(links)
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe_title} · Nollm Visual Toolkit {VERSION}</title>
<style>
:root{{--ink:#182330;--muted:#61717f;--line:#d7dfe5;--paper:#f3f5f7;--accent:#245678}}*{{box-sizing:border-box}}body{{margin:0;font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--paper)}}header{{padding:14px 18px;background:#172a39;color:white;display:flex;justify-content:space-between;gap:12px;align-items:center}}h1{{font-size:18px;margin:0}}header small{{opacity:.75}}main{{display:grid;grid-template-columns:280px minmax(0,1fr);height:calc(100vh - 58px)}}nav{{padding:12px;overflow:auto;background:white;border-right:1px solid var(--line)}}.card{{display:flex;width:100%;text-align:left;flex-direction:column;gap:3px;padding:10px;margin:0 0 8px;border:1px solid var(--line);border-radius:8px;background:white;color:var(--ink);cursor:pointer}}.card:hover,.card.active{{border-color:var(--accent);background:#eef3f7}}.card span{{font-size:12px;color:var(--muted)}}.card code{{font-size:10px;color:var(--muted)}}section{{min-width:0;min-height:0}}iframe{{width:100%;height:100%;border:0;background:white}}.hint{{font-size:11px;color:var(--muted);margin:10px 2px}}@media(max-width:700px){{main{{display:flex;flex-direction:column;height:auto}}nav{{border-right:0;border-bottom:1px solid var(--line);max-height:220px}}section{{height:calc(100vh - 278px);min-height:520px}}header small{{display:none}}}}
</style></head><body>
<header><h1>{safe_title}</h1><small>Nollm Visual Toolkit {VERSION} · static preview · offline/no telemetry</small></header>
<main><nav>{cards_html}<p class="hint">Each workbench is self-contained. The landing page only switches observer pages; it does not merge or rewrite data.</p><noscript><ul>{links_html}</ul></noscript></nav><section><iframe id="preview" title="workbench preview" src="{first}"></iframe></section></main>
<script>'use strict';const frame=document.getElementById('preview');for(const b of document.querySelectorAll('.card'))b.addEventListener('click',()=>{{for(const x of document.querySelectorAll('.card'))x.classList.remove('active');b.classList.add('active');frame.src=b.dataset.href;}});</script>
</body></html>'''


def build_site(
    datasets: Iterable[tuple[str, dict]],
    out_dir: str | Path,
    *,
    title: str = "Nollm Visual Preview",
) -> dict[str, object]:
    """Generate a static landing page plus self-contained workbench pages.

    The output is deterministic for the same ordered datasets and title. No clock,
    host path, random value, or remote resource is embedded.
    """
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    used: set[str] = set()
    pages: list[dict[str, object]] = []
    for index, (label, data) in enumerate(datasets, start=1):
        if not isinstance(label, str) or not label.strip():
            raise ValueError("Site labels must be nonempty strings")
        validate(data)
        slug = _dedupe_slug(_slug(label, f"view-{index}"), used)
        filename = f"{slug}.html"
        html(data, out / filename)
        pages.append({
            "label": label,
            "href": filename,
            "kind": data["kind"],
            "records": len(data["records"]),
            "sha256": fingerprint(data),
        })
    if not pages:
        raise ValueError("At least one dataset is required")
    manifest: dict[str, object] = {
        "schema": SITE_SCHEMA,
        "toolkit_version": VERSION,
        "title": title,
        "pages": pages,
        "observer_boundary": "Static HTML preview only; native identities and source coordinates are unchanged.",
    }
    _write_site(out, manifest)
    return manifest



def _write_site(out: Path, manifest: dict[str, object]) -> None:
    (out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (out / "index.html").write_text(_landing_page(str(manifest["title"]), manifest["pages"]), encoding="utf-8")


def add_multiplicative_page(
    manifest: dict[str, object],
    out_dir: str | Path,
    *,
    count: int = 65536,
    seed: int = DEFAULT_SEED,
    label: str = "multiplicative-field",
) -> dict[str, object]:
    """Add a self-contained multiplicative-field observer to an existing generated site."""
    out = Path(out_dir)
    if manifest.get("schema") != SITE_SCHEMA or not isinstance(manifest.get("pages"), list):
        raise ValueError("Expected a NOLLM_VISUAL_SITE_V1 manifest")
    used = {Path(str(page["href"])).stem.casefold() for page in manifest["pages"]}
    slug = _dedupe_slug(_slug(label, "multiplicative-field"), used)
    href = f"{slug}.html"
    config = multiplicative_config(count=count, seed=seed)
    multiplicative_html(out / href, count=count, seed=seed)
    manifest["pages"].append({
        "label": label,
        "href": href,
        "kind": "multiplicative-field-observer",
        "records": count,
        "sha256": config_fingerprint(config),
    })
    _write_site(out, manifest)
    return manifest

def demo_site(
    out_dir: str | Path,
    *,
    hex_count: int = 65536,
    include_x6: bool = True,
    title: str = "Nollm Visual Preview",
    include_multiplicative: bool = False,
    multiplicative_seed: int = DEFAULT_SEED,
) -> dict[str, object]:
    datasets: list[tuple[str, dict]] = [(f"hex-{hex_count}", demo_hex(hex_count))]
    if include_x6:
        datasets.append(("x6-729", demo_x6()))
    manifest = build_site(datasets, out_dir, title=title)
    if include_multiplicative:
        add_multiplicative_page(manifest, out_dir, count=hex_count, seed=multiplicative_seed)
    return manifest


def _is_loopback_host(host: str) -> bool:
    if host.casefold() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


class _PreviewHandler(SimpleHTTPRequestHandler):
    server_version = "NollmPreview/0.4"

    def log_message(self, fmt: str, *args: object) -> None:
        if getattr(self.server, "quiet", False):
            return
        super().log_message(fmt, *args)

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()

    def _scope_file(self) -> bool:
        target = getattr(self.server, "single_file", None)
        if target is None:
            return True
        path = urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
        allowed = {"/", "/" + target.name}
        if path not in allowed:
            self.send_error(404, "Preview is scoped to one generated HTML file")
            return False
        if path == "/":
            self.path = "/" + urllib.parse.quote(target.name)
        return True

    def do_GET(self) -> None:
        if self._scope_file():
            super().do_GET()

    def do_HEAD(self) -> None:
        if self._scope_file():
            super().do_HEAD()


@dataclass
class PreviewHandle:
    server: ThreadingHTTPServer
    thread: threading.Thread
    url: str

    def close(self) -> None:
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.server.server_close()


@contextlib.contextmanager
def preview_server(
    target: str | Path,
    *,
    host: str = "127.0.0.1",
    port: int = 0,
    allow_remote: bool = False,
    quiet: bool = True,
):
    """Serve a generated HTML file or site directory on a bounded local server."""
    target = Path(target).resolve()
    if not target.exists():
        raise FileNotFoundError(target)
    if target.is_file() and target.suffix.lower() not in {".html", ".htm"}:
        raise ValueError("Preview file must be HTML; preview a directory for multi-file sites")
    if not _is_loopback_host(host) and not allow_remote:
        raise ValueError("Non-loopback preview requires allow_remote=True")
    if not isinstance(port, int) or isinstance(port, bool) or not 0 <= port <= 65535:
        raise ValueError("port must be an integer in 0..65535")
    root = target if target.is_dir() else target.parent
    single_file = None if target.is_dir() else target

    def handler(*args, **kwargs):
        return _PreviewHandler(*args, directory=str(root), **kwargs)

    server = ThreadingHTTPServer((host, port), handler)
    server.daemon_threads = True
    server.quiet = quiet
    server.single_file = single_file
    bound_host, bound_port = server.server_address[:2]
    shown_host = host
    if host in {"0.0.0.0", "::"}:
        shown_host = "127.0.0.1" if host == "0.0.0.0" else "[::1]"
    if target.is_dir():
        suffix = "/"
    else:
        suffix = "/" + urllib.parse.quote(target.name)
    url = f"http://{shown_host}:{bound_port}{suffix}"
    thread = threading.Thread(target=server.serve_forever, name="nollm-viz-preview", daemon=True)
    thread.start()
    handle = PreviewHandle(server=server, thread=thread, url=url)
    try:
        yield handle
    finally:
        handle.close()


def serve_preview(
    target: str | Path,
    *,
    host: str = "127.0.0.1",
    port: int = 0,
    allow_remote: bool = False,
    open_browser: bool = True,
) -> str:
    """Run a preview until Ctrl-C; returns the URL after orderly shutdown."""
    with preview_server(target, host=host, port=port, allow_remote=allow_remote, quiet=False) as handle:
        print(f"Preview: {handle.url}")
        if open_browser:
            webbrowser.open(handle.url, new=2)
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            print("\nPreview stopped.")
        return handle.url
