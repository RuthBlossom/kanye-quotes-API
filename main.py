from tkinter import *
from PIL import Image, ImageTk
import requests

# Function to fetch and display a Kanye West quote
def get_quote():
    # Make a request to the Kanye REST API
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()  # Parse the response as JSON
    quote = data["quote"]  # Extract the Kanye West quote from the JSON data
    canvas.itemconfig(quote_text, text=quote)  # Update the displayed quote on the canvas

# Create the main Tkinter window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas to display images and text
canvas = Canvas(width=300, height=414)

# Open and display the background image on the canvas
background_img = Image.open("background.png")
background_img = ImageTk.PhotoImage(background_img)
canvas.create_image(150, 207, image=background_img)

# Create a text element on the canvas to display the Kanye West quote
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")

# Place the canvas in the main window's grid
canvas.grid(row=0, column=0)

# Open and display the Kanye West image as a button
kanye_img = Image.open("kanye.png")
kanye_img = ImageTk.PhotoImage(kanye_img)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the Tkinter event loop
window.mainloop()


