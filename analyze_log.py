def analyze_log(log_file):
    try:
        # Open the log file in read mode
        with open(log_file, 'r') as file:
            lines = file.readlines()  # Read all lines from the log file
            total_entries = len(lines)  # Count total log entries

            unique_entries = set(lines)  # Deduplicate log entries to find unique ones
            num_unique_entries = len(unique_entries)

            # Specific patterns to search for (modify as needed)
            critical_patterns = ['error', 'exception', 'failed']

            # Extract and count occurrences of specific patterns
            pattern_count = {pattern: sum(1 for line in lines if pattern in line.lower()) for pattern in critical_patterns}

            # Print the analysis results
            print(f"Total Entries: {total_entries}")
            print(f"Unique Entries: {num_unique_entries}")

            print("Pattern Occurrences:")
            for pattern, count in pattern_count.items():
                print(f"{pattern.capitalize()}: {count}")

    except FileNotFoundError:
        print(f"File '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    log_file_path = input("Enter the path to the log file: ")
    analyze_log(log_file_path)
