# Distributed Caesar Cipher with Python PARCS

This project implements parallel encryption using the classical Caesar Cipher algorithm, executed on a distributed MapReduce-style infrastructure built with Python PARCS and deployed on Google Cloud Platform.

## Features
- Distributed execution using PARCS master–worker architecture  
- Parallel text processing (Map) and result aggregation (Reduce)  
- Caesar Cipher encryption with configurable shift  
- Scalable execution using 1–3+ workers  
- Performance measurement across different numbers of workers  
- Google Cloud monitoring analysis: CPU, network, disk

## Technologies
- Python 3  
- Pyro4 / PARCS  
- Google Cloud Compute Engine  
- MapReduce paradigm  

## Structure
- `solution.py` — main distributed algorithm implementation  
- `input.txt` — large text used for testing  
- `output.txt` — final encrypted output  

## How it works
1. Master divides the input text into equal parts  
2. Each worker encrypts its fragment using Caesar Cipher  
3. Master collects results and writes output file  
4. Cloud monitoring tracks performance across VMs  

Lab work for Distributed and Parallel Programming course.
