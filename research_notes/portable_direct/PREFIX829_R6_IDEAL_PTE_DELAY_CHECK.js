'use strict';
// PREFIX-829 / exact positive weighted named Q=R+A, no floating point.
const EXAMPLES={
  "1": [
    [
      1
    ],
    [
      2
    ]
  ],
  "2": [
    [
      1,
      4
    ],
    [
      2,
      3
    ]
  ],
  "3": [
    [
      1,
      5,
      6
    ],
    [
      2,
      3,
      7
    ]
  ],
  "4": [
    [
      1,
      7,
      8,
      14
    ],
    [
      2,
      4,
      11,
      13
    ]
  ],
  "5": [
    [
      1,
      18,
      19,
      44,
      48
    ],
    [
      4,
      8,
      33,
      34,
      51
    ]
  ],
  "6": [
    [
      1,
      6,
      7,
      17,
      18,
      23
    ],
    [
      2,
      3,
      11,
      13,
      21,
      22
    ]
  ],
  "12": [
    [
      1,
      12,
      25,
      66,
      91,
      130,
      174,
      213,
      238,
      279,
      292,
      303
    ],
    [
      4,
      6,
      31,
      58,
      105,
      117,
      187,
      199,
      246,
      273,
      298,
      300
    ]
  ]
};
function elementary(xs) {
  const e=Array(xs.length+1).fill(0n);e[0]=1n;
  let count=0;
  for(const x0 of xs){const x=BigInt(x0);count++;for(let k=count;k>=1;k--)e[k]+=x*e[k-1];}
  return e;
}

function factorial(n){let x=1n;for(let j=2;j<=n;j++)x*=BigInt(j);return x;}

function namedHistogram(xs,q,maxSteps){
  const p=xs.length;
  let states=new Map([[(String((1<<p)-1)+":0"),1n]]);
  const all=[];
  for(let step=0;step<=maxSteps;step++){
    const h=Array(q+1).fill(0n);
    for(const [key,mass] of states){
      const s=key.split(":");
      const mask=Number(s[0]),mark=Number(s[1]);
      let pop=0;for(let k=0;k<p;k++)pop+=(mask>>k)&1;
      h[pop+mark]+=mass;
    }
    all.push(h);
    if(step===maxSteps)break;
    const next=new Map();
    function put(mask,mark,weight){const key=String(mask)+":"+String(mark);next.set(key,(next.get(key)||0n)+weight);}
    for(const [key,mass] of states){
      const sp=key.split(":");const mask=Number(sp[0]),mark=Number(sp[1]);
      let pop=0;
      for(let k=0;k<p;k++) if((mask>>k)&1){pop++;put(mask^(1<<k),mark,mass*BigInt(xs[k]));}
      if(mark)put(mask,0,mass*3n);
      else if(pop<q)put(mask,1,mass*2n);
    }
    states=next;
  }
  return all;
}

function run(){
  const cases=[];
  let namedComparisons=0;
  let elementaryComparisons=0;
  for(const [ns,pair] of Object.entries(EXAMPLES)){
    const n=Number(ns),A=pair[0],B=pair[1];
    if(A.length!==n||B.length!==n)throw Error("bad input size: "+n);
    if(A.some(x=>x<=0)||B.some(x=>x<=0))throw Error("nonpositive weights");
    const ea=elementary(A),eb=elementary(B);
    for(let k=0;k<n;k++){elementaryComparisons++;if(ea[k]!==eb[k])throw Error("early elementary discrepancy n="+n+" k="+k);}
    if(ea[n]===eb[n])throw Error("no distinction at n="+n);
    const HA=namedHistogram(A,n,n), HB=namedHistogram(B,n,n);
    for(let t=0;t<n;t++){
      for(let bin=0;bin<=n;bin++){namedComparisons++;if(HA[t][bin]!==HB[t][bin])throw Error("early named discrepancy n="+n+" t="+t+" bin="+bin);}
    }
    let nonzero=[];
    for(let bin=0;bin<=n;bin++){namedComparisons++;const d=HA[n][bin]-HB[n][bin];if(d!==0n)nonzero.push({bin,delta:d.toString()});}
    const expected=factorial(n)*(ea[n]-eb[n]);
    if(nonzero.length!==1||nonzero[0].bin!==0||BigInt(nonzero[0].delta)!==expected)throw Error("wrong first witness n="+n);
    cases.push({n,source_count:n,A,B,delta_e_n:(ea[n]-eb[n]).toString(),first_difference_step:n,first_difference_bin:0,delta_named_histogram:expected.toString()});
  }
  const lifts=[];
  for(const ns of [4,5,6,12]){
    const A=EXAMPLES[String(ns)][0],B=EXAMPLES[String(ns)][1];
    const h=Math.max(...A,...B)+1;
    const AP=A.concat(B.map(x=>x+h)),BP=B.concat(A.map(x=>x+h));
    const ea=elementary(AP),eb=elementary(BP);
    for(let k=0;k<=ns;k++){elementaryComparisons++;if(ea[k]!==eb[k])throw Error("lift mismatch n="+ns+", k="+k);}
    const expected=BigInt(ns)*BigInt(h)*(elementary(A)[ns]-elementary(B)[ns]);
    if(ea[ns+1]-eb[ns+1]!==expected||expected===0n)throw Error("lift first diff wrong");
    lifts.push({seed_n:ns,new_delay:ns+1,source_count:2*ns,shift:h,delta_e_new:expected.toString(),new_delta_histogram:(factorial(ns+1)*expected).toString()});
  }
  return {status:"ALL_EXACT_ASSERTIONS_PASSED",arithmetic:"JavaScript BigInt",scope:"n=1,2,3,4,5,6,12 complete labeled Q-branch enumeration through first difference; n=4,5,6,12 exact lift symmetric checks",a:"2",b:"3",tested_cases:cases.length,independent_named_histogram_scalar_comparisons:namedComparisons,elementary_coefficient_comparisons:elementaryComparisons,examples:cases,lifts,source_notes:["PREFIX-827 exact state-trace closed form, frozen source f42f2906d77f24085c123f3ccfe9667d41caa96d","PREFIX-828 Prouhet binary-parity delayed trace construction","n=6 and n=12 numeric PTE witnesses independently verified from literature examples; n=5 symmetric construction independently found and checked"]};
}
const output=run();
console.log(JSON.stringify(output,null,2));
