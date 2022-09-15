# Natural-Language-Query-Search-Engine
<h1>Description Of Project</h1>
The user enters their query in natural human language. This query is converted to vector
embedding and stored.
The database we are using consists of collection of research papers. It has the title, abstract
,URL, venue and its year of publishing.
Since we only need title, abstract and year of publishing we remove the other two features.
We concatenate the title, abstract and year of publishing for each tuple in the dataset .This
is converted into vector embedding and the query embedding is compared to each paper
embedding and those with top 5 high similarity scores are displayed as search results.
Another facet of this project is every query we enter is stored in a separate place. We
convert these previously entered queries into vector embeddings. These are compared to
the query user has entered at the present and those with top 5 similarity scores are
displayed as a suggestion to the user.
<br><br>
Natural language search allows users to speak or type into a device using their everyday
language rather than keywords. Users can use full sentences in their native language as if
they are speaking to another human, leaving the computer to transform the query into
something it can understand. Thanks to Google and other search engines, users have
become accustomed to using keyword searches. But keyword searches are not an intuitive
way for users to ask questions, and users are actually pretty bad at using them to find what
they need. They force users to strip out question words and other connective language to
form literal text strings that the search engine can use to query data. It also may require
effort on the part of the business to mine intent from keyword searches.
With the rise of digital voice assistants such as Siri and Alexa, however, people are becoming
accustomed to having conversations with their devices in full and grammatically complex
sentences. The effect is that many users now form queries like questions over different devices and
platforms. Users are becoming accustomed to using natural language to get information and expect
fast results. Therefore, it is essential that search systems of all types can begin to accept natural
language searches.
This is what we will extend as the scope of this project. To build a natural query search engine that
fetches top five related research articles on the basis of similarity scores of the query with each
article.
