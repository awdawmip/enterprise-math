# T6 p13 q13 split(6,7) negative (7): scoped combinatorial audit

2026-11-28. Driver EM-DVR-DEBB5E. Author EM-DIRECT-D03BC9 (journal onhour-20261128-0000-p13q13-split6-7-len1-complete), frozen source d84bd940cfb093cdc60e569f15cad58772a51dca. Actual compact certificate a7d1501e36cce3f9ad6abe647b3d9494c8149e10:research_checks/T6_P13_Q13_SPLIT6_7_LEN1_COMPLETE_CERT_20261128.json blob d4f184a4db1b66ece816d9ad65d77a4f2ec4e7f8.

In the one-power maximal-p13 model with q-positive atoms (q,r), 1<=r<=12, cost 169q+13r-1, total q=6 or 7 and cap 2331 per side. For negative partition (7), all 12 r are under budget (cost <=1338), and every positive partition of 6 has total mass <=1014+6*155=1944. Supports are disjoint because no positive atom has q=7. For positive q multiplicity m_q, number of literal rosters is product binom(12+m_q-1,m_q); true p13-smooth domain replaces 12 by count of r with 13q+r 13-smooth. Negative count is likewise 12 or smooth count at q=7. The formula retains same-side multiplicities. All 11 raw row counts and summed node counter match author certificate. No claim of reexecuting affine exclusions; source author evidence remains AUTHOR_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED. Filtered domain count is a mathematical domain restriction, not independent proof of solver coverage.

Actual exact calculation:
```json
{
  "smoothAtomCounts": [
    9,
    7,
    7,
    6,
    5,
    5,
    4
  ],
  "rows": [
    {
      "partition": [
        6
      ],
      "raw": 144,
      "expected": 144,
      "filtered": 20,
      "nodes": 264
    },
    {
      "partition": [
        1,
        5
      ],
      "raw": 1728,
      "expected": 1728,
      "filtered": 180,
      "nodes": 3183
    },
    {
      "partition": [
        2,
        4
      ],
      "raw": 1728,
      "expected": 1728,
      "filtered": 168,
      "nodes": 3220
    },
    {
      "partition": [
        3,
        3
      ],
      "raw": 936,
      "expected": 936,
      "filtered": 112,
      "nodes": 1709
    },
    {
      "partition": [
        1,
        1,
        4
      ],
      "raw": 11232,
      "expected": 11232,
      "filtered": 1080,
      "nodes": 19932
    },
    {
      "partition": [
        1,
        2,
        3
      ],
      "raw": 20736,
      "expected": 20736,
      "filtered": 1764,
      "nodes": 36697
    },
    {
      "partition": [
        2,
        2,
        2
      ],
      "raw": 4368,
      "expected": 4368,
      "filtered": 336,
      "nodes": 7715
    },
    {
      "partition": [
        1,
        1,
        1,
        3
      ],
      "raw": 52416,
      "expected": 52416,
      "filtered": 4620,
      "nodes": 90519
    },
    {
      "partition": [
        1,
        1,
        2,
        2
      ],
      "raw": 73008,
      "expected": 73008,
      "filtered": 5040,
      "nodes": 126455
    },
    {
      "partition": [
        1,
        1,
        1,
        1,
        2
      ],
      "raw": 196560,
      "expected": 196560,
      "filtered": 13860,
      "nodes": 331185
    },
    {
      "partition": [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "raw": 148512,
      "expected": 148512,
      "filtered": 12012,
      "nodes": 243964
    }
  ],
  "raw": 511368,
  "filtered": 39192,
  "nodes": 864843,
  "coverageMatches": true
}
```
Reproducer (call count with parsed exact source certificate):
```js
function count(d){
 function choose(n,k){let z=1;for(let i=1;i<=k;i++)z=z*(n-i+1)/i;return z}
 function smooth(x){for(let p=2;p<=13;p++)while(x%p===0)x/=p;return x===1}
 let a=Array.from({length:7},(_,i)=>Array.from({length:12},(_,j)=>13*(i+1)+j+1).filter(smooth).length);
 let rows=d.rows.map(r=>{let m={};for(let q of r[0])m[q]=(m[q]||0)+1;let raw=12,filtered=a[6];for(let [q,k] of Object.entries(m)){raw*=choose(12+k-1,k);filtered*=choose(a[Number(q)-1]+k-1,k)}return {partition:r[0],raw,expected:r[2],filtered,nodes:r[5]};});
 return {smoothAtomCounts:a,rows,raw:rows.reduce((s,r)=>s+r.raw,0),filtered:rows.reduce((s,r)=>s+r.filtered,0),nodes:rows.reduce((s,r)=>s+r.nodes,0),coverageMatches:rows.every(r=>r.raw===r.expected)};
}
```
The author journal at d13bb4ca5320a29ec2797048c6884df002cb97d7 reports q13 coverage 329/343 and split67 next negative (1,6); preserve this active author frontier and avoid duplicate work.
