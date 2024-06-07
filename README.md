# Rememberance

Open-Source System designed to mimic functionality of desktop-based AI recall systems. 

## Modular Components 

We'll build out the system fairly modularly so it won't be too difficult to swap out any given compnent (that's the goal at least - I'm writing this before building the system so that's subject to change.) 

It's important to note that we won't necessarily be using SOTA or top-performance ai models as defaults as we want this system to be able to run on your local device. I'll try to use standardized transformers pipelines where possible, so changing the model should be as simple as changing the model source string. ~~For this reason I might avoid using model-specific libraries (e.g. [paddleOCR](https://pypi.org/project/paddleocr/) or [pytesseract](https://pypi.org/project/pytesseract/)) even if they have a relatively easy and accessible library - tbd~~. Screw that just going to use PaddleOCR for OCR as hf hub seems to be relatively deficicient when it comes to OCR models while paddleOCR is relatively lightweight and well-maintained. 

I'll probably include options to use cloud-based APIs for certain AI Inference subroutines - tbd. The goal is to run everything locally by default. 

### Database
My personal preference is for a local vector db so we're going to start with that. Will use the vectordb python library ([pypi docs](https://pypi.org/project/vectordb/), [usage docs](https://vectordb.com/)). VectorDB requires tons on installs/space for large libraries so may just use sqlite depends how much those libraries overlap with libs we need for other modules.

Other closed-source analogs reportedly use OCR-processed text saved to a local SQLite db. This may be to ensure performance on lower end devices. I'll probably build both of these out more or less in parallel. I want to set up image-based search so I'll use the sqlite db to store the image blobs and OCR'd text. 

### Screenshots
To take screenshots we'll use pillows image grab function. I've used pyautogui in the past and found it easy to use/stable - that's an alternative if you're encountering issues. 

[See here for other options](https://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python).

### OCR
Once we have a screenshot we'll then use OCR to extract image text. We'll then push this OCR'd text to our database. We'll use PaddleOCR as it is relatively lightweight, well-maintained and multilingual. 

I may include a pytesseract option if you want an even lighterweight OCR system or you're concerned about paddleOCR. Trade off is poorer performance. 

! HTML read probably superior for web usage but that requires much more browser integration (native browser integration probably ideal)

### Classification
Not totally necessary may skip for init build. If skipped we'll use the class "placeholder" as a placeholder for sql writes/reads. Mainly so we have a valid string here.  

May make this soemthing we can toggle on/off. Once we have the OCR'd text we'll classify that text using a zeroshot classifier. We use a zeroshot classifier to retain flexibility in classes that the sytem can accomodate. For our purposes I'll probably use bart-large-mnli classifier since I used this fairly recently ([github](https://github.com/GeorgeDavila/cog-bart-large-mnli), [replicate api](https://replicate.com/georgedavila/bart-large-mnli-classifier)). This is a fairly robust classification model so it should suffice for most use cases. Here we'll be using a transformers classification pipeline so you should be able to switch your model fairly easily.

For our default pipeline we'll use the classes "work, study, shopping, other". We will store the classes in predominant order. All classes must add up to 100% using this model our current working assumption is that the "other" class should take over when none of the main classes are likely. Of course we're working with OCR'd screenshots so its hard to say if this will hold up when tested, for instance ads might cause the "shopping" label to be overepresented. We'll adjust this after testing on real examples. 

### QA
Finally we need to let users query the DB for answers. VectorDB can be queried with a text prompt. For querying the the SQLite DB I'm not yet certain whether I'll use a table-QA model a la [tableqa-tapas-large](https://replicate.com/georgedavila/tableqa-tapas-large) or some alternative method. 

May later incorporate visual QA - remains to be seen.

## Resources & References

- https://sqlitebrowser.org/

- https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/
- https://www.geeksforgeeks.org/python-sqlite-working-with-date-and-datetime/#
- https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

