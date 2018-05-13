import csv

import os
import re
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def remove_useless_words(s):
    """
    Remove RT, URLs, and mentions
    """
    return re.sub('(rt|http\S+|@\S+)', '', s, flags=re.I)


def get_documents(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                            dialect=csv.excel)
        return [remove_useless_words(row[0]) for row in reader]


def main():
    documents = []
    ls = os.listdir('data')
    for filename in ls:
        documents += get_documents('data/{}'.format(filename))

    no_features = 1000

    # NMF is able to use tf-idf
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(documents)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()

    # LDA can only use raw term counts for LDA because it is a probabilistic graphical model
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(documents)
    tf_feature_names = tf_vectorizer.get_feature_names()

    no_components = 2

    # Run NMF
    nmf = NMF(n_components=no_components, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

    # Run LDA
    lda = LatentDirichletAllocation(n_components=no_components, max_iter=5, learning_method='online',
                                    learning_offset=50., random_state=0).fit(tf)

    def display_topics(model, feature_names, no_top_words, label):
        print('\n\n--- {} ---'.format(label))
        for topic_idx, topic in enumerate(model.components_):
            topic = " ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]])
            print("Topic {}: {}".format(topic_idx, topic))

    no_top_words = 10
    display_topics(nmf, tfidf_feature_names, no_top_words, ' NMF Topics')
    display_topics(lda, tf_feature_names, no_top_words, 'LDA Topics')


if __name__ == '__main__':
    main()
