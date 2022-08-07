from flask import Flask, Response
import os

app = Flask(__name__)


IMAGE_FOLDER = os.path.join('images', 'image_home')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER 

@app.route("/home")
def home():
    img_path = os.path.join(app.config['IMAGE_FOLDER'], 'image_home.jpg')
    return render_template('home.html', image=img_path)

@app.route("")

@app.route("/wav")
def streamwav():
    def generate():
        with open("signals/song.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


#@app.route("/ogg")
#def streamogg():
#    def generate():
#        with open("signals/song.ogg", "rb") as fogg:
#            data = fogg.read(1024)
#            while data:
#                yield data
#                data = fogg.read(1024)
#    return Response(generate(), mimetype="audio/ogg")
#
if __name__ == "__main__":
    app.run(debug=True)
