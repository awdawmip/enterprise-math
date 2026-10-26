// R306 exact verifier: Node.js with BigInt, no dependencies.
// Recompute the complete 2<=d<=200 certificate and independent six-edge DP checks.
'use strict';
const verify = function verify(){
  const DMAX=200;
  const Q=[Array(4).fill(0n),Array(7).fill(0n)];Q[0][3]=1n;Q[1][6]=1n;
  const multipliers=[
    [[1,1n],[2,-1n],[3,1n]],
    [[3,1n],[4,-3n],[5,2n]],
    [[6,-1n],[7,2n],[8,-1n]],
    [[8,1n],[9,-3n],[10,3n],[11,-1n]]
  ];
  for(let d=2;d<=DMAX;d++){
    const q=[];
    for(let j=1;j<=4;j++)if(d-j>=0)
      for(const [shift,c] of multipliers[j-1])
        for(let i=0;i<Q[d-j].length;i++){
          const k=i+shift;while(q.length<=k)q.push(0n);
          q[k]+=c*Q[d-j][i];
        }
    if(d===2){q[6]-=1n;q[7]+=1n;}
    if(d===3){q[8]+=1n;q[9]-=2n;q[10]+=1n;}
    while(q.length&&q[q.length-1]===0n)q.pop();
    if(q.length-1>3*d+3)throw Error("degree bound fails at d="+d);
    Q.push(q);
  }
  function binom(n,r){
    if(n<0||r<0||r>n)return 0n;
    let b=1n;for(let i=1;i<=r;i++)b=b*BigInt(n-i+1)/BigInt(i);
    return b;
  }
  function D(d,n){
    if(d===0)return n===3?1n:0n;
    let value=0n;
    for(let k=0;k<Q[d].length;k++)
      if(Q[d][k]!==0n && n>=k)
        value+=Q[d][k]*binom(n-k+d-1,d-1);
    return value;
  }
  let total=0,smallest=null;
  const per_defect=[];
  for(let d=2;d<=DMAX;d++){
    const threshold=4*d+4;
    const values=Array.from({length:d},(_,j)=>D(d,threshold+j));
    const differences=[];
    for(let len=d;len>=1;len--){
      differences.push(values[0]);
      for(let i=0;i<len-1;i++)values[i]=values[i+1]-values[i];
    }
    const minimum=differences.reduce((a,b)=>a<b?a:b);
    if(minimum<=0n)throw Error("NONPOSITIVE NEWTON COEFFICIENT at defect "+d);
    if(differences[d-1]!==1n)throw Error("INCORRECT LEADING COEFFICIENT "+d);
    if(smallest===null||minimum<smallest)smallest=minimum;
    total+=d;
    per_defect.push({
      d, n0:threshold, Q_degree:Q[d].length-1,
      at_n0:differences[0].toString(),
      min_delta:minimum.toString(),
      highest_delta:differences[d-1].toString()
    });
  }
  const edges=[
    [[0,2,-1,-1],[1,2,1,-1]],
    [[0,0,-1,-1],[1,0,1,-1]],
    [[0,1,1,1],[1,2,1,-1]]
  ];
  let states=new Map([["0|2|1|0",1n]]), crosschecks=0;
  for(let n=0;n<=80;n++){
    if(n>0){
      const next=new Map();
      for(const [key,count] of states){
        const [q,previous,epsilon,k]=key.split("|").map(Number);
        for(const [bit,nq,eta,c] of edges[q]){
          if(previous===0&&bit===0)continue;
          const nextKey=`${nq}|${bit}|${eta*epsilon}|${eta*k+c}`;
          next.set(nextKey,(next.get(nextKey)??0n)+count);
        }
      }
      states=next;
    }
    const byD=new Map();
    for(const [key,count] of states){
      const [q,previous,epsilon,k]=key.split("|").map(Number);
      if(q!==0||n===0)continue;
      if((n+k-2)%2!==0)throw Error("nonintegral defect");
      const d=(n+k-2)/2;
      if(d>=0)byD.set(d,(byD.get(d)??0n)+BigInt(epsilon)*count);
    }
    for(let d=0;d<=Math.min(n,60);d++){
      const direct=byD.get(d)??0n, formal=D(d,n);
      if(direct!==formal)throw Error(`direct DP mismatch n=${n}, d=${d}, direct=${direct}, formal=${formal}`);
      crosschecks++;
    }
  }
  return {
    schema:"EM_R306_BOUNDED_LINEAR_STRIP_CERTIFICATE_V1", status:"PASS",
    arithmetic:"JavaScript BigInt, exact integer binomial coefficients and differences",
    formal_input:"R305 bivariate F(x,z) for complete positive-weight ordered six-edge BRC effect counts",
    theorem:"For every integer 2<=d<=200 and every integer n>=4d+4, D_d(n)>0",
    degree_bound:"For d>=1 F_d(x)=Q_d(x)/(1-x)^d; degree(Q_d)<=3d+3",
    polynomiality:"D_d(n) is an integer-valued polynomial of degree <=d-1 for every integer n>=3d+3",
    newton_origin:"n0(d)=4d+4",
    defect_range:[2,200],
    checked_newton_coefficients:total,
    all_checked_newton_coefficients_strictly_positive:true,
    minimum_coefficient:smallest.toString(),
    highest_difference_for_each_d:"1",
    direct_six_edge_bigint_dp_length_range:[0,80],
    direct_dp_crosschecks:crosschecks,
    per_defect,
    limitation:"Exact finite parameter certificate yields infinite-n positivity only for 2<=d<=200; d>200 and global peak not resolved",
    independent_driver_review:"NOT_PERFORMED",
    physical_native_transfer:"NOT_ESTABLISHED"
  };
};
const evidence = verify();
process.stdout.write(JSON.stringify(evidence,null,2)+'\n');
