import os
import re

def search_keywords(keywords, directory, result_filename):
    try:
        # List of file extensions to search through (can be expanded)
        file_extensions = ['.txt', '.log']

        # List to store files containing the keywords
        files_with_keywords = {keyword: [] for keyword in keywords.split(',')}
        
        # Regular expression pattern for exact word match
        patterns = {keyword: re.compile(rf'\b{re.escape(keyword)}\b') for keyword in keywords.split(',')}

        # Walk through the specified directory and subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file has a relevant extension
                if file.lower().endswith(tuple(file_extensions)):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        # Read each line and check for the keywords
                        for line_number, line in enumerate(f, start=1):
                            for keyword in keywords.split(','):
                                if re.search(patterns[keyword], line):
                                    # If exact word match found, add file path and line number to the list
                                    files_with_keywords[keyword].append(f"{file_path} - Line {line_number}: {line.strip()}")

        # Write results to a user-specified text file
        with open(result_filename + '.txt', 'w', encoding='utf-8') as result_file:
            for keyword in files_with_keywords:
                if files_with_keywords[keyword]:
                    result_file.write(f"Files containing '{keyword}' in {directory}:\n")
                    result_file.write('\n'.join(files_with_keywords[keyword]))
                    result_file.write('\n\n')
            print(f"Search completed. Results saved in '{result_filename}.txt'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Please provide keywords separated by commas (e.g., rain,sun,cloud)")
    search_words = input("Enter the keywords to search for: ")
    
    print("Please provide the directory path using forward slashes (/) for directories (e.g., C:/Users/Username/Documents)")
    search_directory = input("Enter the directory path to search in: ")
    
    result_file_name = input("Enter the filename to save the results in: ")

    search_keywords(search_words, search_directory, result_file_name)
