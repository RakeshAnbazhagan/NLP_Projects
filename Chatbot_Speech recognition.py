import speech_recognition as sr #package

class Hotel_xyz_Chatbot:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen_input(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            text = self.r.recognize_google(audio)
            return text
        except Exception as e:
            print(e)
            return ""

    def booking_eligibility(self, name, mobile_number,dob, address, id_proof):
        # check if the customer is eligible to book a room
        # for example, you can check if the customer is above 18 years old and has a valid ID proof
        return True

    def book_room(self, name, mobile_number,age, address, id_proof, room_type, arrival_date, departure_date):
        if self.booking_eligibility(name, mobile_number,age, address, id_proof):
            # book the room and return a confirmation message
            return f"Congratulations, {name}! Your room has been booked successfully. " \
                   f"Details: Room Type: {room_type}, Arrival Date: {arrival_date}, Departure Date: {departure_date}"
        else:
            return "Sorry, you are not eligible to book a room."

    def run(self):
        while True:
            print("Welcome to the Hotel Booking Chatbot!")
            print("Please tell us your name:")
            name = self.listen_input()
            print("Please tell us your mobile number:")
            mobile_number = self.listen_input()
            print("Please tell us your address:")
            age = self.listen_input()
            print("Please tell your Age")
            address = self.listen_input()
            print("Please provide your ID proof:")
            id_proof = self.listen_input()
            print("Please select the type of room you would like to book:")
            room_type = self.listen_input()
            print("Please tell us the arrival date:")
            arrival_date = self.listen_input()
            print("Please tell us the departure date:")
            departure_date = self.listen_input()
            print(self.book_room(name, mobile_number,age, address, id_proof, room_type, arrival_date, departure_date))
            print("Thank you for using our chatbot. Have a nice day!")
            break

if __name__ == "__main__":
    chatbot = Hotel_xyz_Chatbot()
    chatbot.run()
