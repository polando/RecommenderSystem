import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('E:/programmingPRoj/ml-latest-small/ratings.csv', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('E:/programmingPRoj/ml-latest-small/movies.csv', names=m_cols, usecols=range(2))

ratings = pd.merge(movies,ratings)

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

CorrMatrix = movieRatings.corr(method='pearson', min_periods=100)

myRatings = movieRatings.loc[5].dropna()

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    sims = CorrMatrix[myRatings.index[i]].dropna()
    sims = sims.map(lambda x: x*myRatings[i])
    simCandidates = simCandidates.append(sims)

simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace=True, ascending=False)

print(simCandidates.head())