# onco-ext
Generating highly realistic synthetic cancer data, and fine-tuning large language models (LLM) on synthetic data, to extract detailed cancer timelines.

## Introduction
More than 80% of clinical information is found in unstructured data. This number is arguably higher for cancer data, where only high level information is coded, and key information about symptoms, cancer subtypes and biomarkers, and treatment response and endpoints, are typically found in cancer clinic letters. Accurate extraction and structuring of this data at scale - over tens to hundreds of millions of documents for a cancer centre - are an incredibly rich source of retrospective Real-World Data.

Given the semantic complexity and range of information found in unstructured sources, large language models with specific fine-tuning, are likely to outperform traditional models (e.g. BERT-based) in tasks such as diverse information extraction from highly complex unstructured data. However, there are a number of limitations:
(1) Availability of local high compute environments for fine-tuning even 8B parameter LLMs;
(2) Difficulty in egressing large quantities of raw unstructured text to cloud environemnts, due to privacy concerns;
(3) Variability, including over time, in semantic structures, can lead to new edge cases, without an easy way to update models (due to (1) and (2)).

At the same time, LLMs can express and incredible range of semantic richness. In building this repository, we hypothesise that enterprise LLMs can create high fidelity clinical documentation without fine-tuning, through 'many-shot' prompting with rich context only. We secondly hypothesise that 8B parameter models, which are deployable in most local environments that have a GPU, can be fine-tuned on synthetic data samples to comprehensively and accurately extract structured data from real clinic letters.

## Project Structure
This repository, for now, has two elements:
* ```/synthdatagen```: Synthetic data generation is performed using prompting techniques and carefully Domain Expert created examples, via commercial, long context, LLM APIs (we find Claude Sonnet 3.5 is the highest performing)
* ```finetune```: Scripts for training data creation (.jsonl). Fine-tuning and test deployments are presently performed through the [Openpipe API](https://openpipe.ai/).

Est. total cost to generate synthetic data and train a high performing llama 3.1 8B parameter model on 1000 samples = $150

<br>
<a href="https://www.aicentre.co.uk/"><img src="https://openhealthhub.org/uploads/default/original/1X/3494038bee19363220a0f498ea780ce17a202e4d.gif" alt="London AI Centre" title="" height="70" /></a>