from playwright.sync_api import Page, expect, Route


def test_iphone(page: Page):


    def handle_response(route: Route):
        response = route.fetch()
        text = response.text()

        normal_text = text.replace('\u00a0', " ")
        new_text = normal_text.replace('iPhone 17 Pro', 'яблокофон 17 про')

        route.fulfill(
            response=response,
            body=new_text
        )

    page.route('**/shop/api/digital-mat?path=library/step0_iphone/digitalmat**', handle_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('button', has_text='iPhone 17 Pro').first.click()
    result = page.locator('#rf-digitalmat-overlay-label-0').first
    expect(result).to_have_text('яблокофон 17 про')
