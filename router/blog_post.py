from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List, Dict, Tuple

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    aliase: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    tags: List[str] = []
    metadata: Dict[str, str] = {'key': 'value'}
    # we can use costumed model that has multitypes by creating a class that has those types as properties then use the model
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {'id': id,
            'data': blog,
            'version': version}


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_title: str = Query(None,
                                              title='Id of the comment',
                                              description='description of the comment id',
                                              alias='commentTitled',
                                              deprecated=True),
                   content: str = Body(...,  # ... (((or))) Ellipsis: make it mandatory
                                       min_length=10,
                                       max_length=30,
                                       regex='^[a-z\s]*$'),
                   v: Optional[List[str]] = Query(['1.0', '1.1', '1.3']),
                   comment_id: int = Path(None, le=9)
                   ):
    return {'blog': blog,
            'id': id,
            'comment_id': comment_id,
            'content': content,
            'version': v}
