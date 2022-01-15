import json 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])

edit_text = QTextEdit()
list_name = QListWidget()
list_tag = QListWidget()

add_note_btn = QPushButton("Append note")
del_note_btn = QPushButton("Remove note")
save_note_btn = QPushButton("Save note")

add_tag_btn = QPushButton("Add tag to note")
del_tag_btn = QPushButton("Delete tag from note")
find_tag_btn = QPushButton("Find note by tag")

note_label = QLabel("List of notes")
tag_label = QLabel("List of tags")

tag_line = QLineEdit()

basement_layout = QHBoxLayout()
main_layout1 = QVBoxLayout()
main_layout2 = QVBoxLayout()
layout_label_notes = QHBoxLayout()
layout_list_notes = QHBoxLayout()
layout_btns_notes = QHBoxLayout()
layout_btns2_notes = QHBoxLayout()
layout_label_tag = QHBoxLayout()
layout_list_tag = QHBoxLayout()
layout_btns_tag = QHBoxLayout()
layout_btns2_tag = QHBoxLayout()
layout_tag_line = QHBoxLayout()

basement_layout.addLayout(main_layout1)
basement_layout.addLayout(main_layout2)
main_layout2.addLayout(layout_label_notes)
main_layout2.addLayout(layout_list_notes)
main_layout2.addLayout(layout_btns_notes)
main_layout2.addLayout(layout_btns2_notes)
main_layout2.addLayout(layout_label_tag)
main_layout2.addLayout(layout_list_tag)
main_layout2.addLayout(layout_tag_line)
main_layout2.addLayout(layout_btns_tag)
main_layout2.addLayout(layout_btns2_tag)

main_layout1.addWidget(edit_text)
layout_label_notes.addWidget(note_label)
layout_list_notes.addWidget(list_name)
layout_btns_notes.addWidget(add_note_btn)
layout_btns_notes.addWidget(del_note_btn)
layout_btns2_notes.addWidget(save_note_btn)
layout_label_tag.addWidget(tag_label)
layout_tag_line.addWidget(tag_line)
layout_list_tag.addWidget(list_tag)
layout_btns_tag.addWidget(add_tag_btn)
layout_btns_tag.addWidget(del_tag_btn)
layout_btns2_tag.addWidget(find_tag_btn)

with open ("quotes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
list_name.addItems(notes)

def note_find():
    note = list_name.selectAll()[0].text()
    tag = list_tag.selectedItems()[0].text()
    for note in notes:
        if tag in note:
            print (note)

def show_note():
    note = list_name.selectedItems()[0].text()
    print(note)
    edit_text.setText(notes[note]["text"])
    list_tag.clear()
    list_tag.addItems(notes[note]["tags"])

def add_note():
    note_name, ok = QInputDialog.getText(window,"New note", "Input note name")
    if ok:
        notes[note_name] = {"text": "", "tags": []}
        with open ("quotes.json", "w") as file:
            json.dump(notes, file)
        list_name.clear()
        list_name.addItems(notes)

def save_note():
    if list_name.selectedItems(): 
        key = list_name.selectedItems()[0].text()
        notes[key]["text"] = edit_text.toPlainText()
        with open ("quotes.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        dlg2 = QDialog()
        b2 = QLabel("Please select note",dlg2)
        b2.move(150,50)
        dlg2.setWindowTitle("Error")
        dlg2.setWindowModality(Qt.ApplicationModal)
        dlg2.exec()

def del_note():
    if list_name.selectedItems():
        key = list_name.selectedItems()[0].text()
        del notes[key]
        list_name.clear()
        list_tag.clear()
        edit_text.clear()
        list_name.addItems(notes)
        with open ("quotes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
        dlg_del = QDialog()
        b_del = QLabel("Note deleted!",dlg_del)
        b_del.move(150,50)
        dlg_del.setWindowTitle("Succes")
        dlg_del.setWindowModality(Qt.ApplicationModal)
        dlg_del.exec_()
    else:
        dlg_del2 = QDialog()
        b_del2 = QPushButton("Select note!",dlg_del2)
        b_del2.move(150,50)
        dlg_del2.setWindowTitle("Error")
        dlg_del2.setWindowModality(Qt.ApplicationModal)
        dlg_del2.exec_()


def add_tag():
    if list_name.selectedItems():
        key = list_name.selectedItems()[0].text()
        tag = tag_line.text()
        if not tag in notes[key]["tags"] and len(tag) > 0:
            notes[key]["tags"].append(tag)
            list_tag.addItem(tag)
            tag_line.clear()
        with open ("quotes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        list_tag.clear()
        list_tag.addItems(notes[key]["tags"])
        print(notes)
        dlg_add_tag = QDialog()
        b_add_tag = QPushButton("Tag added!",dlg_add_tag)
        b_add_tag.move(150,50)
        dlg_add_tag.setWindowTitle("Succes")
        dlg_add_tag.setWindowModality(Qt.ApplicationModal)
        dlg_add_tag.exec_()
    else:
        dlg_add_tag2 = QDialog()
        b_add_tag2 = QPushButton("Select note!",dlg_add_tag2)
        b_add_tag2.move(150,50)
        dlg_add_tag2.setWindowTitle("Error")
        dlg_add_tag2.setWindowModality(Qt.ApplicationModal)
        dlg_add_tag2.exec_()

def del_tag():
    if list_tag.selectedItems():
        key = list_name.selectedItems()[0].text()
        tag = list_tag.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tag.clear()
        list_tag.addItems(notes[dhkey]["tags"])
        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        dlg_del_tag = QDialog()
        b_del_tag = QPushButton("Tag removed!!",dlg_del_tag)
        b_del_tag.move(150,50)
        dlg_del_tag.setWindowTitle("Succes")
        dlg_del_tag.setWindowModality(Qt.ApplicationModal)
        dlg_del_tag.exec_()
    else:
        dlg_del_tag2 = QDialog()
        b_del_tag2 = QPushButton("Select tag!",dlg_del_tag2)
        b_del_tag2.move(150,50)
        dlg_del_tag2.setWindowTitle("Error")
        dlg_del_tag2.setWindowModality(Qt.ApplicationModal)
        dlg_del_tag2.exec_()

list_name.itemClicked.connect(show_note)
add_note_btn.clicked.connect(add_note)
save_note_btn.clicked.connect(save_note)
del_note_btn.clicked.connect(del_note)
add_tag_btn.clicked.connect(add_tag)
del_tag_btn.clicked.connect(del_tag)
find_tag_btn.clicked.connect(note_find)

window = QWidget()
window.setLayout(basement_layout)
window.resize(900,700)
window.setWindowTitle("Intelectual notes")
window.show()
app.exec_()
