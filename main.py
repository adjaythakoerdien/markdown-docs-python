import os.path
import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
import markdown

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def list_dir():
    links = []
    for root, dirs, files in os.walk("md/", topdown=True):
        print(root, dirs, files)
        links = files
    return links


def process_markdown(text: str):
    links = list_dir()
    html_links = ""
    for link in links:
        html_links += f"<p><a href='{link}'>{link}</a></p>"
    text = html_links + text
    text = markdown.markdown(text)
    text = text.replace("<h1>", "<h1><span style='color: red;'># </span>")
    text = text.replace(
        "<blockquote>", "<div class='square-brackets-quote'><blockquote>"
    )
    text = text.replace("</blockquote>", "</div></blockquote>")
    return text


@app.get("/view/{filename}")
async def root(request: Request, filename: str):
    print("[FILENAME] - ", filename)
    with open(f"md/{filename}", "r", encoding="utf8") as infile:
        text = infile.read()

    text = process_markdown(text)
    print(text)
    return templates.TemplateResponse(
        request=request,
        name="first.html",
        context={"body": text},
        media_type="text/html",
    )


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    body = ""
    links = list_dir()
    html_links = ""
    for link in links:
        html_links += f"<p><a href='view/{link}'>{link}</a></p>"
    body = html_links + body
    body = markdown.markdown(body)
    body = body.replace("<h1>", "<h1><span style='color: red;'># </span>")
    body = body.replace(
        "<blockquote>", "<div class='square-brackets-quote'><blockquote>"
    )
    body = body.replace("</blockquote>", "</div></blockquote>")
    print(body)
    return templates.TemplateResponse(
        request=request,
        name="first.html",
        context={"body": body},
        media_type="text/html",
    )
