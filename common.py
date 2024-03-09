from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 50, 50))
        self.logo.setMinimumSize(QtCore.QSize(50, 50))
        self.logo.setMaximumSize(QtCore.QSize(50, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo-javascript.svg"))
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 901, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 971, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 991, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(390, 400, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #f0dc55;\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.btn_1.mousePressEvent = lambda event: self.open_js_window(event, MainWindow)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(390, 460, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #f0dc55;\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.btn_2.mousePressEvent = lambda event: self.open_dom_window(event, MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Современный учебник JavaScript"))
        self.label_2.setText(_translate("MainWindow", "<p style=\"font-weight: 500\">Перед вами учебник по JavaScript, начиная с основ,<br> включающий в себя много тонкостей и фишек<br> JavaScript/DOM</p>."))
        self.label_3.setText(_translate("MainWindow", "Содержание"))
        self.label_4.setText(_translate("MainWindow", "<p style=\"font-weight: 500\">Первые две части посвящены JavaScript и его использованию в браузере. Затем идут<br> дополнительные циклы статей на разные темы.</p>"))
        self.btn_1.setText(_translate("MainWindow", "Язык JavaScript"))
        self.btn_2.setText(_translate("MainWindow", "Браузер/DOM"))

    def open_js_window(self, event, MainWindow):
        self.js_window = QtWidgets.QMainWindow()
        self.ui = Ui_JsWindow()
        self.ui.setupUi(self.js_window)
        self.js_window.show()
        MainWindow.close()

    def open_dom_window(self, event, MainWindow):
        self.dom_window = QtWidgets.QMainWindow()
        self.ui = Ui_DomWindow()
        self.ui.setupUi(self.dom_window)
        self.dom_window.show()
        MainWindow.close()

class Ui_DomWindow(object):
    def setupUi(self, DomWindow):
        DomWindow.setObjectName("DomWindow")
        DomWindow.resize(1000, 700)
        DomWindow.setMinimumSize(QtCore.QSize(1000, 700))
        DomWindow.setMaximumSize(QtCore.QSize(1000, 700))
        DomWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(DomWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_main_window(event, DomWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 6, 901, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 971, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 991, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_1.setGeometry(QtCore.QRect(20, 180, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_1.setFont(font)
        self.btn_1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_1.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_1.setObjectName("btn_1_1")
        self.btn_1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_2.setGeometry(QtCore.QRect(450, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_2.setFont(font)
        self.btn_1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_2.setObjectName("btn_1_2")
        self.btn_1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_3.setGeometry(QtCore.QRect(630, 180, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_3.setFont(font)
        self.btn_1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_3.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_3.setObjectName("btn_1_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 991, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_1.setGeometry(QtCore.QRect(20, 430, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_1.setFont(font)
        self.btn_2_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_1.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_1.setObjectName("btn_2_1")
        self.btn_1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_4.setGeometry(QtCore.QRect(20, 230, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_4.setFont(font)
        self.btn_1_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_4.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_4.setObjectName("btn_1_4")
        self.btn_1_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_5.setGeometry(QtCore.QRect(410, 230, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_5.setFont(font)
        self.btn_1_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_5.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_5.setObjectName("btn_1_5")
        self.btn_1_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_6.setGeometry(QtCore.QRect(20, 280, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_6.setFont(font)
        self.btn_1_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_6.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_6.setObjectName("btn_1_6")
        self.btn_1_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_7.setGeometry(QtCore.QRect(280, 280, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_7.setFont(font)
        self.btn_1_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_7.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_7.setObjectName("btn_1_7")
        self.btn_1_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_8.setGeometry(QtCore.QRect(550, 280, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_8.setFont(font)
        self.btn_1_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_8.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_8.setObjectName("btn_1_8")
        self.btn_1_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_10.setGeometry(QtCore.QRect(20, 330, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_10.setFont(font)
        self.btn_1_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_10.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_10.setObjectName("btn_1_10")
        self.btn_1_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_11.setGeometry(QtCore.QRect(400, 330, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_11.setFont(font)
        self.btn_1_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_11.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_11.setObjectName("btn_1_11")
        self.btn_1_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_9.setGeometry(QtCore.QRect(760, 280, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_9.setFont(font)
        self.btn_1_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_9.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_9.setObjectName("btn_1_9")
        self.btn_2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_2.setGeometry(QtCore.QRect(400, 430, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_2.setFont(font)
        self.btn_2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_2.setObjectName("btn_2_2")
        self.btn_2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_3.setGeometry(QtCore.QRect(690, 430, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_3.setFont(font)
        self.btn_2_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_3.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_3.setObjectName("btn_2_3")
        self.btn_2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_4.setGeometry(QtCore.QRect(20, 480, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_4.setFont(font)
        self.btn_2_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_4.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_4.setObjectName("btn_2_4")
        self.btn_2_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_5.setGeometry(QtCore.QRect(410, 480, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_5.setFont(font)
        self.btn_2_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_5.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_5.setObjectName("btn_2_5")
        DomWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DomWindow)
        QtCore.QMetaObject.connectSlotsByName(DomWindow)

    def retranslateUi(self, DomWindow):
        _translate = QtCore.QCoreApplication.translate
        DomWindow.setWindowTitle(_translate("DomWindow", "MainWindow"))
        self.label.setText(_translate("DomWindow", "Браузер/DOM"))
        self.label_2.setText(_translate("DomWindow", "<p style=\"font-weight: 500\">Изучаем работу со страницей – как получать элементы, манипулировать их размерами,<br> динамически создавать интерфейсы и взаимодействовать с посетителем.</p>."))
        self.label_3.setText(_translate("DomWindow", "Документ"))
        self.btn_1_1.setText(_translate("DomWindow", "1.1 Браузерное окружение, спецификации"))
        self.btn_1_2.setText(_translate("DomWindow", "1.2 DOM-дерево"))
        self.btn_1_3.setText(_translate("DomWindow", "1.3 Навигация по DOM-элементам"))
        self.label_4.setText(_translate("DomWindow", "Введение в события"))
        self.btn_2_1.setText(_translate("DomWindow", "2.1 Введение в браузерные события"))
        self.btn_1_4.setText(_translate("DomWindow", "1.4 Поиск: getElement*, querySelector*"))
        self.btn_1_5.setText(_translate("DomWindow", "1.5 Свойства узлов: тип, тег и содержимое"))
        self.btn_1_6.setText(_translate("DomWindow", "1.6 Атрибуты и свойства"))
        self.btn_1_7.setText(_translate("DomWindow", "1.7 Изменение документа"))
        self.btn_1_8.setText(_translate("DomWindow", "1.8 Стили и классы"))
        self.btn_1_10.setText(_translate("DomWindow", "1.10 Размеры и прокрутка элементов"))
        self.btn_1_11.setText(_translate("DomWindow", "1.11 Размеры и прокрутка элементов"))
        self.btn_1_9.setText(_translate("DomWindow", "1.9 Координаты"))
        self.btn_2_2.setText(_translate("DomWindow", "2.2 Всплытие и погружение"))
        self.btn_2_3.setText(_translate("DomWindow", "2.3 Делегирование событий"))
        self.btn_2_4.setText(_translate("DomWindow", "2.4 Действия браузера по умолчанию"))
        self.btn_2_5.setText(_translate("DomWindow", "2.5 Генерация пользовательских событий"))

    def open_main_window(self, event, DomWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        DomWindow.close()


class Ui_JsWindow(object):
    def setupUi(self, JsWindow):
        JsWindow.setObjectName("JsWindow")
        JsWindow.resize(1000, 700)
        JsWindow.setMinimumSize(QtCore.QSize(1000, 700))
        JsWindow.setMaximumSize(QtCore.QSize(1000, 700))
        JsWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(JsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_main_window(event, JsWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 6, 901, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 971, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 991, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_1.setGeometry(QtCore.QRect(20, 220, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_1.setFont(font)
        self.btn_1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_1.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_1.setObjectName("btn_1_1")
        self.btn_1_1.mousePressEvent = lambda event: self.open_Js_1_1_window(event, JsWindow)
        self.btn_1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_2.setGeometry(QtCore.QRect(300, 220, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_2.setFont(font)
        self.btn_1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_2.setObjectName("btn_1_2")
        self.btn_1_2.mousePressEvent = lambda event: self.open_Js_1_2_window(event, JsWindow)
        self.btn_1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_3.setGeometry(QtCore.QRect(650, 220, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_1_3.setFont(font)
        self.btn_1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1_3.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_1_3.setObjectName("btn_1_3")
        self.btn_1_3.mousePressEvent = lambda event: self.open_Js_1_3_window(event, JsWindow)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 991, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_1.setGeometry(QtCore.QRect(20, 320, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_1.setFont(font)
        self.btn_2_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_1.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_1.setObjectName("btn_2_1")
        self.btn_2_1.mousePressEvent = lambda event: self.open_Js_2_1_window(event, JsWindow)
        self.btn_2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_2.setGeometry(QtCore.QRect(200, 320, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_2.setFont(font)
        self.btn_2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_2.setObjectName("btn_2_2")
        self.btn_2_2.mousePressEvent = lambda event: self.open_Js_2_2_window(event, JsWindow)
        self.btn_2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_3.setGeometry(QtCore.QRect(410, 320, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_3.setFont(font)
        self.btn_2_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_3.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_3.setObjectName("btn_2_3")
        self.btn_2_3.mousePressEvent = lambda event: self.open_Js_2_3_window(event, JsWindow)
        self.btn_2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_4.setGeometry(QtCore.QRect(590, 320, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_4.setFont(font)
        self.btn_2_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_4.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_4.setObjectName("btn_2_4")
        self.btn_2_4.mousePressEvent = lambda event: self.open_Js_2_4_window(event, JsWindow)
        self.btn_2_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_5.setGeometry(QtCore.QRect(20, 370, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_5.setFont(font)
        self.btn_2_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_5.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_5.setObjectName("btn_2_5")
        self.btn_2_5.mousePressEvent = lambda event: self.open_Js_2_5_window(event, JsWindow)
        self.btn_2_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_6.setGeometry(QtCore.QRect(300, 370, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_6.setFont(font)
        self.btn_2_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_6.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_6.setObjectName("btn_2_6")
        self.btn_2_6.mousePressEvent = lambda event: self.open_Js_2_6_window(event, JsWindow)
        self.btn_2_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_7.setGeometry(QtCore.QRect(680, 370, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_7.setFont(font)
        self.btn_2_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_7.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_7.setObjectName("btn_2_7")
        self.btn_2_7.mousePressEvent = lambda event: self.open_Js_2_7_window(event, JsWindow)
        self.btn_2_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_8.setGeometry(QtCore.QRect(20, 420, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_8.setFont(font)
        self.btn_2_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_8.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_8.setObjectName("btn_2_8")
        self.btn_2_8.mousePressEvent = lambda event: self.open_Js_2_8_window(event, JsWindow)
        self.btn_2_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_9.setGeometry(QtCore.QRect(330, 420, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_9.setFont(font)
        self.btn_2_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_9.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_9.setObjectName("btn_2_9")
        self.btn_2_9.mousePressEvent = lambda event: self.open_Js_2_9_window(event, JsWindow)
        self.btn_2_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_10.setGeometry(QtCore.QRect(610, 420, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_10.setFont(font)
        self.btn_2_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_10.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_10.setObjectName("btn_2_10")
        self.btn_2_10.mousePressEvent = lambda event: self.open_Js_2_10_window(event, JsWindow)
        self.btn_2_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_11.setGeometry(QtCore.QRect(20, 470, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_11.setFont(font)
        self.btn_2_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_11.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_11.setObjectName("btn_2_11")
        self.btn_2_12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_12.setGeometry(QtCore.QRect(290, 470, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_12.setFont(font)
        self.btn_2_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_12.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_12.setObjectName("btn_2_12")
        self.btn_2_13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_13.setGeometry(QtCore.QRect(440, 470, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_13.setFont(font)
        self.btn_2_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_13.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_13.setObjectName("btn_2_13")
        self.btn_2_14 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_14.setGeometry(QtCore.QRect(700, 470, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_14.setFont(font)
        self.btn_2_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_14.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_14.setObjectName("btn_2_14")
        self.btn_2_15 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_15.setGeometry(QtCore.QRect(20, 520, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_15.setFont(font)
        self.btn_2_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_15.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_15.setObjectName("btn_2_15")
        self.btn_2_16 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_16.setGeometry(QtCore.QRect(610, 520, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_16.setFont(font)
        self.btn_2_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_16.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_16.setObjectName("btn_2_16")
        self.btn_2_17 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2_17.setGeometry(QtCore.QRect(460, 520, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_2_17.setFont(font)
        self.btn_2_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2_17.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color:#f16a30;\n"
"border: none;\n"
"border-radius: 8px;\n"
"transition: all 0.3s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: #4169e1\n"
";\n"
"}")
        self.btn_2_17.setObjectName("btn_2_17")
        JsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(JsWindow)
        QtCore.QMetaObject.connectSlotsByName(JsWindow)

    def retranslateUi(self, JsWindow):
        _translate = QtCore.QCoreApplication.translate
        JsWindow.setWindowTitle(_translate("JsWindow", "MainWindow"))
        self.label.setText(_translate("JsWindow", "Язык JavaScript"))
        self.label_2.setText(_translate("JsWindow", "<p style=\"font-weight: 500\">Здесь вы можете изучить JavaScript, начиная с нуля и заканчивая продвинутыми<br> концепциями вроде ООП.\n"
"\n"
"Мы сосредоточимся на самом языке, изредка добавляя заметки<br> о средах его исполнения.</p>."))
        self.label_3.setText(_translate("JsWindow", "Введение"))
        self.btn_1_1.setText(_translate("JsWindow", "1.1 Введение в JavaScript"))
        self.btn_1_2.setText(_translate("JsWindow", "1.2 Справочники и спецификации"))
        self.btn_1_3.setText(_translate("JsWindow", "1.3 Редакторы кода"))
        self.label_4.setText(_translate("JsWindow", "Основы JavaScript"))
        self.btn_2_1.setText(_translate("JsWindow", "2.1 Привет, мир!"))
        self.btn_2_2.setText(_translate("JsWindow", "2.2 Структура кода"))
        self.btn_2_3.setText(_translate("JsWindow", "2.3 Переменные"))
        self.btn_2_4.setText(_translate("JsWindow", "2.4 Типы данных"))
        self.btn_2_5.setText(_translate("JsWindow", "2.5 Преобразование типов"))
        self.btn_2_6.setText(_translate("JsWindow", "2.6 Базовые операторы, математика"))
        self.btn_2_7.setText(_translate("JsWindow", "2.7 Операторы сравнения"))
        self.btn_2_8.setText(_translate("JsWindow", "2.8 Условное ветвление: if, \'?\'"))
        self.btn_2_9.setText(_translate("JsWindow", "2.9 Логические операторы"))
        self.btn_2_10.setText(_translate("JsWindow", "2.10 Циклы while и for"))
        self.btn_2_11.setText(_translate("JsWindow", "2.11 Конструкция \"switch\""))
        self.btn_2_12.setText(_translate("JsWindow", "2.12 Функции"))
        self.btn_2_13.setText(_translate("JsWindow", "2.13 Function Expression"))
        self.btn_2_14.setText(_translate("JsWindow", "2.14 Стрелочные функции"))
        self.btn_2_15.setText(_translate("JsWindow", "2.15 Взаимодействие: alert, prompt, confirm"))
        self.btn_2_16.setText(_translate("JsWindow", "2.17 Особенности JavaScript"))
        self.btn_2_17.setText(_translate("JsWindow", "2.16 Объекты"))
    
    def open_main_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_1_1_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_1_1()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_1_2_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_1_2()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_1_3_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_1_3()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_1_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_1()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_2_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_2()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_3_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_3()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_4_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_4()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_5_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_5()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_6_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_6()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_7_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_7()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_8_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_8()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_9_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_9()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()

    def open_Js_2_10_window(self, event, JsWindow):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_Js_2_10()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        JsWindow.close()


class Ui_Js_1_1(object):
    def setupUi(self, Js_1_1):
        Js_1_1.setObjectName("Js_1_1")
        Js_1_1.resize(770, 700)
        Js_1_1.setMinimumSize(QtCore.QSize(770, 700))
        Js_1_1.setMaximumSize(QtCore.QSize(770, 700))
        Js_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_1_1)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_1_1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 461, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 3828))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_intro.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_1_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_1_1)
        QtCore.QMetaObject.connectSlotsByName(Js_1_1)

    def retranslateUi(self, Js_1_1):
        _translate = QtCore.QCoreApplication.translate
        Js_1_1.setWindowTitle(_translate("Js_1_1", "MainWindow"))
        self.label.setText(_translate("Js_1_1", "<h2>Введение в JavaScript</h2>"))

    def open_Js_window(self, event, Js_1_1):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_1_1.close()


class Ui_Js_1_2(object):
    def setupUi(self, Js_1_2):
        Js_1_2.setObjectName("Js_1_2")
        Js_1_2.resize(770, 700)
        Js_1_2.setMinimumSize(QtCore.QSize(770, 700))
        Js_1_2.setMaximumSize(QtCore.QSize(770, 700))
        Js_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_1_2)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_1_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 461, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 1016))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_manuals-specifications.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_1_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_1_2)
        QtCore.QMetaObject.connectSlotsByName(Js_1_2)

    def retranslateUi(self, Js_1_2):
        _translate = QtCore.QCoreApplication.translate
        Js_1_2.setWindowTitle(_translate("Js_1_2", "MainWindow"))
        self.label.setText(_translate("Js_1_2", "<h2>Справочники и спецификации</h2>"))

    def open_Js_window(self, event, Js_1_2):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_1_2.close()


class Ui_Js_1_3(object):
    def setupUi(self, Js_1_3):
        Js_1_3.setObjectName("Js_1_3")
        Js_1_3.resize(770, 700)
        Js_1_3.setMinimumSize(QtCore.QSize(770, 700))
        Js_1_3.setMaximumSize(QtCore.QSize(770, 700))
        Js_1_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_1_3)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_1_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 461, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 1160))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_code-editors.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_1_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_1_3)
        QtCore.QMetaObject.connectSlotsByName(Js_1_3)

    def retranslateUi(self, Js_1_3):
        _translate = QtCore.QCoreApplication.translate
        Js_1_3.setWindowTitle(_translate("Js_1_3", "MainWindow"))
        self.label.setText(_translate("Js_1_3", "<h2>Редакторы кода</h2>"))

    def open_Js_window(self, event, Js_1_3):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_1_3.close()


class Ui_Js_2_1(object):
    def setupUi(self, Js_2_1):
        Js_2_1.setObjectName("Js_2_1")
        Js_2_1.resize(770, 700)
        Js_2_1.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_1.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_1)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 211, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 3047))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_hello-world.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_1)
        QtCore.QMetaObject.connectSlotsByName(Js_2_1)

    def retranslateUi(self, Js_2_1):
        _translate = QtCore.QCoreApplication.translate
        Js_2_1.setWindowTitle(_translate("Js_2_1", "MainWindow"))
        self.label.setText(_translate("Js_2_1", "<h2>Привет, мир!</h2>"))

    def open_Js_window(self, event, Js_2_1):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_1.close()


class Ui_Js_2_2(object):
    def setupUi(self, Js_2_2):
        Js_2_2.setObjectName("Js_2_2")
        Js_2_2.resize(770, 700)
        Js_2_2.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_2.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_2)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 251, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 3429))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_structure.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_2)
        QtCore.QMetaObject.connectSlotsByName(Js_2_2)

    def retranslateUi(self, Js_2_2):
        _translate = QtCore.QCoreApplication.translate
        Js_2_2.setWindowTitle(_translate("Js_2_2", "MainWindow"))
        self.label.setText(_translate("Js_2_2", "<h2>Структура кода</h2>"))

    def open_Js_window(self, event, Js_2_1):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_1.close()


class Ui_Js_2_3(object):
    def setupUi(self, Js_2_3):
        Js_2_3.setObjectName("Js_2_3")
        Js_2_3.resize(770, 700)
        Js_2_3.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_3.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_3)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 251, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 8090))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_variables.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_3)
        QtCore.QMetaObject.connectSlotsByName(Js_2_3)

    def retranslateUi(self, Js_2_3):
        _translate = QtCore.QCoreApplication.translate
        Js_2_3.setWindowTitle(_translate("Js_2_3", "MainWindow"))
        self.label.setText(_translate("Js_2_3", "<h2>Переменные</h2>"))

    def open_Js_window(self, event, Ui_Js_2_3):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Ui_Js_2_3.close()


class Ui_Js_2_4(object):
    def setupUi(self, Js_2_4):
        Js_2_4.setObjectName("Js_2_4")
        Js_2_4.resize(770, 700)
        Js_2_4.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_4.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_4)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 251, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -6229, 743, 6863))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_types.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_4.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_4)
        QtCore.QMetaObject.connectSlotsByName(Js_2_4)

    def retranslateUi(self, Js_2_4):
        _translate = QtCore.QCoreApplication.translate
        Js_2_4.setWindowTitle(_translate("Js_2_4", "MainWindow"))
        self.label.setText(_translate("Js_2_4", "<h2>Типы данных</h2>"))

    def open_Js_window(self, event, Js_2_4):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_4.close()


class Ui_Js_2_5(object):
    def setupUi(self, Js_2_5):
        Js_2_5.setObjectName("Js_2_5")
        Js_2_5.resize(770, 700)
        Js_2_5.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_5.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_5)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 380, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 2114, 4160))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_type-conversions.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_5.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_5)
        QtCore.QMetaObject.connectSlotsByName(Js_2_5)

    def retranslateUi(self, Js_2_5):
        _translate = QtCore.QCoreApplication.translate
        Js_2_5.setWindowTitle(_translate("Js_2_5", "MainWindow"))
        self.label.setText(_translate("Js_2_5", "<h2>Преобразование типов</h2>"))

    def open_Js_window(self, event, Js_2_5):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_5.close()


class Ui_Js_2_6(object):
    def setupUi(self, Js_2_6):
        Js_2_6.setObjectName("Js_2_6")
        Js_2_6.resize(770, 700)
        Js_2_6.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_6.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_6)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 531, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 10485))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_operators.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_6.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_6)
        QtCore.QMetaObject.connectSlotsByName(Js_2_6)

    def retranslateUi(self, Js_2_6):
        _translate = QtCore.QCoreApplication.translate
        Js_2_6.setWindowTitle(_translate("Js_2_6", "MainWindow"))
        self.label.setText(_translate("Js_2_6", "<h2>Базовые операторы, математика</h2>"))

    def open_Js_window(self, event, Ui_Js_2_6):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Ui_Js_2_6.close()


class Ui_Js_2_7(object):
    def setupUi(self, Js_2_7):
        Js_2_7.setObjectName("Js_2_7")
        Js_2_7.resize(770, 700)
        Js_2_7.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_7.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_7)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_7)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 531, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 4986))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_comparison.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_7.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_7)
        QtCore.QMetaObject.connectSlotsByName(Js_2_7)

    def retranslateUi(self, Js_2_7):
        _translate = QtCore.QCoreApplication.translate
        Js_2_7.setWindowTitle(_translate("Js_2_7", "MainWindow"))
        self.label.setText(_translate("Js_2_7", "<h2>Операторы сравнения</h2>"))

    def open_Js_window(self, event, Js_2_7):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_7.close()


class Ui_Js_2_8(object):
    def setupUi(self, Js_2_8):
        Js_2_8.setObjectName("Js_2_8")
        Js_2_8.resize(770, 700)
        Js_2_8.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_8.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_8)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_8)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 531, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 4919))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_ifelse.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_8.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_8)
        QtCore.QMetaObject.connectSlotsByName(Js_2_8)

    def retranslateUi(self, Js_2_8):
        _translate = QtCore.QCoreApplication.translate
        Js_2_8.setWindowTitle(_translate("Js_2_8", "MainWindow"))
        self.label.setText(_translate("Js_2_8", "<h2>Условное ветвление: if, \'?\'</h2>"))

    def open_Js_window(self, event, Js_2_8):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_8.close()


class Ui_Js_2_9(object):
    def setupUi(self, Js_2_9):
        Js_2_9.setObjectName("Js_2_9")
        Js_2_9.resize(770, 700)
        Js_2_9.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_9.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_9)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_9)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 531, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 8816))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_logical-operators.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_9.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_9)
        QtCore.QMetaObject.connectSlotsByName(Js_2_9)

    def retranslateUi(self, Js_2_9):
        _translate = QtCore.QCoreApplication.translate
        Js_2_9.setWindowTitle(_translate("Js_2_9", "MainWindow"))
        self.label.setText(_translate("Js_2_9", "<h2>Логические операторы</h2>"))

    def open_Js_window(self, event, Js_2_9):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_9.close()


class Ui_Js_2_10(object):
    def setupUi(self, Js_2_10):
        Js_2_10.setObjectName("Js_2_10")
        Js_2_10.resize(770, 700)
        Js_2_10.setMinimumSize(QtCore.QSize(770, 700))
        Js_2_10.setMaximumSize(QtCore.QSize(770, 700))
        Js_2_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Js_2_10)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(9, 9, 40, 40))
        self.logo.setMinimumSize(QtCore.QSize(40, 40))
        self.logo.setMaximumSize(QtCore.QSize(40, 40))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("QLabel{\n"
"border-radius: 8px;\n"
"teax-align:center;\n"
"background-color:#f16a30;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: #f0dc55;\n"
"}")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("arrow.svg"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_10)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 9, 531, 41))
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 760, 634))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 634))
        self.scrollArea.setStyleSheet("border: none;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 743, 8727))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("learn.javascript.ru_while-for.jpg"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Js_2_10.setCentralWidget(self.centralwidget)

        self.retranslateUi(Js_2_10)
        QtCore.QMetaObject.connectSlotsByName(Js_2_10)

    def retranslateUi(self, Js_2_10):
        _translate = QtCore.QCoreApplication.translate
        Js_2_10.setWindowTitle(_translate("Js_2_10", "MainWindow"))
        self.label.setText(_translate("Js_2_10", "<h2>Циклы while и for</h2>"))

    def open_Js_window(self, event, Js_2_10):
      self.main_window = QtWidgets.QMainWindow()
      self.ui = Ui_JsWindow()
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      Js_2_10.close()




# self.logo.mousePressEvent = lambda event: self.open_Js_window(event, Js_2_4)






