function verifyR743(){
  const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  const assert=(v,m)=>{if(!v)throw new Error(m)};
  const perms=a=>a.length===0?[[]]:a.flatMap((v,i)=>perms(a.filter((_,j)=>j!==i)).map(t=>[v,...t]));
  const compose=(a,b)=>b.map(i=>a[i]);
  const inverse=a=>a.map((_,i)=>a.indexOf(i));
  const identity=[0,1,2],labels=[[0,1,2],[0,2,1],[1,0,2],[2,1,0]],loop=[1,0,2];
  let previous=null, epsHist={}, currentHist={}, pairHist={}, hHist={};
  let examples=[];
  for(const sigma of perms([0,1,2,3])){
    const word=[...sigma.map(i=>i+1),5,6,-5,-6,...sigma.slice().reverse().map(i=>-i-1)];
    assert(word.length===12,"length");
    assert(eq(word.slice().sort((a,b)=>a-b),[-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]),"tokens");
    assert(word.every((x,i)=>i===0||x!==-word[i-1]),"nonbacktrack");
    const x=[0,0,0,0,0,0],j=new Map();
    for(const step of word){
      const axis=Math.abs(step)-1,y=x.slice(),sgn=Math.sign(step);
      y[axis]+=sgn;
      const lower=(sgn>0?x:y).join(",")+":"+axis;
      j.set(lower,(j.get(lower)||0)+sgn);
      for(let i=0;i<6;i++)x[i]=y[i];
    }
    assert(x.every(v=>v===0),"root");
    const observed=[...j].filter(([k,v])=>v!==0).sort((a,b)=>a[0].localeCompare(b[0]));
    assert(observed.length===4,"support");
    const current=JSON.stringify(observed);
    if(previous===null)previous=current;else assert(previous===current,"current collision");
    const first=[],seen=new Set();
    for(const step of word){const a=Math.abs(step)-1;if(!seen.has(a)){first.push(a);seen.add(a);assert(step>0,"first-sign")}}
    let inversions=0;for(let i=0;i<6;i++)for(let k=i+1;k<6;k++)if(first[i]>first[k])inversions++;
    const epsilon=inversions%2===0?"+":"-";
    let H=identity;
    for(const i of sigma)H=compose(labels[i],H);
    const h=compose(compose(inverse(H),loop),H).join("");
    epsHist[epsilon]=(epsHist[epsilon]||0)+1;
    currentHist[current]=(currentHist[current]||0)+1;
    const joint=epsilon+":"+h;pairHist[joint]=(pairHist[joint]||0)+1;
    hHist[h]=(hHist[h]||0)+1;
    if(examples.length<3)examples.push({sigma:sigma.join(""),word:word.join(","),epsilon,h});
  }
  assert(Object.keys(currentHist).length===1,"single current");
  assert(eq(epsHist,{"+":12,"-":12}),"parity balance");
  assert(Object.keys(hHist).length===3&&Object.values(hHist).every(v=>v===8),"holonomy 8-fibers");
  assert(Object.keys(pairHist).length===6&&Object.values(pairHist).every(v=>v===4),"joint 4-fibers");
  return {
    validation:"R743_X6_CONJUGATE_CONNECTOR_BRC_EXACT_PASS",
    scope:"All 24 permutations of four connector axes, 12 signed unit steps on six axes",
    paths:24, nonbacktracking:24, shared_signed_current_classes:1,shared_signed_current_support:4,
    first_signs:"all positive",
    epsilon_fibers:epsHist, holonomy_fibers:hHist, joint_fibers:pairHist,
    labels:{axis0:labels[0],axis1:labels[1],axis2:labels[2],axis3:labels[3],square:loop},
    bits_worst:{current:5,current_plus_epsilon:4,current_plus_h:3,current_plus_h_and_epsilon:2},
    samples:examples,
    frozen_science_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    independent_evidence:"Direct Python standard-library permutation/current and S3 enumeration was also executed."
  };
}

if (typeof console !== 'undefined') console.log(JSON.stringify(verifyR743(), null, 2));
