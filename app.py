from bottle import *
import re

@route('/hello/:name')
def index(name='World'):
    response.set_cookie('current_u4ser', name, path='/')
    if request.get_cookie(safe_cookie(name)):
        return '<b>Hello <i>again</i> %s</b>' % name
    else:
        response.set_cookie(safe_cookie(name), 'yes')
        return '<b>Hello %s!</b>' % name

def safe_cookie(c):
    return re.sub(' ', '', c)
    
@route('/hello/name')
def index():
    name = request.cookies.get('current_user', 'friend')
    return 'It\'s %s, right?' % name
    
@route('/counter')
def counter():
    count = int( request.cookies.get('counter', '0') )
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count

@route('/maths/:a/:b')
def index(a=0,b=0):
    if not (is_int(a) and is_int(b)):
        return 'You should check those numbers...'
    result = str(int(a)**int(b))
    name = request.cookies.get('current_user', 'my friend')
    print name
    return 'The answer, %(name)s, is %(result)s' % {'name':name, 'result':result}

def is_int(n):
    return re.match('\d+', n)


run(host='localhost', port=8080, reloader=True)
