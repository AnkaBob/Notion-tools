import re

file_name = 'isActiveForTheDay'

def transform_file(file_name):

    file_path = "NotionFormulas/Formatted/" + file_name 
    # Read the file
    with open(file_path, 'r') as file:
        content = file.readlines()

    # Transform the content
    function_continue = True
    # find all occurrences of "FileFunction(filename)" and replace them with the content of the file
    while(function_continue):
        function_continue = False
        step1 = []
        for line in content:
            # Check if the line contains a FileFunction
            file_function = re.search(r'FileFunction\((.+?)\)', line)
            if file_function:
                # Get the file name
                function_file_name = "NotionFormulas/Formatted/functions/" + file_function.group(1)
                # Read the file
                with open(function_file_name, 'r') as file:
                    file_content = file.readlines()
                # Append the remaining part of the line after FileFunction
                starting_line = line[:file_function.start()]
                # Append the remaining line only if it is not empty or whitespace
                if starting_line.strip():
                    step1.append(starting_line)
                # Append the file content to the transformed content
                step1.extend(file_content)
                # Append the remaining part of the line after FileFunction
                remaining_line = line[file_function.end():]
                # Append the remaining line only if it is not empty or whitespace
                if remaining_line.strip():
                    step1.append(remaining_line)
                function_continue = True
            else:
                # Append the line to the transformed content
                step1.append(line)
        content = step1


    step2 = []
    for line in step1:
        # Remove comments
        line = line.split('#')[0].strip()
        # Remove leading and trailing spaces
        line = line.strip()
        # Remove spaces not between quotes
        line = re.sub(r'\s+(?=([^"]*"[^"]*")*[^"]*$)', '', line)
        # Append the line to the transformed content
        step2.append(line)

    transformed_content = step2
    # Join the lines into a single line document
    transformed_content = ' '.join(transformed_content)

    # Save the transformed content into a new file
    new_file_path = 'NotionFormulas/Raw/'+ file_name 
    with open(new_file_path, 'w') as file:
        file.write(transformed_content)

    print(f'Transformed content saved to {new_file_path}')

transform_file(file_name)