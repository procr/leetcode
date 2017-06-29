#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std ;

vector<string> split(const string &s, const string &seperator) {
	vector<string> result;
	typedef string::size_type string_size;
	string_size i = 0;

	while(i != s.size()){
		int flag = 0;
		while(i != s.size() && flag == 0){
			flag = 1;
			for(string_size x = 0; x < seperator.size(); ++x)
				if(s[i] == seperator[x]) {
					++i;
					flag = 0;
					break;
				}
		}

		//找到又一个分隔符，将两个分隔符之间的字符串取出；
		flag = 0;
		string_size j = i;
		while(j != s.size() && flag == 0){
			for(string_size x = 0; x < seperator.size(); ++x)
				if(s[j] == seperator[x]){
					flag = 1;
					break;
				}
			if(flag == 0) 
				++j;
		}
		if(i != j){
			result.push_back(s.substr(i, j-i));
			i = j;
		}
	}
	return result;
}



int main()
{

	// vector
	vector< vector<int> > b(1 + 1, vector<int>(1 + 1, 0));
	b[0][0] = 1;
	b[1][0] = 3;
	cout << b[0][0] << b[1][0] << endl;



	// map
	map<string , int >mm;         
	mm.insert(pair<string, int>("key1", 1));
	mm.insert(map<string, int>::value_type("key2", 2));

	map <string, int>::iterator iter;

	for ( iter = mm.begin(); iter != mm.end(); iter++ ) {
		cout << iter->first << ": " <<iter->second << endl;
	}

	iter = mm.find("key1");
	if(iter == mm.end()) {
		cout << "we do not find" << endl;
	} else {
		mm.erase(iter);
		cout << "deleted" << endl;
		for ( iter = mm.begin(); iter != mm.end(); iter++ ) {
			cout << iter->first << ": " <<iter->second << endl;
		}
	}



	// split
	string s = "a,b*c*d,e";
	vector<string> v = split(s, ",*"); //可按多个字符来分隔;
	for(vector<string>::size_type i = 0; i != v.size(); ++i)
		cout << v[i] << " ";
	cout << endl;








	return 0;
}