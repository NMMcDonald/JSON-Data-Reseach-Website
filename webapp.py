from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/Time-To-beat-Compared-to-Metacritic-Rating")
def render_second():
    if "P1years" in request.args:
        with open('myData.json') as ttb_data:
            data = json.load(ttb_data)
        year = request.args['P1years']
        game = "Title"
        length = 0
        metrics = 0
        for g in data:
            if str(g["Release"]["Year"]) == year and g["Metrics"]["Review Score"] > metrics and g["Length"]["All PlayStyles"]["Average"] > length:
                length = g["Length"]["All PlayStyles"]["Average"]
                metrics = g["Metrics"]["Review Score"]
                game = g["Title"]
        return render_template('page1.html', response = game, pT = length, score = metrics)
    else:
        return render_template('page1.html')

@app.route("/Comparing-The-Revenue-of-Each-Console")
def render_third():
    return render_template('page2.html', nDs = plus("Nintendo DS"), spsp = plus("Sony PSP"), xbx360 = plus("X360"), wii = plus("Nintendo Wii"), ps3 = plus("PlayStation 3"))

def plus(gconsole):
    with open('myData.json') as console_data:
        cdata = json.load(console_data)
        revg = 0
        for k in cdata:
            if gconsole == k["Release"]["Console"]:
                revg = revg + k["Metrics"]["Sales"]
        return revg







if __name__=="__main__":
    app.run(debug=True)
