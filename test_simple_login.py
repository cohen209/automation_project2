def test_simple_login(page):
    page.goto('BASE')
    page.fill("#username", 'ADMIN')
    page.fill("#password", 'PASSWORD')
    page.get_by_role("button", name="Login").click()
    assert page.locator(".post-title").text_content() == "Logged In Successfully"
   
