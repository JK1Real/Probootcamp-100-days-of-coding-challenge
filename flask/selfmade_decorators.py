
# These are decorators to use 
def make_bold(function):
    def wrapped():
        text = function()
        html=f"<b>{text}</b>"
        return html
    return wrapped


def make_emphasis(function):
    def wrapped():
        text = function()
        html=f"<em>{text}</em>"
        return html
    return wrapped

def make_underline(function):
    def wrapped():
        text = function()
        html=f"<u>{text}</u>"
        return html
    return wrapped