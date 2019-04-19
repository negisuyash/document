from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/bag_packing.html')
def bag_packing():
    return render_template('bag_packing.html')

@app.route('/gensim.models.word2vec.html')
def gensim():
    return render_template('gensim.models.word2vec.html')

@app.route('/geopy.geocoders.html')
def geopy():
    return render_template('geopy.geocoders.html')

@app.route('/get_add_vec.html')
def get_add_vec():
     return render_template('get_add_vec.html')

@app.route('/get_geocode.html')
def get_geocode():
    return render_template('get_geocode.html')

@app.route('/googlemaps.html')
def googlemaps():
    return render_template('googlemaps.html')

@app.route('/inspect.html')
def inspect():
    return render_template('inspect.html')

@app.route('/keras_based_multiple.html')
def keras_based_multiple():
    return render_template('/keras_based_multiple.html')

@app.route('/logging.html')
def logging():
    return render_template('logging.html')

@app.route('/math.html')
def math():
    return render_template('math.html')

@app.route('/ml_beta.html')
def ml_beta():
    return render_template('ml_beta.html')

@app.route('/multiprocessing.html')
def multi():
    return render_template('multiprocessing.html')

@app.route('/nltk.html')
def nltk():
    return render_template('nltk.html')

@app.route('/numpy.html')
def numpy():
    return render_template('nltk.html')

@app.route('/os.html')
def os():
    return render_template('os.html')

@app.route('/pandas.html')
def pandas():
    return render_template('pandas.html')

@app.route('/pickle.html')
def pickle():
    return render_template('pickle.html')

@app.route('/preprocess_add.html')
def preprocess():
    return render_template('preprocess_add.html')

@app.route('/re.html')
def re():
    return render_template('re.html')

@app.route('/regen_data.html')
def regen_data():
    return render_template('regen_data.html')

@app.route('/sklearn.manifold.html')
def sklearn():
    return render_template('sklearn.manifold.html')

@app.route('/sklearn.tree.html')
def sklearn_tree():
    return render_template('sklearn.tree.html')

@app.route('/threading.html')
def thread():
    return render_template('threading.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)