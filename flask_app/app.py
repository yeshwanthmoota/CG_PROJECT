from flask import Flask, request, render_template, redirect
import os

from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/SpaceInvaders", methods=["GET"])
def spaceInvaders():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Space_Invaders")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 main.py")

    return redirect(url_for('home'))


@app.route("/FlappyBird", methods=["GET"])
def flappyBird():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Flappy_Bird")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 main.py")
        

    return redirect(url_for('home'))



@app.route("/PhysicsPong", methods=["GET"])
def pingPong():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Physics_Pong_Singleplayer")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 main.py")

        
    return redirect(url_for('home'))

@app.route("/PlanetaryGravitation", methods=["GET"])
def gravitation():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Planetary_Gravitation_Simulation")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 main.py")

        
    return redirect(url_for('home'))


@app.route("/CollisionSimulation", methods=["GET"])
def collision():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Collision_Simulation")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 main.py")

        
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)