"""
config
Created by Jonathan deWerd on 2012-01-19.
"""
import util, cadnano
from . import autoskipconfig_ui
from . import autoskip
util.qtWrapImport('QtGui', globals(), ['QKeySequence'])
util.qtWrapImport('QtCore', globals(), ['Qt'])
util.qtWrapImport('QtWidgets', globals(), ['QDialog', 'QDialogButtonBox'])


class AutoskipConfig(QDialog, autoskipconfig_ui.Ui_Dialog):
    def __init__(self, parent, handler):
        QDialog.__init__(self, parent, Qt.Sheet)
        self.setupUi(self)
        self.handler = handler
        fb = self.buttonBox.button(QDialogButtonBox.Cancel)
        fb.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_R ))

    def keyPressEvent(self, e):
        return QDialog.keyPressEvent(self, e)

    def closeDialog(self):
        self.close()

    def accept(self):
        part = self.handler.doc.controller().activePart()
        if part != None:
            settings = {\
                'targetBpbetweenSkip'             : self.targetBpbetweenSkipBox.value(),\
                'initialPosition'          				: self.initialPositionBox.value(),\
                'numOfSkip'					    : self.numOfSkipBox.value(),\
                'numberofHelices'    					: '2',\
            }
            self.handler.win.pathGraphicsView.setViewportUpdateOn(False)
            # print "pre verify"
            # part.verifyOligos()
            # print "insertStaples"
            autoskip.skipExtraBp(part, settings)
            # print "post break verify"
            # part.verifyOligos()
            self.handler.win.pathGraphicsView.setViewportUpdateOn(True)
        self.close()
