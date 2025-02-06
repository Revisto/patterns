class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailService:
    def send_email(self, customer, message):
        # Sending an email to the customer
        pass

class OrderService:
    def place_order(self, customer, order):
        # Placing an order
        pass

class InvoiceService:
    def generate_invoice(self, customer, invoice):
        # Generating an invoice
        pass

class FeedbackService:
    def add_feedback(self, customer, feedback):
        # add customer feedback
        pass