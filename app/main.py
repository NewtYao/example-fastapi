from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)
origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"Hello": "Welcome to my api!!!!!"}

#testing
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):

#     posts = db.query(models.Post).all()
#     return {"data": posts}

# @app.get("/posts", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     # cursor.execute(""" SELECT * FROM posts """)
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).all()
#     return posts

# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(post.title, post.content, post.published))

#     # new_post = cursor.fetchone()
#     # conn.commit() # save the post to database
    
#     new_post = models.Post(**post.model_dump())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post

# @app.get("/posts/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     # cursor.execute(""" SELECT * from posts WHERE id = %s """, (str(id),))
#     # post = cursor.fetchone()
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail = f"post with id:{id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id:{id} was not found"}
#     return post

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     # deleting post
#     # find the index in the array that has required ID
#     # my_post.pop(index)
#     # cursor.execute(""" DELETE FROM posts WHERE id = %s returning *""",(str(id),) )
#     # deleted_post = cursor.fetchone()
#     # conn.commit()
#     post = db.query(models.Post).filter(models.Post.id == id)
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id:{id} does not exist")
#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
#     # updated_post = cursor.fetchone()
#     # conn.commit()
#     post_query = db.query(models.Post).filter(models.Post.id == id)

#     post = post_query.first()

#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail = f"post with id:{id} does not exist")
    
#     post_query.update(updated_post.model_dump(), synchronize_session=False)

#     db.commit()
    
#     return  post_query.first()


# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     # hash the password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# @app.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"User with id: {id} does not exist")
    
#     return user