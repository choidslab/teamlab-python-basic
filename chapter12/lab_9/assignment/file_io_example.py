# -*- coding: utf8 -*-

def get_file_contents(filename):
    # '''
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 파일에 나오는 모든 Text 데이터를 문자열로 반환
    # Examples:
    # >>> import file_io_example as fie
    # >>> fie.get_file_contents("1984.txt").split("\n")[0]
    # GEORGE ORWELL
    # ===Modify codes below=============
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()

    # ==================================
    return contents

def get_number_of_characters_with_blank(filename):
    # '''
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 빈칸을 포함하여 해당 파일에 나오는 글자 수의 총합
    # Examples:
    # >>> import file_io_example as fie
    # >>> fie.get_number_of_characters_with_blank("1984.txt")
    # 558841
    # ===Modify codes below=============
    result = len(get_file_contents(filename))

    # ==================================
    return result

def get_number_of_characters_without_blank(filename):
    # '''
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 빈칸을 포함하지 않는 해당 파일에 나오는 글자 수의 총합
    #     여기서 빈칸이라고 함은 " ", "\t", "\n" 을 모두 포함함
    # Examples:
    # >>> import file_io_example as fie
    # >>> fie.get_number_of_characters_without_blank("1984.txt")
    # 459038
    # ===Modify codes below=============
    contents = get_file_contents(filename).replace(" ", "")
    new_contents = " ".join(contents.split())
    result = len(new_contents)

    # ==================================
    return result

def get_number_of_lines(filename):
    # '''
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 해당 파일의 모든 라인수의 총합
    #     단 마지막 줄 수는 제외함
    # Examples:
    # >>> import file_io_example as fie
    # >>> fie.get_number_of_lines("1984.txt")
    # 1414
    # ===Modify codes below=============
    contents_list = get_file_contents(filename).split('\n')
    result = len(contents_list)-1
    # ==================================
    return result

def get_number_of_target_words(filename, target_words):
    # '''
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    #   - target_words : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 대소문자 구분없이 해당 파일에  target_words가 포함된 횟수
    # Examples:
    # >>> import file_io_example as fie
    # >>> fie.get_number_of_words("1984.txt", "Hi")
    # 3938
    # >>> fie.get_number_of_words("1984.txt", "had")
    # 1327
    # >>> fie.get_number_of_words("1984.txt", "and")
    # 2750
    # ===Modify codes below=============
    contents_list = get_file_contents(filename).split()
    # print(contents)
    count = 0
    for word in contents_list:
        if target_words.lower() in word.lower():
            count += 1
    result = count

    # ==================================
    return result
#
# print(get_number_of_lines('1984.txt'))
# print(get_number_of_lines('sample.txt'))
# print(get_number_of_target_words("1984.txt", "Hi"))
# print(get_number_of_target_words("1984.txt", "had"))
# print(get_number_of_target_words("1984.txt", "and"))