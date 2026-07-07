#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
using namespace std;

void part1(){
    ifstream file("input3.txt");
    unordered_map<char, int> items;
    int answer = 0;
    int linelen, dupe_score;
    char duplicate;
    string line, pouch_1, pouch_2;
    while(getline(file, line)){
        items.clear();
        linelen = line.length();
        pouch_1 = line.substr(0, linelen / 2);
        pouch_2 = line.substr(linelen / 2, linelen);
        for(char c : pouch_1){
            items[c] = 1;
        }
        for (char c : pouch_2){
            if(items.count(c) > 0){
                duplicate = c;
                break;
            }
        }
        dupe_score = static_cast<int>(duplicate);
        if(dupe_score < 95){
            // uppercase
            dupe_score -= 38;
        } else{
            // lowercase
            dupe_score -= 96;
        }
        answer += dupe_score;
        // cout << pouch_1 << "-" << pouch_2 << ", " << duplicate << ", " << dupe_score << "\n\n";
    }
    cout << answer << "\n";
}

void part2(){
    ifstream file("input3.txt");
    int answer = 0, i = 1, linelen, dupe_score;
    char duplicate;
    string line, pouch_1, pouch_2;
    unordered_map<char, int> added_items;
    unordered_map<char, int> items;
    items.clear();
    while(getline(file, line)){
        // grab characters from batches of 3 lines
        added_items.clear();
        for(char c : line){
            if(added_items.count(c) == 0){
                added_items[c] = 1;
                if(items.count(c) > 0){
                    items[c] += 1;
                }else{
                    items[c] = 1;
                }
            }
        }        
        // every 3 lines clear current list and establish dupe
        if(i % 3 == 0){
            for(auto [key, value] : items){
                if(value == 3){
                    dupe_score = static_cast<int>(key);
                    break;
                }
            }
            items.clear();
            if(dupe_score < 95){
                // uppercase
                dupe_score -= 38;
            } else{
                // lowercase
                dupe_score -= 96;
            }
            answer += dupe_score;
            // cout << pouch_1 << "-" << pouch_2 << ", " << duplicate << ", " << dupe_score << "\n\n";
        }
        i++;
    }
    cout << answer << "\n";
}

int main(){
    part1();
    part2();
    return 0;
}