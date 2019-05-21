# -*- coding: utf-8 -*-
import os
import nuke

import PathChanger.FUmod2 as mod
import webbrowser
reload(mod)

try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtWidgets import *
except:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtUiTools import QUiLoader

class PathChanger(QMainWindow):

    WINDOW = 'PathChanger'

    def __init__ (self, parent=None):
        parent_win = QApplication.activeWindow()

        QMainWindow.__init__(self, parent_win)

        loader = QUiLoader()

        self.setWindowTitle(self.WINDOW)

        
    def set_ui(self):
        
        self.ui_path = r'Y:\users\env\nuke\11.2\PathChanger\UI\fu2.ui'

        self.UI = QUiLoader().load(self.ui_path, self)
        self.setWindowTitle("%s" % (self.WINDOW))
        self.setObjectName(self.WINDOW)

        self.target_nodes = [] #Fileが含まれているノード
        self.node_num = 0#対象のノード数
        self.list = []
        self.item = []
        self.name = []
        self.fname = []
        self.name_value = []
        self.checklist = [] #置換対象確認用
        self.cancelnum = [] #変換したか確認用
        self.cancellist = [] #ひとつ前のリスト保管用
        self.sorttable = [] #二次元table
        self.firstlist = []
        self.selectedrow = []

        self.UI.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        self.UI.apply_btn.clicked.connect(self.apply_btn_clicked)
        self.UI.check_btn.clicked.connect(self.check_btn_clicked)
        self.UI.uncheck_btn.clicked.connect(self.uncheck_btn_clicked)
        self.UI.allcheck_btn.clicked.connect(self.allcheck_btn_clicked)
        self.UI.alluncheck_btn.clicked.connect(self.alluncheck_btn_clicked)
        self.UI.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        self.UI.reset_btn.clicked.connect(self.reset_btn_clicked)
        self.UI.dstlist.itemDoubleClicked.connect(self.dstitem_clicked)
        self.UI.open_help.triggered.connect(self.help_pushed)

        mod.list_make(self)
        self.UI.show()

    def refresh_btn_clicked(self):
        mod.delete_table(self)
        mod.list_make(self)

    def apply_btn_clicked(self):
        mod.apply_do(self)

    def check_btn_clicked(self):
        mod.check_do(self)

    def uncheck_btn_clicked(self):
        mod.uncheck_do(self)

    def allcheck_btn_clicked(self):
        mod.allcheck_do(self)

    def alluncheck_btn_clicked(self):
        mod.alluncheck_do(self)

    def cancel_btn_clicked(self):
        mod.cancel_do(self)

    def reset_btn_clicked(self):
        mod.reset_do(self)

    def dstitem_clicked(self):
        mod.move_to(self)

    def help_pushed(self):
        url = 'https://nd.shotgunstudio.com/page/3804#Note_95716'
        webbrowser.open(url)

if __name__ == "__main__":
    main = PathChanger()
    main.set_ui()