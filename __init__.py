from .autoskipconfig import AutoskipConfig
import cadnano, util
util.qtWrapImport('QtGui', globals(), ['QIcon', 'QPixmap'])
util.qtWrapImport('QtWidgets', globals(), ['QAction'])


class ExtrSkipHandler(object):
	def __init__(self, document, window):
		self.doc, self.win = document, window
		icon10 = QIcon()
		icon10.addPixmap(QPixmap(":/pathtools/skip"), QIcon.Normal, QIcon.Off)
		self.actionExtraSkip = QAction(window)
		self.actionExtraSkip.setIcon(icon10)
		self.actionExtraSkip.setText('AutoSkip')
		self.actionExtraSkip.setToolTip("Click this button to generate a default set of staples.")
		self.actionExtraSkip.setObjectName("actionExtraSkip")
		self.actionExtraSkip.triggered.connect(self.actionExtraSkipSlot)
		self.win.menuPlugins.addAction(self.actionExtraSkip)
		self.win.topToolBar.insertAction(self.win.actionFiltersLabel, self.actionExtraSkip)
		self.win.topToolBar.insertSeparator(self.win.actionFiltersLabel)
		self.configDialog = None

	def actionExtraSkipSlot(self):
		"""Only show the dialog if staple strands exist."""
		part = self.doc.controller().activePart()
		if part != None:  # is there a part?
			for vh in part.getVirtualHelices():
				scafSS = vh.scaffoldStrandSet()
				for o in list(part.oligos()):
					if o.isStaple():  # is there a staple oligo?
						if self.configDialog == None:
							self.configDialog = AutoskipConfig(self.win, self)
						self.configDialog.show()
						return


def documentWindowWasCreatedSlot(doc, win):
	doc.extrSkipHandler = ExtrSkipHandler(doc, win)

# Initialization
for c in cadnano.app().documentControllers:
	doc, win = c.document(), c.window()
	doc.extrSkipHandler = ExtrSkipHandler(doc, win)
cadnano.app().documentWindowWasCreatedSignal.connect(documentWindowWasCreatedSlot)
