# Rememberance

Open-Source System designed to mimic functionality of desktop-based AI recall systems. 

## Modular Components 

We'll build out the system fairly modularly so it won't be too difficult to swap out any given compnent (that's the goal at least - I'm writing this before building the system so that's subject to change.) 

It's important to note that we won't necessarily be using SOTA or top-performance ai models as defaults as we want this system to be able to run on your local device. 

I'll probably include options to use cloud-based APIs for certain AI Inference subroutines - tbd. The goal is to run everything locally by default. 

### Database
My personal preference is for a local vector db so we're going to start with that. Will use the vectordb python library ([pypi docs](https://pypi.org/project/vectordb/), [usage docs](https://vectordb.com/))

Other closed-source analogs reportedly use OCR-processed text saved to a local SQLite db. This may be to ensure performance on lower end devices. I'll probably build both of these out more or less in parallel. I want to set up image-based search so I'll use the sqlite db to store the image blobs and OCR'd text. 

### Screenshots
To take screenshots we'll use pillows image grab function. I've used pyautogui in the past and found it easy to use/stable - that's an alternative if you're encountering issues. 

[See here for other options](https://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python).

### OCR
Once we have a screenshot we'll then use OCR to extract image text. 

### QA

