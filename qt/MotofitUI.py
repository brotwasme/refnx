# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/Motofit.ui'
#
# Created: Tue Sep 11 13:27:26 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 462)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1063, 462))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 125, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphs = QtGui.QTabWidget(self.centralwidget)
        self.graphs.setObjectName("graphs")
        self.reflectivity = QtGui.QWidget()
        self.reflectivity.setObjectName("reflectivity")
        self.gridLayout_5 = QtGui.QGridLayout(self.reflectivity)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphs.addTab(self.reflectivity, "")
        self.sld = QtGui.QWidget()
        self.sld.setObjectName("sld")
        self.gridLayout_4 = QtGui.QGridLayout(self.sld)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphs.addTab(self.sld, "")
        self.gridLayout_3.addWidget(self.graphs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 22))
        self.menubar.setObjectName("menubar")
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuModel = QtGui.QMenu(self.menubar)
        self.menuModel.setObjectName("menuModel")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPlot_type = QtGui.QMenu(self.menubar)
        self.menuPlot_type.setObjectName("menuPlot_type")
        self.menuExperiment = QtGui.QMenu(self.menubar)
        self.menuExperiment.setObjectName("menuExperiment")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(450, 440))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.use_errors_checkbox = QtGui.QCheckBox(self.tab)
        self.use_errors_checkbox.setObjectName("use_errors_checkbox")
        self.gridLayout_2.addWidget(self.use_errors_checkbox, 2, 1, 1, 1)
        self.dataset_comboBox = QtGui.QComboBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dataset_comboBox.setFont(font)
        self.dataset_comboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dataset_comboBox.setObjectName("dataset_comboBox")
        self.gridLayout_2.addWidget(self.dataset_comboBox, 0, 0, 1, 1)
        self.do_fit_button = QtGui.QPushButton(self.tab)
        self.do_fit_button.setMinimumSize(QtCore.QSize(0, 60))
        self.do_fit_button.setObjectName("do_fit_button")
        self.gridLayout_2.addWidget(self.do_fit_button, 0, 1, 2, 1)
        self.res_SpinBox = QtGui.QDoubleSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.res_SpinBox.setFont(font)
        self.res_SpinBox.setWrapping(False)
        self.res_SpinBox.setFrame(True)
        self.res_SpinBox.setReadOnly(False)
        self.res_SpinBox.setDecimals(1)
        self.res_SpinBox.setMaximum(10.0)
        self.res_SpinBox.setSingleStep(0.1)
        self.res_SpinBox.setProperty("value", 5.0)
        self.res_SpinBox.setObjectName("res_SpinBox")
        self.gridLayout_2.addWidget(self.res_SpinBox, 3, 0, 1, 1)
        self.use_dqwave_checkbox = QtGui.QCheckBox(self.tab)
        self.use_dqwave_checkbox.setChecked(True)
        self.use_dqwave_checkbox.setObjectName("use_dqwave_checkbox")
        self.gridLayout_2.addWidget(self.use_dqwave_checkbox, 3, 1, 1, 1)
        self.model_comboBox = QtGui.QComboBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.model_comboBox.setFont(font)
        self.model_comboBox.setObjectName("model_comboBox")
        self.gridLayout_2.addWidget(self.model_comboBox, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.layerModelView = QtGui.QTableView(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layerModelView.setFont(font)
        self.layerModelView.setObjectName("layerModelView")
        self.layerModelView.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.layerModelView, 5, 0, 1, 2)
        self.baseModelView = QtGui.QTableView(self.tab)
        self.baseModelView.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.baseModelView.setFont(font)
        self.baseModelView.setObjectName("baseModelView")
        self.baseModelView.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.baseModelView, 4, 0, 1, 2)
        self.horizontalSlider = QtGui.QSlider(self.tab)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 18))
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider.setMaximum(999)
        self.horizontalSlider.setProperty("value", 499)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 6, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dataOptions_tableView = QtGui.QTableView(self.tab_2)
        self.dataOptions_tableView.setObjectName("dataOptions_tableView")
        self.dataOptions_tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.dataOptions_tableView.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.dataOptions_tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 2, 2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionLoad_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Data.setCheckable(False)
        self.actionLoad_Data.setChecked(False)
        self.actionLoad_Data.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionSave_Data = QtGui.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionSave_Model = QtGui.QAction(MainWindow)
        self.actionSave_Model.setObjectName("actionSave_Model")
        self.actionLoad_Model = QtGui.QAction(MainWindow)
        self.actionLoad_Model.setObjectName("actionLoad_Model")
        self.actionLogR_vs_Q = QtGui.QAction(MainWindow)
        self.actionLogR_vs_Q.setCheckable(True)
        self.actionLogR_vs_Q.setChecked(True)
        self.actionLogR_vs_Q.setObjectName("actionLogR_vs_Q")
        self.actionRQ4_vs_Q = QtGui.QAction(MainWindow)
        self.actionRQ4_vs_Q.setObjectName("actionRQ4_vs_Q")
        self.actionRQ4_vs_Q_2 = QtGui.QAction(MainWindow)
        self.actionRQ4_vs_Q_2.setObjectName("actionRQ4_vs_Q_2")
        self.actionRefresh_Datasets = QtGui.QAction(MainWindow)
        self.actionRefresh_Datasets.setObjectName("actionRefresh_Datasets")
        self.actionLoad_experiment = QtGui.QAction(MainWindow)
        self.actionLoad_experiment.setObjectName("actionLoad_experiment")
        self.actionSave_experiment = QtGui.QAction(MainWindow)
        self.actionSave_experiment.setObjectName("actionSave_experiment")
        self.menuData.addAction(self.actionLoad_Data)
        self.menuData.addAction(self.actionRefresh_Datasets)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionSave_Data)
        self.menuModel.addAction(self.actionSave_Model)
        self.menuModel.addAction(self.actionLoad_Model)
        self.menuPlot_type.addAction(self.actionLogR_vs_Q)
        self.menuPlot_type.addAction(self.actionRQ4_vs_Q)
        self.menuPlot_type.addAction(self.actionRQ4_vs_Q_2)
        self.menuExperiment.addAction(self.actionLoad_experiment)
        self.menuExperiment.addAction(self.actionSave_experiment)
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuModel.menuAction())
        self.menubar.addAction(self.menuPlot_type.menuAction())
        self.menubar.addAction(self.menuExperiment.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.graphs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.dataset_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Motofit", None, QtGui.QApplication.UnicodeUTF8))
        self.graphs.setTabText(self.graphs.indexOf(self.reflectivity), QtGui.QApplication.translate("MainWindow", "reflectivity", None, QtGui.QApplication.UnicodeUTF8))
        self.graphs.setTabText(self.graphs.indexOf(self.sld), QtGui.QApplication.translate("MainWindow", "sld", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModel.setTitle(QtGui.QApplication.translate("MainWindow", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlot_type.setTitle(QtGui.QApplication.translate("MainWindow", "Plot type", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExperiment.setTitle(QtGui.QApplication.translate("MainWindow", "Experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Motofit", None, QtGui.QApplication.UnicodeUTF8))
        self.use_errors_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Use errors?", None, QtGui.QApplication.UnicodeUTF8))
        self.do_fit_button.setText(QtGui.QApplication.translate("MainWindow", "Do Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.do_fit_button.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+F", None, QtGui.QApplication.UnicodeUTF8))
        self.res_SpinBox.setPrefix(QtGui.QApplication.translate("MainWindow", "dq/q(%) : ", None, QtGui.QApplication.UnicodeUTF8))
        self.use_dqwave_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Use dq wave?", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Global Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Data.setText(QtGui.QApplication.translate("MainWindow", "Load Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Data.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Data.setText(QtGui.QApplication.translate("MainWindow", "Save Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Data.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Model.setText(QtGui.QApplication.translate("MainWindow", "Save Model", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Model.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Model.setText(QtGui.QApplication.translate("MainWindow", "Load Model", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Model.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogR_vs_Q.setText(QtGui.QApplication.translate("MainWindow", "logR vs Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRQ4_vs_Q.setText(QtGui.QApplication.translate("MainWindow", "R vs Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRQ4_vs_Q_2.setText(QtGui.QApplication.translate("MainWindow", "RQ4 vs Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh_Datasets.setText(QtGui.QApplication.translate("MainWindow", "Refresh Datasets", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh_Datasets.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_experiment.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_experiment.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_experiment.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_experiment.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+M", None, QtGui.QApplication.UnicodeUTF8))

