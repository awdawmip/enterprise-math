// R255 independently implemented exact provenance suffix-count / rank / unrank
// for the explicitly scoped 3-control formal X6 affine effect graph.
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <vector>
using boost::multiprecision::cpp_int;
using namespace std;
struct Edge { int to,eta,b; };
const Edge ED[3][2]={{{2,-1,-1},{2,1,-1}},{{0,-1,-1},{0,1,-1}},{{1,1,1},{2,1,-1}}};
using Key=tuple<int,int,int>; // q, sign, translation
using Layer=map<Key,cpp_int>;
using Tables=vector<Layer>;
struct Obs{int q,eps,k; bool operator==(const Obs& o) const {return tie(q,eps,k)==tie(o.q,o.eps,o.k);} };
Obs observe(const string& word,int start=0) {
    Obs x{start,1,0};
    for(char c:word){ assert(c=='0'||c=='1');auto a=ED[x.q][c-'0']; x={a.to,a.eta*x.eps,a.eta*x.k+a.b}; }
    return x;
}
Tables build(int target,int n){
    Tables t(n+1); t[0][{target,1,0}]=1;
    for(int len=1;len<=n;len++){
      for(int q=0;q<3;q++)for(int s=0;s<2;s++){
        const auto &a=ED[q][s];
        for(const auto &kv:t[len-1]) {
          auto [qt,tau,d]=kv.first;
          if(qt!=a.to)continue;
          t[len][{q,a.eta*tau,tau*a.b+d}]+=kv.second;
        }
      }
    }
    return t;
}
cpp_int lookup(const Layer& layer,const Key& k){auto it=layer.find(k);return it==layer.end()?cpp_int(0):it->second;}
cpp_int tails(const string& prefix,int horizon,const Obs& ob,const Tables& tables,int start=0){
    assert((int)prefix.size()<=horizon); auto p=observe(prefix,start);
    int rem=horizon-(int)prefix.size(),tau=ob.eps*p.eps, d=ob.k-tau*p.k;
    return lookup(tables[rem],{p.q,tau,d});
}
cpp_int rank_word(const string& word,const Obs& ob,const Tables& table,int source=0){
    assert(observe(word,source)==ob);cpp_int ans=0;string prefix;
    for(char c:word){if(c=='1')ans+=tails(prefix+'0',(int)word.size(),ob,table,source);prefix+=c;}
    return ans;
}
string unrank_word(cpp_int r,int m,const Obs& ob,const Tables& table,int source=0){
    cpp_int total=lookup(table[m],{source,ob.eps,ob.k});assert(r>=0&&r<total);string w;
    for(int i=0;i<m;i++){cpp_int zeros=tails(w+'0',m,ob,table,source);if(r<zeros)w+='0';else{r-=zeros;w+='1';}}
    assert(r==0 && observe(w,source)==ob);return w;
}
int main(){
    const int N=96; vector<Tables> tabs;for(int t=0;t<3;t++)tabs.push_back(build(t,N));
    int exhaustive_words=0;
    for(int source=0;source<3;source++)for(int m=0;m<=10;m++)for(int v=0;v<(1<<m);v++){
      string w(m,'0');for(int j=0;j<m;j++)w[j]=((v>>(m-1-j))&1)?'1':'0';
      Obs ob=observe(w,source);auto &tab=tabs[ob.q];auto r=rank_word(w,ob,tab,source);assert(unrank_word(r,m,ob,tab,source)==w);exhaustive_words++;
    }
    Obs a=observe("000"),b=observe("101");assert(a==b&&a.q==0&&a.eps==1&&a.k==-1);
    assert(rank_word("000",a,tabs[a.q])==0&&rank_word("101",a,tabs[a.q])==1);
    cout<<"{\"status\":\"PASS\",\"exhaustive_words_depth_0_to_10_three_sources\":"<<exhaustive_words<<",\"selected\":{";
    bool first=true;
    for(int m : {3,12,24,40,48,64,96}){
      cpp_int mass=0,mx=0;Obs best{-1,1,0};
      for(int target=0;target<3;target++)for(const auto&kv:tabs[target][m]) {
        auto [source,eps,k]=kv.first;
        if(source!=0) continue;
        mass+=kv.second;
        if(kv.second>mx){mx=kv.second;best={target,eps,k};}
      }
      assert(mass==(cpp_int(1)<<m));
      const auto &tab=tabs[best.q];
      for(const cpp_int& r : vector<cpp_int>{0,mx/2,mx-1}){
        string w=unrank_word(r,m,best,tab);
        assert(rank_word(w,best,tab)==r);
      }
      if(!first) { cout<<","; }
      first=false;
      cout<<"\""<<m<<"\":\""<<mx<<"\"";
    }
    cout<<"},\"native_module_execution\":false}"<<endl;
}
