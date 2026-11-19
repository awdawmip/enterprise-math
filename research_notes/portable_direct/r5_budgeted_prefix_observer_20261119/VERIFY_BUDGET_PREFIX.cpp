// Exhaustive finite enumeration for budgeted positive prefix observers.
// Domain: N=3, ordered A=2, one Boolean label, edge costs in {0,1}.
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
struct Res {bool safe; int witness_len;};
// M[a][z] deterministic transitions; C[a][z] nonnegative edge costs.
Res decide(const int M[2][3], const int C[2][3], int labels,int S,int x,int B){
  const int base=B+2, inf=B+1;
  int powb[3]={1,base,base*base};
  int cap=3*(B+1)*base*base*base;
  vector<unsigned char> seen(cap,0);
  // encoded queue: key integer and depth. Each V records per-state minimum spend.
  queue<pair<int,int>> Q;
  auto encode=[&](int u,int spent,const int v[3]){
    return (u*(B+1)+spent)*base*base*base+v[0]+v[1]*powb[1]+v[2]*powb[2];
  };
  int v[3]={inf,inf,inf};
  for(int y=0;y<3;y++)if(y!=x && (S&(1<<y)) && (!(labels&(1<<x))||(labels&(1<<y)))) v[y]=0;
  int root=encode(x,0,v);
  if(v[0]==inf && v[1]==inf && v[2]==inf)return {false,0};
  Q.push({root,0});seen[root]=1;
  while(!Q.empty()){
    auto [key,depth]=Q.front();Q.pop();
    int vec=key%(base*base*base);int t=key/(base*base*base);
    int sx=t%(B+1),u=t/(B+1);
    int oldv[3];for(int z=0;z<3;z++){oldv[z]=vec%base;vec/=base;}
    for(int a=0;a<2;a++){
      int nxspent=sx+C[a][u];if(nxspent>B)continue;
      int nu=M[a][u];int nv[3]={inf,inf,inf};
      for(int y=0;y<3;y++)if(oldv[y]<=B){
        int cy=oldv[y]+C[a][y];if(cy>B)continue;
        int ny=M[a][y];
        if((labels&(1<<nu)) && !(labels&(1<<ny)))continue;
        nv[ny]=min(nv[ny],cy);
      }
      if(nv[0]==inf && nv[1]==inf && nv[2]==inf)return {false,depth+1};
      int nk=encode(nu,nxspent,nv);
      if(!seen[nk]){seen[nk]=1;Q.push({nk,depth+1});}
    }
  }
  return {true,-1};
}
int main(){
  uint64_t num=0,safe[4]={},unsafe[4]={}, toggles=0, toggle_up=0, toggle_down=0;
  int max_len[4]={};
  int first[4][8]={{0}}; bool found[4]={};
  // first indexed 1 if safe(0), !safe(1), safe(2); second 0->1 failure ...
  int count_mask[16]={}; uint64_t subset_cases=0,subset_safe[4]={};
  int all_zero_safe=0,all_zero_cases=0;
  for(int m0=0;m0<27;m0++)for(int m1=0;m1<27;m1++){
    int M[2][3];int codes[]={m0,m1};
    for(int a=0;a<2;a++){int code=codes[a];for(int z=0;z<3;z++){M[a][z]=code%3;code/=3;}}
    for(int labs=0;labs<8;labs++)for(int cbits=0;cbits<64;cbits++){
      int C[2][3];for(int a=0;a<2;a++)for(int z=0;z<3;z++) C[a][z]=(cbits>>(3*a+z))&1;
      for(int S=1;S<8;S++)if(__builtin_popcount((unsigned)S)>=2)
      for(int x=0;x<3;x++)if(S&(1<<x)){
        int flags=0; bool vals[4];
        for(int B=0;B<4;B++){
          Res r=decide(M,C,labs,S,x,B);vals[B]=r.safe;
          if(r.safe){safe[B]++;flags|=1<<B; if(m0<4 && m1<4)subset_safe[B]++;}else{unsafe[B]++;max_len[B]=max(max_len[B],r.witness_len);}
        }
        ++num;count_mask[flags]++; if(m0<4 && m1<4)subset_cases++;
        for(int B=0;B<3;B++)if(vals[B]!=vals[B+1]){
          toggles++;
          if(vals[B] && !vals[B+1])toggle_down++;
          else toggle_up++;
        }
        if(cbits==0){all_zero_cases++;if(vals[0])all_zero_safe++;}
        if(vals[0]&&!vals[1]&&vals[2]&&!found[0]){
          found[0]=true;first[0][0]=m0;first[0][1]=m1;first[0][2]=labs;first[0][3]=cbits;first[0][4]=S;first[0][5]=x;
        }
      }
    }
  }
  cout << "{\n  \"scope\":\"exhaustive N=3, A=2 ordered, Boolean support, edge costs 0/1, S>=2, x in S\",\n";
  cout << "  \"cases\":"<<num<<",\n";
  cout << "  \"budget_safe\":["<<safe[0]<<","<<safe[1]<<","<<safe[2]<<","<<safe[3]<<"],\n";
  cout << "  \"subset_m0_m1_0_3\":{\"cases\":"<<subset_cases<<",\"safe\":["<<subset_safe[0]<<","<<subset_safe[1]<<","<<subset_safe[2]<<","<<subset_safe[3]<<"]},\n";
  cout << "  \"budget_unsafe\":["<<unsafe[0]<<","<<unsafe[1]<<","<<unsafe[2]<<","<<unsafe[3]<<"],\n";
  cout << "  \"max_shortest_failure_length\":["<<max_len[0]<<","<<max_len[1]<<","<<max_len[2]<<","<<max_len[3]<<"],\n";
  cout << "  \"adjacent_changes\":{\"all\":"<<toggles<<",\"safe_to_unsafe\":"<<toggle_down<<",\"unsafe_to_safe\":"<<toggle_up<<"},\n";
  cout << "  \"zero_cost_baseline\":{\"cases\":"<<all_zero_cases<<",\"safe\":"<<all_zero_safe<<"},\n";
  cout << "  \"mask_counts\":{";
  bool comma=false;for(int f=0;f<16;f++)if(count_mask[f]){if(comma)cout<<",";comma=true;cout<<"\""<<f<<"\":"<<count_mask[f];}
  cout<<"},\n  \"safe_unsafe_safe_witness\":{\"action_map_indices\":["<<first[0][0]<<","<<first[0][1]<<"],\"labels_mask\":"<<first[0][2]<<",\"cost_mask\":"<<first[0][3]<<",\"S_mask\":"<<first[0][4]<<",\"x\":"<<first[0][5]<<"}\n}\n";
}