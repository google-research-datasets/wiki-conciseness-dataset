# The wiki-conciseness dataset

This is a manually curated evaluation set in English for concise rewrites of
20000 Wikipedia sentences. *Concise-Lite* (2-way annotated) annotators were
asked to make minimal changes to the original sentence, whereas *Concise-Full*
(5-way annotated) annotators were given the option to make larger rewrites. More
details are in [our paper](https://www.todo.com).

## Evaluation
The outputs of our best systems in the paper are in the `outputs/`
directory. To compute F0.5 scores with
[ERRANT](https://github.com/chrisjbryant/errant), follow the
[instructions](https://github.com/chrisjbryant/errant#installation) to
install ERRANT and spaCy. Then, use `tokenize_with_spacy.py` to spaCy-tokenize
the input and output sentences, and run `errant_parallel` to generate the M2
file:

```
cut -f1 concise_full.tsv | python3 tokenize_with_spacy.py > tmp.src.spacy.txt
cat outputs/transformer_rt.txt | python3 tokenize_with_spacy.py > tmp.trg.spacy.txt
errant_parallel -orig tmp.src.spacy.txt -cor tmp.trg.spacy.txt -out tmp.m2
```

The scores from Table 6 in [the paper](https://www.todo.com) can be reproduced by
comparing `tmp.m2` to `concise_lite.m2` or `concise_full.m2`:

```
errant_compare -hyp tmp.m2 -ref concise_lite.m2

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
894     5695    3305    0.1357  0.2129  0.1463
==============================================
```

```
errant_compare -hyp tmp.m2 -ref concise_full.m2

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
1390    5199    4061    0.211   0.255   0.2185
==============================================
```


## License
This dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).


## BibTeX
If you found this dataset useful, please cite our [paper](https://www.todo.com/).

```
@inproceedings{wiki-conciseness,
    title = "Conciseness: An Overlooked Language Task",
    author = "Stahlberg, Felix and Kumar, Aashish and Alberti, Chris and Kumar, Shankar",
    booktitle = "Proceedings of the 1st EMNLP Workshop on Text Simplification, Accessibility, and Readability (TSAR)",
    month = dec,
    year = "2022",
    publisher = "Association for Computational Linguistics",
}
```

**This is not an officially supported Google product.**
