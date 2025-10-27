import base64

def main():
    def _f(word: str) -> str:
        if len(word) <= 2:
            return word
        return f'{word[0]}{len(word)-2}{word[-1]}'
    def process_text(text: str) -> str:
        result = []
        current_word = ""
        for char in text:
            if char.isalnum(): 
                current_word += char
            else:
                if current_word:
                    result.append(_f(current_word))
                    current_word = ""
                result.append(char)
        
        if current_word:
            result.append(_f(current_word))
        
        return ''.join(result)
    
    print("input text:")
    user_input = input().strip()
    
    processed_text = process_text(user_input)
    base64_result = base64.b64encode(processed_text.encode('utf-8')).decode('ascii')
    print(f"{base64_result}")

if __name__ == "__main__":
    main()

# flag{aTdoX2lzX2YzeQ==}