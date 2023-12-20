import Note

def write_file(array, mode):
    file = open('notes.json', mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open('notes.json', mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close


def read_file():
    try:
        array_notes = []
        file = open('notes.json', 'r', encoding='utf-8')
        notes = file.read().strip().split('\n')
        for n in notes:
            split_note = n.split(';')
            note = Note.Note(id=split_note[0], name=split_note[1], content=split_note[2], date=split_note[3])
            array_notes.append(note)
    except Exception:
        print('There are no saved notes.')
    finally:
        return array_notes
