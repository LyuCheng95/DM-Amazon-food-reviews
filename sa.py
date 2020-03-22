import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
df = pd.read_csv('Reviews.csv')
sa_compound_score = []
for i in range(0,len(df)):
    sa_compound_score.append(sid.polarity_scores(df.iloc[i]['Text'])['compound'])
df['sa_compound_score']= sa_compound_score
df.to_csv('Reviews_sa.csv')