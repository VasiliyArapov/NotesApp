import File_handler
import Note
import Note_creator

min_size = 3
note_not_found_error = 'Note not found. Check the input ID.'

def add():
    note = Note_creator.create_note(min_size)
    array = File_handler.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    File_handler.write_file(array, 'a')
    print('Note added successfully!')


def show(text):
    logic = True
    array = File_handler.read_file()
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.info(notes))

        elif text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes) + '; Name: ' + Note.Note.get_name(notes) + '.')

        elif text == 'date':
            logic = False
            print('Date of creation: ' + Note.Note.get_date(notes) + '; Name: ' + Note.Note.get_name(notes) + '.')

    if logic == True:
        print('Save new note!')


def id_rewrite():
    id = input(
        'Select the ID of the note you want to overwrite (WARNING: the previous information in this note will be deleted!): ')
    array = File_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            note = Note_creator.create_note(min_size)
            Note.Note.set_name(notes, note.get_name())
            Note.Note.set_content(notes, note.get_content())
            Note.Note.set_date(notes)
            print('Changes saved')
    if logic == True:
        print(note_not_found_error)
    File_handler.write_file(array, 'a')


def id_delete():
    id = input('Input the ID of the note you want to delete (the note cannot be restored): ')
    array = File_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            prov = input('Confirm (y or n): ').strip().lower()
            if prov == 'y':
                array.remove(notes)
                print('Note successfully deleted')
            elif prov == 'n':
                print('Operation canceled')
    if logic == True:
        print(note_not_found_error)
    File_handler.write_file(array, 'a')


def id_show():
    id = input('Input the ID of the note: ')
    array = File_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print(note_not_found_error)
    File_handler.write_file(array, 'a')


def date_show():
    date = input('Enter the date and time of last edit: ')
    array = File_handler.read_file()
    logic = True
    for notes in array:
        if date == Note.Note.get_date(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print(note_not_found_error)
    File_handler.write_file(array, 'a')
