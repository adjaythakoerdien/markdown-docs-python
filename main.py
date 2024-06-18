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
    for _, _, files in os.walk("md/", topdown=True):
        links = [f for f in files if ".md" in f]
    links = sorted(links)
    return links


def add_links(text, path):
    links = list_dir()
    html_links = ""
    for link in links:
        link_string = link.replace(".md", "")
        html_links += f"<a href='{path}{link}'>{link_string}</a> <span style='color: #4ade80;'>|</span> "
    html_links += "<br><hr>\n\n"
    text = html_links + text
    return text


def process_markdown(text: str):
    html_links = ""

    text = markdown.markdown(text, extensions=["fenced_code", "codehilite"])
    text = text.replace("<a", "<a target='_blank'")
    text = text.replace("<h1>", "<h1><span class='h1'># </span>")
    text = text.replace("<h2>", "<h2><span class='h1'>## </span>")
    # text = text.replace("<h3>", "<h3><span class='h1'>### </span>")
    text = text.replace(
        "<blockquote>", "<div class='square-brackets-quote'><blockquote>"
    )
    text = text.replace("</blockquote>", "</div></blockquote>")

    return text


@app.get("/view/{filename}")
async def root(request: Request, filename: str):
    with open(f"md/{filename}", "r", encoding="utf8") as infile:
        text = infile.read()

    text = process_markdown(text)
    text = add_links(text, "")
    return templates.TemplateResponse(
        request=request,
        name="first.html",
        context={"body": text},
        media_type="text/html",
    )


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    with open("md/_home.md", "r", encoding="utf8") as infile:
        body = infile.read()

    body = process_markdown(body)
    body = add_links(body, "/view/")
    return templates.TemplateResponse(
        request=request,
        name="first.html",
        context={"body": body},
        media_type="text/html",
    )
