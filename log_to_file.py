"""
This could be a cool little program.

I like writing in the terminal, it's a nice experience sometimes. The whole "blank page approach".

What if we could have something which just logs my output, with each line being a bullet point.

It would by default output the notes into a markdown file, though you could make it configurable.

I'd say it'd be in a file somewhere, or like you could run a command which would let you configure the 
options.

This could be super cool, the more I talk about it.
"""
filename = "console-output.log"

try:
    print(f"Creating output file {filename}...")
    open(filename, "x")
    print("File created!")
except FileExistsError:
    print("The file already exists! We're in business")

with open(filename, "a") as file:
    while True:
        value = input()
        if value == "exit":
            break

        file.write(f"{value}\n")
        file.flush()
