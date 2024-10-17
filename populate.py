import json
import random

def generate_latex(randomize=False):
    # Step 1: Read the JSON file
    with open('exercises-intervals.json', 'r') as file:
        data = json.load(file)

    # Step 2: Extract exercises and solutions into lists
    pairs = [(item['exercise'], item['solution']) for item in data]

    # Step 3: Randomize the pairs if the option is set
    if randomize:
        random.shuffle(pairs)

    # Step 4: Create the LaTeX content
    with open('content.tex', 'w') as latex_file:
        # Start LaTeX structure
        latex_file.write("\\vdomi{START}{" + pairs[0][0] + "}\n")

        # Write the alternating solutions and exercises
        for i in range(1, len(pairs)):
            latex_file.write("\\vdomi{" + pairs[i-1][1] + "}{" + pairs[i][0] + "}\n")

        # End LaTeX structure with the final solution
        latex_file.write("\\vdomi{" + pairs[-1][1] + "}{END}\n")

        if (len(pairs) % 2 == 0):
            latex_file.write("\\vdomi{}{}\n")

# Call the function, you can set randomize=True to shuffle the pairs
generate_latex(randomize=True)
