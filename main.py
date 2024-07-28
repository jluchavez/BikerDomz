import sys
import calendar
from datetime import datetime
import sqlite3
from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
# Importing Dialogs
from ui_login import Ui_Login_Dialog
from ui_register import Ui_SignIn_Dialog
from ui_main import Ui_MainWindow
from ui_edit import Ui_Edit_Dialog
from ui_add import Ui_Add_Dialog
from ui_order import Ui_Order_Dialog
from ui_add_stock import Ui_AddStock_Dialog
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

# Creating Database
conn = sqlite3.connect("DBMS.db")
cursor = conn.cursor()
# Creating Table for users
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password INTEGER)")
conn.commit()
# Creating Table for items
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, productname TEXT, category TEXT, quantity INTEGER, price INTEGER, date DATE)")
conn.commit()
# Creating Table for order list
cursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY, order_productname TEXT, order_category TEXT, order_price INTEGER, order_quantity INTEGER, order_discount INTEGER, total INTEGER, order_date DATE,  item_id INTEGER REFERENCES items(id))")
#cursor.execute("ALTER TABLE orders ADD COLUMN total INTEGER")
#cursor.execute("ALTER TABLE orders MODIFY COLUMN total INTEGER AFTER item_id")
conn.commit()
# Creating Table for stock history
cursor.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, item_id INTEGER REFERENCES items(id), productname TEXT, date DATE, stock_change INTEGER, current_stock INTEGER)")
conn.commit()

# Login
class Login(QDialog):
    login_success = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login_Dialog()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.loginfunction)
        self.ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.ui.signin_btn.clicked.connect(self.gotocreate)
        self.login_success.connect(self.accept)
    def loginfunction(self):
        username=self.ui.username_lineEdit.text()
        password=self.ui.password_lineEdit.text()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result:
            print("Successfully logged in with username: ", username, "and password:", password)
            self.login_success.emit()
            print("accepting input and closing dialog...")
        elif not all([username, password]):
            QMessageBox.warning(self, 'Error', 'Please fill in all fields.')
        else:
            print("Incorrect username or password") 
            QMessageBox.warning(self, 'Error', 'Incorrect username or password.')
        
class AddDialog(QDialog):
        itemAdded = Signal()
        def __init__(self, parent=None):
            super(AddDialog, self).__init__(parent)
            # Create and show dialog
            self.ui = Ui_Add_Dialog()
            self.ui.setupUi(self)

            # Connect the button to the slot
            self.ui.add_btn.clicked.connect(self.addData)
        def addData(self):
            # Line Edits
            product_name = self.ui.product_name_lineEdit.text()
            category = self.ui.category_lineEdit.text()
            quantity_str = self.ui.quantity_lineEdit.text()
            price_str = self.ui.price_lineEdit.text()
            # Try to convert quantity and price to integers

            #quantity = int(self.ui.quantity_lineEdit.text())
            #price = self.ui.price_lineEdit.text()
            date = datetime.now().strftime('%Y-%m-%d') 

            # Add the data to the table
            if not all([product_name, category, quantity_str, price_str]):
                QMessageBox.warning(self, 'Error', 'Please fill in all fields.')

                return
            
            
            if not quantity_str.isdigit() and not price_str.isdigit():
                QMessageBox.warning(self, 'Error', 'Price and Quantity must be numeric.')
                self.ui.price_lineEdit.clear()
                self.ui.quantity_lineEdit.clear()
            elif not quantity_str.isdigit():
                QMessageBox.warning(self, 'Error', 'Quantity must be numeric.')
                self.ui.quantity_lineEdit.clear()
            elif not price_str.isdigit():
                QMessageBox.warning(self, 'Error', 'Price must be numeric.')
                self.ui.price_lineEdit.clear()

            else:
                quantity = int(quantity_str)
                price = int(price_str)
                cursor.execute("SELECT * FROM items WHERE productname = ?",(product_name,))
                if cursor.fetchone() is not None:
                    # If the item exists, show a QMessageBox
                    QMessageBox.warning(self, 'Error', f'Item {product_name} already exist.')
                else:
                    cursor.execute(f"INSERT INTO items (productname, category, quantity, price, date) VALUES (?, ?, ?, ?, ?)", (product_name, category, quantity, price, date))
                    conn.commit()
                    print("Successfully created items: ", product_name, category, quantity, price, date)

                    self.itemAdded.emit()
                    self.close()

class EditDialog(QDialog):
    item_edited = Signal()
    def __init__(self, parent=None, row_data=None):
        super(EditDialog, self).__init__(parent)
        self.ui = Ui_Edit_Dialog()
        self.ui.setupUi(self)

        self.row_data = row_data
        


        if row_data is not None:
            #self.ui.item_id_lineEdit.setText(str(row_data[1]))
            self.ui.product_name_lineEdit.setText(row_data[2])
            self.ui.category_lineEdit.setText(row_data[3])
            self.ui.quantity_lineEdit.setText(row_data[4])
            self.ui.price_lineEdit.setText(row_data[5])


        self.ui.save_btn.clicked.connect(self.save_changes)
        self.ui.cancel_btn.clicked.connect(self.reject)
        

    def save_changes(self):
        #item_id = self.ui.item_id_lineEdit.text()
        product_name = self.ui.product_name_lineEdit.text()
        category = self.ui.category_lineEdit.text()
        quantity_str = self.ui.quantity_lineEdit.text()
        price_str = self.ui.price_lineEdit.text()
        if not all([product_name, category, quantity_str, price_str]):
            QMessageBox.warning(self, 'Error', 'Please fill in all fields.')
            return
        if not quantity_str.isdigit() and not price_str.isdigit():
            QMessageBox.warning(self, 'Error', 'Price and Quantity must be numeric.')
            self.ui.price_lineEdit.clear()
            self.ui.quantity_lineEdit.clear()
        elif not quantity_str.isdigit():
            QMessageBox.warning(self, 'Error', 'Quantity must be numeric.')
            self.ui.quantity_lineEdit.clear()
        elif not price_str.isdigit():
            QMessageBox.warning(self, 'Error', 'Price must be numeric.')
            self.ui.price_lineEdit.clear()
        else: 
            quantity = int(quantity_str)
            price = int(price_str)
            #date = datetime.now().strftime('%Y-%m-%d')

            id = self.row_data[1]
            query = "UPDATE items SET productname = ?, category = ?, quantity = ?, price = ? WHERE id = ?"
            cursor.execute(query, (product_name, category, quantity, price, id))
            conn.commit()
            
            

            self.item_edited.emit()
            self.accept()

