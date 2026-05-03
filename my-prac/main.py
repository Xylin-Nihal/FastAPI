from fastapi import FastAPI, requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app=FastAPI()
templates = Jinja2Templates(directory="templates")
post_data = {
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "author": "John Doe"
}
@app.get("/api", response_class=HTMLResponse)
def home():
    return f"<h1>Welcome to FastAPI!</h1><p>This is a simple HTML response.</p>"
@app.get("/template")
def template(request: requests.Request):
    return templates.TemplateResponse(request, "home.html", {"title": "Home Page", "post": post_data})