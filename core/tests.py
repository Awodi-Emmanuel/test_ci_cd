from django.test import TestCase, RequestFactory

# Create your tests here.

def test_uses_index_html_template_2(self):
    req_fact = RequestFactory()
    req = req_fact.get('/')
    req.session = {}
    
    res = index(req)
    re = self.assertContains(res, "<title>Your MVP</title>")

    
    print(re)


test_uses_index_html_template_2()