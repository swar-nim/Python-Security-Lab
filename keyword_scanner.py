import os

def search_keyword(keyword, directory):
    try:
        # List of file extensions to search through (can be expanded)
        file_extensions = ['.txt', '.log']

        # List to store files containing the keyword
        files_with_keyword = []

        # Walk through the specified directory and subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file has a relevant extension
                if file.lower().endswith(tuple(file_extensions)):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Read each line and check for the keyword
                        for line_number, line in enumerate(f, start=1):
                            if keyword in line:
                                # If keyword found, add file path and line number to the list
                                files_with_keyword.append(f"{file_path} - Line {line_number}: {line.strip()}")

        # Write results to a results.txt file
        with open('results.txt', 'w', encoding='utf-8') as result_file:
            if files_with_keyword:
                result_file.write(f"Files containing '{keyword}' in {directory}:\n")
                result_file.write('\n'.join(files_with_keyword))
                print("Search completed. Results saved in 'results.txt'")
            else:
                result_file.write(f"No files containing '{keyword}' found in {directory}.")
                print(f"No files containing '{keyword}' found in {directory}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_word = input("Enter the keyword to search for: ")
    search_directory = input("Enter the directory path to search in: ")
    search_keyword(search_word, search_directory)
