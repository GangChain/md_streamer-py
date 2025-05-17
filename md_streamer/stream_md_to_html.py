import re
import mistune


class MDStreamer:
    last_length = 0
    last_stream_length = 0
    partial: bool = False
    partial_count: int = 0
    chunk_buffer = ""

    async def aprocess_chunk(self, chunk, last=False):
        if last:
            response_to_send = "".join([mistune.html(c) for c in self.chunk_buffer.split("\n\n") if c]).replace("\n", "")
            return response_to_send
        response_to_send = ""
        self.chunk_buffer += chunk
        return self.remove_trailing_html_tags(self.__markdown_to_html())
    
    def process_chunk(self, chunk, last=False):
        if last:
            response_to_send = "".join([mistune.html(c) for c in self.chunk_buffer.split("\n\n") if c]).replace("\n", "")
            return response_to_send
        response_to_send = ""
        self.chunk_buffer += chunk
        return self.remove_trailing_html_tags(self.__markdown_to_html())

    @staticmethod
    def find_partial_markdown(text):
        partial_pattern = r"\*+|\`+"
        return len(re.findall(partial_pattern, text))

    @staticmethod
    def remove_trailing_html_tags(text):
        return re.sub(r"(</[a-zA-Z0-9]+>\s*)+$", "", text)

    @staticmethod
    def replace_strong_tag(text):
        # Replace '**text' with '<strong>text'
        text = re.sub(r'\*\*(\S+)', r'<strong>\1', text)
        # Replace '*text' with '<em>text'
        text = re.sub(r'\*(\S+)', r'<em>\1', text)
        #Replace '`text' with <code>text
        text = re.sub(r'\`(\S+)', r'<code>\1', text)
        # Replace '```<code-language> or ```\n' with ''<pre><code class="language-{code-lang}>'
        code_pattern = r"```[\\n|\n]|```(\S+)"
        code_tags = re.search(code_pattern, text)
        if code_tags:
            if code_tags.group(1):
                text = re.sub(code_pattern, f'<pre><code class="language-{code_tags.group(1)}">\1', text)
            else:
                text = re.sub(code_pattern, r'<pre><code>\1', text)
        return text
    
    def __markdown_to_html(self, partial=False):
        response_to_send = ""
        if resp := [c for c in self.chunk_buffer.split("\n\n") if c]:
            if len(resp) - 1 > self.last_length:
                self.last_stream_length = 0
                self.last_length = len(resp) - 1
            for text in resp[:-1]:
                response_to_send += mistune.html(text)
            stream_response = self.split_mark_text(resp[-1])
            # stream_length = len(stream_response) if partial else len(stream_response) - 1
            stream_length = len(stream_response) - 1
            if stream_length > self.last_stream_length:
                self.last_stream_length = stream_length     
            if stream_response[:self.last_stream_length]:
                length_to_process = self.find_last_word_index(stream_response[:self.last_stream_length])
                response_to_send += self.replace_strong_tag(mistune.html("".join(stream_response[:length_to_process+1])))
        return response_to_send.replace('\n', '')
    
    @staticmethod
    def find_last_word_index(tokens: list) -> int:
        for index in range(len(tokens)-1, -1, -1):
            if re.search(r'^[A-Za-z]', tokens[index]):
                return index
        return 0

    @staticmethod
    def split_mark_text(text):
        split_text = []
        for index, t in enumerate(text.split("\n")):
            if t: 
                x = re.findall(r'\S+|\s+', t)
                if index > 0:
                    x[0] = "\n" + x[0]
                split_text.extend(x)
        return split_text
