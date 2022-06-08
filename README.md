# PersianSimilarity
A simple, fast Python package which finds **Persian(Farsi)** words similarities.

Target audience is the natural language processing (NLP) community.

Model is based on Neural Network. Trained using [Gensim Library](https://github.com/RaRe-Technologies/gensim), with **6,000,000,000** Farsi words

### Supported Algorithms:
- **[Word2Vec](https://en.wikipedia.org/wiki/Word2vec)**



### Who is this package for?
- `Persian Software engineers`
- `Persian Data scientists`
- `Persian College graduates`
- `Persian Product Managers`



## Usage:

- Copy files to your project



### Call method with **positive** parameters:
```python

from  PersianSimilarity import PersianSimilarity
PersianSimilarity = PersianSimilarity()
result = PersianSimilarity.getSimilarities(['تیبا','پراید']))

```

### Call method with **positive/negative** parameters:
```python

from  PersianSimilarity import PersianSimilarity
PersianSimilarity = PersianSimilarity()
result = PersianSimilarity.getSimilarities(['تیبا','پراید'],['سایپا'])

```
