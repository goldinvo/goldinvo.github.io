# goldinvo.com
My personal website 

## Usage of Layouts
- **`default`** includes *`head`*: for webpages where you don't want the sidebar
    - include scripts using `script: [path]` 
- **`page`** extends **`default`** includes *sidebar*: Contains the sidebar and a reserved space for content.
    - Required properties:
        - `title`:
- **`short-post`** extends **`page`**: For posts with a one/a few pictures and a short description/caption
    - Required properties:
        - `images`: array of image paths to feature in gallery reel
        - `featured-image`: the image to be featured on post listings
- **`long-post`** extends **`page`**:
    - Required properties:
        -`featured-image`
- both short-post and long-post posts should be named `YYYY-MM-DD-TITLE-MORETITLE.md`. The title and date properties from this file name are used in the website.

## Some categories (not really used, for now)
crochet, knitting, tatting, bobbin-lace, weaving, misc

Run using `jekyll serve`




