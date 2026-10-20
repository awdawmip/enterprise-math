import json,hashlib
from pathlib import Path
import r055_core as r
ROOT=Path('/mnt/data/r055_work')

def decode_hex(h):
    b=bytes.fromhex(h)
    return tuple((b[i],b[i+1]) for i in range(0,len(b),2))
def sid(enc): return r.state_id(tuple(enc))
def state_obj(h):
    enc=decode_hex(h); C=frozenset(enc)
    return {'state_id':sid(enc),'canonical_state':[list(x) for x in enc],'diagnostics':r.diagnostics(C)}

# Parse N1-11 main exact quotient data
main={n:{'gmins':[],'pmins':[],'locals':{},'basins':{}} for n in range(1,13)}
for line in (ROOT/'exhaustive_upto12_omp.tsv').read_text().splitlines():
    if not line or line.startswith('#'):continue
    p=line.split('\t');typ=p[0];n=int(p[1])
    if n>11:continue
    d=main[n]
    if typ=='SUMMARY':
        d['summary']={'connected_classes':int(p[2]),'hole_free_classes':int(p[3]),'global_G_min':int(p[4]),'global_G_min_count':int(p[5]),'global_P_edge_min':int(p[6]),'global_P_edge_min_count':int(p[7]),'G_P_min_overlap_count':int(p[8]),'D1_local_min_count':int(p[9]),'D1_local_not_D2_min_count':int(p[10])}
    elif typ=='GMIN':d['gmins'].append(p[2])
    elif typ=='PMIN':d['pmins'].append(p[2])
    elif typ=='LOCAL':d['locals'][p[2]]={'D2_minimum':bool(int(p[3])),'G':int(p[4])}
    elif typ=='BASIN' and p[2] in ('T0_CANONICAL_MIN','T1_CANONICAL_MAX'):
        d['basins'].setdefault(p[2],{})[p[3]]=int(p[4])
# N12 exact T0/T1 + stats
for line in (ROOT/'n12_basin.tsv').read_text().splitlines():
    if not line or line.startswith('#'):continue
    p=line.split('\t');typ=p[0];n=int(p[1]);d=main[n]
    if typ=='SUMMARY':
        d['summary']={'connected_classes':683101,'hole_free_classes':int(p[2]),'global_G_min':int(p[3]),'global_G_min_count':int(p[4]),'global_P_edge_min':int(p[5]),'global_P_edge_min_count':int(p[6]),'G_P_min_overlap_count':int(p[7]),'D1_local_min_count':int(p[8]),'D1_local_not_D2_min_count':int(p[9])}
    elif typ=='GMIN':d['gmins'].append(p[2])
    elif typ=='PMIN':d['pmins'].append(p[2])
    elif typ=='LOCAL':d['locals'][p[2]]={'D2_minimum':bool(int(p[3])),'G':int(p[4])}
    elif typ=='BASIN' and p[2] in ('T0_CANONICAL_MIN','T1_CANONICAL_MAX'):
        d['basins'].setdefault(p[2],{})[p[3]]=int(p[4])
# Correct orientation-retaining T2 N1-11
for line in (ROOT/'t2_oriented.tsv').read_text().splitlines():
    if not line or line.startswith('#'):continue
    p=line.split('\t');typ=p[0];n=int(p[1])
    if n>11:continue
    if typ=='BASIN':main[n]['basins'].setdefault('T2_ORIENTATION_MOVE_LEX',{})[p[3]]=int(p[4])

rows=[]
for n in range(1,13):
    d=main[n]
    relevant=set(d['gmins'])|set(d['pmins'])|set(d['locals'])
    states={h:state_obj(h) for h in sorted(relevant)}
    local=[]
    for h,meta in sorted(d['locals'].items()):
        x=states[h].copy();x.update(meta);local.append(x)
    basins={}
    for tie,bmap in d['basins'].items():
        basins[tie]=[{'terminal_state_id':states[h]['state_id'],'terminal_state':[list(x) for x in decode_hex(h)],'basin_size':c} for h,c in sorted(bmap.items())]
    if n==12:
        basins['T2_ORIENTATION_MOVE_LEX']={'status':'COMPUTATIONAL_CUTOFF','reason':'Exact orientation-retaining T2 trajectory basin pass exceeded the bounded execution window at N=12. T0/T1 basins and all N=12 state/global/local-minimum facts are exact exhaustive. No quotient-recanonicalized T2 approximation is promoted.'}
    rows.append({
        'N':n,**d['summary'],
        'G_P_minimizer_sets_coincide':set(d['gmins'])==set(d['pmins']),
        'global_G_minimizers':[states[h] for h in d['gmins']],
        'global_P_edge_minimizers':[states[h] for h in d['pmins']],
        'D1_local_minima':local,'basins':basins,
        'T2_orientation_policy':'Each free-class initial state uses its canonical representative orientation; after each accepted T2 move only translation normalization is applied, never D6 reorientation.'
    })
atlas={
 'schema':'R055_SMALL_N_EXHAUSTIVE_ATLAS_V1','researcher_id':'EM-R055-4C2A71',
 'scope':'all connected hole-free clusters modulo translation+D6 for N=1..12 under the frozen same-6-neighbor exterior test',
 'enumeration_method':'generate all connected free polyhex classes first, then filter hole-free; no hole-free-only growth shortcut',
 'exactness':{'state_classes_N1_12':'EXACT_EXHAUSTIVE','G_P_global_minima_N1_12':'EXACT_EXHAUSTIVE','D1_local_minima_N1_12':'EXACT_EXHAUSTIVE','D2_improvement_test_on_all_D1_minima_N1_12':'EXACT_EXHAUSTIVE','T0_T1_basins_N1_12':'EXACT_EXHAUSTIVE','T2_orientation_retaining_basins_N1_11':'EXACT_EXHAUSTIVE','T2_orientation_retaining_basin_N12':'COMPUTATIONAL_CUTOFF'},
 'results':rows,
 'smallest_counterexamples':{
   'D1_LOCAL_MINIMUM_NOT_D2_MINIMUM':6,
   'MULTIPLE_D1_ATTRACTORS':6,
   'TIE_BREAK_DEPENDENCE':6,
   'G_MINIMIZER_SET_DIFFERS_FROM_P_EDGE_MINIMIZER_SET':6
 },
 'interpretation_guard':'Exact through declared small-N scope only; not an all-N or asymptotic theorem.'
}
r.json_dump(ROOT/'artifacts/R055_SMALL_N_EXHAUSTIVE_ATLAS.json',atlas)
print(ROOT/'artifacts/R055_SMALL_N_EXHAUSTIVE_ATLAS.json')
print('sha256',r.sha256_file(ROOT/'artifacts/R055_SMALL_N_EXHAUSTIVE_ATLAS.json'))
for row in rows:
  print(row['N'],row['connected_classes'],row['hole_free_classes'],row['global_G_min'],row['global_P_edge_min'],row['D1_local_min_count'],row['D1_local_not_D2_min_count'],row['G_P_minimizer_sets_coincide'])
