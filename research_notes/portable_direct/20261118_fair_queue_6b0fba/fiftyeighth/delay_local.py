"""Local positive-state repair for the pinned R11 closed cube.
Every numerical update at a recomputed node calls the source BRC/feedback
primitives. Flow and fields of other nodes come from the six-state background.
"""
from dataclasses import replace


def repair_one(R,m,s,bg,bg_next,bg_inc):
    pending=[{} for _ in range(8)]
    other=[{} for _ in range(8)]
    for key,n in s.pending.items():pending[key[0]][key]=n
    for key,n in bg.pending.items():other[key[0]][key]=n
    dirty={v for v,loc in enumerate(m.locations)
           if s.b[loc]!=bg.b[loc] or s.q[v]!=bg.q[v] or s.wall[v]!=bg.wall[v]
           or pending[v]!=other[v]}
    t=m.a.add(s.t,1)
    if not dirty:return replace(bg_next,t=t),bg_inc,0
    work=dirty|{m.target(v,j) for v in dirty for j in range(3)}
    assert None not in work
    q=list(bg_next.q);b=list(bg_next.b); wall=list(bg_next.wall)
    pp={key:n for key,n in bg_next.pending.items() if key[0] not in work}
    rows=[]
    for v in sorted(work):
        loc=m.locations[v]
        qq=list(s.q[v]);wall[v]=s.wall[v]
        # All real arrivals due at v, including those sent by unmodified nodes.
        for port in range(3):
            w=m.target(v,port)
            for (src,j,role,d),n in pending[w].items():
                if j==port and d==1:qq[role]=m.a.add(qq[role],n)
        for (w,j,role,d),n in sorted(pending[v].items()):
            if d==1:
                rows.append(['handoff',t,v,j,role,n,m.target(v,j)])
            else:
                m.put(pp,(v,j,role,m.a.gap(d,1)),n)
        phase=R.R10.ROT[1][s.b[loc]]
        done,after,hist=R.R10.burst_unit(m.a,min(qq),phase,m.gates[v],m.feedback[v])
        q[v]=tuple(m.a.gap(x,done) for x in qq) if done else tuple(qq)
        b[loc]=after
        if done:
            rows.append(['feedback-release',t,v,done,phase,after,list(hist)])
            for kind,num in enumerate(hist):
                if num:
                    for j,d in enumerate(m.delays):m.put(pp,(v,j,R.R10.ROT[kind][j],d),num)
    inc={k:n for k,n in bg_inc.items() if int(k.split(':')[1]) not in work}
    inc.update(R.event_flow(m.a,rows))
    return R.State(t,tuple(q),pp,tuple(wall),tuple(b)),inc,len(work)
