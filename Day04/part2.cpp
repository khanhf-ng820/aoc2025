#include <iostream>
#include <fstream>
#include <string>
#include <vector>



int main(){
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	std::vector<std::string> grid;

	while (std::getline(fin, line)) {
		grid.push_back(line);
	}

	const size_t rows = grid.size();
	const size_t cols = grid[0].length();
	std::vector<std::pair<int, int>> removable;
	removable.reserve(rows * cols);
	int totalCount = 0;
	int count = -1;

	while (count != 0) {
		count = 0;
		removable.clear();

		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < cols; j++) {
				if (grid[i][j] != '@') continue;
				int adjacent = 0;
				for (int di = -1; di < 2; di++) {
					for (int dj = -1; dj < 2; dj++) {
						if (di == 0 && dj == 0) continue;
						int i0 = i+di, j0 = j+dj;
						if (i0 >= 0 && i0 < rows && j0 >= 0 && j0 < cols
							&& grid[i0][j0] == '@')
							adjacent++;
					}
				}
				if (adjacent < 4) {
					count++;
					removable.push_back(std::make_pair(i, j));
				}
			}
		}

		totalCount += count;

		for (const auto& [i, j] : removable) {
			grid[i][j] = '.';
		}
	}



	fin.close();

	std::cout << "The answer is: " << totalCount << std::endl;

	return 0;
}
