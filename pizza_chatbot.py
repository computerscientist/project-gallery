import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define some predefined responses
responses = {
    "pizza": "What kind of pizza do you want today?",
    "cheese": "You selected cheese pizza",
    "pepperoni": "You selected pepperoni pizza",
    "meat": "You selected meat pizza",
    "bacon": "You added bacon as a topping",
    "ham" : "You added ham as a topping",
    "chicken": "You added chicken as a topping",
    "mushroom": "You added mushrooms as a topping",
    "onion": "You added onions as a topping",
    "spinach": "You added spinach as a topping",
    "olive": "You added olives as a topping",
    "tomato": "You added tomatoes as a topping",
    "tomatoe": "You added tomatoes as a topping",
    "bye": "Goodbye! Hope to see you again soon!",
    "default": "I'm sorry, I don't understand that. Can you rephrase?"
}

possible_toppings = ["pepperoni", "bacon", "ham", "chicken", "mushroom", "onion", "spinach", "olive", "tomato", "tomatoe"]
toppings = []

pizza_type = ""

CHEESE = "cheese"
PEPPERONI = "pepperoni"
MEAT = "meat"

def add_topping(topping):
    global toppings
    if topping == "tomatoe":
        topping = "tomato"

    if topping in toppings:
        print("This topping is already added.")
        return False
    else:
        toppings.append(topping)
        return True


# Function to find the appropriate response
def get_response(input_text):
    global pizza_type
    global toppings

    doc = nlp(input_text)
    # print(doc)
    for token in doc:
        if token.lemma_ in [CHEESE]:
            if pizza_type == CHEESE:
                return handle_reset_case(pizza_type)
            pizza_type = token.lemma_
            print(pizza_type)
            toppings = []
            return responses[CHEESE]
        elif token.lemma_ in [PEPPERONI]:
            if pizza_type == PEPPERONI:
                return handle_reset_case(pizza_type)
            pizza_type = token.lemma_
            toppings = []
            return responses[PEPPERONI]
        elif token.lemma_ in [MEAT]:
            if pizza_type == MEAT:
                return handle_reset_case(pizza_type)
            pizza_type = token.lemma_
            toppings = []
            return responses[MEAT]
        elif token.lemma_ in possible_toppings:
            if pizza_type:
                added = add_topping(token.lemma_)
                if added:
                    return responses[token.lemma_]
                else:
                    return "This topping is already added."
            else:
                return "Please select a pizza type first."
        elif token.lemma_ in ["bye", "goodbye"]:
            if pizza_type:
                toppings_list = ', '.join(toppings) if toppings else 'no additional toppings'
                print(f"You ordered a {pizza_type} pizza with the following toppings: {toppings_list}.")
            return responses["bye"]
    return responses["default"]


# Function to reset the toppings for a pizza
def handle_reset_case(pizza_type):
    global toppings
    toppings = []
    response = f"Resetting toppings for {pizza_type} pizza."
    return response


# Function to handle pepperoni special case
def handle_pepperoni_special_case(input_text):
    global pizza_type
    global toppings

    doc = nlp(input_text)
    for token in doc:
        print(token.lemma_)
        if token.lemma_ in [PEPPERONI, "pizza"]:
            if pizza_type == PEPPERONI:
                return handle_reset_case(pizza_type)
            pizza_type = PEPPERONI
            toppings = []
            return "Ok, pepperoni pizza it is!"
        elif token.lemma_ in ["top", "topping", "toppings"]:
            if pizza_type == PEPPERONI:
                return "You already have a pepperoni pizza. Can't add pepperoni as a topping..."
            added = add_topping(PEPPERONI)
            if added:
                return "Okay, I'll add pepperoni as a topping."
            else:
                return "This topping is already added."
        elif token.lemma_ in ["bye", "goodbye"]:
            if pizza_type:
                toppings_list = ', '.join(toppings) if toppings else 'no additional toppings'
                print(f"You ordered a {pizza_type} pizza with the following toppings: {toppings_list}.")
            return responses["bye"]

    return "I'm sorry, I didn't catch that. Please answer with 'pepperoni' or 'topping'."


# Main loop to interact with the chatbot
def chat():
    global pizza_type

    print("Chatbot: Welcome to the pizza ordering app! Type 'bye' at any time to end the conversation.")
    print("Pizzas available: we have cheese, pepperoni, and meat pizzas available.")
    print("To reset the toppings for a pizza, simply type the same pizza name again.")
    print(responses["pizza"])

    while True:
        if pizza_type:
            print("Possible toppings: " + ", ".join(possible_toppings))
        user_input = input("You: " if not pizza_type else "Enter toppings, or change pizza type: ")
        doc = nlp(user_input)
        pepperoni_special_case = False
        for token in doc:
            if token.lemma_ in [PEPPERONI] and pizza_type:
                pepperoni_special_case = True

        if pepperoni_special_case:
            pepperoni_input = input("Would you like a pepperoni pizza or pepperoni as a topping? ")
            pepperoni_response = handle_pepperoni_special_case(pepperoni_input)
            if pepperoni_response == responses["bye"]:
                break
        else:
            response = get_response(user_input)

        if not pepperoni_special_case and response == responses["bye"]:
            break

        if pepperoni_special_case:
            print(f"Chatbot: {pepperoni_response}")
        else:
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()
