import json
import os
from sentence_transformers import SentenceTransformer, util
from re import U
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
import torch

import numpy as np
import pandas as pd
import torch
from models import Article
app = FastAPI()


#First, we load the papers dataset (with title and abstract information)
dataset_file = 'emnlp2016-2018.json'

if not os.path.exists(dataset_file):
  util.http_get("https://sbert.net/datasets/emnlp2016-2018.json", dataset_file)

with open(dataset_file) as fIn:
  papers = json.load(fIn)
  print(papers[0])
  for paper in papers:
    paper.pop('url')

 # print(papers[0])

print(len(papers), "papers loaded")
#We then load the allenai-specter model with SentenceTransformers
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

#To encode the papers, we must combine the title and the abstracts to a single string
paper_texts = [paper['title'] + '[SEP]' + paper['abstract'] for paper in papers]

#Compute embeddings for all papers
corpus_embeddings = model.encode(paper_texts, convert_to_tensor=True)
#torch.save(corpus_embeddings, 'tensor.pt')

torch.load('tensor.pt')
#We define a function, given title & abstract, searches our corpus for relevant (similar) papers
def search_papers(query):
  query_embedding = model.encode(query, convert_to_tensor=True)

  search_hits = util.semantic_search(query_embedding, corpus_embeddings)
  search_hits = search_hits[0]  #Get the hits for the first query
  cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]

  print("Paper:", query)
  print("Most similar papers:")
  related_papers: List[Article]=[]

  for hit in search_hits:
    related_paper = papers[hit['corpus_id']]
    related_paper['score']=hit['score']
    
    related_papers.append(related_paper)
    print("{:.2f}\t{}\t{} {}".format(hit['score'], related_paper['title'], related_paper['abstract'], related_paper['year']))
  return related_papers


def search_query(query):
   sim=[]
   embedder = SentenceTransformer('all-MiniLM-L6-v2')
   # Corpus with example sentences
   with open ('D:/fastapi/streamlit/data.txt', "r") as myfile:
    data = myfile.read().splitlines()
   corpus_embeddings = embedder.encode(data, convert_to_tensor=True)
   top_k = min(5, len(data))
   query_embedding = embedder.encode(query, convert_to_tensor=True)
   cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
   top_results = torch.topk(cos_scores, k=top_k)
   print("\n\n======================\n\n")
   print("Query:", query)
   print("\nTop 5 most similar sentences in corpus:")
   for score, idx in zip(top_results[0], top_results[1]):
    print(data[idx], "(Score: {:.4f})".format(score))
    if(score<1):
      sim.append(data[idx])
  
   with  open("D:/fastapi/streamlit/data.txt", "a+") as file:
            content = query+" \n"
            file.write(content)
            file.close()
   return sim
#multi-qa-MiniLM-L6-cos-v1
@app.get("/")
async def root():
    
    return {"message": "Hello World"}

@app.get("/api/articles/{query}")
async def fetch_articles(query):
    q=query
    print(q)
    return search_papers(q);


@app.get("/api/queries/{query}")
async def fetch_queries(query):
  q=query
  return search_query(q);


