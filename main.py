from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

posts = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is the content of the first post.",
        "date_posted": datetime(2023, 10, 1, 12, 0, 0),
        "image_file": "default.png"
    },
    {
        "id": 2,
        "author": "Jane Smith",
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "date_posted": datetime(2023, 10, 2, 14, 30, 0),
        "image_file": "default.png"
    }
]




app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, 'title':'Home'})    


@app.get('/posts')
def get_posts():
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")