class OrderDialog(QDialog):
    itemAdded = Signal()
    def __init__(self, parent=None):
        super(OrderDialog, self).__init__(parent)
        # Create and show dialog
        self.ui = Ui_Order_Dialog()
        self.ui.setupUi(self)

        # Connect the button to the slot
        self.ui.add_btn.clicked.connect(self.addData)
        self.ui.cancel_btn.clicked.connect(self.reject)
            
        cursor.execute("SELECT productname FROM items")
        results = cursor.fetchall()

        for row in results:
            self.ui.product_dropdown.addItem(row[0])
            
        self.ui.quantity_SpinBox.textChanged.connect(self.on_quantity_changed)
        self.ui.discount_lineEdit.textChanged.connect(self.on_quantity_changed)
        self.ui.product_dropdown.currentIndexChanged.connect(self.reset_quantity_spinbox)
        self.ui.discount_lineEdit.text()
        
        def on_combo_box_current_text_changed(text):
            cursor.execute(f"SELECT category, price, quantity FROM items WHERE productname='{text}'")
            data = cursor.fetchone()

            if data is not None:
                self.ui.category_lineEdit.setText(str(data[0]))
                check_quantity = int(data[2])
                #quantity = self.ui.quantity_SpinBox.text()
                
                price = int(data[1])
                self.ui.price_lineEdit.setText(str(price))
                price_text = str(data[1])
                check_quantity = int(data[2])

                # Set the minimum, maximum, and single step values for the quantity spin box
                self.ui.quantity_SpinBox.setMinimum(1)
                self.ui.quantity_SpinBox.setMaximum(check_quantity)
                self.ui.quantity_SpinBox.setSingleStep(1)

                # Check if the item is out of stock
                if check_quantity <= 0:
                    QMessageBox.warning(self, 'Out of Stock', 'Selected item is currently out of stock.')
                    self.ui.product_dropdown.setCurrentIndex(0)
                    self.ui.quantity_SpinBox.setEnabled(False)
                    return
                self.ui.quantity_SpinBox.setEnabled(True)
                if price_text:
                    price = int(price_text)
                else:
                    price = 0

            self.calculate_total()
            
        self.ui.product_dropdown.currentTextChanged.connect(on_combo_box_current_text_changed)
    def reset_quantity_spinbox(self):
            self.ui.quantity_SpinBox.setValue(1)
    def addData(self):
        # Line Edits
        product_name = self.ui.product_dropdown.currentText()
            
        # Query items table for item_id
        cursor.execute("SELECT id FROM items WHERE productname=?", (product_name,))
        result = cursor.fetchone()
        if result is None:
            QMessageBox.warning(self, 'Error', 'Selected product name not found in items table.')
            return
        item_id = result[0]
            
        # Get the quantity of the current item
        cursor.execute(f"SELECT quantity FROM items WHERE productname='{product_name}'")
        current_stock = cursor.fetchone()[0]

        category = self.ui.category_lineEdit.text()
        quantity = int(self.ui.quantity_SpinBox.text())
        price = self.ui.price_lineEdit.text()
        try:
            discount = int(self.ui.discount_lineEdit.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Discount must be a numeric value.")
            self.ui.discount_lineEdit.clear()

        #discount = int(self.ui.discount_lineEdit.text())
        total = self.ui.total_lineEdit.text()
        date = datetime.now().strftime('%Y-%m-%d')

        # Add the data to the table
        if not all([product_name, category, quantity, price]):
            QMessageBox.warning(self, 'Error', 'Please fill in all fields.')
            return
        else:
            cursor.execute(f"INSERT INTO orders (order_productname, order_category, order_quantity, order_price, order_discount, order_date, total, item_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (product_name, category, quantity, price, discount, date, total, item_id))
            conn.commit()
            print("Successfully Inserted items: ", product_name, category, quantity, price, discount, date, total, item_id)
                
            # Assigning new variable for quantity
            order_quantity = quantity
            print("Ordered Quantity: ",order_quantity)
            # Update the stock in the item stocks table
            new_stock = current_stock - order_quantity
            print("Updated Stock: ",new_stock)
            cursor.execute(f"UPDATE items SET quantity={new_stock} WHERE productname='{product_name}'")
            conn.commit()
                
            # Making the order_quantity to a negative value
            order_quantity = - order_quantity
            cursor.execute(f"INSERT INTO history (item_id, productname, date, stock_change, current_stock) VALUES (?, ?, ?, ?, ?)", (item_id, product_name, date,  order_quantity, new_stock))
            conn.commit()

            # Trigger the signal
            self.itemAdded.emit()
            self.close()
    def on_quantity_changed(self):
        self.calculate_total()
    def calculate_total(self):
        quantity_text = self.ui.quantity_SpinBox.text()
        
        if quantity_text:
            quantity = int(quantity_text)
        else:
            quantity = 0
        price_text = self.ui.price_lineEdit.text()
        if price_text:
            price = int(price_text)
        else:
            price = 0
        discount_text = self.ui.discount_lineEdit.text()
        amount = quantity * price
        max_discount = int(amount)
        discount = 0
        if discount_text:
            discount = int(discount_text)
            if discount > max_discount:
                QMessageBox.warning(self, "Warning", "Discount value is invalid")
                discount = 0
                self.ui.discount_lineEdit.setText(str(discount))
        else:
            discount = 0
        total = amount - discount
        self.ui.total_lineEdit.setText(str(total))
class AddStockDialog(QDialog):
    itemAdded = Signal()
    def __init__(self, parent=None, row_data=None):
        super(AddStockDialog, self).__init__(parent)
        # Create and show dialog
        self.ui = Ui_AddStock_Dialog()
        self.ui.setupUi(self)

        self.row_data = row_data
        if row_data is not None:
            self.ui.productname_lineEdit.setText(str(row_data[2]))
            self.ui.productname_lineEdit.setEnabled(False)
        self.ui.save_btn.clicked.connect(self.add_stock)
        self.ui.cancel_btn.clicked.connect(self.reject)
    def add_stock(self):
        # Get the stock quantity from the line edit
        try:
            added_quantity = int(self.ui.newquantity_lineEdit.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Quantity must be a numeric value.")
            self.ui.newquantity_lineEdit.clear()
        
        date = datetime.now().strftime('%Y-%m-%d') 
        # Get the row index from the row data
        productname = (self.row_data[2])
        self.accept()

        # Query items table for item_id
        cursor.execute("SELECT id FROM items WHERE productname=?", (productname,))
        result = cursor.fetchone()
        if result is None:
            QMessageBox.warning(self, 'Error', 'Selected product name not found in items table.')
            return
        item_id = result[0]
        
        cursor.execute("SELECT quantity FROM items WHERE productname = ?", (productname,))
        result = cursor.fetchone()
        if result is None:
            # Handle the case where the id value is not found
            print("Error: id value not found")
        else:
            quantity = result[0]
            # Do something with the quantity value
            new_quantity = quantity + added_quantity
            query = "UPDATE items SET quantity = ? WHERE productname = ?"
            cursor.execute(query, (new_quantity, productname))
            cursor.execute("INSERT INTO history (item_id, productname, date, stock_change, current_stock) VALUES (?, ?, ?, ?, ?)", (item_id, productname, date,  added_quantity, new_quantity))
            conn.commit()

        self.itemAdded.emit()
        self.accept()

class TodayDateEdit(QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.calendar_widget = self.findChild(QCalendarWidget)
        self.today_button = QToolButton(self.calendar_widget)
        self.today_button.setText("Today")
        self.today_button.clicked.connect(self.set_today_date)
        layout = QVBoxLayout(self.calendar_widget)
        layout.addWidget(self.today_button)

    def set_today_date(self):
        today = QDate.currentDate()
        self.setDate(today)
        self.hideCalendarWidget()

class MainWindow(QMainWindow):
    checkbox_states = {}
    def __init__(self): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        login = Login()
        login.close()

        # Side Bar Menu
        self.menu_button()
        # Load All Data
        self.load_allData()
        # Table Modifications
        self.tables()
        # Search Functions
        self.search_functions()
        # CRUD Functions
        self.crud_functions()
        # Dashboard Menu
        self.dashboard_menu()
        self.ui.tableWidget.cellClicked.connect(self.toggle_checkbox)
        self.ui.stackedWidget.currentChanged.connect(self.refresh_table)
        self.ui.stackedWidget.currentChanged.connect(self.update_low_stock_items)
        self.ui.stackedWidget.currentChanged.connect(self.refresh_table_3)
    def load_allData(self):
        # Load the data in the table
        self.loadData()
        self.loadData_2()
        self.loadData_3()
        self.loadData_4()
    def search_functions(self):    
        # Connect Search Function
        self.ui.search_lineEdit_2.textChanged.connect(self.search_function_2)
        self.ui.search_lineEdit_3.textChanged.connect(self.search_function_3)
        self.ui.dateEdit.dateChanged.connect(self.search_by_date_function)
        self.ui.dateEdit_2.dateChanged.connect(self.search_by_date_function)
    def crud_functions(self):
        # Connect Delete Function
        self.ui.delete_btn.clicked.connect(self.delete_function)
        # Connect Open AddDialog
        self.ui.openAddDialog_btn.clicked.connect(self.open_addDialog)
        # Connect Open EditDialog
        self.ui.edit_btn.clicked.connect(self.open_editDialog)
        # Connect Open OrderDialog
        self.ui.openOrderDialog_btn.clicked.connect(self.open_orderDialog)
        # Connect Open AddStockDialog
        self.ui.openAddStock_btn.clicked.connect(self.open_addStockDialog)

        self.ui.logout_btn.clicked.connect(self.logout_function)
        self.ui.clear_btn.clicked.connect(self.clear_date_function)
        self.ui.today_btn.clicked.connect(self.todays_date_function)
        self.ui.stackedWidget.currentChanged.connect(self.on_page_changed)
    def dashboard_menu(self):
        self.sales_overview_Dashboard()
        self.inventory_overview_Dashboard()
        self.inventory_summary_Dashboard()
        self.product_details_Dashboard()
        #self.low_stock_items()
        self.update_low_stock_items()
        self.setup_graph()
    def tables(self):
        # Set section resize mode for each column to Stretchs
        header = self.ui.tableWidget.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Resize columns to fit their contents
        self.ui.tableWidget.resizeColumnsToContents()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header = self.ui.tableWidget.horizontalHeader()
        for i in range(1, header.count()):                                                  
            header.setSectionResizeMode(i, QHeaderView.Stretch) 
            

        # Resize columns to fit their contents  
        self.ui.tableWidget.resizeColumnsToContents()

        header = self.ui.tableWidget_2.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Resize columns to fit their contents
        self.ui.tableWidget_2.resizeColumnsToContents()

        header = self.ui.tableWidget_3.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for i in range(1, header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Resize columns to fit their contents
        self.ui.tableWidget_3.resizeColumnsToContents()

        header = self.ui.tableWidget_4.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for i in range(1, header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        # Resize columns to fit their contents
        self.ui.tableWidget_4.resizeColumnsToContents()
        self.show()

        #self.ui.tableWidget.itemClicked.connect(self.onTableItemClicked)
        #self.ui.tableWidget_4.itemClicked.connect(self.onTableItemClicked4)
    def menu_button(self):
        # Connect menu buttons to their respective pages
        self.ui.btn_menu_1.clicked.connect(lambda: self.show_page(self.ui.page_1, self.ui.btn_menu_1))
        self.ui.btn_menu_2.clicked.connect(lambda: self.show_page(self.ui.page_2, self.ui.btn_menu_2))
        self.ui.btn_menu_3.clicked.connect(lambda: self.show_page(self.ui.page_3, self.ui.btn_menu_3))
        self.ui.btn_menu_4.clicked.connect(lambda: self.show_page(self.ui.page_4, self.ui.btn_menu_4))
        #self.ui.btn_menu_5.clicked.connect(lambda: self.show_page(self.ui.page_5, self.ui.btn_menu_5))

        # Set the initial selected button and page
        self.selected_button = self.ui.btn_menu_1
        self.selected_page = self.ui.page_1

        # Highlight the initial selected button
        self.show_page(self.ui.page_1, self.ui.btn_menu_1)
    def setup_graph(self):
        # Adding drop down function for line graph
        self.ui.month_dropdown.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        self.ui.year_dropdown.addItems(['2020','2021','2022','2023'])
        self.ui.month_dropdown.currentIndexChanged.connect(self.update_graph)
        self.ui.year_dropdown.currentIndexChanged.connect(self.update_graph)

        # Set the default selection to the current month and year
        self.ui.month_dropdown.setCurrentIndex(datetime.now().month-1)  
        self.ui.year_dropdown.setCurrentText(str(datetime.now().year))

        # Set up the line graph
        selected_month = self.ui.month_dropdown.currentText()
        selected_year = self.ui.year_dropdown.currentText()

        # Convert the selected month to a two-digit number
        month_number = datetime.strptime(selected_month, '%B').month
        selected_month = f"{month_number:02d}"

        # Combine the selected month and year into a string that matches the format of the order_date column
        date_str = f"{selected_year}-{selected_month}-__"

        # Set up the line graph
        cursor.execute(f"SELECT order_date, order_quantity FROM orders WHERE order_date LIKE '{date_str}'")
        rows = cursor.fetchall()

        # Convert data to a list of tuples
        data = {}
        for row in rows:
            date_str, quantity = row
            date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%b %d') 
            data[date] = data.get(date, 0) + quantity

        # Convert data to lists
        dates = list(data.keys())
        quantities = list(data.values())

        frame = self.findChild(QWidget, 'graph_frame_2')
            
        # Set up the line graph
        self.fig = plt.figure(figsize=(8.5, 3.25))
        self.ax = self.fig.add_subplot(111)
       
        self.ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
        self.ax.plot(dates, quantities, marker='o', color='black')
        self.ax.set_frame_on(False)
        self.ax.fill_between(dates, quantities, 0, color='black', alpha=0.1)
            
        # Create a QGraphicsView to hold the FigureCanvas
        view = QGraphicsView(frame)
        view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #view.setAlignment(Qt.AlignCenter)
            
        scene = QGraphicsScene(view)
        # Add the FigureCanvas to the QGraphicsView
        canvas = FigureCanvas(self.fig)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
        scene.addWidget(canvas)
        view.setScene(scene)

        # Add the QGraphicsView to the layout of the frame
        layout = QGridLayout(frame)
        layout.addWidget(view) # row 0, column 0, row span 1, column span 1)
        frame.setLayout(layout)
    def update_graph(self):
        self.ui.month_dropdown.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        self.ui.year_dropdown.addItems(['2020','2021','2022','2023'])
        # Get the selected month and year
        selected_month = self.ui.month_dropdown.currentText()
        selected_year = self.ui.year_dropdown.currentText()

        # Convert the selected month to a two-digit number
        month_number = datetime.strptime(selected_month, '%B').month
        selected_month = f"{month_number:02d}"

        # Combine the selected month and year into a string that matches the format of the order_date column
        date_str = f"{selected_year}-{selected_month}-__"

        # Set up the line graph
        cursor.execute(f"SELECT order_date, order_quantity FROM orders WHERE order_date LIKE '{date_str}'")
        rows = cursor.fetchall()
            
        # Convert data to a list of tuples
        data = {}
        for row in rows:
            date_str, quantity = row
            date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%b %d')
            data[date] = data.get(date, 0) + quantity

        # Convert data to lists
        dates = list(data.keys())
        quantities = list(data.values())
        
        self.ax.clear()
        self.ax.plot(dates, quantities, marker='o', color='black')
        self.ax.set_frame_on(False)
        self.ax.fill_between(dates, quantities, 0, color='black', alpha=0.1)
        
        self.fig.canvas.draw()
    def show_page(self, page, button):
        # Change the current page
        self.ui.stackedWidget.setCurrentWidget(page)

        # Highlight the selected button
        self.selected_button.setStyleSheet("QPushButton {border: none;color: black; border-radius: 10px; text-align: left; padding-left: 20px;}"
        "QPushButton:hover {background-color: #f4f4f4;}")
        button.setStyleSheet("background-color: #ffffff; border: 1px solid #ebebea;color: black; border-radius: 10px; text-align: left; padding-left: 20px;")
        self.selected_button = button
        self.selected_page = page

        #self.ui.month_dropdown.setStyleSheet("QPushButton:hover {border: 1px solid black;}")

    def on_page_changed(self, index):
        if index == self.ui.stackedWidget.indexOf(self.ui.page_1):
            # Call todaysales_Dashboard to update the label
            self.sales_overview_Dashboard()
            self.inventory_overview_Dashboard()
            self.inventory_summary_Dashboard()
            self.product_details_Dashboard()
            self.update_graph()
            self.update_low_stock_items()

    def addCheckBox(self, row):
        # Add Checkbox to Table 1
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox = QTableWidgetItem()
            checkbox.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox.setCheckState(Qt.Unchecked)
            self.ui.tableWidget.setItem(row, 0, checkbox)
            self.ui.tableWidget.item(row, 0).setCheckState(Qt.Unchecked)

        self.ui.tableWidget.setColumnWidth(0, 0)
        # Make the first column clickable
        self.ui.tableWidget.horizontalHeaderItem(0).setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.ui.tableWidget.horizontalHeaderItem(0).setCheckState(Qt.Unchecked)
    def toggle_checkbox(self, row):
        # Get the checkbox item at the clicked row
        checkbox_item = self.ui.tableWidget.item(row, 0)
        
        # Toggle the checkbox state
        if checkbox_item.checkState() == Qt.Checked:
            checkbox_item.setCheckState(Qt.Unchecked)
        else:
            checkbox_item.setCheckState(Qt.Checked)
    def addCheckBoxTable4(self, row):
        # Add Checkbox to Table 4
        for row in range(self.ui.tableWidget_4.rowCount()):
            checkbox = QTableWidgetItem()
            checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            checkbox.setCheckState(Qt.CheckState.Unchecked)
            self.ui.tableWidget_4.setItem(row, 0, checkbox)
            self.ui.tableWidget_4.setColumnWidth(0, 0)
        # Connect the cellClicked signal of the table to a slot that checks the corresponding checkbox
        #self.ui.tableWidget_4.cellClicked.connect(self.checkCheckboxTable4)
        # Hide the first column
        #self.ui.tableWidget_4.setColumnWidth(0, 0)
    
    # Open Add Dialog
    def open_addDialog(self):
        # Create and show the dialog
        dialog = AddDialog(self)
        dialog.itemAdded.connect(self.refresh_table)
        dialog.exec()
    # Open Edit Dialog
    def open_editDialog(self):
        rows = []
        for i in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.item(i, 0).checkState() == Qt.Checked:
                rows.append(i)

        if len(rows) == 0:
            QMessageBox.warning(self, "Warning", "Please select at least one item to edit.")
            return
        if len(rows) > 1:
            QMessageBox.warning(self, "Warning", "Please select only one item to edit.")
            return
        row = rows[0]

        # get row data
        row_data = []
        for i in range(self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row, i)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append('')  

        dialog = EditDialog(self, row_data=row_data)
        dialog.item_edited.connect(self.refresh_table)
        dialog.exec()


    def open_orderDialog(self):
        # Create and show the dialog
        dialog = OrderDialog(self)
        dialog.itemAdded.connect(self.refresh_table_2)
        dialog.exec()

    def open_addStockDialog(self):
        rows = []
        for i in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.item(i, 0).checkState() == Qt.Checked:
                rows.append(i)
        if len(rows) == 0:
            QMessageBox.warning(self, "Warning", "Please select at least one item to add a stock.")
            return
        if len(rows) > 1:
            QMessageBox.warning(self, "Warning", "Please select only one item to add a stock.")
            return
        row = rows[0]

        # get row data
        row_data = []
        for i in range(self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row, i)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append('')
    
        dialog = AddStockDialog(self, row_data=row_data)
        dialog.itemAdded.connect(self.refresh_table)
        dialog.exec()

        
    # Refresh the table when user add a record
    def refresh_table(self):
        self.loadData()
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox = QTableWidgetItem()
            checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            checkbox.setCheckState(Qt.CheckState.Unchecked)
            checkbox.setText("")
            self.ui.tableWidget.setItem(row, 0, checkbox)
    def refresh_table_2(self):
        self.loadData_2()
    
    def refresh_table_3(self):
        self.loadData_3()

    def refresh_table_4(self):
        self.loadData_4()
        for row in range(self.ui.tableWidget_4.rowCount()):
            checkbox = QTableWidgetItem()
            checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            checkbox.setCheckState(Qt.CheckState.Unchecked)
            checkbox.setText("")
            self.ui.tableWidget_4.setItem(row, 0, checkbox)

    def search_function(self):
        #self.ui.tableWidget.cellClicked.connect(self.checkCheckbox)
        search_term = self.ui.search_lineEdit.text()
        if not search_term:
            self.loadData()
            return

        # Query the database for rows matching the search term
        cursor.execute(f"SELECT * FROM items WHERE productname LIKE '%{search_term}%' OR category LIKE '%{search_term}%' ORDER BY id DESC;")
        rows = cursor.fetchall()
        self.loadData(rows)
    def search_function_2(self):
        search_term_2 = self.ui.search_lineEdit_2.text()
        if not search_term_2:
            self.loadData_2()
            return

        # Query the database for rows matching the search term
        cursor.execute(f"SELECT * FROM orders WHERE order_productname LIKE '%{search_term_2}%' OR order_category LIKE '%{search_term_2}%' ORDER BY order_id DESC;")
        rows = cursor.fetchall()

        self.loadData_2(rows)
    def search_function_3(self): 
        search_term_3 = self.ui.search_lineEdit_3.text()
        if not search_term_3:
            self.loadData_3()
            return

        # Query the database for rows matching the search term
        cursor.execute(f"SELECT * FROM history WHERE productname LIKE '%{search_term_3}%' ORDER BY id DESC;")
        rows = cursor.fetchall()

        self.loadData_3(rows)
    def search_function_4(self):
        self.ui.tableWidget_4.cellClicked.connect(self.checkCheckboxTable4)
        search_term_4 = self.ui.search_lineEdit_4.text()
        if not search_term_4:
            self.loadData_4()
            return

        # Query the database for rows matching the search term
        cursor.execute(f"SELECT * FROM items WHERE productname LIKE '%{search_term_4}%' OR category LIKE '%{search_term_4}%' ORDER BY id DESC;")
        rows = cursor.fetchall()
        self.loadData_4(rows)
    def search_by_date_function(self):
        selected_date = self.ui.dateEdit.date()
        end_date = self.ui.dateEdit_2.date()

        date_str = selected_date.toString(Qt.ISODate)
        end_date_str = end_date.toString(Qt.ISODate)

        cursor.execute("SELECT * FROM history WHERE date BETWEEN ? AND ? ORDER BY id DESC;", (date_str, end_date_str))
        rows = cursor.fetchall()

        self.loadData_3(rows)

    def clear_date_function(self):
        default_date = QDate(2023, 1, 1)
        self.ui.dateEdit.setDate(default_date)
        self.ui.dateEdit_2.setDate(default_date)

        # query the database for all rows
        cursor.execute("SELECT * FROM history ORDER BY id DESC;")
        rows = cursor.fetchall()

        # load the r    esults into the table
        self.loadData_3(rows)
    def todays_date_function(self):
        self.ui.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateEdit_2.setDateTime(QDateTime.currentDateTime())
    def delete_function(self):
        # Get the selected rows
        selected_rows = []
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox = self.ui.tableWidget.item(row, 0)
            if checkbox.checkState() == Qt.Checked:
                selected_rows.append(row)
        if len(selected_rows) == 0:
            QMessageBox.warning(self, "Warning", "Please select at least one item to delete.")
            return
        # Delete the selected rows from the table widget and the database
        elif selected_rows:
            reply = QMessageBox.question(self, 'Delete Rows', 'Are you sure you want to delete the selected rows?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                connection = sqlite3.connect("DBMS.db")
                cursor = connection.cursor()
                for row in reversed(selected_rows):
                    id = int(self.ui.tableWidget.item(row, 1).text())
                    cursor.execute("DELETE FROM items WHERE id=?", (id,))
                    self.ui.tableWidget.removeRow(row)
                connection.commit()
                connection.close()
    def low_stock_items(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            low_inventory_threshold = 2
            query = f"SELECT productname, quantity FROM items WHERE quantity <= {low_inventory_threshold} ORDER BY quantity ASC LIMIT 2;"
            cursor.execute(query)
                
            # fetch result and update label
            low_stock_items = cursor.fetchall()

            # Low Stock Items (5)
            if len(low_stock_items) == 0:
                self.clear_line_edits()
            elif len(low_stock_items) >= 1:
                self.ui.itemname_1.setText(f"{low_stock_items[0][0]}")
                self.ui.item1_stock.setText(f"{low_stock_items[0][1]}")
            elif len(low_stock_items) >= 2:
                self.ui.itemname_2.setText(f"{low_stock_items[1][0]}")
                self.ui.item2_stock.setText(f"{low_stock_items[1][1]}")
            elif len(low_stock_items) >= 3:
                self.ui.itemname_3.setText(f"{low_stock_items[2][0]}")
                self.ui.item3_stock.setText(f"{low_stock_items[2][1]}")
            elif len(low_stock_items) >= 4:
                self.ui.itemname_4.setText(f"{low_stock_items[3][0]}")
                self.ui.item4_stock.setText(f"{low_stock_items[3][1]}")
            elif len(low_stock_items) >= 5:
                self.ui.itemname_5.setText(f"{low_stock_items[4][0]}")
                self.ui.item5_stock.setText(f"{low_stock_items[4][1]}")
    def update_low_stock_items(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            low_inventory_threshold = 2
            query = f"SELECT productname, quantity FROM items WHERE quantity <= {low_inventory_threshold} ORDER BY quantity ASC LIMIT 5;"
            cursor.execute(query)

            # fetch result and update label
            low_stock_items = cursor.fetchall()

            # Clear all line edits displaying low stock items
            self.ui.itemname_1.clear()
            self.ui.item1_stock.clear()
            self.ui.itemname_2.clear()
            self.ui.item2_stock.clear()
            self.ui.itemname_3.clear()
            self.ui.item3_stock.clear()
            self.ui.itemname_4.clear()
            self.ui.item4_stock.clear()
            self.ui.itemname_5.clear()
            self.ui.item5_stock.clear()

            # Refresh line edits with latest low stock items
            if len(low_stock_items) >= 1:
                self.ui.itemname_1.setText(f"{low_stock_items[0][0]}")
                self.ui.item1_stock.setText(f"{low_stock_items[0][1]}")
            if len(low_stock_items) >= 2:
                self.ui.itemname_2.setText(f"{low_stock_items[1][0]}")
                self.ui.item2_stock.setText(f"{low_stock_items[1][1]}")
            if len(low_stock_items) >= 3:
                self.ui.itemname_3.setText(f"{low_stock_items[2][0]}")
                self.ui.item3_stock.setText(f"{low_stock_items[2][1]}")
            if len(low_stock_items) >= 4:
                self.ui.itemname_4.setText(f"{low_stock_items[3][0]}")
                self.ui.item4_stock.setText(f"{low_stock_items[3][1]}")
            if len(low_stock_items) >= 5:
                self.ui.itemname_5.setText(f"{low_stock_items[4][0]}")
                self.ui.item5_stock.setText(f"{low_stock_items[4][1]}")            
    def sales_overview_Dashboard(self):
        # Check if the current page is the dashboard page
        # Today Sales
        if self.ui.stackedWidget.currentIndex() == 0:
            # Get the sales for today from the database
            today = datetime.now().strftime('%Y-%m-%d')
            query = f"SELECT total FROM orders WHERE order_date = '{today}'"
            cursor.execute(query)
            rows = cursor.fetchall()  

            todaysales = sum([row[0] for row in rows])

            self.ui.todaysales_label.setText(f'{todaysales}')

            # Sales in Month
            self.ui.month_dropdown.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
            self.ui.year_dropdown.addItems(['2020','2021','2022','2023'])

            self.ui.month_dropdown.currentIndexChanged.connect(self.update_sales_overview)
            self.ui.year_dropdown.currentIndexChanged.connect(self.update_sales_overview)
            # Set the default selection to the current month and year
            self.ui.month_dropdown.setCurrentIndex(datetime.now().month-1)  
            self.ui.year_dropdown.setCurrentText(str(datetime.now().year))

            selected_month = self.ui.month_dropdown.currentText()
            selected_year = self.ui.year_dropdown.currentText()

            # Convert the selected month to a two-digit number
            month_number = datetime.strptime(selected_month, '%B').month
            selected_month = f"{month_number:02d}"

            # Combine the selected month and year into a string that matches the format of the order_date column
            date_str = f"{selected_year}-{selected_month}-__"

            query = f"SELECT SUM(total) FROM orders WHERE order_date LIKE '{date_str}'"
            cursor.execute(query)
            total_sales = cursor.fetchone()[0]
            self.ui.totalsales_label.setText(f'{total_sales}')
    def update_sales_overview(self):
        # Check if the current page is the dashboard page
        # Update Sales overview
        if self.ui.stackedWidget.currentIndex() == 0:
            # Get the sales for today from the database
            today = datetime.now().strftime('%Y-%m-%d')
            query = f"SELECT total FROM orders WHERE order_date = '{today}'"
            cursor.execute(query)
            rows = cursor.fetchall()  

            todaysales = sum([row[0] for row in rows])

            self.ui.todaysales_label.setText(f'{todaysales}')

            # Sales in Month
            self.ui.month_dropdown.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
            self.ui.year_dropdown.addItems(['2020','2021','2022','2023'])

            selected_month = self.ui.month_dropdown.currentText()
            selected_year = self.ui.year_dropdown.currentText()

            # Convert the selected month to a two-digit number
            month_number = datetime.strptime(selected_month, '%B').month
            selected_month = f"{month_number:02d}"

            # Combine the selected month and year into a string that matches the format of the order_date column
            date_str = f"{selected_year}-{selected_month}-__"

            query = f"SELECT SUM(total) FROM orders WHERE order_date LIKE '{date_str}'"
            cursor.execute(query)
            total_sales = cursor.fetchone()[0]
            self.ui.totalsales_label.setText(f'{total_sales}')
    def inventory_overview_Dashboard(self):
        # Sold Stocks Today
        if self.ui.stackedWidget.currentIndex() == 0:
            today = datetime.now().strftime('%Y-%m-%d')
            query = f"SELECT order_quantity FROM orders WHERE order_date = '{today}'"
            cursor.execute(query)
            rows = cursor.fetchall() 

            soldstock = sum([row[0] for row in rows])

            self.ui.soldstockstoday_label.setText(f'{soldstock}')
            
            # Sales in Month
            self.ui.month_dropdown.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
            self.ui.year_dropdown.addItems(['2020','2021','2022','2023'])

            self.ui.month_dropdown.currentIndexChanged.connect(self.update_inventory_overview)
            self.ui.year_dropdown.currentIndexChanged.connect(self.update_inventory_overview)
            # Set the default selection to the current month and year
            self.ui.month_dropdown.setCurrentIndex(datetime.now().month-1)  
            self.ui.year_dropdown.setCurrentText(str(datetime.now().year))

            selected_month = self.ui.month_dropdown.currentText()
            selected_year = self.ui.year_dropdown.currentText()

            # Convert the selected month to a two-digit number
            month_number = datetime.strptime(selected_month, '%B').month
            selected_month = f"{month_number:02d}"

            # Combine the selected month and year into a string that matches the format of the order_date column
            date_str = f"{selected_year}-{selected_month}-__"

            query = f"SELECT SUM(order_quantity) FROM orders WHERE order_date LIKE '{date_str}'"
            cursor.execute(query)
            totalsold_stocks = cursor.fetchone()[0]
            self.ui.totalsoldstocks_label.setText(f'{totalsold_stocks}')
    def update_inventory_overview(self):
        # Sold Stocks Today
        if self.ui.stackedWidget.currentIndex() == 0:
            today = datetime.now().strftime('%Y-%m-%d')
            query = f"SELECT order_quantity FROM orders WHERE order_date = '{today}'"
            cursor.execute(query)
            rows = cursor.fetchall() 

            soldstock = sum([row[0] for row in rows])

            self.ui.soldstockstoday_label.setText(f'{soldstock}')
            
            # Sales in Month
            self.ui.month_dropdown.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
            self.ui.year_dropdown.addItems(['2020','2021','2022','2023'])

            selected_month = self.ui.month_dropdown.currentText()
            selected_year = self.ui.year_dropdown.currentText()

            # Convert the selected month to a two-digit number
            month_number = datetime.strptime(selected_month, '%B').month
            selected_month = f"{month_number:02d}"

            # Combine the selected month and year into a string that matches the format of the order_date column
            date_str = f"{selected_year}-{selected_month}-__"

            query = f"SELECT SUM(order_quantity) FROM orders WHERE order_date LIKE '{date_str}'"
            cursor.execute(query)
            totalsold_stocks = cursor.fetchone()[0]
            self.ui.totalsoldstocks_label.setText(f'{totalsold_stocks}')
    def inventory_summary_Dashboard(self):
        # Total Stocks
        if self.ui.stackedWidget.currentIndex() == 0:
            query = f"SELECT SUM(quantity) FROM items"
            cursor.execute(query)
            total_stocks = cursor.fetchone()[0]
            self.ui.totalstocks_label_2.setText(f'{total_stocks}')

            query = f"SELECT SUM(stock_change) FROM history WHERE stock_change > 0;"
            cursor.execute(query)
            rows = cursor.fetchone()[0]
            self.ui.stockreceived_label.setText(f'{rows}')
    def product_details_Dashboard(self):

        if self.ui.stackedWidget.currentIndex() == 0:
            query = f"SELECT COUNT(productname) FROM items"
            cursor.execute(query)
            no_items = cursor.fetchone()[0]

            self.ui.no_items_label_2.setText(f'{no_items}')

        #if self.ui.stackedWidget.currentIndex() == 0:
            low_inventory_threshold = 2
            query = f"SELECT COUNT(*) FROM items WHERE quantity <= {low_inventory_threshold}"
            cursor.execute(query)

            # fetch result and update label
            num_low_inventory_items = cursor.fetchone()[0]
            self.ui.lowstockitems_label_2.setText(f"{num_low_inventory_items}")

        #if self.ui.stackedWidget.currentIndex() == 0:
            cursor.execute("SELECT COUNT(DISTINCT category) FROM items")
            no_category = cursor.fetchone()[0]
            
            self.ui.no_category_label_2.setText(f'{no_category}')

        
    # Load Data for Items Table
    def loadData(self, rows=None):
        connection = sqlite3.connect("DBMS.db")
        cursor = connection.cursor()

        # If rows are not provided, select all rows from the database
        if rows is None:
            query = "SELECT * FROM items ORDER BY id DESC;"
            result = cursor.execute(query).fetchall()
        else:
            result = rows

        self.ui.tableWidget.setRowCount(0)
        tablerow = 0
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            self.ui.tableWidget.setRowHeight(row_number, 40)
            #self.ui.tableWidget.setStyleSheet("QTableWidget::item { border-bottom:1px solid #ebebea;}")
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number+1, QTableWidgetItem(str(data))) 
            self.addCheckBox(row_number)   
    def loadData_2(self, rows=None):
        # load Data from orders table
        if rows is None:
            query = "SELECT * FROM orders ORDER BY order_id DESC;"
            result = cursor.execute(query).fetchall()
        else:
            result = rows

        self.ui.tableWidget_2.setRowCount(0)
        tablerow = 0
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_2.insertRow(row_number)
            self.ui.tableWidget_2.setRowHeight(row_number, 40)
            #self.ui.tableWidget_2.setStyleSheet("QTableWidget::item { border-bottom:1px solid #ebebea;}")
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data))) 
            #self.addCheckBox_2(row_number)
    def loadData_3(self, rows=None):
        # load Data from history table
        if rows is None:
            query = "SELECT * FROM history ORDER BY id DESC;"
            result = cursor.execute(query).fetchall()
        else:
            result = rows

        self.ui.tableWidget_3.setRowCount(0)
        tablerow = 0
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_3.insertRow(row_number)
            self.ui.tableWidget_3.setRowHeight(row_number, 40)
            #self.ui.tableWidget_3.setStyleSheet("QTableWidget #tableWidget_3::item { border-bottom:1px solid #ebebea;}")
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(data))) 
        
            #self.addCheckBox_2(row_number)
    def loadData_4(self, rows=None):
        # If rows are not provided, select all rows from the database
        if rows is None:
            query = "SELECT * FROM items ORDER BY id DESC;"
            result = cursor.execute(query).fetchall()
        else:   
            result = rows

        self.ui.tableWidget_4.setRowCount(0)
        tablerow = 0
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_4.setItem(row_number, column_number+1, QTableWidgetItem(str(data))) 
            self.addCheckBoxTable4(row_number)
    
    def logout_function(self):
        reply = QMessageBox.question(self, 'Confirm Logout', 'Are you sure you want to logout?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
if __name__ == "__main__":
    app=QApplication(sys.argv)
    login_dialog = Login()
    login_dialog.setWindowTitle("Login")
    login_dialog.setFixedSize(420, 520)
    login_dialog.show()

    # Define a slot to show the main application window
    def show_main_window():
        main_window = MainWindow()
        main_window.showMaximized()
        
        login_dialog.close()

    login_dialog.login_success.connect(show_main_window)
    app.exec()
    
        
    