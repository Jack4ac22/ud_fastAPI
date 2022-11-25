from enum import Enum
from fastapi import APIRouter, status, Response, Depends
from router.blog_post import required_functionality
from typing import Optional


router = APIRouter(
    prefix="/blog",
    tags=["blog"])


@router.get(
    '/all',
    summary="retrive all blogs",
    description="a test api call that simulate fetching all blogs",
    response_description="The list of all avaliable blogs."
)
def get_all_blog(page=1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"all {page_size} on blog {page}", 'req': req_parameter}


@router.get("/{id}/comments/{comment_id}",
            tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulate retriving a comment of a blog
    - ** id ** mandatory path parameter
    - ** comment_id ** mandatory path parameter
    - ** valid ** optional path parameter
    - ** username ** optional path parameter
    """
    return {"message": f"blog id is: {id}, comment id is: {comment_id}, valid: {valid}, username: {username}."}


# @router.get('/all')
# def get_all_blog():
#     return {'message': 'all the blog posts'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'blog type is: {type}'}


@router.get('/{id}',
            status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 6:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} was not found."}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'blog ID is: {id}.'}
