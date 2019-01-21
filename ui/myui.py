# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.externals import joblib
clf = joblib.load('mlpdata_log.joblib')
ct = joblib.load('ct_log.joblib')
le = joblib.load('le_log.joblib')
class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 214)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 341, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 347, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton.clicked.connect(self.uygula)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ürün Kategorisi Tahmin"))
        self.pushButton.setText(_translate("Form", "Tahmin Et"))
        self.label.setText(_translate("Form", "Tahmin etmek istediğiniz ürün hakkında açıklama yazın"))
        self.label_2.setText(_translate("Form", "Sonuç"))
    def uygula(self):        
        deger=self.lineEdit.text()
        print(deger)
        #deger=ui.lineEdit.text()
        dene=[deger]
        denect=ct.transform(dene)
        deneme=clf.predict(denect)
        asd=le.inverse_transform(deneme)
        ui.label_2.setText(str(asd))

        #print(clf.predict_proba(denect))
if __name__=='__main__':
    import sys
    app =QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())