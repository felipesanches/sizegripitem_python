import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import QRectF, Qt
from PyQt5.uic import loadUi
from SizeGripItem import SizeGripItem

class SimpleResizer():
    def __init__(self, item):
        self.item = item

    def resize(self, rect):
        self.item.setRect(rect)

class Demo(QMainWindow):
    def __init__(self, *args):
        super(Demo, self).__init__(*args)
  
        loadUi('MainWindow.ui', self)
        scene = QGraphicsScene()

        rectItem = QGraphicsRectItem(QRectF(0, 0, 320, 240))
        rectItem.setBrush(Qt.red)
        #rectItem.setPen(Qt.NoPen)
        rectItem.setFlag(QGraphicsItem.ItemIsMovable)
        scene.addItem(rectItem)

        ellipseItem = QGraphicsEllipseItem(QRectF(0, 0, 200, 200))
        ellipseItem.setBrush(Qt.blue)
        #ellipseItem.setPen(Qt.NoPen)
        ellipseItem.setFlag(QGraphicsItem.ItemIsMovable)
        scene.addItem(ellipseItem)

        rectSizeGripItem = SizeGripItem(SimpleResizer(rectItem), rectItem)
        ellipseSizeGripItem = SizeGripItem(SimpleResizer(ellipseItem), ellipseItem)

        graphicsView = QGraphicsView(self)
        graphicsView.setScene(scene)

        self.setCentralWidget(graphicsView)

  
app = QApplication(sys.argv)
widget = Demo()
widget.show()
sys.exit(app.exec_())
