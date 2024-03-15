from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__, template_folder='templates', static_url_path='/static')

# Sample data for training the model
training_data = {
    'text': ['Mayil Aattam,mayil aattam,MAYIL AATTAM ,Oyil Aattam,oyil aattam,OYIL AATTAM, Puli Aattam,puli aattam,PULI AATTAM, Barathanatiyam,barathanatiyam,BARATHANATIYAM, Karakaatam,karakaatam,KARAKAATAM, POIKAL KUTHIRAI,Poikal Kuthirai,poikal kuthirai', 'Villu Paatu,villu paatu,VILLU PAATU, kummi,KUMMI,Kummi', 'Cultural Festivals,CULTURAL FESTIVALS,cultural festivals'],
    'label': ['Dance', 'Music', 'Festivals']
}

# Create a Naive Bayes classifier pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(training_data['text'], training_data['label'])

# Default label for unrecognized arts
default_label = 'Other'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Get form data
        print(request.form)

        Name = request.form.get('name')
        Mobile_Number = request.form.get('mobile_number')
        Email = request.form.get('email')
        Arts_Known = request.form.get('arts_known')
        Years_of_Experience = request.form.get('experience')

        print("Received data: {Name}, {Mobile_Number}, {Email}, {Arts_Known}, {Years_of_Experience}")

        # Perform Naive Bayes classification or any other processing you need
        # This is just an example, replace it with your actual logic
        predicted_label = model.predict([Arts_Known])[0]

        # Check if the predicted label is in the original training labels
        if predicted_label not in training_data['label']:
            # Assign a default label for unrecognized arts
            predicted_label = default_label

        # Return classification result to the HTML template
        return render_template('result.html', 
                               name=Name, 
                               mobile_number=Mobile_Number, 
                               email=Email, 
                               arts_known=Arts_Known, 
                               years_of_experience=Years_of_Experience, 
                               result=predicted_label)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
