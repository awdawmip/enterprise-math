"""Verbatim callable extracts from the observed repository source.
Source: awdawmip/enterprise-math@d40aa672623d6fc82af4cbb60964e6a628267e62
experiments/ns_native_event_capacity_d5c00d.py, blob
70e5cec37847d34fe0c4bcc4f5305fd224fca08d. This is NOT the full module.
Only definitions required to execute its published two-tick route are included.
"""
STARS = ((0, 2, 5), (0, 3, 4), (1, 2, 4), (1, 3, 5))
ZERO = (0,) * 6

def unit(i):
    return tuple(int(i==j) for j in range(6))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))

def frame_axes(frame, template=STARS):
    """Orient the current triple by the stored order of its three neighbors."""
    a,*others=frame
    ans=[]
    for b in others:
        shared=set(template[a]) & set(template[b])
        if len(shared)!=1:
            raise ValueError('template must have the stated pairwise intersections')
        ans.append(next(iter(shared)))
    return tuple(ans)

def macro_step(tokens, frame, template=STARS):
    if sorted(tokens)!=list(range(6)) or sorted(frame)!=list(range(4)):
        raise ValueError('distinct six tokens and four-event frame required')
    axes=frame_axes(frame,template)
    out=list(tokens)
    for k,i in enumerate(axes): out[axes[(k+1)%3]]=tokens[i]
    return tuple(out),frame[1:]+frame[:1]

def micro_path(tokens,frame,anchor=ZERO,template=STARS):
    """Return token-id indexed start/middle/end for a two-tick event.

    Frame and phase determine the entire next step; no external selector.
    At midpoint tokens carry the same current frame; commit rotates that frame.
    """
    axes=frame_axes(frame,template)
    start={tokens[i]:add(anchor,unit(i)) for i in range(6)}
    middle=dict(start);end=dict(start)
    for k,i in enumerate(axes):
        j=axes[(k+1)%3]
        middle[tokens[i]]=add(add(anchor,unit(i)),unit(j))
        end[tokens[i]]=add(anchor,unit(j))
    return start,middle,end
