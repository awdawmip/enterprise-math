"""Exact finite completeness and passive-frame roundtrip checks."""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
import json
import random
import chart_transport as ct
import x6_development as x

counts=Counter()
def need(ok,name):
    if not ok: raise AssertionError(name)
    counts[name]+=1

E=x.EDGES
# Enumerate ALL 2^6 possible shared-edge-compatible transition selections.
# Opposite orientations share inverse; each candidate is an involution.
flat_configs=[]; covariant_configs=[]
for bits in product((0,1),repeat=6):
    table={e:ct.transition(*e,kind='flat' if bit else 'single') for e,bit in zip(E,bits)}
    def T(u,v):
        return x.brc.IDENTITY if u==v else table[tuple(sorted((u,v))) ]
    flat=all(x.brc.compose(T(v,w),T(u,v))==T(u,w) for u,v,w in product(range(4),repeat=3))
    covariant=all(T(g[u],g[v])==x.brc.compose(x.brc.compose(g,T(u,v)),x.brc.inverse(g))
                  for g in x.GROUP for u,v in permutations(range(4),2))
    if flat: flat_configs.append(bits)
    if covariant: covariant_configs.append(bits)
need(covariant_configs==[(0,)*6,(1,)*6],'complete_covariant_classification')
need(flat_configs==[(1,)*6],'unique_flat_connection_even_without_covariance')

for u,v in permutations(range(4),2):
    allowed={g for g in x.GROUP if g[u]==v and g[v]==u}
    need(allowed=={ct.transition(u,v),ct.transition(u,v,kind='single')},'all_compatible_edge_maps')
for u,v,w in permutations(range(4),3):
    need(ct.transport_word((u,v,w,u))==x.brc.IDENTITY,'flat_triangle')
    p=list(range(4));p[v],p[w]=w,v
    need(ct.transport_word((u,v,w,u),kind='single')==tuple(p),'single_triangle_holonomy')
for walk in product(range(4),repeat=6):
    need(ct.transport_word(walk)==ct.transition(walk[0],walk[-1]),'all_six_vertex_walks')

rng=random.Random(90605)
for i in range(100):
    cell=x.Cell()
    for _ in range(rng.randrange(1,12)):
        cell=cell.push(rng.randrange(4),x.LocalMove(rng.randrange(-3,4),rng.randrange(-3,4)))
    for u,v in product(range(4),repeat=2):
        f=ct.FramedCell.encode(cell,u)
        need(f.reframe(v).decode()==cell,'passive_frame_roundtrip')
        need(f.observer()==f.reframe(v).observer(),'global_readout_frame_independence')
        need(f.coordinates.gauge_terms()==f.reframe(v).coordinates.gauge_terms(),'frame_gauge_preservation')
    g=rng.choice(x.GROUP); u,v=rng.randrange(4),rng.randrange(4)
    f=ct.FramedCell.encode(cell,u)
    need(f.reframe(v).relabel_chart_and_coordinates(g)==f.relabel_chart_and_coordinates(g).reframe(g[v]),'relabel_reframe_commuting_square')
    need(f.active_rotate(g).reframe(v)==f.reframe(v).active_rotate(g),'active_reframe_commuting_square')
    need(f.active_rotate(g).decode()==cell.rotate(g),'active_preserves_full_packet_action')

for u,v in permutations(range(4),2):
    before=x.PacketPath(x.Cell(),(x.Event(u,v),)).endpoint
    after=before.rotate(ct.transition(u,v))
    target=x.PacketPath(x.Cell(),(x.Event(v,u),)).endpoint
    need(after==target and before.gauge_terms()==after.gauge_terms()==(1,), 'shared_positive_axis_gauge')
    # This is NOT the fixed-frame inverse seam identification.
    inv_target=x.PacketPath(x.Cell(),(x.Event(v,u,-1),)).endpoint
    need(after!=inv_target and inv_target.gauge_terms()==(2,), 'passive_not_inverse_seam')

# Deliberately test the exact frame-loss mechanism, not only successful maps.
seeds=[x.PacketPath(x.Cell(),(x.Event(v,w),)).endpoint for v in range(4) for w in x.neighbours(v)]
passive_kernel=[]; active_kernel=[]
for g in x.GROUP:
    if all(ct.FramedCell.encode(c,0).relabel_chart_and_coordinates(g).decode()==c for c in seeds):
        passive_kernel.append(g)
    if all(ct.FramedCell.encode(c,0).active_rotate(g).decode()==c for c in seeds):
        active_kernel.append(g)
need(set(passive_kernel)=={ct.transition(0,v) for v in range(4)},'joint_relabel_quotient_kernel_exactly_V4')
need(active_kernel==[x.brc.IDENTITY],'active_action_is_faithful')
for g in x.GROUP:
    for h in x.GROUP:
        c=seeds[0]; f=ct.FramedCell.encode(c,2)
        need(f.active_rotate(h).active_rotate(g)==f.active_rotate(x.brc.compose(g,h)),'active_group_law')

result={'status':'PASS_EXACT_CHART_TRANSPORT_NOT_NATIVE_ENDPOINT_GLUING',
        'counts':dict(counts),'edge_selection_configurations':64,
        'covariant_connections':covariant_configs,'flat_connections':flat_configs,
        'flatness_is_explicit_selector':True,'joint_relabel_kernel':passive_kernel,'active_kernel':active_kernel}
Path('verification_chart_transport.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
