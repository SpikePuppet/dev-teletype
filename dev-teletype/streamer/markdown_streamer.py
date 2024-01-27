import pendulum

# (27/01/2024) I guess we could make this a parent class, but right now there's no real point.
# Remember, we don't need perfect structure in the beginning.
class MarkdownStreamer():
    def __init__(self, filename=f"{pendulum.now().to_date_string()}.md"):
        self.filename = filename

    def create_output_file(self) -> None:
        try:
            print(f"Creating output file {self.filename}...")
            open(self.filename, "x")
            print("File created!")
        except FileExistsError:     
            print("The file already exists!")

    def stream(self) -> None:
        with open(self.filename, "a") as file:
            while True:
                note = input()
                if note == "exit" or note == "quit":
                    break;

                file.write(f"- {note}\n")
                file.flush()
