from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QDialog, QLineEdit, QFormLayout, QHBoxLayout, QMessageBox, QComboBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QSpinBox,  QDateEdit
from PyQt5.QtCore import QDate, Qt

import sys
import re
import sqlite3
import mysql.connector


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About KUCINA UNOSANA")
        self.setGeometry(500, 320, 900, 600)

        self.setStyleSheet("""
            QDialog {
                background-color: #F0F0F0; /* Set background color */
                border: 2px solid #C0C0C0; /* Add border */
                border-radius: 10px; /* Rounded corners */
            }
            QLabel {
                color: #303030; /* Text color */
            }
            QPushButton {
                background-color: #607274; /* Button background color */
                color: white; /* Button text color */
                border: 2px solid #F5F5F5; /* Button border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px 10px; /* Add padding */
            }
            QPushButton:hover {
                background-color: #435C66; /* Change background color on hover */
            }
        """)

        layout = QVBoxLayout()

        about_label = QLabel(
            "KUCINA UNOSANA is a fine dining restaurant specializing in different cuisines such as Italian, Japanese, "
            "and Asian. We, at Kucina Unosana, serve food that makes our customers feel satisfied and full. "
            "Located in the heart of the city of Mayfair, we offer a cozy and elegant ambiance, as well as friendly "
            "servers for our guests to enjoy authentic dishes prepared with the freshest ingredients and highly skilled chefs in the world. "
            "Experience the taste of wonderful foods at KUCINA UNOSANA!\n\n\n"

            "-----LOCATION-----\n"
            "1ST Narnian St. Winterfell City, Mayfair, PH\n\n\n"

            "------ CONTACT US -----\n"
            "Email                    : kusinaunosana@gmail.com\n"
            "Website               : www.kusinaunosana.com\n"
            "Facebook Page  : Kusina Unosana\n"
            "Telephone No.    : 011-0101-0111\n")
        about_label.setFont(QFont("Arial", 14))
        about_label.setWordWrap(True)
        layout.addWidget(about_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)


