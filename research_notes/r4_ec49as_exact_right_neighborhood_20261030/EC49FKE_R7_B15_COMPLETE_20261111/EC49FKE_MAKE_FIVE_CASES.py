#!/usr/bin/env python3
"""Generate five-label native-prefix cases for the still-unclassified B15 groups."""
from pathlib import Path
from collections import defaultdict
R=Path(__file__).resolve().parent
c4=defaultdict(list)
for row in (R.parent/'EC49FKD_R7_B15_FOUR_20261111'/'EC49FKD_FOUR_CASES.tsv').read_text().splitlines():
 f=row.split('\t');c4[tuple(f[:2])].append(f)
solved={tuple(row.split('\t')[:2]) for row in (R.parent/'EC49FKD_R7_B15_FOUR_20261111'/'EC49FKD_FOUR_RESULTS.tsv').read_text().splitlines()}
rows=[]
for k,v in sorted(c4.items()):
 if k in solved:continue
 labels=sorted({p for line in v for p in line[3].split(';')},key=lambda x:tuple(map(int,x.split(','))))
 assert len(v)==5 and len(labels)==5,(k,len(v),len(labels))
 rows.append('\t'.join([k[0],k[1],v[0][2],';'.join(labels),v[0][4],v[0][5]]))
assert len(rows)==28
(R/'EC49FKE_FIVE_CASES.tsv').write_text('\n'.join(rows)+'\n')
print('EC49FKE_FIVE_INPUT_PASS',len(rows))
