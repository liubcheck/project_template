from app.io.input import input_from_console, read_from_file_pandas, read_from_file
from app.io.output import output_to_console, write_to_file

def main():
    user_input = input_from_console()
    output_to_console(user_input)
    write_to_file('data/user_input.txt', user_input)

    file_content = read_from_file('data/Bublyk_zapovidi.txt')
    output_to_console(file_content)
    write_to_file('data/Bublyk_zapovidi_content.txt', file_content)

    df_content = read_from_file_pandas('data/druzi_list.csv')
    df_text = df_content.to_string()
    output_to_console(df_text)
    write_to_file('data/druzi_list_content.txt', df_text)

if __name__ == '__main__':
    main()
