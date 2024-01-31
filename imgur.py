import re

def replace_links(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    updated_content = re.sub(r'http://i.imgur.com/([^\s]+)', r'https://images.weserv.nl/?url=http://i.imgur.com/\1', content)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(updated_content)

if __name__ == "__main__":
    mod_path = input("Mod Id: ")
    input_file_path = f'{mod_path}.json'
    output_file_path = f'{mod_path}.json'

    replace_links(input_file_path, output_file_path)
