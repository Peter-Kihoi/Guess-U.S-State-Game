import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

game_on = True
score = 0
guessed_states = []
while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_state = []
        for state_name in data.state.to_list():
            if state_name not in guessed_states:
                missing_state.append(state_name)
        game_on = False
    if answer_state in data.state.to_list():
        guessed_states.append(answer_state)
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        score += 1

        state = turtle.Turtle()
        state.penup()
        state.goto(x, y)
        state.hideturtle()
        state.clear()
        state.write(answer_state, align="center", font=("algerian", 10, "normal"))

    if score == 50:
        game_on = False
