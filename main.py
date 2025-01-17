from typing import List

def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    def process_file(file):
        file = file.strip()  # 파일의 양 끝 공백 제거
        if '\\' in file:
            file = file.replace('\\', '\\\\')
        if '/' in file:
            file = file.replace('/', '\\/')
        if '"' in file:
            file = file.replace('"', '\\"')
        return file

    template = '{{"English":"{}","German":"{}"}}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        processed_file_list.append(template.format(process_file(english_file), process_file(german_file)))
    return processed_file_list



def write_file_list(file_list: List[str], path: str) -> None:
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')
