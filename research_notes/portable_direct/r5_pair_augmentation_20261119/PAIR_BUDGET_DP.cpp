#include <bits/stdc++.h>
using namespace std;
struct Act{int k;vector<int> masks;};
struct Sig{int id,u,v,mult,f0;vector<Act>acts;};
vector<Sig> read_sigs(){
 vector<Sig> out;ifstream f("pair_signature_census.tsv");string line;getline(f,line);
 while(getline(f,line)){
  istringstream in(line);Sig q;int m;in>>q.id>>q.u>>q.v>>q.mult>>q.f0>>m;
  for(int i=0;i<m;i++){
   string s;in>>s;auto p=s.find(':');Act a;a.k=stoi(s.substr(0,p));
   string t;stringstream qin(s.substr(p+1));
   while(getline(qin,t,','))if(!t.empty())a.masks.push_back(stoi(t));
   q.acts.push_back(a);
  }out.push_back(q);
 }return out;
}
struct DP{
 int f,base,powb[9],stamp=0;
 vector<int>value,version;
 DP(int x):f(x),base(x+2){
  powb[0]=1;for(int i=1;i<=8;i++)powb[i]=powb[i-1]*base;
  value.resize(powb[8]);version.resize(powb[8]);
 }
 int solve(int state,const vector<Act>&aa){
  if(version[state]==stamp)return value[state];
  int e[8],live=0,x=state;
  for(int i=0;i<8;i++){e[i]=x%base;x/=base;if(e[i]<=f)live|=1<<i;}
  if(__builtin_popcount((unsigned)live)<=1){
   version[state]=stamp;return value[state]=0;
  }
  int best=1000000000;
  for(auto&a:aa){
   bool no_progress=false;
   for(int s:a.masks)if((s&live)==live){no_progress=true;break;}
   if(no_progress)continue;
   int mx=0;
   for(int s:a.masks){
    int ns=state;
    for(int i=0;i<8;i++)if(!(s&(1<<i))&&e[i]<f+1)ns+=powb[i];
    mx=max(mx,solve(ns,aa));if(a.k+mx>=best)break;
   }
   best=min(best,a.k+mx);
  }
  if(best==1000000000){cerr<<"NO PROGRESS\n";exit(3);}
  version[state]=stamp;return value[state]=best;
 }
 int root(const vector<Act>&aa){++stamp;return solve(0,aa);}
};
int main(int argc,char**argv){
 int max_f=argc>1?stoi(argv[1]):5;
 int first=argc>2?stoi(argv[2]):0;
 auto all=read_sigs();
 int stop=argc>3?stoi(argv[3]):int(all.size());
 if(max_f<1||max_f>8||first<0||stop>int(all.size()))return 2;
 vector<unique_ptr<DP>>dp(max_f+1);
 for(int f=1;f<=max_f;f++)dp[f]=make_unique<DP>(f);
 ofstream out("pair_budget_results.tsv",first?ios::app:ios::out);
 if(!first)out<<"# id u v multiplicity f0 f1 ... fmax\n";
 for(int i=first;i<stop;i++){
  auto&z=all[i];out<<z.id<<" "<<z.u<<" "<<z.v<<" "<<z.mult<<" "<<z.f0;
  for(int f=1;f<=max_f;f++)out<<" "<<dp[f]->root(z.acts);
  out<<"\n";
  if(i%100==0)out.flush();
 }
 cout<<"BUDGET_DONE first="<<first<<" stop="<<stop<<" max_f="<<max_f<<"\n";
}
