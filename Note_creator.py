import Note

def create_note(min_size):
    name = check_len_text(input('Input name of the note: '), min_size)
    content = input('Input a note content: ')
    return Note.Note(name=name, content=content)


def check_len_text(text, min_size):
    while len(text) <= min_size:
        print(f'The note is empty.')
        text = input('\n Input text: \n')
    else:
        return text
