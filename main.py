import sys
from PyQt5.QtWidgets import QApplication
from app.widgets.search import SearchWidget


app = QApplication(sys.argv)
search = SearchWidget(app)
sys.exit(app.exec())
