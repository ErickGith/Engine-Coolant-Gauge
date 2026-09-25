# Author : Erick Lanchipa
# Class : ITN160
# Class Section : 201
# Date : 0/17/2026
# Module 11 Project 3: Engine Coolant Gauge


# 1. Import from Python Libraries
from guizero import App,Slider, Waffle, Text

# 2. Change slider value into a number
def update_temp(slider):
    temp = int(slider.value)

    # 3.Save waffle and text
    waffle = update_temp.waffle
    text = update_temp.text

    # 4. Power off
    if temp == 0:
        waffle.set_all("black")
        text.value = "Power off - The temperature is Not good to sail, Capitan Jack!!!"

    # 5. Warming up
    elif 1 <= temp <= 194:
        waffle.set_all("blue")
        text.value = "Warming up - The temperature is almost good to sail, Capitan Jack!!!"

    # 6. Normal
    elif 195 <= temp <= 220:
        waffle.set_all("green")
        text.value = "Normal - The temperature is good to sail, Capitan Jack!!!"

    # 7. Hot
    elif 221 <= temp <= 300:
        waffle.set_all("red")
        text.value = "Hot - The temperature is too Hot to sail, Capitan Jack!!!"


# 8. Main program
def main():
    # 9. Make the app window
    app = App(title="Coolant Gauge Temperature", width=300, height=400)

    # 10.Slider for the coolant temp(0 to 300)
    slider = Slider(app, start=0, end=300, width=50, height=300, align="left")

    # 11. Waffle square to show the temp color (1x1)
    waffle = Waffle(app, width=1, height=1, dim=50, align="left")
    waffle.set_all("black")
    # 12. Text label for my message
    text = Text(app, text="The temperature is good to sail, Capitan Jack!!!")

    # 13. Add waffle and text to the update function
    update_temp.waffle = waffle
    update_temp.text = text

    # 14. Connect the slider to the update function
    app.repeat(50,lambda: update_temp(slider))

    # 15. Show the window
    app.display()


# 16. Run the program Capitan Jack!!!
main()