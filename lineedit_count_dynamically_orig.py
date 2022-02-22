# lineedit_count_dynamically_orig.py

from PyQt5.QtWidgets import (QWidget, QSpinBox, QPushButton, QLineEdit,
                             QLabel, QGroupBox, QVBoxLayout,
                             QGridLayout, QApplication)


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(300, 300)
        self.items = []
        self.item_count = 0

        label = QLabel("NUMBER OF LINE EDITS")

        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(0, 7)
        self.spinBox.valueChanged.connect(self.set_item_count)

        # self.button = QPushButton("apply", clicked=self.on_clicked)
        #############################################################
        self.button = QPushButton("apply")
        self.button.clicked.connect(self.on_clicked)

        self.lineEdit = QLineEdit

        groupBox = QGroupBox("Line Edit")
        self.item_layout = QVBoxLayout(groupBox)
        self.item_layout.addStretch(2)

        g_layout = QGridLayout(self)
        g_layout.addWidget(label, 0, 0, 1, 2)
        g_layout.addWidget(self.spinBox, 0, 2, 1, 1)
        g_layout.addWidget(self.button, 1, 0, 1, 1)
        g_layout.addWidget(groupBox, 2, 0, 5, 3)

    def on_clicked(self):
        print(*[item.text() for item in self.items[:self.spinBox.value()]], sep="\n")

    def set_item_count(self, new_count: int):
        n_items = len(self.items)

        for ii in range(n_items, new_count):
            item = self.lineEdit(self)
            self.items.append(item)
            self.item_layout.insertWidget(n_items, item)

        for ii in range(self.item_count, new_count):
            self.item_layout.itemAt(ii).widget().show()

        for ii in range(new_count, self.item_count):
            self.item_layout.itemAt(ii).widget().hide()

        self.item_count = new_count


if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()
    app.exec()

