import sys

from PyQt5.QtWidgets import (QWidget, QSpinBox, QPushButton, QLineEdit,
                             QLabel, QGroupBox, QVBoxLayout,
                             QGridLayout, QApplication, QHBoxLayout)


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.hbox = None
        self.resize(300, 300)
        self.items = []
        self.item_count = 0

        label = QLabel("NUMBER OF LINE EDITS")
        label.setStyleSheet("background-color: lightgreen")

        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(0, 7)
        self.spinBox.valueChanged.connect(self.set_item_count)
        self.spinBox.setStyleSheet("background-color: lightgreen")

        # self.button = QPushButton("apply", clicked=self.on_clicked)
        #############################################################
        self.button = QPushButton("apply")
        self.button.clicked.connect(self.on_clicked)

        self.lineEdit = QLineEdit

        self.groupBox = QGroupBox("Line Edit Group Box")
        
        self.vbox_in_group = QVBoxLayout(self.groupBox)

        g_layout = QGridLayout(self)
        g_layout.addWidget(label, 0, 0, 1, 2)
        g_layout.addWidget(self.spinBox, 0, 2, 1, 1)
        g_layout.addWidget(self.button, 1, 0, 1, 1)
        g_layout.addWidget(self.groupBox, 2, 0, 5, 3)

        self.vbox_in_group.addStretch(2)


    def on_clicked(self):
        pass
    #     print(*[item.text() for item in self.items[:self.spinBox.value()]], sep="\n")

    def set_item_count(self, new_count: int):
        self.hbox = {}
        n_items = len(self.items)
        for ii in range(n_items, new_count):
            self.hbox[ii] = QHBoxLayout(self.groupBox)

        n_items = len(self.items)

        for ii in range(n_items, new_count):
            item_left = self.lineEdit(self)
            item_left.setStyleSheet("background-color: yellow")
            self.hbox[ii].insertWidget(n_items, item_left)
            self.items.append(item_left)

            item_right = self.lineEdit(self)
            item_right.setStyleSheet("background-color: yellow")
            self.hbox[ii].insertWidget(n_items, item_right)

            self.vbox_in_group.addLayout(self.hbox[ii])

        for ii in range(self.item_count, new_count):
            # self.vbox_in_group.layout().show()
            self.hbox[ii].itemAt(ii).widget().show()

        for ii in range(new_count, self.item_count):
            self.hbox[ii].itemAt(ii).widget().hide()

        self.item_count = new_count

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook


if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()

    app.exec()
