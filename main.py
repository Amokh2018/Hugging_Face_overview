from transformers import pipeline

summerize = pipeline("summerization", model="t5-small", tokenizer="t5-small", truncation = True, framework="tf")
