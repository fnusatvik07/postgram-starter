# Demo posts

24 images to post live in class. One folder per image, each holding:

- `image.jpg` : the photo (themed, so you can see what you are posting)
- `caption.txt` : the caption on the first line, then the author and the `image_url` to post

```
demo-posts/
├── 01-coffee/      image.jpg + caption.txt
├── 02-mountain/    image.jpg + caption.txt
├── 03-dog/         ...
└── 24-cafe/
```

## Test them (post into a running Postgram)

The app stores an `image_url` (it does not upload files), so `post.py` reads each folder's
`caption.txt` and sends the caption, author, and image URL to the API.

```bash
# post one folder
python3 post.py 05-beach

# post all 24
python3 post.py all
```

If the backend runs on a port other than 8000 (8000 is often taken):

```bash
POSTGRAM_API=http://localhost:8001/api  python3 post.py all
```

## Test one by hand

Open any `NN-name/caption.txt`, copy the caption and `image_url`, and use the app UI or curl:

```bash
curl -X POST http://localhost:8000/api/posts \
  -H 'Content-Type: application/json' \
  -d '{"image_url":"<from caption.txt>","caption":"<first line>","author":"<from caption.txt>"}'
```

Note: images are from loremflickr (Creative Commons photos from Flickr) and render from the URL in
each `caption.txt`, so posting needs an internet connection. The local `image.jpg` files let you
preview and pick without loading anything.
