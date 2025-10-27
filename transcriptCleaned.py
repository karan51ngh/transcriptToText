import re

def replace_if_timestamp(input_string):

    # Matches formats like 9:30, 14:45, or 8:05:22
    timestamp_regex = r'\d{1,2}:\d{2}(:\d{2})?'

    if re.fullmatch(timestamp_regex, input_string):
        return ' '
    else:
        return input_string

# function to open and parse a file 
def process_file_lines(filepath):
  print(f"--- Processing file: '{filepath}' ---\n")
  try:
    # Use 'with open' to ensure the file is automatically closed
    with open(filepath, 'r', encoding='utf-8') as file:
        processed_lines = []
        for line in file:
            stripped_line = line.strip()
            processed_line = replace_if_timestamp(stripped_line)
            processed_lines.append(processed_line)
        print(processed_lines)
        return processed_lines

  except FileNotFoundError:
    print(f"Error: The file '{filepath}' was not found.")
    return None


if __name__ == "__main__":
    final_content = process_file_lines('./transcript.txt')
    
    output_file = "processed_data.txt" 
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for line in final_content:
            if line[-1] == '.':
                f_out.write(line + '\n')
            else:
                f_out.write(line)
