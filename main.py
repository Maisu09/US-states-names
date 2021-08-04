import turtle
import pandas

screen = turtle.Screen()
screen.title("U S State Game")
# tr=turtle.Turtle()
image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)

# answer_state = screen.textinput(title="Guess the State", prompt="What's another state ?")

data = pandas.read_csv("50_states.csv")
# x = data[data['state'] == 'Alabama']
# x.to_dict()


#print(str(x['state'])) Putem da asa loop prin ele 
# x = data[data['state'] == answer_state]['state']
# if x.item() == answer_state:
#     print(answer_state)
guess_number = 0
while True:

    answer_state = screen.textinput(title=f"Guess the State {guess_number}/50", prompt="What's another state ?")
    x = data[data['state'] == answer_state]['state']
    try:
        if x.item() == answer_state:
            print(answer_state)
            turtle.setposition(int(data[data['state'] == answer_state]['x']), int(data[data['state'] == answer_state]['y']))
            turtle.write(f"{str(x)}")
            turtle.home()
            guess_number += 1
        
    except ValueError:
        pass




turtle.exitonclick()
