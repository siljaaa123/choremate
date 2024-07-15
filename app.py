from litestar import Litestar, get

# get request to root URL
@get("/")
# asynchrous method allows you to perform non-blocking operations,
# meaning that the fn can execute other tasks while waiting for some operations to cpmplete
async def index() -> str:
    return 
