import pandas
import turtle

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 10, "normal")
IMAGE = "blank_states_img.gif"


def app():
# ---------------------------- UI SETUP ------------------------------- #
    screen = turtle.Screen()
    screen.title("U.S States Game")
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)
    bob_the_turtle = turtle.Turtle()
    bob_the_turtle.hideturtle()
    bob_the_turtle.penup()

# ---------------------------- GAME LOGIC ------------------------------- #
    guessed_states = 0
    guessed_states_list = []
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()

    game_is_on = True
    while game_is_on:
        answer_state = screen.textinput(title=f"{guessed_states}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            break
        if (answer_state in state_list) and (answer_state not in guessed_states_list):
            state_axis = data[data.state == answer_state]
            bob_the_turtle.goto(state_axis.x.item(), state_axis.y.item())
            bob_the_turtle.write(f"{answer_state}", align="center", font=FONT)
            guessed_states += 1
            guessed_states_list.append(answer_state)
        if guessed_states == 50:
            game_is_on = False

# ---------------------------- STATES NOT GUESSED ------------------------------- #
    difference = list(set(state_list) - set(guessed_states_list))
    new_data = pandas.DataFrame(difference)
    new_data.to_csv("states_to_learn.csv")
    turtle.mainloop()


if __name__ == "__main__":
    app()
