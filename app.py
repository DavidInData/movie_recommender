import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv("thisIsLast.csv")

df['features'] = df['director'] + ' '  + df['genre_names'] + ' ' + df['tag_names'] + ' ' + df['synopsis'] + ' '  + df['cast_names']
df['features'] = df[['features']].stack().str.replace(',',' ').unstack()
df['features'] = df[['features']].stack().str.replace('  ',' ').unstack()

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
df['features'] = df['features'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df['features'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#Construct a reverse map of indices and movie titles
indices = pd.Series(df.index, index=df['Name']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[0:11]
    #print (sim_scores)

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    #print (scores)

    # Return the top 10 most similar movies
    final_df = df[['Name','rating','num_raters','genre_names','director']].iloc[movie_indices]
    final_df['Score'] = np.array(scores) 
    return final_df


#get_recommendations('Parasite')


from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        #access the data from form
        ## Age
        age = str(request.form["age"])
        #get prediction
        prediction = get_recommendations(age)
        output = prediction
        #return render_template("index.html", prediction_text='Your suggested movies are {}'.format(output['Name']))
        return render_template("index.html", prediction_text=output['Name'].iloc[1], 
            prediction_text1 = output['Name'].iloc[2],
            prediction_text2 = output['Name'].iloc[3],
            prediction_text3 = output['Name'].iloc[4],
            prediction_text4 = output['Name'].iloc[5],
            prediction_text5 = output['Name'].iloc[6],
            prediction_text6 = output['Name'].iloc[7],
            prediction_text7 = output['Name'].iloc[8],
            prediction_text8 = output['Name'].iloc[9],
            prediction_text9 = output['Name'].iloc[10],)
if __name__ == "__main__":
    app.run(debug=True)
