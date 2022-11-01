import turtle
import pandas as pd

screen = turtle.Screen()
# give screen function Screen()
screen.title("US States Game")
# give title to GUI
img = "blank_states_img.gif"
# import file image
screen.addshape(img)
# to create new shape with image
turtle.shape(img)
# untuk menampilkan shape

data = pd.read_csv("50_states.csv")
# import file csv
all_state = data.state.to_list()
# mengambil baris state pada file csv lalu diubah ke list
# hanya berisi data state
guess_state = []
# array kosong

while len(guess_state) < 50:
    # pengulangan
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 Guess the state",
    # untuk menyimpan jawaban dari user, len(guess_state) untuk menampilkan isi array
                                    prompt="What the state another name ?").title()
    # if they got it right:
    if answer_state == "exit":
        # menyesuaikan jawaban user
        missing_state = []
        for state in all_state:
            # mengambil isi data dari data all_State
            if state not in all_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # create turtle to write
        t.write(state_data.state.item())

# states_to_learn.csv
