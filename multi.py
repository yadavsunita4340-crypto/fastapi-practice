from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True

@app.get("/")
def read_root():
    return {"Hello": "my world\\\\"}

my_posts=[{"title 1":"beaches","content":"florida", "id" :1},{"title 2":"food","content":"pizza","id": 2 }]

@app.get("/posts")
def get_posts():
    return {"data" :my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    return {"data":post_dict}
    
def find_posts(id):
        for p in my_posts:
            if p["id"]==id:
                return p

@app.get("/posts/{id}")
def get_post(id: int):
    post=find_posts(id)
    return{"post_detail": post}


