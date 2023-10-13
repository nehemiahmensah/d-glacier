# name = input("Enter text ")
# name = name.isalpha()
# if name == True:
#     print("Good ")
# else:
#     print("Not true")

import gooeypie as gp

def nwmg(event):
    if email_inp == 'me':
        app2 = gp.GooeyPieApp('Home')
        app2.width = 400
        app.exit()
        app2.run()
    
    

    
    


app = gp.GooeyPieApp('LOGIN')
app.width = 350
#set labels
email_label = gp.Label(app, "Email:")
pass_label  = gp.Label(app, "Password: ")
log_label   = gp.Label(app, " ")
email_inp   = gp.Input(app)
pass_inp    = gp.Secret(app)
log_btn     = gp.Button(app, "Login", nwmg)

#postiton labels in window
app.set_grid(4,2)
app.add(email_label,1, 1)
app.add(email_inp, 1, 2)
app.add(pass_label, 2, 1)
app.add(pass_inp, 2 , 2)
app.add(log_btn, 3, 2)
app.add(log_label, 4, 2)

app.run()