from os import path
from gensim.models import FastText,Word2Vec


class PersianSimilarity:

    #Class Variables
    _FastTextModel=0;
    _Word2VecModel=0;
    _models_path = path.join(path.dirname(__file__), 'models')

    def __init__(self):
        """
        initializing Class
        """
        #Loading FastText Model...
        self._FastTextModel = FastText.load(self._models_path+"/FastText_Farsi.model")
        #Loading Word2Vec Model...
        self._Word2VecModel = Word2Vec.load(self._models_path+"/Word2Vec_Farsi.model")


    def getSimilarities(self,positive_list=[],negative_list=[],algorithm='w2v',topn=8):
        """
        Finds the similarities of the given words.
        Parameters:
            positive_list
            negative_list
            algorithm  --> 'w2v'  or 'ft'
            topn
        """
        if algorithm == 'w2v':
            result = self._Word2VecModel.wv.most_similar_cosmul(positive=positive_list, negative=negative_list,topn=topn)
        else:
            result = self._FastTextModel.wv.most_similar_cosmul(positive=positive_list, negative=negative_list,topn=topn)

        output = sorted(result, key=lambda x: x[1])
        output.reverse()
        return output

