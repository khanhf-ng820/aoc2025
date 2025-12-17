#include <iostream>
#include <fstream>
#include <string>
#define ll long long int

// Runs in O(nk) time, where k = 12
// Runs in O(k) space, where k = 12



ll charToLL(char c) { return static_cast<ll>(c - '0'); }

int main(){
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	ll totalJoltage = 0;

	while (std::getline(fin, line)) {
		const size_t len = line.length();

		ll maxJoltage = 0;
		ll digits[12];

		int maxDigitIdx = -1;
		for (int i = 11; i >= 0; i--) {
			ll maxDigit = 0;
			for (int idx = maxDigitIdx + 1; idx < len - i; idx++) {
				if (charToLL(line[idx]) > maxDigit) {
					maxDigit = charToLL(line[idx]);
					maxDigitIdx = idx;
				}
			}
			digits[11 - i] = maxDigit;
		}

		ll pow10 = 1;
		for (int i = 11; i >= 0; i--) {
			maxJoltage += digits[i] * pow10;
			pow10 *= 10;
		}

		totalJoltage += maxJoltage;
	}

	fin.close();

	std::cout << "The answer is: " << totalJoltage << std::endl;

	return 0;
}
