from PyQt5 import QtCore, QtGui, QtWidgets
import string
import os
from main import main


class UIDialog(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 230)
        Dialog.setAcceptDrops(True)
        self.formLayout_2 = QtWidgets.QFormLayout(Dialog)
        self.formLayout_2.setObjectName("formLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_13 = QtWidgets.QFormLayout()
        self.formLayout_13.setObjectName("formLayout_13")
        self.startColumnLabel = QtWidgets.QLabel(Dialog)
        self.startColumnLabel.setObjectName("startColumnLabel")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startColumnLabel)
        self.startColumnLineEdit = QtWidgets.QLineEdit(Dialog)
        self.startColumnLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.startColumnLineEdit.setInputMask("")
        self.startColumnLineEdit.setObjectName("startColumnLineEdit")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startColumnLineEdit)
        self.endColumnLabel = QtWidgets.QLabel(Dialog)
        self.endColumnLabel.setObjectName("endColumnLabel")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.endColumnLabel)
        self.endColumnLineEdit = QtWidgets.QLineEdit(Dialog)
        self.endColumnLineEdit.setObjectName("endColumnLineEdit")
        self.formLayout_13.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endColumnLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout_13)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_6.setObjectName("formLayout_6")
        self.startRowLabel = QtWidgets.QLabel(Dialog)
        self.startRowLabel.setObjectName("startRowLabel")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startRowLabel)
        self.startRowLineEdit = QtWidgets.QLineEdit(Dialog)
        self.startRowLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoPredictiveText)
        self.startRowLineEdit.setObjectName("startRowLineEdit")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startRowLineEdit)
        self.endRowLabel = QtWidgets.QLabel(Dialog)
        self.endRowLabel.setObjectName("endRowLabel")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.endRowLabel)
        self.endRowLineEdit = QtWidgets.QLineEdit(Dialog)
        self.endRowLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.endRowLineEdit.setObjectName("endRowLineEdit")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endRowLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout_6)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.selectFileButton = QtWidgets.QPushButton(Dialog)
        self.selectFileButton.setObjectName("selectFileButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.selectFileButton)
        self.fileNameLabel = QtWidgets.QLabel(Dialog)
        self.fileNameLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fileNameLabel.setText("")
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fileNameLabel)
        self.clustersLabel = QtWidgets.QLabel(Dialog)
        self.clustersLabel.setObjectName("clustersLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.clustersLabel)
        self.clustersSpinBox = QtWidgets.QSpinBox(Dialog)
        self.clustersSpinBox.setMinimum(1)
        self.clustersSpinBox.setMaximum(50)
        self.clustersSpinBox.setProperty("value", 5)
        self.clustersSpinBox.setObjectName("clustersSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.clustersSpinBox)
        self.labelColumnLabel = QtWidgets.QLabel(Dialog)
        self.labelColumnLabel.setObjectName("labelColumnLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelColumnLabel)
        self.labelColumnLineEdit = QtWidgets.QLineEdit(Dialog)
        self.labelColumnLineEdit.setObjectName("labelColumnLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelColumnLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem2)

        self.retranslate_ui(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.selectFileButton.clicked.connect(self.set_file)
        self.buttonBox.accepted.connect(self.execute)

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quick Cluster Tool"))
        self.startColumnLabel.setText(_translate("Dialog", "Start Column:"))
        self.startColumnLineEdit.setText(_translate("Dialog", "D"))
        self.startColumnLineEdit.setPlaceholderText(_translate("Dialog", "e.g. \'A\', \'BB\'"))
        self.endColumnLabel.setText(_translate("Dialog", "End Column:"))
        self.endColumnLineEdit.setText(_translate("Dialog", "I"))
        self.endColumnLineEdit.setPlaceholderText(_translate("Dialog", "e.g. \'A\', \'BB\'"))
        self.startRowLabel.setText(_translate("Dialog", "Start Row:"))
        self.startRowLineEdit.setText(_translate("Dialog", "2"))
        self.startRowLineEdit.setPlaceholderText(_translate("Dialog", "e.g. \'1\', \'5\'"))
        self.endRowLabel.setText(_translate("Dialog", "End Row:"))
        self.endRowLineEdit.setText(_translate("Dialog", "102"))
        self.endRowLineEdit.setPlaceholderText(_translate("Dialog", "e.g. \'1\', \'5\'"))
        self.selectFileButton.setText(_translate("Dialog", "Select File"))
        self.clustersLabel.setText(_translate("Dialog", "Clusters:"))
        self.labelColumnLabel.setText(_translate("Dialog", "Label Column:"))
        self.labelColumnLineEdit.setText(_translate("Dialog", "A"))
        self.labelColumnLineEdit.setPlaceholderText(_translate("Dialog", "The column (e.g. \'A\', \'BB\') with datapoint names"))

    def set_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Spreadsheet", "", "Excel Files (*.xlsx)")
        if file_name:
            self.fileNameLabel.setText(file_name)

    def number_from_column(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        return num

    def execute(self):
        if os.path.exists(self.fileNameLabel.text()):
            id, f = os.path.split(self.fileNameLabel.text())
            try:
                lc = self.number_from_column(self.labelColumnLineEdit.text())
                sc = self.number_from_column(self.startColumnLineEdit.text())
                c = self.number_from_column(self.endColumnLineEdit.text()) - sc
                sr = int(self.startRowLineEdit.text())
                r = int(self.endRowLineEdit.text()) - sr
            except ValueError:
                print('Invalid input')
            main("", f=f, id=id, lc=lc, sc=sc, c=c, sr=sr, r=r)
        else:
            print('File path does not exist')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UIDialog()
    ui.setup_ui(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

