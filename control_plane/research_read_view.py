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
_ATOMIC_READ_TYPES = frozenset({type(None),bool,int,float,complex,str,bytes})


def _copy_read(value,memo=None):
    """Keep deepcopy semantics while handling ordinary JSON containers directly."""
    kind=type(value)
    if kind in _ATOMIC_READ_TYPES:return value
    if memo is None:memo={}
    identity=id(value)
    if identity in memo:return memo[identity]
    if kind is dict:
        result={};memo[identity]=result
        for key,child in value.items():result[_copy_read(key,memo)]=_copy_read(child,memo)
        return result
    if kind is list:
        result=[];memo[identity]=result
        result.extend(_copy_read(child,memo) for child in value)
        return result
    if kind is tuple:
        children=[_copy_read(child,memo) for child in value]
        # A tuple can participate in a cycle through a mutable child.
        if identity in memo:return memo[identity]
        result=value if all(a is b for a,b in zip(value,children)) else tuple(children)
        memo[identity]=result
        return result
    return deepcopy(value,memo)


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
        return _copy_read(saved[1])
    view.computing.add(key)
    try:
        result=compute()
        view.values[key]=(_copy_read(inputs),_copy_read(result))
        return result
    finally:
        view.computing.discard(key)


_SOURCE = ContextVar('research_immutable_source_view', default=None)


def _copy_source(value):
    # The loaders return accepted JSON records, not arbitrary Python objects.
    if isinstance(value, dict):
        return {key: _copy_source(child) for key, child in value.items()}
    if isinstance(value, list):
        return [_copy_source(child) for child in value]
    return value


@contextmanager
def immutable_source_view(root):
    """Raw records only, across bootstrap on a host-owned immutable read input.

    Adapter installation changes operational interpretation. This separate
    scope never caches that interpretation, authorization, or a current owner.
    CLI/writer paths do not enable it; every new native input gets a new scope.
    """
    target = Path(root).resolve()
    prior = _SOURCE.get()
    if prior is not None and prior.active and prior.root == target:
        yield
        return
    view = _ReadView(target)
    token = _SOURCE.set(view)
    try:
        yield
    finally:
        view.active = False
        view.values.clear()
        _SOURCE.reset(token)


def source_rows(root, key, compute):
    view = _SOURCE.get()
    if view is None or not view.active or view.root != Path(root).resolve():
        return compute()
    identity = ('rows', key)
    if identity not in view.values:
        view.values[identity] = compute()
    return _copy_source(view.values[identity])


def source_object(path, compute):
    view = _SOURCE.get()
    if view is None or not view.active:
        return compute()
    try:
        relative = Path(path).relative_to(view.root)
    except ValueError:
        return compute()
    if '..' in relative.parts:
        return compute()
    identity = ('object', relative.as_posix())
    if identity not in view.values:
        view.values[identity] = compute()
    return _copy_source(view.values[identity])
