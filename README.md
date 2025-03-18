# md_streamer-py Streaming Markdown to HTML Converter

## Overview
This repository provides a lightweight and efficient Python package for converting streaming Markdown content into HTML in real-time. It is designed for applications that need dynamic Markdown rendering, such as live blogging, documentation platforms, and chat applications.

## Features
- **Streaming Conversion**: Processes Markdown input incrementally and converts it to HTML on the fly.
- **Lightweight and Fast**: Optimized for performance and minimal resource usage.
- **Easy Integration**: Can be used as a standalone module or integrated into larger applications.

## Installation

```sh
pip install md-streamer
```

## Usage

### Basic Example
```python
from md_streamer import MDStreamer

md_stream_obj = MDStreamer()

example_content = """Certainly! To split a string in Python, you can use the built-in `split()` method, which divides a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace."""

for md_text in example_content.split(): 
    html_text = md_stream_obj.process_chunk(f" {md_text}")
    print(html_text)
```

### When stream ends to get final output
``` python
html_text = md_stream_obj.process_chunk("", last=True)
print(html_text)
```

### Async Example
```python
import asyncio
from md_streamer import MDStreamer

md_stream_obj = MDStreamer()

example_content = """Certainly! To split a string in Python, you can use the built-in `split()` method, which divides a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace."""

async def md_to_html(text):
    for md_text in text.split(): 
        print(await md_stream_obj.aprocess_chunk(f" {md_text}")))
    print(await md_stream_obj.aprocess_chunk("", last=True))

asyncio.run(md_to_html(example_text))
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the Apache License. See the `LICENSE` file for details.


