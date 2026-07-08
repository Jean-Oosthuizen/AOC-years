#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void part1(){
    ifstream file("input6.txt");
    string data, current_chars;
    int answer = 0;
    bool found;
    getline(file, data);
    for(int i = 3; i < data.size(); ++i){
        found = true;
        current_chars = data.substr(i - 3, 4);
        for(int j = 0; j < 3; ++j){
            for(int k = j+1; k < 4; ++k){
                if(current_chars[j] == current_chars[k]){
                    found = false;
                    break;
                }
            }
            if(!found){
                break;
            }
        }
        if(found){
            answer = i + 1;
            break;
        }
    }
    cout << answer << "\n";
}

void part2(){
    ifstream file("input6.txt");
    string data, current_chars;
    int answer = 0;
    bool found;
    getline(file, data);
    for(int i = 13; i < data.size(); ++i){
        found = true;
        current_chars = data.substr(i - 13, 14);
        for(int j = 0; j < 13; ++j){
            for(int k = j+1; k < 14; ++k){
                if(current_chars[j] == current_chars[k]){
                    found = false;
                    break;
                }
            }
            if(!found){
                break;
            }
        }
        if(found){
            answer = i + 1;
            break;
        }
    }
    cout << answer << "\n";
}

int main(){
    part1();
    part2();
    return 0;
}