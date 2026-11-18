#include <bits/stdc++.h>
using namespace std;
constexpr int INF=1000000;
struct Node {int parent;uint32_t sup;int label;};
struct DP {int s[6],p[15],t[20];};
int pi_[15],pj_[15],ti_[20],tj_[20],tk_[20],pidx[6][6];
int main(int argc,char**argv){
 if(argc<4){cerr<<"USAGE trie qs limit\n";return 2;}
 ifstream f(argv[1]); vector<Node> v;int a,b,c;
 while(f>>a>>b>>c)v.push_back({a,(uint32_t)b,c?__builtin_ctz((unsigned)c):-1});
 int N=v.size();for(int i=0,k=0;i<6;i++)for(int j=i+1;j<6;j++,k++){pi_[k]=i;pj_[k]=j;pidx[i][j]=pidx[j][i]=k;}
 for(int i=0,k=0;i<6;i++)for(int j=i+1;j<6;j++)for(int l=j+1;l<6;l++,k++){ti_[k]=i;tj_[k]=j;tk_[k]=l;}
 vector<DP> dp(N);ifstream in(argv[2]);string line;int checked=0,pair_excluded=0,triple_excluded=0,survivors=0;map<int,int> failure_hist_pair, failure_hist_triple;vector<string> survivors_lines;
 auto st=chrono::steady_clock::now();while(getline(in,line)){
  if(line.empty())continue; if(atoi(argv[3])>0&&checked>=atoi(argv[3]))break;
  stringstream ss(line);int q[6];uint32_t mask=0;int local[24];fill(local,local+24,-1);for(int j=0;j<6;j++){ss>>q[j];mask|=1u<<q[j];local[q[j]]=j;}
  for(int i=0;i<N;i++){
   fill(dp[i].s,dp[i].s+6,INF);fill(dp[i].p,dp[i].p+15,INF);fill(dp[i].t,dp[i].t+20,INF);
   int lab=v[i].label; if(lab>=0&&local[lab]>=0)dp[i].s[local[lab]]=0;
  }
  for(int u=N-1;u>=1;u--){
   int par=v[u].parent, edge=(v[u].sup & ~mask)?0:1;
   DP &x=dp[par],&y=dp[u];
   for(int k=0;k<20;k++){
    int i=ti_[k],j=tj_[k],l=tk_[k];int z=min(x.t[k],y.t[k]+edge);
    z=min(z,x.p[pidx[i][j]]+y.s[l]+edge);z=min(z,x.p[pidx[i][l]]+y.s[j]+edge);z=min(z,x.p[pidx[j][l]]+y.s[i]+edge);
    z=min(z,x.s[i]+y.p[pidx[j][l]]+edge);z=min(z,x.s[j]+y.p[pidx[i][l]]+edge);z=min(z,x.s[l]+y.p[pidx[i][j]]+edge);
    x.t[k]=z;
   }
   for(int k=0;k<15;k++){
    int i=pi_[k],j=pj_[k];int z=min(x.p[k], y.p[k]+edge);
    z=min(z,x.s[i]+y.s[j]+edge);z=min(z,x.s[j]+y.s[i]+edge);x.p[k]=z;
   }
   for(int k=0;k<6;k++)x.s[k]=min(x.s[k],y.s[k]+edge);
  }
  int failpair=0,failtriple=0;
  for(int k=0;k<15;k++)if(dp[0].p[k]>11){failpair=k+1;break;}
  if(failpair){pair_excluded++;failure_hist_pair[failpair]++;}
  else {for(int k=0;k<20;k++)if(dp[0].t[k]>11){failtriple=k+1;break;}
   if(failtriple){triple_excluded++;failure_hist_triple[failtriple]++;}
   else {survivors++;survivors_lines.push_back(line);}}
  checked++;
  if(checked%500==0)cerr<<"cases="<<checked<<" pair="<<pair_excluded<<" triple="<<triple_excluded<<" survivors="<<survivors<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<"\n";
 }
 cout<<"{\"checked\":"<<checked<<",\"pair_excluded\":"<<pair_excluded<<",\"triple_new_excluded\":"<<triple_excluded<<",\"triple_survivors\":"<<survivors<<",\"elapsed_s\":"<<fixed<<setprecision(3)<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<",\"first_failed_pair\":{";
 bool first=true;for(auto [k,n]:failure_hist_pair){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":"<<n;}cout<<"},\"first_failed_triple\":{";first=true;for(auto [k,n]:failure_hist_triple){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":"<<n;}cout<<"}}\n";
 for(string s:survivors_lines)cout<<"SURV "<<s<<"\n";
}
