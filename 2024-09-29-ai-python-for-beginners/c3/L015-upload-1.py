import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt6.QtCore import Qt

class FileUploader(QWidget):
    def __init__(self):
        super().__init__()

        # 设置用户界面
        self.setWindowTitle("文件上传器")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # 标签，用于显示选择的文件路径
        self.file_label = QLabel("未选择文件")
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 将文本居中对齐
        layout.addWidget(self.file_label)

        # 按钮，用于打开文件对话框
        self.upload_button = QPushButton("上传文件")
        self.upload_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.upload_button)

        # 设置布局
        self.setLayout(layout)

    def open_file_dialog(self):
        # 打开文件对话框选择文件
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*)")
        
        if file_name:
            # 在标签上显示选中的文件路径
            self.file_label.setText(f"选中的文件: {file_name}")
            
            # 如果 'docs' 目录不存在，则创建它
            docs_dir = os.path.join(os.getcwd(), 'docs')
            if not os.path.exists(docs_dir):
                os.makedirs(docs_dir)
            
            # 将选中的文件复制到 'docs' 目录
            try:
                destination_path = os.path.join(docs_dir, os.path.basename(file_name))
                shutil.copy(file_name, destination_path)
                self.file_label.setText(f"文件保存至: {destination_path}")
            except Exception as e:
                self.file_label.setText(f"保存文件时出错: {str(e)}")
        else:
            self.file_label.setText("未选择文件")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uploader = FileUploader()
    uploader.show()
    sys.exit(app.exec())
