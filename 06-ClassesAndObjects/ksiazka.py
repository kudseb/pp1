class ebook(object):
    def __init__(s,name,author,no_pages):
        s.name=name
        s.author=author
        s.no_pages=no_pages
        s.cur_page=0
        s.is_open=False
    def __str__(s):
        return (f'T:{s.name} A:{s.author} No P:{s.no_pages} C P:{s.cur_page}')
    def open_book(s):
        s.is_open=True
    def close_book(s):
        s.is_open=False
    def next_page(s):
        if s.is_open:
            if s.cur_page<s.no_pages:
                s.cur_page+1
        else:
            print('Nie da rady, ksiazka zamknieta')
    def prev_page(s):
        if s.is_open:
            if s.cur_page>0:
                s.cur_page-1
        else:
            print('Nie da rady, ksiazka zamknieta')
