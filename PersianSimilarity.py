from os import path
from gensim.models import Word2Vec


class PersianSimilarity:

    #Class Variables
    _Word2VecModel=0;
    _models_path = path.join(path.dirname(__file__), 'models')

    def __init__(self):
        """
        initializing Class
        """
        #Loading Word2Vec Model...
        self._Word2VecModel = Word2Vec.load(self._models_path+"/Word2Vec_Farsi.model")


    def getSimilarities(self,positive_list=[],negative_list=[],topn=8):
        """
        Finds the similarities of the given words.
        """

        result = self._Word2VecModel.wv.most_similar_cosmul(positive=positive_list, negative=negative_list,topn=topn)

        output = sorted(result, key=lambda x: x[1])
        output.reverse()
        return output
