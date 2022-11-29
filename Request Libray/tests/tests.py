from scrape import status_code, count_items

def test_status_code():
    status, file = status_code('https://github.com/topic/python') 
    assert status == 200 and file

def test_item():
    assert count_items() == 180
    
