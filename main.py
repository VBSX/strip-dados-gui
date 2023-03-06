import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication
import os
import webbrowser

######
#   Coded By Vitor Hugo Borges Dos Santos
#   github.com/vbsx
######

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.handle_paths = PathHandle()
        filter_icon_path = 'filter.png'
        self.github_icon = 'github.png'
        #config of the window
        self.setStyleSheet("padding :15px;background-color: #00008b;color: #FFFFFF ")
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Password Generator')
        self.resize(400, 200)



        self.text_raw = QtWidgets.QLineEdit()
        self.note_of_text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.note_of_text.setText("Coloque o texto a ser filtrado")

        self.text_filtrade = QtWidgets.QPushButton("Retirar 'Traços' e  'Pontos'  !", clicked=self.copy_text)
        
        self.text_mode_title = QtWidgets.QPushButton("Colocar em modo titulo!", clicked=self.make_mode_title)
        self.button_git = QtWidgets.QPushButton('Visite Meu Github', clicked=self.open_git_on_web)
        
        self.text_raw.setStyleSheet("background-color: #008b8b;color: #000000")
        self.text_raw.setStyleSheet("background-color: #FFFFFF;color: #000000")
        
        self.note_of_text.setStyleSheet("background-color: #008b8b;color: #000000")
        
        self.button_git.setIcon(QtGui.QIcon(self.github_icon))
        self.button_git.setIconSize(QtCore.QSize(64,64))
        self.button_git.setStyleSheet("margin-top:20px;background-color: #008b8b;color: #000000")
        
        
        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.layout.addWidget(self.note_of_text)
        
        
        self.layout.addWidget(self.text_raw)
        
        self.layout.addWidget(self.text_filtrade)
        self.layout.addWidget(self.text_mode_title)
        
        self.layout.addWidget(self.button_git)
          
        
    def verify_text_not_empty(self, text):
        if text:
            return True
        
        
        else:
            self.show_dialog("Coloque um texto primeiro!")
            
                
    def filter_of_text(self, text):
        text_without_spaces = text.strip()
        text_filter = text_without_spaces.replace(".", "").replace("-", "")
        return text_filter
        
        
    def copy_text(self):
        text_raw = self.text_raw.text()
        
        if self.verify_text_not_empty(text_raw):
            
            text = self.filter_of_text(text_raw)
            clip = QGuiApplication.clipboard()
            clip.clear()
            clip.setText(text)
            self.show_dialog('O Conteúdo foi copiado para a area de transferência')
        
            
    def make_mode_title(self):
        text = self.text_raw.text()
        
        if self.verify_text_not_empty(text):
            text_mode_title = self.title_mode(text)
            clip = QGuiApplication.clipboard()
            clip.clear()
            clip.setText(text_mode_title)
            self.show_dialog('O Conteúdo foi copiado para a area de transferência')      
    
    def title_mode(self, text):
        
        
        nome_modo_titulo = text.title()
        return nome_modo_titulo           
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
        
        
    def open_git_on_web(self):
        webbrowser.open_new_tab(
        'https://github.com/vbsx'
        )




class PathHandle():

    def resource_path(self,relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())