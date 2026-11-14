"""Request-local reuse of pure reads over a caller-owned immutable input view.

The backend enables this only for read operations on its private invocation
view. CLI tools and writers do not opt in. No files, hashes or certificates are
created; each invocation discards its ordinary in-memory results on exit.
"""
from contextlib import contextmanager
from contextvars import ContextVar
from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class _ReadView:
    root: Path
    values: dict = field(default_factory=dict)
    computing: set = field(default_factory=set)
    active: bool = True


_CURRENT = ContextVar('research_request_read_view', default=None)


@contextmanager
def read_view(root):
    target=Path(root).resolve()
    prior=_CURRENT.get()
    if prior is not None and prior.active and prior.root==target:
        yield
        return
    view=_ReadView(target)
    token=_CURRENT.set(view)
    try:
        yield
    finally:
        view.active=False
        view.values.clear()
        view.computing.clear()
        _CURRENT.reset(token)


def reuse_read(root, key, inputs, compute):
    view=_CURRENT.get()
    if view is None or not view.active or view.root!=Path(root).resolve() or key in view.computing:
        return compute()
    saved=view.values.get(key)
    if saved is not None and saved[0]==inputs:
        return deepcopy(saved[1])
    view.computing.add(key)
    try:
        result=compute()
        view.values[key]=(deepcopy(inputs),deepcopy(result))
        return result
    finally:
        view.computing.discard(key)
