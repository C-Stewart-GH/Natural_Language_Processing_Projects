
<a name="BackToTop"></a>


# Natural Language Processing Projects

**Contributors: Cameron Stewart**

>The projects in this repository increasingly dive deeper into Natural Language Processing (NLP) concepts to gather insight. The purpose of these projects was purely academic to explore tools used to scrape data from websites and apply NLP analysis with the latest tools.

---

## Table of Contents
- [Project 1 - Analyze Books by Reading Level](#P1)
- [Project 2 - Create Text Difficulty Score](#P2)
- [Project 3 - Comparing sentence outputs of Stemming and Lemmatizing](#P3)
- [Project 4 - Compare Part of Speech Taggers on Complex Sentences](#P4)
- [Project 5 - EDA](#P5)
- [Project 6 - SVM and LR Modeling](#P6)
- [References](#References)

---

<a name="P1"></a>

## Project 1 - Analyze Books by Reading Level

[Project 1](../main/Project%201/Project_1.ipynb)

This project looks at the interaction between lexical diversity and vocabulary size at multiple reading levels. The text was tokenized using Python's NLTK package. Books analyzed were found at: [Project Gutenberg](http://www.gutenberg.org/ebooks/bookshelf/215).

[Back to Top](#BackToTop)

---

<a name="P2"></a>

## Project 2 - Create Text Difficulty Score

[Project 2](../main/Project%202/Project_2.ipynb)

This project develops a normalized score for both the vocabulary size of text and the long word vocabulary size of text. Using the mean of these normalized scores, I developed a text difficulty score that was tested across multiple reading levels. The project showed the created text difficulty score increased with the reading level. The text was tokenized using Python's NLTK package. Books analyzed were found at: [Project Gutenberg](http://www.gutenberg.org/ebooks/bookshelf/215).

[Back to Top](#BackToTop)

---

<a name="P3"></a>

## Project 3 - Comparing sentence outputs of Stemming and Lemmatizing

[Project 3](../main/Project%203/Project_3.ipynb)

This is a simple project with two parts. Part 1 - Stemmed Book Titles were tested for interpretability with another user. Part 2 - Compare examples in terms of % difference when you stem vs. lemmatize text. The text was tokenized, stemmed, and lemmatized using Python's NLTK package.

[Back to Top](#BackToTop)

---

<a name="P4"></a>

## Project 4 - Compare Part of Speech Taggers on Complex Sentences

[Project 4](../main/Project%204/Project_4.ipynb)

Using Python's NLTK and Flair packages, I compared the accuracy of Part of Speech taggers for each tool on complex sentences. The Flair package proved to be the more accurate tagger in this project.

[Back to Top](#BackToTop)

---

<a name="P5"></a>

## Project 5 - Scrape IMDB Movie Reviews and Extract Noun Phrases

[Project 5](../main/Project%205/Project_5.ipynb)

Using Python's BeautifulSoup package, I scraped 894 links to individual reviews describing 18 movies directly from the advanced search page. Using built-in filters and conditional statements, I ensured each movie met the following criteria:

- Feature Film
- Related to Marvel Comics
- Superhero Movie
- At least 7.0 IMDb user rating (average)
- 2015-2021 Release year or range
- Movie had at least 3000 rating votes to ensure the film was relevant and had sufficient reviews

Next, I pulled the highest and lowest 25 reviews (50 total) for each movie to ensure there was a mix of sentiment. Any review that did not have at least 10 characters was removed due to lack of content.

With all the reviews gathered, I then used BeautifulSoup to scrape 475 of the top actor and character names of the 18 movies being analyzed to identify Proper Nouns that may not be in my lexicon.

Finally, I used Python's Spacy package and the list of top actor and character names to extract all the Noun Phrases from each movie review.

For next steps, this project could be utilized to generate Word Clouds from the reviews for each movie. Another potential project would be to attempt to sort the reviews for each movie with sentiment analysis.

[Back to Top](#BackToTop)

---

<a name="P6"></a>

## Project 6 - Comparing Text Similarity of Book Titles

[Project 6](../main/Project%206/Project_6.ipynb)

Using Python's BeautifulSoup package, I scraped the top 24 book titles displayed. Utilizing Python's Spacy package, I evaluated a pairwise cosine similarity score for every set of Book Titles. For organization, I stored these scores in a square NumPy array where the Book Titles were in the same order for both the rows and columns. I then used SciPy's RankData function to order all the comparisons from most similar to least similar.

In additioon, I queried one Book Title in a Google Search and extracted the text in the 1st and 20th capsule. Using cosine similarity, I showed the higher result had a higher similarity with the queried text. It is worth noting Google uses many factors with ranking search results beyond similarity.

[Back to Top](#BackToTop)

---

<a name="References"></a>

## References

[Project 1](../main/Project%201/Project_1.ipynb)

[Project 2](../main/Project%202/Project_2.ipynb)

[Project 3](../main/Project%203/Project_3.ipynb)

[Project 4](../main/Project%204/Project_4.ipynb)

[Project 5](../main/Project%205/Project_5.ipynb)

[Project 6](../main/Project%206/Project_6.ipynb)


##### Technologies:

Jupyter Notebook

Python 3.7.7

[Back to Top](#BackToTop)
