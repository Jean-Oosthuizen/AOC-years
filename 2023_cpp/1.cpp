#include <iostream>
#include <string>
#include <fstream>
#include <regex>
#include <vector>
using namespace std;


void part1(){
    // open file
    ifstream file("input1.txt");
    if (!file){
        cout << "File not found";
        return;
    }

    // init vars
    int answer = 0;
    string line, temp_val, recent_char;
    
    // go through each line
    while(getline(file, line)){
        temp_val = "";
        recent_char = "";
        cout << line << "\n";
        
        // extract relevent digits
        for(char c : line){
            if(isdigit(c)){
                if(temp_val == ""){
                    temp_val = c;
                }
                recent_char = c;
            }
        }

        // update totals
        temp_val += recent_char;
        answer += stoi(temp_val);
    }

    // output answer
    cout << answer << "\n";
}

void part2(){
    vector<string> digits = {
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    };
    ifstream file("input1.txt");
    if(!file){
        cout << "Input file could not be found\n";
        return;
    }


    string line, temp_val, recent_char;
    while(getline(file, line)){
        // clean data
        for(int i = 0; i < digits.size(); ++i){
            line = regex_replace(line, regex(digits[i]), to_string(i));
        }
        cout << line << "\n";
    }

}

int main(){
    part1();
    part2(); // too new at cpp to be able to complete part 2
}