class ReservationDialogStep1(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Reservation")
        self.setGeometry(500, 320, 600, 400)  # Larger size

        self.setStyleSheet("""
            QDialog {
                background-color: #F0F0F0; /* Set background color */
                border: 2px solid #C0C0C0; /* Add border */
                border-radius: 10px; /* Rounded corners */
            }
            QLabel, QLineEdit {
                color: #303030; /* Text color */
                font-size: 16px; /* Font size */
            }
            QLineEdit {
                padding: 10px; /* Add padding to input fields */
                border: 1px solid #C0C0C0; /* Add border to input fields */
                border-radius: 5px; /* Rounded corners */
            }
            QPushButton {
                background-color: #607274; /* Button background color */
                color: white; /* Button text color */
                border: 2px solid #F5F5F5; /* Button border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px 20px; /* Add padding */
                margin-top: 20px; /* Add margin between buttons */
            }
            QPushButton:hover {
                background-color: #435C66; /* Change background color on hover */
            }
        """)

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.contact_input = QLineEdit()

        form_layout.addRow("Reservation Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Contact No.:", self.contact_input)

        button_layout = QHBoxLayout()
        proceed_button = QPushButton("Proceed")
        cancel_button = QPushButton("Cancel")
        proceed_button.clicked.connect(self.validate_inputs)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(proceed_button)
        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def validate_inputs(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        contact = self.contact_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Input Error", "Please enter your name.")
            return
        if not email or not self.is_valid_email(email):
            QMessageBox.warning(self, "Input Error", "Please enter a valid email address.")
            return
        if not contact:
            QMessageBox.warning(self, "Input Error", "Please enter your contact number.")
            return

        self.accept()
        reservation_dialog_step2 = ReservationDialogStep2(name, email, contact)
        reservation_dialog_step2.exec_()

    def is_valid_email(self, email):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return email_regex.match(email) is not None


class ConfirmationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmation")
        self.setGeometry(600, 400, 400, 200)

        layout = QVBoxLayout()

        label = QLabel("Please confirm if the entered information is correct:")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        confirm_button = QPushButton("Confirm")
        confirm_button.clicked.connect(self.accept)
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(edit_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)


class ReservationDialogStep2(QDialog):
    def __init__(self, name, email, contact):
        super().__init__()
        self.setWindowTitle("Reservation Area")
        self.setGeometry(500, 320, 600, 500)  

        self.name = name
        self.email = email
        self.contact = contact

        self.setStyleSheet("""
            QDialog {
                background-color: #F0F0F0; 
                border: 2px solid #C0C0C0; 
                border-radius: 10px; 
            }
            QLabel, QLineEdit, QComboBox, QSpinBox, QDateEdit {
                color: #303030; 
                font-size: 16px; 
            }
            QComboBox, QSpinBox, QDateEdit {
                padding: 10px; 
                border: 2px solid #C0C0C0; 
                border-radius: 5px; 
            }
            QLineEdit[placeholder="Select Area"], QLineEdit[placeholder="No. of Pax"], QLineEdit[placeholder="Select Time"], QLineEdit[placeholder="Select Date"] {
                color: #8C8C8C; 
            }
            QPushButton {
                background-color: #607274; 
                color: white; 
                border: 2px solid #F5F5F5; 
                border-radius: 5px; 
                padding: 10px 20px; 
                margin-top: 20px; 
            }
            QPushButton:hover {
                background-color: #435C66; 
            }
        """)

        form_layout = QFormLayout()

        self.area_combo = QComboBox()
        self.area_combo.addItems(["Inside Dining", "Al Fresco", "Balcony", "Rooftop", "VIP Lounge", "Family Lounge", "Function Hall"])

        self.pax_spinbox = QSpinBox()
        self.pax_spinbox.setMinimum(1)
        self.pax_spinbox.setMaximum(300)

        self.time_combo = QComboBox()
        self.time_combo.addItems(["BREAKFAST (7:00 AM-10:59 AM)",
                                  "LUNCH (11:00 AM-1:59 PM)",
                                  "LATE LUNCH (2:00 PM-5:59 PM)",
                                  "EARLY DINNER (6:00 PM-8:59 PM)",
                                  "LATE DINNER(9:00 PM-10:59 PM)"])

        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())

        self.price_label = QLabel("\n\nPRICE PER PAX        : 200\n"
                                  "\nAREA PRICES"
                                  "\nInside Dining          :  500"
                                  "\nAl Fresco              :  500"
                                  "\nBalcony                :  600"
                                  "\nRooftop                :  700"
                                  "\nVIP Lounge             :  1000"
                                  "\nFamily Lounge          : 2000"
                                  "\nFunction Hall          : 10000")
        self.price_label.setStyleSheet("color: #303030; font-size: 14px;")

        form_layout.addRow("Select Area:", self.area_combo)
        form_layout.addRow("No. of Pax:", self.pax_spinbox)
        form_layout.addRow("Select Time:", self.time_combo)
        form_layout.addRow("Select Date:", self.date_edit)
        form_layout.addRow("Price:", self.price_label)  

        self.payment_method_combo = QComboBox()
        self.payment_method_combo.addItems(["Credit Card", "PayPal", "PayMaya","G-cash"])

        form_layout.addRow("Payment Method:", self.payment_method_combo)

        button_layout = QHBoxLayout()
        confirm_proceed_button = QPushButton("Proceed")
        cancel_button = QPushButton("Cancel")
        confirm_proceed_button.clicked.connect(self.confirm_proceed_reservation)

        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(confirm_proceed_button)

        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def confirm_proceed_reservation(self):
        confirmation_dialog = ConfirmationDialog(self)
        if confirmation_dialog.exec_() == QDialog.Accepted:
            self.proceed_reservation()

    def proceed_reservation(self):
        area = self.area_combo.currentText()
        pax = self.pax_spinbox.value()
        time = self.time_combo.currentText()
        date = self.date_edit.date().toString("yyyy-MM-dd")
        payment_method = self.payment_method_combo.currentText()

        # Calculate prices
        area_prices = {"Inside Dining": 500, "Al Fresco": 500,
                                "Balcony": 600, "Rooftop": 700,
                                "VIP Lounge": 1000,
                                "Family Lounge": 2000, "Function Hall": 10000}
        area_price = area_prices.get(area, 0)
        pax_price = 200 * pax
        total_price = area_price + pax_price

        # Connect to the database using XAMPP
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kusinaunosana"
        )

        # Create a new cursor
        cursor = database.cursor()

        # Insert reservation details into the database
        insert_query = "INSERT INTO reservations (name, email, contact, area, pax, time, date, payment_method, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"  
        reservation_data = (self.name, self.email, self.contact, area, pax, time, date, payment_method, total_price)
        cursor.execute(insert_query, reservation_data)

        # Commit the transaction
        database.commit()

        # Close the cursor and the database connection
        cursor.close()
        database.close()

        QMessageBox.information(self, "Reservation Confirmed",
                                f"Your reservation has been confirmed for {area} - {pax} pax at {time} on {date}. "
                                f"Payment method: {payment_method}\n"
                                f"Price breakdown:\n"
                                f"Area fee: ${area_price}\n"
                                f"Price per pax: ${pax_price}\n"
                                f"Total price: ${total_price}")
        self.accept()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("KUCINA UNOSANA")
        self.setGeometry(100, 100, 1200, 800)

        self.label = QLabel(self)
        self.pixmap = QPixmap("bg4.png")
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

        # Add buttons with absolute positioning
        reserve_button = QPushButton("RESERVE TABLE", self)
        reserve_button.setGeometry(500, 700, 300, 80)
        reserve_button.setFont(QFont("Arial", 15))
        reserve_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #607274;"
            "   color: white;"
            "   border: 2px solid #F5F5F5;"
            "   border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #435C66;"
            "}"
        )
        reserve_button.clicked.connect(self.show_reservation_dialog_step1)

        about_button = QPushButton("ABOUT US", self)
        about_button.setGeometry(900, 700, 300, 80)
        about_button.setFont(QFont("Arial", 15))
        about_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #607274;"
            "   color: white;"
            "   border: 2px solid #F5F5F5;"
            "   border-radius: 10px;"
            "}"
            "QPushButton:hover {"
            "   background-color: #435C66;"
            "}"
        )
        about_button.clicked.connect(self.show_about_dialog)

    def show_about_dialog(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()

    def show_reservation_dialog_step1(self):
        reservation_dialog_step1 = ReservationDialogStep1()
        reservation_dialog_step1.exec_()

    def resizeEvent(self, event):
        self.label.resize(self.size())
        super().resizeEvent(event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
