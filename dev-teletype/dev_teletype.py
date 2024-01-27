from streamer import markdown_streamer

if __name__ == "__main__":
    streamer = markdown_streamer.MarkdownStreamer()  
    streamer.create_output_file()
    streamer.stream()