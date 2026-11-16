'use strict';
// PREFIX-830 independent exact named Q-only BRC dynamics; no floating point.
const RAW={
  "7": {
    "A": [
      0,
      18,
      27,
      58,
      64,
      89,
      101
    ],
    "B": [
      1,
      13,
      38,
      44,
      75,
      84,
      102
    ],
    "shift": 1
  },
  "8": {
    "A": [
      -25,
      -21,
      -16,
      -2,
      2,
      16,
      21,
      25
    ],
    "B": [
      -24,
      -23,
      -14,
      -5,
      5,
      14,
      23,
      24
    ],
    "shift": 26
  },
  "9": {
    "A": [
      -98,
      -82,
      -58,
      -34,
      13,
      16,
      69,
      75,
      99
    ],
    "B": [
      -99,
      -75,
      -69,
      -16,
      -13,
      34,
      58,
      82,
      98
    ],
    "shift": 100
  },
  "10": {
    "A": [
      -313,
      -301,
      -188,
      -100,
      -99,
      99,
      100,
      188,
      301,
      313
    ],
    "B": [
      -308,
      -307,
      -180,
      -131,
      -71,
      71,
      131,
      180,
      307,
      308
    ],
    "shift": 314
  }
};
function factorial(n){let x=1n;for(let i=2;i<=n;i++)x*=BigInt(i);return x;}

function elementary(v){let out=Array(v.length+1).fill(0n);out[0]=1n;let i=0;for(const val of v){i++;for(let k=i;k>=1;k--)out[k]+=BigInt(val)*out[k-1];}return out;}

function trace(w){const n=w.length,q=n;let states=new Map([[(2**n-1)+"/0",1n]]),traces=[];for(let t=0;t<=n;t++){const h=Array(q+1).fill(0n);for(const [key,mass] of states){const [mask0,mark0]=key.split("/");let mask=Number(mask0),mark=Number(mark0);let cnt=mark;for(let i=0;i<n;i++)cnt+=(mask>>>i)&1;h[cnt]+=mass;}traces.push(h);if(t===n)break;let nxt=new Map();function plus(key,x){nxt.set(key,(nxt.get(key)||0n)+x)}for(const [key,mass] of states){const [mask0,mark0]=key.split("/");const mask=Number(mask0),mark=Number(mark0);let cnt=0;for(let i=0;i<n;i++)if(mask&(1<<i)){cnt++;plus((mask^(1<<i))+"/"+mark,mass*BigInt(w[i]));}if(mark)plus(mask+"/0",mass*3n);else if(cnt<n)plus(mask+"/1",mass*2n);}states=nxt;}return traces;}

function run(){const rows=[];let compared=0,elementaryAssertions=0;for(const [k,row] of Object.entries(RAW)){const n=Number(k),A=row.A.map(x=>x+row.shift),B=row.B.map(x=>x+row.shift);if(A.length!==n||B.length!==n||A.some(x=>x<1)||B.some(x=>x<1))throw Error("invalid positive source pair");const ea=elementary(A),eb=elementary(B);for(let j=0;j<n;j++){elementaryAssertions++;if(ea[j]!==eb[j])throw Error("early elementary discrepancy "+n);}if(ea[n]===eb[n])throw Error("no nth discrepancy "+n);const TA=trace(A),TB=trace(B);for(let t=0;t<n;t++)for(let i=0;i<=n;i++){compared++;if(TA[t][i]!==TB[t][i])throw Error("early histogram mismatch "+n+" t="+t+" bin="+i)}let dif=[];for(let i=0;i<=n;i++){compared++;dif.push(TA[n][i]-TB[n][i]);}const expected=factorial(n)*(ea[n]-eb[n]);if(dif[0]!==expected||dif.slice(1).some(x=>x!==0n))throw Error("witness mismatch "+n);rows.push({n,A,B,shift:row.shift,delta_e_n:(ea[n]-eb[n]).toString(),first_difference_step:n,first_difference_bin:0,delta_first_count:expected.toString()});}return {status:"ALL_EXACT_ASSERTIONS_PASSED",arithmetic:"BigInt exact integer",positive_mark_weights:{a:2,b:3},tested_n:[7,8,9,10],independent_named_histogram_scalar_comparisons:compared,elementary_equality_assertions:elementaryAssertions,results:rows,scope:"Exhaustive exact subset-state dynamic programming for all reachable named states, n=7..10, t=0..n; general minimum theorem separately from PREFIX-829"};}
console.log(JSON.stringify(run(),null,2));
